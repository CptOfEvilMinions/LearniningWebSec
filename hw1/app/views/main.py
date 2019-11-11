from flask import request, Blueprint, render_template, make_response
from datetime import datetime
from app import app

# Add blueprints
main = Blueprint('main', __name__, template_folder='templates')

# Create hello world 
@app.route('/')
def helloworld():
    return "Hello world"

# Create status route
@main.route('/status')
def status():
    return "{'status': 'running'}"

# Create a route to take in a query from the URL
@main.route('/vulnerable_query_no_render', methods=['GET'])
def vulnerable_query_no_render():
    # Extract the query string(s) from the URL
    query = request.args

    # Print the queries
    print ( query )

    # Print the bad query
    print ( query['query'] )

    # Return the query
    return query['query']


# Create a route to take in a query from the URL
@main.route('/vulnerable_query_render', methods=['GET'])
def vulnerable_query_render():
    # Extract the query string(s) from the URL
    query = request.args

    # Print the queries
    print ( query )

    # Print the bad query
    print ( query['query'] )

    # Return the queries
    return render_template('main/vulnerable_query_render.html', query=query['query'])


# Create a route to take in a query from the URL
@main.route('/vulnerable_query_print_cookie', methods=['GET'])
def vulnerable_query_print_cookie():
    
    response = None
    if request.args:
        # Extract the query string(s) from the URL
        query = request.args

        # Print the queries
        print ( query )

        # Print the bad query
        print ( query['query'] )

        # Create response
        response = make_response(render_template('main/vulnerable_query_render.html', query=query['query']))
        response.set_cookie('foo','bar')  
    else:
        response = make_response (render_template('main/vulnerable_query_render.html'))
        response.set_cookie('foo','bar')  
    
    return response

# Create a route to take in a query from the URL and set a cookie
@main.route('/vulnerable_query_post_cookie', methods=['GET'])
def vulnerable_query_push_cookie():
    # Extract the query string(s) from the URL
    query = request.args

    # Print the queries
    print ( query )

    # Print the bad query
    print ( query['query'] )

    # Set cookie
    response = make_response(render_template('main/vulnerable_query_render.html', query=query['query']))

    # Set HttpOnly in cookie to False 
    response.set_cookie('not_secure_foo','not_secure_bar')

    # Set HttpOnly in cookie to True 
    response.set_cookie('super_secure_foo','super_secure_bar', secure=True)    

    # Create response
    return response