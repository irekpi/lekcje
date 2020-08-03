import unittest
import roman


class KnownResults(unittest.TestCase):

    def setUp(self) -> tuple:
        self.known_values = (
            (1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V'), (6, 'VI'), (7, 'VII'), (8, 'VIII'),
            (9, 'IX'), (10, 'X'), (50, 'L'), (100, 'C'), (500, 'D'), (1000, 'M'), (31, 'XXXI'),
            (148, 'CXLVIII'), (294, 'CCXCIV'), (312, 'CCCXII'), (421, 'CDXXI'), (528, 'DXXVIII'),
            (621, 'DCXXI'), (782, 'DCCLXXXII'), (870, 'DCCCLXX'), (941, 'CMXLI'), (1043, 'MXLIII'),
            (1110, 'MCX'), (1226, 'MCCXXVI'), (1301, 'MCCCI'), (1485, 'MCDLXXXV'), (1509, 'MDIX'),
            (1607, 'MDCVII'), (1754, 'MDCCLIV'), (1832, 'MDCCCXXXII'), (1993, 'MCMXCIII'), (2074, 'MMLXXIV'),
            (2152, 'MMCLII'), (2212, 'MMCCXII'), (2343, 'MMCCCXLIII'), (2499, 'MMCDXCIX'), (2574, 'MMDLXXIV'),
            (2646, 'MMDCXLVI'), (2723, 'MMDCCXXIII'), (2892, 'MMDCCCXCII'), (2975, 'MMCMLXXV'), (3051, 'MMMLI'),
            (3185, 'MMMCLXXXV'), (3250, 'MMMCCL'), (3313, 'MMMCCCXIII'), (3408, 'MMMCDVIII'), (3501, 'MMMDI'),
            (3610, 'MMMDCX'), (3743, 'MMMDCCXLIII'), (3844, 'MMMDCCCXLIV'),
            (3888, 'MMMDCCCLXXXVIII'), (3940, 'MMMCMXL'), (3999, 'MMMCMXCIX'), (3999, 'MMMCMXCIX'), (4000, 'MMMM'),
            (4500, 'MMMMD'), (4888, 'MMMMDCCCLXXXVIII'), (4999, 'MMMMCMXCIX') )

    def test_to_roman_known_values(self):
        '''This should result with a proper roman number'''
        for _int, roman_num in self.known_values:
            result = roman.to_roman(_int)
            self.assertEqual(result, roman_num)

    def test_from_roman(self):
        '''This should result with an int number converted from roman'''
        for _int, roman_num in self.known_values:
            result = roman.from_roman(roman_num)
            self.assertEqual(_int, result)

    def tearDown(self) -> None:
        del self.known_values


class ToRomanBadInput(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_too_large(self):
        '''to_roman should fail with large number'''
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, 5000)

    def test_negative_number(self):
        '''to_roman should fail with negative numbers'''
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, -2)

    def test_zero_number(self):
        '''to_roman should fail with 0 as provided nubmer'''
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, 0)

    def test_not_integer(self):
        '''to_roman should fail with float number'''
        self.assertRaises(roman.NotIntegerError, roman.to_roman, 0.5)

    def tearDown(self) -> None:
        pass


class RoundTripCheck(unittest.TestCase):

    def test_roundtrip(self):
        '''from_roman(to_roman(n)) == n for all n'''
        for _int in range(1, 5000):
            roman_num = roman.to_roman(_int)
            result = roman.from_roman(roman_num)
            self.assertEqual(_int, result)


class FromRomanBadInput(unittest.TestCase):

    def test_to_many_repeated_numbers(self):
        '''You can't use to many reapeatable numbs'''
        for roman_numb in ('MMMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            self.assertRaises(roman.InvalidRomanNumeralError, roman.from_roman, roman_numb)

    def test_repeated_pairs(self):
        '''from_roman should fail with repeated pairs of numbers'''
        for roman_numb in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV', 'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(roman.InvalidRomanNumeralError, roman.from_roman, roman_numb)

    def test_malformed_ancedencs(self):
        '''from_roman should fail with malformed antecedents'''
        for roman_numb in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV', 'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(roman.InvalidRomanNumeralError, roman.from_roman, roman_numb)

    def test_blank(self):
        ''' if the input is '' error should be risen'''
        self.assertRaises(roman.InvalidRomanNumeralError, roman.from_roman, '')


if __name__ == '__main__':
    unittest.main()
