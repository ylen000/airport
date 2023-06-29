from odoo import models, fields


class AirportMedicalAssistScreening(models.Model):
    _name = 'airport.medical.assist.screening'
    _description = 'Airport medical assist screening model'

    name = fields.Char(string='協助篩檢名稱')
    medical_ids = fields.One2many('airport.medical', 'assist_screening_id')