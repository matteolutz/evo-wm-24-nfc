#!/bin/bash

source venv/bin/activate

echo "[EVO-NFC] Starting NFC.."
echo "[EVO-NFC] Installing dependencies.."
pip3 install -r requirements.txt

echo "[EVO-NFC] Running main.py.."
python3 main.py $1

echo "[EVO-NFC] Goodbye!"
