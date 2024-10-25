import json
import os

def organize(dataList):
    for item in dataList:
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
    maxLength += 1
    data["ID incrementer"] = maxLength
    with open("C:\\Users\\frisc\\OneDrive\\Desktop\\ShivProjects\\DatabaseProject\\randomData.json", "w") as file:
        json.dump(data,file,indent=2)
    print("SUCESS!")

def removeItemByNameFromDB(data,dataList):
    name = input("TYPE THE NAME OF THE ITEM YOU WANT TO REMOVE: ")
    for item in dataList:
        if item["NAME"] == name:
            dataList.remove(item)
            data['items'] = dataList
            with open("C:\\Users\\frisc\\OneDrive\\Desktop\\ShivProjects\\DatabaseProject\\randomData.json", "w") as file:
                json.dump(data,file,indent=2)
            print("SUCESS!")
            return
    print(f"ITEM {name} NOT FOUND...")

def searchByName(dataList):
    name = input("TYPE THE NAME OF THE ITEM YOU WANT SEARCH FOR: ")
    for item in dataList:
        if item["NAME"] == name:
            print(item)
    print("")
    return

def quit():
     os.system('cls')

os.system('cls')
while True:
    query = input("TYPE 1 TO VIEW DATA, TYPE 2 TO ADD ITEM, TYPE 3 TO REMOVE AN ITEM BY NAME, TYPE 4 TO SEARCH, TYPE 5 TO QUIT: ")
    with open ("randomData.json","r") as file:
                data = json.load(file)
    maxLength = data["ID incrementer"]
    dataList = data["items"]

    try:
      int(query)   
    except:
        continue
    
    match int(query):
        case 1:
            organize(dataList)
        case 2:
            writeItemToDB(data,maxLength)
        case 3:
            removeItemByNameFromDB(data,dataList)
        case 4:
            searchByName(dataList)
        case 5:
            quit()
            break
    print("")

