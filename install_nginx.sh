#!/bin/bash
sudo apt-get install nginx
sudo cp -r config/nginx/* /etc/nginx/
sudo systemctl start nginx
sudo cp -r static /var/www/html/
