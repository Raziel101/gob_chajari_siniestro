from odoo import models, fields

class GobChajariSiniestro(models.Model):
    _name = 'gob_chajari.siniestro'
    _description = 'Siniestro Vial'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'numero_id'

    numero_id = fields.Char(
        string='Número',
        required=True,
        tracking=True
    )
    ubicacion = fields.Char(string='Ubicación',required=True, tracking=True)
    fecha_hora = fields.Datetime(string='Fecha y Hora',required=True, tracking=True)

    tipo_intervencion = fields.Selection([
        ('sin_lesiones', 'Accidente de tránsito sin lesiones'),
        ('lesiones_leves', 'Accidente de tránsito con lesiones leves'),
        ('lesiones_graves', 'Accidente de tránsito con lesiones graves'),
        ('muerte', 'Accidente de tránsito con muerte'),
    ], string='Tipo de Intervención', tracking=True)

    siniestro_tipo = fields.Selection([
        ('colision', 'Colisión'),
        ('choque', 'Choque'),
        ('despiste', 'Despiste'),
        ('vuelco', 'Vuelco'),
    ], string='Tipo Siniestro', tracking=True)

    causa_sinistro = fields.Char(stirng='Causa del Siniestro', tracking=True)

    tipo_colision = fields.Selection([
        ('rozamiento', 'Rozamiento'),
        ('frontal', 'Frontal'),
        ('fronto_lateral', 'Fronto lateral'),
        ('lateral', 'Embestida lateral'),
        ('alcance', 'Alcance')
    ], string='Tipo de Colisión', tracking=True)

    caracteristica_calzada = fields.Selection([
        ('interseccion', 'Intersección'),
        ('recta', 'Recta'),
        ('rotonda', 'Rotonda'),
        ('puente', 'Puente'),
        ('fuera', 'Fuera de calzada'),
        ('otros', 'Otros'),
    ], string='Características de la Calzada', tracking=True)

    otros_calzada = fields.Char(
        string="Otros Calzada", tracking=True
    )

    material_calzada = fields.Selection([
        ('asfalto', 'Asfalto'),
        ('ripio', 'Ripio'),
        ('tierra', 'Tierra'),
        ('hormigon', 'Hormigón'),
        ('otros', 'Otros'),
    ], string='Material de la Calzada', tracking=True)

    estado_calzada = fields.Selection([
        ('humedo', 'Húmedo'),
        ('seco', 'Seco'),
    ], string='Estado de la Calzada', tracking=True)

    tipo_clima = fields.Selection([
        ('soleado', 'Soleado'),
        ('lluvia', 'Lluvia'),
        ('nublado', 'Nublado'),
    ], string='Tipo Clima', tracking=True)

    visibilidad = fields.Selection([
        ('artificial_buena', 'Luz Artificial - Buena'),
        ('artificial_regular', 'Luz Artificial - Regular'),
        ('artificial_mala', 'Luz Artificial - Mala'),
        ('natural_buena', 'Luz Natural - Buena'),
        ('natural_regular', 'Luz Natural - Regular'),
        ('natural_mala', 'Luz Natural - Mala'),
    ], string='Visibilidad', tracking=True)

    semaforo = fields.Boolean(string='Semáforo', tracking=True)

    observacion = fields.Text(string='Observaciones', tracking=True)

    croquis = fields.Binary(string='Croquis', tracking=True)
    croquis2 = fields.Binary(string='Croquis2', tracking=True)

    participacion_ids = fields.One2many(
        'gob_chajari.siniestro.participacion',
        'siniestro_id',
        string='Personas y Vehículos'
    )