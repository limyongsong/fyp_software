#This script aims to create folders at the target location every 1st day of the month (or any other day if there are no readings on 1st day)
#Files are created and updated everyday based on the readings (default values are XXX), Data stored are time,rfid,weight,imageID
#At the start of the next month (during the 1st reading), all data from previous months will be collated into a single csv file
#End result should be to have monthly folders that contain daily files
import os
import time
from datetime import date
from datetime import datetime
from argparse import ArgumentParser
import pandas as pd

#every 1st day of the month, we want to create a new directory
def create_dir(today,dirpath):
	newdir = dirpath+"\\"+str(today)
	if not (os.path.isdir("./"+str(today))): # if dir does not exist
		os.mkdir(newdir) #create new folder to store data for new month

#compile the previous month data into a graph
def compile_prev(today,dirpath):
	if (str(today)[-5:-3]=="01"): #check the current month, cause want collate previous month data
		str_month = str(12)
	else:
		month = int(str(today)[-5:-3])-1 #change month to correct format
		if month<10:
			str_month = "0"+str(month) 
		else:
			str_month = str(month)
	lastmonth = str(today)[0:5] + str_month + str(today)[-3:]
	if (os.path.isdir("./"+lastmonth)):
		flag = 0
		for filename in os.listdir(dirpath +"\\"+lastmonth): #compile all the csv file of the prev month together
			if filename.endswith(".csv") and flag == 0:
				my_data = pd.read_csv(dirpath +"\\"+lastmonth+"\\"+filename)
				flag = 1
			elif filename.endswith(".csv"):
				my_data = my_data.append(pd.read_csv(dirpath +"\\"+lastmonth+"\\"+filename),ignore_index=True,sort=False)
		my_data.to_csv(dirpath +"\\"+lastmonth+"\\"+ "compiled_" +str_month+".csv",mode='w+')
	else:
		None #here means previous month folder does not exist

#creates or updates the files everyday when there is a new reading
def update_file(dirpath, today, currentmonth, now, rfid, weight, imageID):
	currentmonth_folder = str(today)[0:5] + currentmonth + "-01"
	if (os.path.isdir("./"+currentmonth_folder)): # if the folder exist then do stuff
		if not (os.path.isfile("./"+currentmonth_folder+"\\"+str(today)+".csv")): #if file not yet created for that day
			f = open(currentmonth_folder+"\\"+str(today)+".csv", "w+") #create new file
			f.write("time,rfid,weight,imageID\n")
		else:
			f = open(currentmonth_folder+"\\"+str(today)+".csv", "a+")
		f.write(str(now) + "," + rfid + "," + weight + "," + imageID + "\n")
	else: 
		newdir = dirpath+"\\"+str(today)[0:5] + currentmonth + "-01"
		os.mkdir(newdir) #create new folder to store data for new month if day 1 not created
		if not (os.path.isfile("./"+currentmonth_folder+"\\"+str(today)+".csv")): #if file not yet created for that day
			f = open(currentmonth_folder+"\\"+str(today)+".csv", "w+") #create new file
			f.write("time,rfid,weight,imageID\n")
		else:
			f = open(currentmonth_folder+"\\"+str(today)+".csv", "a+")
		f.write(str(now) + "," + rfid + "," + weight + "," + imageID + "\n")

def main(rfid, weight, imageID):
	dirpath = os.getcwd() #might need change for labview integration to determine where to place the files
	today = date.today()
	now = datetime.now()#.strftime("%H:%M:%S")# add this is dont want date
	if (str(today)[-2:]=="01") and not (os.path.isdir("./"+str(today))): #first day of month do stuff
		create_dir(today,dirpath)
		compile_prev(today,dirpath)
	currentmonth = str(today)[-5:-3]
	update_file(dirpath, today, currentmonth, now, rfid, weight, imageID)

if __name__ == "__main__":
	parser = ArgumentParser(description='Store data from labview')
	parser.add_argument('-rfid', dest='rfid', default='XXXX-XXXX-XXXX',help='input RFID, e.g., 00AB-11CD-22EF')
	parser.add_argument('-weight', dest='weight', default='XX',help='input weight in grams, e.g., 10')
	parser.add_argument('-imageID', dest='imageID', default='XXXXXXXX',help='input imageID, i.e. where to get the image, e.g., abcd1234.jpg')
	args = parser.parse_args()
	main(args.rfid, args.weight, args.imageID)
