import os

class Config:
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:gomesp2006@localhost/ftvgonzaga"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
