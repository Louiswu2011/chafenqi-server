import falcon
import jwt


def auth(req, resp, secret):
    token = req.auth[7:]

    try:
        decoded = jwt.decode(token, secret, 'HS256')
        return decoded
    except jwt.exceptions.InvalidTokenError:
        # Invalid JWT Token
        resp.text = 'INVALID'
        return None
