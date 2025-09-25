from .interfaces.imemory_manager import IMemoryManager
from .primary_memory import PrimaryMemory
from .secondary_memory import SecondaryMemory
from .memory_manager import MemoryManager
from .page_map_table import PageMapTable

class MemoryFactory:
    @staticmethod
    def create_memory_manager(page_size: int, primary_memory_size: int, secondary_memory_size: int) -> IMemoryManager:
        primary_memory = PrimaryMemory(page_size, primary_memory_size)
        secondary_memory = SecondaryMemory(page_size, secondary_memory_size)
        pmt = PageMapTable()
        return MemoryManager(primary_memory, secondary_memory, pmt)