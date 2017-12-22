#!/bin/bash
sudo rm Output/*
sudo rm Features/*
sudo rm Contours/*
sudo docker-compose down
sudo docker-compose up -d