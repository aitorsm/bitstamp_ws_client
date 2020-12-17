from bitstamp_wsclient import wsClient

myclient = wsClient(channels='order_book_btcusd')
myclient.start()
