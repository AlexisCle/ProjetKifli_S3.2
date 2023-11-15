def gen_pochon(n):
    pass


def gen_cle_privee(n):
    pass


def gen_cle_publique(cle_privee):
    pass


def solve_pochon(pochon, c):
    pass


def chiffrer(m, cle_publique):
    pass


def dechiffrer(mc, cle_privee):
    pass


def test_chiffrement_dechiffrement(message, n):
    print("Message: {}".format(message))
    cle_privee = gen_cle_privee(n)
    cle_publique = gen_cle_publique(cle_privee)
    mc = chiffrer(message, cle_publique)
    m = dechiffrer(mc, cle_privee)
    print("Message chiffré: {}".format(mc))
    print("Message déchiffré: {}".format(m))


def text_to_binary(text):
    return [int(i) for i in ''.join([bin(ord(i))[2:].zfill(8) for i in text])]


def binary_to_text(binary):
    return ''.join([chr(int(''.join(binary[i:i + 8]), 2)) for i in range(0, len(binary), 8)])


def main():
    msg1 = "Hello World!"
    msg2 = "Kifli"
    test_chiffrement_dechiffrement(msg1, text_to_binary(msg1))
    test_chiffrement_dechiffrement(msg2, text_to_binary(msg2))
