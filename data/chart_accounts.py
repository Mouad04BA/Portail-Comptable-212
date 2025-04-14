"""
Moroccan Chart of Accounts data
Classes 1-7 with descriptions and codes
"""

def get_all_accounts():
    """
    Returns all chart of accounts organized by class
    """
    chart_accounts = [
        {
            "class_number": 1,
            "class_name": "Comptes de financement permanent",
            "class_description": "Accounts for permanent financing",
            "accounts": [
                {
                    "code": "11",
                    "name": "Capitaux propres",
                    "description": "Equity capital",
                    "sub_accounts": [
                        {"code": "111", "name": "Capital social ou personnel", "description": "Social or personal capital"},
                        {"code": "112", "name": "Primes d'émission, de fusion et d'apport", "description": "Issue, merger and contribution premiums"},
                        {"code": "113", "name": "Écarts de réévaluation", "description": "Revaluation differences"},
                        {"code": "114", "name": "Réserve légale", "description": "Legal reserve"},
                        {"code": "115", "name": "Autres réserves", "description": "Other reserves"},
                        {"code": "116", "name": "Report à nouveau", "description": "Retained earnings"},
                        {"code": "118", "name": "Résultats nets en instance d'affectation", "description": "Net results pending allocation"},
                        {"code": "119", "name": "Résultat net de l'exercice", "description": "Net result for the financial year"}
                    ]
                },
                {
                    "code": "13",
                    "name": "Capitaux propres assimilés",
                    "description": "Similar equity capital",
                    "sub_accounts": [
                        {"code": "131", "name": "Subventions d'investissement", "description": "Investment grants"},
                        {"code": "135", "name": "Provisions réglementées", "description": "Regulated provisions"}
                    ]
                },
                {
                    "code": "14",
                    "name": "Dettes de financement",
                    "description": "Financing debts",
                    "sub_accounts": [
                        {"code": "141", "name": "Emprunts obligataires", "description": "Bond loans"},
                        {"code": "148", "name": "Autres dettes de financement", "description": "Other financing debts"}
                    ]
                },
                {
                    "code": "15",
                    "name": "Provisions durables pour risques et charges",
                    "description": "Sustainable provisions for risks and charges",
                    "sub_accounts": [
                        {"code": "151", "name": "Provisions pour risques", "description": "Provisions for risks"},
                        {"code": "155", "name": "Provisions pour charges", "description": "Provisions for charges"}
                    ]
                }
            ]
        },
        {
            "class_number": 2,
            "class_name": "Comptes d'actif immobilisé",
            "class_description": "Fixed asset accounts",
            "accounts": [
                {
                    "code": "21",
                    "name": "Immobilisations en non-valeurs",
                    "description": "Non-value fixed assets",
                    "sub_accounts": [
                        {"code": "211", "name": "Frais préliminaires", "description": "Preliminary expenses"},
                        {"code": "212", "name": "Charges à répartir sur plusieurs exercices", "description": "Expenses to be distributed over several financial years"}
                    ]
                },
                {
                    "code": "22",
                    "name": "Immobilisations incorporelles",
                    "description": "Intangible assets",
                    "sub_accounts": [
                        {"code": "221", "name": "Immobilisations en recherche et développement", "description": "Research and development assets"},
                        {"code": "222", "name": "Brevets, marques, droits et valeurs similaires", "description": "Patents, trademarks, rights and similar values"},
                        {"code": "223", "name": "Fonds commercial", "description": "Commercial fund"}
                    ]
                },
                {
                    "code": "23",
                    "name": "Immobilisations corporelles",
                    "description": "Tangible assets",
                    "sub_accounts": [
                        {"code": "231", "name": "Terrains", "description": "Land"},
                        {"code": "232", "name": "Constructions", "description": "Buildings"},
                        {"code": "233", "name": "Installations techniques, matériel et outillage", "description": "Technical installations, equipment and tools"},
                        {"code": "234", "name": "Matériel de transport", "description": "Transport equipment"},
                        {"code": "235", "name": "Mobilier, matériel de bureau et aménagements divers", "description": "Furniture, office equipment and various fixtures"}
                    ]
                },
                {
                    "code": "24/25",
                    "name": "Immobilisations financières",
                    "description": "Financial fixed assets",
                    "sub_accounts": [
                        {"code": "241", "name": "Prêts immobilisés", "description": "Fixed loans"},
                        {"code": "248", "name": "Autres créances financières", "description": "Other financial receivables"},
                        {"code": "251", "name": "Titres de participation", "description": "Equity securities"},
                        {"code": "258", "name": "Autres titres immobilisés", "description": "Other fixed securities"}
                    ]
                },
                {
                    "code": "27",
                    "name": "Écarts de conversion - Actif",
                    "description": "Translation differences - Assets",
                    "sub_accounts": [
                        {"code": "271", "name": "Diminution des créances immobilisées", "description": "Decrease in fixed receivables"},
                        {"code": "272", "name": "Augmentation des dettes de financement", "description": "Increase in financing debts"}
                    ]
                },
                {
                    "code": "28",
                    "name": "Amortissements des immobilisations",
                    "description": "Depreciation of fixed assets",
                    "sub_accounts": [
                        {"code": "281", "name": "Amortissements des non-valeurs", "description": "Depreciation of non-values"},
                        {"code": "282", "name": "Amortissements des immobilisations incorporelles", "description": "Depreciation of intangible assets"},
                        {"code": "283", "name": "Amortissements des immobilisations corporelles", "description": "Depreciation of tangible fixed assets"}
                    ]
                },
                {
                    "code": "29",
                    "name": "Provisions pour dépréciation des immobilisations",
                    "description": "Provisions for depreciation of fixed assets",
                    "sub_accounts": [
                        {"code": "292", "name": "Provisions pour dépréciation des immobilisations incorporelles", "description": "Provisions for depreciation of intangible assets"},
                        {"code": "293", "name": "Provisions pour dépréciation des immobilisations corporelles", "description": "Provisions for depreciation of tangible fixed assets"},
                        {"code": "294/295", "name": "Provisions pour dépréciation des immobilisations financières", "description": "Provisions for depreciation of financial fixed assets"}
                    ]
                }
            ]
        },
        {
            "class_number": 3,
            "class_name": "Comptes d'actif circulant (hors trésorerie)",
            "class_description": "Current asset accounts (excluding cash)",
            "accounts": [
                {
                    "code": "31",
                    "name": "Stocks",
                    "description": "Inventories",
                    "sub_accounts": [
                        {"code": "311", "name": "Marchandises", "description": "Merchandise"},
                        {"code": "312", "name": "Matières et fournitures consommables", "description": "Materials and consumable supplies"},
                        {"code": "313", "name": "Produits en cours", "description": "Products in progress"},
                        {"code": "314", "name": "Produits intermédiaires et produits résiduels", "description": "Intermediate products and residual products"},
                        {"code": "315", "name": "Produits finis", "description": "Finished products"}
                    ]
                },
                {
                    "code": "34",
                    "name": "Créances de l'actif circulant",
                    "description": "Current asset receivables",
                    "sub_accounts": [
                        {"code": "341", "name": "Fournisseurs débiteurs, avances et acomptes", "description": "Supplier debtors, advances and deposits"},
                        {"code": "342", "name": "Clients et comptes rattachés", "description": "Customers and related accounts"},
                        {"code": "343", "name": "Personnel - débiteur", "description": "Staff - debtor"},
                        {"code": "345", "name": "État - débiteur", "description": "State - debtor"},
                        {"code": "346", "name": "Comptes d'associés - débiteurs", "description": "Partner accounts - debtors"},
                        {"code": "348", "name": "Autres débiteurs", "description": "Other debtors"},
                        {"code": "349", "name": "Comptes de régularisation - actif", "description": "Regularization accounts - assets"}
                    ]
                },
                {
                    "code": "35",
                    "name": "Titres et valeurs de placement",
                    "description": "Securities and investment securities",
                    "sub_accounts": [
                        {"code": "350", "name": "Titres et valeurs de placement", "description": "Securities and investment securities"}
                    ]
                },
                {
                    "code": "37",
                    "name": "Écarts de conversion - Actif (Éléments circulants)",
                    "description": "Translation differences - Assets (Current elements)",
                    "sub_accounts": [
                        {"code": "370", "name": "Écarts de conversion - Actif (Éléments circulants)", "description": "Translation differences - Assets (Current elements)"}
                    ]
                },
                {
                    "code": "39",
                    "name": "Provisions pour dépréciation des comptes de l'actif circulant",
                    "description": "Provisions for depreciation of current asset accounts",
                    "sub_accounts": [
                        {"code": "391", "name": "Provisions pour dépréciation des stocks", "description": "Provisions for depreciation of inventories"},
                        {"code": "394", "name": "Provisions pour dépréciation des créances de l'actif circulant", "description": "Provisions for depreciation of current asset receivables"},
                        {"code": "395", "name": "Provisions pour dépréciation des titres et valeurs de placement", "description": "Provisions for depreciation of securities and investment securities"}
                    ]
                }
            ]
        },
        {
            "class_number": 4,
            "class_name": "Comptes de passif circulant (hors trésorerie)",
            "class_description": "Current liability accounts (excluding cash)",
            "accounts": [
                {
                    "code": "44",
                    "name": "Dettes du passif circulant",
                    "description": "Current liabilities",
                    "sub_accounts": [
                        {"code": "441", "name": "Fournisseurs et comptes rattachés", "description": "Suppliers and related accounts"},
                        {"code": "442", "name": "Clients créditeurs, avances et acomptes", "description": "Client creditors, advances and deposits"},
                        {"code": "443", "name": "Personnel - créditeur", "description": "Staff - creditor"},
                        {"code": "444", "name": "Organismes sociaux", "description": "Social organizations"},
                        {"code": "445", "name": "État - créditeur", "description": "State - creditor"},
                        {"code": "446", "name": "Comptes d'associés - créditeurs", "description": "Partner accounts - creditors"},
                        {"code": "448", "name": "Autres créanciers", "description": "Other creditors"},
                        {"code": "449", "name": "Comptes de régularisation - passif", "description": "Regularization accounts - liabilities"}
                    ]
                },
                {
                    "code": "45",
                    "name": "Autres provisions pour risques et charges",
                    "description": "Other provisions for risks and charges",
                    "sub_accounts": [
                        {"code": "450", "name": "Autres provisions pour risques et charges", "description": "Other provisions for risks and charges"}
                    ]
                },
                {
                    "code": "47",
                    "name": "Écarts de conversion - Passif (Éléments circulants)",
                    "description": "Translation differences - Liabilities (Current elements)",
                    "sub_accounts": [
                        {"code": "470", "name": "Écarts de conversion - Passif (Éléments circulants)", "description": "Translation differences - Liabilities (Current elements)"}
                    ]
                }
            ]
        },
        {
            "class_number": 5,
            "class_name": "Comptes de trésorerie",
            "class_description": "Cash flow accounts",
            "accounts": [
                {
                    "code": "51",
                    "name": "Trésorerie - Actif",
                    "description": "Cash - Assets",
                    "sub_accounts": [
                        {"code": "511", "name": "Chèques et valeurs à encaisser", "description": "Checks and values to be cashed"},
                        {"code": "514", "name": "Banques, Trésorerie Générale et C.C.P.", "description": "Banks, General Treasury and C.C.P."},
                        {"code": "516", "name": "Caisses, Régies d'avances et accréditifs", "description": "Cash, advance funds and letters of credit"}
                    ]
                },
                {
                    "code": "55",
                    "name": "Trésorerie - Passif",
                    "description": "Cash - Liabilities",
                    "sub_accounts": [
                        {"code": "552", "name": "Crédits d'escompte", "description": "Discount credits"},
                        {"code": "553", "name": "Crédits de trésorerie", "description": "Cash credits"},
                        {"code": "554", "name": "Banques (soldes créditeurs)", "description": "Banks (credit balances)"}
                    ]
                },
                {
                    "code": "59",
                    "name": "Provisions pour dépréciation des comptes de trésorerie",
                    "description": "Provisions for depreciation of cash accounts",
                    "sub_accounts": [
                        {"code": "590", "name": "Provisions pour dépréciation des comptes de trésorerie", "description": "Provisions for depreciation of cash accounts"}
                    ]
                }
            ]
        },
        {
            "class_number": 6,
            "class_name": "Comptes de charges",
            "class_description": "Expense accounts",
            "accounts": [
                {
                    "code": "61",
                    "name": "Charges d'exploitation",
                    "description": "Operating expenses",
                    "sub_accounts": [
                        {"code": "611", "name": "Achats revendus de marchandises", "description": "Resold purchases of goods"},
                        {"code": "612", "name": "Achats consommés de matières et fournitures", "description": "Consumed purchases of materials and supplies"},
                        {"code": "613/614", "name": "Autres charges externes", "description": "Other external expenses"},
                        {"code": "617", "name": "Charges de personnel", "description": "Staff costs"},
                        {"code": "618", "name": "Autres charges d'exploitation", "description": "Other operating expenses"},
                        {"code": "619", "name": "Dotations d'exploitation", "description": "Operating allocations"}
                    ]
                },
                {
                    "code": "63",
                    "name": "Charges financières",
                    "description": "Financial expenses",
                    "sub_accounts": [
                        {"code": "631", "name": "Charges d'intérêts", "description": "Interest expenses"},
                        {"code": "633", "name": "Pertes de change", "description": "Exchange losses"},
                        {"code": "638", "name": "Autres charges financières", "description": "Other financial expenses"},
                        {"code": "639", "name": "Dotations financières", "description": "Financial allocations"}
                    ]
                },
                {
                    "code": "65",
                    "name": "Charges non courantes",
                    "description": "Non-current expenses",
                    "sub_accounts": [
                        {"code": "651", "name": "Valeurs nettes d'amortissements des immobilisations cédées", "description": "Net values of depreciation of transferred fixed assets"},
                        {"code": "656", "name": "Subventions accordées", "description": "Subsidies granted"},
                        {"code": "658", "name": "Autres charges non courantes", "description": "Other non-current expenses"},
                        {"code": "659", "name": "Dotations non courantes", "description": "Non-current allocations"}
                    ]
                },
                {
                    "code": "67",
                    "name": "Impôts sur les résultats",
                    "description": "Income taxes",
                    "sub_accounts": [
                        {"code": "670", "name": "Impôts sur les résultats", "description": "Income taxes"}
                    ]
                }
            ]
        },
        {
            "class_number": 7,
            "class_name": "Comptes de produits",
            "class_description": "Products accounts",
            "accounts": [
                {
                    "code": "71",
                    "name": "Produits d'exploitation",
                    "description": "Operating income",
                    "sub_accounts": [
                        {"code": "711", "name": "Ventes de marchandises", "description": "Sales of goods"},
                        {"code": "712", "name": "Ventes de biens et services produits", "description": "Sales of goods and services produced"},
                        {"code": "713", "name": "Variation des stocks de produits", "description": "Change in product inventories"},
                        {"code": "714", "name": "Immobilisations produites par l'entreprise pour elle-même", "description": "Fixed assets produced by the company for itself"},
                        {"code": "716", "name": "Subventions d'exploitation", "description": "Operating subsidies"},
                        {"code": "718", "name": "Autres produits d'exploitation", "description": "Other operating income"},
                        {"code": "719", "name": "Reprises d'exploitation, transferts de charges", "description": "Operating reversals, transfers of charges"}
                    ]
                },
                {
                    "code": "73",
                    "name": "Produits financiers",
                    "description": "Financial products",
                    "sub_accounts": [
                        {"code": "732", "name": "Produits des titres de participation et autres titres immobilisés", "description": "Income from equity securities and other fixed securities"},
                        {"code": "733", "name": "Gains de change", "description": "Exchange gains"},
                        {"code": "738", "name": "Intérêts et autres produits financiers", "description": "Interest and other financial income"},
                        {"code": "739", "name": "Reprises financières, transferts de charges", "description": "Financial reversals, transfers of charges"}
                    ]
                },
                {
                    "code": "75",
                    "name": "Produits non courants",
                    "description": "Non-current products",
                    "sub_accounts": [
                        {"code": "751", "name": "Produits des cessions d'immobilisations", "description": "Income from disposals of fixed assets"},
                        {"code": "756", "name": "Subventions d'équilibre", "description": "Balance subsidies"},
                        {"code": "758", "name": "Autres produits non courants", "description": "Other non-current income"},
                        {"code": "759", "name": "Reprises non courantes, transferts de charges", "description": "Non-current reversals, transfers of charges"}
                    ]
                }
            ]
        }
    ]
    
    return chart_accounts

def get_account_by_code(account_code):
    """
    Returns account details by code
    """
    accounts = get_all_accounts()
    
    for account_class in accounts:
        for account in account_class["accounts"]:
            if account["code"] == account_code:
                return account
            for sub_account in account.get("sub_accounts", []):
                if sub_account["code"] == account_code:
                    return sub_account
    
    return None
