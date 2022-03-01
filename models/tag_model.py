from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Tag:
    id: Optional[int]
    name: str
    color: str
