# Flask API - Türkiye Futbol Takımları İstatistikleri

Bu proje, Türkiye Futbol Federasyonu'nun (TFF) resmi web sitesindeki futbol takımlarının istatistiklerini çeker ve bir Flask API aracılığıyla JSON formatında sunar.

## Özellikler

- TFF'nin resmi web sitesinden futbol takımlarının maç istatistiklerini çeker.
- Flask web framework'ü ile geliştirilmiştir.
- API, JSON formatında takımların istatistiklerini döner.
- Web scraping kullanarak veriler dinamik bir şekilde alınır.

## Gereksinimler

Projeyi çalıştırabilmek için aşağıdaki Python kütüphanelerini yüklemeniz gerekecek:

- Flask
- Requests
- BeautifulSoup4

```bash

git clone https://github.com/muhammetemiraslan/tr-standing-api.git
cd flask-teams-api

```

```bash
python app.py
```


API'yi Kullanın:

API çalışmaya başladığında, aşağıdaki endpoint üzerinden verilere erişebilirsiniz:

```bash
GET /api/teams
```

dönen yanıt şu şekilde olacaktır:

```bash
[
    {
        "team_name": "Takım Adı",
        "games_played": "Oynanan Maç Sayısı",
        "wins": "Kazanan Maç Sayısı",
        "draws": "Beraberlik Sayısı",
        "losses": "Kaybedilen Maç Sayısı",
        "goals_for": "Atılan Gol Sayısı",
        "goals_against": "Yenilen Gol Sayısı",
        "goal_difference": "Averaj",
        "points": "Toplanan Puan"
    },
    ...
]
```

