import json

from sqlalchemy import inspect


def get_json_from(obj):
    if isinstance(obj, list):
        elements = [
            {c.key: getattr(el, c.key) for c in inspect(el).mapper.column_attrs}
            for el in obj
        ]
        return json.dumps(elements)
    else:
        return json.dumps(
            {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}
        )
