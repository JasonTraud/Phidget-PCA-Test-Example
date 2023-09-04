# Phidget-PCA-Test-Example
Basic PCA level automated test example using Phidgets to power cycle a circuit board, take voltage data, plot, and store data in a CSV.

## Wiring Diagram
![Wiring Diagram](https://github.com/JasonTraud/Phidget-PCA-Test-Example/blob/main/images/wiring_diagram.png?raw=true "Wiring Diagram")

For the purposes of this example the PCA under test is just a power supply in order to accentuate the output waveform. For a practical application this would be tied to whatever output or test signal that you wish to measure. 

### BOM
- [VINT Phidget HUB0001_0](https://www.phidgets.com/?tier=3&catid=64&pcid=57&prodid=1202)
- [Votage Input Phidget VCP1000_0](https://www.phidgets.com/?tier=3&catid=106&pcid=86&prodid=953)
- [Relay Phidget REL2001_0](https://www.phidgets.com/?tier=3&catid=46&pcid=39&prodid=722)
- Generic Power Supply

## GUI
![Form GUI](https://github.com/JasonTraud/Phidget-PCA-Test-Example/blob/main/images/form_gui.png?raw=true "Form GUI")

Basic form accepts:
- **Serial Number:** Tagged serial number for DUT that's tagged in output file names
- **Start Up:** Time in seconds data is collected prior to test (before power-up)
- **Duration:** Time in seconds data is collected during the test
- **Shutdown:** Time in seconds data is collected after test (after power-down)
- **Trials:** Number of iterations of test

# Output Data Files

The output data files are named in the syntax "YYYY-MM-DD HH-MM-SS [Serial Number]". For example "2023-09-03 13-05-21 SN12345"

The output data plot would appear as follows if the the voltage input Phidget was connected to a 3.3V supply. Each trial is overlayed.

![Output Plot](https://github.com/JasonTraud/Phidget-PCA-Test-Example/blob/main/images/test_output.png?raw=true "Output Plot")

The output CSV file is in the format below. 

| Sample    | Trial     | Elapsed   | Data      |
| --------- | --------- | --------- | --------- |
| 0         | 0         | 0         | -0.0027   |
| 1         | 0         | 0.012917  | -0.0027   |
| ...       | ...       | ...       | ...       |