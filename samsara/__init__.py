# coding: utf-8

# flake8: noqa

"""
    Samsara API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2020-06-15
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from samsara.api.samsara_api import SamsaraApi

# import ApiClient
from samsara.api_client import ApiClient
from samsara.configuration import Configuration
from samsara.exceptions import OpenApiException
from samsara.exceptions import ApiTypeError
from samsara.exceptions import ApiValueError
from samsara.exceptions import ApiKeyError
from samsara.exceptions import ApiException
# import models into sdk package
from samsara.models.address import Address
from samsara.models.address_geofence import AddressGeofence
from samsara.models.address_geofence_circle import AddressGeofenceCircle
from samsara.models.address_geofence_polygon import AddressGeofencePolygon
from samsara.models.address_geofence_polygon_vertices import AddressGeofencePolygonVertices
from samsara.models.address_response import AddressResponse
from samsara.models.asset_create import AssetCreate
from samsara.models.asset_location import AssetLocation
from samsara.models.asset_patch import AssetPatch
from samsara.models.asset_response import AssetResponse
from samsara.models.asset_response_location_data_input import AssetResponseLocationDataInput
from samsara.models.asset_response_parent_asset import AssetResponseParentAsset
from samsara.models.asset_response_running_status_data_input import AssetResponseRunningStatusDataInput
from samsara.models.attribute import Attribute
from samsara.models.attribute_entity import AttributeEntity
from samsara.models.attribute_expanded import AttributeExpanded
from samsara.models.attribute_expanded_all_of import AttributeExpandedAllOf
from samsara.models.attribute_expanded_response import AttributeExpandedResponse
from samsara.models.attribute_response import AttributeResponse
from samsara.models.attribute_tiny import AttributeTiny
from samsara.models.carrier_proposed_assignment import CarrierProposedAssignment
from samsara.models.carrier_proposed_assignment_driver import CarrierProposedAssignmentDriver
from samsara.models.carrier_proposed_assignment_response import CarrierProposedAssignmentResponse
from samsara.models.carrier_proposed_assignment_vehicle import CarrierProposedAssignmentVehicle
from samsara.models.contact import Contact
from samsara.models.contact_response import ContactResponse
from samsara.models.contact_tiny_response import ContactTinyResponse
from samsara.models.create_address_request import CreateAddressRequest
from samsara.models.create_address_request_geofence import CreateAddressRequestGeofence
from samsara.models.create_attribute_request import CreateAttributeRequest
from samsara.models.create_attribute_request_entities import CreateAttributeRequestEntities
from samsara.models.create_carrier_proposed_assignment_request import CreateCarrierProposedAssignmentRequest
from samsara.models.create_contact_request import CreateContactRequest
from samsara.models.create_driver_request import CreateDriverRequest
from samsara.models.create_driver_request_attributes import CreateDriverRequestAttributes
from samsara.models.create_driver_request_carrier_settings import CreateDriverRequestCarrierSettings
from samsara.models.create_dvir_request import CreateDvirRequest
from samsara.models.create_tag_request import CreateTagRequest
from samsara.models.create_user_request import CreateUserRequest
from samsara.models.create_user_request_roles import CreateUserRequestRoles
from samsara.models.current_duty_status import CurrentDutyStatus
from samsara.models.data_input_list_response import DataInputListResponse
from samsara.models.data_input_response import DataInputResponse
from samsara.models.data_input_response_all_of import DataInputResponseAllOf
from samsara.models.data_input_snapshot import DataInputSnapshot
from samsara.models.data_input_snapshot_all_of import DataInputSnapshotAllOf
from samsara.models.data_input_snapshot_response import DataInputSnapshotResponse
from samsara.models.data_input_tiny_response import DataInputTinyResponse
from samsara.models.data_inputs_tiny_response import DataInputsTinyResponse
from samsara.models.defect import Defect
from samsara.models.defect_patch import DefectPatch
from samsara.models.defect_resolved_by import DefectResolvedBy
from samsara.models.defect_response import DefectResponse
from samsara.models.defects_response import DefectsResponse
from samsara.models.document_pdf_generation_request import DocumentPdfGenerationRequest
from samsara.models.document_pdf_generation_response import DocumentPdfGenerationResponse
from samsara.models.document_pdf_generation_response_data import DocumentPdfGenerationResponseData
from samsara.models.document_pdf_query_response import DocumentPdfQueryResponse
from samsara.models.document_pdf_query_response_data import DocumentPdfQueryResponseData
from samsara.models.driver import Driver
from samsara.models.driver_activation_status import DriverActivationStatus
from samsara.models.driver_carrier_settings import DriverCarrierSettings
from samsara.models.driver_efficiencies_response import DriverEfficienciesResponse
from samsara.models.driver_efficiencies_response_data import DriverEfficienciesResponseData
from samsara.models.driver_efficiency import DriverEfficiency
from samsara.models.driver_eld_ruleset import DriverEldRuleset
from samsara.models.driver_eld_ruleset_cycle import DriverEldRulesetCycle
from samsara.models.driver_eld_ruleset_daily_off_duty import DriverEldRulesetDailyOffDuty
from samsara.models.driver_eld_ruleset_rest_break import DriverEldRulesetRestBreak
from samsara.models.driver_eld_ruleset_restart import DriverEldRulesetRestart
from samsara.models.driver_eld_ruleset_shift import DriverEldRulesetShift
from samsara.models.driver_eld_ruleset_us_short_haul_type import DriverEldRulesetUsShortHaulType
from samsara.models.driver_eld_settings import DriverEldSettings
from samsara.models.driver_locale import DriverLocale
from samsara.models.driver_response import DriverResponse
from samsara.models.driver_static_assigned_vehicle import DriverStaticAssignedVehicle
from samsara.models.driver_tachograph_activity_response import DriverTachographActivityResponse
from samsara.models.driver_tiny_response import DriverTinyResponse
from samsara.models.driver_vehicle_group_tag import DriverVehicleGroupTag
from samsara.models.dvir import Dvir
from samsara.models.dvir_author_signature import DvirAuthorSignature
from samsara.models.dvir_response import DvirResponse
from samsara.models.dvir_second_signature import DvirSecondSignature
from samsara.models.dvir_signature import DvirSignature
from samsara.models.dvir_third_signature import DvirThirdSignature
from samsara.models.dvir_trailer import DvirTrailer
from samsara.models.dvir_trailer_defects_items import DvirTrailerDefectsItems
from samsara.models.dvir_vehicle import DvirVehicle
from samsara.models.dvirs_list_response import DvirsListResponse
from samsara.models.equipment import Equipment
from samsara.models.equipment_engine_rpm import EquipmentEngineRpm
from samsara.models.equipment_engine_seconds import EquipmentEngineSeconds
from samsara.models.equipment_engine_state import EquipmentEngineState
from samsara.models.equipment_fuel_percent import EquipmentFuelPercent
from samsara.models.equipment_gateway_engine_seconds import EquipmentGatewayEngineSeconds
from samsara.models.equipment_gateway_engine_state import EquipmentGatewayEngineState
from samsara.models.equipment_gateway_j1939_engine_seconds import EquipmentGatewayJ1939EngineSeconds
from samsara.models.equipment_gps_odometer_meters import EquipmentGpsOdometerMeters
from samsara.models.equipment_list_response import EquipmentListResponse
from samsara.models.equipment_location import EquipmentLocation
from samsara.models.equipment_locations_list_response import EquipmentLocationsListResponse
from samsara.models.equipment_locations_list_response_data import EquipmentLocationsListResponseData
from samsara.models.equipment_locations_response import EquipmentLocationsResponse
from samsara.models.equipment_locations_response_data import EquipmentLocationsResponseData
from samsara.models.equipment_obd_engine_seconds import EquipmentObdEngineSeconds
from samsara.models.equipment_obd_engine_state import EquipmentObdEngineState
from samsara.models.equipment_response import EquipmentResponse
from samsara.models.equipment_stats_list_response import EquipmentStatsListResponse
from samsara.models.equipment_stats_list_response_data import EquipmentStatsListResponseData
from samsara.models.equipment_stats_response import EquipmentStatsResponse
from samsara.models.equipment_stats_response_data import EquipmentStatsResponseData
from samsara.models.extended_driver_tiny_response import ExtendedDriverTinyResponse
from samsara.models.fft_spectra_data_point import FftSpectraDataPoint
from samsara.models.fft_spectra_data_point_fft_spectra import FftSpectraDataPointFftSpectra
from samsara.models.get_attributes_by_entity_type_response import GetAttributesByEntityTypeResponse
from samsara.models.get_route_feed_response import GetRouteFeedResponse
from samsara.models.hos_break import HosBreak
from samsara.models.hos_clocks import HosClocks
from samsara.models.hos_clocks_for_driver import HosClocksForDriver
from samsara.models.hos_clocks_response import HosClocksResponse
from samsara.models.hos_cycle import HosCycle
from samsara.models.hos_drive import HosDrive
from samsara.models.hos_log_entry import HosLogEntry
from samsara.models.hos_logs_for_driver import HosLogsForDriver
from samsara.models.hos_logs_response import HosLogsResponse
from samsara.models.hos_shift import HosShift
from samsara.models.hos_status_type import HosStatusType
from samsara.models.hos_violations import HosViolations
from samsara.models.inline_response200 import InlineResponse200
from samsara.models.j1939_d1_status_data_point import J1939D1StatusDataPoint
from samsara.models.j1939_d1_status_data_point_value import J1939D1StatusDataPointValue
from samsara.models.list_addresses_response import ListAddressesResponse
from samsara.models.list_carrier_proposed_assignment_response import ListCarrierProposedAssignmentResponse
from samsara.models.list_contacts_response import ListContactsResponse
from samsara.models.list_drivers_response import ListDriversResponse
from samsara.models.list_industrial_assets_response import ListIndustrialAssetsResponse
from samsara.models.list_tags_response import ListTagsResponse
from samsara.models.list_user_roles_response import ListUserRolesResponse
from samsara.models.list_users_response import ListUsersResponse
from samsara.models.list_vehicles_response import ListVehiclesResponse
from samsara.models.location import Location
from samsara.models.location_data_point import LocationDataPoint
from samsara.models.location_data_point_gps_location import LocationDataPointGpsLocation
from samsara.models.location_data_point_gps_location_place import LocationDataPointGpsLocationPlace
from samsara.models.location_type import LocationType
from samsara.models.minimal_route import MinimalRoute
from samsara.models.minimal_route_stop import MinimalRouteStop
from samsara.models.number_data_point import NumberDataPoint
from samsara.models.organization_info import OrganizationInfo
from samsara.models.organization_info_carrier_settings import OrganizationInfoCarrierSettings
from samsara.models.organization_info_response import OrganizationInfoResponse
from samsara.models.pagination_response import PaginationResponse
from samsara.models.parent_tag import ParentTag
from samsara.models.patch_tag_request import PatchTagRequest
from samsara.models.replace_tag_request import ReplaceTagRequest
from samsara.models.resolved_by import ResolvedBy
from samsara.models.route_tiny_response import RouteTinyResponse
from samsara.models.safety_event import SafetyEvent
from samsara.models.safety_event_behavior_label import SafetyEventBehaviorLabel
from samsara.models.safety_event_behavior_label_source import SafetyEventBehaviorLabelSource
from samsara.models.safety_event_behavior_label_type import SafetyEventBehaviorLabelType
from samsara.models.safety_event_coaching_state import SafetyEventCoachingState
from samsara.models.safety_event_driver import SafetyEventDriver
from samsara.models.safety_event_location import SafetyEventLocation
from samsara.models.safety_event_vehicle import SafetyEventVehicle
from samsara.models.safety_events_list_response import SafetyEventsListResponse
from samsara.models.standard_error_response import StandardErrorResponse
from samsara.models.string_data_point import StringDataPoint
from samsara.models.tachograph_activity import TachographActivity
from samsara.models.tachograph_activity_list_wrapper import TachographActivityListWrapper
from samsara.models.tachograph_driver_file import TachographDriverFile
from samsara.models.tachograph_driver_file_list_wrapper import TachographDriverFileListWrapper
from samsara.models.tachograph_driver_files_response import TachographDriverFilesResponse
from samsara.models.tachograph_vehicle_file import TachographVehicleFile
from samsara.models.tachograph_vehicle_file_list_wrapper import TachographVehicleFileListWrapper
from samsara.models.tachograph_vehicle_files_response import TachographVehicleFilesResponse
from samsara.models.tag import Tag
from samsara.models.tag_all_of import TagAllOf
from samsara.models.tag_response import TagResponse
from samsara.models.tag_tiny_response import TagTinyResponse
from samsara.models.tagged_object import TaggedObject
from samsara.models.tiny_tag import TinyTag
from samsara.models.trailer_name_only_response import TrailerNameOnlyResponse
from samsara.models.trailer_tiny_response import TrailerTinyResponse
from samsara.models.update_address_request import UpdateAddressRequest
from samsara.models.update_attribute_request import UpdateAttributeRequest
from samsara.models.update_contact_request import UpdateContactRequest
from samsara.models.update_driver_request import UpdateDriverRequest
from samsara.models.update_dvir_request import UpdateDvirRequest
from samsara.models.update_user_request import UpdateUserRequest
from samsara.models.update_vehicle_request import UpdateVehicleRequest
from samsara.models.user import User
from samsara.models.user_auth_type import UserAuthType
from samsara.models.user_response import UserResponse
from samsara.models.user_role import UserRole
from samsara.models.user_role_assignment import UserRoleAssignment
from samsara.models.user_role_assignment_request import UserRoleAssignmentRequest
from samsara.models.user_tiny_response import UserTinyResponse
from samsara.models.vehicle import Vehicle
from samsara.models.vehicle_aux_input_type import VehicleAuxInputType
from samsara.models.vehicle_aux_input_type1 import VehicleAuxInputType1
from samsara.models.vehicle_aux_input_type10 import VehicleAuxInputType10
from samsara.models.vehicle_aux_input_type2 import VehicleAuxInputType2
from samsara.models.vehicle_aux_input_type3 import VehicleAuxInputType3
from samsara.models.vehicle_aux_input_type4 import VehicleAuxInputType4
from samsara.models.vehicle_aux_input_type5 import VehicleAuxInputType5
from samsara.models.vehicle_aux_input_type6 import VehicleAuxInputType6
from samsara.models.vehicle_aux_input_type7 import VehicleAuxInputType7
from samsara.models.vehicle_aux_input_type8 import VehicleAuxInputType8
from samsara.models.vehicle_aux_input_type9 import VehicleAuxInputType9
from samsara.models.vehicle_harsh_acceleration_setting_type import VehicleHarshAccelerationSettingType
from samsara.models.vehicle_location import VehicleLocation
from samsara.models.vehicle_location_reverse_geo import VehicleLocationReverseGeo
from samsara.models.vehicle_location_time import VehicleLocationTime
from samsara.models.vehicle_locations_list_response import VehicleLocationsListResponse
from samsara.models.vehicle_locations_list_response_data import VehicleLocationsListResponseData
from samsara.models.vehicle_locations_response import VehicleLocationsResponse
from samsara.models.vehicle_locations_response_data import VehicleLocationsResponseData
from samsara.models.vehicle_response import VehicleResponse
from samsara.models.vehicle_static_assigned_driver import VehicleStaticAssignedDriver
from samsara.models.vehicle_stats_ambient_air_temp_milli_c import VehicleStatsAmbientAirTempMilliC
from samsara.models.vehicle_stats_ambient_air_temp_milli_c_with_decoration import VehicleStatsAmbientAirTempMilliCWithDecoration
from samsara.models.vehicle_stats_aux_input import VehicleStatsAuxInput
from samsara.models.vehicle_stats_aux_input_decoration import VehicleStatsAuxInputDecoration
from samsara.models.vehicle_stats_aux_input_with_decoration import VehicleStatsAuxInputWithDecoration
from samsara.models.vehicle_stats_barometric_pressure_pa import VehicleStatsBarometricPressurePa
from samsara.models.vehicle_stats_barometric_pressure_pa_with_decoration import VehicleStatsBarometricPressurePaWithDecoration
from samsara.models.vehicle_stats_battery_voltage import VehicleStatsBatteryVoltage
from samsara.models.vehicle_stats_battery_voltage_with_decoration import VehicleStatsBatteryVoltageWithDecoration
from samsara.models.vehicle_stats_decorations import VehicleStatsDecorations
from samsara.models.vehicle_stats_decorations_ambient_air_temperature_milli_c import VehicleStatsDecorationsAmbientAirTemperatureMilliC
from samsara.models.vehicle_stats_decorations_barometric_pressure_pa import VehicleStatsDecorationsBarometricPressurePa
from samsara.models.vehicle_stats_decorations_battery_milli_volts import VehicleStatsDecorationsBatteryMilliVolts
from samsara.models.vehicle_stats_decorations_def_level_milli_percent import VehicleStatsDecorationsDefLevelMilliPercent
from samsara.models.vehicle_stats_decorations_ecu_speed_mph import VehicleStatsDecorationsEcuSpeedMph
from samsara.models.vehicle_stats_decorations_engine_coolant_temperature_milli_c import VehicleStatsDecorationsEngineCoolantTemperatureMilliC
from samsara.models.vehicle_stats_decorations_engine_load_percent import VehicleStatsDecorationsEngineLoadPercent
from samsara.models.vehicle_stats_decorations_engine_oil_pressure_k_pa import VehicleStatsDecorationsEngineOilPressureKPa
from samsara.models.vehicle_stats_decorations_engine_rpm import VehicleStatsDecorationsEngineRpm
from samsara.models.vehicle_stats_decorations_engine_states import VehicleStatsDecorationsEngineStates
from samsara.models.vehicle_stats_decorations_fuel_percents import VehicleStatsDecorationsFuelPercents
from samsara.models.vehicle_stats_decorations_gps import VehicleStatsDecorationsGps
from samsara.models.vehicle_stats_decorations_gps_distance_meters import VehicleStatsDecorationsGpsDistanceMeters
from samsara.models.vehicle_stats_decorations_gps_odometer_meters import VehicleStatsDecorationsGpsOdometerMeters
from samsara.models.vehicle_stats_decorations_intake_manifold_temperature_milli_c import VehicleStatsDecorationsIntakeManifoldTemperatureMilliC
from samsara.models.vehicle_stats_decorations_obd_engine_seconds import VehicleStatsDecorationsObdEngineSeconds
from samsara.models.vehicle_stats_decorations_obd_odometer_meters import VehicleStatsDecorationsObdOdometerMeters
from samsara.models.vehicle_stats_def_level_milli_percent import VehicleStatsDefLevelMilliPercent
from samsara.models.vehicle_stats_def_level_milli_percent_with_decoration import VehicleStatsDefLevelMilliPercentWithDecoration
from samsara.models.vehicle_stats_ecu_speed_mph import VehicleStatsEcuSpeedMph
from samsara.models.vehicle_stats_ecu_speed_mph_with_decoration import VehicleStatsEcuSpeedMphWithDecoration
from samsara.models.vehicle_stats_engine_coolant_temp_milli_c import VehicleStatsEngineCoolantTempMilliC
from samsara.models.vehicle_stats_engine_coolant_temp_milli_c_with_decoration import VehicleStatsEngineCoolantTempMilliCWithDecoration
from samsara.models.vehicle_stats_engine_load_percent import VehicleStatsEngineLoadPercent
from samsara.models.vehicle_stats_engine_load_percent_with_decoration import VehicleStatsEngineLoadPercentWithDecoration
from samsara.models.vehicle_stats_engine_oil_pressure_k_pa import VehicleStatsEngineOilPressureKPa
from samsara.models.vehicle_stats_engine_oil_pressure_k_pa_with_decoration import VehicleStatsEngineOilPressureKPaWithDecoration
from samsara.models.vehicle_stats_engine_rpm import VehicleStatsEngineRpm
from samsara.models.vehicle_stats_engine_rpm_with_decoration import VehicleStatsEngineRpmWithDecoration
from samsara.models.vehicle_stats_engine_state import VehicleStatsEngineState
from samsara.models.vehicle_stats_engine_state_setting import VehicleStatsEngineStateSetting
from samsara.models.vehicle_stats_engine_state_with_decoration import VehicleStatsEngineStateWithDecoration
from samsara.models.vehicle_stats_fault_codes import VehicleStatsFaultCodes
from samsara.models.vehicle_stats_fault_codes_ignition_type import VehicleStatsFaultCodesIgnitionType
from samsara.models.vehicle_stats_fault_codes_j1939 import VehicleStatsFaultCodesJ1939
from samsara.models.vehicle_stats_fault_codes_j1939_lights import VehicleStatsFaultCodesJ1939Lights
from samsara.models.vehicle_stats_fault_codes_j1939_trouble_code import VehicleStatsFaultCodesJ1939TroubleCode
from samsara.models.vehicle_stats_fault_codes_obdii import VehicleStatsFaultCodesOBDII
from samsara.models.vehicle_stats_fault_codes_obdii_trouble_code import VehicleStatsFaultCodesOBDIITroubleCode
from samsara.models.vehicle_stats_fault_codes_passenger_dtc import VehicleStatsFaultCodesPassengerDtc
from samsara.models.vehicle_stats_fault_codes_passenger_monitor_status import VehicleStatsFaultCodesPassengerMonitorStatus
from samsara.models.vehicle_stats_fault_codes_passenger_monitor_status_value import VehicleStatsFaultCodesPassengerMonitorStatusValue
from samsara.models.vehicle_stats_fault_codes_value import VehicleStatsFaultCodesValue
from samsara.models.vehicle_stats_fault_codes_value_j1939 import VehicleStatsFaultCodesValueJ1939
from samsara.models.vehicle_stats_fault_codes_value_j1939_check_engine_lights import VehicleStatsFaultCodesValueJ1939CheckEngineLights
from samsara.models.vehicle_stats_fault_codes_value_j1939_diagnostic_trouble_codes import VehicleStatsFaultCodesValueJ1939DiagnosticTroubleCodes
from samsara.models.vehicle_stats_fault_codes_value_j1939_vendor_specific_fields import VehicleStatsFaultCodesValueJ1939VendorSpecificFields
from samsara.models.vehicle_stats_fault_codes_value_obdii import VehicleStatsFaultCodesValueObdii
from samsara.models.vehicle_stats_fault_codes_value_obdii_confirmed_dtcs import VehicleStatsFaultCodesValueObdiiConfirmedDtcs
from samsara.models.vehicle_stats_fault_codes_value_obdii_diagnostic_trouble_codes import VehicleStatsFaultCodesValueObdiiDiagnosticTroubleCodes
from samsara.models.vehicle_stats_fault_codes_value_obdii_monitor_status import VehicleStatsFaultCodesValueObdiiMonitorStatus
from samsara.models.vehicle_stats_fault_codes_vendor_specific_fields import VehicleStatsFaultCodesVendorSpecificFields
from samsara.models.vehicle_stats_fault_codes_with_decoration import VehicleStatsFaultCodesWithDecoration
from samsara.models.vehicle_stats_fuel_percent import VehicleStatsFuelPercent
from samsara.models.vehicle_stats_fuel_percent_with_decoration import VehicleStatsFuelPercentWithDecoration
from samsara.models.vehicle_stats_gps import VehicleStatsGps
from samsara.models.vehicle_stats_gps_distance_meters import VehicleStatsGpsDistanceMeters
from samsara.models.vehicle_stats_gps_distance_meters_with_decoration import VehicleStatsGpsDistanceMetersWithDecoration
from samsara.models.vehicle_stats_gps_odometer_meters import VehicleStatsGpsOdometerMeters
from samsara.models.vehicle_stats_gps_odometer_meters_with_decoration import VehicleStatsGpsOdometerMetersWithDecoration
from samsara.models.vehicle_stats_intake_manifold_temp_milli_c import VehicleStatsIntakeManifoldTempMilliC
from samsara.models.vehicle_stats_intake_manifold_temp_milli_c_with_decoration import VehicleStatsIntakeManifoldTempMilliCWithDecoration
from samsara.models.vehicle_stats_list_gps import VehicleStatsListGps
from samsara.models.vehicle_stats_list_response import VehicleStatsListResponse
from samsara.models.vehicle_stats_list_response_data import VehicleStatsListResponseData
from samsara.models.vehicle_stats_list_synthetic_engine_seconds import VehicleStatsListSyntheticEngineSeconds
from samsara.models.vehicle_stats_nfc_card_scan import VehicleStatsNfcCardScan
from samsara.models.vehicle_stats_nfc_card_scan_card import VehicleStatsNfcCardScanCard
from samsara.models.vehicle_stats_nfc_card_scan_with_decoration import VehicleStatsNfcCardScanWithDecoration
from samsara.models.vehicle_stats_obd_engine_seconds import VehicleStatsObdEngineSeconds
from samsara.models.vehicle_stats_obd_engine_seconds_with_decoration import VehicleStatsObdEngineSecondsWithDecoration
from samsara.models.vehicle_stats_obd_odometer_meters import VehicleStatsObdOdometerMeters
from samsara.models.vehicle_stats_obd_odometer_meters_with_decoration import VehicleStatsObdOdometerMetersWithDecoration
from samsara.models.vehicle_stats_response import VehicleStatsResponse
from samsara.models.vehicle_stats_response_data import VehicleStatsResponseData
from samsara.models.vehicle_stats_synthetic_engine_seconds import VehicleStatsSyntheticEngineSeconds
from samsara.models.vehicle_stats_time import VehicleStatsTime
from samsara.models.vehicle_stats_tire_pressure import VehicleStatsTirePressure
from samsara.models.vehicle_stats_tire_pressure_with_decoration import VehicleStatsTirePressureWithDecoration
from samsara.models.vehicle_stats_tire_pressures import VehicleStatsTirePressures
from samsara.models.vehicle_summary import VehicleSummary
from samsara.models.vehicle_tiny_response import VehicleTinyResponse

