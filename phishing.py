# phishing.py

import logging
import sys

# Configure logging
logging.basicConfig(filename='phishing_simulation.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def simulate_phishing():
    phishing_email = "Congratulations! You've won a prize. Click this link to claim it."
    logging.info(f"Phishing email sent: {phishing_email}")
    print("Phishing simulation complete. Check phishing_simulation.log for details.")

if __name__ == '__main__':
    simulate_phishing()
