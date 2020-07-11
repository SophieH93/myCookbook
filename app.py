import os
from flask import Flask, render_template, url_for, session, redirect, request, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "create_recipes"
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
mongo = PyMongo(app)




@app.route("/")
@app.route("/index")
def index():
    return render_template('pages/index.html', page_title="Home")


@app.route("/login", methods=["GET", "POST"])
def login():   
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name' : request.form['username']})
        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
                flash('You have been successfully logged in!')
                return redirect(url_for('index'))        
        return 'Invalide username/password combination'
    return render_template('pages/login.html')

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})
        flash('You have been successfully Registered!')
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            
            return redirect(url_for('index'))

        return 'That username already exists!'

    return render_template('pages/register.html')

# My Recipes
@app.route('/recipes')
def recipes():
    return render_template('pages/recipes.html')

# Add Recipes
@app.route('/add_recipe')
def add_recipe():
    return render_template('pages/add_recipe.html')

# Logout
@app.route('/logout')
def logout():
    return render_template('pages/logout.html')



if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True) 