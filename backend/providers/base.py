from abc import ABC, abstractmethod


class BaseProvider(ABC):
    @abstractmethod
    def generate(self, messages, tools=None, **kwargs):
        raise NotImplementedError
