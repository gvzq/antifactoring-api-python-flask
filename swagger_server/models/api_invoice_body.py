# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ApiInvoiceBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, file: Object=None):  # noqa: E501
        """ApiInvoiceBody - a model defined in Swagger

        :param file: The file of this ApiInvoiceBody.  # noqa: E501
        :type file: Object
        """
        self.swagger_types = {
            'file': Object
        }

        self.attribute_map = {
            'file': 'file'
        }
        self._file = file

    @classmethod
    def from_dict(cls, dikt) -> 'ApiInvoiceBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The api_invoice_body of this ApiInvoiceBody.  # noqa: E501
        :rtype: ApiInvoiceBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def file(self) -> Object:
        """Gets the file of this ApiInvoiceBody.


        :return: The file of this ApiInvoiceBody.
        :rtype: Object
        """
        return self._file

    @file.setter
    def file(self, file: Object):
        """Sets the file of this ApiInvoiceBody.


        :param file: The file of this ApiInvoiceBody.
        :type file: Object
        """
        if file is None:
            raise ValueError("Invalid value for `file`, must not be `None`")  # noqa: E501

        self._file = file
