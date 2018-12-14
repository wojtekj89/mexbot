import BitmexTicker
import threading
import time
import logging
import requests


class Mexbot():
    # Main class of application. Starting all threads, storing data and routing all events

    def __init__(self):
        self.logger = setup_logger()
        self.logger.info("Starting Mexbot")
        self.symbol = "XBTUSD"
        self.ticker = None
        self.mexbotTicker = threading.Thread(
            target=BitmexTicker.run, args=[self])
        self.mexbotTicker.start()
        # # Prepare HTTPS session
        # self.session = requests.Session()
        # # These headers are always sent
        # self.session.headers.update({'user-agent': 'mexbot-' + constants.VERSION})
        # self.session.headers.update({'content-type': 'application/json'})
        # self.session.headers.update({'accept': 'application/json'})

    def updateTicker(self, ticker):
        self.ticker = ticker


def setup_logger():
    # Prints logger info to terminal
    logger = logging.getLogger()
    # Change this to DEBUG if you want a lot more info
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


if __name__ == "__main__":
    mexbot = Mexbot()
    while (True):
        time.sleep(5)
        mexbot.logger.info(mexbot.ticker)
