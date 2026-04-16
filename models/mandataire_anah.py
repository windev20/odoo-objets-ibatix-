from odoo import fields, models


class IbatixMandataireAnah(models.Model):
    _name = 'ibatix.mandataire.anah'
    _description = 'Mandataire ANAH'

    name = fields.Char(string='Nom', required=True)

    # Informations du gérant
    prenom = fields.Char(string='Prénom')
    nom_gerant = fields.Char(string='Nom')
    titre = fields.Selection([
        ('monsieur', 'Monsieur'),
        ('madame', 'Madame'),
    ], string='Titre')
    email = fields.Char(string='Email')
    mobile = fields.Char(string='Mobile')
    street = fields.Char(string='Rue')
    city = fields.Char(string='Ville')
    zip = fields.Char(string='Code postal')

    # Propriétés
    representant_administratif = fields.Boolean(string='Représentant administratif')
    representant_financier = fields.Boolean(string='Représentant financier')
    is_default = fields.Boolean(string='Est par défaut')
    signature_image = fields.Binary(string='Image de signature')
