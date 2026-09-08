import unittest

from src.notification_consumer.app import lambda_handler


class NotificationConsumerTests(unittest.TestCase):

    def test_one_sqs_record(self):
        event = {
            "Records": [
                {
                    "messageId": "unit-test-message-001"
                }
            ]
        }

        result = lambda_handler(event, None)

        self.assertEqual(
            result,
            {"processed_records": 1}
        )

    def test_no_sqs_records(self):
        result = lambda_handler({}, None)

        self.assertEqual(
            result,
            {"processed_records": 0}
        )


if __name__ == "__main__":
    unittest.main()
