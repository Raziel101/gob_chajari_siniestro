from odoo import models, fields

class GobChajariSiniestroPersona(models.Model):
    _name = 'gob_chajari.siniestro.persona'
    _description = 'Persona involucrada en Siniestro'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'nombre'

    nombre = fields.Char(
        string='Nombre',
        required=True,
        tracking=True
    )
    fecha_nacimiento = fields.Date(
        string='Fecha de Nacimiento',
        tracking=True
    )
    dni = fields.Char(string='DNI', tracking=True)
    
    edad = fields.Char(string='Edad', required=True)

    estado_civil = fields.Selection([
        ('soltero', 'Soltero/a'),
        ('casado', 'Casado/a'),
        ('divorciado', 'Divorciado/a'),
        ('viudo', 'Viudo/a'),
    ], string='Estado Civil', tracking=True)

    licencia = fields.Selection([
        ('si', 'Sí'),
        ('no', 'No'),
        ('vencida', 'Vencida'),
    ], string='Licencia', tracking=True)

    participacion_ids = fields.One2many(
        'gob_chajari.siniestro.participacion',
        'persona_id',
        string='Participaciones'
    )
