import random
import uuid

actions = ["create", "update", "delete"]


def message(entityId: str, action: str):
    return {
        "entityId": entityId,
        "action": action
    }


def generate_message():
    return message(entityId=str(uuid.uuid4()), action=random.choice(actions))
