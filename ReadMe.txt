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


save_data.py is used to create folder and files to store data 
-should called the main() function in labview (it should have 3 inputs) (rfid, weight, imageID)

-----
Note: 
Python should be 3.6 or 2.7 and should be 32-bit version at the default location (since our labview is 32bit and only compatible w/ 3.6 and 2.7 and looks at the default location?)
To get the correct version: https://forums.ni.com/t5/LabVIEW/Labview-2018-Python-Node-and-Anaconda-Environment/td-p/3853701/page/2?profile.language=en
(do not use anaconda)
1).Install python 3.6 from https://www.python.org/downloads/release/python-360/
(install default location, should be installed to C:\Users\experiment\AppData\Local\Programs\Python\Python36-32)
Remember to tick set path during installation
Check 'python' and 'pip' at command prompt
-make sure it is 3.6.0
1b(not always needed)).download pip from and follow instructions https://www.liquidweb.com/kb/install-pip-windows/ if not installed
2).Install all the relevant libraries using pip install
e.g
"type "pip install numpy", "pip install pandas" and the other libraries that you want. 

----

Telegram bot master API for message sending: https://github.com/ladikvadim/Telegram-Bot
