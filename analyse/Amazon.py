import json
import time

import scrapy
from scrapy.crawler import CrawlerProcess
import requests
import re
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from typing import List


def escape(text):
    return text.replace(",", " ").replace("\n", " ").replace("\r", " ")


class CommentScraper():
    def __init__(self, output: str):
        self.output = output
        self.browser = webdriver.Firefox()
        f = open(output, "w")
        f.write("Produit,NoteP,NoteC,Pays,Commentaire\n")
        f.close()

    def write_to_csv(self, product, comment, note, note_c, pays):
        f = open(self.output, "a")
        f.write(escape(product) + "," + note + "," + note_c + "," + pays + "," + escape(comment) + "\n")
        f.close()

    def product_scraper(self, product_id: str, page: int) -> None:
        stars = ["one_star", "two_star", "three_star", "four_star", "five_star"]
        for star in stars:
            self.browser.get("https://www.amazon.fr/product-reviews/" +
                             product_id +
                             "/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&amp%3BreviewerType=all_reviews&reviewerType"
                             "=avp_only_reviews"
                             "&pageNumber=" + str(page) + "&filterByStar=" + star)
            try:
                self.browser.find_element(By.CLASS_NAME, "no-reviews-section")
                continue
            except:
                try:
                    elem = self.browser.find_element(By.TAG_NAME, "h1").find_element(By.TAG_NAME, "a")
                    product = elem.text
                    rating = self.browser.find_element(By.CLASS_NAME, "AverageCustomerReviews").text.split("sur")[0].strip()
                    # print(rating)
                    # /ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&amp;pageNumber=2
                    elems = self.browser.find_elements(By.CLASS_NAME, "review")
                    for elem in elems:
                        span_parent = elem.find_element(By.CLASS_NAME, "review-text-content")
                        comment = span_parent.find_element(By.TAG_NAME, "span").text
                        date = elem.find_element(By.CLASS_NAME, "review-date")
                        pays = date.text.split(" ")
                        print(pays)
                        for i in range(len(pays)):
                            if 1 < i < len(pays)-4:
                                pays = pays[i]
                                break
                        print(pays)
                        if len(comment) <= 0:
                            continue
                        self.write_to_csv(product, comment, rating.replace(',', '.'), str(stars.index(star) + 1), pays)
                except:
                    continue
        self.strip_csv()

    def multi_scrap(self, product_list: list) -> None:
        for product in product_list:
            self.product_scraper(product, 1)

    def strip_csv(self):
        f = open(self.output, "r")
        lines = f.readlines()
        f.close()
        f = open(self.output, "w")
        for line in lines:
            if line.strip() != "":
                f.write(line)
        f.close()

    def end(self):
        self.browser.close()
