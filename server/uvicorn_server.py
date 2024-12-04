import time
import webbrowser

from uvicorn import Config, Server
from threading import Thread


class UvicornServer:
    def __init__(self) -> None:
        self.host = "0.0.0.0"


    def set_ip(self, ip: str) -> None:
        self.ip = ip


    def set_port(self, port: int) -> None:
        self.port = port


    def set_app(self, app) -> None:
        self.app = app


    def open_in_browser(self):
        """Open the browser after the server is ready."""
        time.sleep(2)  # Delay to allow the server to start
        webbrowser.open(f"http://{self.ip}:{self.port}")
        

    def run(self):
        """Run the FastAPI app."""
        # Configure Uvicorn server
        config = Config(
            app=self.app,
            host=self.host,
            port=self.port
        )
        server = Server(config)

        # Start the browser-opening thread
        Thread(target=self.open_in_browser, daemon=True).start()

        # Run the Uvicorn server
        server.run()