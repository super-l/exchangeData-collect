import zlib

from interface.wss.okex.okcoin_websocket import *


def on_open(self):
    #subscribe okcoin.com spot ticker
    self.send("{'event':'addChannel','channel':'ok_sub_spotusd_btc_ticker','binary':'true'}")

    #subscribe okcoin.com future this_week ticker
    #self.send("{'event':'addChannel','channel':'ok_sub_futureusd_btc_ticker_this_week','binary':'true'}")

    #subscribe okcoin.com future depth
    #self.send("{'event':'addChannel','channel':'ok_sub_futureusd_ltc_depth_next_week_20','binary':'true'}")

    #subscrib real trades for self
    #realtradesMsg = realtrades('ok_sub_spotusd_trades',api_key,secret_key)
    #self.send(realtradesMsg)


    #spot trade via websocket
    #spotTradeMsg = spotTrade('ok_spotusd_trade',api_key,secret_key,'ltc_usd','buy_market','1','')
    #self.send(spotTradeMsg)


    #spot trade cancel
    #spotCancelOrderMsg = spotCancelOrder('ok_spotusd_cancel_order',api_key,secret_key,'btc_usd','125433027')
    #self.send(spotCancelOrderMsg)

    #future trade
    futureTradeMsg = futureTrade(api_key,secret_key,'btc_usd','this_week','','2','1','1','20')
    self.send(futureTradeMsg)

    #future trade cancel
    #futureCancelOrderMsg = futureCancelOrder(api_key,secret_key,'btc_usd','65464','this_week')
    #self.send(futureCancelOrderMsg)

    #subscrbe future trades for self
    #futureRealTradesMsg = futureRealTrades(api_key,secret_key)
    #self.send(futureRealTradesMsg)
def on_message(self,evt):
    data = inflate(evt) #data decompress
    print(data)


def inflate(data):
    decompress = zlib.decompressobj(-zlib.MAX_WBITS)
    inflated = decompress.decompress(data)
    inflated += decompress.flush()
    return inflated

def on_error(self,evt):
    print (evt)

def on_close(self,evt):
    print ('DISCONNECT')


if __name__ == "__main__":
    url = "wss://real.okcoin.com:10440/websocket/okcoinapi"
    #if okcoin.cn  change url wss://real.okcoin.cn:10440/websocket/okcoinapi
    api_key ='your api_key which you apply'
    secret_key = "your secret_key which you apply"

    websocket.enableTrace(False)
    if len(sys.argv) < 2:
        host = url
    else:
        host = sys.argv[1]
    ws = websocket.WebSocketApp(host,
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
