import datetime
from . import Helpers

class Meta :
    """
    Track Meta Data:
        # cycles <int>                                    Number of heartbeat cycles
        # start_time <datetime>                           Start time of session
        # end_time <datetime>                             End time of session
        # start_funds (USD) <float>                       Starting amount in USD
        current_funds (USD) <float>                        Ending amount in USD
        change_percentage <float>                       Percent change in funds
        avg_time_between_orders (Seconds) <float>       Average seconds between order placements
        avg_order_size (USD) <float>                    Average size of order in USD
        avg_fill_size (USD) <float>                     Average size of filled order in USD
        # signal_count <int>                              Number of signals raised in session
        # order_count <int>                               Number of orders opened in session
        # cancel_count <int>                           Number of cancelled orders in session
        # fill_count <int>                                Number of filled orders in session
        side_ratio (-1/1) <float>                       Ratio of buy/sell orders
        avg_fee (USD) <float>                           Average fee per order fill
        order_type_ratio (-1/1) <float>                 Ratio of limit/market orders
        product_distribution <object>                   Breakdown of products acted upon in session
        exchange_distribution <object>                  Breakdown of exchanges acted upon in session
    """

    def __init__(self, args) :
        self.args = args
        self.cycles = 0
        self.current_duration = 0
        self.granularity = 10
        self.current_funds = 0
        self.change_cycle_spread = 10
        self.change_over_time = []
        self.signal_count = 0
        self.order_count = 0
        self.fill_count = 0
        self.cancel_count = 0

    def return_event_meta(self) :
        """
        Return meta data for each event where an action takes place
        """

        return {
            'cycles': self.cycles,
            'current_duration': self.current_duration,
            'start_funds': self.start_funds,
            'current_funds': self.current_funds,
            'change': self.change,
            'avg_time_between_orders': self.avg_time_between_orders,
            'avg_order_size': self.avg_order_size,
            'avg_fill_size': self.avg_fill_size,
            'signal_count': self.signal_count,
            'order_count': self.order_count,
            'cancel_count': self.cancel_count,
            'fill_count': self.fill_count,
            'buy_percentage': Helpers.calc_percentage(self.order_sides.count('SELL'), self.order_sides.count('BUY'), 2),
            'sell_percentage': Helpers.calc_percentage(self.order_sides.count('BUY'), self.order_sides.count('SELL'), 2),
            'market_type_percentage': Helpers.calc_percentage(self.order_types.count('MARKET'), self.order_types.count('LIMIT'), 2),
            'limit_type_percentage': Helpers.calc_percentage(self.order_types.count('LIMIT'), self.order_types.count('MARKET'), 2),
            'avg_fee': self.avg_fee
        }

    def return_meta(self) :
        """
        Return meta data at the end of the session
        """

        return {
            'cycles': self.cycles,
            'current_duration': self.current_duration,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'start_funds': self.start_funds,
            'current_funds': self.current_funds,
            'change': self.change,
            'change_over_time': self.change_over_time,
            'avg_time_between_orders': self.avg_time_between_orders,
            'avg_order_size': self.avg_order_size,
            'avg_fill_size': self.avg_fill_size,
            'signal_count': self.signal_count,
            'order_count': self.order_count,
            'cancel_count': self.cancel_count,
            'fill_count': self.fill_count,
            'buy_percentage': Helpers.calc_percentage(self.order_sides.count('SELL'), self.order_sides.count('BUY'), 2),
            'sell_percentage': Helpers.calc_percentage(self.order_sides.count('BUY'), self.order_sides.count('SELL'), 2),
            'market_type_percentage': Helpers.calc_percentage(self.order_types.count('MARKET'), self.order_types.count('LIMIT'), 2),
            'limit_type_percentage': Helpers.calc_percentage(self.order_types.count('LIMIT'), self.order_types.count('MARKET'), 2),
            'avg_fee': self.avg_fee,
            'product_distribution': self.product_distribution,
            'exchange_distribution': self.exchange_distribution
        }

    def increment_cycles(self) :
        self.cycles += 1

    def increment_duration(self) :
        self.current_duration = self.cycles * self.granularity

    def set_start_time(self) :
        self.start_time = datetime.datetime.now()

    def set_end_time(self) :
        self.end_time = datetime.datetime.now()

    def set_start_funds(self, funds_usd) :
        self.start_funds = funds_usd

    def set_current_funds(self, current_funds_usd) :
        self.current_funds = current_funds_usd

    def set_change(self) :
        self.change = (
            self.start_funds,
            self.current_funds,
            self.start_funds - self.current_funds,
            round(self.start_funds / self.current_funds, 8)
        )

    def append_change_over_time(self, current_funds_usd) :
        if self.cycles % self.change_cycle_spread == 1 :
            self.change_over_time.append(
                (
                    self.current_duration,
                    self.current_funds,
                    current_funds_usd,
                    self.current_funds - current_funds_usd,
                    round(self.current_funds / current_funds_usd, 8)
                )
            )
            self.current_funds = current_funds_usd

    def update_avg_order_time_spread(self, time) :
        self.avg_time_between_orders = Helpers.update_avg(self.avg_time_between_orders, self.order_count, time, 8)

    def update_avg_order_size(self, order_size_usd) :
        self.avg_order_size = Helpers.update_avg(self.avg_order_size, self.order_count, order_size_usd, 8)

    def update_avg_fill_size(self, fill_size_usd) :
        self.avg_fill_size = Helpers.update_avg(self.avg_fill_size, self.fill_count, fill_size_usd, 8)

    def update_avg_fee(self, last_fee_usd) :
        self.avg_fee = Helpers.update_avg(self.avg_fee, self.fill_count, last_fee_usd, 8)

    def update_signal_count(self) :
        self.signal_count += 1

    def update_order_count(self) :
        self.order_count += 1

    def update_fill_count(self) :
        self.fill_count += 1

    def get_cancel_count(self, cancel_count) :
        self.cancel_count = cancel_count

    def update_side_ratio(self, side) :
        self.order_sides.append(side)

    def update_order_type_ratio(self, order_type) :
        self.order_types.append(side)

    def update_product_distrubution(self, product) :
        if self.product_distribution[product['pair']] :
            self.product_distribution[product['pair']]['cycles'].append(self.cycles)
        else :
            self.product_distribution[product['pair']] = {
                'id': product['id'],
                'pair': product['pair'],
                'cycles': [self.cycles]
            }

    def update_exchange_distribution(self, exchange) :
        if self.exchange_distribution[exchange['name']] :
            self.exchange_distribution[exchange['name']]['cycles'].append(self.cycles)
        else :
            self.exchange_distribution[exchange['name']] = {
                'id': exchange['id'],
                'name': exchange['name'],
                'cycles': [self.cycles]
            }
