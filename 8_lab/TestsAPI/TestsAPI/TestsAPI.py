import jsonschema.exceptions
from Controller import Controller
import unittest
import jsonschema
import json
from parameterized import parameterized
import requests

class TestAPI(unittest.TestCase):
    def setUp(self):
        with open('TestData/exampleData.json') as file:
            self.__test_data = json.load(file)
            
        with open('conf/productsForm.json') as file:
            self.__products_form = json.load(file)
            
        with open('conf/addUpProductForm.json') as file:
            self.__au_product_schema = json.load(file)
            
        self.__products_to_removed = []        
        self.__controller = Controller()
        
    def tearDown(self):
        for item in self.__products_to_removed:
            self.__controller.delete(item['id'])    

    @parameterized.expand([
        ['valid'],
        ['valid_id_min'],
        ['valid_id_max'],
        ['valid_hit'],
        ['valid_hit_min'],
    ])
    
    def test_add_valid_product(self, name):
        item = self.__test_data[name]
        self.assertTrue(self.check_valid_json(item, self.__au_product_schema), f'error with add {name} product')
        
        response = self.__controller.create(item)
        item['id'] = response['id']
        
        self.__products_to_removed.append(item)
        
        self.assertTrue(self.check_availability_by_id(item['id']), msg='error with adding item to list')  
        self.assertEqual(response['status'], 1, 'error with response status')

    def test_add_valid_alias(self):
        item = self.__test_data["valid_alias"]
        self.assertTrue(self.check_valid_json(item, self.__au_product_schema), f'error with add valid_alias product')
        response = self.__controller.create(item)
        item['id'] = response['id']
        self.__products_to_removed.append(item)


        item2 = self.__test_data["valid_alias"]
        self.assertTrue(self.check_valid_json(item, self.__au_product_schema), f'error with add valid_alias product')
        response2 = self.__controller.create(item)
        item2['id'] = response2['id']
        self.__products_to_removed.append(item2)

        item = self.get_by_id(response["id"])
        item2 = self.get_by_id(response2["id"])
        
        self.assertEqual(item["alias"] + "-0", item2["alias"], f'Error with alias')
        
    @parameterized.expand([
        ['null'],
        ['invalid_id'],
        ['invalid_price'],
        # ['invalid_status'],
        # ['invalid_hit'],
    ])
    def test_invalid_product(self, name):
        item = self.__test_data[name]

        self.assertFalse(self.check_valid_json(item, self.__products_form), 'error with add invalid product')
        response = self.__controller.create(item)
        if response != None:
            self.__products_to_removed.append(response)
        self.assertEqual(response, None, 'error with response status')
    
    def test_success_edit_product(self):
        item = self.__test_data['valid']
        response = self.__controller.create(item)
        item['id'] = response['id']
        self.__products_to_removed.append(item)
        
        item['content'] = 'pomenyal'
        item['keywords'] = 'euro'
        item['price'] = 52
        
        response = self.__controller.edit(item)
        edit_item = self.get_by_id(item['id'])
        
        self.assertTrue(self.check_valid_json(item, self.__au_product_schema), msg='error with success edit')
        self.assertEqual(item['content'], edit_item['content'], msg='error with editing')
        self.assertEqual(item['keywords'], edit_item['keywords'], msg='error with editing')
        self.assertEqual(str(item['price']), str(edit_item['price']), msg='error with editing')

    def test_edit_product_invalid_values(self):
        item = self.__test_data['valid']
        response = self.__controller.create(item)
        item['id'] = response['id']
        self.__products_to_removed.append(item)
        
        item['content'] = None
        item['keywords'] = '54666'
        item['price'] = 'slgbjhab'

        response = self.__controller.edit(item)
        self.assertFalse(self.check_valid_json(item, self.__au_product_schema), msg='error with edit invalid values')
        self.assertEqual(response, None, 'error with response status')

    def check_valid_json(self, json, schema):
        try:
            jsonschema.validate(json, schema)
        except jsonschema.exceptions.ValidationError as error:
            return False    
        return True       
    
    def check_availability_by_id(self, id):
        all = self.__controller.get_all()
        for item in all:
            if item['id'] == str(id):
                return True
        return False
    
    def get_by_id(self, id):
        all = self.__controller.get_all()
        for item in all:
            if item['id'] == str(id):
                return item
        return None 