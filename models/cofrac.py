from odoo import fields, models


class IbatixCofrac(models.Model):
    _name = 'ibatix.cofrac'
    _description = 'Cofrac'

    name = fields.Char(string='Nom', required=True)
    logo = fields.Binary(string='Logo / Image')
    street = fields.Char(string='Rue')
    city = fields.Char(string='Ville')
    zip = fields.Char(string='Code postal')
    email = fields.Char(string='Email')
    mobile = fields.Char(string='Mobile')
    siren = fields.Char(string='SIREN')
    cofrac = fields.Char(string="Numéro d'accréditation COFRAC")
    date_fin_certificat = fields.Date(string='Date de fin du certificat')
    is_default = fields.Boolean(string='Est par défaut')
