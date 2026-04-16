from odoo import fields, models


class IbatixAuditeur(models.Model):
    _name = 'ibatix.auditeur'
    _description = 'Auditeur'

    name = fields.Char(string='Nom', required=True)
    avatar = fields.Binary(string='Photo / Avatar')
    street = fields.Char(string='Rue')
    city = fields.Char(string='Ville')
    zip = fields.Char(string='Code postal')
    email = fields.Char(string='Email')
    mobile = fields.Char(string='Mobile')
    representant_legal = fields.Char(string='Représentant Légal')
    nom_societe = fields.Char(string='Nom de la société')
    siren = fields.Char(string='SIREN')
    siret = fields.Char(string='SIRET')
    certificat = fields.Char(string='Certificat')
    is_default = fields.Boolean(string='Est par défaut')
    signature_image = fields.Binary(string='Image de signature')
