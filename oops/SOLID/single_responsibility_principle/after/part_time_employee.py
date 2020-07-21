#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .employee import Employee


class PartTimeEmployee(Employee):
    def __init__(self, full_name, monthly_income):
        super().__init__(full_name, monthly_income)
        self.set_nb_hours_per_week(20)
