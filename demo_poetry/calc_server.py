from typing import Annotated
from fastapi import FastAPI, Header, HTTPException,Request

class Calc:
    def __init__(self):
        self.result = 0.0

    def add(self, num):
        self.result += float(num)

    def subtract(self, num):
        self.result -= float(num)

    def multiply(self, num):
        self.result *= float(num)

    def divide(self, num):
        if float(num) != 0:
            self.result /= float(num)
        else:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed.")

    def put_in(self, num):
        self.result = float(num)

    def clear(self):
        self.result = 0.0

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
calc = Calc()
@app.get('/calculate/add')
async def calculate(num,user_agent: Annotated[str | None, Header()] = None):
    calc = get_user_calc(user_agent)
    operator = 'add'
    result = get_answer(calc, operator, num)
    return {'result': result}

@app.get('/calculate/subtract')
async def calculate(num,user_agent: Annotated[str | None, Header()] = None):
    calc = get_user_calc(user_agent)
    operator = 'subtract'
    result = get_answer(calc, operator, num)
    return {'result': result}

@app.get('/calculate/multiply')
async def calculate(num,user_agent: Annotated[str | None, Header()] = None):
    calc = get_user_calc(user_agent)
    operator = 'multiply'
    result = get_answer(calc, operator, num)
    return {'result': result}

@app.get('/calculate/divide')
async def calculate(num,user_agent: Annotated[str | None, Header()] = None):
    calc = get_user_calc(user_agent)
    operator = 'divide'
    result = get_answer(calc, operator, num)
    return {'result': result}

@app.patch('/calculate/put_in')
async def calculate(num,user_agent: Annotated[str | None, Header()] = None):
    calc = get_user_calc(user_agent)
    operator = 'put_in'
    result = get_answer(calc, operator, num)
    return {'result': result}

@app.delete('/calculate/clear')
async def calculate(num,user_agent: Annotated[str | None, Header()] = None):
    calc = get_user_calc(user_agent)
    operator = 'clear'
    result = get_answer(calc, operator, num)
    return {'result': result}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/")
async def read_item1():
    return len(users)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
