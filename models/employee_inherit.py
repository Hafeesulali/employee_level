from odoo import models, fields
from odoo.exceptions import UserError


class EmployeeInherit(models.Model):
    _inherit = "hr.employee"

    employee_level_id = fields.Many2one("employee.level", string="Employee Level", readonly=True)
    salary = fields.Integer(related='employee_level_id.salary')
    button_visibility = fields.Boolean(string="Button Visibility")
    level_count = fields.Integer(default=0)

    def button_promote(self):

        id_list = [i.id for i in self.env['employee.level'].search([])]
        if self.env['employee.level'].search([]):
            self.employee_level_id = id_list[self.level_count]
            self.level_count += 1
            if self.employee_level_id == self.env['employee.level'].search([], order='id desc', limit=1):
                self.button_visibility = True
        else:
            raise UserError("Please create Levels")
