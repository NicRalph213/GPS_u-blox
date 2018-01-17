#Nic Ralph 2018
#Western Sydney University 

#Check presence of serial library and import
try:
    import serial
except:
    print "PySerial library missing"
    exit(1)

class GPS:

    def __init__(self,port,baud):

        #Device Configuration
        # port may need to be changed between devicess
        self.port = port
        self.baud = baud

        self.raw_NMEA_response = None
        self.raw_GPGGA_response = None
        self.parsed_GPGGA_response = None
        self.time = None
        self.latitude = None
        self.longitude = None
        self.altitude = None
        self.coord_quality = None
        self.num_sats = None

    def checksum(self,response_string):
        """
        GPS NMEA response checksum
            originally implemented by 
            :param self: 
            :param response_string: raw NMEA serial output from u-blox
        """

        # all NMEA messages start with $
        if not response_string.startswith("$"): return False

        # additionally, all NMEA messages will prefix checksum integer with an * 
        if not response_string[-3:].startswith("*"): return False

        payload = response_string[1:-3]
        checksum = 0

        for i in range(len(payload)):
            checksum = checksum^ord(payload[i])
    
        return ("%02X" % checksum) == response_string[-2:]

    def parse_GPGGA_code(self,response_string):
        """
        Sort through GPGGA response string for latitude, etc.
        Assigns parsed values to respective class instance variable

            :param self: 
            :param response_string: string list in format:
                GPGGA,BAT,HHMM.MMM,Latitude,N,Longitude,E,FS,NoSV,
                HDOP,msl,m,Altref,m,DiffAge,DiffStation*cs,<CR><LF>

                note: 'm' refers to units metres
                Latitude N expressed in S etc, will naturally vary depending on location
        """
        #store all correct fields in class instance variables
        self.time = response_string[1]
        self.latitude = response_string[2] + " " + response_string[3]
        self.longitude = response_string[4] + " " + response_string[5]
        self.coord_quality = response_string[6]
        self.num_sats = response_string[7]
        self.altitude = response_string[9]

    def parse_NMEA_resp(self,response):
        """
        parsing and preprocessing of entire raw NMEA serial response
        NMEA field of interest is 'GPGGA' - general GPS fix information
            :param self: 
            :param response: raw NMEA serial response from gps
            :param return: string list of GPGGA response
        """
        #clean up and 
        response = response.split("$")
        parsed_NMEA_response = [x for x in response if "GPGGA" in x]
        
        if parsed_NMEA_response:
            parsed_NMEA_response = "".join(parsed_NMEA_response)
            parsed_NMEA_response = parsed_NMEA_response.split(",")

        return parsed_NMEA_response 
        
    def get_data(self):
        """
        main class method
        collect serial data from u-blox and parse for latitude etc.
        operation stores the parsed data in respective instance variables
        
        only interested in GPGGA (gps fix) response!

            :param self: 
        """
        # establish serial connection to specified port and baud rate
        serial_obj = serial.Serial(self.port, self.baud)

        # loop until succesful fix 
        while True:
            # read gps response from serial object and preprocess
            NMEA_recieved_line = serial_obj.readline()
            NMEA_recieved_line = NMEA_recieved_line.strip()

            # assign current raw serial line to instance variable
            self.raw_NMEA_response = NMEA_recieved_line
        
            #regading checksum passed
            if self.checksum(NMEA_recieved_line):
                
                #parse each response for GPGGA gps fix serial line
                NMEA_recieved_line = self.parse_NMEA_resp(NMEA_recieved_line)

                # Check if actually the required GPGGA line 
                if len(NMEA_recieved_line)>0:

                    self.raw_GPGGA_response = NMEA_recieved_line

                    # final parse to store GPGGA response values 
                    #  in respective instance variables
                    self.parse_GPGGA_code(NMEA_recieved_line)

                    # final check of GPGGA quality indicator                  
                    if self.coord_quality == str(1):
                        break
                    else:
                        print("GPS fix unavailable")
            else:
                print('Failed checksum')

        serial_obj.close()
    




