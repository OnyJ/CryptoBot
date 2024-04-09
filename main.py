'''
Main file for the intelligent website bot.
'''
from flask import Flask, render_template
from bot import Bot
app = Flask(__name__)
@app.route('/')
def index():
    # Create an instance of the bot
    bot = Bot()
    # Get the buying and selling signals
    buying_signals, selling_signals = bot.get_signals()
    # Render the index.html template with the signals
    return render_template('index.html', buying_signals=buying_signals, selling_signals=selling_signals)
if __name__ == '__main__':
    app.run(debug=True)