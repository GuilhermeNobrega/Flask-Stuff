# Instalação do Flask

## Crie um ambiente de desenvolvimento completo para seus projetos Flask!

Este guia detalhado o ajudará a instalar e configurar o Flask em seu ambiente local, permitindo que você comece a criar aplicações web poderosas e dinâmicas.

### Pré-requisitos:

Para iniciar, certifique-se de ter os seguintes softwares instalados em sua máquina:

- Python: A linguagem de programação base para o desenvolvimento de aplicações Flask.
- pip: O gerenciador de pacotes Python para instalar e gerenciar bibliotecas e dependências.

### Verifique a instalação:

Para confirmar se o Python e o pip estão instalados corretamente, abra um terminal e execute os seguintes comandos:

```bash
python --version
pip --version

```

## Instalação do Flask:

Com os pré-requisitos em mãos, instale o Flask usando o pip:

```bash
pip install Flask
flask --version
pip show flask

```

<h2>Estrutura do Projeto Flask</h2>

    <table>
        <thead>
            <tr>
                <th>Diretório/Arquivo</th>
                <th>Descrição</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>meu_projeto/</td>
                <td>Diretório raiz do projeto</td>
            </tr>
            <tr>
                <td>├── app/</td>
                <td>Diretório principal da aplicação</td>
            </tr>
            <tr>
                <td>│   ├── static/</td>
                <td>Arquivos estáticos (CSS, JavaScript, imagens)</td>
            </tr>
            <tr>
                <td>│   ├── templates/</td>
                <td>Arquivos de template HTML</td>
            </tr>
            <tr>
                <td>│   ├── __init__.py</td>
                <td>Arquivo de inicialização da aplicação</td>
            </tr>
            <tr>
                <td>│   └── routes.py</td>
                <td>Arquivo de rotas e lógica da aplicação</td>
            </tr>
            <tr>
                <td>├── venv/</td>
                <td>Ambiente virtual Python (opcional)</td>
            </tr>
            <tr>
                <td>├── README.md</td>
                <td>Arquivo de documentação do projeto</td>
            </tr>
            <tr>
                <td>└── main.py</td>
                <td>Ponto de entrada da aplicação</td>
            </tr>
        </tbody>
    </table>

  ## Recursos Adicionais para Flask

- [Documentação Flask (Português)](https://readthedocs.org/projects/flask/)
- [Download do Python](https://www.python.org/downloads/)
- [Tutorial Flask no YouTube](https://m.youtube.com/watch?v=Z1RJmh_OqeA)
