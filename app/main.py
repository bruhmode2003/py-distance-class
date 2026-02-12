class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def _value(other: object) -> float:
        if isinstance(other, Distance):
            return other.km
        return other  # type: ignore[return-value]

    def __add__(self, other: object) -> "Distance":
        return Distance(self.km + self._value(other))

    def __iadd__(self, other: object) -> "Distance":
        self.km += self._value(other)
        return self

    def __mul__(self, other: object) -> "Distance | None":
        if isinstance(other, Distance):
            return None
        return Distance(self.km * other)  # type: ignore[arg-type]

    def __truediv__(self, other: object) -> "Distance | None":
        if isinstance(other, Distance):
            return None
        return Distance(round(self.km / other, 2))  # type: ignore[arg-type]

    def __lt__(self, other: object) -> bool:
        return self.km < self._value(other)

    def __gt__(self, other: object) -> bool:
        return self.km > self._value(other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, (Distance, int, float)):
            return False
        return self.km == self._value(other)

    def __le__(self, other: object) -> bool:
        return self.km <= self._value(other)

    def __ge__(self, other: object) -> bool:
        return self.km >= self._value(other)
