def _map_list(data: list, model):
    _liste = []
    if not data:
        return _liste

    for item in data:
        _liste.append(model(item))
    return _liste


class HealthCheckResponse:
    def __init__(self, json_response: dict):
        self.body = json_response.get('body')
        self.status_code_value = json_response.get('statusCodeValue')
        self.status_code = json_response.get('statusCode')


class AnnuaireDestinataireResponse:
    def __init__(self, json_response: dict):
        self.code_retour = json_response.get('codeRetour')
        self.fichier_resultat = json_response.get('fichierResultat')
        self.libelle = json_response.get('libelle')


class DeposerFluxResponse:
    def __init__(self, json_response: dict):
        self.code_retour = json_response.get('codeRetour')
        self.date_depot = json_response.get('dateDepot')
        self.libelle = json_response.get('libelle')
        self.numero_flux_depot = json_response.get('numeroFluxDepot')
        self.syntaxe_flux = json_response.get('syntaxeFlux')


class ListeErreurDP:
    def __init__(self, data: dict):
        self.identifiant_destinataire = data.get("identifiantDestinataire")
        self.identifiant_fournisseur = data.get("identifiantFournisseur")
        self.libelle_erreur_dP = data.get("libelleErreurDP")
        self.numero_dp = data.get("numeroDP")


class ListeErreurTechnique:
    def __init__(self, data: dict):
        self.code_erreur = data.get("codeErreur")
        self.libelle_erreur = data.get("libelleErreur")
        self.nature_erreur = data.get("natureErreur")


class ConsulterCrResponse:
    def __init__(self, json_response: dict):
        self.code_appli_partenaire = json_response.get('codeAppliPartenaire')
        self.code_interface_flux = json_response.get('codeInterfaceFlux')
        self.code_retour = json_response.get('codeRetour')
        self.date_depot_flux = json_response.get('dateDepotFlux')
        self.date_heure_etat_courant_flux = json_response.get('dateHeureEtatCourantFlux')
        self.designation_partenaire = json_response.get('designationPartenaire')
        self.etat_courant_flux = json_response.get('etatCourantFlux')
        self.fichier_cr = json_response.get('fichierCR')
        self.libelle = json_response.get('libelle')
        self.nom_fichier_flux = json_response.get('nomFichierFlux')
        self.numero_flux_depot = json_response.get('numeroFluxDepot')


class ConsulterCrDetailleResponse:
    def __init__(self, json_response: dict):
        self.code_retour = json_response.get("codeRetour")
        self.libelle = json_response.get("libelle")
        self.nomFichier = json_response.get("nomFichier")
        self.date_depot_flux = json_response.get("dateDepotFlux")
        self.code_interface_depot_flux = json_response.get("codeInterfaceDepotFlux")
        self.etat_courant_depot_flux = json_response.get("etatCourantDepotFlux")
        self.date_heure_etat_courant_flux = json_response.get("dateHeureEtatCourantFlux")
        self.liste_erreur_dp = _map_list(json_response.get("listeErreurDP"), ListeErreurDP)
        self.liste_erreur_technique = _map_list(json_response.get("listeErreurTechnique"), ListeErreurTechnique)


class InformationSiretResponse:
    def __init__(self, json_response: dict):
        self.adresse = json_response.get("adresse")
        self.categorie_entreprise = json_response.get("categorieEntreprise")
        self.categorie_juridique = json_response.get("categorieJuridique")
        self.civilite = json_response.get("civilite")
        self.code_retour = json_response.get("codeRetour")
        self.date_creation_entreprise = json_response.get("dateCreationEntreprise")
        self.date_creation_etablissement = json_response.get("dateCreationEtablissement")
        self.date_reactivation_etablissement = json_response.get("dateReactivationEtablissement")
        self.estActif = json_response.get("estActif")
        self.libelle = json_response.get("libelle")
        self.localisation_siege = json_response.get("localisationSiege")
        self.non_diffusible_insee = json_response.get("nonDiffusibleInsee")
        self.numero_interne_classement = json_response.get("numeroInterneClassement")
        self.raison_sociale = json_response.get("raisonSociale")
        self.siege = json_response.get("siege")
        self.siren = json_response.get("siren")
        self.siret = json_response.get("siret")
        self.siret_predecesseur_successeur = json_response.get("siretPredecesseurSuccesseur")


class RechercheResponse:
    def __init__(self, json_response: dict):
        self.code_retour = json_response.get("codeRetour")
        self.libelle = json_response.get("libelle")


class ListeStructures:
    def __init__(self, data: dict):
        self.id_structure_cpp = data.get("idStructureCPP")
        self.type_identifiant_structure = data.get("typeIdentifiantStructure")
        self.identifiant_structure = data.get("identifiantStructure")
        self.designation_structure = data.get("designationStructure")
        self.statut = data.get("statut")


class RechercheStructureResponse(RechercheResponse):
    def __init__(self, json_response: dict):
        super().__init__(json_response)
        self.liste_structures = _map_list(json_response.get("listeStructures"), ListeStructures)


class ListeServices:
    def __init__(self, data: dict):
        self.code_service = data.get("codeService")
        self.est_actif = data.get("estActif")
        self.id_service = data.get("idService")
        self.libelle_service = data.get("libelleService")
        self.statut_service = data.get("statutService")


