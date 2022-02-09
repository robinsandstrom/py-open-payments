# coding: utf-8

"""
    NextGenPSD2 XS2A Framework

    # Summary **Open Payments Europe NextGenPSD2 API** definition is based on The Berlin Group NextGenPSD2 Framework with some additional services like the ASPSP Information Services. The **NextGenPSD2** *Framework Version 1.3.3* offers a modern, open, harmonised and interoperable set of  Application Programming Interfaces (APIs) as the safest and most efficient way to provide data securely.  The NextGenPSD2 Framework reduces XS2A complexity and costs, addresses the problem of multiple competing standards  in Europe and, aligned with the goals of the Euro Retail Payments Board, enables European banking customers to benefit from innovative products and services ('Banking as a Service')  by granting TPPs safe and secure (authenticated and authorised) access to their bank accounts and financial data.  The possible Approaches are:   * Redirect SCA Approach   * OAuth SCA Approach   * Decoupled SCA Approach   * Embedded SCA Approach without SCA method   * Embedded SCA Approach with only one SCA method available   * Embedded SCA Approach with Selection of a SCA method    Not every message defined in this API definition is necessary for all approaches.    Furthermore this API definition does not differ between methods which are mandatory, conditional, or optional  ## Some General Remarks Related to this version of the OpenAPI Specification: * **This API definition is based on the Implementation Guidelines of the Berlin Group PSD2 API.**    It is not an replacement in any sense.   The main specification is (at the moment) always the Implementation Guidelines of the Berlin Group PSD2 API. * **This API definition contains the REST-API for requests from the PISP to the ASPSP.** * **This API definition contains the messages for all different approaches defined in the Implementation Guidelines.** * According to the OpenAPI-Specification [https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.1.md]        \"If in is \"header\" and the name field is \"Accept\", \"Content-Type\" or \"Authorization\", the parameter definition SHALL be ignored.\"      The element \"Accept\" will not be defined in this file at any place.      The elements \"Content-Type\" and \"Authorization\" are implicitly defined by the OpenApi tags \"content\" and \"security\".    * There are several predefined types which might occur in payment initiation messages,    but are not used in the standard JSON messages in the Implementation Guidelines.   Therefore they are not used in the corresponding messages in this file either.   We added them for the convenience of the user.   If there is a payment product, which need these field, one can easily use the predefined types.   But the ASPSP need not to accept them in general.    * **We omit the definition of all standard HTTP header elements (mandatory/optional/conditional)    except they are mention in the Implementation Guidelines.**   Therefore the implementer might add the in his own realisation of a PSD2 comlient API in addition to the elements define in this file.     ## General Remarks on Data Types  The Berlin Group definition of UTF-8 strings in context of the PSD2 API have to support at least the following characters  a b c d e f g h i j k l m n o p q r s t u v w x y z  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  0 1 2 3 4 5 6 7 8 9  / - ? : ( ) . , ' +  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    OpenAPI spec version: 1.3.3
    Contact: info@openpayments.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AccountReferenceWithGiro(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'iban': 'Iban',
        'bban': 'Bban',
        'pan': 'Pan',
        'masked_pan': 'MaskedPan',
        'msisdn': 'Msisdn',
        'bankgiro_number': 'BankGiroNumber',
        'plusgiro_number': 'PlusGiroNumber',
        'clearing_number': 'ClearingNumber',
        'currency': 'CurrencyCode'
    }

    attribute_map = {
        'iban': 'iban',
        'bban': 'bban',
        'pan': 'pan',
        'masked_pan': 'maskedPan',
        'msisdn': 'msisdn',
        'bankgiro_number': 'bankgiroNumber',
        'plusgiro_number': 'plusgiroNumber',
        'clearing_number': 'clearingNumber',
        'currency': 'currency'
    }

    def __init__(self, iban=None, bban=None, pan=None, masked_pan=None, msisdn=None, bankgiro_number=None, plusgiro_number=None, clearing_number=None, currency=None):  # noqa: E501
        """AccountReferenceWithGiro - a model defined in Swagger"""  # noqa: E501
        self._iban = None
        self._bban = None
        self._pan = None
        self._masked_pan = None
        self._msisdn = None
        self._bankgiro_number = None
        self._plusgiro_number = None
        self._clearing_number = None
        self._currency = None
        self.discriminator = None
        if iban is not None:
            self.iban = iban
        if bban is not None:
            self.bban = bban
        if pan is not None:
            self.pan = pan
        if masked_pan is not None:
            self.masked_pan = masked_pan
        if msisdn is not None:
            self.msisdn = msisdn
        if bankgiro_number is not None:
            self.bankgiro_number = bankgiro_number
        if plusgiro_number is not None:
            self.plusgiro_number = plusgiro_number
        if clearing_number is not None:
            self.clearing_number = clearing_number
        if currency is not None:
            self.currency = currency

    @property
    def iban(self):
        """Gets the iban of this AccountReferenceWithGiro.  # noqa: E501


        :return: The iban of this AccountReferenceWithGiro.  # noqa: E501
        :rtype: Iban
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this AccountReferenceWithGiro.


        :param iban: The iban of this AccountReferenceWithGiro.  # noqa: E501
        :type: Iban
        """

        self._iban = iban

    @property
    def bban(self):
        """Gets the bban of this AccountReferenceWithGiro.  # noqa: E501


        :return: The bban of this AccountReferenceWithGiro.  # noqa: E501
        :rtype: Bban
        """
        return self._bban

    @bban.setter
    def bban(self, bban):
        """Sets the bban of this AccountReferenceWithGiro.


        :param bban: The bban of this AccountReferenceWithGiro.  # noqa: E501
        :type: Bban
        """

        self._bban = bban

    @property
    def pan(self):
        """Gets the pan of this AccountReferenceWithGiro.  # noqa: E501


        :return: The pan of this AccountReferenceWithGiro.  # noqa: E501
        :rtype: Pan
        """
        return self._pan

    @pan.setter
    def pan(self, pan):
        """Sets the pan of this AccountReferenceWithGiro.


        :param pan: The pan of this AccountReferenceWithGiro.  # noqa: E501
        :type: Pan
        """

        self._pan = pan

    @property
    def masked_pan(self):
        """Gets the masked_pan of this AccountReferenceWithGiro.  # noqa: E501


        :return: The masked_pan of this AccountReferenceWithGiro.  # noqa: E501
        :rtype: MaskedPan
        """
        return self._masked_pan

    @masked_pan.setter
    def masked_pan(self, masked_pan):
        """Sets the masked_pan of this AccountReferenceWithGiro.


        :param masked_pan: The masked_pan of this AccountReferenceWithGiro.  # noqa: E501
        :type: MaskedPan
        """

        self._masked_pan = masked_pan

    @property
    def msisdn(self):
        """Gets the msisdn of this AccountReferenceWithGiro.  # noqa: E501


        :return: The msisdn of this AccountReferenceWithGiro.  # noqa: E501
        :rtype: Msisdn
        """
        return self._msisdn

    @msisdn.setter
    def msisdn(self, msisdn):
        """Sets the msisdn of this AccountReferenceWithGiro.


        :param msisdn: The msisdn of this AccountReferenceWithGiro.  # noqa: E501
        :type: Msisdn
        """

        self._msisdn = msisdn

    @property
    def bankgiro_number(self):
        """Gets the bankgiro_number of this AccountReferenceWithGiro.  # noqa: E501


        :return: The bankgiro_number of this AccountReferenceWithGiro.  # noqa: E501
        :rtype: BankGiroNumber
        """
        return self._bankgiro_number

    @bankgiro_number.setter
    def bankgiro_number(self, bankgiro_number):
        """Sets the bankgiro_number of this AccountReferenceWithGiro.


        :param bankgiro_number: The bankgiro_number of this AccountReferenceWithGiro.  # noqa: E501
        :type: BankGiroNumber
        """

        self._bankgiro_number = bankgiro_number

    @property
    def plusgiro_number(self):
        """Gets the plusgiro_number of this AccountReferenceWithGiro.  # noqa: E501


        :return: The plusgiro_number of this AccountReferenceWithGiro.  # noqa: E501
        :rtype: PlusGiroNumber
        """
        return self._plusgiro_number

    @plusgiro_number.setter
    def plusgiro_number(self, plusgiro_number):
        """Sets the plusgiro_number of this AccountReferenceWithGiro.


        :param plusgiro_number: The plusgiro_number of this AccountReferenceWithGiro.  # noqa: E501
        :type: PlusGiroNumber
        """

        self._plusgiro_number = plusgiro_number

    @property
    def clearing_number(self):
        """Gets the clearing_number of this AccountReferenceWithGiro.  # noqa: E501


        :return: The clearing_number of this AccountReferenceWithGiro.  # noqa: E501
        :rtype: ClearingNumber
        """
        return self._clearing_number

    @clearing_number.setter
    def clearing_number(self, clearing_number):
        """Sets the clearing_number of this AccountReferenceWithGiro.


        :param clearing_number: The clearing_number of this AccountReferenceWithGiro.  # noqa: E501
        :type: ClearingNumber
        """

        self._clearing_number = clearing_number

    @property
    def currency(self):
        """Gets the currency of this AccountReferenceWithGiro.  # noqa: E501


        :return: The currency of this AccountReferenceWithGiro.  # noqa: E501
        :rtype: CurrencyCode
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this AccountReferenceWithGiro.


        :param currency: The currency of this AccountReferenceWithGiro.  # noqa: E501
        :type: CurrencyCode
        """

        self._currency = currency

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AccountReferenceWithGiro, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AccountReferenceWithGiro):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
