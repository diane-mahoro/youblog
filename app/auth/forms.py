from flask_wtf import FlaskForm
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError

class SignUpForm(FlaskForm):
    username=StringField('User name',validators=[Required()])
    email=StringField('Email',validators=[Required(),Email()])
    passhere=PasswordField('your password',validators=[Required(),EqualTo('pass_comfirm',message='Passwods entered must match')])
    pass_comfirm=PasswordField('comfirm password')
    submit=StringField('sign up')

    def validate_email(self,data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError("There is an account with that email")

    def validate_username(self,data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError("There is an account with that username")
