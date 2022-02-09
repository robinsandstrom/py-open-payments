# PaymentInitiationJson

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_to_end_identification** | **str** |  | [optional] 
**debtor_account** | [**AccountReferenceWithGiro**](AccountReferenceWithGiro.md) |  | 
**instructed_amount** | [**Amount**](Amount.md) |  | 
**creditor_account** | [**AccountReference**](AccountReference.md) |  | 
**creditor_agent** | [**Bicfi**](Bicfi.md) |  | [optional] 
**creditor_agent_name** | [**CreditorAgentName**](CreditorAgentName.md) |  | [optional] 
**creditor_name** | [**CreditorName**](CreditorName.md) |  | 
**creditor_address** | [**Address**](Address.md) |  | [optional] 
**remittance_information_unstructured** | [**RemittanceInformationUnstructured**](RemittanceInformationUnstructured.md) |  | [optional] 
**requested_execution_date** | **str** | Date when payment is scheduled to be executed in ISO-Date Format, e.g. 2020-10-30 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

