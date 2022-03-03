from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class Task():
    id: Optional[int]
    title: str
    description: Optional[str]
    tag: Optional[str]
    done: bool = field(default=False)
    completed_at: Optional[datetime] = field(init=False, default=None)
    created_at: datetime = field(default=datetime.now())
