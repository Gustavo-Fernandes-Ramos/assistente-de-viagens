# Servidor

servidor da aplicação **Assistente de Viagens**

## Observações
Devido a natureza do protocolo HTTP, nem o cliente nem o navegador podem reter informações entre diferentes solicitações nas páginas da web.

## Requisitos

### Avaliação de atrações para aprendizado de máquina

- fornecer tela de avaliação
- fornecer locais de diferentes categorias para servirem de primeira avaliação para um viajante
- receber a avaliação das atrações e com base nelas definir as features iniciais do viajante

### Autenticar viajante

- autenticar token do viajante
- criar novo token de autenticação para o viajante
- deletar token do viajante após longo período de inatividade

### Montar roteiro de viagem

- fornecer tela formulário + recomendação
- fornecer recomendações de locais com base na predição do knn tendo as features do viajante como parâmetro
- receber informações básicas + recomendações aprovadas pelo viajante

- montar roteiro com base nas informações + recomendações
- fornecer tela roteiro
- fornecer roteiro de viagem personalizado

### Armazenar roteiros de viagem criados anteriormente para serem visualizados pelo viajante

- salvar roteiro de viagem no banco de dados, associado ao token do viajante
- fornecer tela lista roteiros salvos
- fornecer informações básicas de todos os roteiros salvos do viajante

- fornecer tela roteiro salvo
- receber solicitação para remover roteiro

### Geral

- fornecer tela inicial
- fornecer tela detalhes
- cancelar qualquer operação em andamento a qualquer momento, para determinado usuário com token

