# sql_injection.py

import logging
import sqlite3

# Configure logging
logging.basicConfig(filename='sql_injection_simulation.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def simulate_sql_injection():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
    c.execute("INSERT INTO users VALUES ('admin', 'adminpass')")
    # Simulating SQL Injection
    user_input = "' OR '1'='1"
    c.execute(f"SELECT * FROM users WHERE username = {user_input}")
    result = c.fetchall()
    conn.close()
    logging.info(f"SQL Injection simulation complete. Result: {result}")
    print("SQL Injection simulation complete. Check sql_injection_simulation.log for details.")

if __name__ == '__main__':
    simulate_sql_injection()
