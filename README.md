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
- `photo_url_author` - author¹
- `usdz_model_url` - link to meter USDZ 3d model¹
- `usdz_model_url_author` - author¹

¹-optional

Important: All assets must be public domain!

### Specs

All meter specs are expressed as key-values where key is amount of hours from calibration.

#### Absolute Quantities 

|               Identifier              | Unit     | Description                          |
|:--------------------------------------|:---------| :------------------------------------|
| `absolute.voltage.dc` 		 		| Volts    | DC Voltage
| `absolute.current.dc`					| Amperes  | DC Current
| `absolute.voltage.ac` 				| Volts    | AC Voltage
| `absolute.current.ac`					| Amperes  | AC Current
| `absolute.resistance.2w`				| Ohms     | Resistance 2-Wire
| `absolute.resistance.4w`				| Ohms     | Resistance 4-Wire
| `absolute.frequency`					| Herz     | Frequency
| `absolute.capacitance`				| Farad    | Capacitance at Frequency
| `absolute.inductance`					| Henres   | Inductance at Frequency
| `absolute.impedance.phase`			| degrees  | Phase Angle of Impedance

This list is NOT part of the MACDRv1 specification, more identifiers will be added along the way.

#### Transfer Quantities 

|               Identifier              | Unit     | Description                          |
|:--------------------------------------|:---------| :------------------------------------|
| `transfer.voltage.dc` 				| Volts    | DC Voltage Transfer
| `transfer.voltage.ac` 				| Volts    | AC Voltage Transfer
| `transfer.voltage.acdc` 				| Volts    | AC/DC Voltage Transfer
| `transfer.resistance.2w`				| Ohms     | Resistance 2-Wire Transfer
| `transfer.resistance.4w`				| Ohms     | Resistance 4-Wire Transfer

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
	"maximum_temperature_change_celsius": 0,
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
