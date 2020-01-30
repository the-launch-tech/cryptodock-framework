from abc import ABC
import json
from . import Helpers
from . import Response

class Socket(ABC) :
    """
    Abstracted utilities for SDK framework websocket client.
    """

    @staticmethod
    def URL(host, port, id) :
        return 'ws://{}:{}?id={}'.format(host, port, id)

    @staticmethod
    def PING(id, message) :
        return json.dumps({'command': Response.PING, 'id': id, 'message': message}, default=Helpers.json_serial)

    @staticmethod
    def START_TRADING(id) :
        return json.dumps({'command': Response.START_TRADING, 'id': id}, default=Helpers.json_serial)

    @staticmethod
    def FINISHED_TRADING(id, meta) :
        return json.dumps({'command': Response.FINISHED_TRADING, 'id': id, 'meta': meta}, default=Helpers.json_serial)
