from odoo import fields, models


class IbatixGestionnaireReseau(models.Model):
    _name = 'ibatix.gestionnaire.reseau'
    _description = 'Gestionnaire de réseau'

    name = fields.Char(string='Nom', required=True)
    logo = fields.Binary(string='Logo / Image')
    street = fields.Char(string='Rue')
    city = fields.Char(string='Ville')
    zip = fields.Char(string='Code postal')
    email = fields.Char(string='Email')
    mobile = fields.Char(string='Mobile')
    siren = fields.Char(string='SIREN')
    siret = fields.Char(string='SIRET')
