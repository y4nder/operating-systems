class MemoryManager:
    def __init__(self):
      self.ram_instance = Ram()
      
    def has_limit_reached(self, counter: int):
      return self.ram_instance.has_limit_reached(counter)
    
    def load(self, location: int, value: str):
      self.ram_instance.load(location, value)
      
    def dump(self):
      return f"\n[Memory]: {self.ram_instance.dump()}"

class Ram:
    def __init__(self):
      self.limit = 5
      self.addresses: list[str] = [""] * self.limit 
      
    def load(self, location: int, value: str):
        self.addresses[location] = value

    def has_limit_reached(self, counter: int):
        return self.limit == counter
      
    def dump(self):
      return self.addresses
