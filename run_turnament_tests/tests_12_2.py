import runner_and_tournament as tur
from unittest import TestCase
import unittest

class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run_1 = tur.Runner('Усейн', 10)
        self.run_2 = tur.Runner('Андрей', 9)
        self.run_3 = tur.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print({key: str(runner) for key, runner in result.items()})

    def test_1(self):
        t1 = tur.Tournament(90, self.run_1, self.run_3)
        result1 = t1.start()
        last_runner1 = list(result1.values())
        self.assertTrue(last_runner1[-1] == 'Ник')
        self.all_results['test_1'] = result1

    def test_2(self):
        t2 = tur.Tournament(90, self.run_2, self.run_3)
        result2 = t2.start()
        last_runner2 = list(result2.values())
        self.assertTrue(last_runner2[-1] == 'Ник')
        self.all_results['test_2'] = result2

    def test_3(self):
        t3 = tur.Tournament(90, self.run_1, self.run_2, self.run_3)
        result3 = t3.start()
        last_runner3 = list(result3.values())
        self.assertTrue(last_runner3[-1] == 'Ник')
        self.assertTrue(last_runner3[-2] == 'Андрей')
        self.all_results['test_3'] = result3

if __name__ == '__main__':
    unittest.main()