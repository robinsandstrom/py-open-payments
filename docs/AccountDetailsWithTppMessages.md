# AccountDetailsWithTppMessages

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | This shall be filled, if addressable resource are created by the ASPSP on the /accounts or /card-accounts endpoint. | [optional] 
**iban** | [**Iban**](Iban.md) |  | [optional] 
**bban** | [**Bban**](Bban.md) |  | [optional] 
**msisdn** | [**Msisdn**](Msisdn.md) |  | [optional] 
**bankgiro_number** | [**BankGiroNumber**](BankGiroNumber.md) |  | [optional] 
**plusgiro_number** | [**PlusGiroNumber**](PlusGiroNumber.md) |  | [optional] 
**currency** | [**CurrencyCode**](CurrencyCode.md) |  | 
**name** | **str** | Name of the account given by the bank or the PSU in online-banking. | [optional] 
**product** | **str** | Product name of the bank for this account, proprietary definition. | [optional] 
**cash_account_type** | [**CashAccountType**](CashAccountType.md) |  | [optional] 
**status** | [**AccountStatus**](AccountStatus.md) |  | [optional] 
**bic** | [**Bicfi**](Bicfi.md) |  | [optional] 
**linked_accounts** | **str** | Case of a set of pending card transactions, the APSP will provide the relevant cash account the card is set up on. | [optional] 
**usage** | **str** | Specifies the usage of the account   * PRIV: private personal account   * ORGA: professional account  | [optional] 
**details** | **str** | Specifications that might be provided by the ASPSP   - characteristics of the account   - characteristics of the relevant card  | [optional] 
**balances** | [**BalanceList**](BalanceList.md) |  | [optional] 
**links** | [**LinksAccountDetails**](LinksAccountDetails.md) |  | [optional] 
**owner_name** | **str** | Name of the legal account owner.  If there is more than one owner, then e.g. two names might be noted here.  For a corporate account, the corporate name is used for this attribute. Even if supported by the ASPSP, the provision of this field might depend on the fact whether an explicit consent to this specific additional account information has been given by the PSU.  | [optional] 
**clearing_number** | [**ClearingNumber**](ClearingNumber.md) |  | [optional] 
**tpp_messages** | [**list[TppMessage2XX]**](TppMessage2XX.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

