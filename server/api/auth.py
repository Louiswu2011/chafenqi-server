import datetime
import sqlite3
import jwt
from sqlite3 import *
from falcon import *


class Auth:
    secret = ''

    def __init__(self, secret):
        self.secret = secret

    async def on_post(self, req, resp):
        payload = await req.media
        username = payload['username']
        password = payload['password']

        db = connect("user.db")
        cur = db.cursor()

        try:
            cur.execute('select rowid, password, is_premium from user where username=?', [username])
            data = cur.fetchone()
            if data is None:
                resp.text = 'NOT EXIST'
                resp.status = falcon.HTTP_400
            else:
                (rowid, pass_hash, premium) = data
                if password == pass_hash:
                    encoded = jwt.encode({
                        'sub': username,
                        'id': rowid,
                        'premium': premium
                    }, self.secret)
                    resp.text = encoded
                    resp.status = falcon.HTTP_200
                else:
                    resp.text = 'MISMATCH'
                    resp.status = falcon.HTTP_400
        except sqlite3.Error as err:
            print(err)
            resp.text = err.sqlite_errorname
            resp.status = falcon.HTTP_400
        finally:
            cur.close()
            db.close()


class Register:
    async def on_post(self, req, resp):
        payload = await req.media
        username = payload['username']
        password = payload['password']

        db = connect("user.db")
        cur = db.cursor()

        print(username, password)
        try:
            timestamp = int(datetime.datetime.now().timestamp())

            cur.execute('''
            create table if not exists user(
                username unique not null,
                password not null,
                is_premium not null,
                create_time not null
            )
            ''')
            cur.execute('insert into "user" values(?,?,?,?)', [username, password, 0, timestamp])
            db.commit()
            resp.status = falcon.HTTP_200
        except sqlite3.Error as err:
            print(err)
            if err.sqlite_errorcode == 2067:
                # Username not unique
                resp.text = 'NOT UNIQUE'
            resp.status = falcon.HTTP_400
        finally:
            cur.close()
            db.close()
