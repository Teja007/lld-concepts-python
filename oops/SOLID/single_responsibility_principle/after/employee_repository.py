#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from .employee import Employee
from .part_time_employee import PartTimeEmployee
from .full_time_employee import FullTimeEmployee
from .employee_file_serializer import EmployeeFileSerializer


class EmployeeRepository:
    @staticmethod
    def find_all():
        # Employees are kept in memory for simplicity
        anna = FullTimeEmployee("Anna Smith", 2000)
        billy = FullTimeEmployee("Billy Leech", 920)

        steve = PartTimeEmployee("Steve Jones", 800)
        magda = PartTimeEmployee("Magda Iovan", 920)

        return [anna, billy, steve, magda]

    @staticmethod
    def save(employee):
        employee_file_serializer = EmployeeFileSerializer()
        serialized_employee = employee_file_serializer.serialize(employee)

        try:
            file_path = os.path.join(
                os.getcwd(),
                employee.get_full_name().replace(' ', '_') + ".rec"
            )
            f1 = open(file_path, "w")
            f1.write(serialized_employee)
            f1.close()
        except IOError as ex:
            raise IOError("Failed to save employee" + str(ex))