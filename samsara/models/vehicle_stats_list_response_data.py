# coding: utf-8

"""
    Samsara API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2020-06-15
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from samsara.configuration import Configuration


class VehicleStatsListResponseData(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'ambient_air_temperature_milli_c': 'list[VehicleStatsAmbientAirTempMilliCWithDecoration]',
        'aux_input1': 'list[VehicleStatsAuxInputWithDecoration]',
        'aux_input10': 'list[VehicleStatsAuxInputWithDecoration]',
        'aux_input2': 'list[VehicleStatsAuxInputWithDecoration]',
        'aux_input3': 'list[VehicleStatsAuxInputWithDecoration]',
        'aux_input4': 'list[VehicleStatsAuxInputWithDecoration]',
        'aux_input5': 'list[VehicleStatsAuxInputWithDecoration]',
        'aux_input6': 'list[VehicleStatsAuxInputWithDecoration]',
        'aux_input7': 'list[VehicleStatsAuxInputWithDecoration]',
        'aux_input8': 'list[VehicleStatsAuxInputWithDecoration]',
        'aux_input9': 'list[VehicleStatsAuxInputWithDecoration]',
        'barometric_pressure_pa': 'list[VehicleStatsBarometricPressurePaWithDecoration]',
        'battery_milli_volts': 'list[VehicleStatsBatteryVoltageWithDecoration]',
        'def_level_milli_percent': 'list[VehicleStatsDefLevelMilliPercentWithDecoration]',
        'ecu_speed_mph': 'list[VehicleStatsEcuSpeedMphWithDecoration]',
        'engine_coolant_temperature_milli_c': 'list[VehicleStatsEngineCoolantTempMilliCWithDecoration]',
        'engine_load_percent': 'list[VehicleStatsEngineLoadPercentWithDecoration]',
        'engine_oil_pressure_k_pa': 'list[VehicleStatsEngineOilPressureKPaWithDecoration]',
        'engine_rpm': 'list[VehicleStatsEngineRpmWithDecoration]',
        'engine_states': 'list[VehicleStatsEngineStateWithDecoration]',
        'fault_codes': 'list[VehicleStatsFaultCodesWithDecoration]',
        'fuel_percents': 'list[VehicleStatsFuelPercentWithDecoration]',
        'gps': 'list[VehicleStatsListGps]',
        'gps_distance_meters': 'list[VehicleStatsGpsDistanceMetersWithDecoration]',
        'gps_odometer_meters': 'list[VehicleStatsGpsOdometerMetersWithDecoration]',
        'id': 'str',
        'intake_manifold_temperature_milli_c': 'list[VehicleStatsIntakeManifoldTempMilliCWithDecoration]',
        'name': 'str',
        'nfc_card_scans': 'list[VehicleStatsNfcCardScanWithDecoration]',
        'obd_engine_seconds': 'list[VehicleStatsObdEngineSecondsWithDecoration]',
        'obd_odometer_meters': 'list[VehicleStatsObdOdometerMetersWithDecoration]',
        'synthetic_engine_seconds': 'list[VehicleStatsListSyntheticEngineSeconds]'
    }

    attribute_map = {
        'ambient_air_temperature_milli_c': 'ambientAirTemperatureMilliC',
        'aux_input1': 'auxInput1',
        'aux_input10': 'auxInput10',
        'aux_input2': 'auxInput2',
        'aux_input3': 'auxInput3',
        'aux_input4': 'auxInput4',
        'aux_input5': 'auxInput5',
        'aux_input6': 'auxInput6',
        'aux_input7': 'auxInput7',
        'aux_input8': 'auxInput8',
        'aux_input9': 'auxInput9',
        'barometric_pressure_pa': 'barometricPressurePa',
        'battery_milli_volts': 'batteryMilliVolts',
        'def_level_milli_percent': 'defLevelMilliPercent',
        'ecu_speed_mph': 'ecuSpeedMph',
        'engine_coolant_temperature_milli_c': 'engineCoolantTemperatureMilliC',
        'engine_load_percent': 'engineLoadPercent',
        'engine_oil_pressure_k_pa': 'engineOilPressureKPa',
        'engine_rpm': 'engineRpm',
        'engine_states': 'engineStates',
        'fault_codes': 'faultCodes',
        'fuel_percents': 'fuelPercents',
        'gps': 'gps',
        'gps_distance_meters': 'gpsDistanceMeters',
        'gps_odometer_meters': 'gpsOdometerMeters',
        'id': 'id',
        'intake_manifold_temperature_milli_c': 'intakeManifoldTemperatureMilliC',
        'name': 'name',
        'nfc_card_scans': 'nfcCardScans',
        'obd_engine_seconds': 'obdEngineSeconds',
        'obd_odometer_meters': 'obdOdometerMeters',
        'synthetic_engine_seconds': 'syntheticEngineSeconds'
    }

    def __init__(self, ambient_air_temperature_milli_c=None, aux_input1=None, aux_input10=None, aux_input2=None, aux_input3=None, aux_input4=None, aux_input5=None, aux_input6=None, aux_input7=None, aux_input8=None, aux_input9=None, barometric_pressure_pa=None, battery_milli_volts=None, def_level_milli_percent=None, ecu_speed_mph=None, engine_coolant_temperature_milli_c=None, engine_load_percent=None, engine_oil_pressure_k_pa=None, engine_rpm=None, engine_states=None, fault_codes=None, fuel_percents=None, gps=None, gps_distance_meters=None, gps_odometer_meters=None, id=None, intake_manifold_temperature_milli_c=None, name=None, nfc_card_scans=None, obd_engine_seconds=None, obd_odometer_meters=None, synthetic_engine_seconds=None, local_vars_configuration=None):  # noqa: E501
        """VehicleStatsListResponseData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ambient_air_temperature_milli_c = None
        self._aux_input1 = None
        self._aux_input10 = None
        self._aux_input2 = None
        self._aux_input3 = None
        self._aux_input4 = None
        self._aux_input5 = None
        self._aux_input6 = None
        self._aux_input7 = None
        self._aux_input8 = None
        self._aux_input9 = None
        self._barometric_pressure_pa = None
        self._battery_milli_volts = None
        self._def_level_milli_percent = None
        self._ecu_speed_mph = None
        self._engine_coolant_temperature_milli_c = None
        self._engine_load_percent = None
        self._engine_oil_pressure_k_pa = None
        self._engine_rpm = None
        self._engine_states = None
        self._fault_codes = None
        self._fuel_percents = None
        self._gps = None
        self._gps_distance_meters = None
        self._gps_odometer_meters = None
        self._id = None
        self._intake_manifold_temperature_milli_c = None
        self._name = None
        self._nfc_card_scans = None
        self._obd_engine_seconds = None
        self._obd_odometer_meters = None
        self._synthetic_engine_seconds = None
        self.discriminator = None

        if ambient_air_temperature_milli_c is not None:
            self.ambient_air_temperature_milli_c = ambient_air_temperature_milli_c
        if aux_input1 is not None:
            self.aux_input1 = aux_input1
        if aux_input10 is not None:
            self.aux_input10 = aux_input10
        if aux_input2 is not None:
            self.aux_input2 = aux_input2
        if aux_input3 is not None:
            self.aux_input3 = aux_input3
        if aux_input4 is not None:
            self.aux_input4 = aux_input4
        if aux_input5 is not None:
            self.aux_input5 = aux_input5
        if aux_input6 is not None:
            self.aux_input6 = aux_input6
        if aux_input7 is not None:
            self.aux_input7 = aux_input7
        if aux_input8 is not None:
            self.aux_input8 = aux_input8
        if aux_input9 is not None:
            self.aux_input9 = aux_input9
        if barometric_pressure_pa is not None:
            self.barometric_pressure_pa = barometric_pressure_pa
        if battery_milli_volts is not None:
            self.battery_milli_volts = battery_milli_volts
        if def_level_milli_percent is not None:
            self.def_level_milli_percent = def_level_milli_percent
        if ecu_speed_mph is not None:
            self.ecu_speed_mph = ecu_speed_mph
        if engine_coolant_temperature_milli_c is not None:
            self.engine_coolant_temperature_milli_c = engine_coolant_temperature_milli_c
        if engine_load_percent is not None:
            self.engine_load_percent = engine_load_percent
        if engine_oil_pressure_k_pa is not None:
            self.engine_oil_pressure_k_pa = engine_oil_pressure_k_pa
        if engine_rpm is not None:
            self.engine_rpm = engine_rpm
        if engine_states is not None:
            self.engine_states = engine_states
        if fault_codes is not None:
            self.fault_codes = fault_codes
        if fuel_percents is not None:
            self.fuel_percents = fuel_percents
        if gps is not None:
            self.gps = gps
        if gps_distance_meters is not None:
            self.gps_distance_meters = gps_distance_meters
        if gps_odometer_meters is not None:
            self.gps_odometer_meters = gps_odometer_meters
        if id is not None:
            self.id = id
        if intake_manifold_temperature_milli_c is not None:
            self.intake_manifold_temperature_milli_c = intake_manifold_temperature_milli_c
        if name is not None:
            self.name = name
        if nfc_card_scans is not None:
            self.nfc_card_scans = nfc_card_scans
        if obd_engine_seconds is not None:
            self.obd_engine_seconds = obd_engine_seconds
        if obd_odometer_meters is not None:
            self.obd_odometer_meters = obd_odometer_meters
        if synthetic_engine_seconds is not None:
            self.synthetic_engine_seconds = synthetic_engine_seconds

    @property
    def ambient_air_temperature_milli_c(self):
        """Gets the ambient_air_temperature_milli_c of this VehicleStatsListResponseData.  # noqa: E501

        A list of ambient air temperature readings in millidegree Celsius for the given vehicle.  # noqa: E501

        :return: The ambient_air_temperature_milli_c of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsAmbientAirTempMilliCWithDecoration]
        """
        return self._ambient_air_temperature_milli_c

    @ambient_air_temperature_milli_c.setter
    def ambient_air_temperature_milli_c(self, ambient_air_temperature_milli_c):
        """Sets the ambient_air_temperature_milli_c of this VehicleStatsListResponseData.

        A list of ambient air temperature readings in millidegree Celsius for the given vehicle.  # noqa: E501

        :param ambient_air_temperature_milli_c: The ambient_air_temperature_milli_c of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsAmbientAirTempMilliCWithDecoration]
        """

        self._ambient_air_temperature_milli_c = ambient_air_temperature_milli_c

    @property
    def aux_input1(self):
        """Gets the aux_input1 of this VehicleStatsListResponseData.  # noqa: E501

        A list of auxiliary equipment states.  # noqa: E501

        :return: The aux_input1 of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsAuxInputWithDecoration]
        """
        return self._aux_input1

    @aux_input1.setter
    def aux_input1(self, aux_input1):
        """Sets the aux_input1 of this VehicleStatsListResponseData.

        A list of auxiliary equipment states.  # noqa: E501

        :param aux_input1: The aux_input1 of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsAuxInputWithDecoration]
        """

        self._aux_input1 = aux_input1

    @property
    def aux_input10(self):
        """Gets the aux_input10 of this VehicleStatsListResponseData.  # noqa: E501

        A list of auxiliary equipment states.  # noqa: E501

        :return: The aux_input10 of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsAuxInputWithDecoration]
        """
        return self._aux_input10

    @aux_input10.setter
    def aux_input10(self, aux_input10):
        """Sets the aux_input10 of this VehicleStatsListResponseData.

        A list of auxiliary equipment states.  # noqa: E501

        :param aux_input10: The aux_input10 of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsAuxInputWithDecoration]
        """

        self._aux_input10 = aux_input10

    @property
    def aux_input2(self):
        """Gets the aux_input2 of this VehicleStatsListResponseData.  # noqa: E501

        A list of auxiliary equipment states.  # noqa: E501

        :return: The aux_input2 of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsAuxInputWithDecoration]
        """
        return self._aux_input2

    @aux_input2.setter
    def aux_input2(self, aux_input2):
        """Sets the aux_input2 of this VehicleStatsListResponseData.

        A list of auxiliary equipment states.  # noqa: E501

        :param aux_input2: The aux_input2 of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsAuxInputWithDecoration]
        """

        self._aux_input2 = aux_input2

    @property
    def aux_input3(self):
        """Gets the aux_input3 of this VehicleStatsListResponseData.  # noqa: E501

        A list of auxiliary equipment states.  # noqa: E501

        :return: The aux_input3 of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsAuxInputWithDecoration]
        """
        return self._aux_input3

    @aux_input3.setter
    def aux_input3(self, aux_input3):
        """Sets the aux_input3 of this VehicleStatsListResponseData.

        A list of auxiliary equipment states.  # noqa: E501

        :param aux_input3: The aux_input3 of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsAuxInputWithDecoration]
        """

        self._aux_input3 = aux_input3

    @property
    def aux_input4(self):
        """Gets the aux_input4 of this VehicleStatsListResponseData.  # noqa: E501

        A list of auxiliary equipment states.  # noqa: E501

        :return: The aux_input4 of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsAuxInputWithDecoration]
        """
        return self._aux_input4

    @aux_input4.setter
    def aux_input4(self, aux_input4):
        """Sets the aux_input4 of this VehicleStatsListResponseData.

        A list of auxiliary equipment states.  # noqa: E501

        :param aux_input4: The aux_input4 of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsAuxInputWithDecoration]
        """

        self._aux_input4 = aux_input4

    @property
    def aux_input5(self):
        """Gets the aux_input5 of this VehicleStatsListResponseData.  # noqa: E501

        A list of auxiliary equipment states.  # noqa: E501

        :return: The aux_input5 of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsAuxInputWithDecoration]
        """
        return self._aux_input5

    @aux_input5.setter
    def aux_input5(self, aux_input5):
        """Sets the aux_input5 of this VehicleStatsListResponseData.

        A list of auxiliary equipment states.  # noqa: E501

        :param aux_input5: The aux_input5 of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsAuxInputWithDecoration]
        """

        self._aux_input5 = aux_input5

    @property
    def aux_input6(self):
        """Gets the aux_input6 of this VehicleStatsListResponseData.  # noqa: E501

        A list of auxiliary equipment states.  # noqa: E501

        :return: The aux_input6 of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsAuxInputWithDecoration]
        """
        return self._aux_input6

    @aux_input6.setter
    def aux_input6(self, aux_input6):
        """Sets the aux_input6 of this VehicleStatsListResponseData.

        A list of auxiliary equipment states.  # noqa: E501

        :param aux_input6: The aux_input6 of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsAuxInputWithDecoration]
        """

        self._aux_input6 = aux_input6

    @property
    def aux_input7(self):
        """Gets the aux_input7 of this VehicleStatsListResponseData.  # noqa: E501

        A list of auxiliary equipment states.  # noqa: E501

        :return: The aux_input7 of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsAuxInputWithDecoration]
        """
        return self._aux_input7

    @aux_input7.setter
    def aux_input7(self, aux_input7):
        """Sets the aux_input7 of this VehicleStatsListResponseData.

        A list of auxiliary equipment states.  # noqa: E501

        :param aux_input7: The aux_input7 of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsAuxInputWithDecoration]
        """

        self._aux_input7 = aux_input7

    @property
    def aux_input8(self):
        """Gets the aux_input8 of this VehicleStatsListResponseData.  # noqa: E501

        A list of auxiliary equipment states.  # noqa: E501

        :return: The aux_input8 of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsAuxInputWithDecoration]
        """
        return self._aux_input8

    @aux_input8.setter
    def aux_input8(self, aux_input8):
        """Sets the aux_input8 of this VehicleStatsListResponseData.

        A list of auxiliary equipment states.  # noqa: E501

        :param aux_input8: The aux_input8 of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsAuxInputWithDecoration]
        """

        self._aux_input8 = aux_input8

    @property
    def aux_input9(self):
        """Gets the aux_input9 of this VehicleStatsListResponseData.  # noqa: E501

        A list of auxiliary equipment states.  # noqa: E501

        :return: The aux_input9 of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsAuxInputWithDecoration]
        """
        return self._aux_input9

    @aux_input9.setter
    def aux_input9(self, aux_input9):
        """Sets the aux_input9 of this VehicleStatsListResponseData.

        A list of auxiliary equipment states.  # noqa: E501

        :param aux_input9: The aux_input9 of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsAuxInputWithDecoration]
        """

        self._aux_input9 = aux_input9

    @property
    def barometric_pressure_pa(self):
        """Gets the barometric_pressure_pa of this VehicleStatsListResponseData.  # noqa: E501

        A list of barometric pressure readings in pascals for the given vehicle.  # noqa: E501

        :return: The barometric_pressure_pa of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsBarometricPressurePaWithDecoration]
        """
        return self._barometric_pressure_pa

    @barometric_pressure_pa.setter
    def barometric_pressure_pa(self, barometric_pressure_pa):
        """Sets the barometric_pressure_pa of this VehicleStatsListResponseData.

        A list of barometric pressure readings in pascals for the given vehicle.  # noqa: E501

        :param barometric_pressure_pa: The barometric_pressure_pa of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsBarometricPressurePaWithDecoration]
        """

        self._barometric_pressure_pa = barometric_pressure_pa

    @property
    def battery_milli_volts(self):
        """Gets the battery_milli_volts of this VehicleStatsListResponseData.  # noqa: E501

        A list of battery levels in milliVolts for the given vehicle.  # noqa: E501

        :return: The battery_milli_volts of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsBatteryVoltageWithDecoration]
        """
        return self._battery_milli_volts

    @battery_milli_volts.setter
    def battery_milli_volts(self, battery_milli_volts):
        """Sets the battery_milli_volts of this VehicleStatsListResponseData.

        A list of battery levels in milliVolts for the given vehicle.  # noqa: E501

        :param battery_milli_volts: The battery_milli_volts of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsBatteryVoltageWithDecoration]
        """

        self._battery_milli_volts = battery_milli_volts

    @property
    def def_level_milli_percent(self):
        """Gets the def_level_milli_percent of this VehicleStatsListResponseData.  # noqa: E501

        A list of DEF level milli percentage readings for the given vehicle.  # noqa: E501

        :return: The def_level_milli_percent of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsDefLevelMilliPercentWithDecoration]
        """
        return self._def_level_milli_percent

    @def_level_milli_percent.setter
    def def_level_milli_percent(self, def_level_milli_percent):
        """Sets the def_level_milli_percent of this VehicleStatsListResponseData.

        A list of DEF level milli percentage readings for the given vehicle.  # noqa: E501

        :param def_level_milli_percent: The def_level_milli_percent of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsDefLevelMilliPercentWithDecoration]
        """

        self._def_level_milli_percent = def_level_milli_percent

    @property
    def ecu_speed_mph(self):
        """Gets the ecu_speed_mph of this VehicleStatsListResponseData.  # noqa: E501

        A list of the speeds of the vehicle in miles per hour, as reported by the ECU.  # noqa: E501

        :return: The ecu_speed_mph of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsEcuSpeedMphWithDecoration]
        """
        return self._ecu_speed_mph

    @ecu_speed_mph.setter
    def ecu_speed_mph(self, ecu_speed_mph):
        """Sets the ecu_speed_mph of this VehicleStatsListResponseData.

        A list of the speeds of the vehicle in miles per hour, as reported by the ECU.  # noqa: E501

        :param ecu_speed_mph: The ecu_speed_mph of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsEcuSpeedMphWithDecoration]
        """

        self._ecu_speed_mph = ecu_speed_mph

    @property
    def engine_coolant_temperature_milli_c(self):
        """Gets the engine_coolant_temperature_milli_c of this VehicleStatsListResponseData.  # noqa: E501

        A list of engine coolant temperature readings in millidegree Celsius for the given vehicle.  # noqa: E501

        :return: The engine_coolant_temperature_milli_c of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsEngineCoolantTempMilliCWithDecoration]
        """
        return self._engine_coolant_temperature_milli_c

    @engine_coolant_temperature_milli_c.setter
    def engine_coolant_temperature_milli_c(self, engine_coolant_temperature_milli_c):
        """Sets the engine_coolant_temperature_milli_c of this VehicleStatsListResponseData.

        A list of engine coolant temperature readings in millidegree Celsius for the given vehicle.  # noqa: E501

        :param engine_coolant_temperature_milli_c: The engine_coolant_temperature_milli_c of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsEngineCoolantTempMilliCWithDecoration]
        """

        self._engine_coolant_temperature_milli_c = engine_coolant_temperature_milli_c

    @property
    def engine_load_percent(self):
        """Gets the engine_load_percent of this VehicleStatsListResponseData.  # noqa: E501

        A list of engine load percentage readings for the given vehicle.  # noqa: E501

        :return: The engine_load_percent of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsEngineLoadPercentWithDecoration]
        """
        return self._engine_load_percent

    @engine_load_percent.setter
    def engine_load_percent(self, engine_load_percent):
        """Sets the engine_load_percent of this VehicleStatsListResponseData.

        A list of engine load percentage readings for the given vehicle.  # noqa: E501

        :param engine_load_percent: The engine_load_percent of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsEngineLoadPercentWithDecoration]
        """

        self._engine_load_percent = engine_load_percent

    @property
    def engine_oil_pressure_k_pa(self):
        """Gets the engine_oil_pressure_k_pa of this VehicleStatsListResponseData.  # noqa: E501

        A list of engine oil pressure readings in kilopascals for the given vehicle.  # noqa: E501

        :return: The engine_oil_pressure_k_pa of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsEngineOilPressureKPaWithDecoration]
        """
        return self._engine_oil_pressure_k_pa

    @engine_oil_pressure_k_pa.setter
    def engine_oil_pressure_k_pa(self, engine_oil_pressure_k_pa):
        """Sets the engine_oil_pressure_k_pa of this VehicleStatsListResponseData.

        A list of engine oil pressure readings in kilopascals for the given vehicle.  # noqa: E501

        :param engine_oil_pressure_k_pa: The engine_oil_pressure_k_pa of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsEngineOilPressureKPaWithDecoration]
        """

        self._engine_oil_pressure_k_pa = engine_oil_pressure_k_pa

    @property
    def engine_rpm(self):
        """Gets the engine_rpm of this VehicleStatsListResponseData.  # noqa: E501

        A list engine RPM values for the given vehicle.  # noqa: E501

        :return: The engine_rpm of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsEngineRpmWithDecoration]
        """
        return self._engine_rpm

    @engine_rpm.setter
    def engine_rpm(self, engine_rpm):
        """Sets the engine_rpm of this VehicleStatsListResponseData.

        A list engine RPM values for the given vehicle.  # noqa: E501

        :param engine_rpm: The engine_rpm of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsEngineRpmWithDecoration]
        """

        self._engine_rpm = engine_rpm

    @property
    def engine_states(self):
        """Gets the engine_states of this VehicleStatsListResponseData.  # noqa: E501

        A list of engine state events for the given vehicle.  # noqa: E501

        :return: The engine_states of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsEngineStateWithDecoration]
        """
        return self._engine_states

    @engine_states.setter
    def engine_states(self, engine_states):
        """Sets the engine_states of this VehicleStatsListResponseData.

        A list of engine state events for the given vehicle.  # noqa: E501

        :param engine_states: The engine_states of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsEngineStateWithDecoration]
        """

        self._engine_states = engine_states

    @property
    def fault_codes(self):
        """Gets the fault_codes of this VehicleStatsListResponseData.  # noqa: E501

        A list of engine fault codes.  # noqa: E501

        :return: The fault_codes of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsFaultCodesWithDecoration]
        """
        return self._fault_codes

    @fault_codes.setter
    def fault_codes(self, fault_codes):
        """Sets the fault_codes of this VehicleStatsListResponseData.

        A list of engine fault codes.  # noqa: E501

        :param fault_codes: The fault_codes of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsFaultCodesWithDecoration]
        """

        self._fault_codes = fault_codes

    @property
    def fuel_percents(self):
        """Gets the fuel_percents of this VehicleStatsListResponseData.  # noqa: E501

        A list of fuel percentage readings for the given vehicle.  # noqa: E501

        :return: The fuel_percents of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsFuelPercentWithDecoration]
        """
        return self._fuel_percents

    @fuel_percents.setter
    def fuel_percents(self, fuel_percents):
        """Sets the fuel_percents of this VehicleStatsListResponseData.

        A list of fuel percentage readings for the given vehicle.  # noqa: E501

        :param fuel_percents: The fuel_percents of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsFuelPercentWithDecoration]
        """

        self._fuel_percents = fuel_percents

    @property
    def gps(self):
        """Gets the gps of this VehicleStatsListResponseData.  # noqa: E501

        A list of GPS location events for the given vehicles.  # noqa: E501

        :return: The gps of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsListGps]
        """
        return self._gps

    @gps.setter
    def gps(self, gps):
        """Sets the gps of this VehicleStatsListResponseData.

        A list of GPS location events for the given vehicles.  # noqa: E501

        :param gps: The gps of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsListGps]
        """

        self._gps = gps

    @property
    def gps_distance_meters(self):
        """Gets the gps_distance_meters of this VehicleStatsListResponseData.  # noqa: E501

        A list of GPS distance events for the given vehicle.  # noqa: E501

        :return: The gps_distance_meters of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsGpsDistanceMetersWithDecoration]
        """
        return self._gps_distance_meters

    @gps_distance_meters.setter
    def gps_distance_meters(self, gps_distance_meters):
        """Sets the gps_distance_meters of this VehicleStatsListResponseData.

        A list of GPS distance events for the given vehicle.  # noqa: E501

        :param gps_distance_meters: The gps_distance_meters of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsGpsDistanceMetersWithDecoration]
        """

        self._gps_distance_meters = gps_distance_meters

    @property
    def gps_odometer_meters(self):
        """Gets the gps_odometer_meters of this VehicleStatsListResponseData.  # noqa: E501

        A list of GPS odometer events for the given vehicle.  # noqa: E501

        :return: The gps_odometer_meters of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsGpsOdometerMetersWithDecoration]
        """
        return self._gps_odometer_meters

    @gps_odometer_meters.setter
    def gps_odometer_meters(self, gps_odometer_meters):
        """Sets the gps_odometer_meters of this VehicleStatsListResponseData.

        A list of GPS odometer events for the given vehicle.  # noqa: E501

        :param gps_odometer_meters: The gps_odometer_meters of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsGpsOdometerMetersWithDecoration]
        """

        self._gps_odometer_meters = gps_odometer_meters

    @property
    def id(self):
        """Gets the id of this VehicleStatsListResponseData.  # noqa: E501

        The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed.  # noqa: E501

        :return: The id of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VehicleStatsListResponseData.

        The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed.  # noqa: E501

        :param id: The id of this VehicleStatsListResponseData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def intake_manifold_temperature_milli_c(self):
        """Gets the intake_manifold_temperature_milli_c of this VehicleStatsListResponseData.  # noqa: E501

        A list of intake manifold temperature readings in millidegree Celsius for the given vehicle.  # noqa: E501

        :return: The intake_manifold_temperature_milli_c of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsIntakeManifoldTempMilliCWithDecoration]
        """
        return self._intake_manifold_temperature_milli_c

    @intake_manifold_temperature_milli_c.setter
    def intake_manifold_temperature_milli_c(self, intake_manifold_temperature_milli_c):
        """Sets the intake_manifold_temperature_milli_c of this VehicleStatsListResponseData.

        A list of intake manifold temperature readings in millidegree Celsius for the given vehicle.  # noqa: E501

        :param intake_manifold_temperature_milli_c: The intake_manifold_temperature_milli_c of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsIntakeManifoldTempMilliCWithDecoration]
        """

        self._intake_manifold_temperature_milli_c = intake_manifold_temperature_milli_c

    @property
    def name(self):
        """Gets the name of this VehicleStatsListResponseData.  # noqa: E501

        The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.  # noqa: E501

        :return: The name of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VehicleStatsListResponseData.

        The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.  # noqa: E501

        :param name: The name of this VehicleStatsListResponseData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def nfc_card_scans(self):
        """Gets the nfc_card_scans of this VehicleStatsListResponseData.  # noqa: E501

        A list of NFC cards that were scanned for the given vehicles.  # noqa: E501

        :return: The nfc_card_scans of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsNfcCardScanWithDecoration]
        """
        return self._nfc_card_scans

    @nfc_card_scans.setter
    def nfc_card_scans(self, nfc_card_scans):
        """Sets the nfc_card_scans of this VehicleStatsListResponseData.

        A list of NFC cards that were scanned for the given vehicles.  # noqa: E501

        :param nfc_card_scans: The nfc_card_scans of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsNfcCardScanWithDecoration]
        """

        self._nfc_card_scans = nfc_card_scans

    @property
    def obd_engine_seconds(self):
        """Gets the obd_engine_seconds of this VehicleStatsListResponseData.  # noqa: E501

        A list of OBD engine seconds readings for the given vehicle.  # noqa: E501

        :return: The obd_engine_seconds of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsObdEngineSecondsWithDecoration]
        """
        return self._obd_engine_seconds

    @obd_engine_seconds.setter
    def obd_engine_seconds(self, obd_engine_seconds):
        """Sets the obd_engine_seconds of this VehicleStatsListResponseData.

        A list of OBD engine seconds readings for the given vehicle.  # noqa: E501

        :param obd_engine_seconds: The obd_engine_seconds of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsObdEngineSecondsWithDecoration]
        """

        self._obd_engine_seconds = obd_engine_seconds

    @property
    def obd_odometer_meters(self):
        """Gets the obd_odometer_meters of this VehicleStatsListResponseData.  # noqa: E501

        A list of OBD odometer readings for the given vehicle.  # noqa: E501

        :return: The obd_odometer_meters of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsObdOdometerMetersWithDecoration]
        """
        return self._obd_odometer_meters

    @obd_odometer_meters.setter
    def obd_odometer_meters(self, obd_odometer_meters):
        """Sets the obd_odometer_meters of this VehicleStatsListResponseData.

        A list of OBD odometer readings for the given vehicle.  # noqa: E501

        :param obd_odometer_meters: The obd_odometer_meters of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsObdOdometerMetersWithDecoration]
        """

        self._obd_odometer_meters = obd_odometer_meters

    @property
    def synthetic_engine_seconds(self):
        """Gets the synthetic_engine_seconds of this VehicleStatsListResponseData.  # noqa: E501

        A list of synthetic engine seconds values.  # noqa: E501

        :return: The synthetic_engine_seconds of this VehicleStatsListResponseData.  # noqa: E501
        :rtype: list[VehicleStatsListSyntheticEngineSeconds]
        """
        return self._synthetic_engine_seconds

    @synthetic_engine_seconds.setter
    def synthetic_engine_seconds(self, synthetic_engine_seconds):
        """Sets the synthetic_engine_seconds of this VehicleStatsListResponseData.

        A list of synthetic engine seconds values.  # noqa: E501

        :param synthetic_engine_seconds: The synthetic_engine_seconds of this VehicleStatsListResponseData.  # noqa: E501
        :type: list[VehicleStatsListSyntheticEngineSeconds]
        """

        self._synthetic_engine_seconds = synthetic_engine_seconds

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VehicleStatsListResponseData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VehicleStatsListResponseData):
            return True

        return self.to_dict() != other.to_dict()
