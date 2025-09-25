from abc import ABC, abstractmethod
from typing import Optional
from page_modules.page_frame import PageFrame

class IPrimaryMemory(ABC):
    def __init__(self, frame_size: int, memory_size: int):
        self._frame_size = frame_size
        self._page_frames: list[Optional[PageFrame]] = [None for _ in range(memory_size)]
        
    @property
    def frame_size(self):
        return self._frame_size
    
    @property
    def page_frames(self):
        return self._page_frames
    