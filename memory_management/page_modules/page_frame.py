from .page import Page
from typing import Optional

class PageFrame:
    def __init__(self, page: Optional[Page] = None):
        self.__page = page;
    
    @property
    def data(self):
        return self.__page