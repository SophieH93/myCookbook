# Personal Cookbook!

# **Table of Contents:**
* UX    
    * Project Goals   
    * User Stories
    * User Goals
* Strategy
* Scope
* Structure
* Surface       
    * Design Choices
        * Fonts
        * Colours
        * Styling
        * Images
    * Features  
        * Current Features
        * Future features
* Skeleton
    * Wireframes
        * Website layout
        * Flowchart
* Information Architecture
* Technologies Used
    * Languages
    * Frameworks
    * Tools
* Testing
* Bugs
* Deployment
    * Deploying to Heroku
    * Locally run the project
* Closing Notes
* Credits
* Disclaimer

# **UX**
## Project Goals:



## User Stories

* As a user, I would expect the website **site** to be **secure**.
* As a user, I would like be able to **create** my own recipes.
* As a user, I would like be able to  **view** all my recipes easily.
* As a user, I would like be able to **Edit** recipes.
* As a user, I would like be able to **Deleted** recipes I no longer want.
* As a user, I would like be able to be able to filter recipes into **categories** e.g breakfast, lunch and dinner to make it easier to view.
* As a user, I would expect the website to be **responsive** on different devices.
* As a user, I would expect to able to **delete** or **change** my **username/password/account** if I please.

## User Goals

* Include different **categories** when searching for a recipe e.g breakfast.
* Website to **protect** the **users information**.
* Website to be easy to use and **visually** **appealing**.
* Website to easily allow the user to **create, edit, read and delete** recipes.

# **Strategy:**
The value of this website, is that it allows users to store all their recipes and view them in one place online.
User's will no longer have to look up recipes online which can be time-consuming.

