import connexion
import six

from swagger_server.models.invoice_schema import InvoiceSchema  # noqa: E501
from swagger_server import util


def scan_invoice(file, api_key=None):  # noqa: E501
    """Get the details of an invoice by using OCR and AI.

    Retrieve details of an invoice by sending a multipart form request of a pdf document, jpeg image, png image, bmp image, webp image, or text file. # noqa: E501

    :param file: 
    :type file: dict | bytes
    :param api_key: API key of the user
    :type api_key: dict | bytes

    :rtype: InvoiceSchema
    """
    if connexion.request.is_json:
        file = Object.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        api_key = Object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
