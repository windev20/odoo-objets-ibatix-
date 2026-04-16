from odoo import fields, models


class IbatixMatricePrecarite(models.Model):
    _name = 'ibatix.matrice.precarite'
    _description = 'Matrice de précarité'

    name = fields.Char(string='Nom', required=True)
    date_debut = fields.Date(string='Date de début de validité')
    date_fin = fields.Date(string='Date de fin de validité')
    active = fields.Boolean(string='Actif', default=True)
    ligne_ids = fields.One2many(
        'ibatix.matrice.precarite.ligne', 'matrice_id', string='Lignes')


class IbatixMatricePrecariteLigne(models.Model):
    _name = 'ibatix.matrice.precarite.ligne'
    _description = 'Ligne de la matrice de précarité'
    _order = 'zone, nb_personnes'

    matrice_id = fields.Many2one(
        'ibatix.matrice.precarite', string='Matrice',
        required=True, ondelete='cascade')
    zone = fields.Selection([
        ('idf', 'Île-de-France'),
        ('hors_idf', 'Hors IDF + Outre-mer'),
    ], string='Zone géographique', required=True)
    nb_personnes = fields.Integer(string='Nombre de personnes', required=True)
    plafond_tres_modeste = fields.Float(string='Très modeste (€)', digits=(10, 0))
    plafond_modeste = fields.Float(string='Modeste (€)', digits=(10, 0))
    plafond_intermediaire = fields.Float(string='Intermédiaire (€)', digits=(10, 0))
