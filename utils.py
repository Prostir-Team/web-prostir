from datetime import datetime
from uuid import uuid1


def get_date() -> str:
    return ":".join(str(datetime.today()).split(":")[:-1])

def generate_uuid() -> str:
    return str(uuid1())