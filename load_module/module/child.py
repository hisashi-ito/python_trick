#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#【child】
#
try:
    from . parent import Parent
    print(". のほうが呼ばれたよ")
except:
    print(".なしが呼ばれたよ")
    from parent import Parent

class Child(Parent):
    def __init__(self):
        super().__init__()


# 作ったクラスのファイルをそのまま起動した場合
# UTとかでよく利用する
if __name__ == '__main__':
    Child()
