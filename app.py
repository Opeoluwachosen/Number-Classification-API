from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import math

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Check if a number is perfect
def is_perfect(n):
    if n < 2:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

# Check if a number is an Armstrong number
def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    return sum(int(digit) ** num_digits for digit in num_str) == n

# Check parity (even/odd)
def get_parity(n):
    return "even" if n % 2 == 0 else "odd"

# Calculate digit sum
def digit_sum(n):
    return sum(int(digit) for digit in str(n))

# Fetch a fun fact about the number
def get_fun_fact(n):
    url = f"http://numbersapi.com/{n}/math"
    try:
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            return response.text
    except requests.exceptions.RequestException:
        return "Fun fact unavailable at the moment."
    return f"No fun fact available for {n}."

# Get all properties of a number
def get_properties(n):
    properties = [get_parity(n)]
    if is_armstrong(n):
        properties.append("armstrong")
    return properties

# API Endpoint
@app.route("/api/classify-number", methods=['GET'])
def classify_number():
    number_str = request.args.get("number")  # Fixed query parameter name

    # Validate input: Ensure it's a valid integer
    if number_str is None or not number_str.lstrip('-').isdigit():
        return jsonify({"number": "alphabet", "error": True}), 400

    number = int(number_str)

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": get_properties(number),
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number),
    }

    # Override fun fact if Armstrong number
    if is_armstrong(number):
        digits = [int(d) for d in str(number)]
        length = len(digits)
        calculation = " + ".join(f"{d}^{length}" for d in digits) + f" = {number}"
        response["fun_fact"] = f"{number} is an Armstrong number because {calculation}"

    return jsonify(response), 200

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

