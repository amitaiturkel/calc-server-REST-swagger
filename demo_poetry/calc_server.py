from fastapi import FastAPI, Header, HTTPException

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
            raise HTTPException(status_code=400, detail="Division by zero is not allowed.")

    def put_in(self, num):
        self.result = num

    def clear(self):
        self.result = 0

    def get_result(self):
        return self.result

app = FastAPI()
users = dict()
def get_user_calc(user_id):
    if user_id not in users.keys():
        users[user_id] = Calc()
    return users[user_id]

    
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
        raise HTTPException(status_code=400, detail="Invalid operator")
    return calc.get_result()

@app.get('/calculate/add')
async def calculate(num,user_id: str = Header(None)):
    calc = get_user_calc(user_id)
    operator = 'add'
    result = get_answer(calc, operator, num)
    return {'result': result}

@app.get('/calculate/subtract')
async def calculate(num,user_id: str = Header(None)):
    calc = get_user_calc(user_id)
    operator = 'subtract'
    result = get_answer(calc, operator, num)
    return {'result': result}

@app.get('/calculate/multiply')
async def calculate(num,user_id: str = Header(None)):
    calc = get_user_calc(user_id)
    operator = 'multiply'
    result = get_answer(calc, operator, num)
    return {'result': result}

@app.get('/calculate/divide')
async def calculate(num,user_id: str = Header(None)):
    calc = get_user_calc(user_id)
    operator = 'divide'
    result = get_answer(calc, operator, num)
    return {'result': result}

@app.patch('/calculate/put_in')
async def calculate(num,user_id: str = Header(None)):
    calc = get_user_calc(user_id)
    operator = 'put_in'
    result = get_answer(calc, operator, num)
    return {'result': result}

@app.delete('/calculate/clear')
async def calculate(num,user_id: str = Header(None)):
    calc = get_user_calc(user_id)
    operator = 'clear'
    result = get_answer(calc, operator, num)
    return {'result': result}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/")
async def read_item1():
    return "hello"