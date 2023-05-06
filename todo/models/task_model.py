from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime

@dataclass
class Task():
    id: Optional[int]
    title: str
    description: Optional[str]
    tag: Optional[str]
    done: bool = field(default=False)
    created_at: datetime = field(default=datetime.now())
    completed_at: Optional[datetime] = field(default=None)
