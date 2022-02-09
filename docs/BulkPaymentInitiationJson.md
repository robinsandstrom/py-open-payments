# BulkPaymentInitiationJson

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_booking_preferred** | [**BatchBookingPreferred**](BatchBookingPreferred.md) |  | [optional] 
**debtor_account** | [**AccountReference**](AccountReference.md) |  | 
**requested_execution_date** | **date** |  | [optional] 
**requested_execution_time** | **datetime** |  | [optional] 
**payments** | [**list[PaymentInitiationBulkElementJson]**](PaymentInitiationBulkElementJson.md) | A list of generic JSON bodies payment initations for bulk payments via JSON.  Note: Some fields from single payments do not occcur in a bulk payment element  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

