from pydantic import BaseModel
from typing import List

class Grid(BaseModel):
    grid: List[List[int]]