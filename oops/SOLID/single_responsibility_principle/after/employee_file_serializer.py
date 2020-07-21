#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from .employee import Employee


class EmployeeFileSerializer:
    @staticmethod
    def serialize(employee):
        employee_record = "### EMPLOYEE RECORD ####\n"
        employee_record += "NAME: "
        employee_record += employee.get_full_name() + "\n"
        employee_record += "POSITION: "
        employee_record += employee.__class__.__name__ + "\n"
        employee_record += "EMAIL: "
        employee_record += employee.get_email() + "\n"
        employee_record += "MONTHLY WAGE: "
        employee_record += str(employee.get_monthly_income()) + "\n"
        return employee_record
