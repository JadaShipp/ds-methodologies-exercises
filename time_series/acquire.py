import pandas as pd
import numpy as np
import requests


def get_response(url):
    '''
    Function to pass in a url
    return the data in JSON 
    '''
    base_url = url
    response = requests.get(base_url + '/documentation')
    print(response.json()['payload'])