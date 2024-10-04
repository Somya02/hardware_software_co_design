# hardware_software_co_design
Final project presentation for hardware and software co-design

# Embedded Serial Utility

This Python-based utility communicates with an embedded system via serial ports to enable real-time data monitoring and device control. The utility helps reduce integration time and simplifies hardware debugging and testing.

## Features
- Serial communication with embedded devices.
- Real-time data monitoring.
- Hardware control via the serial port.

## Requirements
- Python 3.x
- pySerial
- matplotlib

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

# For data monitoring

```bash
python src/main.py --mode monitor
```

# For device control

```bash
python src/main.py --mode control --command "<your_command>"
```