import requests, json, random

for i in range(100):
	url = "http://localhost:9090/invoice_fe/CREATE_INVOICE/"

	payload = json.dumps([
	  {
	    "CODIGO": i + 1,
	    "DESCRIPCION": "harina",
	    "VAL. UNIT": random.randint(1500, 5000),
	    "IVA": '19%',
	    "VAL. DESC.": 0,
	    "CANTIDAD": "1",
	    "date": "2022-12-14",
	    "date_expired": "2022-12-14",
	    "time": "21:45",
	    "payment_form": 1,
	    "cancelled": True,
	    "employee": 1,
	    "client": 4,
	    "company": 3,
	    "type": 1
	  }
	])
	headers = {
	  'Content-Type': 'application/json'
	}
	response = requests.request("POST", url, headers=headers, data=payload)
	print(response.text)