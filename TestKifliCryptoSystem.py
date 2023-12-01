import unittest
import kifli as kifli


class TestKifliCryptoSystem(unittest.TestCase):

    def test_gen_pochon(self):
        n = 5
        pochon = kifli.gen_pochon(n)
        self.assertEqual(len(pochon), n)
        self.assertTrue(all(pochon[i] < pochon[i + 1] for i in range(n - 1)))

    def test_gen_cle_privee_publique(self):
        n = 5
        cle_privee = kifli.gen_cle_privee(n)
        cle_publique = kifli.gen_cle_publique(cle_privee)
        self.assertEqual(len(cle_publique), n)

    def test_solve_pochon(self):
        pochon = [2, 5, 11, 23, 55]
        cible = 1214
        solution = kifli.solve_pochon(pochon, cible)
        self.assertEqual(len(solution), len(pochon))
        self.assertEqual(sum(p * b for p, b in zip(pochon, solution)), cible)


if __name__ == '__main__':
    unittest.main()
