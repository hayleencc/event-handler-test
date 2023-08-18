from handler import event_listener, send_to_sqs
from message import generate_message


def main():
    queue_url = 'https://sqs.us-east-1.amazonaws.com/143992986020/test-handler-event.fifo'

    for _ in range(10):
        send_to_sqs(message=generate_message(), queue_url=queue_url)
    event_listener(queue_url=queue_url)


main()
