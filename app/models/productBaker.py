from app import db

class ProductBaker(db.Model):
    __tablename__= 'product_baker'
    id = db.Column(db.Integer, primary_key=True)
    products = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    bakers = db.Column(db.Integer, db.ForeignKey('baker.id'), primary_key=True)
    fechaprepa = db.Column(db.Date, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)