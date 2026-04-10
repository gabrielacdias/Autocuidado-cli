# 🌿 CLI Autocuidado & Hidratação

**Versão:** 1.0.0
**Autor:** Gabriela Costa Dias
**Status do Projeto:** ![Pipeline de CI](https://github.com/[gabrielacdias]/Autocuidado-cli/actions/workflows/ci.yml/badge.svg)

## Problema Real
Atualmente, devido ao cotidiano muito movimentado e corrido, é comum que as pessoas esqueçam de se hidratar e de realizar atividades de autocuidado, o que prejudica diariamente a vida desses indivíduos.

## Proposta de solução
Assim, por meio de um checklist simples e direto via terminal (CLI), é disponibilizado para usuários listar metas de autocuidado e hidratação, como "beber 2l litros de água" ou "meditação", de modo que consigam melhorar os hábitos diários, organizando a rotina, e assim, melhorar a saúde e o bem-estar.

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
    ```
3.  **Verifique o GitHub:** Entre no seu link do GitHub e veja se o texto aparece bonito na página inicial do repositório.

**Agora você tem tudo!** A aplicação funciona, os testes passam, o Lint está config

