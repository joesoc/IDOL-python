__author__ = "Vinay Joseph"

import requests
import os
import configparser
import xml.etree.ElementTree as ET


IDOL_HOSTNAME = 'localhost'
IDOL_ACI_PORT = ''


def get_IDOLServer_ACI_PORT():
	config = configparser.ConfigParser()
	IDOL_config_filename = 'C:\HewlettPackardEnterprise\IDOLServer-11.0.1\idolserver.cfg'
	config.read(IDOL_config_filename)
	if 'Server' in config.sections():
		return config['Server']['Port']

def get_category_details(category):
	action = "CategoryGetDetails"
	get_category_details_action_url = "http://{0}:{1}/action={2}&Category={3}".format(IDOL_HOSTNAME, IDOL_ACI_PORT, action, category)
	resp = requests.get(get_category_details_action_url)
	print("Status = {0}".format(resp.status_code))
	print("Content Type = {0}".format(resp.headers['content-type']))
	print("Encoding = {0}".format(resp.encoding))
	print("------------------------------------")
	
	tree = ET.fromstring(resp.text)

	return tree

def get_category_name(category):
	tree = get_category_details(category)
	for element in tree.iter('{http://schemas.autonomy.com/aci/}name'):
		return element.text

IDOL_ACI_PORT = get_IDOLServer_ACI_PORT()

name = get_category_name(1)
print(name)

