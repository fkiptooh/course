import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or b'S\x95\xfaY\xdb\xc3\x07C\x1bn2:\xf6\xa2\xb2j'

    MONGODB_SETTINGS = { 'db': 'UTA_Enrollment'
        # 'host': 'mongodb://localhost:27017/UTA_Enrollment'
    }