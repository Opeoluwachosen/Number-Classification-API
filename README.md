# Number-Classification-API
This is an API that takes a number and returns interesting mathematical properties about it, along with a fun fact. It is part of HNG12 Internship

## Features
- **Interesting Mathematical Properties**
    - **Prime Number Check**
    - **Perfect Number Check**
    - **Armstrong Number Check**
    - **Digit Sum Calculation**
    - **Parity ("even" or "odd") Check**
- **Fun Fact**: Returns a fun fact from [NUMBERSAPI](http://numbersapi.com/#42)
- **CORS enabled** for cross-origin requests
-  **HTTP Status Codes**
-  **JSON Responses**

## Technology stack
- **Programming Language:** Python
-  **Framework:** Flask
-  **Deployment:** AWS
-   **Version Control:** Git
   
## API Specification
**Endpoint**
- **GET** <your-url>/api/classify-number?number=371
## Response (200 OK)
```
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "class_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```
## Response (400 Bad Request)
```
{
    "number": "alphabet",
    "error": true
}
```

## Setup and Installation
- **launch an ec2 instance in AWS**
- **Allow port 5000 from anywhere for python Flask API**
- **ssh into your instance**
- **Install Python and its dependencies**
```
sudo apt update -y
sudo apt install python3 python3-pip
```
- **Verify the installation of Python and Pip**
```
python3 --version
pip3 --version
```
- **Set Up a Virtual Environment and Install Dependencies in a directory**
```
mkdir num_dir && cd num_dir

[//]: # install python3 virtual environment
sudo apt install python3-venv

[//]: # create a virtual environment
python3 -m venv myenv

[//]: # Activate the virtual environment
source myenv/bin/activate

[//]: # Install required dependencies
pip install -r requirements.txt
```

- **Verify Installation
```
pip list | grep flask
 ```
- **Clone the Project from GitHub into EC2**
  ```
  https://github.com/Opeoluwachosen/Number-Classification-API.git
  ```

- **Run the Flask API**
```
python app.py
```
