from __future__ import annotations

from sphinxy.riddle import Riddle


class IncorrectAnswer(Exception):
    ...


class Sphinx:
    def __init__(self, name: str) -> None:
        """ Init the class Sphinx.

        Args:
            name (str): _description_
        """
        self._name = name
        self._riddle = Riddle(
            question=(
                "What goes on four legs in the morning, two legs at noon, "
                "and three legs in the evening?"
            ),
            answer="man",
        )

    def introduce(self) -> str:
        """Introduction function that give details about the features of the website.

        Returns:
            str: _description_
        """
        return (
            f"Greetings, mortals. I am {self._name}. I have guarded the city of Thebes"
            "for centuries and posed riddles to those who dared to approach me."
        )

    def update_riddle(self, riddle: Riddle) -> str:
        self._riddle = riddle
        return "I have updated my riddle. Are you ready to solve it?"

    def pose_riddle(self, include_hint: bool = False) -> tuple[str, str | None]:
        """Function that manage the creation of a riddle.

        Args:
            include_hint (bool, optional): _description_. Defaults to False.

        Returns:
            tuple[str, str | None]: _description_
        """
        hint = (
            f"Hint: The answer starts with the letter '{self._riddle.get_hint()}'."
            if include_hint
            else None
        )
        return (self._riddle.question, hint)

    def check_riddle_answer(self, answer: str, return_hint: bool = False) -> str:
        """Evaluates the given answer to the riddle.

        Args:
            answer (str): _description_
            return_hint (bool, optional): _description_. Defaults to False.

        Raises:
            IncorrectAnswer: _description_

        Returns:
            str: _description_
        """
 
        if self._riddle.check_answer(answer):
            return "Your answer was correct. You may pass."
        elif return_hint:
            return (
                "Your answer was wrong. Hint: The answer starts with the letter "
                f"'{self._riddle.get_hint()}'."
            )
        else:
            raise IncorrectAnswer("Your answer was wrong. You shall not pass.")
