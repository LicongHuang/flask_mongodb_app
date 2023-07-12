from mongo_query import BaseQuery

def get_flight(departDate, returnDate, city, db):
    query = BaseQuery()
    flights = query.getFlights(departDate, returnDate, city, db)
    
    result = []
    dFlight = flights[0]
    rFlight = flights[1]
    for i in range(len(dFlight)):
        if city == None:
            continue

        print(city)

        entry = {
                'City': city,
                'Departure Date': departDate.strftime('%Y-%m-%d'),
                'Depart Airline': dFlight[i]['airlinename'],
                'Depart Price' : dFlight[i]['price'],
                'Return Date': returnDate.strftime('%Y-%m-%d'),
                'Return Airline': rFlight[i]['airlinename'],
                'Return Price' : rFlight[i]['price']
                }
        #jsonified = jsonify(entry)
        result.append(entry)

    return result


def get_flight_one_way(departDate, city, db):
    query = BaseQuery()
    flights = query.getSingleFlight(departDate, city, db)
    result = []
    print(city)
    for flight in flights:
        if city == None:
            continue

        entry = {
                'City': city,
                'Departure Date': departDate.strftime('%Y-%m-%d'),
                'Depart Airline': flight['airlinename'],
                'Depart Price' : flight['price']
                }
        #jsonified = jsonify(entry)
        result.append(entry)
    return result
#print(get_flight('2023-12-10', '2023-12-16', 'Frankfurt', db))

def get_hotel(checkIn, checkOut, city, db):
    query = BaseQuery()
    hotelsInfo = query.getHotels(checkIn, checkOut, city, db)
    hotelPrices = {}
    print(city)
    for hotelInfo in hotelsInfo:
        if hotelInfo['hotelName'] not in hotelPrices:
            hotelPrices[hotelInfo['hotelName']] = 0
        hotelPrices[hotelInfo['hotelName']] += hotelInfo['price']


    #print(hotelPrices)
    result = []
    for index, (key, value) in enumerate(hotelPrices.items()):
        entry = {
                'City': city,
                'Check In Date': checkIn.strftime('%Y-%m-%d'),
                'Check Out Date': checkOut.strftime('%Y-%m-%d'),
                'Hotel': key,
                'Price' : value
                }
        #jsonified = jsonify(entry)
        result.append(entry)
    resultSorted = sorted(result, key=lambda k: k['Price'])
    return resultSorted




