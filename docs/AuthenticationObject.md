# AuthenticationObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_type** | [**AuthenticationType**](AuthenticationType.md) |  | 
**authentication_version** | **str** | Depending on the \&quot;authenticationType\&quot;. This version can be used by differentiating authentication tools used within performing OTP generation in the same authentication type. This version can be referred to in the ASPSP?s documentation.  | [optional] 
**authentication_method_id** | [**AuthenticationMethodId**](AuthenticationMethodId.md) |  | 
**name** | **str** | This is the name of the authentication method defined by the PSU in the Online Banking frontend of the ASPSP. Alternatively this could be a description provided by the ASPSP like \&quot;SMS OTP on phone +49160 xxxxx 28\&quot;. This name shall be used by the TPP when presenting a list of authentication methods to the PSU, if available.  | [optional] 
**explanation** | **str** | Detailed information about the SCA method for the PSU.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

