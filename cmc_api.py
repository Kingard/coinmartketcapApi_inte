import requests
from requests import Session
import secret
import json
from pprint import pprint as pp



## API doc: https://coinmarketcap.com/api/documentation/v1/

class CMC:

    def __init__(self,apitoken) -> None:
        self.base_url =  'https://pro-api.coinmarketcap.com'
        self.headers = {
                        'Accepts': 'application/json',
                        'X-CMC_PRO_API_KEY': apitoken,
                        }
        self.session = Session()
        self.session.headers.update(self.headers)

    # getAllcoins returns all tokens listed on cmc till last recorded timestamp
    def getAllcoins(self):
        endPoint = '/v1/cryptocurrency/map'
        url = self.base_url+endPoint
        result = self.session.get(url)
        allCoins = pp(result.json()['data'])
        
        return allCoins
   
    # getLatestQuote returns latest quote price of selected token/coin
    def getLatestQuote(self,symbol):
        endPoint = '/v2/cryptocurrency/quotes/latest'
        url = self.base_url + endPoint
        parameters = {
            'symbol':symbol
        }
        result = self.session.get(url,params=parameters)
        data = result.json()['data']
        #latest_quote = pp(data)
        latest_quote = pp(data[symbol][0]['quote']['USD']['price'])

        return latest_quote

    # getLatestAirdrop returns latest airdops ONGOING, ENDED, UPCOMING
    def getLatestAirdrop(self,status):
        endpoint = '/v1/cryptocurrency/airdrops'
        url = self.base_url+endpoint
        parameters = {
            'status':status.upper()
        }
        r = self.session.get(url=url,params=parameters)
        r = r.json()
        return pp(r)
        




cmc = CMC(secret.api_key)
#print(cmc.getAllcoins())
#print(cmc.getLatestQuote('ETH'))
print(cmc.getLatestAirdrop('ongoing'))
#print(pp(request.json()['data'][-1]))


