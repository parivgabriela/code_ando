from flask import Flask, request, jsonify, send_from_directory, render_template
import pandas as pd
import random
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.static_folder = 'static'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Store questions in memory
questions = []
current_session = {
    'correct': 0,
    'total': 0,
    'review_questions': []
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'csv', 'xlsx', 'xls'}

@app.route('/')
def serve_static():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    global questions
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Read file based on extension
        if filename.endswith('.csv'):
            df = pd.read_csv(filepath)
        else:
            df = pd.read_excel(filepath)
        print('se leyo correctamente')
        # Validate columns
        if not all(col in df.columns for col in ['pregunta', 'respuesta']):
            return jsonify({'error': 'El archivo debe contener las columnas "pregunta" y "respuesta"'}), 400
        
        # Store questions
        questions = df[['pregunta', 'respuesta']].to_dict('records')
        current_session['correct'] = 0
        current_session['total'] = 0
        current_session['review_questions'] = []
        print('archivo cargado ok, antes del exitosos')

        
        return jsonify({'message': 'Archivo cargado exitosamente', 'total_questions': len(questions)})
    print('antes del error de tipo de archvio no permitido')
    return jsonify({'error': 'Tipo de archivo no permitido'}), 400

@app.route('/question', methods=['GET'])
def get_question():
    if not questions:
        return jsonify({'error': 'No hay preguntas cargadas'}), 400
    
    question = random.choice(questions)
    return jsonify({
        'pregunta': question['pregunta'],
        'respuesta': question['respuesta']
    })

@app.route('/submit', methods=['POST'])
def submit_answer():
    data = request.json
    current_session['total'] += 1
    
    if data.get('correct'):
        current_session['correct'] += 1
    else:
        current_session['review_questions'].append({
            'pregunta': data.get('pregunta'),
            'respuesta': data.get('respuesta')
        })
    
    return jsonify({
        'correct': current_session['correct'],
        'total': current_session['total']
    })

@app.route('/results', methods=['GET'])
def get_results():
    if current_session['total'] == 0:
        return jsonify({
            'percentage': 0,
            'review_questions': []
        })
    
    percentage = (current_session['correct'] / current_session['total']) * 100
    return jsonify({
        'percentage': round(percentage, 2),
        'review_questions': current_session['review_questions']
    })

if __name__ == '__main__':
    app.run(debug=True)