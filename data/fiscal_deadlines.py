"""
Fiscal deadlines data for Moroccan taxes
"""
from datetime import datetime, timedelta
import calendar


def get_all_deadlines():
    """
    Returns all fiscal deadlines for IS, IR, and TVA
    """
    # Get current year
    current_year = datetime.now().year

    # Corporate Tax (IS) deadlines
    is_deadlines = [{
        "tax_type": "IS",
        "name": "Impôt sur les Sociétés (IS) - Déclaration Annuelle",
        "description":
        "Dépôt de la déclaration annuelle de l'impôt sur les sociétés pour les exercices non-calendaires",
        "due_date": f"{current_year}-03-31",
        "details":
        "Les sociétés dont l'exercice se termine le 31 décembre doivent déposer leur déclaration annuelle d'IS avant le 31 mars de l'année suivante.",
        "category": "annual",
        "payment_required": True
    }, {
        "tax_type": "IS",
        "name": "Impôt sur les Sociétés (IS) - Premier Acompte",
        "description":
        "Premier acompte trimestriel de l'impôt sur les sociétés",
        "due_date": f"{current_year}-03-31",
        "details":
        "Les sociétés doivent payer le premier acompte de l'IS avant le 31 mars.",
        "category": "quarterly",
        "payment_required": True
    }, {
        "tax_type": "IS",
        "name": "Corporate Tax (IS) - Second Installment",
        "description":
        "Second quarterly installment payment for corporate tax",
        "due_date": f"{current_year}-06-30",
        "details":
        "Companies must pay the second installment of corporate tax by June 30.",
        "category": "quarterly",
        "payment_required": True
    }, {
        "tax_type": "IS",
        "name": "Corporate Tax (IS) - Third Installment",
        "description": "Third quarterly installment payment for corporate tax",
        "due_date": f"{current_year}-09-30",
        "details":
        "Companies must pay the third installment of corporate tax by September 30.",
        "category": "quarterly",
        "payment_required": True
    }, {
        "tax_type": "IS",
        "name": "Corporate Tax (IS) - Fourth Installment",
        "description":
        "Fourth quarterly installment payment for corporate tax",
        "due_date": f"{current_year}-12-31",
        "details":
        "Companies must pay the fourth installment of corporate tax by December 31.",
        "category": "quarterly",
        "payment_required": True
    }]

    # Income Tax (IR) deadlines
    ir_deadlines = [{
        "tax_type": "IR",
        "name": "Income Tax (IR) - Annual Return Filing",
        "description": "Filing of annual income tax return for individuals",
        "due_date": f"{current_year}-03-31",
        "details":
        "Individuals must file their annual income tax return by March 31 of the year following the tax year.",
        "category": "annual",
        "payment_required": True
    }, {
        "tax_type": "IR",
        "name": "Income Tax (IR) - Monthly Withholding",
        "description": "Monthly withholding tax on salaries and wages",
        "due_date": "Monthly (End of month)",
        "details":
        "Employers must withhold income tax from salaries and wages and remit it to the tax authorities by the end of each month.",
        "category": "monthly",
        "payment_required": True
    }, {
        "tax_type": "IR",
        "name": "Income Tax (IR) - Professional Income",
        "description":
        "Quarterly installment payments for professional income",
        "due_date": "Quarterly (Mar 31, Jun 30, Sep 30, Dec 31)",
        "details":
        "Individuals with professional income must make quarterly installment payments by the end of each quarter.",
        "category": "quarterly",
        "payment_required": True
    }]

    # Value Added Tax (TVA) deadlines
    tva_deadlines = [{
        "tax_type": "TVA",
        "name": "Taxe sur la Valeur Ajoutée (TVA) - Déclaration Mensuelle",
        "description":
        "Déclaration mensuelle de TVA pour les entreprises dont le chiffre d'affaires dépasse 1 million de MAD",
        "due_date": "Mensuel (Fin du mois suivant)",
        "details":
        "Les entreprises dont le chiffre d'affaires dépasse 1 million de MAD doivent déposer leurs déclarations de TVA et effectuer le paiement avant la fin du mois suivant la période d'imposition.",
        "category": "monthly",
        "payment_required": True
    }, {
        "tax_type": "TVA",
        "name": "Taxe sur la Valeur Ajoutée (TVA) - Déclaration Trimestrielle",
        "description":
        "Déclaration trimestrielle de TVA pour les entreprises dont le chiffre d'affaires est inférieur à 1 million de MAD",
        "due_date": "Trimestriel (Fin du mois suivant)",
        "details":
        "Les entreprises dont le chiffre d'affaires est inférieur à 1 million de MAD peuvent opter pour une déclaration trimestrielle de TVA, à déposer avant la fin du mois suivant le trimestre.",
        "category": "quarterly",
        "payment_required": True
    }]

    # Generate monthly TVA deadlines for the current year
    monthly_tva = []
    for month in range(1, 13):
        last_day = calendar.monthrange(current_year, month)[1]
        next_month = month + 1 if month < 12 else 1
        next_year = current_year if month < 12 else current_year + 1
        next_month_last_day = calendar.monthrange(next_year, next_month)[1]

        monthly_tva.append({
            "tax_type": "TVA",
            "name":
            f"Taxe sur la Valeur Ajoutée (TVA) - Déclaration {calendar.month_name[month]}",
            "description":
            f"Déclaration mensuelle de TVA pour {calendar.month_name[month]} {current_year}",
            "due_date": f"{next_year}-{next_month:02d}-{next_month_last_day}",
            "details":
            f"Déposer la déclaration de TVA et effectuer le paiement pour {calendar.month_name[month]} {current_year}",
            "category": "monthly",
            "payment_required": True
        })

    # Combine all deadlines
    all_deadlines = is_deadlines + ir_deadlines + tva_deadlines + monthly_tva

    # Sort by due date
    all_deadlines.sort(key=lambda x: x["due_date"] if isinstance(
        x["due_date"], str) and len(x["due_date"]) == 10 else "9999-12-31")

    return all_deadlines


def get_upcoming_deadlines(limit=3):
    """
    Returns upcoming fiscal deadlines
    """
    all_deadlines = get_all_deadlines()

    # Filter only deadlines with proper date format
    dated_deadlines = [
        d for d in all_deadlines
        if isinstance(d["due_date"], str) and len(d["due_date"]) == 10
    ]

    # Get today's date
    today = datetime.now().date()

    # Filter future deadlines
    upcoming = []
    for deadline in dated_deadlines:
        try:
            due_date = datetime.strptime(deadline["due_date"],
                                         "%Y-%m-%d").date()
            if due_date >= today:
                upcoming.append(deadline)
        except ValueError:
            continue

    # Sort by due date
    upcoming.sort(
        key=lambda x: datetime.strptime(x["due_date"], "%Y-%m-%d").date())

    # Return limited number of upcoming deadlines
    return upcoming[:limit]
