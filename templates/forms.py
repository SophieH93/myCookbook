from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo


class addRecipe(FlaskForm)
    recipe_name = StringField('Recipe Name', 
                                validators=[DataRequired(), Length(min=3, max=20)])
    recipe_description = StringField('Recipe Description',
                                validators=[DataRequired(), Length(min=3, max=20)])                        
    cooking_time = IntegerField('Cooking Time', validators=[DataRequired()])
    prep_time = IntegerField('Prep Time', validators=[DataRequired()])
    category = SelectField('Category')
    ingredients = TextAreaField('Ingredients',
                                validators=[DataRequired()])
    steps = TextAreaField('Steps',
                               validators=[DataRequired()])
    image = StringField('Recipe Image')                          
    submit = SubmitField('Add Recipe')                    