from flask import Flask
import logging
app = Flask(__name__)
@app.route('/')
def home():
    app.logger.info("This is a sample log statement that exceeds 200 bytes. " * 20)
    return "Check logs for the generated log statement."
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
