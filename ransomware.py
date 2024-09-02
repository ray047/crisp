# ransomware.py

import logging
import os

# Configure logging
logging.basicConfig(filename='ransomware_simulation.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def simulate_ransomware():
    try:
        with open('ransomware_test_file.txt', 'w') as file:
            file.write('This is a test file for ransomware simulation.')
        os.rename('ransomware_test_file.txt', 'ransomware_test_file.enc')
        logging.info("Ransomware simulation complete: File renamed to 'ransomware_test_file.enc'.")
        print("Ransomware simulation complete. Check ransomware_simulation.log for details.")
    except Exception as e:
        logging.error(f"Error during ransomware simulation: {e}")

if __name__ == '__main__':
    simulate_ransomware()
