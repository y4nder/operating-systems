from os_module.operating_system import OperatingSystem
from instructions.instructions import get_sample_instructions

if __name__ == "__main__":
    os = OperatingSystem()
    os.run(get_sample_instructions())