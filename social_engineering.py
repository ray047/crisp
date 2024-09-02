# social_engineering.py

import logging

# Configure logging
logging.basicConfig(filename='social_engineering_simulation.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def simulate_social_engineering():
    deceptive_message = "Hi, I’m from IT support. Please provide your password for a quick verification."
    logging.info(f"Social engineering message sent: {deceptive_message}")
    print("Social engineering simulation complete. Check social_engineering_simulation.log for details.")

if __name__ == '__main__':
    simulate_social_engineering()
