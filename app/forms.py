from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField("Please enter your full name", validators=[DataRequired()])
    email = StringField("Please enter your e-mail address", validators=[DataRequired(), Email()])
    subject = StringField("Please enter the subject of your message.", validators=[DataRequired()])
    message = TextAreaField("Please enter your message you would like to send", validators=[DataRequired()])
    submit = SubmitField("Send Email")