<h1 align="center">Sistema para Gerenciar Candidatos</h1>

## Descrição do Projeto
<p align="justity">
  O sistema prover uma API RESTfull para cadastro de candidatos com contatos. As principais funcionalidades são:
</p>
<ul>
  <li>Cadastro, listagem, atualização de contatos.</li>
  <li>Adicionar e atualizar contatos por candidato.</li>
</ul>

## Restrições
<p align="justity">Não há controle de usuário.</p> 

## Executando do Projeto
<ol>
  <li>Clonar o repositório</li>
  <li>Criar o ambiente virtual - virtualenv [nome_do_ambiente]</li>
  <li>Entre na pasta do projeto - cd pasta_do_projeto </li>
  <li>Ativar o ambiente virtual - source /caminho_do_ambiente/bin/activate</li>
  <li>Executar a instalação das dependências - pip install -r requirements.txt </li>
  <li>Atualize o schema de banco de dados - ./manage.py migrate </li>
  <li>Executar a aplicação - ./manage.py runserver</li>
</ol>

## Links para as principais funcionalidades
<ul>
  <li>Listar candidatos - GET /candidate/</li>
  <li>Cadastrar candidato - POST /candidate/</li>
  <li>Detalhar candidato - GET /candidate/{id}/</li>
  <li>Atualizar candidato (enviar todos os dados) - PUT /candidate/{id}/</li>
  <li>Atualizar candidato (enviar somente os dados que deseja atualizar) - PATCH /candidate/{id}/</li>
  <li>Excluir candidato - DELETE /candidate/{id}/</li>
  <li>Adicionar contato (necessário id do candidato) - POST /candidate/{id}/contact/add/</li>
  <li>Exibir contato - GET /contact/{id}/</li>
  <li>Atualizar contato (enviar todos os dados) - PUT /contact/{id}/</li>
  <li>Atualizar contato (enviar somente os dados que irá atualizar) - PATCH /contact/{id}/</li>
</ul>

## ROTAS PARA AS SOLICITAÇÕES
### Samuca
<p align="justity">
    Para atualizar nome e sobrenome deve-se acessar a rota <strong>/candidate/{id}/</strong> e enviar os dados via método <strong>PATCH</strong>.
</p> 
<p align="justity">
    Para atualizar o contato é necessário acessar a rota <strong>/contact/{id}/</strong> e enviar os dados via método <strong>PUT</strong>, caso deseje atualizar todos os dados ou via <strong>PATCH</strong> para atualizar parcialmente.
</p> 