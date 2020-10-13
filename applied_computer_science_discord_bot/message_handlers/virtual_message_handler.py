from abc import abstractmethod


class Handler:
    @abstractmethod
    def handle(self, message):
        pass
