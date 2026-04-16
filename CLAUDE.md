# Objets IBATIX — Cahier des charges

## Contexte
IBATIX est un logiciel destiné aux professionnels de la rénovation énergétique. Il permet de réaliser des devis intégrant automatiquement le calcul des primes CEE (Certificats d'Économies d'Énergie) et des aides MaPrimeRénov', en se basant sur le profil du client et les dispositifs gouvernementaux en cours.

Ce module a pour rôle de répertorier les objets de référence nécessaires aux calculs de primes dans Odoo. Ces objets n'existent pas nativement dans Odoo.

## Objectif du module
Fournir un registre des entités de référence (délégataires, mandataires, médiateurs, etc.) utilisées dans les étapes de calcul des primes CEE et MaPrimeRénov' au sein des devis IBATIX.

## Fonctionnalités attendues
- Gestion des 8 objets de référence IBATIX
- Saisie et consultation des fiches par objet
- Liaison entre objets (ex : Délégataire CEE → Médiateur)
- Matrice de précarité annuelle duplicable d'une année sur l'autre
- Vues liste et formulaire pour chaque objet

## Modèles de données

### 1. Mandataire ANAH (`ibatix.mandataire.anah`)
Représentant habilité pour les dossiers d'aides ANAH (Agence Nationale de l'Habitat).

**Section Informations du gérant :**

| Champ | Type | Description |
|-------|------|-------------|
| name | Char | Nom du mandataire (ex : SONERGIA) |
| prenom | Char | Prénom du gérant |
| nom_gerant | Char | Nom du gérant |
| titre | Selection | Titre (Monsieur / Madame) |
| email | Char | Email |
| mobile | Char | Mobile |
| street | Char | Adresse (rue) |
| city | Char | Ville |
| zip | Char | Code postal |

**Section Propriétés :**

| Champ | Type | Description |
|-------|------|-------------|
| representant_administratif | Boolean | Représentant administratif |
| representant_financier | Boolean | Représentant financier |
| is_default | Boolean | Est par défaut |
| signature_image | Binary | Image de signature |

---

### 2. Délégataire CEE (`ibatix.delegataire.cee`)
Organisme délégataire dans le cadre du dispositif CEE. Modèle riche avec 4 onglets.

**Champs principaux :**

| Champ | Type | Description |
|-------|------|-------------|
| name | Char | Nom |
| company | Char | Société |
| mediateur_id | Many2one | Médiateur (→ ibatix.mediateur.cee) |
| street | Char | Rue |
| city | Char | Ville |
| zip | Char | Code postal |
| phone | Char | Téléphone |
| website | Char | Site Web |
| siren | Char | SIREN |
| siret | Char | SIRET |
| is_default | Boolean | Contrat par défaut |
| logo_rge | Binary | Logo / Image RGE |

**Onglet Opérations (`ibatix.delegataire.operation` — One2many) :**

| Champ | Type | Description |
|-------|------|-------------|
| code | Char | Code opération CEE (ex : BAR-TH-171) |
| cumac_classique | Float | Évaluation Cumac Classique (MWhc) |
| cumac_precaire | Float | Évaluation Cumac Précaire (MWhc) |
| cumac_total | Float | Évaluation Cumac Total (MWhc) |

**Onglet Multi-contrat (`ibatix.delegataire.contrat` — One2many) :**

| Champ | Type | Description |
|-------|------|-------------|
| numero_contrat | Char | Numéro de contrat |
| objectif | Float | Objectif (montant) |
| date_debut | Date | Date de début |
| date_fin | Date | Date de fin |
| valo_precaire_reelle | Float | Valorisation Précaire Réelle |
| valo_precaire_client | Float | Valorisation Précaire Client |
| diff_precaire | Float | Différence Précaire |
| valo_classique_reelle | Float | Valorisation Classique Réelle |
| valo_classique_client | Float | Valorisation Classique Client |
| diff_classique | Float | Différence Classique |

**Onglet Mentions et réductions :**

| Champ | Type | Description |
|-------|------|-------------|
| citation_mention_totale | Selection | Mention totale — Citation |
| citation_mention_corps | Text | Mention du corps — Citation (variable `{primeCee}`) |
| facture_mention_totale | Selection | Mention totale — Facture d'achat |
| facture_mention_corps | Text | Mention du corps — Facture d'achat (variable `{primeCee}`) |

