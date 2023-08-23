class FluxCode:
    def __init__(self, code, description):
        """
        Retourne le code associé et la description du code
        """
        self.code = code
        self.description = description


class EtatCourantFlux:
    """
    Le service ConsulterCR permet de consulter les informations liées au dépôt d'un flux et de récupérer au format
    PDF le compte rendu de traitement du flux déposé via le portail ou le service exposé DeposerFluxFacture.
    """

    IN_RECU = FluxCode("IN_RECU", "Le flux a été reçu par Chorus Pro")

    IN_TRAITE_SE_CPP = FluxCode("IN_TRAITE_SE_CPP", "Le fichier arrivé dans le système d’échange Chorus Pro")

    IN_EN_ATTENTE_TRAITEMENT_CPP = FluxCode("IN_EN_ATTENTE_TRAITEMENT_CPP", "Le flux est en liste d’attente")

    IN_EN_COURS_TRAITEMENT_CPP = FluxCode("IN_EN_COURS_TRAITEMENT_CPP", "Le flux est en cours de traitement")

    IN_INCIDENTE = FluxCode("IN_INCIDENTE", "Flux non traité par le système d’échange, "
                                            "il sera nécessaire de reprendre le flux intégralement.")

    IN_REJETE = FluxCode("IN_REJETE", "Le flux a été traité mais rejeté car il comporte des anomalies")

    IN_EN_ATTENTE_RETRAITEMENT_CPP = FluxCode("IN_EN_ATTENTE_RETRAITEMENT_CPP",
                                              "Le flux a été bloqué, il attend une reprise manuelle")

    IN_INTEGRE = FluxCode("IN_INTEGRE", "Le flux a été traité et tout a été intégré dans Chorus Pro.")

    IN_INTEGRE_PARTIEL = FluxCode("IN_INTEGRE_PARTIEL", "Cela concerne des flux qui sont en rejet partiel, "
                                                        "seules les factures correctes sont intégrées.")
