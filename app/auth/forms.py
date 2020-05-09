rom flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class SignUpForm(FlaskForm):
    email = StringField('Enter your email Address', validators=[Required(),Email()])
    username = StringField('Enter your username',validators=[Required()])
    password = PasswordField('Password'validators=[Required(),EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm your password',validators = [Required()])

    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

