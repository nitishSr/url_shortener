from wtforms import Form, StringField

# Import Form validators
from wtforms.validators import DataRequired


# Define the login form (WTForms)

class UrlShortenerForm(Form):
    input_url    = StringField('URL', [
                DataRequired(message='URL field cannot be empty !')])
