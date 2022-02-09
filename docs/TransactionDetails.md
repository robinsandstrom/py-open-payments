# TransactionDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | the Transaction Id can be used as access-ID in the API, where more details on an transaction is offered.  If this data attribute is provided this shows that the AIS can get access on more details about this  transaction using the GET Transaction Details Request   | [optional] 
**entry_reference** | **str** | Is the identification of the transaction as used e.g. for reference for deltafunction on application level.  The same identification as for example used within camt.05x messages.  | [optional] 
**end_to_end_id** | **str** | Unique end to end identity. | [optional] 
**mandate_id** | **str** | Identification of Mandates, e.g. a SEPA Mandate ID. | [optional] 
**check_id** | **str** | Identification of a Cheque. | [optional] 
**creditor_id** | **str** | Identification of Creditors, e.g. a SEPA Creditor ID. | [optional] 
**booking_date** | [**BookingDate**](BookingDate.md) |  | [optional] 
**value_date** | **date** | The Date at which assets become available to the account owner in case of a credit. | [optional] 
**transaction_amount** | [**Amount**](Amount.md) |  | 
**currency_exchange** | [**ReportExchangeRateList**](ReportExchangeRateList.md) |  | [optional] 
**creditor_name** | [**CreditorName**](CreditorName.md) |  | [optional] 
**creditor_account** | [**TrnsCreditorAccountReference**](TrnsCreditorAccountReference.md) |  | [optional] 
**ultimate_creditor** | [**UltimateCreditor**](UltimateCreditor.md) |  | [optional] 
**debtor_name** | [**DebtorName**](DebtorName.md) |  | [optional] 
**debtor_account** | [**AccountReference**](AccountReference.md) |  | [optional] 
**ultimate_debtor** | [**UltimateDebtor**](UltimateDebtor.md) |  | [optional] 
**remittance_information_unstructured** | [**RemittanceInformationUnstructured**](RemittanceInformationUnstructured.md) |  | [optional] 
**remittance_information_structured** | **str** | Reference as contained in the structured remittance reference structure (without the surrounding XML structure).  Different from other places the content is containt in plain form not in form of a structered field.  | [optional] 
**additional_information** | **str** | Might be used by the ASPSP to transport additional transaction related information to the PSU.  | [optional] 
**purpose_code** | [**PurposeCode**](PurposeCode.md) |  | [optional] 
**bank_transaction_code** | [**BankTransactionCode**](BankTransactionCode.md) |  | [optional] 
**proprietary_bank_transaction_code** | [**ProprietaryBankTransactionCode**](ProprietaryBankTransactionCode.md) |  | [optional] 
**transaction_list_id** | [**TransactionListId**](TransactionListId.md) |  | [optional] 
**links** | [**LinksTransactionDetails**](LinksTransactionDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

