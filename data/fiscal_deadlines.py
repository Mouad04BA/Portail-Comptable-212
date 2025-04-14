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
    is_deadlines = [
        {
            "tax_type": "IS",
            "name": "Corporate Tax (IS) - Annual Return Filing",
            "description": "Filing of annual corporate tax return for non-calendar fiscal years",
            "due_date": f"{current_year}-03-31",
            "details": "Companies with a fiscal year ending December 31 must file their annual corporate tax return by March 31 of the following year.",
            "category": "annual",
            "payment_required": True
        },
        {
            "tax_type": "IS",
            "name": "Corporate Tax (IS) - First Installment",
            "description": "First quarterly installment payment for corporate tax",
            "due_date": f"{current_year}-03-31",
            "details": "Companies must pay the first installment of corporate tax by March 31.",
            "category": "quarterly",
            "payment_required": True
        },
        {
            "tax_type": "IS",
            "name": "Corporate Tax (IS) - Second Installment",
            "description": "Second quarterly installment payment for corporate tax",
            "due_date": f"{current_year}-06-30",
            "details": "Companies must pay the second installment of corporate tax by June 30.",
            "category": "quarterly",
            "payment_required": True
        },
        {
            "tax_type": "IS",
            "name": "Corporate Tax (IS) - Third Installment",
            "description": "Third quarterly installment payment for corporate tax",
            "due_date": f"{current_year}-09-30",
            "details": "Companies must pay the third installment of corporate tax by September 30.",
            "category": "quarterly",
            "payment_required": True
        },
        {
            "tax_type": "IS",
            "name": "Corporate Tax (IS) - Fourth Installment",
            "description": "Fourth quarterly installment payment for corporate tax",
            "due_date": f"{current_year}-12-31",
            "details": "Companies must pay the fourth installment of corporate tax by December 31.",
            "category": "quarterly",
            "payment_required": True
        }
    ]
    
    # Income Tax (IR) deadlines
    ir_deadlines = [
        {
            "tax_type": "IR",
            "name": "Income Tax (IR) - Annual Return Filing",
            "description": "Filing of annual income tax return for individuals",
            "due_date": f"{current_year}-03-31",
            "details": "Individuals must file their annual income tax return by March 31 of the year following the tax year.",
            "category": "annual",
            "payment_required": True
        },
        {
            "tax_type": "IR",
            "name": "Income Tax (IR) - Monthly Withholding",
            "description": "Monthly withholding tax on salaries and wages",
            "due_date": "Monthly (End of month)",
            "details": "Employers must withhold income tax from salaries and wages and remit it to the tax authorities by the end of each month.",
            "category": "monthly",
            "payment_required": True
        },
        {
            "tax_type": "IR",
            "name": "Income Tax (IR) - Professional Income",
            "description": "Quarterly installment payments for professional income",
            "due_date": "Quarterly (Mar 31, Jun 30, Sep 30, Dec 31)",
            "details": "Individuals with professional income must make quarterly installment payments by the end of each quarter.",
            "category": "quarterly",
            "payment_required": True
        }
    ]
    
    # Value Added Tax (TVA) deadlines
    tva_deadlines = [
        {
            "tax_type": "TVA",
            "name": "Value Added Tax (TVA) - Monthly Filing",
            "description": "Monthly VAT return filing for companies with annual turnover exceeding MAD 1 million",
            "due_date": "Monthly (End of following month)",
            "details": "Companies with annual turnover exceeding MAD 1 million must file their VAT returns and make payment by the end of the month following the tax period.",
            "category": "monthly",
            "payment_required": True
        },
        {
            "tax_type": "TVA",
            "name": "Value Added Tax (TVA) - Quarterly Filing",
            "description": "Quarterly VAT return filing for companies with annual turnover less than MAD 1 million",
            "due_date": "Quarterly (End of following month)",
            "details": "Companies with annual turnover less than MAD 1 million can opt for quarterly VAT filing, due by the end of the month following the quarter.",
            "category": "quarterly",
            "payment_required": True
        }
    ]
    
    # Generate monthly TVA deadlines for the current year
    monthly_tva = []
    for month in range(1, 13):
        last_day = calendar.monthrange(current_year, month)[1]
        next_month = month + 1 if month < 12 else 1
        next_year = current_year if month < 12 else current_year + 1
        next_month_last_day = calendar.monthrange(next_year, next_month)[1]
        
        monthly_tva.append({
            "tax_type": "TVA",
            "name": f"Value Added Tax (TVA) - {calendar.month_name[month]} Filing",
            "description": f"Monthly VAT return for {calendar.month_name[month]} {current_year}",
            "due_date": f"{next_year}-{next_month:02d}-{next_month_last_day}",
            "details": f"File VAT return and make payment for {calendar.month_name[month]} {current_year}",
            "category": "monthly",
            "payment_required": True
        })
    
    # Combine all deadlines
    all_deadlines = is_deadlines + ir_deadlines + tva_deadlines + monthly_tva
    
    # Sort by due date
    all_deadlines.sort(key=lambda x: x["due_date"] if isinstance(x["due_date"], str) and len(x["due_date"]) == 10 else "9999-12-31")
    
    return all_deadlines

def get_upcoming_deadlines(limit=3):
    """
    Returns upcoming fiscal deadlines
    """
    all_deadlines = get_all_deadlines()
    
    # Filter only deadlines with proper date format
    dated_deadlines = [d for d in all_deadlines if isinstance(d["due_date"], str) and len(d["due_date"]) == 10]
    
    # Get today's date
    today = datetime.now().date()
    
    # Filter future deadlines
    upcoming = []
    for deadline in dated_deadlines:
        try:
            due_date = datetime.strptime(deadline["due_date"], "%Y-%m-%d").date()
            if due_date >= today:
                upcoming.append(deadline)
        except ValueError:
            continue
    
    # Sort by due date
    upcoming.sort(key=lambda x: datetime.strptime(x["due_date"], "%Y-%m-%d").date())
    
    # Return limited number of upcoming deadlines
    return upcoming[:limit]
