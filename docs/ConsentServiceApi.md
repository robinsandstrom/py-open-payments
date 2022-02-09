# swagger_client.ConsentServiceApi

All URIs are relative to *https://api.sandbox.openbankingplatform.com/psd2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_consent**](ConsentServiceApi.md#create_consent) | **POST** /consent/v1/consents | Create Consent
[**delete_consent**](ConsentServiceApi.md#delete_consent) | **DELETE** /consent/v1/consents/{consentId} | Delete Consent
[**get_consent_authorisation**](ConsentServiceApi.md#get_consent_authorisation) | **GET** /consent/v1/consents/{consentId}/authorisations | Get Consent Authorisation Sub-Resources
[**get_consent_information**](ConsentServiceApi.md#get_consent_information) | **GET** /consent/v1/consents/{consentId} | Get Consent
[**get_consent_sca_status**](ConsentServiceApi.md#get_consent_sca_status) | **GET** /consent/v1/consents/{consentId}/authorisations/{authorisationId} | Get Consent Authorisation SCA Status
[**get_consent_status**](ConsentServiceApi.md#get_consent_status) | **GET** /consent/v1/consents/{consentId}/status | Get Consent Status
[**start_consent_authorisation**](ConsentServiceApi.md#start_consent_authorisation) | **POST** /consent/v1/consents/{consentId}/authorisations | Start Consent Authorisation Process
[**update_consents_psu_data**](ConsentServiceApi.md#update_consents_psu_data) | **PUT** /consent/v1/consents/{consentId}/authorisations/{authorisationId} | Update PSU Data for Consent

# **create_consent**
> ConsentsResponse201 create_consent(x_request_id, x_bic_fi, body=body, x_affiliated_aspsp_id=x_affiliated_aspsp_id, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, tpp_redirect_preferred=tpp_redirect_preferred, tpp_redirect_uri=tpp_redirect_uri, tpp_nok_redirect_uri=tpp_nok_redirect_uri, tpp_explicit_authorisation_preferred=tpp_explicit_authorisation_preferred, tpp_notification_uri=tpp_notification_uri, tpp_notification_content_preferred=tpp_notification_content_preferred, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Create Consent

This method create a consent resource, defining access rights to dedicated accounts of  a given PSU-ID. These accounts are addressed explicitly in the method as  parameters as a core function.  **Side Effects** When this Consent Request is a request where the \"recurringIndicator\" equals \"true\",  and if it exists already a former consent for recurring access on account information  for the addressed PSU, then the former consent automatically expires as soon as the new  consent request is authorised by the PSU.  Optional Extension: As an option, an ASPSP might optionally accept a specific access right on the access on all psd2 related services for all available accounts.   As another option an ASPSP might optionally also accept a command, where only access rights are inserted without mentioning the addressed account.  The relation to accounts is then handled afterwards between PSU and ASPSP.  This option is not supported for the Embedded SCA Approach.  As a last option, an ASPSP might in addition accept a command with access rights   * to see the list of available payment accounts or   * to see the list of available payment accounts with balances. 

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
api_instance = swagger_client.ConsentServiceApi(swagger_client.ApiClient(configuration))
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
body = swagger_client.Consents() # Consents | Requestbody for a consents request
 (optional)
x_affiliated_aspsp_id = 'x_affiliated_aspsp_id_example' # str | The ID of an affiliated ASPSP as related to the X-BicFi header  (optional)
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)
psu_id = 'psu_id_example' # str | Client ID of the PSU in the ASPSP client interface. Might be mandated in the ASPSP's documentation. Is not contained if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session.  (optional)
psu_id_type = 'psu_id_type_example' # str | Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | Might be mandated in the ASPSP's documentation. Only used in a corporate context.  (optional)
psu_corporate_id_type = 'psu_corporate_id_type_example' # str | Might be mandated in the ASPSP's documentation. Only used in a corporate context.  (optional)
tpp_redirect_preferred = 'tpp_redirect_preferred_example' # str | If it equals \"true\", the TPP prefers a redirect over an embedded SCA approach. If it equals \"false\", the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  (optional)
tpp_redirect_uri = 'tpp_redirect_uri_example' # str | URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically  when TPP-Redirect-Preferred equals \"true\". It is recommended to always use this header field.  **Remark for Future:**  This field might be changed to mandatory in the next version of the specification.  (optional)
tpp_nok_redirect_uri = 'tpp_nok_redirect_uri_example' # str | If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP.  (optional)
tpp_explicit_authorisation_preferred = 'tpp_explicit_authorisation_preferred_example' # str | If it equals \"true\", the TPP prefers to start the authorisation process separately,  e.g. because of the usage of a signing basket.  This preference might be ignored by the ASPSP, if a signing basket is not supported as functionality.  If it equals \"false\" or if the parameter is not used, there is no preference of the TPP.  This especially indicates that the TPP assumes a direct authorisation of the transaction in the next step,  without using a signing basket.  (optional)
tpp_notification_uri = 'tpp_notification_uri_example' # str | URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  (optional)
tpp_notification_content_preferred = 'tpp_notification_content_preferred_example' # str | The string has the form   status=X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding HTTP request  IP Address field between PSU and TPP.  It shall be contained if and only if this request was actively initiated by the PSU.  (optional)
psu_ip_port = 'psu_ip_port_example' # str | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  (optional)
psu_accept = 'psu_accept_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_accept_charset = 'psu_accept_charset_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_accept_encoding = 'psu_accept_encoding_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_accept_language = 'psu_accept_language_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_user_agent = 'psu_user_agent_example' # str | The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  (optional)
psu_http_method = 'psu_http_method_example' # str | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  (optional)
psu_device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID need to be unaltered until removal from device.  (optional)
psu_geo_location = 'psu_geo_location_example' # str | The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  (optional)

try:
    # Create Consent
    api_response = api_instance.create_consent(x_request_id, x_bic_fi, body=body, x_affiliated_aspsp_id=x_affiliated_aspsp_id, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, tpp_redirect_preferred=tpp_redirect_preferred, tpp_redirect_uri=tpp_redirect_uri, tpp_nok_redirect_uri=tpp_nok_redirect_uri, tpp_explicit_authorisation_preferred=tpp_explicit_authorisation_preferred, tpp_notification_uri=tpp_notification_uri, tpp_notification_content_preferred=tpp_notification_content_preferred, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentServiceApi->create_consent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
 **body** | [**Consents**](Consents.md)| Requestbody for a consents request
 | [optional] 
 **x_affiliated_aspsp_id** | **str**| The ID of an affiliated ASPSP as related to the X-BicFi header  | [optional] 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 
 **psu_id** | **str**| Client ID of the PSU in the ASPSP client interface. Might be mandated in the ASPSP&#x27;s documentation. Is not contained if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session.  | [optional] 
 **psu_id_type** | **str**| Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  | [optional] 
 **psu_corporate_id** | **str**| Might be mandated in the ASPSP&#x27;s documentation. Only used in a corporate context.  | [optional] 
 **psu_corporate_id_type** | **str**| Might be mandated in the ASPSP&#x27;s documentation. Only used in a corporate context.  | [optional] 
 **tpp_redirect_preferred** | **str**| If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  | [optional] 
 **tpp_redirect_uri** | **str**| URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically  when TPP-Redirect-Preferred equals \&quot;true\&quot;. It is recommended to always use this header field.  **Remark for Future:**  This field might be changed to mandatory in the next version of the specification.  | [optional] 
 **tpp_nok_redirect_uri** | **str**| If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP.  | [optional] 
 **tpp_explicit_authorisation_preferred** | **str**| If it equals \&quot;true\&quot;, the TPP prefers to start the authorisation process separately,  e.g. because of the usage of a signing basket.  This preference might be ignored by the ASPSP, if a signing basket is not supported as functionality.  If it equals \&quot;false\&quot; or if the parameter is not used, there is no preference of the TPP.  This especially indicates that the TPP assumes a direct authorisation of the transaction in the next step,  without using a signing basket.  | [optional] 
 **tpp_notification_uri** | **str**| URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  | [optional] 
 **tpp_notification_content_preferred** | **str**| The string has the form   status&#x3D;X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP.  | [optional] 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding HTTP request  IP Address field between PSU and TPP.  It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
 **psu_ip_port** | **str**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] 
 **psu_accept** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_accept_charset** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_accept_encoding** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_accept_language** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_user_agent** | **str**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] 
 **psu_http_method** | **str**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] 
 **psu_device_id** | [**str**](.md)| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID need to be unaltered until removal from device.  | [optional] 
 **psu_geo_location** | **str**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] 

### Return type

[**ConsentsResponse201**](ConsentsResponse201.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_consent**
> delete_consent(consent_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Delete Consent

The TPP can delete an account information consent object if needed.

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
api_instance = swagger_client.ConsentServiceApi(swagger_client.ApiClient(configuration))
consent_id = swagger_client.ConsentId() # ConsentId | ID of the corresponding consent object as returned by an Account Information Consent Request. 
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
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
    # Delete Consent
    api_instance.delete_consent(consent_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
except ApiException as e:
    print("Exception when calling ConsentServiceApi->delete_consent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | [**ConsentId**](.md)| ID of the corresponding consent object as returned by an Account Information Consent Request.  | 
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
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

void (empty response body)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consent_authorisation**
> Authorisations get_consent_authorisation(consent_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Get Consent Authorisation Sub-Resources

Return a list of all authorisation subresources IDs which have been created.  This function returns an array of hyperlinks to all generated authorisation sub-resources. 

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
api_instance = swagger_client.ConsentServiceApi(swagger_client.ApiClient(configuration))
consent_id = swagger_client.ConsentId() # ConsentId | ID of the corresponding consent object as returned by an Account Information Consent Request. 
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
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
    # Get Consent Authorisation Sub-Resources
    api_response = api_instance.get_consent_authorisation(consent_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentServiceApi->get_consent_authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | [**ConsentId**](.md)| ID of the corresponding consent object as returned by an Account Information Consent Request.  | 
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
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

[**Authorisations**](Authorisations.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consent_information**
> ConsentInformationResponse200Json get_consent_information(consent_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Get Consent

Returns the content of an account information consent object.  This is returning the data for the TPP especially in cases,  where the consent was directly managed between ASPSP and PSU e.g. in a re-direct SCA Approach. 

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
api_instance = swagger_client.ConsentServiceApi(swagger_client.ApiClient(configuration))
consent_id = swagger_client.ConsentId() # ConsentId | ID of the corresponding consent object as returned by an Account Information Consent Request. 
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
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
    # Get Consent
    api_response = api_instance.get_consent_information(consent_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentServiceApi->get_consent_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | [**ConsentId**](.md)| ID of the corresponding consent object as returned by an Account Information Consent Request.  | 
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
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

[**ConsentInformationResponse200Json**](ConsentInformationResponse200Json.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consent_sca_status**
> ScaStatusResponse get_consent_sca_status(consent_id, authorisation_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Get Consent Authorisation SCA Status

This method returns the SCA status of a consent initiation's authorisation sub-resource. 

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
api_instance = swagger_client.ConsentServiceApi(swagger_client.ApiClient(configuration))
consent_id = swagger_client.ConsentId() # ConsentId | ID of the corresponding consent object as returned by an Account Information Consent Request. 
authorisation_id = swagger_client.AuthorisationId() # AuthorisationId | Resource identification of the related SCA.
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
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
    # Get Consent Authorisation SCA Status
    api_response = api_instance.get_consent_sca_status(consent_id, authorisation_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentServiceApi->get_consent_sca_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | [**ConsentId**](.md)| ID of the corresponding consent object as returned by an Account Information Consent Request.  | 
 **authorisation_id** | [**AuthorisationId**](.md)| Resource identification of the related SCA. | 
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
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

[**ScaStatusResponse**](ScaStatusResponse.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consent_status**
> ConsentStatusResponse200 get_consent_status(consent_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Get Consent Status

Read the status of an account information consent resource.

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
api_instance = swagger_client.ConsentServiceApi(swagger_client.ApiClient(configuration))
consent_id = swagger_client.ConsentId() # ConsentId | ID of the corresponding consent object as returned by an Account Information Consent Request. 
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
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
    # Get Consent Status
    api_response = api_instance.get_consent_status(consent_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentServiceApi->get_consent_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | [**ConsentId**](.md)| ID of the corresponding consent object as returned by an Account Information Consent Request.  | 
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
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

[**ConsentStatusResponse200**](ConsentStatusResponse200.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_consent_authorisation**
> StartScaprocessResponse start_consent_authorisation(x_request_id, x_bic_fi, consent_id, body=body, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, tpp_redirect_preferred=tpp_redirect_preferred, tpp_redirect_uri=tpp_redirect_uri, tpp_nok_redirect_uri=tpp_nok_redirect_uri, tpp_notification_uri=tpp_notification_uri, tpp_notification_content_preferred=tpp_notification_content_preferred, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Start Consent Authorisation Process

Create an authorisation sub-resource and start the authorisation process of a consent.  The message might in addition transmit authentication and authorisation related data.  his method is iterated n times for a n times SCA authorisation in a  corporate context, each creating an own authorisation sub-endpoint for  the corresponding PSU authorising the consent.  The ASPSP might make the usage of this access method unnecessary,  since the related authorisation resource will be automatically created by  the ASPSP after the submission of the consent data with the first POST consents call.  The start authorisation process is a process which is needed for creating a new authorisation  or cancellation sub-resource.   This applies in the following scenarios:    * The ASPSP has indicated with an 'startAuthorisation' hyperlink in the preceding Payment      Initiation Response that an explicit start of the authorisation process is needed by the TPP.      The 'startAuthorisation' hyperlink can transport more information about data which needs to be      uploaded by using the extended forms.     * 'startAuthorisationWithPsuIdentfication',      * 'startAuthorisationWithPsuAuthentication'      * 'startAuthorisationWithEncryptedPsuAuthentication'     * 'startAuthorisationWithAuthentciationMethodSelection'    * The related payment initiation cannot yet be executed since a multilevel SCA is mandated.   * The ASPSP has indicated with an 'startAuthorisation' hyperlink in the preceding      Payment Cancellation Response that an explicit start of the authorisation process is needed by the TPP.      The 'startAuthorisation' hyperlink can transport more information about data which needs to be uploaded      by using the extended forms as indicated above.   * The related payment cancellation request cannot be applied yet since a multilevel SCA is mandate for      executing the cancellation.   * The signing basket needs to be authorised yet. 

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
api_instance = swagger_client.ConsentServiceApi(swagger_client.ApiClient(configuration))
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
consent_id = swagger_client.ConsentId() # ConsentId | ID of the corresponding consent object as returned by an Account Information Consent Request. 
body = swagger_client.ConsentIdAuthorisationsBody() # ConsentIdAuthorisationsBody |  (optional)
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)
psu_id = 'psu_id_example' # str | Client ID of the PSU in the ASPSP client interface. Might be mandated in the ASPSP's documentation. Is not contained if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session.  (optional)
psu_id_type = 'psu_id_type_example' # str | Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | Might be mandated in the ASPSP's documentation. Only used in a corporate context.  (optional)
psu_corporate_id_type = 'psu_corporate_id_type_example' # str | Might be mandated in the ASPSP's documentation. Only used in a corporate context.  (optional)
tpp_redirect_preferred = 'tpp_redirect_preferred_example' # str | If it equals \"true\", the TPP prefers a redirect over an embedded SCA approach. If it equals \"false\", the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  (optional)
tpp_redirect_uri = 'tpp_redirect_uri_example' # str | URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically  when TPP-Redirect-Preferred equals \"true\". It is recommended to always use this header field.  **Remark for Future:**  This field might be changed to mandatory in the next version of the specification.  (optional)
tpp_nok_redirect_uri = 'tpp_nok_redirect_uri_example' # str | If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP.  (optional)
tpp_notification_uri = 'tpp_notification_uri_example' # str | URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  (optional)
tpp_notification_content_preferred = 'tpp_notification_content_preferred_example' # str | The string has the form   status=X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding HTTP request  IP Address field between PSU and TPP.  It shall be contained if and only if this request was actively initiated by the PSU.  (optional)
psu_ip_port = 'psu_ip_port_example' # str | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  (optional)
psu_accept = 'psu_accept_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_accept_charset = 'psu_accept_charset_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_accept_encoding = 'psu_accept_encoding_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_accept_language = 'psu_accept_language_example' # str | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  (optional)
psu_user_agent = 'psu_user_agent_example' # str | The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  (optional)
psu_http_method = 'psu_http_method_example' # str | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  (optional)
psu_device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID need to be unaltered until removal from device.  (optional)
psu_geo_location = 'psu_geo_location_example' # str | The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  (optional)

try:
    # Start Consent Authorisation Process
    api_response = api_instance.start_consent_authorisation(x_request_id, x_bic_fi, consent_id, body=body, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, tpp_redirect_preferred=tpp_redirect_preferred, tpp_redirect_uri=tpp_redirect_uri, tpp_nok_redirect_uri=tpp_nok_redirect_uri, tpp_notification_uri=tpp_notification_uri, tpp_notification_content_preferred=tpp_notification_content_preferred, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentServiceApi->start_consent_authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
 **consent_id** | [**ConsentId**](.md)| ID of the corresponding consent object as returned by an Account Information Consent Request.  | 
 **body** | [**ConsentIdAuthorisationsBody**](ConsentIdAuthorisationsBody.md)|  | [optional] 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 
 **psu_id** | **str**| Client ID of the PSU in the ASPSP client interface. Might be mandated in the ASPSP&#x27;s documentation. Is not contained if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session.  | [optional] 
 **psu_id_type** | **str**| Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  | [optional] 
 **psu_corporate_id** | **str**| Might be mandated in the ASPSP&#x27;s documentation. Only used in a corporate context.  | [optional] 
 **psu_corporate_id_type** | **str**| Might be mandated in the ASPSP&#x27;s documentation. Only used in a corporate context.  | [optional] 
 **tpp_redirect_preferred** | **str**| If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  | [optional] 
 **tpp_redirect_uri** | **str**| URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically  when TPP-Redirect-Preferred equals \&quot;true\&quot;. It is recommended to always use this header field.  **Remark for Future:**  This field might be changed to mandatory in the next version of the specification.  | [optional] 
 **tpp_nok_redirect_uri** | **str**| If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP.  | [optional] 
 **tpp_notification_uri** | **str**| URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  | [optional] 
 **tpp_notification_content_preferred** | **str**| The string has the form   status&#x3D;X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP.  | [optional] 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding HTTP request  IP Address field between PSU and TPP.  It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
 **psu_ip_port** | **str**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] 
 **psu_accept** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_accept_charset** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_accept_encoding** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_accept_language** | **str**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **psu_user_agent** | **str**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] 
 **psu_http_method** | **str**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] 
 **psu_device_id** | [**str**](.md)| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID need to be unaltered until removal from device.  | [optional] 
 **psu_geo_location** | **str**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] 

### Return type

[**StartScaprocessResponse**](StartScaprocessResponse.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_consents_psu_data**
> InlineResponse2002 update_consents_psu_data(x_request_id, x_bic_fi, consent_id, authorisation_id, body=body, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Update PSU Data for Consent

This method update PSU data on the consents  resource if needed.  It may authorise a consent within the Embedded SCA Approach where needed.  Independently from the SCA Approach it supports e.g. the selection of  the authentication method and a non-SCA PSU authentication.  This methods updates PSU data on the cancellation authorisation resource if needed.   There are several possible Update PSU Data requests in the context of a consent request if needed,  which depends on the SCA approach:  * Redirect SCA Approach:   A specific Update PSU Data Request is applicable for      * the selection of authentication methods, before choosing the actual SCA approach. * Decoupled SCA Approach:   A specific Update PSU Data Request is only applicable for   * adding the PSU Identification, if not provided yet in the Payment Initiation Request or the Account Information Consent Request, or if no OAuth2 access token is used, or   * the selection of authentication methods. * Embedded SCA Approach:    The Update PSU Data Request might be used    * to add credentials as a first factor authentication data of the PSU and   * to select the authentication method and   * transaction authorisation.  The SCA Approach might depend on the chosen SCA method.  For that reason, the following possible Update PSU Data request can apply to all SCA approaches:  * Select an SCA method in case of several SCA methods are available for the customer.  There are the following request types on this access path:   * Update PSU Identification   * Update PSU Authentication   * Select PSU Autorization Method      WARNING: This method need a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change.   * Transaction Authorisation     WARNING: This method need a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change. 

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
api_instance = swagger_client.ConsentServiceApi(swagger_client.ApiClient(configuration))
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
consent_id = swagger_client.ConsentId() # ConsentId | ID of the corresponding consent object as returned by an Account Information Consent Request. 
authorisation_id = swagger_client.AuthorisationId() # AuthorisationId | Resource identification of the related SCA.
body = swagger_client.AuthorisationsAuthorisationIdBody1() # AuthorisationsAuthorisationIdBody1 |  (optional)
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)
psu_id = 'psu_id_example' # str | Client ID of the PSU in the ASPSP client interface. Might be mandated in the ASPSP's documentation. Is not contained if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session.  (optional)
psu_id_type = 'psu_id_type_example' # str | Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | Might be mandated in the ASPSP's documentation. Only used in a corporate context.  (optional)
psu_corporate_id_type = 'psu_corporate_id_type_example' # str | Might be mandated in the ASPSP's documentation. Only used in a corporate context.  (optional)
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
    # Update PSU Data for Consent
    api_response = api_instance.update_consents_psu_data(x_request_id, x_bic_fi, consent_id, authorisation_id, body=body, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentServiceApi->update_consents_psu_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
 **consent_id** | [**ConsentId**](.md)| ID of the corresponding consent object as returned by an Account Information Consent Request.  | 
 **authorisation_id** | [**AuthorisationId**](.md)| Resource identification of the related SCA. | 
 **body** | [**AuthorisationsAuthorisationIdBody1**](AuthorisationsAuthorisationIdBody1.md)|  | [optional] 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 
 **psu_id** | **str**| Client ID of the PSU in the ASPSP client interface. Might be mandated in the ASPSP&#x27;s documentation. Is not contained if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session.  | [optional] 
 **psu_id_type** | **str**| Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  | [optional] 
 **psu_corporate_id** | **str**| Might be mandated in the ASPSP&#x27;s documentation. Only used in a corporate context.  | [optional] 
 **psu_corporate_id_type** | **str**| Might be mandated in the ASPSP&#x27;s documentation. Only used in a corporate context.  | [optional] 
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

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

