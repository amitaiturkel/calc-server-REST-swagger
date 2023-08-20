from flask import Flask, request, jsonify
class Calc:


    def __init__(self):
        self.result = 0


    def add(self, num):
        self.result += num


    def subtract(self, num):
        self.result -= num


    def multiply(self, num):
        self.result *= num


    def divide(self, num):
        if num != 0:
            self.result /= num
        else:
            print("Error: Division by zero is not allowed.")

    def put_in(self,num):
        self.result = num

    def clear(self):
        self.result = 0


    def get_result(self):
        return self.result
    
app = Flask("calculator")
calc = Calc()

def get_answer(calc, operator, num1):
    if operator == "add":
        calc.add(num1)
    elif operator == "subtract":
        calc.subtract(num1)
    elif operator == "multiply":
        calc.multiply(num1)
    elif operator == "divide":
        calc.divide(num1)
    elif operator == "put_in":
        calc.put_in(num1)
    elif operator == "clear":
        calc.clear()
    else:
        print("Invalid operator")
    return calc.get_result()

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    operator = data['operator']
    num = data['num']
    result = get_answer(calc, operator, num)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
