## HW1 - Cross-site scripting

## Exercise
This week's exercise is to create a Flask server that is vulnerable cross-site scripting (XSS) with a server to handle the response.
* [HoldMyBeerSecurity blog post - Part 1: Learning web security - Reflected Cross-site Scripting(XSS)]()

## Setup env
1. `virtualenv -p python3 venv`
1. `source venv/bin/activate`
1. `pip3 install -r requirements.txt`

## Setup vulnerable Docker stack
1. `docker-compose up`

## Setup Modsec Docker stack
1. `docker-compose -f docker-compose-waf.yml build nginx-waf`
    1. It will take about ~15mins to build the NGINX container with modsec
1. `docker-compose -f docker-compose-waf.yml up`


## References 
* [Github - Best Practices for Non-root User #48](https://github.com/mhart/alpine-node/issues/48)
* [Python 3 : Convert string to bytes](https://www.mkyong.com/python/python-3-convert-string-to-bytes/)
* [Stackoverflow - How to read a text file into a string variable and strip newlines?](https://stackoverflow.com/questions/8369219/how-to-read-a-text-file-into-a-string-variable-and-strip-newlines)
* [Simple Python HTTP(S) Server — Example](https://blog.anvileight.com/posts/simple-python-http-server/)
* [StackOverFlow - Sending a JSON to server and retrieving a JSON in return, without JQuery](https://stackoverflow.com/questions/24468459/sending-a-json-to-server-and-retrieving-a-json-in-return-without-jquery)
* [Compiling and Installing ModSecurity for NGINX Open Source](https://www.nginx.com/blog/compiling-and-installing-modsecurity-for-open-source-nginx/)
* [Github issue - Failed to load locate the unicode map file from: unicode.mapping 20127](https://github.com/SpiderLabs/ModSecurity/issues/1941)
* [Github - https://github.com/vijay-nallagatla/nginx_production_config/blob/master/Dockerfile - Dockerfile](https://github.com/vijay-nallagatla/nginx_production_config/blob/master/Dockerfile)
* [NGINX With ModSecurity and Brotli: Production setup (Dockerized)](https://medium.com/swlh/nginx-with-modsecurity-and-brotli-production-setup-dockerized-2d1407600415)
* [Module ngx_http_upstream_module](http://nginx.org/en/docs/http/ngx_http_upstream_module.html?)
