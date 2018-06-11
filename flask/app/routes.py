from app import app, db

from flask import render_template, redirect, request
from flask import jsonify
from app.forms import AddItemsForm, SearchItemsForm
from app.models import Items, ItemsSchema
from redis import Redis
import redis
import hashlib
import json


app.secret_key = 'development key'
R_SERVER = redis.StrictRedis(app.config['REDIS_HOST'], 6379, charset="utf-8", decode_responses=True)
items_schema = ItemsSchema(many=True)

@app.route('/')
@app.route('/index')
@app.route('/search', methods=['GET', 'POST'])
def search():
  
    form = SearchItemsForm()
    found_in_cache = "False"
    
    #Display all items for GET request and if it is a blank search in POST
    key = "All"

    #Get the Key
    if request.method == 'POST':
        search_category = request.form['Category']
        if ( (search_category) and  (search_category.isspace() == False) ):
            key = search_category

    #Check if result is already in cache
    if (R_SERVER.get(key)):
        found_in_cache = "True"
        result_json = R_SERVER.get(key)
        result = json.loads(result_json)
    else:

        found_in_cache = "False"
        if key == "All":
             matched_items = Items.query.all()
        else:
            matched_items = Items.query.filter_by(Category=search_category).all()
        
        result = (items_schema.dump(matched_items)).data
        result_json = json.dumps(result)
        R_SERVER.set(key,result_json)
        R_SERVER.expire(key, 30)


    return render_template('search.html', form = form, key = key, found_in_cache = found_in_cache, result = result)


@app.route('/items_add', methods=['GET', 'POST'])
def items_add():
  
    form = AddItemsForm()
    if request.method == 'POST':
        newitem = Items(request.form['Category'], request.form['Vendor'], request.form['Model'], request.form['Price'])
        db.session.add(newitem)
        db.session.commit()
        return render_template('items_add.html', form=form, user_message="Add")
    else:
        return render_template('items_add.html', form=form, user_message="")

