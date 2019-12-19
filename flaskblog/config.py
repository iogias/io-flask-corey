


class Config:
    SECRET_KEY = os.enf.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.enf.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.enf.get('EMAIL_USER')
    MAIL_PASSWORD = os.enf.get('EMAIL_PASS')

