from abc import ABC, abstractmethod
from collections import deque
from cryptodock_api import CryptoDockApi

class CryptoDockPortfolioManager(ABC) :

    def __init__(self, args) :
        self.signal_queue = deque()
        self.args = args
        self.open = []
        self.coinbasepro = []
        self.kucoin = []
        self.Api = CryptoDockApi(args)
        self.populate()

    def populate(self) :
        if self.args.type == 'live' :
            self.populate_live_portfolio()
        elif self.args.type == 'backtest' :
            self.populate_backtest_portfolio()

    def populate_live_portfolio(self) :
        self.coinbasepro = self.Api.CoinbasePro.get_accounts()
        self.kucoin = self.Api.Kucoin.get_accounts()

    def populate_backtest_portfolio(self) :

        def get_coinbasepro_starting(funds) :
            product = self.Api.Local.get_products(exchanges='coinbasepro',pair='BTC-USDC',limit=1)
            tick = self.Api.Local.get_ticker(exchanges='coinbasepro',pair='BTC-USDC',limit=1)
            coinbasepro_start = round(funds / tick[-1]['price'], len(product[-1]['base_min']) - 2)
            self.coinbasepro [
                {
                    "id": "71452118-efc7-4cc4-8780-a5e22d4baa53",
                    "currency": "BTC",
                    "balance": coinbasepro_start,
                    "available": coinbasepro_start,
                    "hold": 0,
                    "profile_id": "75da88c5-05bf-4f54-bc85-5c775bd68254"
                }
            ]

        def get_kucoin_starting(funds) :
            product = self.Api.Local.get_products(exchanges='kucoin',pair='BTC-USDC',limit=1)
            tick = self.Api.Local.get_ticker(exchanges='kucoin',pair='BTC-USDC',limit=1)
            kucoin_start = round(funds / tick[-1]['price'], len(product[-1]['base_min']) - 2)
            self.kucoin = [
                {
                    "id": "5bd6e9216d99522a52e458d6",
                    "currency": "BTC",
                    "type": "trade",
                    "balance": kucoin_start,
                    "available": kucoin_start,
                    "holds": 0
                }
            ]

        get_coinbasepro_starting(self.args.FUNDS)
        get_kucoin_starting(self.args.FUNDS)

    def queue_signal(self, signal) :
        self.signal_queue.appendleft(signal)

    def has_signal_queued(self) :
        return self.signal_queue.count() > 0

    def pop_signal(self) :
        return self.signal_queue.pop()

    @abstractmethod
    def build_order_constraints(self, signal) :
        """
        Params: <object> (signal from data handler) {
            'pair': 'BTC-USDT',
            'exchange': 'coinbasepro',
            'time': time,
            'direction': 'LONG',
            'weight': 0.3
        }

        Return: <object> (order for trade executor) {
            'order_type'
            'side'
            'size_min'
            'size_max'
            'base'
            'quote'
            'stp'
            'stop'
            'stop_price'
            'stop_time'
        }
        """
