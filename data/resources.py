
def get_all_resources():
    """
    Returns all resources and useful links
    """
    resources = [
        {
            "category": "Ressources Gouvernementales Officielles",
            "resources": [
                {
                    "title": "Direction Générale des Impôts (DGI)",
                    "description": "Le site officiel de l'Administration Fiscale Marocaine fournissant les lois fiscales, les réglementations, les formulaires et les services en ligne.",
                    "url": "https://www.tax.gov.ma/",
                    "icon": "fa-solid fa-landmark"
                },
                {
                    "title": "Office Marocain de la Propriété Industrielle et Commerciale (OMPIC)",
                    "description": "Organisme officiel pour l'enregistrement des entreprises et la propriété intellectuelle au Maroc.",
                    "url": "https://www.ompic.ma/",
                    "icon": "fa-solid fa-building"
                },
                {
                    "title": "Trésorerie Générale du Royaume",
                    "description": "La Trésorerie Générale du Royaume du Maroc fournit des informations sur les finances publiques et la comptabilité gouvernementale.",
                    "url": "https://www.tgr.gov.ma/",
                    "icon": "fa-solid fa-money-bill-transfer"
                },
                {
                    "title": "Ministère de l'Economie et des Finances",
                    "description": "Site du Ministère de l'Économie et des Finances du Maroc avec les politiques économiques et les rapports.",
                    "url": "https://www.finances.gov.ma/",
                    "icon": "fa-solid fa-money-bill-trend-up"
                }
            ]
        },
        {
            "category": "Ressources Comptables et Fiscales",
            "resources": [
                {
                    "title": "Conseil National de la Comptabilité (CNC)",
                    "description": "Le Conseil National de la Comptabilité qui établit les normes comptables au Maroc.",
                    "url": "https://www.finances.gov.ma/fr/Pages/CNC/conseil-national-comptabilite.aspx",
                    "icon": "fa-solid fa-book"
                },
                {
                    "title": "Ordre des Experts Comptables",
                    "description": "Organisation professionnelle des experts-comptables agréés au Maroc.",
                    "url": "https://www.oecmaroc.com/",
                    "icon": "fa-solid fa-calculator"
                },
                {
                    "title": "Code Général des Impôts",
                    "description": "Le Code Général des Impôts du Maroc (dernière édition).",
                    "url": "https://www.tax.gov.ma/wps/portal/DGI/Documentation-fiscale/Code-general-des-impots",
                    "icon": "fa-solid fa-file-contract"
                },
                {
                    "title": "SIMPL - Services des Impôts en Ligne",
                    "description": "Plateforme de services fiscaux en ligne pour la déclaration électronique des impôts.",
                    "url": "https://simpl.tax.gov.ma/",
                    "icon": "fa-solid fa-laptop"
                }
            ]
        },
        {
            "category": "Organisations de Soutien aux Entreprises",
            "resources": [
                {
                    "title": "Confédération Générale des Entreprises du Maroc (CGEM)",
                    "description": "L'organisation représentative principale des entreprises du secteur privé au Maroc.",
                    "url": "https://www.cgem.ma/",
                    "icon": "fa-solid fa-handshake"
                },
                {
                    "title": "Agence Marocaine de Développement des Investissements (AMDI)",
                    "description": "L'Agence Marocaine de Développement des Investissements fournissant des informations aux investisseurs.",
                    "url": "https://www.amdie.gov.ma/",
                    "icon": "fa-solid fa-chart-line"
                },
                {
                    "title": "Centres Régionaux d'Investissement (CRI)",
                    "description": "Centres Régionaux d'Investissement offrant un soutien à la création d'entreprise et à l'investissement.",
                    "url": "https://www.cri-invest.ma/",
                    "icon": "fa-solid fa-briefcase"
                },
                {
                    "title": "Maroc PME",
                    "description": "Agence nationale de soutien aux petites et moyennes entreprises au Maroc.",
                    "url": "https://www.marocpme.gov.ma/",
                    "icon": "fa-solid fa-store"
                }
            ]
        },
        {
            "category": "Ressources Juridiques",
            "resources": [
                {
                    "title": "Secrétariat Général du Gouvernement - Législation",
                    "description": "Dépositaire officiel des lois et règlements marocains.",
                    "url": "https://www.sgg.gov.ma/",
                    "icon": "fa-solid fa-gavel"
                },
                {
                    "title": "Code de Commerce",
                    "description": "Le Code de Commerce du Maroc.",
                    "url": "https://www.wipo.int/edocs/lexdocs/laws/fr/ma/ma005fr.pdf",
                    "icon": "fa-solid fa-balance-scale"
                },
                {
                    "title": "Bulletin Officiel",
                    "description": "Le Bulletin Officiel où sont publiées les nouvelles lois et réglementations.",
                    "url": "https://www.sgg.gov.ma/BulletinOfficiel.aspx",
                    "icon": "fa-solid fa-newspaper"
                },
                {
                    "title": "CABINETBASSAMAT & Associée",
                    "description": "Ressources juridiques et mises à jour sur le droit des affaires marocain.",
                    "url": "https://www.cabinetbassamat.com/",
                    "icon": "fa-solid fa-scale-balanced"
                }
            ]
        },
        {
            "category": "Informations Financières",
            "resources": [
                {
                    "title": "Bank Al-Maghrib",
                    "description": "La Banque Centrale du Maroc avec des informations sur la politique monétaire et les rapports économiques.",
                    "url": "https://www.bkam.ma/",
                    "icon": "fa-solid fa-bank"
                },
                {
                    "title": "Bourse de Casablanca",
                    "description": "La Bourse de Casablanca avec les données du marché et les informations sur les sociétés cotées.",
                    "url": "https://www.casablanca-bourse.com/",
                    "icon": "fa-solid fa-chart-simple"
                },
                {
                    "title": "Autorité Marocaine du Marché des Capitaux (AMMC)",
                    "description": "L'Autorité Marocaine du Marché des Capitaux avec les réglementations et la supervision du marché.",
                    "url": "https://www.ammc.ma/",
                    "icon": "fa-solid fa-shield-halved"
                },
                {
                    "title": "Haut Commissariat au Plan",
                    "description": "Le Haut Commissariat au Plan du Maroc avec les statistiques économiques et sociales.",
                    "url": "https://www.hcp.ma/",
                    "icon": "fa-solid fa-chart-pie"
                }
            ]
        },
        {
            "category": "Ressources Éducatives",
            "resources": [
                {
                    "title": "Plan Comptable Marocain (PCM)",
                    "description": "Informations détaillées sur la structure et l'utilisation du Plan Comptable Marocain.",
                    "url": "https://www.compta-maroc.com/plan-comptable-marocain/",
                    "icon": "fa-solid fa-list-ol"
                },
                {
                    "title": "Compta Maroc",
                    "description": "Portail éducatif avec des cours de comptabilité, des exemples et des explications pour la comptabilité marocaine.",
                    "url": "https://www.compta-maroc.com/",
                    "icon": "fa-solid fa-graduation-cap"
                },
                {
                    "title": "Comptazine",
                    "description": "Ressource pour les professionnels de la comptabilité avec des articles, forums et outils.",
                    "url": "https://www.comptazine.fr/",
                    "icon": "fa-solid fa-book-open"
                },
                {
                    "title": "Lexis Maroc",
                    "description": "Portail de ressources juridiques et comptables avec documentation et explications.",
                    "url": "https://www.lexismaroc.ma/",
                    "icon": "fa-solid fa-chalkboard-user"
                }
            ]
        },
        {
            "category": "Normes Internationales",
            "resources": [
                {
                    "title": "Normes Internationales d'Information Financière (IFRS)",
                    "description": "Le site officiel de la Fondation IFRS avec les normes et interprétations.",
                    "url": "https://www.ifrs.org/",
                    "icon": "fa-solid fa-globe"
                },
                {
                    "title": "International Accounting Standards Board (IASB)",
                    "description": "L'organisme de normalisation des IFRS avec les mises à jour et les exposés-sondages.",
                    "url": "https://www.ifrs.org/groups/international-accounting-standards-board/",
                    "icon": "fa-solid fa-earth-africa"
                },
                {
                    "title": "Fédération Internationale des Experts-Comptables (IFAC)",
                    "description": "Organisation mondiale de la profession comptable avec ressources et publications.",
                    "url": "https://www.ifac.org/",
                    "icon": "fa-solid fa-users"
                },
                {
                    "title": "Banque Mondiale - ROSC Comptabilité et Audit pour le Maroc",
                    "description": "Rapports sur l'Observation des Normes et Codes (ROSC) pour la comptabilité au Maroc.",
                    "url": "https://www.worldbank.org/en/country/morocco",
                    "icon": "fa-solid fa-building-columns"
                }
            ]
        }
    ]
    return resources
