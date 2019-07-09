#!/usr/bin/env python3
import requests
import json

def geocode(address):
        parameters = {'address': address, 'key': ''}
        base = 'http://restapi.amap.com/v3/geocode/geo'
        response = requests.get(base, parameters)
        answer = response.json()
        print(address + "的经纬度：", answer['geocodes'][0]['location'])
        result =answer['geocodes'][0]['location']
        json_str = json.dumps(result)
        fileObject = open('result.json', 'a')
        fileObject.write(json_str+'\n')
        fileObject.close()


if __name__=='__main__':
    json_data = """  """
    data = json.loads(json_data)
    for value in data['addressAll']:
        address = value['address']+value['name']
        geocode(address)


