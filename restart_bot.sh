#!/bin/bash

/usr/bin/docker stop composterbot
/usr/bin/docker rm composterbot 

/usr/bin/git pull

/usr/bin/docker build -t composterbot .
/usr/bin/docker run --restart unless-stopped -d --name composterbot composterbot