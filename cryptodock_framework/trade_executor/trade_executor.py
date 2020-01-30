from abc import ABC, abstractmethod
from collections import deque
from cryptodock_api import CryptoDockApi

class CryptoDockTradeExecutor(ABC) :

    def __init__(self, args) :
        self.order_queue = deque()
        self.type = args.TYPE
        self.cancel_count = 0
        self.Api = CryptoDockApi(args)

    def queue_order(self, order) :
        self.order_queue.appendleft(order)

    def has_order_queued(self) :
        return self.order_queue.count() > 0

    def pop_order(self) :
        return self.order_queue.pop()

    def cancel_order(self, order_id) :
        self.order_queue[order_id]
        self.cancel_count += 1

    @abstractmethod
    def execute(self) : pass
