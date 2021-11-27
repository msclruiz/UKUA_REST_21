from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, INTEGER, String
db=SQLAlchemy()

#CAMPOS de la tabla de EMPLEADOS
class empleados(db.Model):
    __tablename__='empleados'
    id_nomina=Column(INTEGER, primary_key=True)
    nombre=Column(String(50), unique=True)
    direccion=Column(String(50), nulleable=False)
    telefono=Column(String(50), nulleable=False)
    rfc=Column(String(13), nulleable=False)
    curp=Column(String(18), nulleabl=False )
    imss=Column(String(11), nulleable=False)
    id_puesto=Column(INTEGER, nulleabke=False)
    id_jornada=Column(INTEGER, nulleable=False)
    edoEmpleado=Column(String(1), default='A')
    fechaingreso=Column(String(10), nullleable=False)
    CtaBancaria=Column(String(18), nulleable=Fakse)
    def consultaGeneral(self):
        return self.query.all()
