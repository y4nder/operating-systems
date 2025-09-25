from page_modules.page import Page
from .interfaces.imemory_manager import IMemoryManager
from .interfaces.iprimary_memory import IPrimaryMemory
from .interfaces.isecondary_memory import ISecondaryMemory
from .errors import memory_errors as err

class MemoryManager(IMemoryManager):
    def __init__(self, primary_memory: IPrimaryMemory, secondary_memory: ISecondaryMemory):
        super().__init__(primary_memory, secondary_memory)
        
    def load_to_secondary_memory(self, pages: list[Page]):
        if(len(pages) > self.secondary_memory.memory_size):
            raise err.LoadingToSecondaryError(f"pages cannot fit inside secondary memory: {len(pages)} > {self.secondary_memory.memory_size}")
        
        for index in range(0, len(pages)):
            self.secondary_memory.pages[index] = pages[index]