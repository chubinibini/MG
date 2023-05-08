from flask import render_template, request, redirect, url_for
from controller import bp_main as main
from controller import db_controller

db = db_controller
app = db.init_database( )
mysql = db.init(app)

@main.route('/', methods=['get','post'])
def home():
    popular_doges =  db.take_popular_dog( app, mysql, 3 )
    print(popular_doges)
    return render_template( 'main.html' , dogs=popular_doges)
    
@main.route('/main', methods=['get','post'])
def main_page():
    popular_doges =  db.take_popular_dog( app, 3 )


    return popular_doges

@main.route('/main/populor_dog', methods=['get','post'])
def main_populor_dog():

    return redirect(url_for('main'))

