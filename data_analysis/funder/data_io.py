from pathlib import Path
import time
from typing import Optional
import json

import morningstar


def download_funds(path: Path) -> None:
    response = morningstar.get_funds()
    assert response.status_code == 200

    with open(path, "wb") as f:
        f.write(response.content)


def download_timeseries(download_dir: Path, sec_id: str, isin: Optional[str] = None,
                        retry_interval_seconds: int = 300) -> None:
    path = download_dir / f"{sec_id}{f"-{isin}" if isin else ""}.json"
    response = morningstar.get_time_series(sec_id)

    while response.status_code in (403, 429):
        print(f"Could not download {sec_id} due to rate limit. Trying again in {retry_interval_seconds} seconds.")
        time.sleep(retry_interval_seconds)
        response = morningstar.get_time_series(sec_id)

    if response.status_code != 200:
        print(f"Could not download {sec_id}, error code: {response.status_code}. Skipping")
        return

    print(f"Saving timeseries for {sec_id} to {path}")
    with open(path, "wb") as f:
        f.write(response.content)


def load_fund_data(path: Path) -> dict:
    with open(path, "rb") as f:
        fund = json.load(f)["rows"]

    return fund


def load_timeseries(path: Path) -> list:
    with open(path, "rb") as f:
        timeseries = json.load(f)

    return timeseries
