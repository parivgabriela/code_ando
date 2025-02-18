# app.py
from flask import Flask, render_template, request, jsonify
import pandas as pd
from werkzeug.utils import secure_filename
import os
#Desktop\Gabriela\Projects>
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'

ALLOWED_EXTENSIONS = {'xlsx', 'csv'}


# Aseguramos que existe el directorio de uploads
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Variable global para almacenar las preguntas
questions_data = None
# question
used_questions = set()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

#cargar el archivo desde index
@app.route('/upload', methods=['POST'])
def upload_file():
    global questions_data
    print("Files in request:", request.files)
    print("Form data:", request.form)
    if 'file' not in request.files:
        return 'No se seleccionó ningún archivo file not in request', 400
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No se seleccionó ningún archivo vacioo', 400
    else:
        print('no esta vacio')
    
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        print('nombre, ', filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Leer el archivo
        if filename.endswith('.xlsx'):
            questions_data = pd.read_excel(filepath)
        else:
            questions_data = pd.read_csv(filepath)
        
        # Verificar las columnas requeridas
        required_columns = ['pregunta', 'respuesta']
        if not all(col in questions_data.columns for col in required_columns):
            return jsonify({'error': 'El archivo debe contener las columnas: pregunta, respuesta'}), 400
        print('tiene las columnas requeridas')
        # Convertir a diccionario para JSON
        questions_list = questions_data.to_dict('records')
        return render_template('quiz.html', questions=questions_list)
    
    return jsonify({'error': 'Tipo de archivo no permitido'}), 400

@app.route('/quiz',  methods=['GET'])
def quiz():
    print('quiz')
    return render_template('quiz.html')

if __name__ == '__main__':
    app.run(debug=True)

