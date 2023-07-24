from unittest import TestCase, main
import json
import requests

class TestCases(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def test_new_user(self):

        url = "http://127.0.0.1:8000/newUser"

        payload = json.dumps({
        "name": "mani",
        "email": "manichandrasaimani@gmail.com",
        "balance": 2000
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload).json()
        
        self.assertEqual(response["status"], "success")


    def test_updatefee(self) :
        url = "http://127.0.0.1:8000/updatefees"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        self.assertEqual(response["status"], "success")

    def test_transact(self):
        url = "http://127.0.0.1:8000/transact"

        payload = json.dumps({
        "u_id": 3,
        "m_id": 1,
        "amount": 600
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload).json()
        self.assertEqual(response["status"], "success")


    def test_getMerchant(self):
        url = "http://127.0.0.1:8000/getMerchant/8"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload).json()
        self.assertEqual(response["status"], "success")


    def test_repay(self):
        url = "http://127.0.0.1:8000/fee/swiggy"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload).json()
        self.assertEqual(response["status"], "success")

        
    def test_fee(self):
        url = "http://127.0.0.1:8000/dues/pooja"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload).json()
        self.assertEqual(response["status"], "success")


    def test_dues(self):
        url = "http://127.0.0.1:8000/dues/mani"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload).json()
        self.assertEqual(response["status"], "success")

    def test_usersAtLimit(self):
        url = "http://127.0.0.1:8000/usersAtLimit"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload).json()
        self.assertEqual(response["status"], "success")
    
    def test_new_merchant(self):
                             
   
   
     def test_totaldues(self):
        url = "http://127.0.0.1:8000/totalDues"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload).json()
        self.assertEqual(response["status"], "success")

if __name__ == '__main__':
    main()