import BitmexAPIConnector
import threading
import time

class Mexbot:
    
    def __init__(self):
        self.ticker = None
        self.symbol = "XBTUSD"
        mexAPIThread = threading.Thread(target=BitmexAPIConnector.run, args=[self])
        mexAPIThread.start()
        # mex = BitmexAPIConnector.run()

    def updateTicker(self, ticker):
        self.ticker = ticker


if __name__ == "__main__":
    print("starting mexbot")
    mexbot = Mexbot()
    while (True):
        print("in ticker loop")
        time.sleep(10)
        print(mexbot.ticker)
