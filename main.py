import requests 
from bs4 import BeautifulSoup

# main.py
from arxiv_scraper.arxiv_scraper import ArxivScraper

if __name__ == "__main__":
    # URL da seção de IA do Arxiv
    url = "https://arxiv.org/list/cs.AI/recent"

    print(f"Scraping da página: {url}")
    scraper = ArxivScraper(url)

    try:
        # Faz a requisição e o parsing
        html = scraper.fetch_page()
        articles = scraper.parse(html)

        # Exibe os resultados
        print(f"Encontrados {len(articles)} artigos:")
        for i, article in enumerate(articles[:50], 1): 
            print(f"{i}. {article}")
    except Exception as e:
        print(f"Erro durante o scraping: {e}")
