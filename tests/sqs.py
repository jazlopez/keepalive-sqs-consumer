import unittest
import sqs


class TestClient(unittest.TestCase):

    def test_receive_message_expect_sqs_client_argument(self):

        """
        :return:
        """

        with self.assertRaises(AssertionError):
            sqs.receive(sqs=None)

    def test_receive_message_expect_queue_url_argument(self):

        """
        :return:
        """

        with self.assertRaises(AssertionError):
            sqs.receive(sqs=sqs.create_client(), url=None)

    def test_receive_message_raise_exception_with_invalid_queue_url_argument(self):

        """
        :return:
        """
        invalid_queue_url = ""

        with self.assertRaises(BaseException):
            sqs.receive(sqs=sqs.create_client(), url=invalid_queue_url)

    def test_receive_message_not_raise_exception_with_valid_arguments(self):

        self.assertIsNotNone(sqs.receive(sqs=sqs.create_client(), url="http://localhost/queue/foo"))


if __name__ == "__main__":
    unittest.main()
