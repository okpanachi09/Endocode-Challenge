import unittest
import requests
import urllib
import threading

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.main import *

ABS_URL = "http://127.0.0.1:8080"

class TestRequests(unittest.TestCase):
    def test_req_stranger(self):
        # construct the endpoint url
        global ABS_URL
        request_url = urllib.parse.urljoin(ABS_URL, 'helloworld')
        print("req url: {}".format(request_url))
        r = requests.get(url=request_url)
        data = r.text
        print("received response {}".format(data))
        self.assertEqual(data, "Hello Stranger")

    def test_req_named(self):
        global ABS_URL
        # construct the endpoint url
        request_url = urllib.parse.urljoin(ABS_URL, 'helloworld')
        params = {'name': 'TestValue'}
        r = requests.get(url=request_url, params=params)
        print("req url: {}".format(r.request.url))
        data = r.text
        print("received response {}".format(data))
        self.assertEqual(data, "Hello Test Value")


class TestUnitFunctionality(unittest.TestCase):
    def test_name_split(self):
        name = "TestBValue"
        split_res = split_name_by_uppercase(name)
        self.assertEqual(split_res, "Test B Value")

if __name__ == "__main__":
    # expect the application to be working in background
    unittest.main()
