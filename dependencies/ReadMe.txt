
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
some commonly installed are numpy, opencv-python, matplotlib, scipy, scikit-learn, pillow, pandas, tensorflow (compatible just with Python 64bits) and keras."

telegrambotmaster is the telegram chatbot

http://www.ni.com/product-documentation/7593/en/ to see how subvi
https://forums.ni.com/t5/Example-Programs/Convert-IMAQ-Image-into-LabVIEW-Image-data-type/ta-p/3522168?profile.language=en
