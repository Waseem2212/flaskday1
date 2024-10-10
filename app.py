from flask import Flask,jsonify,request

app = Flask(__name__)



@app.route('/')
def home():
    return jsonify({'mes':'welcome to the Flask'})

@app.route('/api/get-name', methods=['GET'])
def get_name():
    data = {'name': 'waseem'}
    return jsonify(data)

@app.route('/api/post-name',methods=['POST'])
def post_name():
    data = request.get_json()
    # print(data['name'])
    if data.age < 18:
        return print('Your are adult')
    else:
        print('your are not adult')
    res = {'rec':data}
    # print(res)
    return jsonify(res), 201


if __name__ == "__main__":
    app.run(debug=True, port='8585')