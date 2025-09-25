from abc import ABC, abstractmethod
from typing import Optional
from page_modules.page import Page

class ISecondaryMemory(ABC):
    def __init__(self, page_size: int, memory_size: int):
        self.__page_size = page_size
        self.__pages : list[Optional[Page]] = [None for _ in range(memory_size)]
        self.__memory_size = memory_size
        
    @property
    def page_size(self):
        return self.__page_size
    
    @property
    def pages(self):
        return self.__pages
    
    @property
    def memory_size(self):
        return self.__memory_size