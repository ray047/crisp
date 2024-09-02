# data_breach.py

import logging

# Configure logging
logging.basicConfig(filename='data_breach_simulation.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def simulate_data_breach():
    with open('data_breach.txt', 'w') as file:
        file.write('Sensitive data: Username=admin, Password=1234')
    logging.info("Data breach simulation complete: Sensitive data written to 'data_breach.txt'.")
    print("Data breach simulation complete. Check data_breach_simulation.log for details.")

if __name__ == '__main__':
    simulate_data_breach()
