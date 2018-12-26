from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Email, ValidationError, Optional


class UserText(FlaskForm):
    user = StringField('', validators=[InputRequired()], render_kw={"placeholder": "TiVO E-mail", "class": "form-control"})

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        return True