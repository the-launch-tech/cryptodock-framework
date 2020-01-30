class CryptoDockArgs(object) :
    """
    sysargv from the NodeJS parent process.
    Parsing for use in SDK framework
    """

    def __init__(self, system) :
        self.API_HOST = system[1]
        self.API_PORT = system[2]
        self.API_VERSION = system[3]
        self.TRADING_SOCKET_HOST = system[4]
        self.TRADING_SOCKET_PORT = system[5]
        self.TYPE = system[6]
        self.STRATEGY = system[7]

        if self.TYPE == 'backtest' :
            self.LABEL = system[8]
            self.DESCRIPTION = system[9]
            self.FUNDS = system[10]
            self.GRANULARITY = system[11]
            self.START = system[12]
            self.END = system[13]
