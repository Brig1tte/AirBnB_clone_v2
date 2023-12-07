#!/usr/bin/env bash
# A Bash script to set up web servers for the deployment of web_static

# first install nginx if it does not exist
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# then create a data folder and its sub folders
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# create a file
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

# create a link to point to the data sub folders
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# grant ownership to Ubuntu
sudo chown -hR ubuntu:ubuntu /data/

# configure nginx to server /data/web_static/current/ to hbnb_static
# eg https://mydomainname.tech/hbnb_static
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart
