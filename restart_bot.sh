#!/bin/bash

@echo off

docker stop composterbot
docker rm composterbot 

git pull

docker build -t composterbot .
docker run --restart unless-stopped -d --name composterbot composterbot