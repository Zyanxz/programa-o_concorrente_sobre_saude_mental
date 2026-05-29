from pathlib import Path
from collections import Counter
from time import perf_counter
from multiprocessing import Pool
import argparse
import json

from analyzer import processar_arquivo


REVIEWS_DIR = Path("data/raw/Game Reviews")
RESULTS_DIR = Path("results")


def salvar_resultado(resultado, caminho_saida):
    with open(caminho_saida, mode="w", encoding="utf-8") as file:
        json.dump(resultado, file, indent=4, ensure_ascii=False)


def criar_argumentos():
    parser = argparse.ArgumentParser(
        description="Processamento paralelo de reviews da Steam usando multiprocessing."
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=50,
        help="Quantidade de arquivos CSV que serão processados. Padrão: 50."
    )

    parser.add_argument(
        "--processes",
        type=int,
        default=2,
        help="Quantidade de processos paralelos. Padrão: 2."
    )

    return parser.parse_args()


def main():
    args = criar_argumentos()

    print("=== PROCESSAMENTO PARALELO COM MULTIPROCESSING ===")

    if not REVIEWS_DIR.exists():
        print(f"Erro: pasta de reviews não encontrada: {REVIEWS_DIR}")
        return

    if args.limit <= 0:
        print("Erro: o limite precisa ser maior que zero.")
        return

    if args.processes <= 0:
        print("Erro: a quantidade de processos precisa ser maior que zero.")
        return

    RESULTS_DIR.mkdir(exist_ok=True)

    arquivos_csv = sorted(REVIEWS_DIR.glob("*.csv"))
    arquivos_processar = arquivos_csv[:args.limit]

    print(f"Pasta analisada: {REVIEWS_DIR}")
    print(f"Total de arquivos CSV encontrados: {len(arquivos_csv)}")
    print(f"Arquivos que serão processados: {len(arquivos_processar)}")
    print(f"Processos utilizados: {args.processes}")

    total_reviews = 0
    recomendacoes_gerais = Counter()
    temas_positivos_gerais = Counter()
    temas_negativos_gerais = Counter()

    arquivos_com_erro = 0
    erros = []

    inicio = perf_counter()

    with Pool(processes=args.processes) as pool:
        resultados = pool.imap_unordered(processar_arquivo, arquivos_processar)

        for index, resultado_arquivo in enumerate(resultados, start=1):
            try:
                total_reviews += resultado_arquivo["total_reviews"]
                recomendacoes_gerais.update(resultado_arquivo["recomendacoes"])
                temas_positivos_gerais.update(resultado_arquivo["temas_positivos"])
                temas_negativos_gerais.update(resultado_arquivo["temas_negativos"])

                print(
                    f"[{index}/{len(arquivos_processar)}] "
                    f"{resultado_arquivo['arquivo']} - "
                    f"{resultado_arquivo['total_reviews']} reviews"
                )

            except Exception as erro:
                arquivos_com_erro += 1
                erros.append({
                    "erro": str(erro)
                })
                print(f"Erro ao agregar resultado: {erro}")

    fim = perf_counter()
    tempo_total = fim - inicio

    reviews_por_segundo = 0
    arquivos_por_segundo = 0

    if tempo_total > 0:
        reviews_por_segundo = total_reviews / tempo_total
        arquivos_por_segundo = len(arquivos_processar) / tempo_total

    resultado_final = {
        "modo": "paralelo_multiprocessing",
        "processos": args.processes,
        "arquivos_csv_encontrados": len(arquivos_csv),
        "arquivos_processados": len(arquivos_processar),
        "arquivos_com_erro": arquivos_com_erro,
        "total_reviews": total_reviews,
        "recomendacoes": dict(recomendacoes_gerais),
        "temas_positivos": dict(temas_positivos_gerais),
        "temas_negativos": dict(temas_negativos_gerais),
        "tempo_total_segundos": tempo_total,
        "reviews_por_segundo": reviews_por_segundo,
        "arquivos_por_segundo": arquivos_por_segundo,
        "erros": erros,
    }

    caminho_saida = RESULTS_DIR / (
        f"parallel_results_limit_{len(arquivos_processar)}_processes_{args.processes}.json"
    )

    salvar_resultado(resultado_final, caminho_saida)

    print("\n=== RESULTADO FINAL ===")
    print(f"Arquivos processados: {len(arquivos_processar)}")
    print(f"Arquivos com erro: {arquivos_com_erro}")
    print(f"Total de reviews processadas: {total_reviews}")

    print("\nDistribuição das recomendações:")
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
    print(f"Reviews por segundo: {reviews_por_segundo:.2f}")
    print(f"Arquivos por segundo: {arquivos_por_segundo:.2f}")

    print(f"\nResultado salvo em: {caminho_saida}")


if __name__ == "__main__":
    main()