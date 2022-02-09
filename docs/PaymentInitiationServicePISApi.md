# swagger_client.PaymentInitiationServicePISApi

All URIs are relative to *https://api.sandbox.openbankingplatform.com/psd2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_payment**](PaymentInitiationServicePISApi.md#cancel_payment) | **DELETE** /paymentinitiation/v1/{payment-service}/{payment-product}/{paymentId} | Cancel Payment Initiation
[**get_payment_cancellation_sca_status**](PaymentInitiationServicePISApi.md#get_payment_cancellation_sca_status) | **GET** /paymentinitiation/v1/{payment-service}/{payment-product}/{paymentId}/cancellation-authorisations/{cancellationId} | Get Payment Initiation Cancellation Authorisation SCA Status
[**get_payment_information**](PaymentInitiationServicePISApi.md#get_payment_information) | **GET** /paymentinitiation/v1/{payment-service}/{payment-product}/{paymentId} | Get Payment Initiation
[**get_payment_initiation_authorisation**](PaymentInitiationServicePISApi.md#get_payment_initiation_authorisation) | **GET** /paymentinitiation/v1/{payment-service}/{payment-product}/{paymentId}/authorisations | Get Payment Initiation Authorisation Sub-Resources
[**get_payment_initiation_cancellation_authorisation_information**](PaymentInitiationServicePISApi.md#get_payment_initiation_cancellation_authorisation_information) | **GET** /paymentinitiation/v1/{payment-service}/{payment-product}/{paymentId}/cancellation-authorisations | Get Payment Initiation Cancellation Authorisation Sub-Resources
[**get_payment_initiation_sca_status**](PaymentInitiationServicePISApi.md#get_payment_initiation_sca_status) | **GET** /paymentinitiation/v1/{payment-service}/{payment-product}/{paymentId}/authorisations/{authorisationId} | Get Payment Initiation Authorisation SCA Status
[**get_payment_initiation_status**](PaymentInitiationServicePISApi.md#get_payment_initiation_status) | **GET** /paymentinitiation/v1/{payment-service}/{payment-product}/{paymentId}/status | Get Payment Initiation Status
[**initiate_payment**](PaymentInitiationServicePISApi.md#initiate_payment) | **POST** /paymentinitiation/v1/{payment-service}/{payment-product} | Create Payment Initiation
[**start_payment_authorisation**](PaymentInitiationServicePISApi.md#start_payment_authorisation) | **POST** /paymentinitiation/v1/{payment-service}/{payment-product}/{paymentId}/authorisations | Start Payment Initiation Authorisation Process
[**start_payment_initiation_cancellation_authorisation**](PaymentInitiationServicePISApi.md#start_payment_initiation_cancellation_authorisation) | **POST** /paymentinitiation/v1/{payment-service}/{payment-product}/{paymentId}/cancellation-authorisations | Start Payment Initiation Cancellation Authorisation Process
[**update_payment_cancellation_psu_data**](PaymentInitiationServicePISApi.md#update_payment_cancellation_psu_data) | **PUT** /paymentinitiation/v1/{payment-service}/{payment-product}/{paymentId}/cancellation-authorisations/{cancellationId} | Update PSU Data for Payment Initiation Cancellation
[**update_payment_psu_data**](PaymentInitiationServicePISApi.md#update_payment_psu_data) | **PUT** /paymentinitiation/v1/{payment-service}/{payment-product}/{paymentId}/authorisations/{authorisationId} | Update PSU Data for Payment Initiation

# **cancel_payment**
> PaymentInitiationCancelResponse202 cancel_payment(payment_service, payment_product, payment_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Cancel Payment Initiation

This method initiates the cancellation of a payment.  Depending on the payment-service, the payment-product and the ASPSP's implementation,  this TPP call might be sufficient to cancel a payment.  If an authorisation of the payment cancellation is mandated by the ASPSP,  a corresponding hyperlink will be contained in the response message.  Cancels the addressed payment with resource identification paymentId if applicable to the payment-service, payment-product and received in product related timelines (e.g. before end of business day for scheduled payments of the last business day before the scheduled execution day).   The response to this DELETE command will tell the TPP whether the    * access method was rejected   * access method was successful, or   * access method is generally applicable, but further authorisation processes are needed. 

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
api_instance = swagger_client.PaymentInitiationServicePISApi(swagger_client.ApiClient(configuration))
payment_service = 'payment_service_example' # str | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
payment_product = 'payment_product_example' # str | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro 
payment_id = swagger_client.PaymentId() # PaymentId | Resource identification of the generated payment initiation resource.
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  (optional)
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
    # Cancel Payment Initiation
    api_response = api_instance.cancel_payment(payment_service, payment_product, payment_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->cancel_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service** | **str**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **payment_product** | **str**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro  | 
 **payment_id** | [**PaymentId**](.md)| Resource identification of the generated payment initiation resource. | 
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
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

[**PaymentInitiationCancelResponse202**](PaymentInitiationCancelResponse202.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_cancellation_sca_status**
> ScaStatusResponse get_payment_cancellation_sca_status(payment_service, payment_product, payment_id, cancellation_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Get Payment Initiation Cancellation Authorisation SCA Status

This method returns the SCA status of a payment initiation's authorisation sub-resource. 

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
api_instance = swagger_client.PaymentInitiationServicePISApi(swagger_client.ApiClient(configuration))
payment_service = 'payment_service_example' # str | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
payment_product = 'payment_product_example' # str | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro 
payment_id = swagger_client.PaymentId() # PaymentId | Resource identification of the generated payment initiation resource.
cancellation_id = swagger_client.CancellationId() # CancellationId | Identification for cancellation resource.
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  (optional)
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
    # Get Payment Initiation Cancellation Authorisation SCA Status
    api_response = api_instance.get_payment_cancellation_sca_status(payment_service, payment_product, payment_id, cancellation_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->get_payment_cancellation_sca_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service** | **str**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **payment_product** | **str**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro  | 
 **payment_id** | [**PaymentId**](.md)| Resource identification of the generated payment initiation resource. | 
 **cancellation_id** | [**CancellationId**](.md)| Identification for cancellation resource. | 
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
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

# **get_payment_information**
> InlineResponse200 get_payment_information(payment_service, payment_product, payment_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Get Payment Initiation

Returns the content of a payment object

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
api_instance = swagger_client.PaymentInitiationServicePISApi(swagger_client.ApiClient(configuration))
payment_service = 'payment_service_example' # str | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
payment_product = 'payment_product_example' # str | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro 
payment_id = swagger_client.PaymentId() # PaymentId | Resource identification of the generated payment initiation resource.
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  (optional)
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
    # Get Payment Initiation
    api_response = api_instance.get_payment_information(payment_service, payment_product, payment_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->get_payment_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service** | **str**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **payment_product** | **str**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro  | 
 **payment_id** | [**PaymentId**](.md)| Resource identification of the generated payment initiation resource. | 
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_initiation_authorisation**
> Authorisations get_payment_initiation_authorisation(payment_service, payment_product, payment_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Get Payment Initiation Authorisation Sub-Resources

Read a list of all authorisation subresources IDs which have been created.  This function returns an array of hyperlinks to all generated authorisation sub-resources. 

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
api_instance = swagger_client.PaymentInitiationServicePISApi(swagger_client.ApiClient(configuration))
payment_service = 'payment_service_example' # str | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
payment_product = 'payment_product_example' # str | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro 
payment_id = swagger_client.PaymentId() # PaymentId | Resource identification of the generated payment initiation resource.
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  (optional)
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
    # Get Payment Initiation Authorisation Sub-Resources
    api_response = api_instance.get_payment_initiation_authorisation(payment_service, payment_product, payment_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->get_payment_initiation_authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service** | **str**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **payment_product** | **str**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro  | 
 **payment_id** | [**PaymentId**](.md)| Resource identification of the generated payment initiation resource. | 
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
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

# **get_payment_initiation_cancellation_authorisation_information**
> CancellationList get_payment_initiation_cancellation_authorisation_information(payment_service, payment_product, payment_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Get Payment Initiation Cancellation Authorisation Sub-Resources

Retrieve a list of all created cancellation authorisation sub-resources. 

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
api_instance = swagger_client.PaymentInitiationServicePISApi(swagger_client.ApiClient(configuration))
payment_service = 'payment_service_example' # str | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
payment_product = 'payment_product_example' # str | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro 
payment_id = swagger_client.PaymentId() # PaymentId | Resource identification of the generated payment initiation resource.
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  (optional)
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
    # Get Payment Initiation Cancellation Authorisation Sub-Resources
    api_response = api_instance.get_payment_initiation_cancellation_authorisation_information(payment_service, payment_product, payment_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->get_payment_initiation_cancellation_authorisation_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service** | **str**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **payment_product** | **str**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro  | 
 **payment_id** | [**PaymentId**](.md)| Resource identification of the generated payment initiation resource. | 
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
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

[**CancellationList**](CancellationList.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_initiation_sca_status**
> ScaStatusResponse get_payment_initiation_sca_status(payment_service, payment_product, payment_id, authorisation_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, tpp_redirect_preferred=tpp_redirect_preferred, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Get Payment Initiation Authorisation SCA Status

This method returns the SCA status of a payment initiation's authorisation sub-resource. 

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
api_instance = swagger_client.PaymentInitiationServicePISApi(swagger_client.ApiClient(configuration))
payment_service = 'payment_service_example' # str | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
payment_product = 'payment_product_example' # str | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro 
payment_id = swagger_client.PaymentId() # PaymentId | Resource identification of the generated payment initiation resource.
authorisation_id = swagger_client.AuthorisationId() # AuthorisationId | Resource identification of the related SCA.
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)
tpp_redirect_preferred = 'tpp_redirect_preferred_example' # str | If it equals \"true\", the TPP prefers a redirect over an embedded SCA approach. If it equals \"false\", the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  (optional)
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
    # Get Payment Initiation Authorisation SCA Status
    api_response = api_instance.get_payment_initiation_sca_status(payment_service, payment_product, payment_id, authorisation_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, tpp_redirect_preferred=tpp_redirect_preferred, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->get_payment_initiation_sca_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service** | **str**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **payment_product** | **str**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro  | 
 **payment_id** | [**PaymentId**](.md)| Resource identification of the generated payment initiation resource. | 
 **authorisation_id** | [**AuthorisationId**](.md)| Resource identification of the related SCA. | 
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 
 **tpp_redirect_preferred** | **str**| If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  | [optional] 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
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

[**ScaStatusResponse**](ScaStatusResponse.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_initiation_status**
> PaymentInitiationStatusResponse200Json get_payment_initiation_status(payment_service, payment_product, payment_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Get Payment Initiation Status

Check the transaction status of a payment initiation.

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
api_instance = swagger_client.PaymentInitiationServicePISApi(swagger_client.ApiClient(configuration))
payment_service = 'payment_service_example' # str | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
payment_product = 'payment_product_example' # str | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro 
payment_id = swagger_client.PaymentId() # PaymentId | Resource identification of the generated payment initiation resource.
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  (optional)
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
    # Get Payment Initiation Status
    api_response = api_instance.get_payment_initiation_status(payment_service, payment_product, payment_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->get_payment_initiation_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service** | **str**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **payment_product** | **str**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro  | 
 **payment_id** | [**PaymentId**](.md)| Resource identification of the generated payment initiation resource. | 
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
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

[**PaymentInitiationStatusResponse200Json**](PaymentInitiationStatusResponse200Json.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_payment**
> InlineResponse201 initiate_payment(body, x_request_id, x_bic_fi, psu_ip_address, payment_service, payment_product, x_affiliated_aspsp_id=x_affiliated_aspsp_id, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, consent_id=consent_id, tpp_redirect_preferred=tpp_redirect_preferred, tpp_redirect_uri=tpp_redirect_uri, tpp_nok_redirect_uri=tpp_nok_redirect_uri, tpp_explicit_authorisation_preferred=tpp_explicit_authorisation_preferred, tpp_rejection_no_funds_preferred=tpp_rejection_no_funds_preferred, tpp_notification_uri=tpp_notification_uri, tpp_notification_content_preferred=tpp_notification_content_preferred, psu_ip_port=psu_ip_port, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Create Payment Initiation

This method is used to initiate a payment at the ASPSP.  ## Variants of Payment Initiation Requests  This method to initiate a payment initiation at the ASPSP can be sent with either a JSON body or an pain.001 body depending on the payment product in the path.  There are the following **payment products**:    - Payment products with payment information in *JSON* format:     - ***sepa-credit-transfers***     - ***domestic***     - ***international***     - ***swedish-giro***  Furthermore the request body depends on the **payment-service**   * ***payments***: A single payment initiation request.   * ***bulk-payments***: A collection of several payment iniatiation requests.        In case of a *pain.001* message there are more than one payments contained in the *pain.001 message.          In case of a *JSON* there are several JSON payment blocks contained in a joining list.   * ***periodic-payments***:      Create a standing order initiation resource for recurrent i.e. periodic payments addressable under {paymentId}       with all data relevant for the corresponding payment product and the execution of the standing order contained in a JSON body.   This is the first step in the API to initiate the related recurring/periodic payment.    ## Single and mulitilevel SCA Processes  The Payment Initiation Requests are independent from the need of one ore multilevel  SCA processing, i.e. independent from the number of authorisations needed for the execution of payments.   But the response messages are specific to either one SCA processing or multilevel SCA processing.   For payment initiation with multilevel SCA, this specification requires an explicit start of the authorisation,  i.e. links directly associated with SCA processing like 'scaRedirect' or 'scaOAuth' cannot be contained in the  response message of a Payment Initation Request for a payment, where multiple authorisations are needed.  Also if any data is needed for the next action, like selecting an SCA method is not supported in the response,  since all starts of the multiple authorisations are fully equal.  In these cases, first an authorisation sub-resource has to be generated following the 'startAuthorisation' link. 

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
api_instance = swagger_client.PaymentInitiationServicePISApi(swagger_client.ApiClient(configuration))
body = {
  "$ref" : "#/components/examples/paymentInitiationSctBody_payments_json"
} # object | JSON request body for a payment inition request message 

There are the following payment-products supported:
  * "sepa-credit-transfers" with JSON-Body
  * "domestic" with JSON-Body
  * "international" with JSON-Body
  * "swedish-giro" with JSON-Body
  
There are the following payment-services supported:
  * "payments"
  * "periodic-payments"
  * "bulk-paments"

All optional, conditional and predefined but not yet used fields are defined.

x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
payment_service = 'payment_service_example' # str | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
payment_product = 'payment_product_example' # str | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro 
x_affiliated_aspsp_id = 'x_affiliated_aspsp_id_example' # str | The ID of an affiliated ASPSP as related to the X-BicFi header  (optional)
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)
psu_id = 'psu_id_example' # str | Client ID of the PSU in the ASPSP client interface. Might be mandated in the ASPSP's documentation. Is not contained if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session.  (optional)
psu_id_type = 'psu_id_type_example' # str | Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | Might be mandated in the ASPSP's documentation. Only used in a corporate context.  (optional)
psu_corporate_id_type = 'psu_corporate_id_type_example' # str | Might be mandated in the ASPSP's documentation. Only used in a corporate context.  (optional)
consent_id = swagger_client.ConsentId() # ConsentId | This data element may be contained, if the payment initiation transaction is part of a session, i.e. combined AIS/PIS service. This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation.  (optional)
tpp_redirect_preferred = 'tpp_redirect_preferred_example' # str | If it equals \"true\", the TPP prefers a redirect over an embedded SCA approach. If it equals \"false\", the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  (optional)
tpp_redirect_uri = 'tpp_redirect_uri_example' # str | URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically  when TPP-Redirect-Preferred equals \"true\". It is recommended to always use this header field.  **Remark for Future:**  This field might be changed to mandatory in the next version of the specification.  (optional)
tpp_nok_redirect_uri = 'tpp_nok_redirect_uri_example' # str | If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP.  (optional)
tpp_explicit_authorisation_preferred = 'tpp_explicit_authorisation_preferred_example' # str | If it equals \"true\", the TPP prefers to start the authorisation process separately,  e.g. because of the usage of a signing basket.  This preference might be ignored by the ASPSP, if a signing basket is not supported as functionality.  If it equals \"false\" or if the parameter is not used, there is no preference of the TPP.  This especially indicates that the TPP assumes a direct authorisation of the transaction in the next step,  without using a signing basket.  (optional)
tpp_rejection_no_funds_preferred = 'tpp_rejection_no_funds_preferred_example' # str | If it equals \"true\" then the TPP prefers a rejection of the payment initiation in case the ASPSP is  providing an integrated confirmation of funds request an the result of this is that not sufficient  funds are available.  If it equals \"false\" then the TPP prefers that the ASPSP is dealing with the payment initiation like  in the ASPSPs online channel, potentially waiting for a certain time period for funds to arrive to initiate the payment.  This parameter might be ignored by the ASPSP.  (optional)
tpp_notification_uri = 'tpp_notification_uri_example' # str | URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  (optional)
tpp_notification_content_preferred = 'tpp_notification_content_preferred_example' # str | The string has the form   status=X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP.  (optional)
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
    # Create Payment Initiation
    api_response = api_instance.initiate_payment(body, x_request_id, x_bic_fi, psu_ip_address, payment_service, payment_product, x_affiliated_aspsp_id=x_affiliated_aspsp_id, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, consent_id=consent_id, tpp_redirect_preferred=tpp_redirect_preferred, tpp_redirect_uri=tpp_redirect_uri, tpp_nok_redirect_uri=tpp_nok_redirect_uri, tpp_explicit_authorisation_preferred=tpp_explicit_authorisation_preferred, tpp_rejection_no_funds_preferred=tpp_rejection_no_funds_preferred, tpp_notification_uri=tpp_notification_uri, tpp_notification_content_preferred=tpp_notification_content_preferred, psu_ip_port=psu_ip_port, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->initiate_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON request body for a payment inition request message 

There are the following payment-products supported:
  * &quot;sepa-credit-transfers&quot; with JSON-Body
  * &quot;domestic&quot; with JSON-Body
  * &quot;international&quot; with JSON-Body
  * &quot;swedish-giro&quot; with JSON-Body
  
There are the following payment-services supported:
  * &quot;payments&quot;
  * &quot;periodic-payments&quot;
  * &quot;bulk-paments&quot;

All optional, conditional and predefined but not yet used fields are defined.
 | 
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | 
 **payment_service** | **str**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **payment_product** | **str**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro  | 
 **x_affiliated_aspsp_id** | **str**| The ID of an affiliated ASPSP as related to the X-BicFi header  | [optional] 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 
 **psu_id** | **str**| Client ID of the PSU in the ASPSP client interface. Might be mandated in the ASPSP&#x27;s documentation. Is not contained if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session.  | [optional] 
 **psu_id_type** | **str**| Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  | [optional] 
 **psu_corporate_id** | **str**| Might be mandated in the ASPSP&#x27;s documentation. Only used in a corporate context.  | [optional] 
 **psu_corporate_id_type** | **str**| Might be mandated in the ASPSP&#x27;s documentation. Only used in a corporate context.  | [optional] 
 **consent_id** | [**ConsentId**](.md)| This data element may be contained, if the payment initiation transaction is part of a session, i.e. combined AIS/PIS service. This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation.  | [optional] 
 **tpp_redirect_preferred** | **str**| If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  | [optional] 
 **tpp_redirect_uri** | **str**| URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically  when TPP-Redirect-Preferred equals \&quot;true\&quot;. It is recommended to always use this header field.  **Remark for Future:**  This field might be changed to mandatory in the next version of the specification.  | [optional] 
 **tpp_nok_redirect_uri** | **str**| If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP.  | [optional] 
 **tpp_explicit_authorisation_preferred** | **str**| If it equals \&quot;true\&quot;, the TPP prefers to start the authorisation process separately,  e.g. because of the usage of a signing basket.  This preference might be ignored by the ASPSP, if a signing basket is not supported as functionality.  If it equals \&quot;false\&quot; or if the parameter is not used, there is no preference of the TPP.  This especially indicates that the TPP assumes a direct authorisation of the transaction in the next step,  without using a signing basket.  | [optional] 
 **tpp_rejection_no_funds_preferred** | **str**| If it equals \&quot;true\&quot; then the TPP prefers a rejection of the payment initiation in case the ASPSP is  providing an integrated confirmation of funds request an the result of this is that not sufficient  funds are available.  If it equals \&quot;false\&quot; then the TPP prefers that the ASPSP is dealing with the payment initiation like  in the ASPSPs online channel, potentially waiting for a certain time period for funds to arrive to initiate the payment.  This parameter might be ignored by the ASPSP.  | [optional] 
 **tpp_notification_uri** | **str**| URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  | [optional] 
 **tpp_notification_content_preferred** | **str**| The string has the form   status&#x3D;X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP.  | [optional] 
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

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_payment_authorisation**
> StartScaprocessResponse start_payment_authorisation(x_request_id, x_bic_fi, payment_service, payment_product, payment_id, body=body, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, tpp_redirect_preferred=tpp_redirect_preferred, tpp_redirect_uri=tpp_redirect_uri, tpp_nok_redirect_uri=tpp_nok_redirect_uri, tpp_notification_uri=tpp_notification_uri, tpp_notification_content_preferred=tpp_notification_content_preferred, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Start Payment Initiation Authorisation Process

Create an authorisation sub-resource and start the authorisation process.  The message might in addition transmit authentication and authorisation related data.   This method is iterated n times for a n times SCA authorisation in a  corporate context, each creating an own authorisation sub-endpoint for  the corresponding PSU authorising the transaction.  The ASPSP might make the usage of this access method unnecessary in case  of only one SCA process needed, since the related authorisation resource  might be automatically created by the ASPSP after the submission of the  payment data with the first POST payments/{payment-product} call.  The start authorisation process is a process which is needed for creating a new authorisation  or cancellation sub-resource.   This applies in the following scenarios:    * The ASPSP has indicated with an 'startAuthorisation' hyperlink in the preceding Payment      Initiation Response that an explicit start of the authorisation process is needed by the TPP.      The 'startAuthorisation' hyperlink can transport more information about data which needs to be      uploaded by using the extended forms.     * 'startAuthorisationWithPsuIdentfication',      * 'startAuthorisationWithPsuAuthentication'      * 'startAuthorisationWithEncryptedPsuAuthentication'     * 'startAuthorisationWithAuthentciationMethodSelection'    * The related payment initiation cannot yet be executed since a multilevel SCA is mandated.   * The ASPSP has indicated with an 'startAuthorisation' hyperlink in the preceding      Payment Cancellation Response that an explicit start of the authorisation process is needed by the TPP.      The 'startAuthorisation' hyperlink can transport more information about data which needs to be uploaded      by using the extended forms as indicated above.   * The related payment cancellation request cannot be applied yet since a multilevel SCA is mandate for      executing the cancellation.   * The signing basket needs to be authorised yet. 

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
api_instance = swagger_client.PaymentInitiationServicePISApi(swagger_client.ApiClient(configuration))
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
payment_service = 'payment_service_example' # str | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
payment_product = 'payment_product_example' # str | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro 
payment_id = swagger_client.PaymentId() # PaymentId | Resource identification of the generated payment initiation resource.
body = swagger_client.PaymentIdAuthorisationsBody() # PaymentIdAuthorisationsBody |  (optional)
psu_id = 'psu_id_example' # str | Client ID of the PSU in the ASPSP client interface. Might be mandated in the ASPSP's documentation. Is not contained if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session.  (optional)
psu_id_type = 'psu_id_type_example' # str | Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | Might be mandated in the ASPSP's documentation. Only used in a corporate context.  (optional)
psu_corporate_id_type = 'psu_corporate_id_type_example' # str | Might be mandated in the ASPSP's documentation. Only used in a corporate context.  (optional)
tpp_redirect_preferred = 'tpp_redirect_preferred_example' # str | If it equals \"true\", the TPP prefers a redirect over an embedded SCA approach. If it equals \"false\", the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  (optional)
tpp_redirect_uri = 'tpp_redirect_uri_example' # str | URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically  when TPP-Redirect-Preferred equals \"true\". It is recommended to always use this header field.  **Remark for Future:**  This field might be changed to mandatory in the next version of the specification.  (optional)
tpp_nok_redirect_uri = 'tpp_nok_redirect_uri_example' # str | If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP.  (optional)
tpp_notification_uri = 'tpp_notification_uri_example' # str | URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  (optional)
tpp_notification_content_preferred = 'tpp_notification_content_preferred_example' # str | The string has the form   status=X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP.  (optional)
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  (optional)
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
    # Start Payment Initiation Authorisation Process
    api_response = api_instance.start_payment_authorisation(x_request_id, x_bic_fi, payment_service, payment_product, payment_id, body=body, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, tpp_redirect_preferred=tpp_redirect_preferred, tpp_redirect_uri=tpp_redirect_uri, tpp_nok_redirect_uri=tpp_nok_redirect_uri, tpp_notification_uri=tpp_notification_uri, tpp_notification_content_preferred=tpp_notification_content_preferred, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->start_payment_authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
 **payment_service** | **str**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **payment_product** | **str**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro  | 
 **payment_id** | [**PaymentId**](.md)| Resource identification of the generated payment initiation resource. | 
 **body** | [**PaymentIdAuthorisationsBody**](PaymentIdAuthorisationsBody.md)|  | [optional] 
 **psu_id** | **str**| Client ID of the PSU in the ASPSP client interface. Might be mandated in the ASPSP&#x27;s documentation. Is not contained if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session.  | [optional] 
 **psu_id_type** | **str**| Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  | [optional] 
 **psu_corporate_id** | **str**| Might be mandated in the ASPSP&#x27;s documentation. Only used in a corporate context.  | [optional] 
 **psu_corporate_id_type** | **str**| Might be mandated in the ASPSP&#x27;s documentation. Only used in a corporate context.  | [optional] 
 **tpp_redirect_preferred** | **str**| If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  | [optional] 
 **tpp_redirect_uri** | **str**| URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically  when TPP-Redirect-Preferred equals \&quot;true\&quot;. It is recommended to always use this header field.  **Remark for Future:**  This field might be changed to mandatory in the next version of the specification.  | [optional] 
 **tpp_nok_redirect_uri** | **str**| If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP.  | [optional] 
 **tpp_notification_uri** | **str**| URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  | [optional] 
 **tpp_notification_content_preferred** | **str**| The string has the form   status&#x3D;X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP.  | [optional] 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
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

# **start_payment_initiation_cancellation_authorisation**
> StartScaprocessResponse start_payment_initiation_cancellation_authorisation(payment_service, payment_product, payment_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, tpp_redirect_preferred=tpp_redirect_preferred, tpp_redirect_uri=tpp_redirect_uri, tpp_nok_redirect_uri=tpp_nok_redirect_uri, tpp_notification_uri=tpp_notification_uri, tpp_notification_content_preferred=tpp_notification_content_preferred, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Start Payment Initiation Cancellation Authorisation Process

Creates an authorisation sub-resource and start the authorisation process of the cancellation of the addressed payment.  The message might in addition transmit authentication and authorisation related data.  This method is iterated n times for a n times SCA authorisation in a  corporate context, each creating an own authorisation sub-endpoint for  the corresponding PSU authorising the cancellation-authorisation.  The ASPSP might make the usage of this access method unnecessary in case  of only one SCA process needed, since the related authorisation resource  might be automatically created by the ASPSP after the submission of the  payment data with the first POST payments/{payment-product} call.  The start authorisation process is a process which is needed for creating a new authorisation  or cancellation sub-resource.   This applies in the following scenarios:    * The ASPSP has indicated with an 'startAuthorisation' hyperlink in the preceding Payment      Initiation Response that an explicit start of the authorisation process is needed by the TPP.      The 'startAuthorisation' hyperlink can transport more information about data which needs to be      uploaded by using the extended forms.     * 'startAuthorisationWithPsuIdentfication',      * 'startAuthorisationWithPsuAuthentication'      * 'startAuthorisationWithAuthentciationMethodSelection'    * The related payment initiation cannot yet be executed since a multilevel SCA is mandated.   * The ASPSP has indicated with an 'startAuthorisation' hyperlink in the preceding      Payment Cancellation Response that an explicit start of the authorisation process is needed by the TPP.      The 'startAuthorisation' hyperlink can transport more information about data which needs to be uploaded      by using the extended forms as indicated above.   * The related payment cancellation request cannot be applied yet since a multilevel SCA is mandate for      executing the cancellation.   * The signing basket needs to be authorised yet. 

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
api_instance = swagger_client.PaymentInitiationServicePISApi(swagger_client.ApiClient(configuration))
payment_service = 'payment_service_example' # str | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
payment_product = 'payment_product_example' # str | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro 
payment_id = swagger_client.PaymentId() # PaymentId | Resource identification of the generated payment initiation resource.
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
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
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  (optional)
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
    # Start Payment Initiation Cancellation Authorisation Process
    api_response = api_instance.start_payment_initiation_cancellation_authorisation(payment_service, payment_product, payment_id, x_request_id, x_bic_fi, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, tpp_redirect_preferred=tpp_redirect_preferred, tpp_redirect_uri=tpp_redirect_uri, tpp_nok_redirect_uri=tpp_nok_redirect_uri, tpp_notification_uri=tpp_notification_uri, tpp_notification_content_preferred=tpp_notification_content_preferred, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->start_payment_initiation_cancellation_authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service** | **str**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **payment_product** | **str**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro  | 
 **payment_id** | [**PaymentId**](.md)| Resource identification of the generated payment initiation resource. | 
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
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
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
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

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_cancellation_psu_data**
> InlineResponse2002 update_payment_cancellation_psu_data(x_request_id, x_bic_fi, payment_service, payment_product, payment_id, cancellation_id, body=body, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Update PSU Data for Payment Initiation Cancellation

This method updates PSU data on the cancellation authorisation resource if needed.  It may authorise a cancellation of the payment within the Embedded SCA Approach where needed.  Independently from the SCA Approach it supports e.g. the selection of  the authentication method and a non-SCA PSU authentication.  This methods updates PSU data on the cancellation authorisation resource if needed.   There are several possible Update PSU Data requests in the context of a cancellation authorisation within the payment initiation services needed,  which depends on the SCA approach:  * Redirect SCA Approach:   A specific Update PSU Data Request is applicable for      * the selection of authentication methods, before choosing the actual SCA approach. * Decoupled SCA Approach:   A specific Update PSU Data Request is only applicable for   * adding the PSU Identification, if not provided yet in the Payment Initiation Request or the Account Information Consent Request, or if no OAuth2 access token is used, or   * the selection of authentication methods. * Embedded SCA Approach:    The Update PSU Data Request might be used    * to add credentials as a first factor authentication data of the PSU and   * to select the authentication method and   * transaction authorisation.  The SCA Approach might depend on the chosen SCA method.  For that reason, the following possible Update PSU Data request can apply to all SCA approaches:  * Select an SCA method in case of several SCA methods are available for the customer.  There are the following request types on this access path:   * Update PSU Identification   * Update PSU Authentication   * Select PSU Autorization Method      WARNING: This method need a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change.   * Transaction Authorisation     WARNING: This method need a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change. 

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
api_instance = swagger_client.PaymentInitiationServicePISApi(swagger_client.ApiClient(configuration))
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
payment_service = 'payment_service_example' # str | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
payment_product = 'payment_product_example' # str | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro 
payment_id = swagger_client.PaymentId() # PaymentId | Resource identification of the generated payment initiation resource.
cancellation_id = swagger_client.CancellationId() # CancellationId | Identification for cancellation resource.
body = swagger_client.CancellationauthorisationsCancellationIdBody() # CancellationauthorisationsCancellationIdBody |  (optional)
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)
psu_id = 'psu_id_example' # str | Client ID of the PSU in the ASPSP client interface. Might be mandated in the ASPSP's documentation. Is not contained if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session.  (optional)
psu_id_type = 'psu_id_type_example' # str | Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | Might be mandated in the ASPSP's documentation. Only used in a corporate context.  (optional)
psu_corporate_id_type = 'psu_corporate_id_type_example' # str | Might be mandated in the ASPSP's documentation. Only used in a corporate context.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  (optional)
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
    # Update PSU Data for Payment Initiation Cancellation
    api_response = api_instance.update_payment_cancellation_psu_data(x_request_id, x_bic_fi, payment_service, payment_product, payment_id, cancellation_id, body=body, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->update_payment_cancellation_psu_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
 **payment_service** | **str**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **payment_product** | **str**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro  | 
 **payment_id** | [**PaymentId**](.md)| Resource identification of the generated payment initiation resource. | 
 **cancellation_id** | [**CancellationId**](.md)| Identification for cancellation resource. | 
 **body** | [**CancellationauthorisationsCancellationIdBody**](CancellationauthorisationsCancellationIdBody.md)|  | [optional] 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 
 **psu_id** | **str**| Client ID of the PSU in the ASPSP client interface. Might be mandated in the ASPSP&#x27;s documentation. Is not contained if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session.  | [optional] 
 **psu_id_type** | **str**| Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  | [optional] 
 **psu_corporate_id** | **str**| Might be mandated in the ASPSP&#x27;s documentation. Only used in a corporate context.  | [optional] 
 **psu_corporate_id_type** | **str**| Might be mandated in the ASPSP&#x27;s documentation. Only used in a corporate context.  | [optional] 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
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

# **update_payment_psu_data**
> InlineResponse2002 update_payment_psu_data(x_request_id, x_bic_fi, payment_service, payment_product, payment_id, authorisation_id, body=body, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)

Update PSU Data for Payment Initiation

This methods updates PSU data on the authorisation resource if needed.  It may authorise a payment within the Embedded SCA Approach where needed.  Independently from the SCA Approach it supports e.g. the selection of  the authentication method and a non-SCA PSU authentication.  There are several possible Update PSU Data requests in the context of payment initiation services needed,  which depends on the SCA approach:  * Redirect SCA Approach:   A specific Update PSU Data Request is applicable for      * the selection of authentication methods, before choosing the actual SCA approach. * Decoupled SCA Approach:   A specific Update PSU Data Request is only applicable for   * adding the PSU Identification, if not provided yet in the Payment Initiation Request or the Account Information Consent Request, or if no OAuth2 access token is used, or   * the selection of authentication methods. * Embedded SCA Approach:    The Update PSU Data Request might be used    * to add credentials as a first factor authentication data of the PSU and   * to select the authentication method and   * transaction authorisation.  The SCA Approach might depend on the chosen SCA method.  For that reason, the following possible Update PSU Data request can apply to all SCA approaches:  * Select an SCA method in case of several SCA methods are available for the customer.  There are the following request types on this access path:   * Update PSU Identification   * Update PSU Authentication   * Select PSU Autorization Method      WARNING: This method need a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change.   * Transaction Authorisation     WARNING: This method need a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change. 

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
api_instance = swagger_client.PaymentInitiationServicePISApi(swagger_client.ApiClient(configuration))
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
x_bic_fi = 'x_bic_fi_example' # str | BICFI
payment_service = 'payment_service_example' # str | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
payment_product = 'payment_product_example' # str | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro 
payment_id = swagger_client.PaymentId() # PaymentId | Resource identification of the generated payment initiation resource.
authorisation_id = swagger_client.AuthorisationId() # AuthorisationId | Resource identification of the related SCA.
body = swagger_client.AuthorisationsAuthorisationIdBody() # AuthorisationsAuthorisationIdBody |  (optional)
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)
psu_id = 'psu_id_example' # str | Client ID of the PSU in the ASPSP client interface. Might be mandated in the ASPSP's documentation. Is not contained if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session.  (optional)
psu_id_type = 'psu_id_type_example' # str | Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | Might be mandated in the ASPSP's documentation. Only used in a corporate context.  (optional)
psu_corporate_id_type = 'psu_corporate_id_type_example' # str | Might be mandated in the ASPSP's documentation. Only used in a corporate context.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  (optional)
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
    # Update PSU Data for Payment Initiation
    api_response = api_instance.update_payment_psu_data(x_request_id, x_bic_fi, payment_service, payment_product, payment_id, authorisation_id, body=body, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, tpp_redirect_preferred=tpp_redirect_preferred, psu_accept=psu_accept, psu_accept_charset=psu_accept_charset, psu_accept_encoding=psu_accept_encoding, psu_accept_language=psu_accept_language, psu_user_agent=psu_user_agent, psu_http_method=psu_http_method, psu_device_id=psu_device_id, psu_geo_location=psu_geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->update_payment_psu_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **x_bic_fi** | **str**| BICFI | 
 **payment_service** | **str**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **payment_product** | **str**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT).  The following payment products are supported:   - sepa-credit-transfers   - domestic   - international   - swedish-giro  | 
 **payment_id** | [**PaymentId**](.md)| Resource identification of the generated payment initiation resource. | 
 **authorisation_id** | [**AuthorisationId**](.md)| Resource identification of the related SCA. | 
 **body** | [**AuthorisationsAuthorisationIdBody**](AuthorisationsAuthorisationIdBody.md)|  | [optional] 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 
 **psu_id** | **str**| Client ID of the PSU in the ASPSP client interface. Might be mandated in the ASPSP&#x27;s documentation. Is not contained if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session.  | [optional] 
 **psu_id_type** | **str**| Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  | [optional] 
 **psu_corporate_id** | **str**| Might be mandated in the ASPSP&#x27;s documentation. Only used in a corporate context.  | [optional] 
 **psu_corporate_id_type** | **str**| Might be mandated in the ASPSP&#x27;s documentation. Only used in a corporate context.  | [optional] 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
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

