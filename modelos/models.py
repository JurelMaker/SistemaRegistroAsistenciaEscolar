from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Grupo(db.Model):
    __tablename__='Cat_Grupos'
    id = db.Column(db.Integer,primary_key=True)
    identificador = db.Column(db.String(2))
    alumn = db.relationship('Alumno',backref='alumno_grupo',lazy='dynamic')

class Alumno(db.Model):
    __tablename__='Alumno'
    matricula = db.Column(db.String(8),primary_key=True)
    nombre = db.Column(db.Text)
    apellido = db.Column(db.Text)
    id_grupo = db.Column(db.Integer,db.ForeignKey('Cat_Grupos.id',name='Grupo'))

    def __init__(self,matricula,nombre,apellido,id_grupo):
        self.matricula = matricula
        self.nombre = nombre 
        self.apellido = apellido
        self.id_grupo = id_grupo
