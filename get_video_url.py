import requests
import json
import xml.etree.ElementTree as ET


def get_channel_m3u8(url):
    if 'rai1' == url:
        url = 'https://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=2606803&output=64'
    elif 'rai2' == url:
        url = 'https://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=308718&output=64'
    elif 'rai3' == url:
        url = 'https://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=308709&output=64'
    elif 'rai4' == url:
        url = 'https://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=746966&output=64'
    elif 'rai5' == url:
        url = 'https://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=395276&output=64'
    
    response = requests.get(url)
    if response.status_code == 403:
        return 403
    root = ET.ElementTree(response.content).getroot()
    for child in root:
        if child.tag == 'url' and child.attrib == {'type': 'content'}:
            url = child.text.replace('\n', '').replace('\t', '')
            return url
    
    # We have not found the URL
    return 404