"""
Function 7 Open Function
Author: @ Jerome
"""


class Horoscope:
    def __init__(self):
        # Upon initalization, create a pre-defined tuple of horoscopes,
        # with another nested tuple for the start and end date each
        self.horoscopes = {
            ((3, 21), (4, 19)): "Aries",
            ((4, 20), (5, 20)): "Taurus",
            ((5, 21), (6, 20)): "Gemini",
            ((6, 21), (7, 22)): "Cancer",
            ((7, 23), (8, 22)): "Leo",
            ((8, 23), (9, 22)): "Virgo",
            ((9, 23), (10, 22)): "Libra",
            ((10, 23), (11, 21)): "Scorpio",
            ((11, 22), (12, 21)): "Sagittarius",
            ((12, 22), (1, 19)): "Capricorn",
            ((1, 20), (2, 18)): "Aquarius",
            ((2, 19), (3, 20)): "Pisces"
        }

    # Function to return horoscope type from horoscope using the date input
    def get_horoscope(self, dateInput):
        dateTuple = (dateInput.month, dateInput.day)

        return self.horoscopes[next(iter(filter(lambda x: (x[0] <= dateTuple <= x[1]), self.horoscopes)))]

    # Function to return horoscope date range from horoscope list using the date input
    def get_horoscope_range(self, dateInput):
        dateTuple = (dateInput.month, dateInput.day)

        return next(iter(filter(lambda x: (x[0] <= dateTuple <= x[1]), self.horoscopes)))
