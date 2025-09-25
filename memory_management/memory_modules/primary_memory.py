from page_modules.page_frame import PageFrame
from .interfaces.iprimary_memory import IPrimaryMemory

class PrimaryMemory(IPrimaryMemory):
    def __init__(self, frame_size: int, memory_size: int):
        super().__init__(frame_size, memory_size)
