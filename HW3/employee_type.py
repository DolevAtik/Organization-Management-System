from enum import Enum

"""
Enumeration representing different types of employees in the organization.
Each employee type is assigned a unique integer value.
"""
class EmployeeType(Enum):
    SW_DEVELOPER = 1
    HW_DEVELOPER = 2
    TECH_LEAD = 3
    TEAM_LEADER = 4
    HR_MANAGER = 5
    RECRUITER = 6
    ACCOUNTANT = 7
    FINANCE_MANAGER = 8
    DIRECTOR = 9
    CTO = 10
    CEO = 11
