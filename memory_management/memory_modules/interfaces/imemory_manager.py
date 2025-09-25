from abc import ABC, abstractmethod

from .ipage_map_table import IPageMapTable
from .iprimary_memory import IPrimaryMemory
from .isecondary_memory import ISecondaryMemory
from page_modules.page import Page


class IMemoryManager(ABC):
    def __init__(self, primary_memory: IPrimaryMemory, secondary_memory: ISecondaryMemory, pmt: IPageMapTable):
        self.__primary_memory = primary_memory
        self.__secondary_memory = secondary_memory
    
    @property
    def primary_memory(self):
        return self.__primary_memory
    
    @property
    def secondary_memory(self):
        return self.__secondary_memory
    
    @abstractmethod
    def load_to_secondary_memory(self, pages: list[Page]):
        pass
    