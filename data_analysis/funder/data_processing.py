import bisect
from datetime import datetime, timedelta
import math
from typing import Optional, Iterable
from operator import itemgetter

import pandas as pd

import constants


def top_n(dataframe: pd.DataFrame, column: str, n: int, invert: bool = False) -> pd.DataFrame:
    return dataframe.sort_values(column, ascending=invert).head(n)


def filter_fund_data(dataframe: pd.DataFrame, columns: list[str], return_limit: int = 100) -> pd.DataFrame:
    dataframe = dataframe[columns]
    dataframe = dataframe.dropna()
    dataframe = dataframe[dataframe["ReturnM12"] <= return_limit]
    dataframe = dataframe[dataframe["ReturnM12"] >= -return_limit]

    return dataframe


def average_annual_growth(start_time_ms: int, end_time_ms: int, start_value: float, end_value: float) -> float:
    return math.e ** ((math.log(end_value / start_value)) / ((end_time_ms - start_time_ms) / YEAR_MS))


def returns(timeseries: list[list[int, int]], start_i: int, end_i: int) -> Optional[
    tuple[float, float, float]]:
    start_timestamp_ms, start_price = timeseries[start_i]
    end_timestamp_ms, end_price = timeseries[end_i]

    return (
        end_price - start_price,
        end_price / start_price,
        average_annual_growth(
            start_timestamp_ms,
            end_timestamp_ms,
            start_price,
            end_price
        )
    )


def closest_datapoint(timeseries: list[list[int, float]], date: datetime, threshold: timedelta = timedelta(weeks=1)) -> Optional[tuple[int, float]]:
    if not timeseries:
        return

    date_timestamp_ms = date.timestamp() * 1000
    threshold_ms = threshold.total_seconds() * 1000

    i_right = min(bisect.bisect_right(timeseries, date_timestamp_ms, key=itemgetter(0)), len(timeseries) - 1)
    i_left = min(bisect.bisect_left(timeseries, date_timestamp_ms, key=itemgetter(0)), len(timeseries) - 1)

    timestamp, price = min(timeseries[i_right], timeseries[i_left], key=lambda t: abs(t[0] - threshold_ms))

    if abs(timestamp - date_timestamp_ms) <= threshold_ms:
        return (timestamp, price)


def returns_from_baseline(timeseries: list[list[int, float]], baseline: datetime, month_deltas: Iterable[int]) -> dict[int, float]:
    baseline_datapoint = closest_datapoint(timeseries, baseline)
    if baseline_datapoint is None:
        return {}
    baseline_timestamp, baseline_price = baseline_datapoint

    datapoints = {}
    for month_delta in month_deltas:
        datapoint = closest_datapoint(timeseries, baseline + timedelta(milliseconds=month_delta * constants.MONTH_MS))
        if datapoint is None:
            return {}
        timestamp, price = datapoint

        datapoints[month_delta] = (baseline_price / price) if baseline_timestamp >= timestamp else (
                price / baseline_price)

    return datapoints
