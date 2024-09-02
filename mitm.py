# mitm.py

import logging
from flask import Flask, request

# Configure logging
logging.basicConfig(filename='mitm_simulation.log', level=logging.INFO, format='%(asctime)s - %(message)s')

app = Flask(__name__)

@app.route('/intercept')
def intercept():
    data = request.args.get('data')
    logging.info(f"Intercepted data: {data}")
    return "Data intercepted"

if __name__ == '__main__':
    app.run(port=5000)