**Onglet Rapport :**

| Champ | Type | Description |
|-------|------|-------------|
| exige_manuscrit | Boolean | Exige manuscrit |
| modele_rapport_id | Many2one | Modèle de rapport |
| signature_image | Binary | Image de signature |
| mentions_finales_ah | Html | Mentions finales AH |

---

### 3. Médiateur CEE (`ibatix.mediateur.cee`)

| Champ | Type | Description |
|-------|------|-------------|
| name | Char | Nom |
| street | Char | Rue |
| city | Char | Ville |
| zip | Char | Code postal |
| phone | Char | Téléphone |
| email | Char | Email |
| lien_formulaire | Char | Lien formulaire du contact (URL) |
| website | Char | Site Web |
| is_default | Boolean | Est par défaut |

---

### 4. Cofrac (`ibatix.cofrac`)
Organisme d'accréditation (Comité Français d'Accréditation).

| Champ | Type | Description |
|-------|------|-------------|
| name | Char | Nom |
| logo | Binary | Logo / Image |
| street | Char | Rue |
| city | Char | Ville |
| zip | Char | Code postal |
| email | Char | Email |
| mobile | Char | Mobile |
| siren | Char | SIREN |
| cofrac | Char | Numéro d'accréditation COFRAC |
| date_fin_certificat | Date | Date de fin du certificat |
| is_default | Boolean | Est par défaut |

---

### 5. Gestionnaire de réseau (`ibatix.gestionnaire.reseau`)

| Champ | Type | Description |
|-------|------|-------------|
| name | Char | Nom |
| logo | Binary | Logo / Image |
| street | Char | Rue |
| city | Char | Ville |
| zip | Char | Code postal |
| email | Char | Email |
| mobile | Char | Mobile |
| siren | Char | SIREN |
| siret | Char | SIRET |

---

