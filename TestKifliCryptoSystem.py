import unittest
from math import gcd

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
        self.assertEqual(len(cle_privee['pochon']), n)
        self.assertEqual(len(cle_privee['sigma']), n)
        self.assertTrue(cle_privee['W'] < cle_privee['M'])
        self.assertTrue(cle_privee['W'] > 0)
        self.assertTrue(cle_privee['M'] > 0)
        self.assertTrue(cle_privee['M'] > cle_privee['pochon'][n - 1])
        self.assertTrue(gcd(cle_privee['M'],cle_privee['W'])==1)
        cle_publique = kifli.gen_cle_publique(cle_privee)
        self.assertEqual(len(cle_publique), n)

    def test_solve_pochon(self):
        pochon = [2, 4, 8, 16, 32, 64]
        cible = 90
        solution = kifli.solve_pochon(pochon, cible)
        totSol = 0
        self.assertEqual(len(solution), len(pochon))
        for i in range(len(solution)):
            self.assertTrue(solution[i] in [0, 1])
            totSol += solution[i] * pochon[i]
        self.assertEqual(totSol, cible)

    def test_chiffrer_dechiffrer(self):
        for i in range (100):
            pochon = [2, 5, 11, 23, 55]
            n = 5
            m = 113
            w = 27
            permutation_sigma = [1, 4, 2, 0, 3]
            cle_privee = {'pochon': pochon, 'M': m, 'W': w, 'sigma': permutation_sigma}
            cle_publique = kifli.gen_cle_publique(cle_privee)
            self.assertEqual(len(cle_publique), n)
            self.assertEqual(cle_publique, [22, 16, 71, 54, 56])
            print(cle_publique)
            message_original = [1, 0, 1, 0, 1]
            mc = kifli.chiffrer(message_original, cle_publique)
            self.assertEqual(mc, 149)
            print(mc)
            mdc = kifli.dechiffrer(mc, cle_privee)
            print(mdc)
            self.assertEqual(mdc, message_original)


if __name__ == '__main__':
    unittest.main()
