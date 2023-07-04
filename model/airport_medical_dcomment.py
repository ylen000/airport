from odoo import models, fields


class AirportMedicalDcomment(models.Model):
    _name = 'airport.medical.dcomment'
    _description = 'Airport medical docter comment model'

    name = fields.Char(string='醫師囑言')
    medical_ids = fields.One2many('airport.medical', 'dcomment_id')
