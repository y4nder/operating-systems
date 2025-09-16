from memory_module.memory_manager import MemoryManager
from processor_module.processor_manager import ProcessorManager

class OperatingSystem:
    def __init__(self):
      self.processor_manager = ProcessorManager()
      self.memory_manager = MemoryManager()
      
    def run(self, instructions: list[str]):
        self.processor_manager.initialize_cpu()
        
        while True:
            counter = self.processor_manager.get_program_counter()
            self.processor_manager.increment_program_counter()
            if(counter == len(instructions)):
                print("[OS]: finished loading program...")
                break
            
            current_instruction = instructions[counter]
            
            if(self.memory_manager.has_limit_reached(counter)):
                print("[OS]: stopped loading program, memory limit reached")
                break
            
            self.memory_manager.load(counter, current_instruction)
            
        print(f"{self.memory_manager.dump()}")