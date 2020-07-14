import os
from flask import Flask, render_template, url_for, session, redirect, request, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from templates.forms import addRecipeForm

import bcrypt

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "myCookbook"
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
   return render_template('pages/index.html')



# Edit Recipe
@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    form = addRecipeForm()
    selected_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('pages/edit_recipe.html',  selected_recipe=selected_recipe, form=form)


# My Recipes
@app.route('/recipes')
def recipes():    

    return render_template('pages/recipes.html', recipes=mongo.db.recipes.find())


 # Single Recipe displayed
@app.route('/single_recipe_info/<recipe_id>')
def single_recipe_info(recipe_id):
    '''
    Displays info about a selected recipe.
    '''
    selected_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("pages/single_recipe_info.html", selected_recipe=selected_recipe)

# Add Recipes
@app.route('/add_recipe')   
def add_recipe():
    '''
    The function calls the addRecipeForm class from forms.py
    to display the form for adding a recipe.
    '''
    form = addRecipeForm()
    return render_template('pages/add_recipe.html', form=form)


# Insert recipe to database
@app.route("/insert_recipe", methods=["GET", "POST"])
def insert_recipe():       
    """
    Add the user's inserted data in the database and redirect
    the user to recipes.html page.
    """
    recipes = mongo.db.recipes 

    recipes.insert_one( {
            "recipe_name": request.form.get("recipe_name"),
            "description": request.form.get("recipe_description"),            
            "prep_time": request.form.get("prep_time"),
            "cooking_time": request.form.get("cooking_time"),
            "ingredients": request.form.get('recipe_ingredients'),
            "steps": request.form.get('steps'),
            "image": request.form.get("image")
        })
    
    return redirect(url_for('recipes'))
       
       
@app.route("/login", methods=["GET", "POST"])
def login():       
    if request.method == "POST":
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

# Logout
@app.route('/logout')
def logout():
    session.pop("username",  None)
    return redirect(url_for("index"))



if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True) 