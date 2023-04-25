# -*- coding : utf-8 -*-
# Time       : 2023/4/25 11:20
# Auth       : Yangyang Zhang(张洋洋)
# File       : ReverseWordOrder.py
# Explain    : 颠倒词序

"""
题目：
输入单行英文句子，里面包含英文字母，空格以及 ,.? 三种标点符号，请将句子内每个单词进行倒序，并输出倒序后的语句。
"""


def reverse_sentence_words(sentence: str) -> str:
    """
    将英文句子中的每个单词反转，并输出反转后的整个句子。

    Args:
        sentence: 要反转的英文句子。
    Returns:
        反转后的英文句子。
    """
    target = ""
    index = 0
    flag = True

    for i, c in enumerate(sentence):
        if c in (',', '.', '?', ' '):
            if flag:
                target += sentence[i-1::-1]
                target += c
                index = i+1
                flag = False
            else:
                target += sentence[i-1:index-1:-1]
                target += c
                index = i+1

    return target


if __name__ == '__main__':
    reverse_sentence_words('hello, world. This is a test sentence.')
