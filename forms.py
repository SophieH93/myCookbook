from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo


class addRecipeForm(FlaskForm):

    recipe_name = StringField('Recipe Name',
                              validators=[DataRequired()])
    recipe_description = TextAreaField('Recipe Description',
            validators=[DataRequired()])
    prep_time = IntegerField('Prep Time (min)',
                             validators=[DataRequired()])
    cooking_time = IntegerField('Cooking Time (min)',
                                validators=[DataRequired()])
    category = TextAreaField('category', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients',
                                validators=[DataRequired()])
    steps = TextAreaField('Steps', validators=[DataRequired()])
    image = StringField('Recipe Image')
    submit = SubmitField('Add Recipe')