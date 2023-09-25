from os import path
import json

from utils import write

config_path = path.join(path.dirname(__file__), 'config.json')

def get_config(default_config):
	if path.exists(config_path):
		config = {}
		with open(config_path, "r", encoding="utf8") as f:
			config = json.loads(f.read())
		return config
	else:
		with open(config_path, "w", encoding="utf8") as f:
			f.write(json.dumps(default_config, indent=4))
		write("No Config.json. Creating new one", 2)
		exit()
