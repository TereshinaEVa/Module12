import unittest
from unittest import TestCase
from runner_test import runner as run
from run_turnament_tests import runner_and_tournament as tur


class RunnerTest(TestCase):

    is_frozen = False

    @unittest.skipIf(not is_frozen, 'Тесты этого кейса заморожены')
    def test_walk(self):
        hum1 = run.Runner('Vasiliy')
        for _ in range(10):
            hum1.walk()

        self.assertEquals(hum1.distance, 50)

    @unittest.skipIf(not is_frozen, 'Тесты этого кейса заморожены')
    def test_run(self):
        hum2 = run.Runner('Olga')
        for _ in range(10):
            hum2.run()

        self.assertEquals(hum2.distance, 100)

    @unittest.skipIf(not is_frozen, 'Тесты этого кейса заморожены')
    def test_challenge(self):
        hum3 = run.Runner('Mariya')
        hum4 = run.Runner('Petr')
        for _ in range(10):
            hum3.run()
            hum4.walk()

        self.assertNotEquals(hum3.distance, hum4.distance)


class TournamentTest(TestCase):

    is_frozen = True

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

    @unittest.skipIf(not is_frozen, 'Тесты этого кейса заморожены')
    def test_1(self):
        t1 = tur.Tournament(90, self.run_1, self.run_3)
        result1 = t1.start()
        last_runner1 = list(result1.values())
        self.assertTrue(last_runner1[-1] == 'Ник')
        self.all_results['test_1'] = result1

    @unittest.skipIf(not is_frozen, 'Тесты этого кейса заморожены')
    def test_2(self):
        t2 = tur.Tournament(90, self.run_2, self.run_3)
        result2 = t2.start()
        last_runner2 = list(result2.values())
        self.assertTrue(last_runner2[-1] == 'Ник')
        self.all_results['test_2'] = result2

    @unittest.skipIf(not is_frozen, 'Тесты этого кейса заморожены')
    def test_3(self):
        t3 = tur.Tournament(90, self.run_1, self.run_2, self.run_3)
        result3 = t3.start()
        last_runner3 = list(result3.values())
        self.assertTrue(last_runner3[-1] == 'Ник')
        self.assertTrue(last_runner3[-2] == 'Андрей')
        self.all_results['test_3'] = result3


