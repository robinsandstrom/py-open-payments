# swagger_client.ASPSPInformationServiceASPSPISApi

All URIs are relative to *https://api.sandbox.openbankingplatform.com/psd2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aspsp_details**](ASPSPInformationServiceASPSPISApi.md#get_aspsp_details) | **GET** /aspspinformation/v1/aspsps/{bicFi} | Get ASPSP Details
[**get_aspsp_list**](ASPSPInformationServiceASPSPISApi.md#get_aspsp_list) | **GET** /aspspinformation/v1/aspsps | Get ASPSP List
[**get_city_details**](ASPSPInformationServiceASPSPISApi.md#get_city_details) | **GET** /aspspinformation/v1/cities/{city-id} | Get City Details
[**get_city_list**](ASPSPInformationServiceASPSPISApi.md#get_city_list) | **GET** /aspspinformation/v1/cities | Get City List
[**get_countries_list**](ASPSPInformationServiceASPSPISApi.md#get_countries_list) | **GET** /aspspinformation/v1/countries | Get Country List
[**get_country_details**](ASPSPInformationServiceASPSPISApi.md#get_country_details) | **GET** /aspspinformation/v1/countries/{isoCountryCode} | Get Country Details

# **get_aspsp_details**
> Aspsp get_aspsp_details(bic_fi, x_request_id, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate)

Get ASPSP Details

Gets details about an ASPSP by ID. 

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
api_instance = swagger_client.ASPSPInformationServiceASPSPISApi(swagger_client.ApiClient(configuration))
bic_fi = 'bic_fi_example' # str | The BICFI of the ASPSP 
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)

try:
    # Get ASPSP Details
    api_response = api_instance.get_aspsp_details(bic_fi, x_request_id, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ASPSPInformationServiceASPSPISApi->get_aspsp_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bic_fi** | **str**| The BICFI of the ASPSP  | 
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 

### Return type

[**Aspsp**](Aspsp.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aspsp_list**
> AspspList get_aspsp_list(x_request_id, iso_country_codes=iso_country_codes, city_ids=city_ids, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate)

Get ASPSP List

Gets all ASPSPs currently supported in the Open Banking Platform. 

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
api_instance = swagger_client.ASPSPInformationServiceASPSPISApi(swagger_client.ApiClient(configuration))
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
iso_country_codes = swagger_client.IsoCountryCodes() # IsoCountryCodes | ISO Country Codes for the countries to get ASPSPs for  (optional)
city_ids = swagger_client.CityIds() # CityIds | City IDs for the countries to get ASPSPs for  (optional)
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)

try:
    # Get ASPSP List
    api_response = api_instance.get_aspsp_list(x_request_id, iso_country_codes=iso_country_codes, city_ids=city_ids, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ASPSPInformationServiceASPSPISApi->get_aspsp_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **iso_country_codes** | [**IsoCountryCodes**](.md)| ISO Country Codes for the countries to get ASPSPs for  | [optional] 
 **city_ids** | [**CityIds**](.md)| City IDs for the countries to get ASPSPs for  | [optional] 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 

### Return type

[**AspspList**](AspspList.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_city_details**
> City get_city_details(city_id, x_request_id, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate)

Get City Details

Gets a city by ID 

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
api_instance = swagger_client.ASPSPInformationServiceASPSPISApi(swagger_client.ApiClient(configuration))
city_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the city 
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)

try:
    # Get City Details
    api_response = api_instance.get_city_details(city_id, x_request_id, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ASPSPInformationServiceASPSPISApi->get_city_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city_id** | [**str**](.md)| The ID of the city  | 
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 

### Return type

[**City**](City.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_city_list**
> CityList get_city_list(x_request_id, iso_country_codes=iso_country_codes, city_ids=city_ids, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate)

Get City List

Gets all cities currently supported in the Open Banking Platform. 

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
api_instance = swagger_client.ASPSPInformationServiceASPSPISApi(swagger_client.ApiClient(configuration))
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
iso_country_codes = swagger_client.IsoCountryCodes() # IsoCountryCodes | ISO Country Codes for the countries to get ASPSPs for  (optional)
city_ids = swagger_client.CityIds() # CityIds | City IDs for the countries to get ASPSPs for  (optional)
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)

try:
    # Get City List
    api_response = api_instance.get_city_list(x_request_id, iso_country_codes=iso_country_codes, city_ids=city_ids, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ASPSPInformationServiceASPSPISApi->get_city_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **iso_country_codes** | [**IsoCountryCodes**](.md)| ISO Country Codes for the countries to get ASPSPs for  | [optional] 
 **city_ids** | [**CityIds**](.md)| City IDs for the countries to get ASPSPs for  | [optional] 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 

### Return type

[**CityList**](CityList.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_countries_list**
> CountryList get_countries_list(x_request_id, iso_country_codes=iso_country_codes, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate)

Get Country List

Gets all countries currently supported in the Open Banking Platform. 

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
api_instance = swagger_client.ASPSPInformationServiceASPSPISApi(swagger_client.ApiClient(configuration))
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
iso_country_codes = swagger_client.IsoCountryCodes() # IsoCountryCodes | ISO Country Codes for the countries to get ASPSPs for  (optional)
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)

try:
    # Get Country List
    api_response = api_instance.get_countries_list(x_request_id, iso_country_codes=iso_country_codes, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ASPSPInformationServiceASPSPISApi->get_countries_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **iso_country_codes** | [**IsoCountryCodes**](.md)| ISO Country Codes for the countries to get ASPSPs for  | [optional] 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 

### Return type

[**CountryList**](CountryList.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_country_details**
> City get_country_details(iso_country_code, x_request_id, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate)

Get Country Details

Gets a country by ISO Country Code 

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
api_instance = swagger_client.ASPSPInformationServiceASPSPISApi(swagger_client.ApiClient(configuration))
iso_country_code = 'iso_country_code_example' # str | ISO Country Code for the country 
x_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request. (optional)
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.  (optional)
tpp_signature_certificate = 'B' # str | The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  (optional)

try:
    # Get Country Details
    api_response = api_instance.get_country_details(iso_country_code, x_request_id, digest=digest, signature=signature, tpp_signature_certificate=tpp_signature_certificate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ASPSPInformationServiceASPSPISApi->get_country_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iso_country_code** | **str**| ISO Country Code for the country  | 
 **x_request_id** | [**str**](.md)| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding.  Must be contained if a signature is contained.  | [optional] 

### Return type

[**City**](City.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

