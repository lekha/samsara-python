# VehicleStatsResponseData

A vehicle and its most recent stat.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aux_input1** | [**VehicleStatsAuxInput**](VehicleStatsAuxInput.md) |  | [optional] 
**aux_input2** | [**VehicleStatsAuxInput**](VehicleStatsAuxInput.md) |  | [optional] 
**battery_milli_volts** | [**VehicleStatsBatteryVoltage**](VehicleStatsBatteryVoltage.md) |  | [optional] 
**engine_rpm** | [**VehicleStatsEngineRpm**](VehicleStatsEngineRpm.md) |  | [optional] 
**engine_state** | [**VehicleStatsEngineState**](VehicleStatsEngineState.md) |  | [optional] 
**fault_codes** | [**VehicleStatsFaultCodes**](VehicleStatsFaultCodes.md) |  | [optional] 
**fuel_percent** | [**VehicleStatsFuelPercent**](VehicleStatsFuelPercent.md) |  | [optional] 
**gps** | [**VehicleStatsGps**](VehicleStatsGps.md) |  | [optional] 
**gps_distance_meters** | [**VehicleStatsGpsDistanceMeters**](VehicleStatsGpsDistanceMeters.md) |  | [optional] 
**gps_odometer_meters** | [**VehicleStatsGpsOdometerMeters**](VehicleStatsGpsOdometerMeters.md) |  | [optional] 
**id** | **str** | The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed. | 
**name** | **str** | The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time. | 
**nfc_card_scan** | [**VehicleStatsNfcCardScan**](VehicleStatsNfcCardScan.md) |  | [optional] 
**obd_engine_seconds** | [**VehicleStatsObdEngineSeconds**](VehicleStatsObdEngineSeconds.md) |  | [optional] 
**obd_odometer_meters** | [**VehicleStatsObdOdometerMeters**](VehicleStatsObdOdometerMeters.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


