#!/usr/bin/env python3
import requests
import os
from .error import RequestNotFound, RequestInvalid

# Create globals
base_url = "https://3.basecampapi.com"

class AuthenticateUser(API_TOKEN=None):
    def __init__(self, API_TOKEN):
        if API_TOKEN is None:
            pass
        else:
            return os.environ["API_TOKEN"]



class BC4(API_TOKEN=None):
    def __init__(self, API_TOKEN):
        self.token = AuthenticateUser(API_TOKEN)

    def make_request(self, request=None):
        try:
            if request is None:
                raise RequestNotFound
        except RequestNotFound:
            print("Exception: request returned NoneType, expected <str>")
