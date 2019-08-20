import boto3
import botocore
import settings


def create_client():

    """
    :return:
    """
    return boto3.client('sqs', endpoint_url=settings.ENDPOINT_URL)


def receive(sqs=None, url=None):

    """
    :param sqs:
    :param url:
    :return:
    """

    assert isinstance(sqs, botocore.client.BaseClient)
    assert url

    return sqs.receive_message(QueueUrl=url, AttributeNames=['All'])

