### Import Abstract Base Class Package to set up abstract class Servicable
from abc import ABC, abstractmethod

### Servicable Class
class Servicable(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass