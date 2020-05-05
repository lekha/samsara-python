# HosLogEntry

A single HOS log entry.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codrivers** | [**list[DriverTinyResponse]**](DriverTinyResponse.md) | The codriver information. | [optional] 
**end_time** | **str** | UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | [optional] 
**hos_status_type** | **str** | The Hours of Service status type. | [optional] 
**id** | **float** | The unique Samsara ID of the HOS log. This is automatically generated when the Driver object is created. It cannot be changed. | 
**log_recorded_location** | [**Location**](Location.md) |  | [optional] 
**remark** | **str** | Remark associated with the log entry. | [optional] 
**start_time** | **str** | UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | 
**vehicle** | [**VehicleTinyResponse**](VehicleTinyResponse.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

