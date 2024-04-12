"""
Run the following command to install dependencies:
pip install matplotlib pandas requests
"""

from datetime import datetime, timedelta
import json
from itertools import product
from pprint import pprint
from pathlib import Path
from collections import defaultdict
from operator import itemgetter
from multiprocessing import Pool

import matplotlib.pyplot as plt
import pandas as pd

import constants
import data_processing
import data_io


def setup_padnas_printing() -> None:
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_colwidth", None)
    pd.set_option("display.width", None)


def download_data(threads: int) -> None:
    fund_data_path = constants.DATA_DIR / "funds.json"

    if not fund_data_path.exists():
        data_io.download_funds(fund_data_path)

    raw_fund_data = pd.DataFrame(data_io.load_fund_data(fund_data_path))
    filtered_fund_data = data_processing.filter_fund_data(
        raw_fund_data,
        ["Isin", "SecId", "ReturnM12"]
    )

    download_dir = constants.FUND_TIMESERIES_DIR / "all"

    if download_dir.exists():
        return

    download_dir.mkdir(parents=True)

    args = [
        (download_dir, fund["SecId"], fund["Isin"])
        for _, fund in
        filtered_fund_data.iterrows()
    ]

    with Pool(threads) as p:
        p.starmap(data_io.download_timeseries, args)


def process_multiple_timeseries(timeseries_dir: Path, baseline: datetime, pre_month_deltas: tuple[int],
                                post_month_deltas: tuple[int], offset: timedelta = timedelta()) -> dict[
    tuple[int, int], tuple[float, float]]:
    fund_data = {}
    for i, path in enumerate(timeseries_dir.iterdir()):
        if not i % 1000:
            print(i, offset)

        returns = data_processing.returns_from_baseline(
            data_io.load_timeseries(path),
            baseline + offset,
            pre_month_deltas + post_month_deltas
        )
        if returns:
            fund_data[path] = returns

    if not fund_data:
        print("NO FUND DATA")

    df = pd.DataFrame.from_dict(fund_data, orient="index")

    result = {}
    for pre_month_delta in pre_month_deltas:
        top = data_processing.top_n(df, pre_month_delta, 100)

        for post_month_delta in post_month_deltas:
            result[(pre_month_delta, post_month_delta)] = (top[post_month_delta].mean(), top[post_month_delta].std())

    return result


def main() -> None:
    setup_padnas_printing()

    threads = 24

    download_data(threads)

    timeseries_dir = constants.FUND_TIMESERIES_DIR / "all"

    baseline = datetime(2023, 1, 1)
    pre_month_deltas = (-1, -3, -6, -12, -24, -36, -60)
    post_month_deltas = (1, 3, 6, 12)

    roll_months = 240

    args = [
        (
            timeseries_dir,
            baseline,
            pre_month_deltas,
            post_month_deltas,
            timedelta(milliseconds=constants.MONTH_MS * -i)
        )
        for i in range(roll_months)
    ]

    with Pool(threads) as p:
        results: list[dict[tuple[int, int], tuple[float, float]]] = p.starmap(process_multiple_timeseries, args)

    final_result = {
        key: (
            sum(result[key][0] for result in results) / len(results),
            sum(result[key][1] for result in results) / len(results)
        )
        for key in results[0].keys()
    }

    pprint(final_result)


if __name__ == "__main__":
    main()
