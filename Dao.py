from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, INTEGER, String

db=SQLAlchemy()

#CAMPOS de la tabla de EMPLEADOS
class empleados(db.Model):
    __tablename__='empleados'
    id_nomina=Column(INTEGER, primary_key=True)
    nombre=Column(String(50), unique=True)
    direccion=Column(String(50), nullable=False)
    telefono=Column(String(50), nullable=False)
    rfc=Column(String(13), nullable=False)
    curp=Column(String(18), nullable=False )
    imss=Column(String(11), nullable=False)
    id_puesto=Column(INTEGER, nullable=False)
    id_jornada=Column(INTEGER, nullable=False)
    edoEmpleado=Column(String(1), default='A')
    fechaingreso=Column(String(10), nullable=False)
    CtaBancaria=Column(String(18), nullable=False)
    def consultaGeneral(self):
        return self.query.all()
