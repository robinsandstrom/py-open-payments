# PaymentInitationRequestResponse201

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_status** | [**TransactionStatus**](TransactionStatus.md) |  | 
**payment_id** | [**PaymentId**](PaymentId.md) |  | 
**transaction_fees** | [**Amount**](Amount.md) |  | [optional] 
**transaction_fee_indicator** | [**TransactionFeeIndicator**](TransactionFeeIndicator.md) |  | [optional] 
**requested_execution_date** | **str** | Date when payment is scheduled to be executed in ISO-Date Format, e.g. 2020-10-30 | [optional] 
**remittance_information_structured** | [**RemittanceInformationStructured**](RemittanceInformationStructured.md) |  | [optional] 
**sca_methods** | [**ScaMethods**](ScaMethods.md) |  | [optional] 
**chosen_sca_method** | [**AuthenticationObject**](AuthenticationObject.md) |  | [optional] 
**challenge_data** | [**ChallengeData**](ChallengeData.md) |  | [optional] 
**links** | [**LinksPaymentInitiation**](LinksPaymentInitiation.md) |  | 
**psu_message** | [**PsuMessageText**](PsuMessageText.md) |  | [optional] 
**tpp_messages** | [**list[TppMessage2XX]**](TppMessage2XX.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

