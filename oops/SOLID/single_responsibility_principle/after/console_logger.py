#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ConsoleLogger:
    @staticmethod
    def write_info(msg):
        print("Info: " + msg)

    @staticmethod
    def write_error(msg, ex):
        print("Error: " + msg + ";" + ex)
