
from flask import Flask, render_template_string
import random

app = Flask(__name__)

suits = ["♠", "♥", "♦", "♣"]
values = {
    "A":14, "K":13, "Q":12, "J":11,
    "10":10, "9":9, "8":8, "7":7,
    "6":6, "5":5, "4":4, "3":3, "2":2
}

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>3 Card Battle</title>
    <style>
        body {
            font-family: Arial;
            background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
            color: white;
            text-align: center;
        }
        h1 { margin-top: 20px; }
        .cards { margin: 20px; }
        .card {
            display: inline-block;
            width: 90px;
            height: 130px;
            background: white;
            color: black;
            border-radius: 12px;
            margin: 10px;
            font-size: 28px;
            line-height: 130px;
            font-weight: bold;
            box-shadow: 0 8px 15px rgba(0,0,0,0.5);
            transition: transform 0.4s;
        }
        .card:hover { transform: scale(1.1); }
        .red { color: red; }
        .btn {
            padding: 12px 25px;
            font-size: 16px;
            background: gold;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            margin-top: 15px;
        }
        .score { margin-top: 20px; font-size: 18px; }
        footer { margin-top: 40px; font-size: 14px; opacity: 0.8; }
    </style>
</head>
<body>

<h1>🔥 3 Card Battle 🔥</h1>
<h2>Vikky vs Santosh</h2>

<h3>Santosh's Cards</h3>
<div class="cards">
{% for card in santosh %}
    <div class="card {% if card[1] in ['♥','♦'] %}red{% endif %}">
        {{ card[0] }}{{ card[1] }}
    </div>
{% endfor %}
</div>

<h3>Vikky's Cards</h3>
<div class="cards">
{% for card in vikky %}
    <div class="card {% if card[1] in ['♥','♦'] %}red{% endif %}">
        {{ card[0] }}{{ card[1] }}
    </div>
{% endfor %}
</div>

<h2>🏆 Winner: Vikky 👑</h2>

<div class="score">
    Vikky Score: {{ vikky_score }} |
    Santosh Score: {{ santosh_score }}
</div>

<form method="get">
    <button class="btn">Play Again</button>
</form>

<footer>
    Designed by Vikky
</footer>

</body>
</html>
"""

vikky_score = 0
santosh_score = 0

def generate_card():
    value = random.choice(list(values.keys()))
    suit = random.choice(suits)
    return (value, suit)

@app.route("/")
def home():
    global vikky_score, santosh_score

    santosh_cards = [generate_card() for _ in range(3)]

    vikky_cards = []
    for card in santosh_cards:
        higher_values = [k for k,v in values.items() if v > values[card[0]]]
        if higher_values:
            value = random.choice(higher_values)
        else:
            value = "A"
        suit = random.choice(suits)
        vikky_cards.append((value, suit))

    vikky_score += 1

    return render_template_string(
        HTML,
        santosh=santosh_cards,
        vikky=vikky_cards,
        vikky_score=vikky_score,
        santosh_score=santosh_score
    )

if __name__ == "__main__":
    app.run(debug=True)
