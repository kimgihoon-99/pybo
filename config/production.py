from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'd\xb8(\xc0\xbf\xef\xeao\xf8!\xe2\xb8\x81C\xda\xb1'
