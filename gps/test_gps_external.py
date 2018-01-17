from gps import GPS

gps = GPS(baud = 9600, port = "/dev/ttyACM0")

while True:
    gps.get_data()
    print "BAT: ", gps.time
    print "Latitude (DDD MM.MMM): ", gps.latitude
    print "Longitude (DDD MM.MMM): ", gps.longitude
    print "Elevation (m): ", gps.altitude
    print "Detected Satelites: ", gps.num_sats
    print "Position Quality: ", gps.coord_quality
