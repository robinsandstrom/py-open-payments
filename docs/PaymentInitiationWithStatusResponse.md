# PaymentInitiationWithStatusResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_to_end_identification** | **str** |  | [optional] 
**debtor_account** | [**AccountReference**](AccountReference.md) |  | 
**instructed_amount** | [**Amount**](Amount.md) |  | 
**creditor_account** | [**AccountReference**](AccountReference.md) |  | 
**creditor_agent** | [**Bicfi**](Bicfi.md) |  | [optional] 
**creditor_name** | [**CreditorName**](CreditorName.md) |  | 
**creditor_address** | [**Address**](Address.md) |  | [optional] 
**remittance_information_unstructured** | [**RemittanceInformationUnstructured**](RemittanceInformationUnstructured.md) |  | [optional] 
**remittance_information_structured** | [**RemittanceInformationStructured**](RemittanceInformationStructured.md) |  | [optional] 
**requested_execution_date** | **str** | Date when payment is scheduled to be executed in ISO-Date Format, e.g. 2020-10-30 | [optional] 
**transaction_status** | [**TransactionStatus**](TransactionStatus.md) |  | [optional] 
**tpp_messages** | [**list[TppMessage2XX]**](TppMessage2XX.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