The website implements the implements the [CRUD](https://www.codecademy.com/articles/what-is-crud) functionality. 
The users who wish to avail of the site will be able to create their own **Personal Cookbook**, 
allowing them to **create**/upload recepies, **read** through their existing recipes/sample recipes
stored on the site, **update** their recipes and to **delete** recipes they no longer wish.

**Primary Audience** - People who want to store their favourite recipes in one place online.

# **Scope:**
The website is easy to use and stores the user's information in [MongoDB](https://www.mongodb.com/). Due to time rectricions
I was unable to create a search & category button which would have allowed the customer to look up a recipe or filter their recipes by
different categories e.g breakfast, lunch etc.

# **Structure**

* **Navbar:**   
If the user is **not logged in** the navbar contains a **Register & Login** links.   
If the user is **logged in** the navbar contains a **Recipes, Add Recipes, Logout** links.
**Python** will determine is the user is logged in to the site or not by checking **if session.username** and passes this data to **Jinja** to 
display the correct navbar for the user.   

* **Register Page:**   
Contains a form where the user enters a **Username, Password and Confirm Password** field. The Passwords must match and are **hashed** for security purposes.    

* **Login Page:**   
Contains a form for the user to enter their **Psername & Password** allowing them to log into their account, providing their details are corrent.   
If the details match the ones in the database, the user is redirected to the home pages and informed with a **flash message** that they have successfully logged in.

* **My Recipes:**  
Allows the user to view all their recipes in a card formatat. The card will displays the **recipe image, meal type, cooking time** and two **buttons, edit & delete**.

* **Single Recipe Page:**   
Renders when the user clicks on the recipe card.  This page will display informaiton about the selected recipe.

* **Add Recipes Page:**  
The user is able to add their recipe through a form which is validated. When the user has added their recipe to the database they are redirected to the **Recipe page**.

* **Edit Recipes Page:**  
The user is able to update information about a recipe. The form layout is the same as the *add recipe page**.   
The page also contains two **buttons**, **edit** and **cancel**.

* **Delete Recipes:**
Once the user clicks the delete button, which is displayed on the recipes page in the card, the recipe will be **deleted from the database** and the user will 
be **redirected** to the *recipes page*

* **Logout:**   
Clicking the logout button will end the user's session and redirect them back to the home page.

* **Footer:**   
Contains **links** to the developers relevent social media links **Github & Linkedin** which opens in a new tab.

# **Surface:**
## **Design Choice**

 **Typography**: [Open Sans](https://fonts.google.com/specimen/Open+Sans?preview.text=My+Cookbook&preview.text_type=custom&sidebar.open&selection.family=Lora|Open+Sans&query=Open+Sans#standard-styles) for the **body** and [Lora](https://fonts.google.com/specimen/Lora?preview.text=My+Cookbook&preview.text_type=custom&sidebar.open&selection.family=Lora|Open+Sans#standard-styles) for **H1** headings. These fonts where choosen from Google Fonts. I initally chose Lora first for the heading and [Google Fonts](https://fonts.google.com/?preview.text=My+Cookbook&preview.text_type=custom&sidebar.open&selection.family=Lora|Open+Sans#standard-styles) recommended Open Sans as it's complimentary font.

 **Colours**: I decided to use the [Bootswatch: Journal](https://bootswatch.com/journal/) template for my site which provided me with a colour template.    
 Click [here](https://github.com/SophieH93/myCookbook/tree/master/wireframes/Colour-Palette) to view my **Color Palette**.
 Main Color Palette:
 * Fire Opal: #EB6864 
 * Silver Chalice: #aaaaaa
 * Cultured: #F8F9FA
 * Heat Wave: #FD7E14
 * Green Pantone: #22B24C 

**Shadows**: **Radial-gradient(rgba(249, 238, 238, 0.91), rgba(152, 142, 142, 0.04))** - Used for the login/register/add/edit background image.

**Icons**: I used [Font Awesome](https://fontawesome.com/start) icons to enhance user experience. The icons are displayed on the all the forms beside the labels..

**Images:** The images chosen for the website were taking from [Unsplash](https://unsplash.com/collections/2136555/flatlay) under a 'cooking' search.


## Features:
* [Bootswatch](https://bootswatch.com/journal/) Journal **Template**.
* [Start Bootstrwap](https://startbootstrap.com/snippets/) for **login** and **register** pages.
* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) - Database
* [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) - Creating the Add/edit forms.

## Future Features:
* **Pagination-** So only a few recipes will show on on the page and the remainder on the next page etc. At the moment all Recipes are displayed on the same page.
* **Change Password/Username-** To allow the user to change their details if they wish.
* **Recover Password-** If the user have forgotton their password will be able to re-set it.
* **Filter Recipes-** To make it easier to find a certain recipe.
* **Search Option-** Search a recipe by name.

# Skeleton:
## **Wireframes**
My Wireframes:  
[Desktop](https://github.com/SophieH93/MS3/tree/master/wireframes/desktop
)   
[Tablet](https://github.com/SophieH93/MS3/tree/master/wireframes/tablet)  
[Mobile](https://github.com/SophieH93/MS3/tree/master/wireframes/mobile)   
[Flowchart](https://github.com/SophieH93/MS3/tree/master/wireframes/flowchart)
[Color Palette](https://github.com/SophieH93/myCookbook/tree/master/wireframes/Colour-Palette)

I created my wireframes and Flowchart using [MockFlow](https://www.mockflow.com/) for various devices.
The **edit recipe page**  will be the same as the **add recipe page** hence I did not create an official wireframe for this page.   
The **delete recipie** will display a pop up to confirm with the user if they actually want to delete the recipe.


# Information Architecture
Using NoSql features in MongoDB I was able to map out the following colelctions.

## Data Storage Types
* ObjectID
* String
* Boolean
* Array
* Object
* Binary

**Users Collection:**
````
_id: <ObjectId>
name:<string>
password: Binary(string)
````


**Recipe Collection:**
````
_id: <ObjectId>
recipe_name: <string>
description: <string>
prep_time: <string>
cooking_time: <string>
ingredients: <string>
steps: <string>
images: <string>
````



# Technologies used

## Languages
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [JavaScript](https://www.javascript.com/)
* [Python](https://www.python.org/)
* [JSON](https://www.json.org/json-en.html)

## Frameworks
* [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
* [Bootswatch](https://bootswatch.com/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
* [JQuery](https://jquery.com/)
* [Google Fonts](https://fonts.google.com/)
* [Font Awesome](https://fontawesome.com/start)


## Tools 
* [GitHub](https://github.com/)
* [GitPod](https://www.gitpod.io/)
* [Git](https://git-scm.com/about)
* [PyMongo](https://pymongo.readthedocs.io/en/stable/)
* [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/)
* [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/install.html)
* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
* [W3C Markup Validation](https://validator.w3.org/)
* [WSC CSS Validaion](https://jigsaw.w3.org/css-validator/)
* [MockFlow](https://www.mockflow.com/)
* [Dirty Markup Formatter](https://www.10bestdesign.com/dirtymarkup/)
* [PEP8 Validaion](http://pep8online.com/checkresult)

# Testing
Due to the scope of the website, there will need to be a lot of testing required during this project.


## **Navbar/footer:**

* **Plan-** I will need to ensure all the links work properly so when the user clicks on one they are brought to the correct page.

* **Implementation-** Chcek that the nav links go to the correct page and the social media links open in a new tab to the correct website.

* **Testing-** Use **session variables** and jinja **if/else** statements for the navigation so when the user logs in they are displayed with a different navbar.    
  Use **target="_blank"** to open the **social** media links in a new tab.

* **Result-** Social media links open in a new tab to the correct url. When the user logs into the site the **navbar** changes to display '**Recipes, Add Recipes, Logout."**

## **Create an account:**
* **Plan**-I will need to implement a way that a user will be able to create an account and that their **information** is **stored** in a **database**.        
This invloves checking that the users **passwords match** when they create a password and confirmed the password.   
I will need to **research** the best way to create this feature that's also easy for the user to create an account and properly hash the password when 
it's stored into the database.

* **Implementation-** **Import session and bcrypt** was required to handle the request. The code checks that the passwords entered match to avoid any typos and then checks if the username entered already exists in the database.

* **Testing** - I created a few accounts to check what values are passed and stored in the database and that the passwords match and used [bcrypt](https://pypi.org/project/bcrypt/) for password hashing.   
To achieve this I followed [pretty printed Youtube viedo](https://www.youtube.com/watch?v=vVx1737auSE) to create the Registration form.

* **Result-** This tests passed and the user's username and passwords are stored in the MongoBD database. A **flash message** will appear if the username already exists
and if the user's password do no match a alert appears to advise the user the password do not match.

## **Login to Account:**

* **Plan-** I will need to create a form for the user to login to their account. I will need to make sure the form is validated correctly.

* **Implementation-** To check the information from the form matches the information that is stored in the users collections in the database and if it does not match,
a flash message is triggered to let the user know that their password/username is incorrect.

* **Testing-** I inputted the **wrong informaton** to make sure the **flash error** displays and then created the **correct** login **information** and a **flash messages** displayes to tell the user they have logged in successfully.

* **Result-** The test passed and I was able to sign in the account.

## **Sign Out:**

* **Plan-** There needs to be a signout feature for the user if they wish to logout of their account.

* **Implementation-** Create a route and method using [session.pop](https://www.tutorialspoint.com/flask/flask_sessions.htm#:~:text=To%20release%20a%20session%20variable%20use%20pop()%20method.&text=The%20following%20code%20is%20a,'username'%20is%20not%20set.&text=As%20user%20browses%20to%20'%2Flogin,opens%20up%20a%20login%20form.).

* **Testing-** Click on the logout button in the navigation and the user should be signed out and returned the to home page.

* **Result-** The test **passed** as the session was cleared out and the user was no longer signed in.

## **Create Recipe:**

* **Plan-** I will need to ensure **validation** is inputted on the forms, to make sure the recipe cannot be created unless all required fieds are complete. I will also need to ensure the recipe is added to the Mongo Database.

* **Implementation-** I will use [flask-wtf forms](https://flask.palletsprojects.com/en/1.1.x/patterns/wtforms/) to create the Add recipe form which will also include validation and then create a new route to insert the recipe to the database.

* **Testing-** If a field is not complete the user will not be able to submit their recipe and the field will be highlighted. The user is redirected to the 'Recipes' page when the form is complete. The recipe is inerted into the database successfully.

* **Result-** Working properly. Recipe stored into the MongoDB under the 'recipes' collection.

## **Single Recipe Page:**

* **Plan-** I will need to ensure that when the user selects one of their recipes that the correct recipe info is pulled fromt the database.

* **Implementation-** I will need to create a new route that fetches the recipe from the MongoDB.

* **Testing-** I created a few recipes and using **select_recipe** was able to pull the correct info from the database when clicked on a specific recipe.

* **Result-** The selected recipe is displaying the proper info.

## **My Recipes:**

* **Plan-** I will need to ensure the user is able to view all recipes created when they click on the **My Recipes** nav link and to ensure the edit and delete buttons work too.

* **Implementation-** I will need to **test** that the **search bar** works, the **fitler** by **category** works, that the **full recipe** displays when the user clicks on a recipe and that the **edit** and **delete buttons** work and that the recipe info is pulled from the database and displayed to the website.

* **Testing-** I creaded a **for/loop** in the Recipes html that fetched the recipe card and in the Recipes route added the mongo.db.find to fetch the user's recipes from the database and display then to the site.

* **Result-** The user's recipes are displaying on the page correctly.

## **Edit Page:**

* **Plan-** I will need to ensure that when the **edit button** is clicked the user will be able to edit their recipe. I will also need to ensure that the informaiton is properly updated and stored in the database.

* **Implementation-** This testing will be similar to the create recipe as in to make sure all validation is inputted.
* **Testing-**
* **Result-**


## **Delete Recipes:**

* **Plan-** I will need to create a delete button so the user is able to delete their recipe.

* **Implementation-** Test theses features work and check the database to see if the recipe is removed.

* **Testing-** I created the method to delete the recipe from the website and from the database.

* **Result-** The selected Recipe is deleted when the **delete button** is clicked on and also removed from the MongoDB.


# Bugs
* **Bug:** I wanted to create **two cards** side-by side on the *Single Recipe Page* with the second card displaying the Ingredients and Steps in list format.  
 **Fix:** Unfortunately due to time restrictions I was unable to solve this bug so I amended the page to display just one card with the recipe details and styled
the page with *max-width & auto margin* to center the recipe on the page.

* **Bug:** I wanted to **display** my **recipe's** **side by side** using the Bootsrap grid system. I was having trouble achieving as my cards were only displaying ubove each other and could not understand why.   
**Fix:** Took about a week, but discovered if I removed the **container & row divs** from the **recipe cards html** the recipes would display properly.



# Deployment 
## **Run Locally:**
* **Open** your prefered **IDE** (I used Gitpod)
* **Run MongoDB** Atlas on oyur machine (your database)
    * Click [here](https://docs.atlas.mongodb.com/) to read how to set up your Mongo Atlas.
* In your terminal **install** [Pip](https://pip.pypa.io/en/stable/installing/), [Python3](https://www.python.org/downloads/) and [Git](https://git-scm.com/)   

**Directions**:   
1. Clone this repository into your IDE of your choice by pasting this command
into the terminal 
```
 git clone https://github.com/SophieH93/myCookbook 
```
**Alternatively**, you can **save a copy** of this repository by clicking the green button **"Clone or download"** , then **"Download Zip" button**, and after extract the Zip file to your folder.

2. In your terminal **change direcrory** (cd) to the correct file location or open a terminal session in the unzip folder.

3. Enter the following commannd
```
python -m .venv venv
```

4. **Initilaize** the environment by using the following command.
```
.venv\bin\activate 
```

5. **Install** all requiremetns by putting this command into your terminal:
```
pip3 install -r requirements.txt
```

6. Set up **environment variables**:
    * Create **.env file** in the root directory.
    * On the top of the file add **import os** to set the environment variables in the operating system.
    * Set the connection to your MongoDB database**(MONGO_URI)** and a **SECRET_KEY** with the input:
    ```
    os.environ["SECRET_KEY"] = "YourSecretKey"
    os.environ["MONGO_URI"] = "YourMongoURI
    ```
7. **Run application** using flask run or in terminal type 
    ```
    python3 app.py
    ```

## **Deploying to Heroku:**

1. **Create** a **requirements.txt** file by adding the following to your terminal.
    ```
    pip3 freeze > requirements.txt
    ```
2. Create a **Procfile**, in order to tell Heroku how to run the project. Procfile must start with a capital 'P':
    ```
    echo web: python app.py > Procfile
    ```
3. Push these to your Git repository.

4. Create a new app on Heroku, assign a unique name and set your region (I used Europe)

5. To start the web process, put the following command into the terminal to **scale dynos**:
    ```
    heroku ps:scale web=1
    ```
6. From the Heroku dashboard, click **Deploy -> Deployment method -> GitHub**

7. Connect to your Github repository by adding your **repo name** and clicking the **search button**.

8. In the heroku dashboard for the application, click on **Settings -> Reveal Config Vars** and set the following config vars:   
    * IP: 0.0.0.0
    * PORT: 5000
    * MONGO_URI: *link to your MongoDB database*
    * SECRET_KEY: *your secret key* 
    * DEBUG: FALSE   
**Note-** your MONGO_URI and SECRET_KEY must match the ones you entered in .env.py file

9. **Deploy -> Manual Deploy** select the master branch and click **deploy branch** button.

10. Click **Open App** to view the app.
    
# Closing Notes

# Credits
[Pretty Printed Youtube](https://www.youtube.com/watch?v=vVx1737auSE) for creating **registration/login**.   
[Corey Schafer Youtbe](https://www.youtube.com/watch?v=u0oDDZrDz9U&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=8) for creating the **FlaskWtForm** for **creating** a recipe and how to add **insert** to the database.   
[Unsplash](https://unsplash.com/collections/2136555/flatlay) Used for Jumbotron and Login page background images

# Disclaimer
**This websit is for educational purposes only.**