import json
from typing import Any


def default_json(t: Any) -> str:
    return f'{t}'


def get_json_from(obj: Any) -> str:
    return json.dumps(obj, default=default_json)