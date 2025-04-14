"""
Resources and useful links data for Moroccan accounting
"""

def get_all_resources():
    """
    Returns all resources and useful links
    """
    resources = [
        {
            "category": "Official Government Resources",
            "resources": [
                {
                    "title": "Direction Générale des Impôts (DGI)",
                    "description": "The official website of the Moroccan Tax Authority providing tax laws, regulations, forms, and online services.",
                    "url": "https://www.tax.gov.ma/",
                    "icon": "fa-solid fa-landmark"
                },
                {
                    "title": "Office Marocain de la Propriété Industrielle et Commerciale (OMPIC)",
                    "description": "Official body for business registration and intellectual property in Morocco.",
                    "url": "https://www.ompic.ma/",
                    "icon": "fa-solid fa-building"
                },
                {
                    "title": "Trésorerie Générale du Royaume",
                    "description": "The General Treasury of the Kingdom of Morocco provides information on public finances and government accounting.",
                    "url": "https://www.tgr.gov.ma/",
                    "icon": "fa-solid fa-money-bill-transfer"
                },
                {
                    "title": "Ministère de l'Economie et des Finances",
                    "description": "Morocco's Ministry of Economy and Finance website with economic policies and reports.",
                    "url": "https://www.finances.gov.ma/",
                    "icon": "fa-solid fa-money-bill-trend-up"
                }
            ]
        },
        {
            "category": "Accounting & Taxation Resources",
            "resources": [
                {
                    "title": "Conseil National de la Comptabilité (CNC)",
                    "description": "The National Accounting Council that establishes accounting standards in Morocco.",
                    "url": "https://www.finances.gov.ma/fr/Pages/CNC/conseil-national-comptabilite.aspx",
                    "icon": "fa-solid fa-book"
                },
                {
                    "title": "Ordre des Experts Comptables",
                    "description": "Professional organization of certified public accountants in Morocco.",
                    "url": "https://www.oecmaroc.com/",
                    "icon": "fa-solid fa-calculator"
                },
                {
                    "title": "Code Général des Impôts",
                    "description": "The General Tax Code of Morocco (latest edition).",
                    "url": "https://www.tax.gov.ma/wps/portal/DGI/Documentation-fiscale/Code-general-des-impots",
                    "icon": "fa-solid fa-file-contract"
                },
                {
                    "title": "SIMPL - Services des Impôts en Ligne",
                    "description": "Online tax services platform for electronic filing of tax returns.",
                    "url": "https://simpl.tax.gov.ma/",
                    "icon": "fa-solid fa-laptop"
                }
            ]
        },
        {
            "category": "Business Support Organizations",
            "resources": [
                {
                    "title": "Confédération Générale des Entreprises du Maroc (CGEM)",
                    "description": "The main representative organization of private sector businesses in Morocco.",
                    "url": "https://www.cgem.ma/",
                    "icon": "fa-solid fa-handshake"
                },
                {
                    "title": "Agence Marocaine de Développement des Investissements (AMDI)",
                    "description": "Moroccan Investment Development Agency providing information for investors.",
                    "url": "https://www.amdie.gov.ma/",
                    "icon": "fa-solid fa-chart-line"
                },
                {
                    "title": "Centres Régionaux d'Investissement (CRI)",
                    "description": "Regional Investment Centers providing support for business creation and investment.",
                    "url": "https://www.cri-invest.ma/",
                    "icon": "fa-solid fa-briefcase"
                },
                {
                    "title": "Maroc PME",
                    "description": "National agency supporting small and medium enterprises in Morocco.",
                    "url": "https://www.marocpme.gov.ma/",
                    "icon": "fa-solid fa-store"
                }
            ]
        },
        {
            "category": "Legal Resources",
            "resources": [
                {
                    "title": "Secrétariat Général du Gouvernement - Législation",
                    "description": "Official repository of Moroccan laws and regulations.",
                    "url": "https://www.sgg.gov.ma/",
                    "icon": "fa-solid fa-gavel"
                },
                {
                    "title": "Code de Commerce",
                    "description": "The Commercial Code of Morocco.",
                    "url": "https://www.wipo.int/edocs/lexdocs/laws/fr/ma/ma005fr.pdf",
                    "icon": "fa-solid fa-balance-scale"
                },
                {
                    "title": "Bulletin Officiel",
                    "description": "The Official Bulletin where new laws and regulations are published.",
                    "url": "https://www.sgg.gov.ma/BulletinOfficiel.aspx",
                    "icon": "fa-solid fa-newspaper"
                },
                {
                    "title": "CABINETBASSAMAT & Associée",
                    "description": "Legal resources and updates on Moroccan business law.",
                    "url": "https://www.cabinetbassamat.com/",
                    "icon": "fa-solid fa-scale-balanced"
                }
            ]
        },
        {
            "category": "Financial Information",
            "resources": [
                {
                    "title": "Bank Al-Maghrib",
                    "description": "The Central Bank of Morocco with monetary policy information and economic reports.",
                    "url": "https://www.bkam.ma/",
                    "icon": "fa-solid fa-bank"
                },
                {
                    "title": "Bourse de Casablanca",
                    "description": "The Casablanca Stock Exchange with market data and listed companies information.",
                    "url": "https://www.casablanca-bourse.com/",
                    "icon": "fa-solid fa-chart-simple"
                },
                {
                    "title": "Autorité Marocaine du Marché des Capitaux (AMMC)",
                    "description": "The Moroccan Capital Market Authority with regulations and market oversight.",
                    "url": "https://www.ammc.ma/",
                    "icon": "fa-solid fa-shield-halved"
                },
                {
                    "title": "Haut Commissariat au Plan",
                    "description": "Morocco's High Commission for Planning with economic and social statistics.",
                    "url": "https://www.hcp.ma/",
                    "icon": "fa-solid fa-chart-pie"
                }
            ]
        },
        {
            "category": "Educational Resources",
            "resources": [
                {
                    "title": "Plan Comptable Marocain (PCM)",
                    "description": "Detailed information on the Moroccan Chart of Accounts structure and usage.",
                    "url": "https://www.compta-maroc.com/plan-comptable-marocain/",
                    "icon": "fa-solid fa-list-ol"
                },
                {
                    "title": "Compta Maroc",
                    "description": "Educational portal with accounting courses, examples, and explanations for Moroccan accounting.",
                    "url": "https://www.compta-maroc.com/",
                    "icon": "fa-solid fa-graduation-cap"
                },
                {
                    "title": "Comptazine",
                    "description": "Resource for accounting professionals with articles, forums, and tools.",
                    "url": "https://www.comptazine.fr/",
                    "icon": "fa-solid fa-book-open"
                },
                {
                    "title": "Lexis Maroc",
                    "description": "Legal and accounting resource portal with documentation and explanations.",
                    "url": "https://www.lexismaroc.ma/",
                    "icon": "fa-solid fa-chalkboard-user"
                }
            ]
        },
        {
            "category": "International Standards",
            "resources": [
                {
                    "title": "International Financial Reporting Standards (IFRS)",
                    "description": "The official website of the IFRS Foundation with standards and interpretations.",
                    "url": "https://www.ifrs.org/",
                    "icon": "fa-solid fa-globe"
                },
                {
                    "title": "International Accounting Standards Board (IASB)",
                    "description": "The standard-setting body for IFRS with updates and exposure drafts.",
                    "url": "https://www.ifrs.org/groups/international-accounting-standards-board/",
                    "icon": "fa-solid fa-earth-africa"
                },
                {
                    "title": "International Federation of Accountants (IFAC)",
                    "description": "Global organization for the accountancy profession with resources and publications.",
                    "url": "https://www.ifac.org/",
                    "icon": "fa-solid fa-users"
                },
                {
                    "title": "World Bank - Accounting and Auditing ROSC for Morocco",
                    "description": "Reports on the Observance of Standards and Codes (ROSC) for accounting in Morocco.",
                    "url": "https://www.worldbank.org/en/country/morocco",
                    "icon": "fa-solid fa-building-columns"
                }
            ]
        }
    ]
    
    return resources

def get_resources_by_category(category):
    """
    Returns resources filtered by category
    """
    all_resources = get_all_resources()
    for resource_category in all_resources:
        if resource_category["category"].lower() == category.lower():
            return resource_category["resources"]
    return []
