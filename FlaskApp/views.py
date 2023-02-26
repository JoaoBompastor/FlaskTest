from flask import Blueprint, render_template

view = Blueprint(__name__, 'view')

@view.route('/home/')
def Home():
    return render_template('index.html', name= 'satiro')

@view.route('/profile/')
def Profile():
    return render_template('profile.html')

@view.route('/gi/')
def gi():
    return render_template('gi.html')