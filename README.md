# Bitstamp WebSocket Client

A Bitstamp synchronous websocket client for Python.

## Usage example

    from bitstamp_wsclient import wsClient

    myclient = wsClient(channels='order_book_btcusd')
    myclient.start()

## Overwriting methods

You could overwrite these three client methods.  

    from bitstamp_wsclient import wsClient
    
    class myClient(wsClient):
        def on_open(self):
            self.url = 'wss://ws.bitstamp.net'
        def on_message(self,msg):
            # Do whatever you want with the message received
            print(msg)
        def on_close(self):
            print("-- ws closed --")
            
    client=myClient(channels='order_book_btcusd')
    client.start()
