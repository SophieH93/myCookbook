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


'''
Home page
'''
@app.route("/")
@app.route("/index")    
def index():
    '''
    When page loads, index page is displayed.
    '''
    return render_template('pages/index.html')

'''
Login page
'''
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

'''
Register page
'''
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

'''
Recipe page
'''
@app.route('/recipes')
def recipes():    

    return render_template('pages/recipes.html', recipes=mongo.db.recipes.find())

'''
Add Recipe 
'''
@app.route('/add_recipe')   
def add_recipe():
    '''
    The function calls the addRecipeForm class from forms.py
    to display the form for adding a recipe.
    '''
    form = addRecipeForm()
    return render_template('pages/add_recipe.html', form=form)


'''
Insert Recipe to Database
'''
@app.route("/insert_recipe", methods=["GET", "POST"])
def insert_recipe():       
    """
    Add the user's data to the MongoDB and redirect
    the user to Recipe page.
    """
    recipes = mongo.db.recipes 

    recipes.insert_one( {
        "recipe_name": request.form.get("recipe_name"),
        "description": request.form.get("recipe_description"),
        "prep_time": request.form.get("prep_time"),
        "cooking_time": request.form.get("cooking_time"),
        "category": request.form.get("category"),
        "ingredients": request.form.get('ingredients'),
        "steps": request.form.get('steps'),
        "image": request.form.get("image")
    })
    
    return redirect(url_for('recipes'))

'''
Edit Recipe
'''
@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):

    form = addRecipeForm()
    selected_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('pages/edit_recipe.html',  selected_recipe=selected_recipe,  form=form)

'''
Update the Recipe in the database
'''
@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes

    selected_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    if request.method == "POST":
        recipes.update({"_id": ObjectId(recipe_id)}, {
            "recipe_name": request.form.get("recipe_name"),
            "description": request.form.get("recipe_description"),
            "prep_time": request.form.get("prep_time"),
            "cooking_time": request.form.get("cooking_time"),
            "category": request.form.get("category"),
            "ingredients": request.form.get('ingredients'),
            "steps": request.form.get('steps'),
            "image": request.form.get("image")
        })

    return redirect(url_for('single_recipe_info', recipe_id=recipe_id))

'''
Single Recipe 
'''
@app.route('/single_recipe_info/<recipe_id>')
def single_recipe_info(recipe_id):
    '''
    Displays info about a selected recipe.
    '''
    selected_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("pages/single_recipe_info.html", selected_recipe=selected_recipe)


'''
Delete Recipe 
'''
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    '''
    Delete Recipe from the Database
    '''
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)}) 
    return redirect(url_for('recipes'))


'''
Logout
'''
# Logout
@app.route('/logout')
def logout():
    session.pop("username",  None)
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True) 