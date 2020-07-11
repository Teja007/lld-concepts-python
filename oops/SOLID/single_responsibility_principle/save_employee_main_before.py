#!/usr/bin/env python
# -*- coding: utf-8 -*-

from before.employee import Employee
from before.employee_repository import EmployeeRepository


class SaveEmployeeMain():
    @staticmethod
    def main():
        repository = EmployeeRepository()
        employees = repository.find_all()

        for employee in employees:
            Employee.save(employee)


if __name__ == '__main__':
    SaveEmployeeMain.main()
