# swagger_client.AccountInformationServiceAISApi

All URIs are relative to *https://api.sandbox.openbankingplatform.com/psd2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_list**](AccountInformationServiceAISApi.md#get_account_list) | **GET** /accountinformation/v1/accounts | Get Account List
[**get_balances**](AccountInformationServiceAISApi.md#get_balances) | **GET** /accountinformation/v1/accounts/{account-id}/balances | Get Balances
[**get_transaction_details**](AccountInformationServiceAISApi.md#get_transaction_details) | **GET** /accountinformation/v1/accounts/{account-id}/transactions/{transactionId} | Get Transaction Details
[**get_transaction_list**](AccountInformationServiceAISApi.md#get_transaction_list) | **GET** /accountinformation/v1/accounts/{account-id}/transactions | Get Transaction List
[**read_account_details**](AccountInformationServiceAISApi.md#read_account_details) | **GET** /accountinformation/v1/accounts/{account-id} | Get Account Details

# **get_account_list**
> AccountList get_account_list(x_request_id, x_bic_fi, consent_id, with_balance=with_balance, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, psu_accept=psu_accept, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Get Account List

Read the identifiers of the available payment account together with  booking balance information, depending on the consent granted.  It is assumed that a consent of the PSU to this access is already given and stored on the ASPSP system.  The addressed list of accounts depends then on the PSU ID and the stored consent addressed by consentId,  respectively the OAuth2 access token.   Returns all identifiers of the accounts, to which an account access has been granted to through  the /consents endpoint by the PSU.  In addition, relevant information about the accounts and hyperlinks to corresponding account  information resources are provided if a related consent has been already granted.  Remark: Note that the /consents endpoint optionally offers to grant an access on all available  payment accounts of a PSU.  In this case, this endpoint will deliver the information about all available payment accounts  of the PSU at this ASPSP. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oAuth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceAISApi(swagger_client.ApiClient(configuration))
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
consent_id = swagger_client.ConsentId() # ConsentId | This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. 
with_balance = true # bool | If contained, this function reads the list of accessible payment accounts including the booking balance,  if granted by the PSU in the related consent and available by the ASPSP.  This parameter might be ignored by the ASPSP.   (optional)
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding HTTP request  IP Address field between PSU and TPP.  It shall be contained if and only if this request was actively initiated by the PSU.  (optional)
psu_ip_port = 'psu_ip_port_example' # str | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  (optional)
psu_accept = 'psu_accept_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
tpp_redirect_preferred = 'tpp_redirect_preferred_example' # str | If it equals \"true\", the TPP prefers a redirect over an embedded SCA approach. If it equals \"false\", the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  (optional)
psu_accept_charset = 'psu_accept_charset_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_accept_encoding = 'psu_accept_encoding_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_accept_language = 'psu_accept_language_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_user_agent = 'psu_user_agent_example' # str | The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  (optional)
psu_http_method = 'psu_http_method_example' # str | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  (optional)
psu_device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID need to be unaltered until removal from device.  (optional)
psu_geo_location = 'psu_geo_location_example' # str | The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  (optional)

try:
    # Get Account List
    api_response = api_instance.get_account_list(x_request_id, x_bic_fi, consent_id, with_balance=with_balance, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, psu_accept=psu_accept, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->get_account_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
 **consent_id** | [**ConsentId**](.md)| This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation.  | 
 **with_balance** | **bool**| If contained, this function reads the list of accessible payment accounts including the booking balance,  if granted by the PSU in the related consent and available by the ASPSP.  This parameter might be ignored by the ASPSP.   | [optional] 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding HTTP request  IP Address field between PSU and TPP.  It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
 **psu_ip_port** | **str**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] 
 **psu_accept** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **tpp_redirect_preferred** | **str**| If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  | [optional] 
 **psu_accept_charset** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_accept_encoding** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_accept_language** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_user_agent** | **str**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] 
 **psu_http_method** | **str**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] 
 **psu_device_id** | [**str**](.md)| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID need to be unaltered until removal from device.  | [optional] 
 **psu_geo_location** | **str**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] 

### Return type

[**AccountList**](AccountList.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balances**
> ReadAccountBalanceResponse200 get_balances(account_id, x_request_id, x_bic_fi, consent_id, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Get Balances

Reads account data from a given account addressed by \"account-id\".   **Remark:** This account-id can be a tokenised identification due to data protection reason since the path  information might be logged on intermediary servers within the ASPSP sphere.  This account-id then can be retrieved by the \"GET Account List\" call.  The account-id is constant at least throughout the lifecycle of a given consent. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oAuth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceAISApi(swagger_client.ApiClient(configuration))
account_id = swagger_client.AccountId() # AccountId | This identification is denoting the addressed account.  The account-id is retrieved by using a \"Read Account List\" call.  The account-id is the \"id\" attribute of the account structure.  Its value is constant at least throughout the lifecycle of a given consent. 
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
consent_id = swagger_client.ConsentId() # ConsentId | This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. 
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding HTTP request  IP Address field between PSU and TPP.  It shall be contained if and only if this request was actively initiated by the PSU.  (optional)
psu_ip_port = 'psu_ip_port_example' # str | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  (optional)
tpp_redirect_preferred = 'tpp_redirect_preferred_example' # str | If it equals \"true\", the TPP prefers a redirect over an embedded SCA approach. If it equals \"false\", the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  (optional)
psu_accept = 'psu_accept_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_accept_charset = 'psu_accept_charset_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_accept_encoding = 'psu_accept_encoding_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_accept_language = 'psu_accept_language_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_user_agent = 'psu_user_agent_example' # str | The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  (optional)
psu_http_method = 'psu_http_method_example' # str | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  (optional)
psu_device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID need to be unaltered until removal from device.  (optional)
psu_geo_location = 'psu_geo_location_example' # str | The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  (optional)

try:
    # Get Balances
    api_response = api_instance.get_balances(account_id, x_request_id, x_bic_fi, consent_id, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->get_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**AccountId**](.md)| This identification is denoting the addressed account.  The account-id is retrieved by using a \&quot;Read Account List\&quot; call.  The account-id is the \&quot;id\&quot; attribute of the account structure.  Its value is constant at least throughout the lifecycle of a given consent.  | 
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
 **consent_id** | [**ConsentId**](.md)| This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation.  | 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding HTTP request  IP Address field between PSU and TPP.  It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
 **psu_ip_port** | **str**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] 
 **tpp_redirect_preferred** | **str**| If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  | [optional] 
 **psu_accept** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_accept_charset** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_accept_encoding** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_accept_language** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_user_agent** | **str**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] 
 **psu_http_method** | **str**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] 
 **psu_device_id** | [**str**](.md)| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID need to be unaltered until removal from device.  | [optional] 
 **psu_geo_location** | **str**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] 

