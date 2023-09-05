### links

**icones:** https://fonts.google.com/icons

**design das páginas:** https://www.figma.com/file/zeEImDKJikqiyY6i4Q1RRT/travel_assistant_html_prototype?type=design&node-id=0%3A1&mode=design&t=UYFGVd1Iklj40qmM-1

**kanban do projeto(notion):** https://www.notion.so/Assistente-de-Viagens-f7e79a889e3a4f9697b20c338a100ba8

# Aplicação front-end

Ao abrir o aplicativo
		- checar se o usuário possui token no servidor
		- checar status do servidor
			em caso de sucesso, ir pata a tela inicial
			em caso de erro, fechar aplicativo
	
	Implementar funcionalidades da tela inicial
		- botão "roteiros anteriores" só deve ser clicavel se o usuário já tiver um token no servidor
		- ao apertar "montar roteiro de viagem" ou "roteiros anteriores"
			- checar status do servidor
				- em caso de erro, informar ao usuário
		- ao apertar "montar roteiro de viagem":
			- ir para a tela formulario viagem
		- ao apertar "roteiros anteriores":
			- solicitar roteiros anteriores ao servidor
				- em caso de sucesso, exibir roteiros anteriores na tela roteiros salvos
				- em caso de erro, 
			- ir para a tela lista roteiros salvos
	
	Implementar funcionalidades da tela formulário viagem
		ao apertar cancelar: 
		 	- retornar a tela inicial
		ao apertar limpar: 
			- limpar campos de input
		ao apertar confirmar: 
			- validar campos de input
			- exibir mensagens de erro
			- enviar dados coletados ao servidor
			- obter resposta do servidor
				- em caso de sucesso, direcionar para a tela recomendações
				- em caso de erro, informar o usuário e retornar a tela inicial
	
	Implementar funcionalidades da tela avaliação
		requisitar locais para avaliação
		exibir locais na tela avaliação
		enviar mapeamento com (id do local -> avaliação)