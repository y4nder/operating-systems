from job_modules.job import Job
from page_modules.page_mappers.page_mapper_v1 import PageMapperV1
from page_modules.interfaces.ipage_mapper import IPageMapper
from memory_modules.memory_factory import MemoryFactory

if __name__ == "__main__":
    page_size = 100
    memory_manager = MemoryFactory.create_memory_manager(page_size, 4, 10)
    page_mapper: IPageMapper = PageMapperV1(page_size)
    
  
    job = Job(job_id=12, job_size=543)
    created_pages = page_mapper.map_to_pages(job)
    memory_manager.load_to_secondary_memory(created_pages)
    
    
    pages = memory_manager.secondary_memory.pages
    for index in range(0, len(pages)):
        current_page = pages[index]
        print(f"page frame: {index}", f"{(current_page.page_number,current_page.allocated_space, current_page.displacement) if current_page else 'Free'}")
    
    