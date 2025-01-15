# arxiv_scraper/arxiv_scraper.py
from bs4 import BeautifulSoup
from .base_scraper import BaseScraper


class ArxivScraper(BaseScraper):
    """
    Estratégia de scraping para a seção de Inteligência Artificial do Arxiv.
    """

    def parse(self, html):
        """
        Faz o parsing do HTML e retorna uma lista com os títulos dos artigos.
        """
        soup = BeautifulSoup(html, "html.parser")
        titles = soup.find_all("div", class_="list-title")

        # Extrai os títulos limpos
        articles = []
        for title in titles:
            title_text = title.text.strip().replace("Title:", "").strip()
            articles.append(title_text)

        return articles
