import json

import falcon.asgi
import uvicorn

from alive import Alive
from api.auth import Auth, Register


def create_app():
    f = open('config.json')
    data = json.load(f)
    secret = data['jwt_secret']

    alive = Alive()
    auth = Auth(secret)
    register = Register()

    app = falcon.asgi.App()
    app.add_route("/alive", alive)
    app.add_route("/auth", auth)
    app.add_route("/register", register)

    return app


if __name__ == "__main__":
    uvicorn.run(create_app())