### Return type

[**ReadAccountBalanceResponse200**](ReadAccountBalanceResponse200.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_details**
> TransactionDetailsWithTppMessages get_transaction_details(account_id, transaction_id, x_request_id, x_bic_fi, consent_id, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Get Transaction Details

Reads transaction details from a given transaction addressed by \"transactionId\" on a given account addressed by \"account-id\".  This call is only available on transactions as reported in a JSON format.  **Remark:** Please note that the PATH might be already given in detail by the corresponding entry of the response of the  \"Read Transaction List\" call within the _links subfield. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oAuth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceAISApi(swagger_client.ApiClient(configuration))
account_id = swagger_client.AccountId() # AccountId | This identification is denoting the addressed account.  The account-id is retrieved by using a \"Read Account List\" call.  The account-id is the \"id\" attribute of the account structure.  Its value is constant at least throughout the lifecycle of a given consent. 
transaction_id = swagger_client.TransactionId() # TransactionId | This identification is given by the attribute transactionId of the corresponding entry of a transaction list. 
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
consent_id = swagger_client.ConsentId() # ConsentId | This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. 
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding HTTP request  IP Address field between PSU and TPP.  It shall be contained if and only if this request was actively initiated by the PSU.  (optional)
psu_ip_port = 'psu_ip_port_example' # str | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  (optional)
tpp_redirect_preferred = 'tpp_redirect_preferred_example' # str | If it equals \"true\", the TPP prefers a redirect over an embedded SCA approach. If it equals \"false\", the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  (optional)
psu_accept = 'psu_accept_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_accept_charset = 'psu_accept_charset_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_accept_encoding = 'psu_accept_encoding_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_accept_language = 'psu_accept_language_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_user_agent = 'psu_user_agent_example' # str | The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  (optional)
psu_http_method = 'psu_http_method_example' # str | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  (optional)
psu_device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID need to be unaltered until removal from device.  (optional)
psu_geo_location = 'psu_geo_location_example' # str | The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  (optional)

try:
    # Get Transaction Details
    api_response = api_instance.get_transaction_details(account_id, transaction_id, x_request_id, x_bic_fi, consent_id, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->get_transaction_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**AccountId**](.md)| This identification is denoting the addressed account.  The account-id is retrieved by using a \&quot;Read Account List\&quot; call.  The account-id is the \&quot;id\&quot; attribute of the account structure.  Its value is constant at least throughout the lifecycle of a given consent.  | 
 **transaction_id** | [**TransactionId**](.md)| This identification is given by the attribute transactionId of the corresponding entry of a transaction list.  | 
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
 **consent_id** | [**ConsentId**](.md)| This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation.  | 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding HTTP request  IP Address field between PSU and TPP.  It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
 **psu_ip_port** | **str**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] 
 **tpp_redirect_preferred** | **str**| If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  | [optional] 
 **psu_accept** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_accept_charset** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_accept_encoding** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_accept_language** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_user_agent** | **str**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] 
 **psu_http_method** | **str**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] 
 **psu_device_id** | [**str**](.md)| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID need to be unaltered until removal from device.  | [optional] 
 **psu_geo_location** | **str**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] 

