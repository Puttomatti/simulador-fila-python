import time
from collections import deque


def gerar_requisicoes(qtd_requisicoes):
    """Gera requisições simuladas para a fila de atendimento."""

    requisicoes = deque()

    nomes_clientes = [
        "Arthur",
        "Ana Lívia",
        "Deborah",
        "Lavínia",
    ]

    problemas = [
        "Problema de conexão",
        "Erro no sistema",
        "Dúvida sobre faturamento",
        "Solicitação de suporte",
    ]

    for i in range(1, qtd_requisicoes + 1):
        horario = time.strftime("%H:%M:%S")

        requisicao = {
            "id": i,
            "cliente": nomes_clientes[(i - 1) % len(nomes_clientes)],
            "problema": problemas[(i - 1) % len(problemas)],
            "horario": horario,
        }

        requisicoes.append(requisicao)
        time.sleep(0.1)

    return requisicoes


def adicionar_requisicao(fila_requisicoes, nova_requisicao):
    """Adiciona uma nova requisição ao final da fila."""

    fila_requisicoes.append(nova_requisicao)


def processar_requisicao(fila_requisicoes):
    """Processa a primeira requisição da fila seguindo a ordem FIFO."""

    if not fila_requisicoes:
        print("Nenhuma requisição para processar.")
        return

    requisicao = fila_requisicoes.popleft()

    print(
        f"Processando: ID: {requisicao['id']} | "
        f"Cliente: {requisicao['cliente']} | "
        f"Problema: {requisicao['problema']} | "
        f"Horário: {requisicao['horario']}"
    )

    time.sleep(1)


def imprimir_fila(fila_requisicoes, titulo="Fila de requisições:"):
    """Exibe as requisições que estão aguardando atendimento."""

    print(f"\n{titulo}")

    if not fila_requisicoes:
        print("Fila vazia.")
        return

    for requisicao in fila_requisicoes:
        print(
            f"ID: {requisicao['id']} | "
            f"Cliente: {requisicao['cliente']} | "
            f"Problema: {requisicao['problema']} | "
            f"Horário: {requisicao['horario']}"
        )


def principal():
    qtd_inicial_requisicoes = 5

    fila_requisicoes = gerar_requisicoes(qtd_inicial_requisicoes)

    imprimir_fila(
        fila_requisicoes,
        "Fila inicial de requisições:",
    )

    print("\nProcessamento das requisições:")

    while fila_requisicoes:
        processar_requisicao(fila_requisicoes)

    nova_requisicao = {
        "id": qtd_inicial_requisicoes + 1,
        "cliente": "Cliente João",
        "problema": "Reclamação de atraso no serviço",
        "horario": time.strftime("%H:%M:%S"),
    }

    adicionar_requisicao(
        fila_requisicoes,
        nova_requisicao,
    )

    imprimir_fila(
        fila_requisicoes,
        "Nova requisição adicionada:",
    )

    print("\nProcessando nova requisição:")
    processar_requisicao(fila_requisicoes)

    print("\nProcessamento finalizado. Script encerrado.")


if __name__ == "__main__":
    principal()
