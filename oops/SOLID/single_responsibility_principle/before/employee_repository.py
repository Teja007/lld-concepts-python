#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .full_time_employee import FullTimeEmployee
from .part_time_employee import PartTimeEmployee


class EmployeeRepository():
    def find_all(self):
        # Employees are kept in memory for simplicity
        anna = FullTimeEmployee("Anna Smith", 2000)
        billy = FullTimeEmployee("Billy Leech", 920)

        steve = PartTimeEmployee("Steve Jones", 800)
        magda = PartTimeEmployee("Magda Iovan", 920)

        return [anna, billy, steve, magda]
