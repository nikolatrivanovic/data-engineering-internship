import os
import unittest
from unittest.mock import patch, MagicMock
from get_folder import lambda_handler, copy_object

class TestLambdaFunction(unittest.TestCase):

    def setUp(self):
        os.environ['FOLDER_PREFIX'] = 'test-prefix/'

    def tearDown(self):
        if 'FOLDER_PREFIX' in os.environ:
            del os.environ['FOLDER_PREFIX']

    @patch('get_folder.boto3.client')
    def test_lambda_handler_valid(self, mock_boto_client):
        mock_s3_client = MagicMock()
        mock_boto_client.return_value = mock_s3_client

        mock_paginator = MagicMock()
        mock_s3_client.get_paginator.return_value = mock_paginator

        mock_page_iterator = [
            {'Contents': [{'Key': 'test-prefix/Beograd/file1.txt'}, {'Key': 'test-prefix/NotCorrect/file2.txt'}]},
            {'Contents': [{'Key': 'test-prefix/Beograd/file3.txt'}]}
        ]
        mock_paginator.paginate.return_value = mock_page_iterator

        event = {}
        context = {}
        with patch('get_folder.ThreadPoolExecutor') as mock_executor:
            mock_executor_instance = mock_executor.return_value
            mock_executor_instance.__enter__.return_value = mock_executor_instance
            lambda_handler(event, context)

            self.assertEqual(mock_executor_instance.submit.call_count, 2)

    @patch('get_folder.boto3.client')
    def test_lambda_handler_empty_page(self, mock_boto_client):
        mock_s3_client = MagicMock()
        mock_boto_client.return_value = mock_s3_client

        mock_paginator = MagicMock()
        mock_s3_client.get_paginator.return_value = mock_paginator

        mock_page_iterator = [{'Contents': []}]
        mock_paginator.paginate.return_value = mock_page_iterator

        event = {}
        context = {}
        with patch('get_folder.ThreadPoolExecutor') as mock_executor:
            lambda_handler(event, context)
            mock_executor.return_value.submit.assert_not_called()

    @patch('get_folder.boto3.client')
    def test_lambda_handler_missing_prefix(self, mock_boto_client):
        del os.environ['FOLDER_PREFIX']
        mock_s3_client = MagicMock()
        mock_boto_client.return_value = mock_s3_client

        event = {}
        context = {}
        with self.assertRaises(ValueError) as context_manager:
            lambda_handler(event, context)
        self.assertIn("FOLDER_PREFIX is not set", str(context_manager.exception))

    def test_copy_object(self):
        mock_s3_client = MagicMock()

        copy_object(
            mock_s3_client,
            source_bucket="source-bucket",
            destination_bucket="destination-bucket",
            source_key="source-key",
            destination_key="destination-key"
        )

        mock_s3_client.copy_object.assert_called_once_with(
            CopySource={'Bucket': 'source-bucket', 'Key': 'source-key'},
            Bucket='destination-bucket',
            Key='destination-key'
        )


if __name__ == '__main__':
    unittest.main()
