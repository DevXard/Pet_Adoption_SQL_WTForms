from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = '23f3fggg34'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def index():
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

@app.route('/add', methods=['POST', 'GET'])
def create_new_pet():
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        speacies = form.speacies.data
        photo = form.photo.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, speacies=speacies, photo=photo, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('new_pet.html', form=form)

@app.route('/pet/<int:id>')
def pet_info(id):
    pet = Pet.query.get_or_404(id)
    return render_template("pet_info.html", pet=pet)

@app.route('/pet/<int:id>/edit', methods=['POST', 'GET'])
def edit_pet(id):
    pet = Pet.query.get_or_404(id)
    form = PetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.speacies = form.speacies.data
        pet.photo = form.photo.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        db.session.commit()
        return redirect('/')
    else:    
        return render_template('edit.html', form=form)