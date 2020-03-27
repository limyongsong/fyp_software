Make sure the following files/folders are present on the main folder (LabVIEW 2019 should also be installed, Python 3.6.9 should be installed):
/dependencies/
/images/
AverageBird.csv

When opening Overal_system_A.vi:
1). Select the correct Weight VISA resource name (typically com9)
2). Select the correct Camera Name (typically cam0)
For weight detection settings:
3). Select the delay before read(ms) to be '100-500'ms
4). Make sure Serial settings is; '9600' baurd rate, '8' data bits, 'None' parity, '1.0' stopbits, 'None' flow control

A0-X is weight first for start condition
A1-X is RFID first for start condition
