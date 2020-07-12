# Personal Cookbook!

# **Table of Contents:**
* UX    
    * Project Goals   
    * User Stories
    * User Goals
* Design Choices
    * Fonts
    * Colours
    * Styling
    * Images
* Wireframes
    * Website layout
    * Flowchart
* Features  
    * Current Features
    * Future features
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
make it a pitch e.g my awsome website

The goal of this project is to create a site that implements the [CRUD](https://www.codecademy.com/articles/what-is-crud) functionality. 
The users who wish to avail of the site will be able to create their own **online Cookbook**, 
allowing them to **create**/upload recepies, **read** through their existing recipes/sample recipes
stored on the site, **update** their recipes and to **delete** recipes.

## User Stories
As a user I would want/expect my Personal Cookbook:   CHANGE TO AS A USER FOR EACH POINT
* For my **site** to be **secure**.
* To be able to **create** my own recipes.
* To **view** all my recipes easily.
* **Edit** recipes.
* **Update** my recepies.
* **Deleted** recipes I no longer want.
* Filter recipes into **categories** e.g breakfast, lunch and dinner to make it easier to view.
* For the website to be **responsive** on different devices.
* Be able to **delete** or **change** my **username/password/account** if I please.
* to view **sample recipes** layout.

## User Goals
*what u want the user to achieve
* Include different **categories** when searching for a recipe e.g breakfast.
* Website to **protect** the **users information**.
* Website to be easy to use and **visually** **appealing**.
* Website to easily allow the user to **create, edit, read and delete** recipes.


# **Design Choice**

 **Typography**:

 **Colours**: 

# **Structure**
The Website will consist of serveral pages.   
## **Home Page:**
This is the main page of the website that will consist of some information
about the function of website and **sample recipes** so the user can visualise what their recipes will look like.   
The **navbar** which is fixed to the top of the page, will consits of a **logo, login and register** options.   
The **footer** will contain some **social media** icons.

## **Register Page:**
The navbar will be the same as the home page along with the footer. 
This page will contain a simple **form** to allow the user to register to the website.
The **form** will contain a **username**, **password** and **confirm password** textareas to allow the user to get set up and a **submit** button.   

## **Login Page:**
Again, the navbar and footer will be the same and contain another **form** to allow the user to enter their **username** and **password** and a **login button**. 
The form will have **validation** so if the user enters the wrong username or password an **alert** will pop up to advise the user that the information is inncorrect and to try again.

## **User account home page:**
When the user has logged into the website, the **navbar** will be amended to include a **logo, home, my recipies, my account dropdown**. 
The **dropdown** option will contain **edit account, delete account, logout**.    
The **edit account** will allow the user to amend their password.  
The body of the page will contain the user name e.g *Sophie's Cookbook* and a small paragraph informing the user how the Cookbook works.   
There is a **add recipe button** under the paragraph to allow the user to get started.

## **Create/Edit Recipe:**
The different **features** when the user creates a new recipie include the following:   
* Add Category **breakfast, lunch, dinner, desert**
* **Preperation** time.
* **Cook** time.
* Recipe **name**
* Recipe **description**
* **Ingredients**
* **Steps**
* **Image**
* **Add/Cancel buttons**

All these features apart from description will be **mandatory**.

## **Recipes:**
*My recipes* page consists of a **search** option and **filter** by meal type e.g dinner. 
The current recipes created by the user will be displayed with the image of the recipe, name of the recipe and the meal type and cooking time.    
The user will be able to click on their preferred recipe to view more information.

## **Read Recipe:**
This page consists of all the **imformation** selected **from** when the user **created their recipe**, the name of the recipe, image, cook/prep time, ingredients and steps.   
There are two **buttons, edit and delete**.  
The **edit** recipe **page** will be the same as the create recipe page and if the user wished to **delete** the recipe an alert message will appear to confirm if the user wants todelete this recipe.

# **Wireframes**
My Wireframes:  
[Desktop](https://github.com/SophieH93/MS3/tree/master/wireframes/desktop
)   
[Tablet](https://github.com/SophieH93/MS3/tree/master/wireframes/tablet)  
[Mobile](https://github.com/SophieH93/MS3/tree/master/wireframes/mobile)   
[Flowchart](https://github.com/SophieH93/MS3/tree/master/wireframes/flowchart)

I created my wireframes and Flowchart using [MockFlow](https://www.mockflow.com/) for various devices.
The **edit recipe page**  will be the same as the **add recipe page** hence I did not create an official wireframe for this page.   
The **delete recipie** will display a pop up to confirm with the user if they actually want to delete the recipe.

# Features



## Future Features:

# Information Architecture

## Data Storage Types
* ObjectID
 * String
 * Boolean
 * Array
 


# Technologies used

## Languages
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [JavaScript](https://www.javascript.com/)
* [Python](https://www.python.org/)
* [JSON]

## Frameworks
* [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/)* 
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/



## Tools 
* [GitHub](https://github.com/)
* [GitPod](https://www.gitpod.io/)
* [Git](https://git-scm.com/about)
* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
* [W3C Markup Validation](https://validator.w3.org/)
* [WSC CSS Validaion](https://jigsaw.w3.org/css-validator/)
* [MockFlow](https://www.mockflow.com/)
* [Dirty Markup Formatter](https://www.10bestdesign.com/dirtymarkup/)

# Testing
Due to the scope of the website, there will need to be a lot of testing required during this project.


## **Navbar/footer:**

* **Plan-** I will need to ensure all the links work properly so when the user clicks on one they are brought to the correct page.

* **Implementation-** Chcek that the nav links go to the correct page and the social media links open in a new tab to the correct website.

* **Testing-** Use **session variables** and jinja **if/else** statements for the navigation so when the user logs in they are displayed with a different navbar.    
  Use **target="_blank"** to open the **social** media links in a new tab.

* **Result-**Social media links open in a new tab to the correct url. When the user logs into the site the **navbar** changes to display '**Recipes, Add Recipes, Logout."**

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

* **Implementation-**To check the information from the form matches the information that is stored in the users collections in the database and if it does not match,
a flash message is triggered to let the user know that their password/username is incorrect.

* **Testing-** I inputted the **wrong informaton** to make sure the **flash error** displays and then created the **correct** login **information** and a **flash messages** displayes to tell the user they have logged in successfully.
* **Result-** The test passed and I was able to sign in the account.

## **Sign Out:**

* **Plan-**There needs to be a signout feature for the user if they wish to logout of their account.
* **Implementation-** I will need to create a method for this function.
* **Testing-**
* **Result-**

## **Create Recipe:**

* **Plan-** I will need to ensure **validation** is inputted on the forms, to make sure the recipe cannot be created unless all required fieds are complete.
* **Implementation-** Create a recipe without completing a required field e.g ingredients to see if a **flash message** will display to advise the user to fill out required field.
* **Testing-**
* **Result-**

## **Edit Page:**

* **Plan-** I will need to ensure that when the **edit button** is clicked the user will be able to edit their recipe. I will also need to ensure that the informaiton is properly updated and stored in the database.
* **Implementation-** This testing will be similar to the create recipe as in to make sure all validation is inputted.
* **Testing-**
* **Result-**

## **My Recipes:**

* **Plan-** I will need to ensure the user is able to view all recipes created when they click on the **My Recipes** nav link and to ensure the edit and delete buttons work too.
* **Implementation-** I will need to **test** that the **search bar** works, the **fitler** by **category** works, that the **full recipe** displays when the user clicks on a recipe and that the **edit** and **delete buttons** work.
* **Testing-**
* **Result-**

## **Delete Recipes:**

* **Plan-** I will need to create a [sweetalert](https://sweetalert2.github.io/) that asks the user to confirmm if they actually want to delete the recipe.   
If the answer is **Yes** then I will need to ensure the recipe is delete from the database and a confirmation is displayed to the user.   
if the answer is **No** I need to ensure the user is brought back to the recipe.
* **Implementation-** Test theses fectures work and check the database to see if the recipe is removed.
* **Testing-**
* **Result-**


# Bugs

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
    echo web: python run.py > Procfile
    ```
3. Push these to your repository.

4. Create a new app on Heroku, assin a unique name and set your region (I used Europe)

5. Fomr the dashboard, click **Deploy -> Deployment method -> GitHub**
    help them sign into git

6. BE MORE EXPLICIT Link Heroku to your IDE by inputting the following into your command:
    ```
    heroku login
    git push heroku master
    ```

7. In the heroku dashboard for the application, click on **Settings -> Reveal Config Vars** and set the following config vars:   
    * IP: 0.0.0.0
    * PORT: 5000

8. Click **Open App** to view the app.
    
# Closing Notes

# Credits
[Youtube](https://www.youtube.com/watch?v=vVx1737auSE) for creating **registration/login**
https://www.youtube.com/watch?v=803Ei2Sq-Zs&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=7 

# Disclaimer
**This websit is for educational purposes only.**