from odoo import models, fields, api
from odoo.odoo.exceptions import ValidationError





class Property (models.Model):
    _name = 'property'
    _description = 'New property'    # use this this command to create the name in chatter when create new rec
    _inherit = ['mail.thread',  'mail.activity.mixin']
    name = fields.Char(required=1, default='new', size=20)
    description = fields.Text()
    postcode = fields.Char(required=1)
    data_availability = fields.Date(tracking=1)   #use tracking to show updates in chatter
    expected_price = fields.Float()
    selling_price = fields.Float()
    diff = fields.Float(compute='_compute_diff', store=1, readonly=0)
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    user_id = fields.Many2one('res.users')
    garden_orientation = fields.Selection([
    ('north','North'),
    ('south', 'South'),
    ('east', 'East'),
    ('west', 'west'),
    ])
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('closed', 'Closed'),
    ], default='draft')

    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')
    owner_address = fields.Char(related='owner_id.address', readonly=0)
    owner_phone = fields.Char(related='owner_id.phone', readonly=0)
    property_line_ids = fields.One2many('property.line', 'property_id')
    @api.depends('expected_price','selling_price')
    def _compute_diff(self):
        for rec in self:
            print("hi")
            rec.diff = rec.expected_price - rec.selling_price



    @api.onchange('expected_price')
    def _onchange_expected_price(self):
        for rec in self:
            return {
                'warning': {'title': 'warning', 'message': 'negative value', 'type': 'notification'}
            }

    def action_draft(self):
        for rec in self:
          #  print("inside bending")
            rec.state = 'draft'


    def action_pending(self):
        for rec in  self:
            rec.state = 'pending'


    def action_sold(self):
        for rec in self:
            rec.state = 'sold'

    def action_closed(self):
        for rec in self:
            rec.state = 'closed'
    # _sql_constraints= [
    #     ( 'unique_name' , 'unique("name")' , 'this name is exist' )
    # ]
    # @api.constrains('bedrooms')
    # def _check(self):
    #     for rec in self:
    #         if rec.bedrooms == 0:
    #            print("the value is exist")
    #
    #
    # @api.model_create_multi
    # def create(self, vals):
    #      res = super(Property ,self).create(vals)
    #      print("create method0")
    #      return res
    #
    #
    # @api.model
    # def _search(self, domain, offset=0, limit=None, order=None, access_right_vid=None):
    #     res = super(Property, self)._search(domain, offset=0, limit=None, order=None, access_rights_uid=None)
    #     print("inside search method")
    #     return res
    # def write(self,vals):
    #     res = super(Property, self).write(vals)
    #     print("inside write method")
    #     return res
    # def unlink(self):
    #     res = super(Property, self).unlink()
    #     print("inside unlink method")
    #     return res





class PropertyLine(models.Model):
    _name = 'property.line'
    property_id = fields.Many2one('property')
    area = fields.Float()
    description = fields.Char()