### 6. Matrice de précarité (`ibatix.matrice.precarite`)
Barème annuel des plafonds de ressources pour la classification des ménages (CEE / MaPrimeRénov').
Source : Guide des aides financières ANAH — mis à jour chaque année au 1er janvier.

**Modèle principal :**

| Champ | Type | Description |
|-------|------|-------------|
| name | Char | Nom (ex : "Matrice 2026") |
| date_debut | Date | Date de début de validité |
| date_fin | Date | Date de fin de validité |
| active | Boolean | Actif |

**Lignes (`ibatix.matrice.precarite.ligne` — One2many) :**

| Champ | Type | Description |
|-------|------|-------------|
| zone | Selection | Zone géographique : `idf` (Île-de-France) / `hors_idf` (Hors IDF + Outre-mer) |
| nb_personnes | Integer | Nombre de personnes dans le ménage |
| plafond_tres_modeste | Float | Plafond revenus très modestes (€) |
| plafond_modeste | Float | Plafond revenus modestes (€) |
| plafond_intermediaire | Float | Plafond revenus intermédiaires (€) |

> Le niveau **Supérieur** correspond aux revenus au-dessus du seuil intermédiaire (pas de plafond).
> La matrice peut être dupliquée d'une année sur l'autre via le bouton natif Odoo "Dupliquer".

**Valeurs de référence au 1er janvier 2026 :**

| Personnes | Très modeste (IDF) | Modeste (IDF) | Intermédiaire (IDF) |
|-----------|-------------------|---------------|---------------------|
| 1 | 24 031 € | 29 253 € | 40 851 € |
| 2 | 35 270 € | 42 933 € | 60 051 € |
| 3 | 42 357 € | 51 564 € | 71 846 € |
| 4 | 49 455 € | 60 208 € | 84 562 € |
| 5 | 56 580 € | 68 877 € | 96 817 € |
| + par pers. | +7 116 € | +8 663 € | +12 257 € |

| Personnes | Très modeste (Hors IDF) | Modeste (Hors IDF) | Intermédiaire (Hors IDF) |
|-----------|------------------------|-------------------|--------------------------|
| 1 | 17 363 € | 22 259 € | 31 185 € |
| 2 | 25 393 € | 32 553 € | 45 842 € |
| 3 | 30 540 € | 39 148 € | 55 196 € |
| 4 | 35 676 € | 45 735 € | 64 550 € |
| 5 | 40 835 € | 52 348 € | 73 907 € |

---

### 7. Auditeur (`ibatix.auditeur`)

| Champ | Type | Description |
|-------|------|-------------|
| name | Char | Nom |
| avatar | Binary | Photo / Avatar |
| street | Char | Rue |
| city | Char | Ville |
| zip | Char | Code postal |
| email | Char | Email |
| mobile | Char | Mobile |
| representant_legal | Char | Représentant Légal |
| nom_societe | Char | Nom de la société |
| siren | Char | SIREN |
| siret | Char | SIRET |
| certificat | Char | Certificat |
| is_default | Boolean | Est par défaut |
| signature_image | Binary | Image de signature |

---

### 8. Installateur (`equipment.installer`)
Entreprise réalisant les travaux de rénovation énergétique. Modèle riche avec 2 onglets.

**Champs principaux :**

| Champ | Type | Description |
|-------|------|-------------|
| name | Char | Nom de la société |
| logo | Binary | Logo |
| street | Char | Rue |
| city | Char | Ville |
| zip | Char | Code postal |
| country_id | Many2one | Pays (→ res.country) |
| phone | Char | Téléphone |
| mobile | Char | Mobile |
| email | Char | Email |
| website | Char | Site Web |
| siren | Char | SIREN |
| siret | Char | SIRET |
| legal_representative_id | Many2one | Représentant Légal (→ res.partner) |
| partner_id | Many2one | Partenaire (→ res.partner) |
| company_id | Many2one | Société (→ res.company) |
| is_default | Boolean | Est par défaut |
| is_subcontractor | Boolean | Est sous-traitant |
| signature_image | Binary | Image de signature |
| fix_period | Integer | Période de levée de réserve (jours) |
| fix_comment | Text | Commentaire de fix |
| sequence | Integer | Séquence |

**Onglet Assurances (`installer.insurance` — One2many) :**

| Champ | Type | Description |
|-------|------|-------------|
| name | Char | Nom |
| start_date | Date | Date de début |
| end_date | Date | Date de fin |
| duration | Integer | Durée (en jours) |

**Onglet Qualifications (`qualification` — One2many) :**

| Champ | Type | Description |
|-------|------|-------------|
| name | Char | Nom |
| start_date | Date | Date de début |
| end_date | Date | Date de fin |
| duration | Integer | Durée (en jours) |
| qualification_file | Binary | Certificat PDF |
| public_url | Char | Lien URL public |
| is_api | Boolean | Via l'API |
| is_downloaded | Boolean | Enregistré comme pièce jointe |

---

## Vues et interface

### Vues par objet

| Objet | Vue liste | Vue formulaire | Particularités |
|-------|-----------|----------------|----------------|
| Mandataire ANAH | oui | oui | 2 sections : Informations du gérant / Propriétés |
| Délégataire CEE | oui | oui | 4 onglets : Opérations, Multi-contrat, Mentions et réductions, Rapport |
| Médiateur CEE | oui | oui | Formulaire simple |
| Cofrac | oui | oui | Formulaire simple |
| Gestionnaire de réseau | oui | oui | Formulaire simple |
| Matrice de précarité | oui | oui | Tableau One2many groupé par zone |
| Auditeur | oui | oui | Formulaire simple |
| Installateur | oui | oui | 2 onglets : Assurances, Qualifications |

### Structure des menus

```
IBATIX  (menu principal — barre de navigation)
  └── Configuration
        ├── Mandataires ANAH
        ├── Délégataires CEE
        ├── Médiateurs CEE
        ├── Cofrac
        ├── Gestionnaires de réseau
        ├── Matrices de précarité
        ├── Auditeurs
        └── Installateurs
```

## Sécurité et accès
- Tous les utilisateurs internes Odoo (`base.group_user`) ont les droits **lecture, écriture, création et suppression** sur l'ensemble des objets du module.
- Aucune restriction par groupe spécifique.

## Contraintes techniques
- Odoo version : 19
- Dépendances actuelles : `product`, `stock`
- Auteur : ibatix

## Statut du développement

### Fait
- Structure initiale du module (manifest, models, views, security, wizard)
- Cahier des charges complet (8 modèles documentés)

### À faire
- Créer les 8 modèles de données
- Créer les vues liste et formulaire pour chaque modèle
- Configurer les droits d'accès (`ir.model.access.csv`)
- Créer les menus de navigation
