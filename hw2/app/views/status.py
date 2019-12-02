from flask import request, Blueprint, render_template, make_response
from datetime import datetime

# Add blueprints
status = Blueprint('status', __name__, url_prefix="/status", template_folder='templates')

# Create status route
@status.route('/')
def check_status():
    return '{"status": "running"}'
    