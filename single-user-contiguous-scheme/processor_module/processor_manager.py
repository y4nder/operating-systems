class ProcessorManager:
  def __init__(self):
    self.processer_instance = CPU()
  
  def initialize_cpu(self):
    self.processer_instance.store_first_location(0)
  
  def get_program_counter(self) -> int:
    return self.processer_instance.get_current_program_counter()

  def increment_program_counter(self):
    self.processer_instance.increment_program_counter()

class CPU:
    def __init__(self):
      self.base_register = 0
      self.program_counter = 0

    def store_first_location(self, location: int):
        self.base_register = location
        
    def get_current_program_counter(self):
        return self.program_counter
      
    def increment_program_counter(self):
      self.program_counter += 1