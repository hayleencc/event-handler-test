from handler import event_listener, send_to_sqs


def main():
    queue_url = 'queue_url'
    message = {
        "entityId": "610110bbbf404ea38b98d5750b75f1f2",
        "action": "create"
    }
    send_to_sqs(message=message, queue_url=queue_url)
    event_listener(queue_url=queue_url)
