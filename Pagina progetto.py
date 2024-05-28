import sys, signal, os
import http.server
import socketserver

# Sets the directory as the subfolder to make impossible a GET request to the site source code
os.chdir('SitoProgetto')

# Retrieves the port number from command line arguments or defaults to 8080.
def get_port():
  if sys.argv[1:]:
      port = int(sys.argv[1])
  else:
      port = 8080
  return port

# Checks for the Ctrl+C command to shut down the server.
def signal_handler(signal, frame):
    print( 'Server shutting down (Ctrl+C pressed)')
    try:
      if(server):
        server.server_close()
    finally:
      sys.exit(0)

# Main server loop
def run():
  try:
    while True:
      server.serve_forever()
  except KeyboardInterrupt:
    pass

port=get_port()

server = socketserver.ThreadingTCPServer(('',port), http.server.SimpleHTTPRequestHandler )

print("Server acceso sulla porta: " + str(port))

# Set server properties
server.daemon_threads = True  
server.allow_reuse_address = True  

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    run()

server.server_close()