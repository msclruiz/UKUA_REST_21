from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, INTEGER, String
import json
from flask import jsonify

db = SQLAlchemy()


# CAMPOS de la tabla de EMPLEADOS
class empleados(db.Model):
    __tablename__ = 'empleados'
    id_nomina = Column(INTEGER, primary_key=True)
    nombre = Column(String(50), unique=True)
    direccion = Column(String(50), nullable=False)
    telefono = Column(String(50), nullable=False)
    rfc = Column(String(13), nullable=False)
    curp = Column(String(18), nullable=False)
    imss = Column(String(11), nullable=False)
    id_puesto = Column(INTEGER, nullable=False)
    id_jornada = Column(INTEGER, nullable=False)
    edoEmpleado = Column(String(1), default='A')
    fechaingreso = Column(String(10), nullable=False)
    CtaBancaria = Column(String(18), nullable=False)
    def consultaGeneral(self):
        dict_json = {"estatus": "", "mensaje": "", "empleados": []}
        try:
            dict_json['estatus'] = "ok"
            lista = self.querey.filter(empleados.estatus=='A').all()
            if len(lista)>0:
                dict_json['mensaje'] = 'LISTADO DE EMPLEADOS'
                dict_json['empleados'] = self.to_json_list(lista)
            else:
                dict_json['mensaje'] = "NO HAY EMPLEADOS REGISTRADOS"
        except:
            dict_json['estatus'] = 'Error'
            dict_json['mensaje'] = 'ERROR AL EJECUTAR LA CONSULTA DE EMPLEADOS'
        return json.dumps(dict_json)

    def to_json_list(self, lista):
        lista_empleados = []
        for o in lista:
            lista_empleados.append(self.to_json(o))
        return lista_empleados

    def to_json(self,o):
        empleado = {"id_nomina": o.id_nomina, "nombre": o.nombre, "direccion": o.direccion, "telefono": o.telefono,
                    "rfc": o.rfc, "curp": o.curp, "imss": o.imss, "id_puesto": o.id_puesto, "id_jornada": o.id_jornada,
                    "edoEmpleado": o.edoEmpleado, "fechaingreso": o.fechaingreso, "ctaBancaria": o.ctaBancaria}
        return empleado


