Projeto Django com Docker
=========================

Este documento contém instruções completas para configurar e rodar o projeto em uma nova máquina.

Pré-requisitos
--------------
- Docker (https://www.docker.com/get-started) instalado.
- Docker Compose (https://docs.docker.com/compose/install/) instalado.

Clonando o Repositório
----------------------
Abra o terminal e execute:

    git clone <URL_DO_REPOSITORIO>
    cd docker-django-estudo

Configuração do Ambiente
------------------------
1. Variáveis de Ambiente:
   - O arquivo .env encontra-se em "dotenv_files/.env". Certifique-se de que
     as informações (chave secreta, dados de banco, etc.) estão corretas.
   - Atenção: Utilize "#" para comentários em vez de "//".

2. Permissões do Script:
   - O script "scripts/commands.sh" deve ter permissão de execução.
   - No Windows (usando Git Bash ou WSL), execute:
     
       chmod +x scripts/commands.sh

Build e Execução
----------------
1. Construir a Imagem (se necessário):
   
       docker-compose build

2. Subir os Containers:
   
       docker-compose up

   O container do Django ("djangoapp") aguardará o PostgreSQL ("psql") ficar
   disponível, aplicará migrações, coletará arquivos estáticos e iniciará o
   servidor na porta 8000.

Acessando o Projeto
-------------------
- Aplicação Django:
  - Acesse no navegador: http://127.0.0.1:8000/
    (Se a rota raiz não existir, crie uma view ou ajuste as rotas.)

- Admin do Django:
  - Acesse: http://127.0.0.1:8000/admin
  - Utilize um superusuário para fazer login (caso você já o tenha criado).

Executando Comandos do Django
-----------------------------
Use o comando docker-compose exec para executar comandos no container, por exemplo:

    docker-compose exec djangoapp python manage.py migrate

Exemplo para criar um superusuário:

    docker-compose exec djangoapp python manage.py createsuperuser

Desenvolvimento
---------------
- Volumes Mapeados:
  O diretório "djangoapp" está mapeado para o container, portanto, alterações
  no código serão refletidas imediatamente.

- Rebuild da Imagem:
  Se você modificar dependências ou o Dockerfile, será necessário rebuildar:
  
      docker-compose build
      docker-compose up

Parada dos Containers
---------------------
Para interromper, pressione Ctrl+C no terminal onde o docker-compose está rodando.

Para remover os containers em execução, use:

    docker-compose down