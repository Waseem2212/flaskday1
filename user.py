from flask import Flask,request , jsonify

app = Flask(__name__)

@app.route('/api/bio-data', methods=['POST'])
def bio_data():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    city = data.get('city')
    region = data.get('region')

    username = name[0]

    if int(age) < 18:
        return jsonify({'message':'Age is less than 18'})
    
    if region != 'pakistan':
        return jsonify({'message':'you are not from pakistan'})
    

    return jsonify({
        "username" : username,
        "name" : name,
        "age" : age,
        "city" :city,
        "region" : region
    }),200
    
if __name__ == "__main__":
    app.run(debug=True,port=8080)
    
