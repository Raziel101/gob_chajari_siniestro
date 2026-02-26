from odoo import models, fields

class GobChajariSiniestroParticipacion(models.Model):
    _name = 'gob_chajari.siniestro.participacion'
    _description = 'Participación en Siniestro'
    _inherit = ['mail.thread']
    _rec_name = 'persona_id'

    siniestro_id = fields.Many2one(
        'gob_chajari.siniestro',
        string='Siniestro',
        required=True,
        ondelete='cascade'
    )

    persona_id = fields.Many2one(
        'gob_chajari.siniestro.persona',
        string='Persona',
        required=True
    )

    fecha_nacimiento = fields.Date(
        related='persona_id.fecha_nacimiento',
        string='Fecha de Nacimiento',
        store=True,
        readonly='False',
    )

    edad = fields.Char(
        related='persona_id.edad',
        string='Edad',
        store=True,
        readonly=False
    )

    dni = fields.Char(
        related='persona_id.dni',
        string='DNI',
        store=True,
        readonly=False
    )

    estado_civil = fields.Selection(
        related='persona_id.estado_civil',
        string='Estado Civil',
        store=True,
        readonly=False
    )

    licencia = fields.Selection(
        related='persona_id.licencia',
        string='Licencia',
        store=True,
        readonly=False,
    )


    vehiculo = fields.Char(
        string='Vehículo',
        tracking=True,
    )


    tipo_vehiculo = fields.Selection([
        ('auto', 'Auto'),
        ('pick up', 'Pick Up'),
        ('moto', 'Moto'),
        ('camioneta', 'Camioneta'),
        ('camion', 'Camion'),
        ('bicicleta', 'Bicicleta'),

    ])

    dominio = fields.Char(string='Dominio', tracking=True)

    lesiones = fields.Char(
        string='Lesiones',
        tracking=True
    )

    rol = fields.Selection([
        ('conductor', 'Conductor'),
        ('acompaniante', 'Acompañante'),
        ('peaton', 'Peatón'),
    ], string='Rol', tracking=True)
