import re


class OutOfRangeError(ValueError):
    pass


class NotIntegerError(ValueError):
    pass


class InvalidRomanNumeralError(ValueError):
    pass


roman_numeral_map = (('M', 1000),
                     ('CM', 900),
                     ('D', 500),
                     ('CD', 400),
                     ('C', 100),
                     ('XC', 90),
                     ('L', 50),
                     ('XL', 40),
                     ('X', 10),
                     ('IX', 9),
                     ('V', 5),
                     ('IV', 4),
                     ('I', 1))

roman_numeral_pattern = re.compile('''
    ^                   # beginning of string
    M{0,4}              # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string
    ''', re.VERBOSE)


def to_roman(int_number):
    result = ''
    if int_number <= 0 or int_number > 4999:
        raise OutOfRangeError('The number You provided needs to be in range <1, 4999>')
    if not isinstance(int_number, int):
        raise NotIntegerError('This number should be INT type')

    for rom, _int in roman_numeral_map:
        while int_number >= _int:
            result += rom
            int_number -= _int
    return result


def from_roman(roman_numb):
    '''converts roman to int'''
    result = 0
    index = 0
    if not roman_numb:
        raise InvalidRomanNumeralError('The empty string is not good idea')
    if not roman_numeral_pattern.search(roman_numb):
        raise InvalidRomanNumeralError('The numbers is just wrong and needs to be written properly')

    for roman_, _int in roman_numeral_map:
        while roman_numb[index:index + len(roman_)] == roman_:  # index:index konczy iterowanie na ostatnim indexie
            result += _int
            index += len(roman_)
    return result



