# AccountAccess

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**list[AccountReference]**](AccountReference.md) | Is asking for detailed account information.   If the array is empty, the TPP is asking for an accessible account list.  This may be restricted in a PSU/ASPSP authorization dialogue. If the array is empty, also the arrays for balances or transactions shall be empty, if used.  | [optional] 
**balances** | [**list[AccountReference]**](AccountReference.md) | Is asking for balances of the addressed accounts.  If the array is empty, the TPP is asking for the balances of all accessible account lists.  This may be restricted in a PSU/ASPSP authorization dialogue. If the array is empty, also the arrays for accounts or transactions shall be empty, if used.  | [optional] 
**transactions** | [**list[AccountReference]**](AccountReference.md) | Is asking for transactions of the addressed accounts.   If the array is empty, the TPP is asking for the transactions of all accessible account lists.  This may be restricted in a PSU/ASPSP authorization dialogue. If the array is empty, also the arrays for accounts or balances shall be empty, if used.  | [optional] 
**available_accounts** | **str** | Optional if supported by API provider.  Only the values \&quot;allAccounts\&quot; or \&quot;allAccountsWithBalances\&quot; is admitted.  | [optional] 
**all_psd2** | **str** | Optional if supported by API provider.  Only the value \&quot;allAccounts\&quot; is admitted.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

