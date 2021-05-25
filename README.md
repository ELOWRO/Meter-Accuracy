# Meter Accuracy Data Representation

## Purpose

Meter Accuracy Data Representation format, abbreviated as MACDR. JSON file structure.

Portable and open repository of various meters accuracy expressed in uncertainty based on range, reading and absolute offset. Intended for machine to machine consumption.

## Data

All specified meters data is located in `/Meters` folder, for easy M2M consumption `index.js` is auto-generated.

## MACDRv1 Format Specification

### Format Identifier

`org.macdr.v1`

### Values:

All uncertainties values are floating-point numbers (64bit Double) and assumed to be either positive or negative so `0.1` means `±0.1`.

### Filename:

Every unique meter model will be represented by a separate `json` file. Filename should be created as follows:

`{Manufacturer}_{Model Name}.json`

**Example:**

`Keysight_3458A.json`

### Metadata:

- `manufacturer` - manufacturer short name
- `manufacturer_full` - manufacturer name
- `model_name` - model full name
- `uid` - unique product identifier (reverse dns)
- `product_identifier` - manufacturer's product identifier
- `source` - description of source (usually datasheet)
- `source_url` - link to source (usually to a datasheet)
- `photo_url` - link to meter photo²
- `photo_url_copyright` - author¹
- `usdz_model_url` - link to meter USDZ 3d model¹
- `usdz_model_url_copyright` - author¹

¹-optional

Important: All assets must be public domain!

### Specs

All meter specs are expressed as key-values where key is amount of hours from calibration.

#### Measured Absolute Quantities 

|               Identifier              | Unit     | Description                          |
|:--------------------------------------|:---------| :------------------------------------|
| `voltage.dc` 		 					| Volts    | DC Voltage
| `current.dc`							| Amperes  | DC Current
| `voltage.ac` 							| Volts    | AC Voltage
| `current.ac`							| Amperes  | AC Current
| `resistance.2w`						| Ohms     | Resistance 2-Wire
| `resistance.4w`						| Ohms     | Resistance 4-Wire
| `frequency`							| Herz     | Frequency
| `capacitance`							| Farad    | Capacitance at Frequency
| `inductance`							| Henres   | Inductance at Frequency
| `impedance.phase`						| degrees  | Phase Angle of Impedance

This list is NOT part of the MACDRv1 specification, more identifiers will be added along the way.

#### Measured Transferred Quantities 

|               Identifier              | Unit     | Description                          |
|:--------------------------------------|:---------| :------------------------------------|
| `voltage.dc.transfer` 				| Volts    | DC Voltage Transfer
| `voltage.ac.transfer` 				| Volts    | AC Voltage Transfer
| `voltage.acdc.transfer` 				| Volts    | AC/DC Voltage Transfer
| `resistance.2w.transfer`				| Ohms     | Resistance 2-Wire Transfer
| `resistance.4w.transfer`				| Ohms     | Resistance 4-Wire Transfer

This list is NOT part of the MACDRv1 specification, more identifiers will be added along the way.

### Structure

#### Main

```json
{
    "format": "{string}",
	"uid": "{string}",
	"manufacturer": "{string}",
	"model_name": "{string}",
	"product_identifier": "{string}",
	"source": "{url}",
	"source_url": "{url}",
	"transfer": {
		"{Quantity Identifier}": [ ]
	},
	"absolute": {
		"{Quantity Identifier}": [ ]
	}
}
```

#### Specs

- `reading` - fraction of reading
- `range` - fraction of used range
- `absolute` - absolute offset (in relevant unit)

**Absolute**

- `hours_from_calibration` - hours limit from meter calibration/adjustment

```json
{
	"hours_from_calibration": 0,
	"seconds_between_measurements": 0,
	"absolute": 0.0,
	"reading": 0.0,
	"range": 0.0
}	
```

**Transfer**

- `seconds_between_measurements` - used in transfer specs, max time between measurements
- `required_temperature_celsius` - (optional) some manufacturers specify only for selected transfer temperature
- `maximum_temperature_change` - (optional) maximum temperature change between measurements

```json
{
	"seconds_between_measurements": 0,
	"required_temperature_celsius": 0,
	"maximum_temperature_change": 0,
	"absolute": 0.0,
	"reading": 0.0,
	"range": 0.0
}	
```

#### Absolute: DC Voltage

- `range` - range in Volts

```json
{
	"voltage.dc": [
		{
			"range": 0, 
			"specs": []
		}
	]
}
```

#### Absolute: DC Current

- `range` - range in Amperes

```json
{
	"current.dc": [
		{
			"range": 0, 
			"specs": []
		}
	]
}
```

#### Absolute: Resistance

- `range` - range in Ohms
- `current` - current used in Amperes

```json
{
	"resistance.4w": [
		{
			"range": 0, 
			"current": 0,
			"specs": []
		}
	]
}
```

#### Absolute: AC Voltage

- `range` - range in Volts
- `frequency_from` - frequency range start, Herz
- `frequency_to` - frequency range end, Herz

```json
{
	"voltage.ac": [
		{
			"range": 0, 
			"frequency_from": 0.0, 
			"frequency_to": 0.0, 
			"specs": []
		}
	]
}
```
