# Bitstamp WebSocket Client
A Bitstamp synchronous websocket client for Python.
# Usage example
  from bitstamp_wsclient import wsClient

  myclient = wsClient(channels='order_book_btcusd')
  myclient.start()
