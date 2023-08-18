import boto3
import json
from botocore.exceptions import ClientError


def send_to_sqs(message: str, queue_url: str):
    try:
        sqs_client = boto3.client('sqs')
        sqs_client.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(message),
            MessageGroupId='test-event-handler'
        )
        print("Success sending message to SQS with ID: ", message["entityId"])
    except ClientError as e:
        print("Error sending message to SQS: ", e.response['Error']['Message'])
        return None


def event_listener(queue_url: str):
    sqs_client = boto3.client('sqs')
    try:
        while True:
            response = sqs_client.receive_message(
                QueueUrl=queue_url,
                MaxNumberOfMessages=10,
                WaitTimeSeconds=10
            )
            if 'Messages' in response:
                for message in response['Messages']:
                    body = json.loads(message['Body'])
                    print("Message received:", body.get("entityId"))

                    try:
                        receipt_handle = message['ReceiptHandle']
                        sqs_client.delete_message(
                            QueueUrl=queue_url, ReceiptHandle=receipt_handle)
                        print("Message deleted from queue:",
                              message['MessageId'])
                    except ClientError as delete_error:
                        print("Error trying to delete from queue:", delete_error)
            else:
                break
    except ClientError as e:
        print("Error receiving message from SQS:", e)
