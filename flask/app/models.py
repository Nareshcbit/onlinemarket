from app import db
from app import ma

class Items(db.Model):

    __tablename__ = 'Items'

    Uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Category = db.Column(db.String(64), index=True)
    Vendor = db.Column(db.String(64), index=True)
    Model = db.Column(db.String(64), index=True)
    Price = db.Column(db.Integer, index=True)


    def __repr__(self):
        return '<Items {}>'.format(self.Uid)

    def __init__(self, Category, Vendor, Model, Price):
        self.Category = Category
        self.Vendor = Vendor
        self.Model = Model
        self.Price = Price

class ItemsSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('Uid', 'Category', 'Vendor', 'Model', 'Price')