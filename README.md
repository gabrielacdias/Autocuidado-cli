# 🌿 CLI Autocuidado & Hidratação
> 🚀 **Link do Deploy (Release Oficial v2.0.0):** [Acesse a Versão Intermediária Aqui](https://github.com/gabrielacdias/Autocuidado-cli/releases/tag/v2.0.0)
> 📌 **Issue Vinculada:** Resolve a demanda documentada na Issue #2.

**Versão:** 1.0.0
**Autor:** Gabriela Costa Dias
**Status do Projeto:** ![Pipeline de CI](https://github.com/[gabrielacdias]/Autocuidado-cli/actions/workflows/ci.yml/badge.svg)

## Problema Real
Atualmente, devido ao cotidiano muito movimentado e corrido, é comum que as pessoas esqueçam de se hidratar e de realizar atividades de autocuidado, o que prejudica diariamente a vida desses indivíduos.

## Proposta de solução
Assim, por meio de um checklist simples e direto via terminal (CLI), é disponibilizado para usuários listar metas de autocuidado e hidratação, como "beber 2l litros de água" ou "meditação", de modo que consigam melhorar os hábitos diários, organizando a rotinas, e assim, melhorar a saúde e o bem-estar.

## Funcionalidades principais
- Registrar metas para autocuidado.
- Listas metas pendentes.
- Marcar metas como concluídas.
- Listas metas concluídas.

## Tecnologias utilizadas
- Python 3.10+
- Pytest (testes Unitários)
- Flake8 (Análise Estática/Lint)
- GitHub Actions (CI)

## Instrução de Instalação
Certifique-se de ter o **Python 3.10 ou superior** instalado.
1. Clone do repositório:
   ```bash
   git clone https://github.com/gabrielacdias/Autocuidado-cli]
   ```
2. Acesse o diretório do projeto:
    ```bash
   cd Autocuidado-cli
   ```
3. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```
   
## Instruções de Execução
Para iniciar a aplicação e gerenciar o seu checklist, execute o comando:
    ```bash
    python src/app.py
    ```

## Instruções para Rodar os Testes
Para validar se as funcionalidades estão operando corretamente e garantir a integridade do código:
    ```bash
    python -m pytest
    ```

## Instruções para Rodar o Lint
Para verificar a padronização e qualidade estática do código (estilo de codificação):
    ```bash
    python -m flake8 src/
    ```

## Integração Contínua (CI)
O projeto conta com um workflow no GitHub Actions configurado no arquivo ci.yml. A cada push ou pull request, a pipeline executa automaticamente:
- Configuração do ambiente Python. 
- Instalação de dependências. 
- Verificação de Linting (Flake8). 
- Execução de Testes Automatizados (Pytest).

**Envie as mudanças:** No terminal do PyCharm, faça o commit e push final:
    ```bash
    git add README.md
    git commit -m "docs: finaliza documentação detalhada no README"
    git push
    ```
3.  **Verifique o GitHub:** Entre no seu link do GitHub e veja se o texto aparece bonito na página inicial do repositório.

**Agora você tem tudo!** A aplicação funciona, os testes passam, o Lint está config

## 🎯 Sobre o Projeto (Etapa Intermediária)
Esta é a evolução da ferramenta CLI de Autocuidado. Agora, a aplicação conecta-se à internet para buscar frases motivacionais diárias, agregando valor à rotina de cuidados do usuário.

### 🛠️ Novas Funcionalidades Implementadas:
* **Consumo de API Pública:** Integração com a API *ZenQuotes* para fornecimento de citações.
* **Tradução Automática:** Uso da biblioteca `deep-translator` para exibir as frases totalmente em português.
* **Qualidade de Software:** Criação de testes de integração automatizados (`test_app.py`) com `unittest`.

### 💻 Como Instalar e Rodar o Deploy localmente:
1. Faça o download do código-fonte na aba de [Releases](https://github.com/gabrielacdias/Autocuidado-cli/releases/tag/v2.0.0).
2. Instale as dependências executando no terminal:
   ```bash
   pip install requests deep-translator
3. Execute o programa:
    ```bash
   python app.py