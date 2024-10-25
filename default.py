import json

data = {"items": [
	{"ID": 0,
	"NAME": "Mayo Duct",
	"SERIAL ID": "ABC-123",
	"LAST CALIBRATION DATE": "10/10/24",
	"CALIBRATION DUE DATE": "4/10/25"
	},
	{"ID": 1,
	"NAME": "Char Pip",
	"SERIAL ID": "PIP-447",
	"LAST CALIBRATION DATE": "3/10/24",
	"CALIBRATION DUE DATE": "7/10/24"
	},
	{"ID": 2,
	"NAME": "Biff Buffer",
	"SERIAL ID": "BUFF-777",
	"LAST CALIBRATION DATE": "12/1/23",
	"CALIBRATION DUE DATE": "12/1/24"
	},
	{"ID": 3,
	"NAME": "Dryder",
	"SERIAL ID": "LDR444",
	"LAST CALIBRATION DATE": "7/5/24",
	"CALIBRATION DUE DATE": "11/5/24"
	}],
	"ID incrementer": 4
} 
with open("C:\\Users\\frisc\\OneDrive\\Desktop\\ShivProjects\\DatabaseProject\\randomData.json", "w") as file:
	json.dump(data,file,indent=2)
	