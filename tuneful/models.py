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
        song_file_info = session.query(File).filter_by(id =song_file_id).first()
        
        return {
            "id": self.id,
            "file": {
                "id": 7,
                "name": "Shady_Grove.mp3"
                {
        }
        return post
        
class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)
    song = relationship("Song", backref="song", uselist=False)
    
    def as_dictionary(self):
        return {
            "id": self.id,
            "file": {self.filename,
                "id": 7,
                "name": "Shady_Grove.mp3"
                {
        }
        return post