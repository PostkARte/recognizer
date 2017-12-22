#!/bin/bash
sudo rm Output/*
sudo rm Features/*
sudo docker-compose down
sudo docker-compose up -d