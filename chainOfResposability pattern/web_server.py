from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, nxt):
        self._next = nxt

    def handle(self, request):
        if self.do_handle(request):
            return
        if self._next is not None:
            self._next.handle(request)

    @abstractmethod
    def do_handle(self, request):
        pass


class HttpRequest:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password


class WebServer:
    def __init__(self, handler):
        self._handler = handler

    def handle(self, request):
        self._handler.handle(request)


class Authenticator(Handler):
    def do_handle(self, request):
        is_valid = request.get_username() == "admin" and request.get_password() == "1234"
        print("Authentication")
        return not is_valid


class Encryptor(Handler):
    def __init__(self, nxt):
        super().__init__(nxt)

    def do_handle(self, request):
        print("Encryption")


class Compressor(Handler):

    def __init__(self, nxt):
        super().__init__(nxt)

    def do_handle(self, request):
        print("Compress")
        return False


class Logger(Handler):
    def __init__(self, nxt):
        super().__init__(nxt)

    def do_handle(self, request):
        print("Logged")
        return False


encrypt = Encryptor(None)
compressor = Compressor(encrypt)
logger = Logger(compressor)
authenticator = Authenticator(logger)
server = WebServer(authenticator)

server.handle(HttpRequest("admin", "1234"))
