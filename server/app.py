import falcon.asgi
import uvicorn

from server.api.alive import Alive
from server.api.auth import Auth, Register
from server.config import ServerConfig
from server.api.maimai.MaimaiInfo import MaimaiInfo


def create_app():
    config = ServerConfig()

    alive = Alive()
    auth = Auth(config)
    register = Register()

    maiInfo = MaimaiInfo(config)

    app = falcon.asgi.App()
    app.add_route("/alive", alive)

    app.add_route("/auth", auth)
    app.add_route("/register", register)

    app.add_route("/maimai/info", maiInfo)

    return app


if __name__ == "__main__":
    uvicorn.run(create_app(), host='127.0.0.1')
