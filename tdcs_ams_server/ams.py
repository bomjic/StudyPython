#! /usr/bin/env python

import web
import os
import hashlib
import json
import csv
import sys
import logging
import string
import yaml

class YamlConfig:
	def __init__(self, config_name=None):
		self.env_config = {}
		if config_name:
			self.load(config_name)

	def get(self, name):
		return self.get_default(name, None)

	def get_default(self, name, default=''):
		cur_lvl = self.env_config
		for subpath in name.split('.'):
			if not subpath in cur_lvl:
				return default
			cur_lvl = cur_lvl[subpath]
		return cur_lvl

	def load(self, config_name):
		try:
			with open(config_name, 'r') as yamlfile:
				logging.info("Loading configuration from " + config_name)
				try:
					self.env_config = yaml.load(yamlfile)
				except yaml.YAMLError as e:
					logger.error(e)
		except IOError, e:
				pass

#logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

#ROOT_DIR = os.path.expanduser("~")
ROOT_DIR = "/home/mikhail/Documents/StudyPython/tdcs_ams_server"
CONFIG_FILE_NAME = os.path.join(ROOT_DIR, "config.yaml")
LOOKUPDB_FILE_NAME = os.path.join(ROOT_DIR, "stblookupmiddle.csv")
UPGRADEDB_FILE_NAME = os.path.join(ROOT_DIR, "upgradedb.yaml")
HTTP_LOCAL_DIR='/srv/http/DCD/HTTP'

config = YamlConfig(CONFIG_FILE_NAME)
SERVER_PORT = config.get_default('server.port', 6666)
SERVER_ADDR = config.get_default('server.addr', '172.30.112.19')

default_stb_lookup = {
	'lineupId' : 1,
	'TZ'       :'MST7MDT,M3.2.0,M11.1.0',
	'groupCdl' : 0,
	'groupCds' : 0,
	'tdcs_url' : 'http://' + SERVER_ADDR + ':' + str(SERVER_PORT) + '/ams/TDCS',
}

urls = (
	'/ams/STBLookupService', 'stblookup',
	'/ams/TDCS', 'tdcs'
)

def load_db(db, filename):
	try:
		with open(filename, 'rb') as csvfile:
			reader = csv.DictReader(csvfile, delimiter=',')
			for row in reader:
				if not 'mac' in row:
					logging.warning('Invalid db entry')
					continue

				mac = row['mac']
				row.pop('mac', None)
				db[mac] = row
	except:
		logging.error("No valid database file found! '" + filename + "'")
		sys.exit(1)

def get_pci_version(imagename):
	return str(int(imagename.split("_")[4], 16))

def get_dri_version(imagename):
	all = string.maketrans('', '')
	nodigs = all.translate(all, string.digits)
	return imagename.split("_")[4].translate(all, nodigs)

def sha256(fname):
	sha = hashlib.sha256()
	try:
		with open(fname, "rb") as f:
			for chunk in iter(lambda: f.read(4096), b""):
				sha.update(chunk)
	except:
		logging.error("Cannot calculate sha256 for " + fname)
		return ""

	return sha.hexdigest()

def has_component(component, targets):
	for c in targets:
		if c['objectType'] == component:
			return True
	return False

def addobj(targets, imgtype, version, filename, priority='delayed'):
	f = HTTP_LOCAL_DIR + '/' + str(filename)
	if not os.path.isfile(f):
		return

	item = {}
	item['objectType'] = str(imgtype)
	item['url'] = 'http://' + SERVER_ADDR + '/DCD/HTTP/' + str(filename)
	item['swVersion'] = str(version)
	item['priority'] = str(priority)
	item['size'] = os.path.getsize(f)
	item['sha256'] = sha256(f)

	targets.append(item)

def process_target(target, cfrom, cto, mac, priority='delayed'):
	if has_component(target, cfrom):
		img = upgradedb.get('STB'+ mac + '.' + target)
		if not img:
			img = upgradedb.get('default.' + target)

		if img:
			if target == 'PCI':
				version = get_pci_version(img)
			elif target == 'DRI':
				version = get_dri_version(img)
			else: #CAS
				version = '666'

			logging.debug(target + ' image for ' + mac + ': ' + img + ' (' + version + ')')
			addobj(cto, target, version, img, priority)

class AMS(web.application):
	def run(self, port=8080, *middleware):
		func = self.wsgifunc(*middleware)
		return web.httpserver.runsimple(func, ('::', port))

class stblookup:
	def GET(self):
		data = web.input(mac=None, sgid=None)
		if not data.mac:
			logging.error('Invalid stblookup request')
			return None

		logging.debug('StbLokupMiddle request for mac: "' + data.mac + '" and sgid: "' + str(data.sgid) + '"')

		if not data.mac in lookupdb:
			logging.debug('Return default lookup answer: ' + str(default_stb_lookup))
			return json.dumps(default_stb_lookup)

		return json.dumps(lookupdb[data.mac])

class tdcs:
	def POST(self):
		data = web.data();
		try:
			payload = json.loads(data)
			logging.debug(json.dumps(payload, indent=4))
		except:
			logging.error('Not a json payload: ' + data)
			return None

		if not 'targets' in payload:
			logging.error('No targets found in request')
			return None

		mac = payload['mac'].upper()
		if not mac:
			logging.error('No MAC address in request')
			return None

		t = []

		logging.debug('Check updates for: ' + mac)
		process_target('PCI', payload['targets'], t, mac, 'immediate')
		process_target('DRI', payload['targets'], t, mac, 'immediate')
		process_target('CAS', payload['targets'], t, mac)

		ans = {}
		ans['targets'] = t
		return json.dumps(ans);


lookupdb = {}
load_db(lookupdb, LOOKUPDB_FILE_NAME)

upgradedb = YamlConfig(UPGRADEDB_FILE_NAME)

if __name__ == "__main__":
	app = AMS(urls, globals())
	app.run(port=SERVER_PORT)

