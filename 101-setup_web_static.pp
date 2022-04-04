# sets up web servers for the deployement of web_static

exec { 'configure':
  provider => shell,
  command  => 'apt-get install -y nginx && mkdir -p /data/web_static/releases/test/ && mkdir -p /data/web_static/shared && echo "Hello world! from test" > /data/web_static/releases/test/index.html && ln -sfn /data/web_static/releases/test/ /data/web_static/current && chown -fR ubuntu:ubuntu /data/ && sed -i "28 a location /hbnb_static/ {\n\talias /data/web_static/current/;\n}\n" /etc/nginx/sites-enabled/default && service nginx restart',
}
