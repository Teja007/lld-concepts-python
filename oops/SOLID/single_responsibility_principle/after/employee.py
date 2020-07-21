#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Models an employee form a business perspective """

import os


class Employee:
    def __init__(self, full_name, monthly_income):
        self._monthly_income = None
        self._nb_hours_per_week = None
        (self._first_name, self._last_name) = full_name.split(' ')
        self.set_monthly_income(monthly_income)

    def get_email(self):
        return self._first_name + '.' + self._last_name + \
               '@globomanticshr.com'

    def __str__(self):
        return self._first_name + ' ' + self._last_name + \
               ' - ' + str(self._monthly_income)

    def get_monthly_income(self):
        return self._monthly_income

    def set_monthly_income(self, monthly_income):
        if monthly_income < 0:
            raise Exception("Income must be positive")
        self._monthly_income = monthly_income

    def get_nb_hours_per_week(self):
        return self._nb_hours_per_week

    def set_nb_hours_per_week(self, nb_hours_per_week):
        if nb_hours_per_week <= 0:
            raise Exception("Income must be positive")
        self._nb_hours_per_week = nb_hours_per_week

    def get_full_name(self):
        return self._first_name + ' ' + self._last_name

    @staticmethod
    def save(employee):
        try:
            employee_record = "### EMPLOYEE RECORD ####\n"
            employee_record += "NAME: "
            employee_record += employee.get_full_name() + "\n"
            employee_record += "POSITION: "
            employee_record += employee.__class__.__name__ + "\n"
            employee_record += "EMAIL: "
            employee_record += employee.get_email() + "\n"
            employee_record += "MONTHLY WAGE: "
            employee_record += str(employee.get_monthly_income()) + "\n"
            file_path = os.path.join(
                os.getcwd(),
                employee.get_full_name().replace(' ', '_') + ".rec"
            )
            f1 = open(file_path, "w")
            f1.write(employee_record)
            f1.close()
        except IOError as ex:
            raise IOError("Failed to save employee" + str(ex))
