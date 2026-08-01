from dataclasses import dataclass


@dataclass
class Course:
    name: str
    rating: float
    slope: int
    par: int
    hole_pars: list

    def to_dict(self):
        return {
            "name": self.name,
            "rating": self.rating,
            "slope": self.slope,
            "par": self.par,
            "hole_pars": self.hole_pars
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["rating"],
            data["slope"],
            data["par"],
            data["hole_pars"]
        )