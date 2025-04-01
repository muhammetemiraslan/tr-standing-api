from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/api/teams', methods=['GET'])
def get_teams():
    url = "https://www.tff.org/default.aspx?pageID=198"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }

    # Sayfayı çekme
    html = requests.get(url, headers=headers).content
    soup = BeautifulSoup(html, "html.parser")

    # Tabloyu bul ve satırları al
    teamlist = soup.find("table", {"class": "s-table"}).find("tbody").find_all("tr")

    teams_data = []  # Takımların bilgilerini tutacak liste

    # Başlık satırını atla
    for row in teamlist:
        if row.find("th"):
            continue
        
        team_name = row.find("a").text.strip() if row.find("a") else "Bilinmiyor"
        stats = [span.text.strip() for span in row.find_all("span")]
        
        if stats:
            # Verileri bir dictionary olarak ekleyelim
            teams_data.append({
                "team_name": team_name,
                "games_played": stats[0],
                "wins": stats[1],
                "draws": stats[2],
                "losses": stats[3],
                "goals_for": stats[4],
                "goals_against": stats[5],
                "goal_difference": stats[6],
                "points": stats[7]
            })

    # JSON formatında veri döndürme
    return jsonify(teams_data)

if __name__ == '__main__':
    app.run(debug=True)
