from abc import ABC, abstractmethod
from job_modules.job import Job
from ..page import Page


class IPageMapper(ABC):
    
    @abstractmethod
    def map_to_pages(self, job: Job) -> list[Page]:
        pass