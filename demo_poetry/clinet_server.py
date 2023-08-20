import httpx

async def interact_with_calculator():
    print("Welcome to the calculator program. Enter 'Q' to quit at any time.")

    while True:
        operator = input("Enter an operator ('add', 'subtract', 'multiply', 'divide', 'clear', 'put_in') or 'Q' to quit: ")
        
        if operator.lower() == "q":
            print("Exiting the program.")
            break
        
        if operator not in ['add', 'subtract', 'multiply', 'divide', 'clear', 'put_in']:
            print("Invalid operator. Please enter a valid operator or 'Q' to quit.")
            continue
        
        try:
            num = float(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        url = "http://localhost:8000/calculate/"+operator  # URL of the calculator service

        data = {'num': num}
        
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=data)

        if response.status_code == 200:
            result = response.json()['result']
            print(f"Result: {result}")
        else:
            print("An error occurred while communicating with the calculator service.")
    
if __name__ == "__main__":
    import asyncio
    asyncio.run(interact_with_calculator())
