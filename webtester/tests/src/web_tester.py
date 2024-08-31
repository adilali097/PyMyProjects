# src/web_tester.py
import requests
import sys

def check_status(url, method='GET', headers=None, data=None):
    try:
        response = requests.request(method, url, headers=headers, data=data)
        print(f"URL: {url}")
        print(f"Method: {method}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {response.elapsed.total_seconds()} seconds")
        print(f"Response Content: {response.text[:200]}")  # Print the first 200 characters of the response content
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python web_tester.py <url> [method] [headers] [data]")
        sys.exit(1)
    
    url = sys.argv[1]
    method = sys.argv[2] if len(sys.argv) > 2 else 'GET'
    headers = None  # Add logic to parse headers if needed
    data = None  # Add logic to parse data if needed
    
    check_status(url, method, headers, data)

if __name__ == "__main__":
    main()
