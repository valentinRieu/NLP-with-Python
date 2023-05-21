from Amazon import CommentScraper
from nltk import sentiment
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd

# Tondeuse B0721LYLZK
# valise outils B017RKPDP2
# livre B07N17TMFH
# pile B000EGQT82
# coussin gonflable 2.8/5 B08PDZR1X4
# bracelet 3/5 B08RXS9SDF
# "serveur" 1.9/5 B077HVY3SC (peu d'avis)
# T-shirt 4.8/5 B08SY6L6H5

train = [
    "B09FXJ2YGX",  # 50
    "B0BKSKD8MG",  # 100
    "B0B25LZGGW",  # 150
    "B08BS4PW1B",  # 200
    "B00BEJ77WK",  # 250
    "B09G29LLLJ",  # 300
    "B06XYG1P2G",  # 350
    "B07TNK97KW",  # 400
    "B07BS62MKW",  # 450
    "B08QHVCWLN",  # 500
    "B01DT3VX6O",  # 550
    "B08T1HR5CS",  # 600
    "B0BPJHMCJ8",  # 650
    "B0BRZ2YMVC",  # 700
    "B07227RQJ9",  # 750
    "B01AGGJ44K",  # 800
    "B09641H5TG",  # 850
    "B001CM0NV6",  # 900
    "B09VP4VBKL",  # 950
    "B01MTNHX72",  # 1000
    "B08GYG6T12",  # 1050
    "B07FKRWG6D",  # 1100
    "B00BWNYHVC",  # 1150
    "B07N1JPG31",  # 1200
]

test = [
    "B0721LYLZK",
    "B017RKPDP2",
    "B07N17TMFH",
    "B000EGQT82",
    "B08PDZR1X4",
    "B08RXS9SDF",
    "B077HVY3SC",
    "B08SY6L6H5",
    "B014I8SSD0",
    "B088C32FKW",
    "B09BNXY2T3",
    "B08XMFW7MH",
    "B0816FXTB1",
    "B017X8GL9A",
    "B00A0VCJPI"
]


def main():
    print("Scraping...")
    scraper = CommentScraper("train.csv")
    scraper.multi_scrap(train)
    scraper.strip_csv()
    scraper.end()
    print("done")
    scraper = CommentScraper("test.csv")
    scraper.multi_scrap(test)
    scraper.strip_csv()
    scraper.end()
    print("done")
main()
