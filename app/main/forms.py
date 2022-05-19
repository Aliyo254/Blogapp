from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField,SelectField
from wtforms.validators import DataRequired


class BlogForm(FlaskForm):
    title=SelectField('title',choices=[('Sports', 'Sports'), ('Life style', 'Life style'), ('Tech', 'Tech')], validators = [DataRequired()])
    blog = TextAreaField('pitblogch',validators=[DataRequired()])
    submit = SubmitField('submit')
class CommentForm(FlaskForm):
    comment=TextAreaField('comment',validators=[DataRequired()])
    submit = SubmitField('submit')
