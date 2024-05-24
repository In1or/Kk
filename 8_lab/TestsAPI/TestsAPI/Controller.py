import jsonschema.exceptions
import requests
from conf import urls 
import jsonschema
import json

class Controller:  
    def get_all(self):
        data = requests.get(urls.BASE_URL + urls.GET_ALL_PRODUCTS)
        return data.json()
    
    def create(self, product):
        data = requests.post(urls.BASE_URL + urls.ADD_PRODUCT, json=product)
        try:
            return data.json()
        except:
            return None
        
    def delete(self, id):
        data = requests.get(urls.BASE_URL + urls.DELETE_PRODUCT, params={'id': id})
        return data.json() 
    
    def edit(self, product):
        data = requests.post(urls.BASE_URL + urls.EDIT_PRODUCT, json=product)
        try:
            return data.json()
        except:
            return None