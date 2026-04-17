from odoo import api, fields, models


class IbatixOperationCee(models.Model):
    _name = 'ibatix.operation.cee'
    _description = 'Opération CEE standardisée'
    _order = 'code'
    _rec_names_search = ['code', 'name']

    code = fields.Char(string='Code', required=True, index=True)
    name = fields.Char(string='Intitulé', required=True)
    secteur = fields.Selection([
        ('agri', 'Agriculture'),
        ('bar', 'Résidentiel'),
        ('bat', 'Tertiaire'),
        ('ind', 'Industrie'),
        ('res', 'Réseau'),
        ('tra', 'Transport'),
    ], string='Secteur', required=True)
    active = fields.Boolean(string='Actif', default=True)
    fiche_pdf = fields.Binary(string='Fiche PDF', attachment=True)
    fiche_pdf_filename = fields.Char(string='Nom du fichier PDF')
    fiche_date_validite = fields.Date(string='Valide à compter du')

    @api.depends('code', 'name')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.code} — {rec.name}" if rec.code and rec.name else rec.code or rec.name or ''

    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', 'Le code opération CEE doit être unique.'),
    ]
