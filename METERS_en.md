
# Digital Multimeters


## Fluke 8588A
- Model: 8588A Reference Multimeter
- Manufacturer: Fluke Corporation
- Source: [Datasheet](https://download.flukecal.com/pub/literature/8588A_Rev_E_accuracy.pdf)
- Open Source Data: [MACDRv1 JSON](https://github.com/ELOWRO/Meter-Accuracy/blob/main/Meters/Fluke_8588A.json)

### Transfer

#### DC Voltage Transfer

**Maximum time between measurements: 20 minutes**

**± (ppm of reading + ppm of range)**

| Range | Uncertainty |
|--:|:--:|
| 0.1000000V | 0.20 + 2.00  (Confidence 95%)  [Tref ±1.0 °C] |
| 1.0000000V | 0.06 + 0.30  (Confidence 95%)  [Tref ±1.0 °C] |
| 10.0000000V | 0.05 + 0.05  (Confidence 95%)  [Tref ±1.0 °C] |
| [Zin: 10MΩ] 100.0000000V | 0.40 + 0.30  (Confidence 95%)  [Tref ±1.0 °C] |
| [Zin: 1MΩ] 100.0000000V | 2.00 + 5.00  (Confidence 95%)  [Tref ±1.0 °C] |
| [Zin: 10MΩ] 1000.0000000V | 0.40 + 0.50  (Confidence 95%)  [Tref ±1.0 °C] |
| [Zin: 1MΩ] 1000.0000000V | 4.00 + 25.00  (Confidence 95%)  [Tref ±1.0 °C] |

### Absolute Value

## Keysight 3458A
- Model: 3458A Multimeter
- Manufacturer: Keysight Technologies
- Source: [Datasheet](https://www.keysight.com/zz/en/assets/7018-06796/data-sheets/5965-4971.pdf)
- Open Source Data: [MACDRv1 JSON](https://github.com/ELOWRO/Meter-Accuracy/blob/main/Meters/Keysight_3458A.json)

### Transfer

#### DC Voltage Transfer

**Maximum time between measurements: 10 minutes**

**± (ppm of reading + ppm of range)**

| Range | Uncertainty |
|--:|:--:|
| 0.1000000V | 0.50 + 0.50  [Tref ±0.5 °C] |
| 1.0000000V | 3.00 + 0.10  [Tref ±0.5 °C] |
| 10.0000000V | 0.05 + 0.05  [Tref ±0.5 °C] |
| 100.0000000V | 0.50 + 0.10  [Tref ±0.5 °C] |
| 1000.0000000V | 1.50 + 0.05  [Tref ±0.5 °C] |

### Absolute Value

#### DC Voltage
**± (ppm of reading + ppm of range)**

| Range | 1 days | 90 days | 365 days | 730 days |
|--:|:--:|:--:|:--:|:--:|
| 0.1000000V| 2.50 + 3.00 | 5.00 + 3.00 | 9.00 + 3.00 | 14.00 + 3.00 |
| 1.0000000V| 1.50 + 0.30 | 4.60 + 0.30 | 8.00 + 0.30 | 14.00 + 0.30 |
| 10.0000000V| 0.50 + 0.05 | 4.10 + 0.05 | 8.00 + 0.05 | 14.00 + 0.05 |
| 100.0000000V| 2.50 + 0.30 | 6.00 + 0.30 | 10.00 + 0.30 | 14.00 + 0.30 |
| 1000.0000000V| 2.50 + 0.10 | 6.00 + 0.10 | 10.00 + 0.10 | 14.00 + 0.10 |

#### DC Current
**± (ppm of reading + ppm of range)**

| Range | 1 days | 90 days | 365 days | 730 days |
|--:|:--:|:--:|:--:|:--:|
| 0.0000001A| 10.00 + 400.00 | 30.00 + 400.00 | 30.00 + 400.00 | 35.00 + 400.00 |
| 0.0000010A| 10.00 + 40.00 | 15.00 + 40.00 | 20.00 + 40.00 | 25.00 + 40.00 |
| 0.0000100A| 10.00 + 7.00 | 15.00 + 10.00 | 20.00 + 10.00 | 25.00 + 10.00 |
| 0.0001000A| 10.00 + 6.00 | 15.00 + 8.00 | 20.00 + 8.00 | 25.00 + 8.00 |
| 0.0010000A| 10.00 + 4.00 | 15.00 + 5.00 | 20.00 + 5.00 | 25.00 + 5.00 |
| 0.0100000A| 10.00 + 4.00 | 15.00 + 5.00 | 20.00 + 5.00 | 25.00 + 5.00 |
| 0.1000000A| 25.00 + 4.00 | 30.00 + 5.00 | 35.00 + 5.00 | 40.00 + 5.00 |
| 1.0000000A| 100.00 + 10.00 | 100.00 + 10.00 | 110.00 + 10.00 | 115.00 + 10.00 |

## Keysight 3458A-002
- Model: 3458A Multimeter with Option 002
- Manufacturer: Keysight Technologies
- Source: [Datasheet](https://www.keysight.com/zz/en/assets/7018-06796/data-sheets/5965-4971.pdf)
- Open Source Data: [MACDRv1 JSON](https://github.com/ELOWRO/Meter-Accuracy/blob/main/Meters/Keysight_3458A-002.json)

### Transfer

#### DC Voltage Transfer

**Maximum time between measurements: 10 minutes**

**± (ppm of reading + ppm of range)**

| Range | Uncertainty |
|--:|:--:|
| 0.1000000V | 0.50 + 0.50  [Tref ±0.5 °C] |
| 1.0000000V | 3.00 + 0.10  [Tref ±0.5 °C] |
| 10.0000000V | 0.05 + 0.05  [Tref ±0.5 °C] |
| 100.0000000V | 0.50 + 0.10  [Tref ±0.5 °C] |
| 1000.0000000V | 1.50 + 0.05  [Tref ±0.5 °C] |

### Absolute Value

#### DC Voltage
**± (ppm of reading + ppm of range)**

| Range | 1 days | 90 days | 365 days | 730 days |
|--:|:--:|:--:|:--:|:--:|
| 0.1000000V| 2.50 + 3.00 | 3.50 + 3.00 | 5.00 + 3.00 | 10.00 + 3.00 |
| 1.0000000V| 1.50 + 3.00 | 3.10 + 3.00 | 4.00 + 3.00 | 10.00 + 3.00 |
| 10.0000000V| 0.50 + 0.05 | 2.60 + 0.05 | 4.00 + 0.05 | 10.00 + 0.05 |
| 100.0000000V| 2.50 + 0.30 | 4.50 + 0.30 | 6.00 + 0.30 | 10.00 + 0.30 |
| 1000.0000000V| 2.50 + 0.30 | 4.50 + 0.30 | 6.00 + 0.30 | 10.00 + 0.30 |

#### DC Current
**± (ppm of reading + ppm of range)**

| Range | 1 days | 90 days | 365 days | 730 days |
|--:|:--:|:--:|:--:|:--:|
| 0.0000001A| 10.00 + 400.00 | 30.00 + 400.00 | 30.00 + 400.00 | 35.00 + 400.00 |
| 0.0000010A| 10.00 + 40.00 | 15.00 + 40.00 | 20.00 + 40.00 | 25.00 + 40.00 |
| 0.0000100A| 10.00 + 7.00 | 15.00 + 10.00 | 20.00 + 10.00 | 25.00 + 10.00 |
| 0.0001000A| 10.00 + 6.00 | 15.00 + 8.00 | 20.00 + 8.00 | 25.00 + 8.00 |
| 0.0010000A| 10.00 + 4.00 | 15.00 + 5.00 | 20.00 + 5.00 | 25.00 + 5.00 |
| 0.0100000A| 10.00 + 4.00 | 15.00 + 5.00 | 20.00 + 5.00 | 25.00 + 5.00 |
| 0.1000000A| 25.00 + 4.00 | 30.00 + 5.00 | 35.00 + 5.00 | 40.00 + 5.00 |
| 1.0000000A| 100.00 + 10.00 | 100.00 + 10.00 | 110.00 + 10.00 | 115.00 + 10.00 |

## Wavetek 1281
- Model: Model 1281 Selfcal Digital Multimeter
- Manufacturer: Wavetek Corporation
- Source: [Datasheet](https://xdevs.com/doc/Datron/1281/doc/1281_spex.pdf)
- Open Source Data: [MACDRv1 JSON](https://github.com/ELOWRO/Meter-Accuracy/blob/main/Meters/Wavetek_1281.json)

### Transfer

#### DC Voltage Transfer

**Maximum time between measurements: 10 minutes**

**± (ppm of reading + ppm of range)**

| Range | Uncertainty |
|--:|:--:|
| 0.1000000V | 0.20 + 0.25  [23.0 ±1.0 °C] |
| 1.0000000V | 0.20 + 0.07  [23.0 ±1.0 °C] |
| 10.0000000V | 0.20 + 0.05  [23.0 ±1.0 °C] |
| 100.0000000V | 0.20 + 0.07  [23.0 ±1.0 °C] |
| 1000.0000000V | 0.20 + 0.05  [23.0 ±1.0 °C] |

#### Resistance 4-Wire Transfer

**Maximum time between measurements: 10 minutes**

**± (ppm of reading + ppm of range)**

| Range | Uncertainty |
|--:|:--:|
| 10.0000000Ω | 0.20 + 1.00  [23.0 ±1.0 °C] |
| 100.0000000Ω | 0.20 + 0.10  [23.0 ±1.0 °C] |
| 1000.0000000Ω | 0.20 + 0.10  [23.0 ±1.0 °C] |
| 10000.0000000Ω | 0.20 + 0.10  [23.0 ±1.0 °C] |
| 100000.0000000Ω | 0.20 + 0.01  [23.0 ±1.0 °C] |
| 1000000.0000000Ω | 0.30 + 0.01  [23.0 ±1.0 °C] |
| 10000000.0000000Ω | 2.00 + 0.01  [23.0 ±1.0 °C] |
| 100000000.0000000Ω | 40.00 + 1.00  [23.0 ±1.0 °C] |
| 1000000000.0000000Ω | 400.00 + 1.00  [23.0 ±1.0 °C] |

### Absolute Value

#### DC Voltage
**± (ppm of reading + ppm of range)**

| Range | 1 days | 365 days |
|--:|:--:|:--:|
| 0.1000000V| 1.00 + 0.50 | 6.00 + 0.50 |
| 1.0000000V| 0.50 + 0.20 | 3.00 + 0.20 |
| 10.0000000V| 0.50 + 0.10 | 3.00 + 0.10 |
| 100.0000000V| 1.00 + 0.20 | 6.00 + 0.20 |
| 1000.0000000V| 1.00 + 0.20 | 6.00 + 0.20 |

#### Resistance 4-Wire
**± (ppm of reading + ppm of range)**

| Range | 1 days | 365 days |
|--:|:--:|:--:|
| 10.0000000Ω| 3.00 + 1.00 | 12.00 + 1.00 |
| 100.0000000Ω| 1.50 + 0.30 | 8.00 + 0.30 |
| 1000.0000000Ω| 1.00 + 0.30 | 6.00 + 0.30 |
| 10000.0000000Ω| 1.00 + 0.30 | 6.00 + 0.30 |
| 100000.0000000Ω| 1.00 + 0.30 | 6.00 + 0.30 |
| 1000000.0000000Ω| 2.00 + 0.70 | 10.00 + 0.70 |
| 10000000.0000000Ω| 4.00 + 4.00 | 20.00 + 4.00 |
| 100000000.0000000Ω| 30.00 + 45.00 | 200.00 + 45.00 |
| 1000000000.0000000Ω| 300.00 + 450.00 | 2000.00 + 450.00 |
