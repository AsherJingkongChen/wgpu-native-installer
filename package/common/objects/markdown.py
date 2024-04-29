from abc import abstractmethod

class Markdown:
    """
    Abstract Markdown formatting
    """

    def __str__(self) -> str:
        return self.to_markdown()

    @abstractmethod
    def to_markdown(self) -> str:
        raise NotImplementedError
