"""
Серверное приложение для соединений
"""
import asyncio
from asyncio import transports


class ClientProtocol(asyncio.Protocol):
    login: str
    server: 'Server'
    transport: transports.Transport

    def __init__(self, server: 'Server'):
        self.server = server
        self.login = None

    def data_received(self, data: bytes):
        decoded = data.decode()
        print(decoded)

        if self.login is None:
            # login:User
            if decoded.startswith("login:"):
                self.login = decoded.replace("login:", "").replace("\r\n", "")
                if self.login not in self.server.users:
                    self.server.users.append(self.login)
                    self.transport.write(
                        f"Привет, {self.login}!\n".encode()
                    )
                    self.send_history()
                else:
                    self.transport.write(
                        f"Логин {self.login} занят, попробуйте другой".encode()
                    )
                    self.login = None
                    self.transport.abort()
        else:
            self.send_message(decoded)

    def send_history(self):
        print(self.server.history)
        for message in self.server.history:
            self.transport.write(
                f"{message}\n".encode()
            )

    def send_message(self, message):
        format_string = f"<{self.login}>: {message}"
        encoded = format_string.encode()

        for client in self.server.clients:
            if client.login != self.login:
                client.transport.write(encoded)
        if len(self.server.history) < 10:
            self.server.history.append(format_string)
        else:
            old = self.server.history.pop(0)
            self.server.history.append(format_string)

    def connection_made(self, transport: transports.Transport):
        self.transport = transport
        self.server.clients.append(self)
        print("Соединение установлено")

    def connection_lost(self, exception):
        self.server.clients.remove(self)
        print(f"Соединение разорвано")


class Server:
    clients: list

    def __init__(self):
        self.clients = []
        self.users = []
        self.history = []

    def create_protocol(self):
        return ClientProtocol(self)

    async def start(self):
        loop = asyncio.get_running_loop()

        coroutine = await loop.create_server(
            self.create_protocol,
            "127.0.0.1",
            8888
        )

        print("Сервер запущен ...")

        await coroutine.serve_forever()


process = Server()
try:
    asyncio.run(process.start())
except KeyboardInterrupt:
    print("Сервер остановлен вручную")
