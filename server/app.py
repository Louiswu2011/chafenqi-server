import falcon.asgi
import uvicorn

from api.alive import Alive
from api.auth import Auth, Register
from config import ServerConfig
from api.maimai.MaimaiInfo import MaimaiInfo

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

if __name__ == "__main__":
    uvicorn.run(app="app:app", host='127.0.0.1')
