# Servidor

## Requisitos

### Autenticar viajante

- fornecer tela inicial

- autenticar token do viajante

- criar novo token de autenticação para o viajante

- deletar token do viajante após longo período de inatividade

### Montar roteiro de viagem

- fornecer tela formulário viagem

- receber informações básicas sobre a viagem

- cancelar qualquer operação em andamento a qualquer momento, para determinado usuário com token


- fornecer tela detalhes

- receber a avaliação positiva/negativa das 5 atrações e com base nelas definir as características iniciais do viajante


- fornecer tela recomendação

- receber a avaliação negativa das n atrações e com base nelas alterar as características do viajante

- receber a avaliação positiva das n atrações e com base nelas alterar as características do viajante

- receber atrações com as quais o roteiro deve ser montado

### Visualizar roteiros de viagem criados anteriormente

- fornecer tela roteiro

- fornecer roteiro com todas as informações pertinentes

- salvar roteiro no banco de dados, associado ao token do viajante


- fornecer tela roteiros salvos

- fornecer informações básicas dos roteiros salvos

- receber solicitação para remover roteiro

### Avaliação de atrações para aprendizado de máquina

- fornecer tela de avaliação

- fornecer 5 locais de diferentes categorias para servirem de primeira avaliação para um viajante