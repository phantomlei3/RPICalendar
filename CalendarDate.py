from datetime import datetime

month_dict = {
    'January': '1',
    'February': '2',
    'March': '3',
    'April': '4',
    'May': '5',
    'June': '6',
    'July': '7',
    'August': '8',
    'September': '9',
    'October': '10',
    'November': '11',
    'December': '12'
}

def is_integer(var):
    """helper function to test if instance is a int"""
    try:
        int(var)
        return True
    except ValueError:
        return False


class CalendarDate:
    """ CalendarDate represents date with year, month and day """
    """ This API is currently designed for rpi calendar, not ADT"""



    #
    # constructor
    #
    # @param: year, month, day, string
    # @raise: if year, month and day are not int, throw illegal arguments
    # @raise: if len(year) != 4
    #           month <= 0 or month > 12
    #           day <= 0 or day >= 31 throw illegal arguments
    #
    # TODO: verify the amount of day is legal to its month
    # TODO: specify each exception
    def __init__(self, year, month, day):

        if not is_integer(year):
            raise Exception(year+" is Illegal arguments")

        if not is_integer(day):
            raise Exception(day+" is Illegal arguments")

        # convert month to int if its format is in English
        if not is_integer(month):
            if month in month_dict.keys():
                month = month_dict[month]
            else:
                raise Exception("Illegal arguments")

        # scope detection
        if not (len(str(year)) == 4 and 1 <= int(month) <= 12 and 1 <= int(day) <= 31):
            raise Exception("Illegal arguments")

        self._year = int(year)
        self._month = int(month)
        self._day = int(day)

    #
    # <= operator
    #
    # the older the time is, the smaller it is
    # 1990/01/03 <= 1990/01/04 ==> True
    #
    def __le__(self, other):
        if isinstance(other, CalendarDate):
            if self._year == other._year:
                if self._month == other._month:
                    return self._day <= other._day
                else:
                    return self._month <= other._month
            else:
                return self._year <= other._year
        else:
            return False

    #
    # >= operator
    #
    # the older the time is, the smaller it is
    # 1990/01/04 >= 1990/01/03 ==> True
    #
    def __ge__(self, other):
        if isinstance(other, CalendarDate):
            if self._year == other._year:
                if self._month == other._month:
                    return self._day >= other._day
                else:
                    return self._month >= other._month
            else:
                return self._year >= other._year
        else:
            return False

    def __str__(self):
        return "{}/{}/{}".format(self._year, self._month, self._day)

    #
    # compare the date with the current time
    #
    # @return true if passed. Otherwise, return false
    def is_passed(self):
        current_time = datetime.now()
        current_date = CalendarDate(current_time.year, current_time.month, current_time.day);
        if current_date >= self:
            return True
        else:
            return False




