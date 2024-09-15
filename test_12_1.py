import unittest
from unittest import TestCase
import runner as run


class RunnerTest(TestCase):

    def test_walk(self):
        hum1 = run.Runner('Vasiliy')
        for _ in range(10):
            hum1.walk()

        self.assertEquals(hum1.distance, 50)

    def test_run(self):
        hum2 = run.Runner('Olga')
        for _ in range(10):
            hum2.run()

        self.assertEquals(hum2.distance, 100)

    def test_challenge(self):
        hum3 = run.Runner('Mariya')
        hum4 = run.Runner('Petr')
        for _ in range(10):
            hum3.run()
            hum4.walk()

        self.assertNotEquals(hum3.distance, hum4.distance)


if __name__ == '__main__':
    unittest.main()
