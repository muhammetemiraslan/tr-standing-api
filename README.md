Flask API - Teams Data Scraper
Bu proje, Türkiye Futbol Federasyonu (TFF) resmi web sitesindeki bir sayfadan futbol takımlarının istatistiklerini çekip bir API aracılığıyla JSON formatında sunan bir Flask uygulamasıdır.

Gereksinimler
Projeyi çalıştırabilmek için aşağıdaki Python kütüphanelerine ihtiyacınız olacaktır:

Flask

Requests

BeautifulSoup4

Gerekli Kütüphaneleri Yüklemek
Proje için gerekli Python kütüphanelerini yüklemek için aşağıdaki komutu kullanabilirsiniz:

bash
Kopyala
Düzenle
pip install Flask requests beautifulsoup4
Proje Yapısı
bash
Kopyala
Düzenle
project/
│
├── app.py           # Flask uygulamasının ana dosyası
├── requirements.txt # Gereksinimler
└── README.md        # Proje hakkında bilgi
Kullanım
Flask uygulamasını çalıştırın:

bash
Kopyala
Düzenle
python app.py
Uygulama başarıyla başlatıldığında, API'nin aşağıdaki endpoint'ine erişebilirsiniz:

bash
Kopyala
Düzenle
GET /api/teams
Bu endpoint, Türkiye Futbol Federasyonu web sitesindeki takımların istatistiklerini çeker ve aşağıdaki formatta bir JSON çıktısı döner:

json
Kopyala
Düzenle
[
    {
        "team_name": "Takım Adı",
        "games_played": "Oynanan Maç",
        "wins": "Kazanan Maçlar",
        "draws": "Beraberlikler",
        "losses": "Kaybedilen Maçlar",
        "goals_for": "Atılan Gol",
        "goals_against": "Yenilen Gol",
        "goal_difference": "Averaj",
        "points": "Puan"
    },
    ...
]
API Açıklamaları
GET /api/teams
Bu endpoint, TFF'nin belirttiği sayfadan futbol takımlarının istatistiklerini çeker. Çekilen veriler, JSON formatında aşağıdaki alanları içerir:

team_name: Takım adı.

games_played: Takımın oynadığı maç sayısı.

wins: Kazanılan maç sayısı.

draws: Beraberlik yapılan maç sayısı.

losses: Kaybedilen maç sayısı.

goals_for: Takımın attığı toplam gol sayısı.

goals_against: Takımın yediği toplam gol sayısı.

goal_difference: Averaj (attığı - yediği gol).

points: Toplanan puan sayısı.

Hata Yönetimi
Eğer bir hata meydana gelirse, API bir hata mesajı ile birlikte uygun HTTP durum kodu dönecektir.

Örnek Hata Cevabı
json
Kopyala
Düzenle
{
    "error": "Sayfa çekilemedi"
}
Hata Kodu: 500 (Sunucu Hatası)
Projeyi Geliştirmek
Bu proje basit bir futbol takım istatistikleri çekme API'si sunmaktadır. Projeyi geliştirmek için aşağıdaki alanlarda değişiklikler yapabilirsiniz:

Farklı liglerden ve kaynaklardan veri çekmek.

Daha fazla takım istatistiği eklemek (örneğin, takım kadrosu, teknik direktör bilgileri vs.).

Farklı API endpoint'leri ekleyerek daha fazla veri sunmak.
