import xml

import requests
import xmltodict
import json
from xml.dom.minidom import parseString
class TestXMLParsing:
    def test_xml_response(self):
        """
        validates:
         - HTTP status code
         - CONTENT TYPE
         - SPECIFIC XML ELEMENT VALUES
        :return:
        """
        url = 'https://mocktarget.apigee.net/xml'

        resp = requests.get(url)
        assert resp.status_code == 200, 'Wrong status code'
        print(parseString(resp.text).toprettyxml())

        assert resp.headers['content-type'] == 'application/xml; charset=utf-8', 'Wrong content type'

        xml_data = xmltodict.parse(resp.text)
        # print(xml_data)
        print(json.dumps(xml_data, indent=4))

        root = xml_data['root']
        assert root['city'] == 'San Jose', "Wrong city"
        assert root['state'] == 'CA', "Wrong state"

    def test_xml_response_2(self):
        """
        validates:
         - HTTP status code
         - CONTENT TYPE
         - SPECIFIC XML ELEMENT VALUES
        :return:
        """
        url = 'https://httpbin.org/xml'

        resp = requests.get(url)
        assert resp.status_code == 200, 'Wrong status code'
        # print(parseString(resp.text).toprettyxml())

        assert resp.headers['content-type'] == 'application/xml', 'Wrong content type'

        json_data =xmltodict.parse(resp.text)
        json_string = json.dumps(json_data, indent=4)
        # print(json_string)   

        data = json_data['slideshow']
        assert data['@title'] == 'Sample Slide Show', "Wrong title"
        assert data['@author'] == 'Yours Truly', "Wrong author"

        # no of slides
        slide = data['slide']
        assert len(slide) == 2, 'Wrong length'
        assert slide[0]['title'] == 'Wake up to WonderWidgets!', "Wrong slide 1"
        assert slide[1]['title'] == 'Overview', "Wrong slide 2"

        # slide2
        slide_2 = slide[1]['item']
        assert len(slide_2) == 3, 'Wrong length'
        assert slide_2[0]['em'] == 'WonderWidgets', "Wrong em"
        assert slide_2[1] == None, "Wrong slide 3"
        assert slide_2[2]['em'] == 'buys', "Wrong em"
