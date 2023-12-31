#!/bin/bash

python3 -m pip install -r requirements.txt --break-system-packages

sudo apt install nodejs
curl -L https://npmjs.org/install.sh | sudo sh 

sudo npm install pm2 -g

pm2 start pm2.config.json