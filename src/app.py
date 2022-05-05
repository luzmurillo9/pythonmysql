from flask import Flask, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/cur'
app.config['SQALCHEMY_TRACK_MODIFACTIONS']= False

app.secret_key = ''

db = SQLAlchemy(app)
ma = Marshmallow(app)

#crear las tablas de la base de datos

class Articulos(db.Model):
    __tablename__ = "vivero"
    id = db.Column(db.Integer, primary_key=True)
    Nombre_platas = db.Column(db.String(70), uniqued = True)
    valor = db.Column(db.Float())
    cantidad = db.Column(db.Float())

    def __init__(self, Nombre_plantas, valor, cantidad):
       self.Nombre_platas = Nombre_plantas
       self.valor = valor
       self.cantidad = cantidad
db.create_all()

class viveroSchema(ma.Schema):
    class Meta:
        fields = ('id','Nombre_platas','valor','cantidad')

articulo_schema = viveroSchema()
articulos_schema = viveroSchema(many=True)

@app.route('/vivero',methods=['GET','POST'])
def articulos():
    all_vivero = vivero.query.all()
    resultadoVivero = vivero_schema(all_vivero)
    return resultadoVivero

@app.route('/addvivero',methods=['POST'])
def addvivero():
    if request.method == 'POST':
        #aquí obtengo los datos del formulario
        id = request.form['Id']
        viveroexit = Vivero.query.get(id)
        if viveroexit :
            return "no se puede almacernar los datos, el articulo ya existe"
        else:
            Nombre_plantas = request.form['Nombre_plantas']
            valor = request.form['valor']
            cantidad = request.form['cantidad']
            newvivero = Articulos(Nombre_plantas, Precio)
            #agregamos la data en la tabla
            db.session.add(newvivero)
            db.session.commit()
            return "guardado con exito"

