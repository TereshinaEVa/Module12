import unittest
import tests_12_3 as t123

check = unittest.TestSuite()
check.addTest(unittest.TestLoader().loadTestsFromTestCase(t123.RunnerTest))
check.addTest(unittest.TestLoader().loadTestsFromTestCase(t123.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(check)