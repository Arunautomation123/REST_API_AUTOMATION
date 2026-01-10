import requests, json
from jsonschema import validate, ValidationError
import xmlschema

class TestSchemaValidation:
    def test_json_schema(self):
        url = 'https://mocktarget.apigee.net/json'
        res = requests.get(url)
        assert res.status_code == 200, "Wrong status code"

        data = res.json()

        # Load schema
        with open('./json_schema.json', 'r') as infile:
            schema = json.load(infile)

        try:
            validate(data, schema)
            print("Validated JSON Schema")
        except ValidationError as e:
            print(e)
            assert False, "Validation Error"

    def test_xml_schema(self):
        url = 'https://httpbin.org/xml'
        res = requests.get(url)
        assert res.status_code == 200, "Wrong status code"

        print(res.text)
        schema = xmlschema.XMLSchema("./XMLschema.xsd")

        try:
            schema.validate(res.text)
            print("Validated XML Schema")
        except ValidationError as e:
            print(e)
            assert False, "Validation XML Error"