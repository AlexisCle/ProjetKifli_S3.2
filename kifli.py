import random
from math import gcd
from random import randint


def gen_pochon(n):
    res = []
    i = 1
    while len(res) < n:
        res.append(i)
        i = randint(sum(res), sum(res) * 2)
    return res


def gen_cle_privee(n):
    pochon = gen_pochon(n)
    m = sum(pochon) + random.randint(1, 1000)
    w = random.randint(1, m - 1)
    while gcd(w, m) != 1:
        w = random.randint(1, m - 1)
    permutation_sigma = random.sample(range(1, n + 1), n)
    cle_privee = {'pochon': pochon, 'M': m, 'W': w, 'sigma': permutation_sigma}
    return cle_privee


def gen_cle_publique(cle_privee):
    pochon = cle_privee['pochon']
    m = cle_privee['M']
    w = cle_privee['W']
    permutation_sigma = cle_privee['sigma']
    cle_publique = [(pochon[permutation_sigma[i] - 1] * w) % m for i in range(len(pochon))]
    return cle_publique


def solve_pochon(pochon, c):
    res = []
    for i in range(len(pochon)):
        if pochon[i] <= c:
            res.append(1)
            c -= pochon[i]
        else:
            res.append(0)
    return res


def chiffrer(m, cle_publique):
    res = 0
    for i in range(len(m)):
        res += m[i] * cle_publique[i]
    return res


def dechiffrer(message_chiffre, cle_privee):
    pochon = cle_privee['pochon']
    m = cle_privee['M']
    w = cle_privee['W']
    permutation_sigma = cle_privee['sigma']
    inverse_w = pow(w, -1, m)
    d = (inverse_w * message_chiffre) % m
    bits_message_original = solve_pochon(pochon, d)
    message_original = [bits_message_original[permutation_sigma.index(i + 1)] for i in range(len(pochon))]

    return message_original


def test_chiffrement_dechiffrement(message, n):
    print("Message:           {}".format(message))
    cle_privee = gen_cle_privee(n)
    cle_publique = gen_cle_publique(cle_privee)
    mc = chiffrer(message, cle_publique)
    m = dechiffrer(mc, cle_privee)
    print("Message chiffré: {}".format(mc))
    print("Message déchiffré: {}".format(m))
    print("Message déchiffré: {}".format(binary_to_text(m)))


def text_to_binary(text):
    return [int(i) for i in ''.join([bin(ord(i))[2:].zfill(8) for i in text])]


# Turns a binary list into a string
def binary_to_text(binary):
    return ''.join([chr(int(''.join([str(binary[i+j]) for j in range(8)]), 2)) for i in range(0, len(binary), 8)])


def main():
    msg1 = "Hello World!"
    msg2 = "Kifli"
    test_chiffrement_dechiffrement(text_to_binary(msg1), len(msg1) * 8)
    test_chiffrement_dechiffrement(text_to_binary(msg2), len(msg2) * 8)
