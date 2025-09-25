from abc import ABC
from typing import Optional

class IPageMapTable(ABC):
    def __init__(self):
        self.__table: dict[tuple[int, int], Optional[int]] = {}
        
    def add_page_frame(self, job_id: int, page_number: int, page_frame_number: int):
        self.__table[job_id, page_number] = page_frame_number
    
    def find_page_frame(self, job_id: int,page_number: int) -> Optional[int]:
        record = self.__table.get((job_id, page_number))
        if record is None:
            raise KeyError(f"No mapping found for job {job_id}, page {page_number}")
        return record