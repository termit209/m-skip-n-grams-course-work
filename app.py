"""
Main application module.
Use it to serve as docker container entry point.
"""

from json import loads

from flask import Flask, request, jsonify

from cfg import output

script_name = __file__.split("\\")[-1].split(".")[0] if "\\" in __file__ else __file__.split("/")[-1].split(".")[0]
print(script_name)


app = Flask(__name__)


@app.route('/', methods=["GET"])
def hello_world():
    """
    ./ - root endpoint with get method
    describe methods specific to your application here
    :return:
    """
    output.info("Root request")
    output.error("MUST BE SHOWN")

    return 'use "/predict" for prediction with .json application'


@app.route('/predict', methods=["POST"])
def predict():
    """
    Predicts with model based on application content
    :return:
    """
    inp_dct = loads(request.data)
    LOGGER.info(inp_dct)
    return jsonify({"response": list(range(9))})


if __name__ == '__main__':
    app.run(port=8080, host="0.0.0.0")
