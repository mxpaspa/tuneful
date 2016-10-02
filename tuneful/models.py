import os.path

from flask import url_for
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship

from tuneful import app
from .database import Base, engine

class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True)
    song_file_id = Column(Integer, ForeignKey("files.id", nullable=False)
    
        def as_dictionary(self):
            file = session.query(File).filter_by(id =self.song_file_id).first()
        
        return {
            "id": self.id,
            "file": file.as_dictionary()
        }
        
        
class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)
    song = relationship("Song", backref="song", uselist=False)
    file_name = Column(String, nullable=False)
    
    def as_dictionary(self):
        return {
            "id": self.id,
            "file_name": self.file_name
        }
        