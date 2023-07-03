from datetime import datetime
from uuid import uuid1


def get_date() -> str:
    return ":".join(str(datetime.today()).split(":")[:-1])

def generate_uuid() -> str:
    return "".join(str(uuid1()).split("-"))

def article_uuid(uuid: str) -> str:
    return f"article_{uuid}"

def convert_types(info: list):
    out = {}

    for i in info:
        update_type = i[0]
        update_info = i[1]
        
        if update_type not in out:
            out[update_type] = []
        
        out[update_type].append(update_info)
    
    return out
