#Nic Ralph
#Western Sydney University
#Quick live test of GPS, will print values to console  

from lib.gps_class import GPS

#initalise GPS class object with correct port and baud rate
gps = GPS(baud = 9600, port = "/dev/ttyACM0")

#print until ctrl-c interupt 
try:
    while True:
        #parse GPS serial response to relevant class instance variables
        gps.get_data()

        print "BAT: ", gps.time
        print "Latitude (DDD MM.MMM): ", gps.latitude
        print "Longitude (DDD MM.MMM): ", gps.longitude
        print "Elevation (m): ", gps.altitude
        print "Detected Satellites: ", gps.num_sats
        print "Position Quality: ", gps.coord_quality

except KeyboardInterrupt:
    print("End GPS stream")
    pass
