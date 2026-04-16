from odoo import fields, models


class IbatixMediateurCee(models.Model):
    _name = 'ibatix.mediateur.cee'
    _description = 'Médiateur CEE'

    name = fields.Char(string='Nom', required=True)
    street = fields.Char(string='Rue')
    city = fields.Char(string='Ville')
    zip = fields.Char(string='Code postal')
    phone = fields.Char(string='Téléphone')
    email = fields.Char(string='Email')
    lien_formulaire = fields.Char(string='Lien formulaire du contact')
    website = fields.Char(string='Site Web')
    is_default = fields.Boolean(string='Est par défaut')
