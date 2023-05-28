from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Riddle:
    question: str
    answer: str

    def check_answer(self, answer: str) -> bool:
        """ Function that checks if a given answer is right or not.

        Args:
            answer (str): _description_

        Returns:
            bool: _description_
        """
        return answer.lower() == self.answer.lower()

    def get_hint(self) -> Iterator[str]:
        """Function that gives a hint to the user on demand.

        Yields:
            Iterator[str]: _description_
        """
        yield from iter(self.answer)
