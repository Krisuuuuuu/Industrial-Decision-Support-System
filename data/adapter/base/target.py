from abc import abstractmethod


class Target:
    @abstractmethod
    def request(self) -> any: pass
