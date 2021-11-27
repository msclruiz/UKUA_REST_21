from flask import Flask, request, jsonify
import json

app=Flask(__name__)

@app.route('/')
def inicio():
    return 'Escuchando el servicio REST de SISTEMA: Dispersion de Nomina'

@app.route('/empleados')
def empleados():
    return 'Empleados'

@app.route('/empleados/<int:id_nomina>')
def empleado(id_nomina):
    return 'Consultando empleado # ' + str(id_nomina)


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