class RechercheServiceResponse(RechercheResponse):
    def __init__(self, json_response: dict):
        super().__init__(json_response)
        self.liste_structures = _map_list(json_response.get("listeServices"), ListeServices)


class ListeFactures:
    def __init__(self, data: dict):
        self.identifiant_facture_cpp = data.get("identifiantFactureCPP")
        self.type_demande_paiement = data.get("typeDemandePaiement")
        self.code_fournisseur = data.get("codeFournisseur")
        self.type_identifiant_fournisseur = data.get("typeIdentifiantFournisseur")
        self.designation_fournisseur = data.get("designationFournisseur")
        self.id_destinataire = data.get("idDestinataire")
        self.code_destinataire = data.get("codeDestinataire")
        self.designation_destinataire = data.get("designationDestinataire")
        self.type_facture = data.get("typeFacture")
        self.numero_facture = data.get("numeroFacture")
        self.date_facture = data.get("dateFacture")
        self.date_depot = data.get("dateDepot")
        self.montant_ht = data.get("montantHT")
        self.montant_ttc = data.get("montantTTC")
        self.montant_a_payer = data.get("montantAPayer")
        self.devise = data.get("devise")
        self.statut = data.get("statut")
        self.numero_flux_depot = data.get("numeroFluxDepot")
        self.mode_depot = data.get("modeDepot")
        self.nom_prenom_utilisateur_createur = data.get("nomPrenomUtilisateurCreateur")
        self.taille = data.get("taille")
        self.dateHeure_etat_courant = data.get("dateHeureEtatCourant")
        self.rejet_traite = data.get("rejetTraite")


class RechercheFactureResponse(RechercheResponse):
    def __init__(self, json_response: dict):
        super().__init__(json_response)
        self.liste_factures = _map_list(json_response.get("listeFactures"), ListeFactures)


class ListeDevises:
    def __init__(self, data: dict):
        self.code_devise = data.get("codeDevise")
        self.libelle_devise = data.get("libelleDevise")


class RecupererDevisesResponse(RechercheResponse):
    def __init__(self, json_response: dict):
        super().__init__(json_response)
        self.liste_devises = _map_list(json_response.get("listeDevises"), ListeDevises)


class AdressePostaleDuSiege:
    def __init__(self, data: dict):
        self.adresse = data.get("adresse")
        self.code_postal = data.get("codePostal")
        self.complement_adresse_1 = data.get("complementAdresse1")
        self.complement_adresse_2 = data.get("complementAdresse2")
        self.fax = data.get("fax")
        self.indicatif_fax = data.get("indicatifFax")
        self.indicatif_telephone = data.get("indicatifTelephone")
        self.pays = data.get("pays")
        self.telephone = data.get("telephone")
        self.ville = data.get("ville")


class ListeStructureDupliquees:
    def __init__(self, data: dict):
        self.structure_dupliquee = data.get("structureDupliquee")


class InformationGenerales:
    def __init__(self, data: dict):
        self.date_expiration_mot_passe_compte_tech = data.get("dateExpirationMotPasseCompteTech")
        self.email_structure = data.get("emailStructure")
        self.est_valideur_deleguee = data.get("estValideurDeleguee")
        self.id_structure_cpp = data.get("idStructureCPP")
        self.id_structure_origine = data.get("idStructureOrigine")
        self.identifiant_structure = data.get("identifiantStructure")
        self.libelle_structure = data.get("libelleStructure")

        self.liste_structure_dupliquees = _map_list(data.get("listeStructureDupliquees"), ListeStructureDupliquees)

        self.nom_structure = data.get("nomStructure")
        self.numero_rcs_structure = data.get("numeroRcsStructure")
        self.numero_tva = data.get("numeroTVA")
        self.prenom_structure = data.get("prenomStructure")
        self.raison_sociale_structure = data.get("raisonSocialeStructure")
        self.structure_privee_publique = data.get("structurePriveePublique")
        self.type_identifiant_structure = data.get("typeIdentifiantStructure")


class Parametres:
    def __init__(self, data: dict):
        self.code_service_doit_etre_renseigne = data.get("codeServiceDoitEtreRenseigne")
        self.connexion_edi = data.get("connexionEDI")
        self.est_moa_uniquement = data.get("estMoaUniquement")
        self.est_valideur_delegue = data.get("estValideurDelegue")
        self.gestion_numero_ej_ou_code_service = data.get("gestionNumeroEJOuCodeService")
        self.get_amoa = data.get("aMoa")
        self.non_diffusible_insee = data.get("nonDiffusibleInsee")
        self.numero_ej_doit_etre_renseigne = data.get("numeroEJDoitEtreRenseigne")
        self.recevoir_donnees_via_edi = data.get("recevoirDonneesViaEDI")
        self.statut_mise_en_paiement_nest_pas_remonte = data.get("statutMiseEnPaiementNestPasRemonte")


class ConsulterStructureResponse(RechercheResponse):
    def __init__(self, json_response: dict):
        super().__init__(json_response)
        self.adresse_postale_du_siege = AdressePostaleDuSiege(json_response.get("adressePostaleDuSiege", {}))
        self.information_generales = InformationGenerales(json_response.get("informationGenerales", {}))
        self.parametres = Parametres(json_response.get("parametres", {}))
