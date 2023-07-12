from flask import Flask, Response, request, jsonify
import pymongo
import datetime
from datetime import timedelta
from mongo_flask import get_flight, get_flight_one_way, get_hotel
#from pymongo import MongoClient
#import dns

MONGODB = "mongodb+srv://userReadOnly:7ZT817O8ejDfhnBM@minichallenge.q4nve1r.mongodb.net"

app = Flask(__name__)

client = pymongo.MongoClient(MONGODB)
db = client['minichallenge']

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/flight', methods=['GET'])
def get_flights():
    checkinDate = request.args.get('checkInDate')
    checkoutDate = request.args.get('checkOutDate')
    city = request.args.get('destination')
    


    try:
        if not city:
            return jsonify({'error': 'Missing arguments'}), 400
        if not checkinDate:
            checkinDate = datetime.datetime.now().strftime('%Y-%m-%d')
        checkinDate = datetime.datetime.strptime(checkinDate, '%Y-%m-%d')
        if checkoutDate == None:
        
            result = get_flight_one_way(checkinDate, city, db)
        else:
            checkoutDate =  datetime.datetime.strptime(checkoutDate, '%Y-%m-%d')
            result = get_flight(checkinDate, checkoutDate, city, db)

        return jsonify(result), 200
        #return result, 200

    except Exception as e:

        return jsonify({'error': str(e)}), 400

@app.route('/hotel', methods=['GET'])
def get_hotels():
    checkinDate = request.args.get('checkInDate')
    checkoutDate = request.args.get('checkOutDate')
    city = request.args.get('destination')
    
    if not checkinDate or not checkoutDate or not city:
        return jsonify({'error': 'Missing arguments'}), 400
    

    try:
        checkinDate = datetime.datetime.strptime(checkinDate, '%Y-%m-%d')
        checkoutDate =  datetime.datetime.strptime(checkoutDate, '%Y-%m-%d') + timedelta(days=1)
        result = get_hotel(checkinDate, checkoutDate, city, db)

        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
