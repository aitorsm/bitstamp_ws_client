import websocket
import json
from threading import Thread
import time


# Channel options: ['live_trades_[currency_pair]', 'live_orders_[currency_pair]', 'order_book_[currency_pair]', 'detail_order_book_[currency_pair]', 'diff_order_book_[currency_pair]']

class wsClient(object):
    def __init__(self,channels,url='wss://ws.bitstamp.net'):
        self.url = url
        self.channels = channels
        self.ws=None
        self.thread=None

        
    def _connect(self):
        if self.channels is None:
            self.channels = ['order_book_btcusd']
        params = {'event': 'bts:subscribe','data': {'channel': self.channels}}
        self.ws = websocket.create_connection(self.url)
        self.ws.send(json.dumps(params))
        
    def start(self):
        def _go():
            self._connect()
            self._listen()
            self._disconnect()

        self.stop = False
        self.on_open()
        self.thread = Thread(target=_go)
        self.keepalive = Thread(target=self._keepalive)
        self.thread.start()

    def _keepalive(self, interval=30):
        while self.ws.connected:
            self.ws.ping("keepalive")
            time.sleep(interval)

    def _listen(self):
        self.keepalive.start()
        while not self.stop:
            try:
                data = self.ws.recv()
                msg = json.loads(data)
            except ValueError as e:
                self.on_error(e)
            except Exception as e:
                self.on_error(e)
            else:
                self.on_message(msg)
                
    def _disconnect(self):
        try:
            if self.ws:
                self.ws.close()
        except websocket.WebSocketConnectionClosedException as e:
            pass
        finally:
            self.keepalive.join()
            
    def on_open(self):
        print('-- WebSocket Opened --')        

    def on_close(self):        
        print("\n-- WebSocket Closed --")

    def on_message(self, data):        
        print(data)

    def on_error(self,msg):
        print(msg)
