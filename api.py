from flask import Flask, jsonify, request
from flask_cors import CORS
import package_sorter


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route('/sort')
def sort():
    width = request.args.get("width")
    height = request.args.get("height")
    length = request.args.get("length")
    weight = request.args.get("mass")
    
    # dcebuggging
    print(type(width))


    print("Sort endpoint called")
    #  some input checking
    try:
        sortResult = package_sorter.sortFunction(width= float(width), height=float(height),length=float(length), mass=float(weight))
    except ValueError:
        app.logger.error("Sort datatype mismatch")
        return jsonify({"Result": "Error in input"}), 400
    
    return jsonify({"Result": sortResult}), 200


@app.route('/healthcheck')
def ping():
    app.logger.info("Healthcheck endpoint called")
    return jsonify({"status": "healthy"}), 200



if __name__ =='__main__':
    app.run()

