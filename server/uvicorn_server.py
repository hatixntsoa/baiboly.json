import time
import webbrowser

from uvicorn import Config, Server
from threading import Thread

from typing import Any


class UvicornServer:
    def __init__(self) -> None:
        self._ip: str = "127.0.0.1"
        self._host: str = "0.0.0.0"
        self._port: int = 8000
        self._app: Any = None


    def set_ip(self, ip: str) -> "UvicornServer":
        self._ip = ip
        return self


    def set_port(self, port: int) -> "UvicornServer":
        self._port = port
        return self


    def set_app(self, app: Any) -> "UvicornServer":
        self._app = app
        return self


    def open_in_browser(self):
        """Open the browser after the server is ready."""
        time.sleep(2)  # Delay to allow the server to start
        webbrowser.open(f"http://{self._ip}:{self._port}")
        

    def run(self):
        """Run the FastAPI app."""
        # Configure Uvicorn server
        config = Config(
            app=self._app,
            host=self._host,
            port=self._port
        )
        server = Server(config)

        # Start the browser-opening thread
        Thread(target=self.open_in_browser, daemon=True).start()

        # Run the Uvicorn server
        server.run()