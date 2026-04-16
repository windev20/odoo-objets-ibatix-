from odoo import fields, models


class IbatixDelegataireeCee(models.Model):
    _name = 'ibatix.delegataire.cee'
    _description = 'Délégataire CEE'

    name = fields.Char(string='Nom', required=True)
    company = fields.Char(string='Société')
    mediateur_id = fields.Many2one('ibatix.mediateur.cee', string='Médiateur')
    street = fields.Char(string='Rue')
    city = fields.Char(string='Ville')
    zip = fields.Char(string='Code postal')
    phone = fields.Char(string='Téléphone')
    website = fields.Char(string='Site Web')
    siren = fields.Char(string='SIREN')
    siret = fields.Char(string='SIRET')
    is_default = fields.Boolean(string='Contrat par défaut')
    logo_rge = fields.Binary(string='Logo / Image RGE')

    operation_ids = fields.One2many(
        'ibatix.delegataire.operation', 'delegataire_id', string='Opérations')
    contrat_ids = fields.One2many(
        'ibatix.delegataire.contrat', 'delegataire_id', string='Contrats')

    # Onglet Mentions et réductions
    citation_mention_totale = fields.Selection([
        ('deduction_mention', 'Déduction et mention'),
    ], string='Mention totale — Citation')
    citation_mention_corps = fields.Text(string='Mention du corps — Citation')
    facture_mention_totale = fields.Selection([
        ('deduction_mention', 'Déduction et mention'),
    ], string="Mention totale — Facture d'achat")
    facture_mention_corps = fields.Text(string="Mention du corps — Facture d'achat")

    # Onglet Rapport
    exige_manuscrit = fields.Boolean(string='Exige manuscrit')
    modele_rapport_id = fields.Many2one('ir.actions.report', string='Modèle de rapport')
    signature_image = fields.Binary(string='Image de signature')
    mentions_finales_ah = fields.Html(string='Mentions finales AH', sanitize=True)


class IbatixDelegataireOperation(models.Model):
    _name = 'ibatix.delegataire.operation'
    _description = 'Opération CEE du Délégataire'

    delegataire_id = fields.Many2one(
        'ibatix.delegataire.cee', string='Délégataire',
        required=True, ondelete='cascade')
    code = fields.Char(string='Code opération CEE')
    cumac_classique = fields.Float(string='Cumac Classique (MWhc)')
    cumac_precaire = fields.Float(string='Cumac Précaire (MWhc)')
    cumac_total = fields.Float(string='Cumac Total (MWhc)')


class IbatixDelegataireContrat(models.Model):
    _name = 'ibatix.delegataire.contrat'
    _description = 'Contrat du Délégataire CEE'

    delegataire_id = fields.Many2one(
        'ibatix.delegataire.cee', string='Délégataire',
        required=True, ondelete='cascade')
    numero_contrat = fields.Char(string='Numéro de contrat')
    objectif = fields.Float(string='Objectif')
    date_debut = fields.Date(string='Date de début')
    date_fin = fields.Date(string='Date de fin')
    valo_precaire_reelle = fields.Float(string='Valorisation Précaire Réelle')
    valo_precaire_client = fields.Float(string='Valorisation Précaire Client')
    diff_precaire = fields.Float(string='Différence Précaire')
    valo_classique_reelle = fields.Float(string='Valorisation Classique Réelle')
    valo_classique_client = fields.Float(string='Valorisation Classique Client')
    diff_classique = fields.Float(string='Différence Classique')
