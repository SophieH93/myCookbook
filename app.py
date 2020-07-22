import os
from flask import Flask, render_template, url_for, \
    session, redirect, request, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from forms import addRecipeForm
import bcrypt

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

"""MAKE THESE VARIABLES"""
app.config["MONGO_DBNAME"] = "myCookbook"
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
mongo = PyMongo(app)

@app.route("/")
@app.route("/home")
def home():
    """
    When page loads, home page is displayed.
    """
    return render_template('pages/home.html')


@app.route('/recipes')
def recipes():
    """
    Displays users recipes
    """
    return render_template('pages/recipes.html',
                            recipes=mongo.db.recipes.find())


@app.route('/single_recipe_info/<recipe_id>')
def single_recipe_info(recipe_id):
    '''
    Displays info about a selected recipe.
    '''
    selected_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("pages/single_recipe_info.html",
                            selected_recipe=selected_recipe)

   
@app.route('/add/recipe', methods=["GET", "POST"]) 
def addRecipe(): 
    """
    Add Recipe to the database
   """
    if request.method == "POST":
        recipes = mongo.db.recipes 

        recipes.insert_one({
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
    else:
        form = addRecipeForm()
        return render_template('pages/add-recipe.html', form=form)


@app.route("/edit/recipe/<recipe_id>", methods=["GET", "POST"])
def editRecipe(recipe_id):
    """
    Update the Recipe in the database and returns users to recipe page
   """
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
    else:
        form = addRecipeForm()
        return render_template('pages/edit-recipe.html',
                                selected_recipe=selected_recipe, form=form)


@app.route('/delete-recipe/<recipe_id>')
def deleteRecipe(recipe_id):
    '''
    Delete Recipe from the Database
    '''
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)}) 
    return redirect(url_for('recipes'))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        users = mongo.db.users
        login_user = users.find_one({'name' : request.form['username']})
        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'),
                            login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for('home'))
        flash('Invalide username/password !')
    return render_template('pages/login.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), 
                                    bcrypt.gensalt())
            users.insert({'name' : request.form['username'],
                        'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('home'))
        flash('That username already exists!')
    return render_template('pages/register.html')


@app.route('/logout')
def logout():

    session.pop("username",  None)
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)