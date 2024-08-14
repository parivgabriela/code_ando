from flask import Flask, render_template, request
from maths import generate_function

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    #primero seleccionar nivel
    return render_template('index.html')
    
@app.route('/select_level', methods=['POST'])
def select_level():
    level = request.form.get('level')
    random_function, result = generate_function(int(level))
    return render_template('math.html', function_r=random_function)

@app.route('/math')
def math():
    
    return render_template('math.html')


if __name__ == "__main__":
    app.run(debug=True)
