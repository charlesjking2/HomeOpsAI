from pydantic import BaseModel
from typing import List, Optional


class FamilyMember(BaseModel):
    name: str
    age: int
    role: str
    likes: List[str] = []
    dislikes: List[str] = []
    notes: Optional[str] = None


class Family(BaseModel):
    members: List[FamilyMember]

    @property
    def size(self):
        return len(self.members)
