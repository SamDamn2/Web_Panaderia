from app import db

class Product(db.Model):
    __tablename__= 'product'
    id = db.Column(db.Integer, primary_key=True)
    nombrepro = db.Column(db.String(255), nullable=False)
    descripro = db.Column(db.String(255), nullable=False)
    preciopro = db.Column(db.BigInteger, nullable=False)
    bakers = db.relationship('Baker', secondary = 'product_baker')