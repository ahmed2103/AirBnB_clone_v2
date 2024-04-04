#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.

apt-get update
apt-get install nginx -y

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<h1>this content is a test</h1>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/  /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/
echo "
server {
	listen 80;
	listen [::]:80 default_server;
	add_header X-Served-By $HOSTNAME;
	root   /var/www/html;
	index  index.html index.htm;
	location /hbnb_static {
		alias /data/web_static/current/
		index.html index.htm
	}
    	location /redirect_me {
        	return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    	error_page 404 /404.html;
    	location /404 {
      	root /var/www/html;
      	internal;
    }
}" > etc/sites-available/default

service nginx restart

