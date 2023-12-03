from flask import Blueprint, render_template

debugger_bp = Blueprint('debugger', __name__, template_folder='templates')

@debugger_bp.route('/debug')
def debug_route():
    # Your debug route logic goes here
    return render_template('debugger.html')
