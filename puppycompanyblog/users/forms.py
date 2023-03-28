from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileAllowed, FileField

from flask_login import current_user
from puppycompanyblog.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo('pass_confirm', message="Passwords MUST match.")])
    pass_confirm = PasswordField("Confirm Password", validators=[DataRequired()]) ##EQUALTO??
    submit = SubmitField("Register")

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Your email has been registered already.")
    

    def check_username(self, field ):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username is already in use.")


    ###UPDATE, THIS SHOULD BE THE EMAIL FORM??
    def validate_email_form(self, email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError("Email has already been registered")
    ###UPDATE, THIS SHOULD BE THE USERNAME FORM??
    def validate_username_form(self, username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError("Username has already been registered!")

        
'''
    def validate_email(self, email):
        if email.data != current_user.email:
            if User.query.filter_by(email=email.data).first():
                raise ValidationError('Email has been registered')
    def validate_username(self, username):
        if username.data != current_user.username:
            if User.query.filter_by(username=username.data).first():
                raise ValidationError('Username has been registered') 
'''
class UpdateUserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    picture = FileField("Update Profile Picture", validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Update")

    def validate_email(self, email):
        if email.data != current_user.email:
            if User.query.filter_by(email=email.data).first():
                raise ValidationError('Email has been registered')
    
    def validate_username(self, username):
        if username.data != current_user.username:
            if User.query.filter_by(username=username.data).first():
                return ValidationError("Username has already been registered")



