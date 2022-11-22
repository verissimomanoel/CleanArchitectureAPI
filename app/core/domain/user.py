# ----------------------------------------------------------------------------------------------------------------------
#   This is a free software.
# ----------------------------------------------------------------------------------------------------------------------
"""
This is a module for entities class
"""
import dataclasses
from typing import Optional


@dataclasses.dataclass
class User:
    id: Optional[int]
    email: str
    password: str
    is_active: Optional[bool]

    @classmethod
    def from_dict(self, d):
        return self(**d)

    def to_dict(self):
        return dataclasses.asdict(self)