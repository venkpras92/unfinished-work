"""
Class Brand : Accepts dictionary object while instantiation.
Class Brand Methods : set_brand_name, get_brand_name, set_brand_description,
                get_brand_description, dump_schema, get_schema
"""
import json
class Brand:

    # Pass dictionary with keys 'name' and 'description' 
    # if user wants to set values while object instantiation
    def __init__(self, idict: dict = {}):
        self._type = 'Brand'
        self._context = 'http://www.schema.org'
        self._brand_name = idict.get('name')
        self._brand_description = idict.get('description')

    # Method to manually set the value of brand_name by passing a string object
    def set_brand_name(self, value: str):
        self._brand_name = value
    
    # Method to retrieve the brand_name property
    def get_brand_name(self):
        return(self._brand_name)

    # Method to manually set the brand_description property by pasing a string object
    def set_brand_description(self, value: str):
        self._brand_description = value
    # Method to retrieve the brand_description property
    def get_brand_description(self):
        return(self._brand_description)

    # Method to print the brand object JSON-LD to console
    def dump_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['name'] = self._brand_name
        self.d['description'] = self._brand_description
        self.djson = json.dumps(self.d)
        print(self.djson)
    
    # Method to retrieve the brand object JSON-LD elsewhere
    def get_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['name'] = self._brand_name
        self.d['description'] = self._brand_description
        self.djson = json.dumps(self.d)
        return(self.djson)