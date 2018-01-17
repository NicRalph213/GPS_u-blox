#Nic Ralph
#Western Sydney University

#quick live test of GPS, will print values to console  

from gps import GPS

#initalise GPS class object with correct port and baud rate
gps = GPS(baud = 9600, port = "/dev/ttyACM0")

#print untill ctrl-c interupt 
try:
    while True:
        gps.get_data()
        print "BAT: ", gps.time
        print "Latitude (DDD MM.MMM): ", gps.latitude
        print "Longitude (DDD MM.MMM): ", gps.longitude
        print "Elevation (m): ", gps.altitude
        print "Detected Satelites: ", gps.num_sats
        print "Position Quality: ", gps.coord_quality
except KeyboardInterrupt:
    print("End GPS stream")
    pass
