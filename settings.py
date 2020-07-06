import os

from sayhelllo_whd import app


dev_db = 'sqlite:///' + os.path.join(os.path.join(os.path.dirname(app.root_path),'data.db'))

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLAL