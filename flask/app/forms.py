from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired
 
class AddItemsForm(FlaskForm):

  Category = StringField("Category")
  Vendor = StringField("Vendor")
  Model = StringField("Model")
  Price = IntegerField("Price")
  submit = SubmitField("Submit")

class SearchItemsForm(FlaskForm):
  
  Category = StringField("Category")
  Submit = SubmitField("Search")

