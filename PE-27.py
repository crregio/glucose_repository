from flask import Flask, jsonify, request
app = Flask(__name__)
new_glucose = [
        {
            "glucose_id": "1",
            "date": ["July 31, 2000"],
            "glucose": ["48 grams"]
        },
]

@app.route('/new_glucose', methods=['GET'])
def getNewGlucose():
    return jsonify(new_glucose)

@app.route('/new_glucose', methods=['POST'])
def postNewGlucose():
    glucose= request.get_json()
    new_glucose.append(glucose)
    return {'id': len(new_glucose)},200

@app.route('/new_glucose/<int:index>', methods=['DELETE'])
def deleteGlucose(index):
    new_glucose.pop(index)
    return 'Successfully deleted glucose!',200


if __name__ == '__main__':
    app.run()