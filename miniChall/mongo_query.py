class BaseQuery():
    
    def getFlights(self, departureDate, returnDate, destination, db):
        collection = db['flights']
        queryCondition1 = { 'date' : departureDate, 'srccity' : 'Singapore', 'destcity' : destination }
        queryResult1 = collection.find(queryCondition1)
        queryCondition2 = { 'date' : returnDate, 'srccity' : destination, 'destcity' : 'Singapore'}
        queryResult2 = collection.find(queryCondition2)
        departtrip = sorted(queryResult1, key=lambda k: k['price'])
        returntrip = sorted(queryResult2, key=lambda k: k['price'])
        if len(departtrip)== 0 or len(returntrip) == 0:
            return [], []
        return departtrip[0], returntrip[0]

    def getSingleFlight(self, departureDate, destination, db):
        collection = db['flights']
        queryCondition1 = { 'date' : departureDate, 'srccity' : 'Singapore', 'destcity' : destination }
        queryResult1 = collection.find(queryCondition1)
        departtrip = sorted(queryResult1, key=lambda k: k['price'])
        if len(departtrip)== 0:
            return []
        return departtrip[0:4]

    def getHotels(self, checkinDate, checkoutDate, destination, db):
        collection = db['hotels']
        #cid = datetime.datetime.strptime(checkinDate, '%Y-%m-%d')
        #cod = datetime.datetime.strptime(checkoutDate, '%Y-%m-%d') + timedelta(days=1)
        queryCondition = { 'date' : { '$gte' : checkinDate, '$lt' : checkoutDate}, 'city' : destination }
        queryResult = collection.find(queryCondition)
        #sortedResult = sorted(queryResult, key=lambda k: k['price'])
        #sortByHotel = sorted(queryResult, key=lambda k: k['hotelName'])
        # Assuming that all hotels will pump out the row everyday


        return queryResult

#print(j)

#print(BaseQuery().getHotels('2023-12-10', '2023-12-16', 'Frankfurt', db))
