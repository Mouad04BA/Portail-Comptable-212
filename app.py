import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from forms import ContactForm
from data import chart_accounts, fiscal_deadlines, news, bankruptcy, resources

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "moroccan-accounting-secure-key")

# Configure mail settings
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER', 'no-reply@moroccan-accounting.com')

mail = Mail(app)

@app.route('/')
def index():
    # Get featured items for home page
    latest_news = news.get_latest_news(3)
    upcoming_deadlines = fiscal_deadlines.get_upcoming_deadlines(3)
    return render_template('index.html', 
                         latest_news=latest_news,
                         upcoming_deadlines=upcoming_deadlines)

@app.route('/chart-accounts')
def chart_accounts_page():
    # Get chart of accounts data
    accounts_data = chart_accounts.get_all_accounts()
    return render_template('chart_accounts.html', accounts=accounts_data)

@app.route('/fiscal-deadlines')
def fiscal_deadlines_page():
    # Get fiscal deadlines data
    deadlines = fiscal_deadlines.get_all_deadlines()
    return render_template('fiscal_deadlines.html', deadlines=deadlines)

@app.route('/news')
def news_page():
    # Get all news items
    all_news = news.get_all_news()
    return render_template('news.html', news_items=all_news)

@app.route('/bankruptcy')
def bankruptcy_page():
    # Get bankruptcy filing process data
    filing_process = bankruptcy.get_filing_process()
    faq = bankruptcy.get_faq()
    return render_template('bankruptcy.html', 
                         process=filing_process,
                         faq=faq)

@app.route('/resources')
def resources_page():
    # Get resources data
    all_resources = resources.get_all_resources()
    return render_template('resources.html', resources=all_resources)

@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    form = ContactForm()
    if form.validate_on_submit():
        try:
            msg = Message(
                subject=f"Contact Form: {form.subject.data}",
                recipients=[os.environ.get('CONTACT_EMAIL', 'admin@moroccan-accounting.com')],
                body=f"Name: {form.name.data}\nEmail: {form.email.data}\n\n{form.message.data}"
            )
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('contact_page'))
        except Exception as e:
            app.logger.error(f"Error sending email: {e}")
            flash('An error occurred while sending your message. Please try again later.', 'danger')
    
    return render_template('contact.html', form=form)

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('layout.html', error="404 - Page Not Found"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('layout.html', error="500 - Server Error"), 500
