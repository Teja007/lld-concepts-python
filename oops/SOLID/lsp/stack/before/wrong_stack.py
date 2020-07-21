#!/usr/bin/env python
# -*- coding: utf-8 -*-


class WrongStack(list):
    def __init__(self):
        self.__top_pointer = 0

    def push(self, a):
        self.append(a)
        self.__top_pointer += 1

    def pop(self):
        self.__delitem__(self.__top_pointer - 1)
        self.__top_pointer -= 1

    def top(self):
        return self.__getitem__(self.__top_pointer - 1)


if __name__ == "__main__":
    st = WrongStack()
    st.push(1)
    st.push(2)
    print(st.top())
    st.pop()
    print(st.top())
    st.clear()
    print(st.top())
