import falcon
import jwt
from util.JWTAuth import auth


class MaimaiInfo:
    secret = ''

    def __init__(self, config):
        self.secret = config.jwt_secret

    async def on_post(self, req, resp):
        result = auth(req, resp, self.secret)
        if result is not None:
            # TODO: Give info
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_400
