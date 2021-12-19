# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash
from app.mod_url.forms import UrlShortenerForm
from app.mod_url import url_shortener

# Define the blueprint: 'auth', set its url prefix: app.url/auth
api = Blueprint('api', __name__)

# Set the route and accepted methods
@api.route('/', methods=['GET', 'POST'])
def index():
    # If form is submitted
    form = UrlShortenerForm(request.form)

    # Verify the sign in form
    if request.method == "POST":
        input_url = request.form['input_url']
        if input_url:
            shortened_url = url_shortener(input_url)
            # return redirect(url_for('auth.home'))
        else:
            flash('URL is required !', 'error-message')

    return render_template("index.html", form=form)