"""stub functions for Neopixel"""


class NeoPixel:
    """NeoPixel class"""
    def __setitem__(self, index: int, val: tuple) -> None:
        pass

    def __getitem__(self, index) -> tuple:
        return (1, 1, 1)

    def fill(self, color) -> None:
        """Colors all pixels the given ***color***."""

    def show(self) -> None:
        """Shows the new colors on the pixels themselves if they haven't already
        been autowritten.

        The colors may or may not be showing after this function returns because
        it may be done asynchronously.
        """

    def clear(self) -> None:
        """Clear all the pixels"""
