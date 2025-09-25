class Page:
    def __init__(self, page_size: int, page_number: int, allocated_space: int, displacement: int):
        self.__page_size = page_size
        self.__page_number = page_number
        self.__displacement = displacement
        self.__allocated_space = allocated_space
        
    @property
    def page_size(self):
        return self.__page_size
    
    @property
    def page_number(self):
        return self.__page_number
    
    @property
    def allocated_space(self):
        return self.__allocated_space
    
    @property
    def displacement(self):
        return self.__displacement