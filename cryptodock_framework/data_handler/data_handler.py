from abc import ABC, abstractmethod

class CryptoDockDataHandler(ABC) :

    def __init__(self, args) :
        self.type = args.TYPE
        self.datas = []
        self.signals = []

    def get_data(self, time) :
        if self.type == 'live' :
            return self.get_live_data(time)
        elif self.type == 'backtest' :
            return self.get_backtest_data(time)

    @abstractmethod
    def find_signal(self) : pass

    @abstractmethod
    def get_live_data(self) : pass

    @abstractmethod
    def get_backtest_data(self) : pass
