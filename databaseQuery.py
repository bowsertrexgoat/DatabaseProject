import json
import os

def organize(data):
    for key in data.values():
        for item in key:
            print(item)
    return

def writeItemToDB(data,maxLength):
    name = input("TYPE THE NAME OF YOUR ITEM: ")
    serialId = input("TYPE THE ITEM'S SERIAL ID: ")
    lastCalibrationDate = input("TYPE THE ITEM'S LAST CALIBRATION DATE: ")
    calibrationDueDate = input("TYPE THE ITEM'S CALIBRATION DUE DATE: ")
    data["items"].append({
        "ID": maxLength,
        "NAME": name,
        "SERIAL ID": serialId,
        "LAST CALIBRATION DATE": lastCalibrationDate,
        "CALIBRATION DUE DATE": calibrationDueDate
            })
    with open("C:\\Users\\frisc\\OneDrive\\Desktop\\ShivProjects\\DatabaseProject\\randomData.json", "w") as file:
        json.dump(data,file,indent=2)
    print("SUCESS!")

def removeItemByNameFromDB(data):
    name = input("TYPE THE NAME OF THE ITEM YOU WANT TO REMOVE: ")
    for list in data.values():
           for item in list:
                if item["NAME"] == name:
                     list.remove(item)
                     with open("C:\\Users\\frisc\\OneDrive\\Desktop\\ShivProjects\\DatabaseProject\\randomData.json", "w") as file:
                         json.dump(data,file,indent=2)
                     print("SUCESS!")
                     return
    print(f"ITEM {name} NOT FOUND...")

def quit():
     os.system('cls')

maxLength = 0
while True:
    query = input("TYPE 1 TO VIEW DATA, TYPE 2 TO ADD ITEM, TYPE 3 TO REMOVE AN ITEM BY NAME, TYPE 4 TO QUIT: ")
    with open ("randomData.json","r") as file:
                data = json.load(file)
                if len(data["items"]) > maxLength:
                     maxLength = len(data["items"])
    match int(query):
        case 1:
            organize(data)
        case 2:
            writeItemToDB(data,maxLength)
        case 3:
            removeItemByNameFromDB(data)
        case 4:
            quit()
            break
    print("")