### Return type

[**TransactionDetailsWithTppMessages**](TransactionDetailsWithTppMessages.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_list**
> TransactionsResponse200Json get_transaction_list(account_id, booking_status, x_request_id, x_bic_fi, consent_id, date_from=date_from, date_to=date_to, entry_reference_from=entry_reference_from, delta_list=delta_list, with_balance=with_balance, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Get Transaction List

Read transaction reports or transaction lists of a given account ddressed by \"account-id\", depending on the steering parameter  \"bookingStatus\" together with balances.  For a given account, additional parameters are e.g. the attributes \"dateFrom\" and \"dateTo\".  The ASPSP might add balance information, if transaction lists without balances are not supported. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oAuth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceAISApi(swagger_client.ApiClient(configuration))
account_id = swagger_client.AccountId() # AccountId | This identification is denoting the addressed account.  The account-id is retrieved by using a \"Read Account List\" call.  The account-id is the \"id\" attribute of the account structure.  Its value is constant at least throughout the lifecycle of a given consent. 
booking_status = 'booking_status_example' # str | Permitted codes are    * \"booked\",   * \"pending\" and    * \"both\" \"booked\" shall be supported by the ASPSP. To support the \"pending\" and \"both\" feature is optional for the ASPSP,  Error code if not supported in the online banking frontend 
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
consent_id = swagger_client.ConsentId() # ConsentId | This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. 
date_from = '2013-10-20' # date | Conditional: Starting date (inclusive the date dateFrom) of the transaction list, mandated if no delta access is required.  For booked transactions, the relevant date is the booking date.   For pending transactions, the relevant date is the entry date, which may not be transparent  neither in this API nor other channels of the ASPSP.  (optional)
date_to = '2013-10-20' # date | End date (inclusive the data dateTo) of the transaction list, default is \"now\" if not given.   Might be ignored if a delta function is used.  For booked transactions, the relevant date is the booking date.   For pending transactions, the relevant date is the entry date, which may not be transparent  neither in this API nor other channels of the ASPSP.  (optional)
entry_reference_from = 'entry_reference_from_example' # str | This data attribute is indicating that the AISP is in favour to get all transactions after  the transaction with identification entryReferenceFrom alternatively to the above defined period.  This is a implementation of a delta access.  If this data element is contained, the entries \"dateFrom\" and \"dateTo\" might be ignored by the ASPSP  if a delta report is supported.  Optional if supported by API provider.  (optional)
delta_list = true # bool | This data attribute is indicating that the AISP is in favour to get all transactions after the last report access for this PSU on the addressed account. This is another implementation of a delta access-report. This delta indicator might be rejected by the ASPSP if this function is not supported. Optional if supported by API provider (optional)
with_balance = true # bool | If contained, this function reads the list of accessible payment accounts including the booking balance,  if granted by the PSU in the related consent and available by the ASPSP.  This parameter might be ignored by the ASPSP.   (optional)
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding HTTP request  IP Address field between PSU and TPP.  It shall be contained if and only if this request was actively initiated by the PSU.  (optional)
psu_ip_port = 'psu_ip_port_example' # str | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  (optional)
tpp_redirect_preferred = 'tpp_redirect_preferred_example' # str | If it equals \"true\", the TPP prefers a redirect over an embedded SCA approach. If it equals \"false\", the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  (optional)
psu_accept = 'psu_accept_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_accept_charset = 'psu_accept_charset_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_accept_encoding = 'psu_accept_encoding_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_accept_language = 'psu_accept_language_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_user_agent = 'psu_user_agent_example' # str | The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  (optional)
psu_http_method = 'psu_http_method_example' # str | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  (optional)
psu_device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID need to be unaltered until removal from device.  (optional)
psu_geo_location = 'psu_geo_location_example' # str | The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  (optional)

try:
    # Get Transaction List
    api_response = api_instance.get_transaction_list(account_id, booking_status, x_request_id, x_bic_fi, consent_id, date_from=date_from, date_to=date_to, entry_reference_from=entry_reference_from, delta_list=delta_list, with_balance=with_balance, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->get_transaction_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**AccountId**](.md)| This identification is denoting the addressed account.  The account-id is retrieved by using a \&quot;Read Account List\&quot; call.  The account-id is the \&quot;id\&quot; attribute of the account structure.  Its value is constant at least throughout the lifecycle of a given consent.  | 
 **booking_status** | **str**| Permitted codes are    * \&quot;booked\&quot;,   * \&quot;pending\&quot; and    * \&quot;both\&quot; \&quot;booked\&quot; shall be supported by the ASPSP. To support the \&quot;pending\&quot; and \&quot;both\&quot; feature is optional for the ASPSP,  Error code if not supported in the online banking frontend  | 
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
 **consent_id** | [**ConsentId**](.md)| This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation.  | 
 **date_from** | **date**| Conditional: Starting date (inclusive the date dateFrom) of the transaction list, mandated if no delta access is required.  For booked transactions, the relevant date is the booking date.   For pending transactions, the relevant date is the entry date, which may not be transparent  neither in this API nor other channels of the ASPSP.  | [optional] 
 **date_to** | **date**| End date (inclusive the data dateTo) of the transaction list, default is \&quot;now\&quot; if not given.   Might be ignored if a delta function is used.  For booked transactions, the relevant date is the booking date.   For pending transactions, the relevant date is the entry date, which may not be transparent  neither in this API nor other channels of the ASPSP.  | [optional] 
 **entry_reference_from** | **str**| This data attribute is indicating that the AISP is in favour to get all transactions after  the transaction with identification entryReferenceFrom alternatively to the above defined period.  This is a implementation of a delta access.  If this data element is contained, the entries \&quot;dateFrom\&quot; and \&quot;dateTo\&quot; might be ignored by the ASPSP  if a delta report is supported.  Optional if supported by API provider.  | [optional] 
 **delta_list** | **bool**| This data attribute is indicating that the AISP is in favour to get all transactions after the last report access for this PSU on the addressed account. This is another implementation of a delta access-report. This delta indicator might be rejected by the ASPSP if this function is not supported. Optional if supported by API provider | [optional] 
 **with_balance** | **bool**| If contained, this function reads the list of accessible payment accounts including the booking balance,  if granted by the PSU in the related consent and available by the ASPSP.  This parameter might be ignored by the ASPSP.   | [optional] 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding HTTP request  IP Address field between PSU and TPP.  It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
 **psu_ip_port** | **str**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] 
 **tpp_redirect_preferred** | **str**| If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  | [optional] 
 **psu_accept** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_accept_charset** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_accept_encoding** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_accept_language** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_user_agent** | **str**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] 
 **psu_http_method** | **str**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] 
 **psu_device_id** | [**str**](.md)| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID need to be unaltered until removal from device.  | [optional] 
 **psu_geo_location** | **str**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] 

