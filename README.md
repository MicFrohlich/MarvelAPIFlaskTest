# Getting Started
To Get up and running with this Marvel API task please ensure that you have Python and Flask installed
to ensure you have python installed please ensure the code below returns

    python --version

With python installed make sure you have pip and flask installed, if not, please install with the code below

    pip install flask

To run the simple application, once pip, flask and python are installed. Navigate to the directory test_flask_app_version and create a file called:

    secrets.py

Inside secrets.py please place your public and pprivate keys from the Marvel API in the format:

    PUBLIC_KEY = ""
    PRIVATE_KEY = ""

Once the keys/secrets have been placed in the appropriate file, you can run the project using the line below

    flask --app app.py --debug run

When the project is running, please navigate to localhost:5000 on your browser to see the project