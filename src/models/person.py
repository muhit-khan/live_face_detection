# src/models/person.py

from dataclasses import dataclass, field
from typing import List

@dataclass
class FaceEncoding:
    """A numerical representation of a face."""
    encoding: List[float]

@dataclass
class KnownPerson:
    """A person that the system is trained to recognize."""
    name: str
    encodings: List[FaceEncoding] = field(default_factory=list)
