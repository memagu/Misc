import os
from datetime import datetime, timedelta
from functools import partial
import json
from multiprocessing import Manager, Pool
from os import getenv
from typing import Any, Iterable, Optional

from dotenv import load_dotenv
import requests

from util import datetime_to_utc_iso, DATA_DIR, QUEUE_GROUPS_PATH, QUEUES_PATH, CALLS_PATH


def login(username: str, password: str) -> tuple[int, str]:
    data = requests.post(
        "https://app2.zissoninteract.com/web-api/v1.0/login/create-session",
        json={
            "username": username,
            "password": password
        }
    ).json()

    return data["session"]["loginId"], data["bearer"]


def get_history(authorization_token: str, from_date: datetime, to_date: datetime) -> Optional[list[dict[str, Any]]]:
    return requests.post(
        "https://app2.zissoninteract.com/web-api/v1.0/queue-log/search",
        json={
            "fromDate": datetime_to_utc_iso(from_date),
            "toDate": datetime_to_utc_iso(to_date)
        },
        headers={
            "Authorization": f"Bearer {authorization_token}"
        }
    ).json()


def get_call(authorization_token: str, call_session_id: str) -> list[dict]:
    return requests.get(
        f"https://app2.zissoninteract.com/web-api/v3.0/session-data/{call_session_id}/call-history-details",
        headers={
            "Authorization": f"Bearer {authorization_token}"
        }
    ).json()


def retrieve_queue_name(authorization_token: str, queue_id: int, history: list[dict[str, Any]]) -> tuple[
    int, Optional[str]]:
    for entry in history:
        if entry["queueId"] != queue_id:
            continue

        call = get_call(authorization_token, entry["callSessionId"])
        if not call:
            continue

        queue_join_event = next((event for event in call if event["eventType"] == "QueueJoin"), None)
        if queue_join_event is None:
            continue

        return queue_id, queue_join_event["queueDesc"]

    return queue_id, None


def retrieve_queue_names(authorization_token: str, queue_ids: Iterable[int], history: list[dict[str, Any]]) -> dict[
    int, Optional[str]]:
    with Manager() as m:
        shared_history = m.list(history)
        with Pool(os.cpu_count()) as p:
            func = partial(retrieve_queue_name, authorization_token, history=shared_history)
            result = p.map(func, queue_ids)

    return dict(result)


def main():
    load_dotenv()

    username = getenv("ZISSON_USERNAME")
    password = getenv("ZISSON_PASSWORD")

    login_id, token = login(username, password)

    now = datetime.today()
    history = get_history(
        token,
        now - timedelta(days=91),
        now
    )

    if not DATA_DIR.exists():
        DATA_DIR.mkdir(parents=True)

    queue_groups = json.loads(QUEUE_GROUPS_PATH.read_text())
    onitio_queues = set(queue_groups["onitio"])
    fmcg_queues = set(queue_groups["fmcg"])

    if QUEUES_PATH.exists():
        queues = {int(key): value for key, value in json.loads(QUEUES_PATH.read_text()).items()}
    else:
        queues = retrieve_queue_names(token, onitio_queues, history)
        QUEUES_PATH.write_text(json.dumps(queues))

    CALLS_PATH.write_text(json.dumps(
        [
            {"datetime": entry["joinTimestamp"], "queue": queues[entry["queueId"]]}
            for entry in history
            if entry["queueId"] in fmcg_queues and entry["firstQueue"]
        ]
    ))


if __name__ == "__main__":
    main()
