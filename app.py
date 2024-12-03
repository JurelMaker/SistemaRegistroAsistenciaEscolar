from flask import Flask,render_template,redirect,url_for
from modelos.models import db
from flask_migrate import Migrate
import os

app = Flask(__name__)

directorio = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio,'modelos/escuela.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
Migrate(app,db)

if __name__ == '__main__':
    
    app.run(debug=True)
