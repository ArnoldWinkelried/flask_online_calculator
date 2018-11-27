from flask import Flask, render_template, request


app = Flask(__name__)


possible_operations = {'add': lambda x, y: x + y,
                       'subtract': lambda x, y: x - y,
                       'multiply': lambda x, y: x * y,
                       'divide': lambda x, y: x / y
                       }


@app.route('/calculation_result', methods=['POST'])
def operation():
    operator_chosen = request.form['operator']
    first_number = int(request.form['f_number'])
    second_number = int(request.form['s_number'])

    if second_number == 0 and operator_chosen == 'divide':
        result = "Why?"
    else:
        result = possible_operations[operator_chosen](first_number, second_number)

    return render_template('index.html', result=result)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
