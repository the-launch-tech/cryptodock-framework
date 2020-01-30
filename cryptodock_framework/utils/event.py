class Event(object) :
    """
    Events sent from NodeJS parent process websocket.
    Handled in the Strategy base class.
    """

    FIND_SIGNAL = 'FIND_SIGNAL'
    BUILD_ORDER = 'BUILD_ORDER'
    EXECUTE_ORDER = 'EXECUTE_ORDER'
    AUDIT_STRATEGY = 'AUDIT_STRATEGY'
    STORE_FILL = 'STORE_FILL'
    FINISHED_TRADING = 'FINISHED_TRADING'
    TRADING_RESOLVED = 'TRADING_RESOLVED'
