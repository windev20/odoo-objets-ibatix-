from odoo import fields, models


class IbatixInstallateur(models.Model):
    _name = 'ibatix.installateur'
    _description = 'Installateur'

    name = fields.Char(string='Nom de la société', required=True)
    logo = fields.Binary(string='Logo')
    street = fields.Char(string='Rue')
    city = fields.Char(string='Ville')
    zip = fields.Char(string='Code postal')
    country_id = fields.Many2one('res.country', string='Pays')
    phone = fields.Char(string='Téléphone')
    mobile = fields.Char(string='Mobile')
    email = fields.Char(string='Email')
    website = fields.Char(string='Site Web')
    siren = fields.Char(string='SIREN')
    siret = fields.Char(string='SIRET')
    legal_representative_id = fields.Many2one('res.partner', string='Représentant Légal')
    partner_id = fields.Many2one('res.partner', string='Partenaire')
    company_id = fields.Many2one('res.company', string='Société')
    is_default = fields.Boolean(string='Est par défaut')
    is_subcontractor = fields.Boolean(string='Est sous-traitant')
    signature_image = fields.Binary(string='Image de signature')
    fix_period = fields.Integer(string='Période de levée de réserve (jours)')
    fix_comment = fields.Text(string='Commentaire de fix')
    sequence = fields.Integer(string='Séquence', default=10)

    assurance_ids = fields.One2many(
        'ibatix.installateur.assurance', 'installateur_id', string='Assurances')
    qualification_ids = fields.One2many(
        'ibatix.installateur.qualification', 'installateur_id', string='Qualifications')


class IbatixInstallateurAssurance(models.Model):
    _name = 'ibatix.installateur.assurance'
    _description = "Assurance de l'installateur"

    installateur_id = fields.Many2one(
        'ibatix.installateur', string='Installateur',
        required=True, ondelete='cascade')
    name = fields.Char(string='Nom')
    start_date = fields.Date(string='Date de début')
    end_date = fields.Date(string='Date de fin')
    duration = fields.Integer(string='Durée (en jours)')


class IbatixInstallateurQualification(models.Model):
    _name = 'ibatix.installateur.qualification'
    _description = "Qualification de l'installateur"
    _order = 'sequence, id'

    installateur_id = fields.Many2one(
        'ibatix.installateur', string='Installateur',
        required=True, ondelete='cascade')
    name = fields.Char(string='Nom')
    start_date = fields.Date(string='Date de début')
    end_date = fields.Date(string='Date de fin')
    duration = fields.Integer(string='Durée (en jours)')
    qualification_file = fields.Binary(string='Certificat PDF')
    qualification_filename = fields.Char(string='Nom du fichier')
    public_url = fields.Char(string='Lien URL public')
    numero_rge = fields.Char(string='Numéro RGE')
    nom_certificat = fields.Char(string='Libellé certificat')
    is_api = fields.Boolean(string="Via l'API")
    is_downloaded = fields.Boolean(string='Enregistré comme pièce jointe')
    sequence = fields.Integer(string='Séquence', default=10)
