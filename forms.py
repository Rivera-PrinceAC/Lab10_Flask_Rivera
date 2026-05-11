from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import InputRequired, Email, Length, Optional

class RegisterForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[InputRequired(), Email(), Length(max=50)]
    )
    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=4)]
    )
    role = SelectField(
        'Role',
        choices=[('viewer', 'Viewer'), ('admin', 'Admin')]
    )
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[InputRequired(), Email()]
    )
    password = PasswordField(
        'Password',
        validators=[InputRequired()]
    )
    submit = SubmitField('Login')

class ProfileForm(FlaskForm):
    display_name = StringField(
        'Display Name',
        validators=[Optional(), Length(max=100)]
    )
    profile_image = FileField(
        'Profile Picture',
        validators=[
            FileAllowed(['jpg', 'jpeg', 'png'], 'Images only (jpg, png).')
        ]
    )
    submit = SubmitField('Update Profile')