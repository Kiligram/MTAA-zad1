# developed by Andrii Rybak in python 3.9
import socketserver
import time
import logging
import sipfullproxy

# set ip address and port of SIP proxy
HOST, PORT = '10.10.39.24', 5060

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log', level=logging.INFO,
                        datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    logging.info(HOST)
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (HOST, PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (HOST, PORT)
    server = socketserver.UDPServer((HOST, PORT), sipfullproxy.UDPHandler)
    server.serve_forever()


