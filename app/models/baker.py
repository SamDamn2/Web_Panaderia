from app import db

class Baker(db.Model):
    __tablename__= 'baker'
    id = db.Column(db.Integer, primary_key=True)
    nombrepana = db.Column(db.String(255), nullable=False)
    especipana = db.Column(db.String(255), nullable=False)
    products = db.relationship('Product', secondary = 'product_baker')