class Job:
    def __init__(self, job_id: int, job_size: int):
        self.__job_id = job_id
        self.__job_size = job_size
        
    @property
    def job_id(self):
        return self.__job_id
    
    @property
    def job_size(self):
        return self.__job_size