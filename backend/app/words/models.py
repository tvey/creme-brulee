import enum

from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    Enum
)
from sqlalchemy.orm import relationship

from app.database import Base


class Difficulty(enum.Enum):
    easy = 0
    medium = 1
    hard = 2
    extreme = 3


class PartOfSpeech(Base):
    __tablename__ = 'parts_of_speech'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f'PartOfSpeech(name={self.name})'


class Word(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String, nullable=False, unique=True)
    part_of_speech_id = Column(Integer, ForeignKey('parts_of_speech.id'))
    difficulty = Column(Enum(Difficulty))
    stressed_letter_idx = Column(Integer)

    def __repr__(self):
        return f'Word(content={self.content})'
