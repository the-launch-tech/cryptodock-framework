class CryptoDockBacktest :

    def __init__(self, strategy, args, data_handler, portfolio_manager, trade_executor, fill_storage) :
        self.strategy = strategy(
            args=args,
            data_handler=data_handler,
            portfolio_manager=portfolio_manager,
            trade_executor=trade_executor,
            fill_storage=fill_storage
        )

        self.args = args

    def start_test(self) :
        self.strategy.listen()

    def get_results(self) :
        pass
