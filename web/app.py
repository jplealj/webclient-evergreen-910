from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__, template_folder='templates')

# mediciones_list = [
#     {'fecha':'10/09/2019 15:42:44', 'origen':'Sensor en terreno', 'valor':21, 'codigoSensor':1,'observacion':'bien'},
#     {'fecha':'10/09/2019 15:21:02', 'origen':'Imagen dron', 'valor':12, 'codigoSensor':4,'observacion':'peligroso'},
#     {'fecha':'04/09/2019 12:03:59', 'origen':'Imagen satelital', 'valor':29, 'codigoSensor':3,'observacion':'regular'},
#     {'fecha':'03/09/2019 19:59:59', 'origen':'Dato derivado', 'valor':1, 'codigoSensor':2,'observacion':'peligroso'},
#     {'fecha':'29/08/2019 08:43:13', 'origen':'Imagen satelital', 'valor':25, 'codigoSensor':3,'observacion':'regular'},
#     {'fecha':'28/08/2019 10:32:23', 'origen':'Imagen dron', 'valor':14, 'codigoSensor':4,'observacion':'peligroso'}
# ]

origenes_list = ['Sensor en terreno', 'Imagen satelital', 'Imagen dron', 'Dato derivado']

@app.route('/crearSensor', methods=['GET'])
def crearSensor():
    return render_template('crearSensor.html', origenes=origenes_list)

@app.route('/listarSensores', methods=['GET'])
def listarSensores():
    mediciones_list = requests.get('https://api-evergreen-910.azurewebsites.net/mediciones').json()
    return render_template('listarSensores.html', mediciones=mediciones_list)

@app.route('/guardarSensor', methods=['POST'])
def guardarSensor():
    print("1")
    medicion = dict(request.values)
    medicion['valor'] = int(medicion['valor'])
    medicion['fecha'] = str(medicion['fecha'])
    medicion['codigoSensor'] = int(medicion['codigoSensor'])
    medicion['observacion'] = str(medicion['observacion'])
    requests.post('https://api-evergreen-910.azurewebsites.net/mediciones',json=medicion)
    return (listarSensores())


