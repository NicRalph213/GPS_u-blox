# u-blox 6 EVK-6 GPS class

Basic usage:
- from gps_class import GPS class
- create class object, specifying device baud rate and port (string):
  - gps = GPS(baud = 9600, port = '/dev/ttyACM0')
- run operation
  - gps.get_data()
- call on gps.KEYWORD to retrieve keyword as a string 

- retriveable keywords:
  - latitude, longitude
  - alititude (m)
  - quality index 
  - number of satelites 



Note: 
  - baud rate is constant for u-blox 6 EVK-6
  - port may change
  - console user profile must have sufficient permissions to access serial port
  - focusing on GPGGA GPS fix serial string
    - see http://aprs.gids.nl/nmea/

test_external_gps.py is a simple script to show a live console feed of GPS serial 
this shows the GPGGA GPS fix serial string parsed into relevant GPS class instance variables

