import falcon


class Alive:
    async def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
