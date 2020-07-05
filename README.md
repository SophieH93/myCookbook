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

The goal of this project is to create a site that implements the [CRUD](https://www.codecademy.com/articles/what-is-crud) functionality. 
The users who wish to avail of the site will be able to create their own **online Cookbook**, 
allowing them to **create**/upload recepies, **read** through their existing resipies/sample recipies
stored on the site, **update** their recipies and to **delete** recipes.

## User Stories
As a user I would want/expect my Personal Cookbook:   
* To be able to **create** my own recipes to an online site.
* To **view** all my recipes easily.
* **Edit** recipes.
* **Update** my recepies.
* **Deleted** recipes I no longer want.
* Filter recipes into **categories** e.g breakfast, lunch and dinner to make it easier to view.
* For the website to be **responsive** on different devices.
* Be able to **delete** or **change** my **username/password/account** if I please.

## User Goals
* To be **responsive** on mobile, table and destop devices.
* Include different **categories** when searching for a recipe e.g breakfast.
* Website to **protect** the **users information**.
* Website to be easy to use and **visually** **appealing**.
* Website to easily allow the user to create, edit, read and delete recipes.


# **Design Choice**
### Fonts:

### Colours:

### Icons:

### Styling:

### Images: 

# **Structure**
The Website will consist of serveral pages.   
## **Home Page:**
This is the main page of the website that will consist of some information
about function of website and **sample recipes** so the user can visualise what the recipie will look like.   
The **navbar** which is fixed to the top of the page, will consits of a **logo, login and register** options.   
The **footer** will contain some **social media** icons.

## **Register Page:**
The navbar will be the same as the home page along with the footer. 
This page will contain a simple form to allow the user to register to the website.
The **form** will contain a **username**, **password** and **confirm password** textareas to allow the user to get set up and a **submit** button.   

## **Login Page:**
Again, the navbar and footer will be the same and contain another form to allow the user to enter their **username** and **password** and a **login button**. 
The form will have validation so if the user enters the wrong username or password an alert will pop up to advise the user that the information isinncorrect and to try again.

## **User account home page:**
When the user has logged into the website, the **navbar** will be amended to include a **logo, home, my recipies, my account dropdown**. 
The **dropdown** option will contain **edit account, delete account, logout**.   
The body of the page will contain the user name e.g *Sophie's Cookbook* and a small paragraph informing the user how the Cookbook works.   
There is a **add recipe button** under the paragraph to allow the user to get started.

## **Create Recipe**
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

## **All Recipes**
*My recipes* page consists of a **search** option and **filter** by meal type e.g dinner. 
The current recipes created by the user will be displayed with the image of the recipe, name of the recipe and the meal type and cooking time.    
The user will be able to click on their preferred recipe to view more information.

## **Read Recipe**
This page consists of all the **imformation** selected **from** when the user **created a recipe**, the name of the recipe, image, cook/prep time, ingredients and steps.   
There are two **buttons, edit and delete**.  
The **edit** recipe **page** will be the same as the create recipe page and if the user wished to **delete** the recipe an alert message will appear to confirm if the user wants todelete this recipe.

# **Wireframes**
My Wireframes:  
[Desktop](https://github.com/SophieH93/MS3/tree/master/wireframes/desktop
)   
[Tablet](https://github.com/SophieH93/MS3/tree/master/wireframes/tablet)  
[Mobile](https://github.com/SophieH93/MS3/tree/master/wireframes/mobile)   
[Flowchart](https://github.com/SophieH93/MS3/tree/master/wireframes/flowchart)

I created my wireframes using [MockFlow](https://www.mockflow.com/) for various devices.
The **edit recipe page**  will be the same as the **add recipe page** hence I did not create an official woreframe for this page.   
The **delete recipie** will display a pop up to confirm with the user if they actually want to delete the recipe.

# Features



## Future Features:

# Information Architecture

## Database Choice

## Data Storage Types



# Technologies used

## Languages
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [JavaScript](https://www.javascript.com/)
* [Python](https://www.python.org/)

## Frameworks
* [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
* [MockFlow](https://www.mockflow.com/)

## Tools 
* [GitHub](https://github.com/)
* [GitPod](https://www.gitpod.io/)
* [Git](https://git-scm.com/about)
* [W3C Markup Validation](https://validator.w3.org/)
* [WSC CSS Validaion](https://jigsaw.w3.org/css-validator/)
* [Dirty Markup Formatter](https://www.10bestdesign.com/dirtymarkup/)

# Testing
Due to the scope of the website, there will need to be a lot of testing required during this project.

## **Create an account:**
* **Plan**-I will need to implement a way that a user will be able to create an account and that their **information** is **stored** in a **database**.        
This invloves checking that the users **passwords match** when they create a password and confirmed the password.   
I will need to **research** the best way to create this feature that's also easy for the user to create an account and properly hash the password when 
it's stored into the database.

* **Implementation** Sessions storage and [bcrypt](https://pypi.org/project/bcrypt/). Bcrypt is a password hashing function.  
* **Testing** - create a few accounts to check what values are passed and stored in the database. Test that passwords are the same.
* **Result**

## **Login to Account:**

* **Plan-** I will need to create a form for the user to login to their account. I will need to make sure the form is validated correctly.
* **Implementation-**To check the information from the form matches the information that is stored in the users collections and if it does not match,
a flash message is triggered to let the user know that their password/username is incorrect.
* **Testing-**
* **Result-**



# Bugs

# Deployment 

# Closing Notes

# Credits

# Disclaimer
**This websit is for educational purposes only.**