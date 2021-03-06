# AssetCreate

The asset creation arguments
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_metadata** | **dict(str, str)** | The custom fields of an asset. | [optional] 
**location** | [**AssetLocation**](AssetLocation.md) |  | [optional] 
**location_data_input_id** | **str** | Required if locationType is \&quot;dataInput\&quot;. Specifies the id of a location data input which will determine the asset&#39;s location. **The data input will be moved to the new asset.** | [optional] 
**location_type** | [**LocationType**](LocationType.md) |  | [optional] 
**name** | **str** | The name of the asset. | 
**parent_id** | **str** | The id of the parent asset that the asset belongs to. | [optional] 
**running_status_data_input_id** | **str** | The asset&#39;s isRunning status will be true when the associated data input&#39;s value is 1. Data input cannot be of location format. **The data input will be moved to the new asset.** | [optional] 
**tag_ids** | **list[str]** | The ids of the tags that the asset should belong to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


