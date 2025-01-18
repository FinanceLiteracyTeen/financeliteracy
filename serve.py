import http.server
import socketserver
import logging

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

class MyTCPServer(socketserver.TCPServer):
    def process_request(self, request, client_address):
        try:
            super().process_request(request, client_address)
        except Exception as e:
            logging.error(f"Error processing request: {e}")

with MyTCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        logging.error(f"Server error: {e}")
    finally:
        httpd.server_close()
