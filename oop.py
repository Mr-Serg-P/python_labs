import random
from functools import reduce


class SeqLen:

    def __init__(self):
        self._number = random.randint(-100000000, 100000000)

    def __call__(self, *args, **kwargs):
        bits = self.__repr__()
        bit_cur = 0
        longest_seq = 0
        while bit_cur < len(bits):
            if bits[bit_cur] == '1':
                bit_next = bit_cur
                seq_len = 0
                changes = 1
                while bit_next < len(bits):
                    if bits[bit_next] == '1':
                        seq_len += 1
                    elif changes:
                        seq_len += 1
                        changes -= 1
                    else:
                        break
                    bit_next += 1
            else:
                seq_len = 1
                bit_next = bit_cur + 1
                while bit_next < len(bits):
                    if bits[bit_next] == '1':
                        seq_len += 1
                        bit_next += 1
                    else:
                        break

            if seq_len > longest_seq:
                longest_seq = seq_len
            if bit_next == len(bits):
                break
            else:
                bit_cur += 1

        return longest_seq

    def __repr__(self) -> str:
        return bin(self._number).split('b')[1]

    def __str__(self) -> str:
        return '\n'.join([
            "number: {}".format(self._number),
            "bin: {}".format(repr(self))
        ])


if __name__ == '__main__':
    s = SeqLen()
    print(s, s(), sep='\n')
