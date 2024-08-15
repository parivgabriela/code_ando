from flask import Flask, render_template, request
from maths import generate_function
import sys

app = Flask(__name__)

result = None
level = None
result_wrong = 'Wrong! Try again!'
result_ok = 'Well done!'
score = 0

@app.route('/', methods=['GET'])
def index():
    #primero seleccionar nivel
    return render_template('index.html')
    
@app.route('/select_level', methods=['POST'])
def select_level():
    global level
    level = int(request.form.get('level'))
    global result
    random_function, result = generate_function(level)
    return render_template('math.html', function_r=random_function)

@app.route('/check_result', methods=['POST'])
def math():
    result_input = request.form.get('user_result')
    global result
    global score
    if result_input == result:
        score += 100
        random_function, result = generate_function(level)

        return render_template('math.html', function_r=random_function, status_result=result_ok, score=score)
    else:
        score -= 10
        random_function, result = generate_function(level)

        return render_template('math.html', function_r=random_function, status_result=result_ok, score=score)
        

if __name__ == "__main__":
    app.run(debug=True)
