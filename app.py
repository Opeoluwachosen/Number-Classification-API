from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Enable CORS (restricting to API routes for security)
CORS(app, resources={r"/api/*": {"origins": "*"}})

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Check if a number is perfect. Only defined for positive numbers           
def is_perfect(n):
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum = 0

    for i in num_str:
        sum += int(i) ** num_digits
    
    return sum == n

def digit_sum(n):
    return f"{sum(int(i) for i in str((n)))}, // sum of its digits" 

# check if a number is even or odd
def get_parity(n):
    return "even" if int(n) % 2 == 0 else "odd"

# Return a list of mathematical properties.
def get_properties(n):
    properties = [get_parity(n)]
    
    if is_armstrong(n):
        properties.append("armstrong")
    return properties

# Fetch a fun fact about the number from the Numbers API with a timeout.
def get_fun_fact(n):
    url = f"http://numbersapi.com/{(n)}/math"  
    try:
        response = requests.get(url)  # Timeout after 2 seconds
        if response.status_code == 200:
            return response.text
    except requests.exceptions.RequestException:
        return "Fun fact unavailable at the moment."
    return "No fun fact available for {n}."

# API Endpoint
@app.route("/api/classify-number", methods=['GET'])
def classify_number():
    number_str = request.args.get("n")

    # If number parameter is missing
    if number_str is None or not number_str.isdigit():
        return jsonify({"number": "alphabet",    
                        "error": True
                    }), 400
            
    number = int(number_str)
        
    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": get_properties(number),
        "digit_sum": digit_sum(number), 
        "fun_fact": get_fun_fact(number)   
    }
        
        # if fun_fact is an armstrong number, Override
    if is_armstrong(number):
        digits = [int(i) for i in str(number)]
        length = len(digits)
        calculation = f"{' + '.join(f'{i}^{length}' for i in digits)} = {number}"
        response["fun_fact"] = f"{number} is an Armstrong number because {calculation}"


    return jsonify(response), 200   

# Run the app        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
