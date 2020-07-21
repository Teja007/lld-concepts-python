#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oops.SOLID.lsp.stack.after.exceptions.stack_exceptions import StackEmptyException


class Stack:
    def __init__(self):
        self.__l = list()
        self.__top_pointer = 0

    def push(self, val):
        self.__l.append(val)
        self.__top_pointer += 1

    def pop(self):
        if self.__top_pointer > 0:
            self.__top_pointer -= 1
            self.__l.__delitem__(self.__top_pointer)
        else:
            raise StackEmptyException("Cannot pop. Stack is empty!")

    def top(self):
        if self.__top_pointer > 0:
            return self.__l[self.__top_pointer-1]
        else:
            raise StackEmptyException("Stack is empty!")


if __name__ == "__main__":
    st = Stack()
    st.push(1)
    st.push(2)
    print(st.top())
    st.pop()
    print(st.top())
    st.pop()
    print(st.top())
