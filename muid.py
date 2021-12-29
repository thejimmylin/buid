# Memorable uid
import random

vowel_chars = list("aeiou")
consonat_chars = list("bcdfghjklmnpqrstvwxyz")


def get_char(char_type, separator="-"):
    if char_type == "v":
        return random.choice(vowel_chars)
    if char_type == "c":
        return random.choice(consonat_chars)
    if char_type == "-":
        return separator


def get_muid(char_types="cvcv-cvcv-cvcv-cvcv", separator="-"):
    muid_chars = []
    for char_type in char_types:
        char = get_char(char_type, separator=separator)
        muid_chars.append(char)
    muid = "".join(muid_chars)
    return muid


for _ in range(10):
    print(get_muid())
