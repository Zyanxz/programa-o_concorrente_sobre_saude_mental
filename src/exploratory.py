from pathlib import Path
import csv
from collections import Counter
from time import perf_counter


REVIEWS_DIR = Path("data/raw/Game Reviews")
LIMITE_ARQUIVOS = 50


NEGATIVE_KEYWORDS = {
    "bugs": ["bug", "bugs", "glitch", "glitches", "broken"],
    "crashes": ["crash", "crashes", "crashed", "crashing"],
    "performance": ["lag", "fps", "stutter", "optimization", "optimized", "performance"],
    "servers": ["server", "servers", "connection", "disconnect", "matchmaking"],
    "price": ["price", "expensive", "overpriced", "money"],
    "microtransactions": ["microtransaction", "microtransactions", "pay to win", "p2w", "dlc"],
    "content": ["content", "short", "empty", "repetitive", "boring"],
    "balance": ["balance", "balanced", "unbalanced", "nerf", "buff"],
}

POSITIVE_KEYWORDS = {
    "gameplay": ["gameplay", "combat", "mechanics", "controls"],
    "story": ["story", "narrative", "plot", "characters"],
    "soundtrack": ["soundtrack", "music", "sound"],
    "visuals": ["graphics", "art", "visuals", "atmosphere"],
    "value": ["worth", "cheap", "sale", "value", "price"],
    "fun": ["fun", "enjoyable", "addictive", "replayable"],
    "world": ["world", "open world", "exploration", "map"],
}


def contar_temas(review_text, keywords_by_category):
    temas_encontrados = Counter()

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
                temas_positivos.update(contar_temas(review_text, POSITIVE_KEYWORDS))

            elif recommend == "Not Recommended":
                temas_negativos.update(contar_temas(review_text, NEGATIVE_KEYWORDS))

    return total_reviews, recomendacoes, temas_positivos, temas_negativos


def main():
    print("=== TESTE SEQUENCIAL COM ANÁLISE DE TEMAS ===")

    if not REVIEWS_DIR.exists():
        print("Erro: pasta de reviews não encontrada.")
        return

    arquivos_csv = sorted(REVIEWS_DIR.glob("*.csv"))
    arquivos_teste = arquivos_csv[:LIMITE_ARQUIVOS]

    print(f"Pasta analisada: {REVIEWS_DIR}")
    print(f"Total de arquivos CSV encontrados: {len(arquivos_csv)}")
    print(f"Arquivos que serão processados neste teste: {len(arquivos_teste)}")

    total_geral_reviews = 0
    recomendacoes_gerais = Counter()
    temas_positivos_gerais = Counter()
    temas_negativos_gerais = Counter()
    arquivos_com_erro = 0

    inicio = perf_counter()

    for index, csv_path in enumerate(arquivos_teste, start=1):
        try:
            total_reviews, recomendacoes, temas_positivos, temas_negativos = processar_arquivo(csv_path)

            total_geral_reviews += total_reviews
            recomendacoes_gerais.update(recomendacoes)
            temas_positivos_gerais.update(temas_positivos)
            temas_negativos_gerais.update(temas_negativos)

            print(f"[{index}/{len(arquivos_teste)}] {csv_path.name} - {total_reviews} reviews")

        except Exception as erro:
            arquivos_com_erro += 1
            print(f"Erro ao processar {csv_path.name}: {erro}")

    fim = perf_counter()
    tempo_total = fim - inicio

    print("\n=== RESULTADO GERAL DO TESTE ===")
    print(f"Arquivos processados: {len(arquivos_teste)}")
    print(f"Arquivos com erro: {arquivos_com_erro}")
    print(f"Total de reviews processadas: {total_geral_reviews}")

    print("\nDistribuição geral das recomendações:")
    for recommend, quantidade in recomendacoes_gerais.items():
        print(f"{recommend}: {quantidade}")

    print("\nTemas mais comuns em reviews positivas:")
    for tema, quantidade in temas_positivos_gerais.most_common():
        print(f"{tema}: {quantidade}")

    print("\nTemas mais comuns em reviews negativas:")
    for tema, quantidade in temas_negativos_gerais.most_common():
        print(f"{tema}: {quantidade}")

    print("\n=== DESEMPENHO ===")
    print(f"Tempo total: {tempo_total:.4f} segundos")

    if tempo_total > 0:
        reviews_por_segundo = total_geral_reviews / tempo_total
        arquivos_por_segundo = len(arquivos_teste) / tempo_total

        print(f"Reviews por segundo: {reviews_por_segundo:.2f}")
        print(f"Arquivos por segundo: {arquivos_por_segundo:.2f}")


if __name__ == "__main__":
    main()