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
            "title": "Morocco Adopts New Finance Law for 2023",
            "date": "2023-01-15",
            "summary": "The Moroccan government has adopted the new finance law for 2023 with significant changes to corporate taxation.",
            "content": """
                <p>The Moroccan government has adopted the finance law for 2023, which includes several significant changes to the tax system. The key measures include:</p>
                <ul>
                    <li>Reduction of corporate tax rates for small and medium enterprises from 20% to 18%</li>
                    <li>Introduction of new tax incentives for startups and innovative companies</li>
                    <li>Simplification of the VAT refund process for exporters</li>
                    <li>Strengthening of tax collection mechanisms to combat tax evasion</li>
                </ul>
                <p>These changes aim to boost economic growth, support small businesses, and enhance tax compliance in the country. The new measures will take effect on January 1, 2023.</p>
            """,
            "category": "Tax",
            "source": "Ministry of Finance",
            "image_url": "https://images.unsplash.com/photo-1520607162513-77705c0f0d4a"
        },
        {
            "id": 2,
            "title": "Bank Al-Maghrib Maintains Key Interest Rate at 2.5%",
            "date": "2023-03-21",
            "summary": "Morocco's central bank has decided to keep its benchmark interest rate unchanged at 2.5% amid economic recovery.",
            "content": """
                <p>Bank Al-Maghrib, Morocco's central bank, has announced its decision to maintain the key interest rate at 2.5% following its quarterly monetary policy meeting. The decision comes as the economy continues to recover from the impacts of the COVID-19 pandemic and global supply chain disruptions.</p>
                <p>According to the central bank's statement, the decision was based on the following factors:</p>
                <ul>
                    <li>Inflation remains under control at 2.8%, despite global pressures</li>
                    <li>Economic growth is projected at 3.2% for 2023, showing resilience</li>
                    <li>Foreign exchange reserves remain stable, covering approximately 6 months of imports</li>
                    <li>The banking sector continues to show strong liquidity</li>
                </ul>
                <p>The central bank also announced that it will continue to monitor global economic developments and their potential impact on the domestic economy, particularly the effects of rising commodity prices and global inflation trends.</p>
            """,
            "category": "Banking",
            "source": "Bank Al-Maghrib",
            "image_url": "https://images.unsplash.com/photo-1526948531399-320e7e40f0ca"
        },
        {
            "id": 3,
            "title": "New Accounting Standards Announced for Moroccan Companies",
            "date": "2023-05-10",
            "summary": "The National Accounting Council introduces updated accounting standards to align with international practices.",
            "content": """
                <p>The National Accounting Council of Morocco (Conseil National de la Comptabilité) has announced a comprehensive update to the country's accounting standards. The new standards aim to align Moroccan accounting practices more closely with International Financial Reporting Standards (IFRS).</p>
                <p>Key changes in the updated standards include:</p>
                <ul>
                    <li>Enhanced disclosure requirements for financial instruments</li>
                    <li>New methods for revenue recognition that align with IFRS 15</li>
                    <li>Updated guidance on leases and rental agreements</li>
                    <li>Improved valuation methods for intangible assets</li>
                    <li>Stricter rules for recognizing and measuring impairment</li>
                </ul>
                <p>These changes will be phased in over a two-year period, with full compliance required by January 2025. The National Accounting Council will organize training sessions and workshops to help companies transition to the new standards.</p>
                <p>Experts believe these updates will enhance the transparency and comparability of financial statements for Moroccan companies, potentially attracting more foreign investment by making it easier for international stakeholders to understand Moroccan financial reports.</p>
            """,
            "category": "Accounting",
            "source": "National Accounting Council",
            "image_url": "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4"
        },
        {
            "id": 4,
            "title": "Morocco Launches Digital Tax Filing Platform for Businesses",
            "date": "2023-07-05",
            "summary": "The General Tax Administration introduces a new digital platform to simplify tax filing for businesses.",
            "content": """
                <p>The Moroccan General Tax Administration (Direction Générale des Impôts) has launched a new digital platform called "SIMPL-Pro+" aimed at simplifying tax filing procedures for businesses of all sizes. The platform represents a significant step in the country's digital transformation agenda.</p>
                <p>The new platform offers several advanced features:</p>
                <ul>
                    <li>Integrated filing for all tax types (IS, IR, TVA) through a single interface</li>
                    <li>Automated calculation tools to minimize errors</li>
                    <li>Real-time validation of submissions</li>
                    <li>Digital payment options with instant confirmation</li>
                    <li>Document storage and retrieval for up to 10 years</li>
                    <li>Personalized tax calendar with reminders for upcoming deadlines</li>
                </ul>
                <p>According to the Director General of Taxes, this initiative is expected to reduce the administrative burden on businesses by an estimated 65% and improve tax compliance rates. The platform also features a multilingual interface (Arabic, French, and English) to accommodate the diverse business community in Morocco.</p>
                <p>Training sessions are being organized nationwide to help businesses transition to the new system, with full migration expected to be completed by the end of 2023.</p>
            """,
            "category": "Technology",
            "source": "General Tax Administration",
            "image_url": "https://images.unsplash.com/photo-1544717297-fa95b6ee9643"
        },
        {
            "id": 5,
            "title": "Morocco's Foreign Exchange Office Reports Trade Deficit Reduction",
            "date": "2023-09-12",
            "summary": "Latest figures show a 15% reduction in Morocco's trade deficit compared to the previous year.",
            "content": """
                <p>The Foreign Exchange Office of Morocco (Office des Changes) has released its latest trade figures, showing a significant 15% reduction in the country's trade deficit compared to the same period last year. This improvement is attributed to strong export performance in key sectors and stabilizing import costs.</p>
                <p>Key highlights from the report include:</p>
                <ul>
                    <li>Exports increased by 18.5%, with particularly strong performance in automotive (22%), phosphates and derivatives (15%), and agricultural products (12%)</li>
                    <li>Imports grew at a slower rate of 8.3%, with energy imports decreasing by 5% due to strategic reserves and diversification</li>
                    <li>Foreign direct investment inflows increased by 21%, reaching 15.8 billion dirhams</li>
                    <li>Remittances from Moroccans living abroad grew by 9.7% to 54.2 billion dirhams</li>
                </ul>
                <p>Economic analysts view these figures as indicative of Morocco's growing economic resilience and the success of its industrial acceleration plan. The strengthening export sectors, particularly in high-value industries such as automotive and aerospace, point to Morocco's successful integration into global value chains.</p>
                <p>The Foreign Exchange Office projects that if current trends continue, Morocco could see its first trade surplus in over two decades within the next 3-5 years.</p>
            """,
            "category": "Economy",
            "source": "Foreign Exchange Office",
            "image_url": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40"
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
