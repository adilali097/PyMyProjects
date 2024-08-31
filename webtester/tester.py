import requests
import ssl
import socket
from urllib.parse import urlparse

def check_http_status(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.RequestException as e:
        return str(e)

def check_ssl_certificate(url):
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname

    if not hostname:
        return "Invalid URL"
    
    context = ssl.create_default_context()
    try:
        with context.wrap_socket(socket.socket(), server_hostname=hostname) as sock:
            sock.connect((hostname, 443))
            cert = sock.getpeercert()
            return cert
    except Exception as e:
        return str(e)
