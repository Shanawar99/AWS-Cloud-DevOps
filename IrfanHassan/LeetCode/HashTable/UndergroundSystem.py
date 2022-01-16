class UndergroundSystem:
 
    def __init__(self):
        self.rideridtostation = dict() #map of userid to (stationname, starttime)
        self.stationtostation = dict()  ##  (start,end) : (sumsofar, numrides)
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.rideridtostation[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startstation, starttime = self.rideridtostation.pop(id) #removed from dict
        
        total_time = t - starttime
        s2skey = (startstation, stationName)
        sumsofar, numrides = self.stationtostation.get(s2skey, (0, 0) )
        
        sumsofar += total_time
        numrides += 1
        
        self.stationtostation[s2skey] = (sumsofar, numrides) 
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        s2skey = (startStation, endStation)
        sumsofar, numrides = self.stationtostation.get(s2skey)
        
        return sumsofar/numrides