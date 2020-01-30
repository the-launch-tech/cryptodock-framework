from abc import ABC, abstractmethod
from cryptodock_api import CryptoDockApi

class CryptoDockFillStorage(ABC) :

    def __init__(self, args) :
        self.type = args.TYPE
        self.open_orders = []
        self.fill_history = []
        self.Api = CryptoDockApi(args)

    def update_open_orders(self, type, order) :
        if type == 'OPENED' :
            self.open_orders.append(order)
        elif type == 'FILLED' :
            self.open_orders.remove(order)


    def get_recent_fills() :
        for order in self.open_orders :
            coinbasepro_fills = self.Api.CoinbasePro.get_fills(order)
            kucoin_fills = self.Api.Kucoin.get_fills(order)
            fills = self.recent_fills + coinbasepro_fills + kucoin_fills
        return fills

    def store(self, fill) :
        self.fill_history.append(fill)
