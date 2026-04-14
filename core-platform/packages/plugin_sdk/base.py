from abc import ABC, abstractmethod
from typing import Any, Dict


class BasePlugin(ABC):
    name: str = "base"
    version: str = "0.0.0"
    description: str = ""

    @abstractmethod
    def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError
