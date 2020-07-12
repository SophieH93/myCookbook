from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo


class addRecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name', 
                                validators=[DataRequired()])
    recipe_description = TextAreaField('Recipe Description',
                                validators=[DataRequired(), Length(min=3, max=20)])                        
    cooking_time = IntegerField('Cooking Time (min)', validators=[DataRequired()])
    category = SelectField('Category')
    ingredients = TextAreaField('Ingredients',
                                validators=[DataRequired()])
    steps = TextAreaField('Steps',
                               validators=[DataRequired()])
    image = StringField('Recipe Image')                          
    submit = SubmitField('Add Recipe')                    