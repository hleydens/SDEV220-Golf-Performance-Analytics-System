from dataclasses import dataclass


@dataclass
class Course:

    name: str
    rating: float
    slope: int
    par: int
    hole_pars: list