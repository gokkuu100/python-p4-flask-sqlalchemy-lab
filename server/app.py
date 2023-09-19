# #!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id == id).first()
    response_body = f'<ul>ID: {animal.id}</ul>'
    response_body += f'<ul>Name: {animal.name}</ul>'
    response_body += f'<ul>Species: {animal.species}</ul>'
    response_body += '<ul>Zookeeper:</ul>'
    response_body += f'<ul>Name: {animal.zookeeper.name}</ul>'
    response_body += f'<ul>Birthday: {animal.zookeeper.birthday}</ul>'
    response_body += '<ul>Enclosure:</ul>'
    response_body += f'<ul>Environment: {animal.enclosure.environment}</ul>'
    response_body += f'<ul>Open to Visitors: {animal.enclosure.open_to_visitors}</ul>'

    return make_response(response_body)

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()
    response_body = f'<ul>ID: {zookeeper.id}</ul>'
    response_body += f'<ul>Name: {zookeeper.name}</ul>'
    response_body += f'<ul>Birthday: {zookeeper.birthday}</ul>'
    response_body += '<ul>Animals:</ul>'
    for animal in zookeeper.animals:
        response_body += f'<ul>Name: {animal.name}</ul>'
        response_body += f'<ul>Species: {animal.species}</ul>'

    return make_response(response_body)

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()
    response_body = f'<ul>ID: {enclosure.id}</ul>'
    response_body += f'<ul>Environment: {enclosure.environment}</ul>'
    response_body += f'<ul>Open to Visitors: {enclosure.open_to_visitors}</ul>'
    response_body += '<ul>Animals:</ul>'
    for animal in enclosure.animals:
        response_body += f'<ul>Name: {animal.name}</ul>'
        response_body += f'<ul>Species: {animal.species}</ul>'

    return make_response(response_body)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
