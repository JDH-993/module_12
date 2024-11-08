import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        a = Runner("dor")
        for i in range(10):
            a.walk()
        self.assertEqual(a.distance, 50)
    def test_run(self):
        b = Runner("Bor")
        for i in range(10):
            b.run()
        self.assertEqual(b.distance, 100)
    def test_challenge(self):
        y = Runner("tre")
        u = Runner("try")
        for i in range(10):
            y.walk()
            u.run()
        self.assertNotEqual(y.distance, u.distance)