import sys

class AutocuidadoManager:
    def __init__(self):
        # Lista de dicionários: [{'tarefa': str, 'concluída': bool}]
        self.metas = []

    def adicionar_meta(self, nome_meta):
        if not nome_meta.strip():
            return False, "Erro, o nome da meta não pode estar vazio."
        self.metas.append({'tarefa': nome_meta.strip(), "concluída": False})
        return True, f"Meta '{nome_meta}' adicionada com sucesso!"

    def concluir_meta(self, indice):
        try:
            if self.metas[indice]["concluída"]:
                return False, "Essa meta já foi concluída."
            self.metas[indice]["concluída"] = True
            return True, "Meta concluída! Parabéns por estar cuidando de você."
        except IndexError:
            return False, "Erro. Meta não encontrada."

    def listar_metas(self):
        return self.metas

def menu():
    manager = AutocuidadoManager()

    print("\n--- 🌿 CLI Autocuidado & Hidratação 🌿 ---")
    print("Versão 1.0.0")

    while True:
        print("\n1. Adicionar Meta (ex: Beber Água)")
        print("2. Listar Metas")
        print("3. Concluir Meta")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("O que você vai fazer por você hoje? ")
            sucesso, msg = manager.adicionar_meta(nome)
            print(msg)

        elif opcao == "2":
            metas = manager.listar_metas()
            if not metas:
                print("\nSua lista está vazia, você não possui nenhumaa meta. Vamos começar a cuidar de você agora? ")
            else:
                print("\n--- MINHAS METAS ---")
                for i, m in enumerate(metas):
                    status = "✅" if m["concluída"] else "❌"
                    print(f"{i} - {status} {m['tarefa']}")

        elif opcao == "3":
            try:
                idx  = int(input("Digite o número da meta concluída: "))
                sucesso, msg = manager.concluir_meta(idx)
                print(msg)
            except ValueError:
                print("Por favor, digite um número válido.")

        elif opcao == "4":
            print("Até logo. Não se esqueça de beber água. 💧")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()








