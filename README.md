# Calculator Server and Interactive Clients

Welcome to the Calculator Server and Interactive Clients project! This repository contains a simple calculator server along with two interactive client scripts that interact with the server. Additionally, the project includes a folder with test cases for the calculator server.

## Getting Started

To get started with the project, follow these steps:

### Download the Project

Clone this repository to your local machine by running the following command in your terminal:

`git clone https://github.com/amitaiturkel/calc-server-test`
go to calc-server-test foldor 

### Set Up the Virtual Environment

Activate a virtual environment to isolate the project's dependencies. If you're using `virtualenv`, you can create and activate the environment with the following commands:

`python3 -m venv .venv` 
or run `python -m venv .venv`
and then
`source .venv/bin/activate`


### Install Dependencies

Use `poetry` to install the project's dependencies:

`poetry install`


This will ensure that all required packages are installed.

### Running Tests

Run the test suite using the `tox` command:

`tox`


This will execute the test cases located in the `tests` folder to ensure the code's correctness.

### Running the Calculator Server

To run the calculator server, execute the following command:
`python demo_poetry/calc_server.py` or `python3 demo_poetry/calc_server.py`

The server will start, and you'll be able to interact with it using the provided client scripts.

### Using the Interactive Clients

Two interactive client scripts are provided as examples to interact with the server:

1. To use the first interactive client, navigate to the `demo_poetry` folder and run the following command:

`python client_server.py` or  `python3 client_server.py`

2. To use the second interactive client, navigate to the `demo_poetry` folder and run the following command:

`python client_server2.py` or `python3 client_server2.py`


Both clients will allow you to perform various operations on the calculator server.

## Swagger Documentation

The calculator server supports Swagger documentation, which allows you to explore its API endpoints interactively. You can access the Swagger UI by opening the following URL in your web browser after you made sure the server is running:

`http://localhost:8000/docs`


## Contributing

If you'd like to contribute to this project, please follow the standard GitHub pull request process.

## License

This project is licensed under the MIT License.
