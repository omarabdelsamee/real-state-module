from odoo import models, fields



class Owner(models.Model):
    _name = 'owner'
    name = fields.Char()
    phone = fields.Char()
    address = fields.Char()
    property_ids = fields.One2many('property', 'owner_id')

    def action_test(self):
        print("hello")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'you are god',
                'type': 'rainbow_man',
            }
        }

















