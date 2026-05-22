from collections import Counter
import csv

from keywords import NEGATIVE_KEYWORDS, POSITIVE_KEYWORDS


def contar_temas(review_text, keywords_by_category):
    temas_encontrados = Counter()

    if not review_text:
        return temas_encontrados

    texto = review_text.lower()

    for categoria, palavras in keywords_by_category.items():
        for palavra in palavras:
            if palavra in texto:
                temas_encontrados[categoria] += 1
                break

    return temas_encontrados


def processar_arquivo(csv_path):
    total_reviews = 0
    recomendacoes = Counter()
    temas_positivos = Counter()
    temas_negativos = Counter()

    with open(csv_path, mode="r", encoding="utf-8", errors="replace", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_reviews += 1

            recommend = row.get("recommend", "").strip()
            review_text = row.get("review", "")

            recomendacoes[recommend] += 1

            if recommend == "Recommended":
                temas_positivos.update(
                    contar_temas(review_text, POSITIVE_KEYWORDS)
                )

            elif recommend == "Not Recommended":
                temas_negativos.update(
                    contar_temas(review_text, NEGATIVE_KEYWORDS)
                )

    return {
        "arquivo": csv_path.name,
        "total_reviews": total_reviews,
        "recomendacoes": recomendacoes,
        "temas_positivos": temas_positivos,
        "temas_negativos": temas_negativos,
    }