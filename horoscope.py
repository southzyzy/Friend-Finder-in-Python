import datetime


class Horoscope:
    def __init__(self):
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

    def get_horoscope(self, dateInput):
        dateTuple = (dateInput.month, dateInput.day)

        # for h in self.horoscopes:
        #     if h[0] <= dateTuple <= h[1]:
        #         return self.horoscopes[(h[0], h[1])]

        return self.horoscopes[next(iter(filter(lambda x: (x[0] <= dateTuple <= x[1]), self.horoscopes)))]

    def get_horoscope_range(self, dateInput):
        dateTuple = (dateInput.month, dateInput.day)

        # for h in self.horoscopes:
        #     if h[0] <= dateTuple <= h[1]:
        #         return h

        return next(iter(filter(lambda x: (x[0] <= dateTuple <= x[1]), self.horoscopes)))
