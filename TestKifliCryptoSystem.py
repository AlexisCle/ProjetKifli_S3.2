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
        n = 8
        cle_privee = kifli.gen_cle_privee(n)
        cle_publique = kifli.gen_cle_publique(cle_privee)
        message = [1, 0, 1, 1, 0, 0, 1, 1]
        message_chiffre = kifli.chiffrer(message, cle_publique)
        message_dechiffre = kifli.dechiffrer(message_chiffre, cle_privee)
        self.assertEqual(message, message_dechiffre)



if __name__ == '__main__':
    unittest.main()
