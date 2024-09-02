# ddos.py

import logging
import requests
import time

# Configure logging
logging.basicConfig(filename='ddos_simulation.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def simulate_ddos():
    url = 'http://localhost:5000'  # Change to the target URL
    for _ in range(100):  # Simulate 100 requests
        try:
            response = requests.get(url)
            logging.info(f"Request sent, status code: {response.status_code}")
        except requests.RequestException as e:
            logging.error(f"Request failed: {e}")
        time.sleep(1)  # Wait 1 second between requests
    print("DDoS simulation complete. Check ddos_simulation.log for details.")

if __name__ == '__main__':
    simulate_ddos()
