import pandas as pd
import time
import requests
import telegram
from datetime import datetime
import calendar
from binance.client import Client
import datetime as dt
import numpy



#Jeff Bezos Warret +084329901134
chat_id = '-1001720823065'
api_token = '6552511028:AAFOWc_1Z5NqvdmDtPjCZJ9hp_r-R2aOXSw'
bot = telegram.Bot(token='6552511028:AAFOWc_1Z5NqvdmDtPjCZJ9hp_r-R2aOXSw')

apiURL = f'https://api.telegram.org/bot{api_token}/sendMessage'

# for a in all:

symbols = ['AAVEUSDT',
 'ACHUSDT', 'ADABUSD', 'ADAUSDT', 'AGIXBUSD', 'AGIXUSDT', 'AGLDUSDT', 'ALGOUSDT', 'ALICEUSDT', 'ALPHAUSDT', 'AMBBUSD', 'AMBUSDT', 'ANKRUSDT',
 'ANTUSDT', 'APEBUSD', 'APEUSDT', 'API3USDT', 'APTBUSD', 'APTUSDT', 'ARBUSDT', 'ARKMUSDT', 'ARPAUSDT', 'ARUSDT', 'ASTRUSDT', 'ATAUSDT', 'ATOMUSDT', 'AUCTIONBUSD',
 'AUDIOUSDT', 'AVAXBUSD', 'AVAXUSDT', 'AXSUSDT', 'BAKEUSDT', 'BALUSDT', 'BANDUSDT', 'BATUSDT', 'BCHUSDT', 'BELUSDT','BNBUSDT', 'BNXUSDT', 'BTCUSDT', 'BTSUSDT', 'C98USDT', 'CELOUSDT', 'CELRUSDT', 'CFXUSDT',
 'CHRUSDT', 'CHZUSDT', 'CKBUSDT','COMBOUSDT', 'COMPUSDT', 'COTIUSDT', 'CRVUSDT', 'CTKUSDT', 'CTSIUSDT', 'CVCUSDT', 'CVXBUSD', 'CVXUSDT', 'DARUSDT',
  'DASHUSDT', 'DENTUSDT', 'DGBUSDT', 'DODOBUSD', 'DOGEBUSD', 'DOGEUSDT', 'DOTBUSD', 'DOTUSDT', 'DUSKUSDT', 'DYDXUSDT', 'EDUUSDT', 'EGLDUSDT', 'ENJUSDT',
  'ENSUSDT', 'EOSUSDT', 'ETCBUSD', 'ETCUSDT', 'ETHBTC', 'ETHBUSD', 'ETHUSDT', 'FETUSDT', 'FILBUSD', 'FILUSDT', 'FLMUSDT', 'FLOWUSDT','FTMBUSD', 'FTMUSDT','FXSUSDT', 'GALABUSD', 'GALAUSDT', 'GALBUSD', 'GALUSDT', 'GMTBUSD', 'GMTUSDT', 'GMXUSDT', 'GRTUSDT', 'GTCUSDT', 'HBARUSDT',
  'HFTUSDT', 'HIGHUSDT', 'HOOKUSDT', 'HOTUSDT', 'ICPUSDT', 'ICXUSDT', 'IDEXUSDT', 'IDUSDT', 'IMXUSDT', 'INJUSDT', 'IOSTUSDT', 'IOTAUSDT', 'IOTXUSDT', 'JASMYUSDT',
  'JOEUSDT', 'KAVAUSDT', 'KEYUSDT', 'KLAYUSDT', 'KNCUSDT', 'KSMUSDT', 'LDOBUSD', 'LDOUSDT', 'LEVERBUSD', 'LEVERUSDT', 'LINAUSDT', 'LINKBUSD', 'LINKUSDT', 'LITUSDT', 'LPTUSDT',
  'LQTYUSDT', 'LRCUSDT', 'LTCBUSD', 'LTCUSDT', 'MAGICUSDT', 'MANAUSDT', 'MASKUSDT', 'MATICBUSD', 'MATICUSDT', 'MAVUSDT', 'MDTUSDT', 'MINAUSDT', 'MKRUSDT', 'MTLUSDT',
  'NEARBUSD', 'NEARUSDT', 'NEOUSDT', 'NKNUSDT', 'NMRUSDT', 'OCEANUSDT', 'OGNUSDT', 'OMGUSDT', 'ONEUSDT', 'ONTUSDT', 'OPUSDT', 'PENDLEUSDT', 'PEOPLEUSDT', 'PERPUSDT', 'PHBBUSD',
   'PHBUSDT', 'QNTUSDT', 'QTUMUSDT', 'RADUSDT', 'RAYUSDT', 'RDNTUSDT', 'REEFUSDT', 'RENUSDT', 'RLCUSDT', 'RNDRUSDT', 'ROSEUSDT', 'RSRUSDT', 'RUNEUSDT', 'RVNUSDT', 'SANDBUSD',
   'SANDUSDT', 'SCUSDT', 'SFPUSDT', 'SKLUSDT', 'SNXUSDT', 'SOLBUSD', 'SOLUSDT', 'SPELLUSDT','SSVUSDT', 'STGUSDT', 'STMXUSDT', 'STORJUSDT', 'STXUSDT', 'SUIUSDT',
    'SUSHIUSDT', 'SXPUSDT', 'THETAUSDT', 'TLMBUSD', 'TLMUSDT', 'TOMOUSDT', 'TRBUSDT', 'TRUUSDT', 'TRXBUSD', 'TRXUSDT', 'TUSDT', 'UMAUSDT', 'UNFIUSDT', 'UNIBUSD', 'UNIUSDT',
     'USDCUSDT', 'VETUSDT', 'WAVESBUSD', 'WAVESUSDT', 'WLDUSDT', 'WOOUSDT', 'XEMUSDT', 'XLMUSDT', 'XMRUSDT', 'XRPBUSD', 'XRPUSDT', 'XTZUSDT', 'XVGUSDT', 'XVSUSDT', 'YFIUSDT',
     'ZECUSDT', 'ZENUSDT', 'ZILUSDT', 'ZRXUSDT']


