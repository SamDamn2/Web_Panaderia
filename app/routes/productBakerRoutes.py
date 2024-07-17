from flask import Blueprint, render_template, request, redirect, url_for
from app.models.product import Product
from app.models.baker import Baker
from app.models.productBaker import ProductBaker
from sqlalchemy import text
from app import db

bp = Blueprint('productBaker', __name__)

@bp.route('/ProductBaker')
def index():
    data = ProductBaker.query.all()
    products = Product.query.all()
    bakers = Baker.query.all()

    return render_template('productBakers/index.html', data=data, products=products, panadero=bakers)

@bp.route('/addProductBaker', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        product_id = request.form['product_id']
        baker_id = request.form['baker_id']
        fechaprepa = request.form['fechaprepa']
        cantidad = request.form['cantidad']

        newProductBaker = ProductBaker(bakers=product_id, products=baker_id, fechaprepa=fechaprepa, cantidad=cantidad)

        db.session.add(newProductBaker)
        db.session.commit()

        return redirect(url_for('productBaker.index'))
    
    products = Product.query.all()
    bakers =  Baker.query.all()
    return render_template('productBakers/add.html', products=products, bakers=bakers)

@bp.route('/editProductBaker/<int:id>', methods=['GET','POST'])
def edit(id):
    productBaker = ProductBaker.query.get_or_404(id)
    
    if request.method == 'POST':
        productBaker.product_id = request.form['product_id']
        productBaker.baker_id = request.form['baker_id']
        productBaker.fechaprepa = request.form['fechaprepa']
        productBaker.cantidad = request.form['cantidad']

        db.session.commit()

        return redirect(url_for('productBaker.index'))
    products = Product.query.all()
    bakers = Baker.query.all()
    return render_template('productBakers/edit.html', productBaker=productBaker, products=products, bakers=bakers)

@bp.route('/deleteProductBaker/<int:id>')
def delete(id):
    productBaker = ProductBaker.query.get_or_404(id)

    db.session.delete(productBaker)
    db.session.commit()

    return redirect(url_for('productBaker.index'))