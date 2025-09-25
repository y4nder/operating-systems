from page_modules.page import Page
from .interfaces.isecondary_memory import ISecondaryMemory

class SecondaryMemory(ISecondaryMemory):
    def __init__(self, page_size: int, memory_size: int):
        super().__init__(page_size, memory_size)
    