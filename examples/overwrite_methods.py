from bitstamp_wsclient import wsClient

## OVERWRITE SOME METHODS

class myClient(wsClient):
    def on_open(self):
        self.url = 'wss://ws.bitstamp.net'
    def on_message(self,msg):
        # Do whatever with the message received
        print(msg)
    def on_close(self):
        print("-- ws closed --")

## START

client=myClient(channels='order_book_btcusd')
client.start()
