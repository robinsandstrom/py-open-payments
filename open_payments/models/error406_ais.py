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

class Error406AIS(object):
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
        'type': 'str',
        'title': 'str',
        'detail': 'str',
        'code': 'MessageCode406AIS',
        'additional_errors': 'list[Error406AISAdditionalErrors]',
        'links': 'LinksAll'
    }

    attribute_map = {
        'type': 'type',
        'title': 'title',
        'detail': 'detail',
        'code': 'code',
        'additional_errors': 'additionalErrors',
        'links': '_links'
    }

    def __init__(self, type=None, title=None, detail=None, code=None, additional_errors=None, links=None):  # noqa: E501
        """Error406AIS - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._title = None
        self._detail = None
        self._code = None
        self._additional_errors = None
        self._links = None
        self.discriminator = None
        self.type = type
        if title is not None:
            self.title = title
        if detail is not None:
            self.detail = detail
        self.code = code
        if additional_errors is not None:
            self.additional_errors = additional_errors
        if links is not None:
            self.links = links

    @property
    def type(self):
        """Gets the type of this Error406AIS.  # noqa: E501

        A URI reference [RFC3986] that identifies the problem type.  Remark For Future: These URI will be provided by NextGenPSD2 in future.   # noqa: E501

        :return: The type of this Error406AIS.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Error406AIS.

        A URI reference [RFC3986] that identifies the problem type.  Remark For Future: These URI will be provided by NextGenPSD2 in future.   # noqa: E501

        :param type: The type of this Error406AIS.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def title(self):
        """Gets the title of this Error406AIS.  # noqa: E501

        Short human readable description of error type.  Could be in local language.  To be provided by ASPSPs.   # noqa: E501

        :return: The title of this Error406AIS.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Error406AIS.

        Short human readable description of error type.  Could be in local language.  To be provided by ASPSPs.   # noqa: E501

        :param title: The title of this Error406AIS.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def detail(self):
        """Gets the detail of this Error406AIS.  # noqa: E501

        Detailed human readable text specific to this instance of the error.  XPath might be used to point to the issue generating the error in addition. Remark for Future: In future, a dedicated field might be introduced for the XPath.   # noqa: E501

        :return: The detail of this Error406AIS.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this Error406AIS.

        Detailed human readable text specific to this instance of the error.  XPath might be used to point to the issue generating the error in addition. Remark for Future: In future, a dedicated field might be introduced for the XPath.   # noqa: E501

        :param detail: The detail of this Error406AIS.  # noqa: E501
        :type: str
        """

        self._detail = detail

    @property
    def code(self):
        """Gets the code of this Error406AIS.  # noqa: E501


        :return: The code of this Error406AIS.  # noqa: E501
        :rtype: MessageCode406AIS
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Error406AIS.


        :param code: The code of this Error406AIS.  # noqa: E501
        :type: MessageCode406AIS
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def additional_errors(self):
        """Gets the additional_errors of this Error406AIS.  # noqa: E501

        Array of Error Information Blocks.  Might be used if more than one error is to be communicated   # noqa: E501

        :return: The additional_errors of this Error406AIS.  # noqa: E501
        :rtype: list[Error406AISAdditionalErrors]
        """
        return self._additional_errors

    @additional_errors.setter
    def additional_errors(self, additional_errors):
        """Sets the additional_errors of this Error406AIS.

        Array of Error Information Blocks.  Might be used if more than one error is to be communicated   # noqa: E501

        :param additional_errors: The additional_errors of this Error406AIS.  # noqa: E501
        :type: list[Error406AISAdditionalErrors]
        """

        self._additional_errors = additional_errors

    @property
    def links(self):
        """Gets the links of this Error406AIS.  # noqa: E501


        :return: The links of this Error406AIS.  # noqa: E501
        :rtype: LinksAll
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Error406AIS.


        :param links: The links of this Error406AIS.  # noqa: E501
        :type: LinksAll
        """

        self._links = links

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
        if issubclass(Error406AIS, dict):
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
        if not isinstance(other, Error406AIS):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other