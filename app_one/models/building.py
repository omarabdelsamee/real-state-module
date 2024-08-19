from odoo import models,fields






class Building (models.Model):
    _name = 'building'
    _description = 'New building'    # use this command to create the name in chatter when create new rec
    _inherit = ['mail.thread',  'mail.activity.mixin']
    #_rec_name = 'num'                  # use this for rename the number of building by num in header

    name = fields.Char()
    num = fields.Integer()
    code = fields.Char()
    description = fields.Char()
    active = fields.Boolean(default=1)            #for archive


