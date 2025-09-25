from ..interfaces.ipage_mapper import IPageMapper
from job_modules.job import Job
from ..page import Page

class PageMapperV1(IPageMapper):
    def __init__(self, page_size: int):
        self.__page_size = page_size
    
    def map_to_pages(self, job: Job) -> list[Page]:
        page_count = job.job_size // self.__page_size
        final_displacement = job.job_size % self.__page_size
        
        if final_displacement > 0:
            page_count += 1

        pages: list[Page] = []
        
        for count in range(page_count):
            if count == page_count - 1 and final_displacement > 0:
                # Last page with leftover
                allocated_space = final_displacement
                displacement = final_displacement - 1
            else:
                # Full page
                allocated_space = self.__page_size
                displacement = self.__page_size - 1
            
            page = Page(self.__page_size, count, allocated_space, displacement)
            pages.append(page)
        
        return pages
