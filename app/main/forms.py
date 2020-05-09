from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Would you like to tell us about yourself?', validators=[Required()])
    location = StringField('Where are you from?', validators=[Required()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    content = TextAreaField('Content',validators=[Required()])
    submit = SubmitField('Post')    