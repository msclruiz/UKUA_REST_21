from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, INTEGER, String
db=SQLAlchemy()

class table(db.Model):
    __tablename__='empleados'
    idOpcion=db.empleados 


