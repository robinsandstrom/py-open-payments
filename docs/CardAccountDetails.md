# CardAccountDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | This is the data element to be used in the path when retrieving data from a dedicated account. This shall be filled, if addressable resource are created by the ASPSP on the /card-accounts endpoint.  | [optional] 
**masked_pan** | [**MaskedPan**](MaskedPan.md) |  | 
**currency** | [**CurrencyCode**](CurrencyCode.md) |  | 
**name** | **str** | Name of the account given by the bank or the PSU in online-banking. | [optional] 
**product** | **str** | Product name of the bank for this account, proprietary definition. | [optional] 
**status** | [**AccountStatus**](AccountStatus.md) |  | [optional] 
**usage** | **str** | Specifies the usage of the account   * PRIV: private personal account   * ORGA: professional account  | [optional] 
**details** | **str** | Specifications that might be provided by the ASPSP   - characteristics of the account   - characteristics of the relevant card  | [optional] 
**credit_limit** | [**Amount**](Amount.md) |  | [optional] 
**balances** | [**BalanceList**](BalanceList.md) |  | [optional] 
**links** | [**LinksAccountDetails**](LinksAccountDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

