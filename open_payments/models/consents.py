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

class Consents(object):
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
        'access': 'AccountAccess',
        'recurring_indicator': 'RecurringIndicator',
        'valid_until': 'ValidUntil',
        'frequency_per_day': 'FrequencyPerDay',
        'combined_service_indicator': 'bool'
    }

    attribute_map = {
        'access': 'access',
        'recurring_indicator': 'recurringIndicator',
        'valid_until': 'validUntil',
        'frequency_per_day': 'frequencyPerDay',
        'combined_service_indicator': 'combinedServiceIndicator'
    }

    def __init__(self, access=None, recurring_indicator=None, valid_until=None, frequency_per_day=None, combined_service_indicator=None):  # noqa: E501
        """Consents - a model defined in Swagger"""  # noqa: E501
        self._access = None
        self._recurring_indicator = None
        self._valid_until = None
        self._frequency_per_day = None
        self._combined_service_indicator = None
        self.discriminator = None
        self.access = access
        self.recurring_indicator = recurring_indicator
        self.valid_until = valid_until
        self.frequency_per_day = frequency_per_day
        self.combined_service_indicator = combined_service_indicator

    @property
    def access(self):
        """Gets the access of this Consents.  # noqa: E501


        :return: The access of this Consents.  # noqa: E501
        :rtype: AccountAccess
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this Consents.


        :param access: The access of this Consents.  # noqa: E501
        :type: AccountAccess
        """
        if access is None:
            raise ValueError("Invalid value for `access`, must not be `None`")  # noqa: E501

        self._access = access

    @property
    def recurring_indicator(self):
        """Gets the recurring_indicator of this Consents.  # noqa: E501


        :return: The recurring_indicator of this Consents.  # noqa: E501
        :rtype: RecurringIndicator
        """
        return self._recurring_indicator

    @recurring_indicator.setter
    def recurring_indicator(self, recurring_indicator):
        """Sets the recurring_indicator of this Consents.


        :param recurring_indicator: The recurring_indicator of this Consents.  # noqa: E501
        :type: RecurringIndicator
        """
        if recurring_indicator is None:
            raise ValueError("Invalid value for `recurring_indicator`, must not be `None`")  # noqa: E501

        self._recurring_indicator = recurring_indicator

    @property
    def valid_until(self):
        """Gets the valid_until of this Consents.  # noqa: E501


        :return: The valid_until of this Consents.  # noqa: E501
        :rtype: ValidUntil
        """
        return self._valid_until

    @valid_until.setter
    def valid_until(self, valid_until):
        """Sets the valid_until of this Consents.


        :param valid_until: The valid_until of this Consents.  # noqa: E501
        :type: ValidUntil
        """
        if valid_until is None:
            raise ValueError("Invalid value for `valid_until`, must not be `None`")  # noqa: E501

        self._valid_until = valid_until

    @property
    def frequency_per_day(self):
        """Gets the frequency_per_day of this Consents.  # noqa: E501


        :return: The frequency_per_day of this Consents.  # noqa: E501
        :rtype: FrequencyPerDay
        """
        return self._frequency_per_day

    @frequency_per_day.setter
    def frequency_per_day(self, frequency_per_day):
        """Sets the frequency_per_day of this Consents.


        :param frequency_per_day: The frequency_per_day of this Consents.  # noqa: E501
        :type: FrequencyPerDay
        """
        if frequency_per_day is None:
            raise ValueError("Invalid value for `frequency_per_day`, must not be `None`")  # noqa: E501

        self._frequency_per_day = frequency_per_day

    @property
    def combined_service_indicator(self):
        """Gets the combined_service_indicator of this Consents.  # noqa: E501

        If \"true\" indicates that a payment initiation service will be addressed in the same \"session\".   # noqa: E501

        :return: The combined_service_indicator of this Consents.  # noqa: E501
        :rtype: bool
        """
        return self._combined_service_indicator

    @combined_service_indicator.setter
    def combined_service_indicator(self, combined_service_indicator):
        """Sets the combined_service_indicator of this Consents.

        If \"true\" indicates that a payment initiation service will be addressed in the same \"session\".   # noqa: E501

        :param combined_service_indicator: The combined_service_indicator of this Consents.  # noqa: E501
        :type: bool
        """
        if combined_service_indicator is None:
            raise ValueError("Invalid value for `combined_service_indicator`, must not be `None`")  # noqa: E501

        self._combined_service_indicator = combined_service_indicator

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
        if issubclass(Consents, dict):
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
        if not isinstance(other, Consents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
