from odoo import models, fields


class EmployeeLevel(models.Model):
    _name = "employee.level"
    _description = "Employee Level"
    _rec_name = "level"

    level = fields.Char(string="Level")
    salary = fields.Integer(string="salary")
