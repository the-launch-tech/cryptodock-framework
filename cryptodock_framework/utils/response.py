class Response(object) :
    """
    Events sent from SDK framework to NodeJS parent process via websocket client.
    """

    PING = 'PING'
    SIGNAL_QUEUED = 'SIGNAL_QUEUED'
    ORDER_QUEUED = 'ORDER_QUEUED'
    ORDER_PLACED = 'ORDER_PLACED'
    ORDER_FILLED = 'ORDER_FILLED'
    START_TRADING = 'START_TRADING'
    FINISHED_TRADING = 'FINISHED_TRADING'
