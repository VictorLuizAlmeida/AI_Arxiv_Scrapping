import os
import csv
from arxiv_scraper.arxiv_scraper import ArxivScraper


def save_to_csv(data, output_file):
    """
    Salva os dados em um arquivo CSV.

    Args:
        data (list): Lista de strings (títulos dos artigos).
        output_file (str): Caminho completo do arquivo CSV de saída.
    """
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Título"])  
        for row in data:
            writer.writerow([row])

    print(f"Os dados foram salvos em: {output_file}")


if __name__ == "__main__":
    url = "https://arxiv.org/list/cs.AI/recent"

    print(f"Scraping da página: {url}")
    scraper = ArxivScraper(url)

    try:
        html = scraper.fetch_page()
        articles = scraper.parse(html)

        print(f"Encontrados {len(articles)} artigos:")
        for i, article in enumerate(articles[:50], 1): 
            print(f"{i}. {article}")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        output_file = os.path.join(current_dir, "arxiv_articles.csv")

        save_to_csv(articles, output_file)
    except Exception as e:
        print(f"Erro durante o scraping: {e}")
