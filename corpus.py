import requests
import time
# import json

from utils import write
from config import get_config

def main():
	write("Loading config")
	config = get_config({
			"token": "",
			"channel": "",
			"blacklist": []
		})
	
	while True:
		time.sleep(1)
		write("tick")
	
		try:
			messages = requests.get(f"https://discord.com/api/v9/channels/{config['channel']}/messages?limit=5", headers={"authorization": config['token']}).json()
			for message in messages:
				# print(json.dumps(message, indent=4))
				if message['author']['id'] in config['blacklist']:
					write(f"Deleting {message['author']['username']} messages")
					delete_response = requests.delete(f"https://discord.com/api/v9/channels/{config['channel']}/messages/{message['id']}", headers={"authorization": config['token']})
					if delete_response.status_code == 204:
						write("Delete succesful")
					else:
						write(f"Delete failed: {delete_response.text}", 2)
		except Exception as e:
			write(f"Loop Error: {e}", 2)

if __name__ == "__main__":
	main()