### Return type

[**TransactionsResponse200Json**](TransactionsResponse200Json.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/text, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_account_details**
> AccountDetailsWithTppMessages read_account_details(account_id, x_request_id, x_bic_fi, consent_id, with_balance=with_balance, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Get Account Details

Reads details about an account, with balances where required.  It is assumed that a consent of the PSU to  this access is already given and stored on the ASPSP system.  The addressed details of this account depends then on the stored consent addressed by consentId,  respectively the OAuth2 access token.  **NOTE:** The account-id can represent a multicurrency account.  In this case the currency code is set to \"XXX\".  Give detailed information about the addressed account.  Give detailed information about the addressed account together with balance information 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oAuth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceAISApi(swagger_client.ApiClient(configuration))
account_id = swagger_client.AccountId() # AccountId | This identification is denoting the addressed account.  The account-id is retrieved by using a \"Read Account List\" call.  The account-id is the \"id\" attribute of the account structure.  Its value is constant at least throughout the lifecycle of a given consent. 
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
consent_id = swagger_client.ConsentId() # ConsentId | This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. 
with_balance = true # bool | If contained, this function reads the list of accessible payment accounts including the booking balance,  if granted by the PSU in the related consent and available by the ASPSP.  This parameter might be ignored by the ASPSP.   (optional)
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding HTTP request  IP Address field between PSU and TPP.  It shall be contained if and only if this request was actively initiated by the PSU.  (optional)
psu_ip_port = 'psu_ip_port_example' # str | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  (optional)
tpp_redirect_preferred = 'tpp_redirect_preferred_example' # str | If it equals \"true\", the TPP prefers a redirect over an embedded SCA approach. If it equals \"false\", the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  (optional)
psu_accept = 'psu_accept_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_accept_charset = 'psu_accept_charset_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_accept_encoding = 'psu_accept_encoding_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_accept_language = 'psu_accept_language_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_user_agent = 'psu_user_agent_example' # str | The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  (optional)
psu_http_method = 'psu_http_method_example' # str | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  (optional)
psu_device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID need to be unaltered until removal from device.  (optional)
psu_geo_location = 'psu_geo_location_example' # str | The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  (optional)

try:
    # Get Account Details
    api_response = api_instance.read_account_details(account_id, x_request_id, x_bic_fi, consent_id, with_balance=with_balance, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->read_account_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**AccountId**](.md)| This identification is denoting the addressed account.  The account-id is retrieved by using a \&quot;Read Account List\&quot; call.  The account-id is the \&quot;id\&quot; attribute of the account structure.  Its value is constant at least throughout the lifecycle of a given consent.  | 
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
 **consent_id** | [**ConsentId**](.md)| This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation.  | 
 **with_balance** | **bool**| If contained, this function reads the list of accessible payment accounts including the booking balance,  if granted by the PSU in the related consent and available by the ASPSP.  This parameter might be ignored by the ASPSP.   | [optional] 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding HTTP request  IP Address field between PSU and TPP.  It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
 **psu_ip_port** | **str**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] 
 **tpp_redirect_preferred** | **str**| If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  | [optional] 
 **psu_accept** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_accept_charset** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_accept_encoding** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_accept_language** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_user_agent** | **str**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] 
 **psu_http_method** | **str**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] 
 **psu_device_id** | [**str**](.md)| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID need to be unaltered until removal from device.  | [optional] 
 **psu_geo_location** | **str**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] 

### Return type

[**AccountDetailsWithTppMessages**](AccountDetailsWithTppMessages.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

