#!/bin/bash

echo "[EVO-NFC] Hello!"

echo "[EVO-NFC] Checking if venv exists.."
if [ ! -d "venv" ]; then
    echo "[EVO-NFC] Creating venv.."
    python3 -m venv venv
fi

echo "[EVO-NFC] Activating venv.."
source venv/bin/activate

echo "[EVO-NFC] Installing dependencies.."
pip3 install -r requirements.txt

echo "[EVO-NFC] Running main.py.."
python3 main.py $1

echo "[EVO-NFC] Goodbye!"
