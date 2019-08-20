import os

ENDPOINT_URL = os.getenv('SQS_CONSUMER_ENDPOINT_URL', None)
QUEUE_URL = os.getenv('SQS_CONSUMER_QUEUE_URL', None)