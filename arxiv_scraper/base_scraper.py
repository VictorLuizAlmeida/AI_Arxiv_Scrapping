# arxiv_scraper/base_scraper.py
from abc import ABC, abstractmethod


class BaseScraper(ABC):
    """
    Classe base abstrata para definir a interface do scraping.
    """

    def __init__(self, url):
        self.url = url

    def fetch_page(self):
        """
        Faz a requisição HTTP e retorna o HTML da página.
        """
        import requests

        print(f"Buscando página: {self.url}")
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception(f"Erro ao acessar {self.url}. Código: {response.status_code}")
        return response.text

    @abstractmethod
    def parse(self, html):
        """
        Método abstrato para fazer o parsing do HTML e extrair os dados.
        Deve ser implementado pelas subclasses.
        """
        pass
