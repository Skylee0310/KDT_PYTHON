from flask import Blueprint, render_template

bp = Blueprint('main', __name__ , url_prefix='/')

@bp.route('/')
def root() :
    return render_template('main.html')

@bp.route('/<result>')
def result() :
    return render_template('result.html')