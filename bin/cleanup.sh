#!/bin/bash

echo 'Stop all containers'
sudo docker stop $(sudo docker ps | awk '{print $1}')
echo 'Remove all containers'
sudo docker rm $(sudo docker ps -a | awk '{print $1}')
echo 'Remove all volumes'
sudo docker volume rm $(sudo docker volume ls | awk '{print $2}')
echo 'Remove all networks'
sudo docker network rm $(sudo docker network ls | awk '{print $1}')
echo 'Done'
