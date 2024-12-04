from api.baiboly import BaibolyAPI
from server.uvicorn_server import UvicornServer


def main() -> None:
    server = UvicornServer()
  
    server.set_ip("localhost")
    server.set_port(8000)
    
    server.set_app(BaibolyAPI().get_api())
    server.run()


if __name__ == "__main__":
    main()