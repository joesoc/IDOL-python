__author__ = "Vinay Joseph"

import requests
import os
import configparser
import xml.etree.ElementTree as ET
from xml.etree import ElementTree

from xml import etree
from xml.dom import minidom

IDOL_HOSTNAME = 'localhost'
IDOL_ACI_PORT = ''
IDOL_config_filename = 'C:\HewlettPackardEnterprise\IDOLServer-11.0.1\idolserver.cfg'

def prettify(elem):
	"""Return a pretty-printed XML string for the Element.
	"""
	rough_string = ElementTree.tostring(elem, 'utf-8')
	reparsed = minidom.parseString(rough_string)
	return reparsed.toprettyxml(indent="  ")

def get_IDOLServer_ACI_PORT():
	config = configparser.ConfigParser()
	config.read(IDOL_config_filename)
	if 'Server' in config.sections():
		return config['Server']['Port']

def aci_call(category):
	action = "CategoryGetHierDetails"
	get_category_details_action_url = "http://{0}:{1}/action={2}&Category={3}".format(IDOL_HOSTNAME, IDOL_ACI_PORT, action, category)
	resp = requests.get(get_category_details_action_url)
	print("Status = {0}".format(resp.status_code))
	print("Content Type = {0}".format(resp.headers['content-type']))
	print("Encoding = {0}".format(resp.encoding))
	print("------------------------------------")
	
	tree = ET.fromstring(resp.text)
	print(prettify(tree))
	return tree


def get_category_hierarchy_details(category):
	tree = aci_call(category)
	return tree

IDOL_ACI_PORT = get_IDOLServer_ACI_PORT()

root = get_category_hierarchy_details(1)