symbol_rsi_up_70 = []
symbol_rsi_down_30 = []
symbol_rsi_can_push_up_70 = []
symbol_rsi_can_push_down_70 = []
symbol_rsi_can_push_up_30 = []
symbol_rsi_can_push_down_30 = []

# Info for bollinger band
api_key = 'ZYwNM5VCQ24pAzNsFmL7yynws9P8cdYHcJx8oRyPKiiymvYoh2zCHymbMT7Ds6LM'
api_key_secret = 'tUrsBoqDmAIs9PRTKlBPLctxfWCeYybepOhC3Tm44NfxWPEXF5skPjiKfDA9IUGQ'

client = Client(api_key, api_key_secret)

    # ticker of product
symbol_trade = 'OGNUSDT'

    # order quanity ( more than 10 USDT )
orderquantity = 22

    # bollingerband length and width
length = 20
width = 2

#fuction calculator RSI signal
def get_rsi(_symbol):
    timeinterval = 15

    now = datetime.utcnow()
    unixtime = calendar.timegm(now.utctimetuple())
    since = unixtime
    start=str(since-60*60*10)


    url = 'https://fapi.binance.com/fapi/v1/klines?symbol=' + symbol + '&interval='+str(timeinterval)+'m'+'&limit=100'
    data = requests.get(url).json()
    # print(data)



    D = pd.DataFrame(data)
    # print(D)
    D.columns = ['open_time', 'open','high','low','close','volume','close_time','qav','num_trades',
                    'taker_base_vol','taker_quote_vol','is_best_match']

    period = 14
    df=D
    df['close'] = df['close'].astype(float)
    df2=df['close'].to_numpy()


    df2 = pd.DataFrame(df2, columns=['close'])
    delta = df2.diff()


    up,down = delta.copy(), delta.copy()
    up[up < 0 ] = 0
    down[down > 0] = 0


    _gain = up.ewm(com=(period - 1), min_periods=period).mean()
    _loss = down.abs().ewm(com=(period - 1), min_periods=period).mean()


    RS = _gain/_loss


    rsi=100 - (100/(1+RS))
    rsi=rsi['close'].iloc[-1]
    rsi=round(rsi,1)

    return rsi




