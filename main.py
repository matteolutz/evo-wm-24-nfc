from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *

import requests

import argparse

import time

parser = argparse.ArgumentParser("evo-wm-24-nfc")
parser.add_argument("id", help="Id that is used for the fronted to receive events from the correct sensor", type=int)
args = parser.parse_args()

API_URL = "http://evorasp1.local/api/nfc"
SENSOR_ID = args.id

pn532 = Pn532_i2c()
pn532.SAMconfigure()

print("[EVO-NFC] Waiting for NFC card...")

while True:
    card_data = pn532.read_mifare().get_data()
    print("[EVO-NFC] NFC Tag present, sending request...")
    try:
        requests.post(API_URL, json={'id': SENSOR_ID, 'tag': card_data.hex() })
        time.sleep(1)
    except Exception as e:
        print(f"[EVO-NFC] Failed to send request ({e})")

print(card_data)
