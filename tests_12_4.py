import logging
import unittest
from unittest import TestCase
import rt_with_exceptions as run

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format="%(asctime)s | %(levelname)s | %(message)s")
class RunnerTest(TestCase):

    is_frozen = False

   # @unittest.skipIf(not is_frozen, 'Тесты этого кейса заморожены')
    def test_walk(self):
        try:
            hum1 = run.Runner('Vasiliy', -1)
        except ValueError as er:
            logging.warning(f'Неверная скорость для Runner. Ошибка {er}')
        else:
            for _ in range(10):
                hum1.walk()

            self.assertEquals(hum1.distance, 50)
            logging.info('Тест "test_walk" выполнен успешно')

   # @unittest.skipIf(not is_frozen, 'Тесты этого кейса заморожены')
    def test_run(self):
        try:
            hum2 = run.Runner(35)
        except TypeError as er:
            logging.warning(f'Неверный тип данных для объекта Runner. Ошибка: {er}')
        else:
            for _ in range(10):
                hum2.run()

            self.assertEquals(hum2.distance, 100)
            logging.info('Тест "test_run" выполнен успешно')

    @unittest.skipIf(not is_frozen, 'Тесты этого кейса заморожены')
    def test_challenge(self):
        hum3 = run.Runner('Mariya')
        hum4 = run.Runner('Petr')
        for _ in range(10):
            hum3.run()
            hum4.walk()

        self.assertNotEquals(hum3.distance, hum4.distance)



if __name__ == '__main__':
    unittest.main()

