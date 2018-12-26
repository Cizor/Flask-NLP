from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from forms import UserText


def create_app():
    a = Flask(__name__)
    Bootstrap(a)
    return a


app = create_app()
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'A secret key'


@app.route('/')
def hello_world():
    form = UserText()
    if form.validate_on_submit():
        print(request.form)
    return render_template('first_page.html', form=form)


if __name__ == '__main__':
    app.run()
