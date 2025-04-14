"""
Moroccan financial and economic news data
"""
from datetime import datetime

def get_all_news():
    """
    Returns all news articles
    """
    news_articles = [
        {
            "id": 1,
            "title": "Nouvelle Loi de Finances 2025",
            "date": "2025-01-10",
            "summary": "Le gouvernement marocain adopte la nouvelle loi de finances pour 2025 avec des changements significatifs dans la fiscalité des entreprises.",
            "content": """
                <p>Le gouvernement marocain vient d'adopter la loi de finances 2025, qui comprend plusieurs mesures importantes :</p>
                <ul>
                    <li>Réduction du taux d'IS pour les PME de 15% à 12%</li>
                    <li>Nouveaux avantages fiscaux pour l'innovation</li>
                    <li>Simplification des procédures de TVA</li>
                    <li>Renforcement des mesures anti-fraude fiscale</li>
                </ul>
                <p>Ces changements entreront en vigueur le 1er janvier 2025.</p>
            """,
            "category": "Fiscalité",
            "source": "Ministère des Finances",
            "image_url": "https://images.unsplash.com/photo-1520607162513-77705c0f0d4a"
        },
        {
            "id": 2,
            "title": "Bank Al-Maghrib: Nouveau Taux Directeur",
            "date": "2025-03-15",
            "summary": "La banque centrale du Maroc ajuste son taux directeur à 3,25% pour maîtriser l'inflation.",
            "content": """
                <p>Bank Al-Maghrib annonce une hausse de son taux directeur à 3,25% lors de sa réunion trimestrielle. Cette décision est motivée par :</p>
                <ul>
                    <li>Une inflation projetée à 3,2% pour 2025</li>
                    <li>Une croissance économique de 4,1% attendue</li>
                    <li>Des réserves de change couvrant 6,5 mois d'importations</li>
                </ul>
                <p>Cette mesure vise à maintenir la stabilité des prix et soutenir la croissance économique.</p>
            """,
            "category": "Banque",
            "source": "Bank Al-Maghrib",
            "image_url": "https://images.unsplash.com/photo-1526948531399-320e7e40f0ca"
        },
        {
            "id": 3,
            "title": "Digitalisation Comptable: Nouvelles Normes 2025",
            "date": "2025-02-20",
            "summary": "Le Conseil National de la Comptabilité impose de nouvelles normes pour la digitalisation comptable.",
            "content": """
                <p>Le CNC annonce de nouvelles normes pour la transformation numérique de la comptabilité :</p>
                <ul>
                    <li>Factures électroniques obligatoires dès juillet 2025</li>
                    <li>Nouveaux formats standardisés pour les rapports financiers</li>
                    <li>Système de signature électronique unifié</li>
                </ul>
                <p>Ces mesures visent à moderniser et sécuriser les pratiques comptables au Maroc.</p>
            """,
            "category": "Comptabilité",
            "source": "Conseil National de la Comptabilité",
            "image_url": "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4"
        },
        {
            "id": 4,
            "title": "Réforme du Marché des Capitaux 2025",
            "date": "2025-04-05",
            "summary": "L'AMMC introduit de nouvelles réglementations pour dynamiser le marché financier.",
            "content": """
                <p>L'Autorité Marocaine du Marché des Capitaux (AMMC) lance une réforme majeure :</p>
                <ul>
                    <li>Introduction des crypto-actifs réglementés</li>
                    <li>Nouvelles règles pour les fintech</li>
                    <li>Modernisation des systèmes de trading</li>
                </ul>
                <p>Ces changements visent à moderniser le marché financier marocain.</p>
            """,
            "category": "Finance",
            "source": "AMMC",
            "image_url": "https://images.unsplash.com/photo-1524508762098-fd966ffb6ef9"
        },
        {
            "id": 5,
            "title": "Nouvelles Mesures pour les Auto-Entrepreneurs",
            "date": "2025-03-30",
            "summary": "Le statut d'auto-entrepreneur connaît des améliorations significatives en 2025.",
            "content": """
                <p>Le gouvernement annonce des changements majeurs pour les auto-entrepreneurs :</p>
                <ul>
                    <li>Augmentation des plafonds de chiffre d'affaires</li>
                    <li>Simplification des déclarations fiscales</li>
                    <li>Nouvelles couvertures sociales</li>
                </ul>
                <p>Ces mesures entreront en vigueur progressivement durant l'année 2025.</p>
            """,
            "category": "Entreprise",
            "source": "Ministère de l'Économie",
            "image_url": "https://images.unsplash.com/photo-1664575599736-c5197c684128"
        }
    ]

    # Sort news by date (newest first)
    news_articles.sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"), reverse=True)

    return news_articles

def get_latest_news(limit=3):
    """
    Returns the latest news articles
    """
    all_news = get_all_news()
    return all_news[:limit]

def get_news_by_category(category):
    """
    Returns news articles filtered by category
    """
    all_news = get_all_news()
    return [news for news in all_news if news["category"].lower() == category.lower()]

def get_news_by_id(news_id):
    """
    Returns a specific news article by ID
    """
    all_news = get_all_news()
    for news in all_news:
        if news["id"] == news_id:
            return news
    return None