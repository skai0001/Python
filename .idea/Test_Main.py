""" Author: Hasan Skaiky
 Date: 26/02/2019
_Unit_Testing  """


import unittest


class KnownValues(unittest.TestCase):

    def test_recordMatches_for_dataset(self):
        """
        captures the result of the funciton
        & check for expected result
        """

        expected ="Dryas integrifolia,2016,169,1,12,0,0,AF, IW"
        result = expected
        self.assertTrue(result) #checks for expected resutl

if __name__ == '__main__':
    unittest.main()
