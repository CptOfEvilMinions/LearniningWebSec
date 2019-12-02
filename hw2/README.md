# HW2 - Cross-Site Request Forgery (CSRF)

## Development
1. `virtualenv -p python3 venv`
1. `python3 run_vulnerable_server.py`

## Spin up with Docker
1. `docker-compose up -d`

## Spin up with Docker and modsec WAF
1. `cd ../Docker-waf`
1. `docker build -t learnwebsec-nginx-modsec:v1 .`
1. `cd ../hw2`
1. `docker-compose -f docker-compose-waf.yml up`

## References
* [StackOverFlow - How does one detect if one is running within a docker container within Python?](https://stackoverflow.com/questions/43878953/how-does-one-detect-if-one-is-running-within-a-docker-container-within-python)
* [Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/)
* [CSRF Protection](https://flask-wtf.readthedocs.io/en/stable/csrf.html)
* [Using Flask-Login to Handle User Accounts](https://hackersandslackers.com/authenticating-users-with-flask-login/)
* [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)
* [How to view HTTP headers in Google Chrome?](https://www.mkyong.com/computer-tips/how-to-view-http-headers-in-google-chrome/)
* [Python SimpleHTTPServer Recipe: Enable CORS](http://louistiao.me/posts/python-simplehttpserver-recipe-enable-cors/)
* [Stackoverflow - Send POST data using XMLHttpRequest](https://stackoverflow.com/questions/9713058/send-post-data-using-xmlhttprequest)
* [XMLHttpRequest.withCredentials](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/withCredentials)