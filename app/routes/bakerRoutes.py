from flask import Blueprint, render_template, request, redirect, url_for
from app.models.baker import Baker
from app import db

bp = Blueprint('baker', __name__)

@bp.route('/')
def index():
    data = Baker.query.all()
    return render_template('bakers/index.html', data=data)

@bp.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        nombrepana = request.form['nombrepana']
        especipana = request.form['especipana']

        newBaker = Baker(nombrepana=nombrepana, especipana=especipana)

        db.session.add(newBaker) 
        db.session.commit()

        return redirect(url_for('baker.index'))
                                
    return render_template('bakers/add.html')

@bp.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    baker = Baker.query.get_or_404(id)

    if request.method == 'POST':
        baker.nombrepana = request.form['nombrepana']
        baker.especipana = request.form['especipana']

        db.session.commit()

        return redirect(url_for('baker.index'))
    
    return render_template('bakers/edit.html', baker=baker)

@bp.route('/delete/<int:id>')
def delete(id):
    baker = Baker.query.get_or_404(id)

    db.session.delete(baker)
    db.session.commit()

    return redirect(url_for('baker.index'))