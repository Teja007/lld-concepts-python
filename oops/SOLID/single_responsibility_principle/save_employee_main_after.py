#!/usr/bin/env python
# -*- coding: utf-8 -*-

from after.employee import Employee
from after.employee_repository import EmployeeRepository
from after.console_logger import ConsoleLogger


class SaveEmployeeMain:
    @staticmethod
    def main():
        employees = EmployeeRepository.find_all()

        for e in employees:
            try:
                EmployeeRepository.save(e)
                ConsoleLogger.write_info("Saved employee: " + str(e))
            except IOError as ex:
                print(ex)
                ConsoleLogger.write_error("Error saving employee", ex)


if __name__ == '__main__':
    SaveEmployeeMain.main()