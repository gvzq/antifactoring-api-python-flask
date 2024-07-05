# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.invoice_schema import InvoiceSchema  # noqa: E501
from swagger_server.test import BaseTestCase


class TestInvoicesController(BaseTestCase):
    """InvoicesController integration test stubs"""

    def test_scan_invoice(self):
        """Test case for scan_invoice

        Get the details of an invoice by using OCR and AI.
        """
        query_string = [('api_key', Object())]
        data = dict(file=Object())
        response = self.client.open(
            '/openapi.json/api/invoice',
            method='POST',
            data=data,
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
