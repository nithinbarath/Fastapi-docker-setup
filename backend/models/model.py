from sqlalchemy import Column , Integer , String
from application import Base



class ModelsTable(Base):

    __tablename__ = "modelstable"

    id = Column ( Integer , primary_key = True , index = True )
    subject = Column(String)
    