# Fuction get bollinger band
def get_bollinger_band(symbol, width, intervalunit, length):

        if intervalunit == '1T':
            start_str = '100 minutes ago UTC'
            interval_data = '1m'

            dat = client.get_historical_klines(symbol=symbol,start_str=start_str, interval=interval_data)
            # print(dat)

            D = pd.DataFrame(dat
                # client.get_historical_klines(symbol=symbol,start_str=start_str, interval=interval_data)
            )

            # print(D)

            D.columns = ['open_time', 'open','high','low','close','volume','close_time','qav','num_trades',
                    'taker_base_vol','taker_quote_vol','is_best_match']

            D['open_date_time'] = [dt.datetime.fromtimestamp(x/1000) for x in D.open_time]
            D['symbol'] = symbol
            D = D[['symbol','open_date_time','open','high','low','close','volume','num_trades','taker_quote_vol','is_best_match']]

        df = D.set_index("open_date_time")

        df['close'] = df['close'].astype(float)

        df = df['close']

        df1 = df.resample(intervalunit).agg({
            "close": "last"
        })

        unit = width
        band1 = unit * numpy.std(df1['close'][len(df1) - length:len(df1)])
        bb_center = numpy.mean(df1['close'][len(df1) - length:len(df1)])
        band_high = bb_center + band1
        band_low = bb_center - band1
        return band_high, bb_center, band_low,



ii = 1

while True:

    ii = ii + 1

    print(ii)

    for symbol in symbols:

        rsi = get_rsi(symbol)

        print(symbol)

        # print(rsi)

        bb_1m = get_bollinger_band(symbol, width, '1T', length)

        #print('1 minute upper center lower: ', bb_1m)

        marketprice = 'https://api.binance.com/api/v1/ticker/24hr?symbol=' + symbol
        res = requests.get(marketprice)
        data = res.json()
        lastprice = float(data['lastPrice'])
        price_message = str(lastprice)

        try:
            if lastprice > bb_1m[0] and rsi > 70:
             #if rsi < 70:
                #print('Okeeey ne')
                #text_70 = 'Binance Futures\n +  Recommendation: Sell \n Ticker:  +' + symbol + '\n Last Price: ' + lastprice + '\nRSI: ' + str(rsi) + '\n Good Luck!'
                #try:
                text_70 = '!!! Binance Futures\n' + '\n Recommendation: Sell' + ' \n Symbol: ' + symbol + '\n Price: ' + price_message +'\n RSI: ' +  str(rsi) + '\n Good luck!'
                #print(rsi)
                response = requests.post(apiURL, json={'chat_id': chat_id, 'text': text_70})
                #print(text_70)
                #except Exception as e:
#                    print(e)
                # client.order_market_sell(symbol=symbol_trade, quantity = orderquantity)
               # break
            #the loop stops if the order is made
        except:
            pass

        try:
            if lastprice < bb_1m[2] and rsi < 30:
            #if rsi < 70:
                #text_30 = 'Binance Futures \n + Recommendation: Sell \n Ticker:  \n +' + symbol + '\n Last Price:  ' + lastprice + '\n RSI: ' + str(rsi) + '\n Good Luck!'
                text_30 = 'Binance Futures \n' +'\n Recommendation: Buy' + ' \n Symbol: ' + symbol + '\n Price: ' + '\n RSI: ' + str(rsi) + '\n Good luck!'
                try:
                    response = requests.post(apiURL, json={'chat_id': chat_id, 'text': text_30})
                        # print(response.text)                    
                except Exception as e:
                    print(e)
                # client.order_market_buy(symbol = symbol_trade, quantity = orderquantity)
                break
            # the loop stops if the order is made
        except:
            pass
    time.sleep(15)                                                                                                                                                 