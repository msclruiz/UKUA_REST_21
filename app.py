from flask import Flask, request, jsonify
import json

app=Flask(__name__)

#CONFIGURACION DE LA BASE DE DATOS CON SQLALQUEMY
app.config['SQLALCHEMY_DATABAS_URI']='mysql+pymysql://coordinadorRH:Hola.123@localhost:3306/ukuadb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False



@app.route('/')
def inicio():
    return 'Escuchando el servicio REST de SISTEMA: Dispersion de Nomina'

@app.route('/empleados')
def empleados():
    return 'Empleados'

@app.route('/empleados/<int:id_nomina>')
def empleado(id_nomina):
    return 'Consultando empleado # ' + str(id_nomina)


#SECCION PARA INICIALIZAR LOS SERVICIOS A UTILIZAR GET POST ETC

#METODO GET
@app.route('/opciones/',methods=['GET'])
def opciones():
    opciones={"estatus":"ok","mensaje":"LISTADO DE OPCIONES",
              "opciones":[{"idOpcion":1,"nombre":"LEONARDO","descripcion":"conocido"}]}
    return json.dumps(opciones)

@app.route('/opciones/<int:id>',methods=['GET'])
def opcion(id):
    opcion={"estatus":"ok","mensaje":"LISTADO DE OPCIONES",
            "opciones":[{"idOpcion":id,"nombre":"LEONARDO","descripcion":"conocido"}]}
    return json.dumps(opcion)


#METODO POST
@app.route('/opciones/', methods=['POST'])
def registroOpcion():
    opcion = request.get_json()
    salida = {"estatus":"ok", "mensaje":"OPCION REGISTRADA CON EXITO"}
    return json.dumps(salida)

#METODO PUT
@app.route('/opciones/', methods=['PUT'])
def modificarOpcion():
    opcion=request.get_json()
    salida={"esetatus":"ok","mensaje":"OPCION MODIFICADA CON EXITO"}
    return json.dumps(salida)

#METODO DELETE
@app.route('/opciones', methods=['DELETE'])
def eliminaOpcion(id):
    salida={"estatus":"ok","mensaje":"OPCION # " + str(id) + " ELIMINADA CON EXITO"}
    return  jsonify(salida)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

