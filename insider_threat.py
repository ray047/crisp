# insider_threat.py

import logging

# Configure logging
logging.basicConfig(filename='insider_threat_simulation.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def simulate_insider_threat():
    with open('insider_threat_log.txt', 'w') as file:
        file.write('Unauthorized access detected: User=malicious_user')
    logging.info("Insider threat simulation complete: Unauthorized access logged.")
    print("Insider threat simulation complete. Check insider_threat_simulation.log for details.")

if __name__ == '__main__':
    simulate_insider_threat()
