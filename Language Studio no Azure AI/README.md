Anotações referentes aos laboratórios

# Laboratório Azure Speech Studio

passo a passo:
1. entrar no portal: https://ai.azure.com e realizar login;
2. acessar https://ai.azure.com/managementCenter/allResources 
	* clicar em "create new";
	* Escolher "Recurso do hub de IA"
3. Seguir o wizard de criação do projeto
	* Mantive nome de projeto default
	* Escolher uma assinatura
	* Região = Brazil South (suponho que usará o servidor mais próximo)
4. Na aba esquerda acessar "Playgrounds"
    * Escolher o playground de fala

5. Após a utulização, apagar todos arquivos carregados para evitar custo extra.

## Explorando Fala para texto
    * Escolher "Transcrição em tempo real"
    * É possível gravar um audio ou carregar um arquivo de audio.
    * A transcrição é feita na janela da direita.
    * É possível testar outros recursos, como tradução, por exemplo.



# Laboratório Azure Language Studio

passo a passo:
1. entrar no portal: https://ai.azure.com e realizar login;
2. acessar https://ai.azure.com/managementCenter/allResources 
	* clicar em "create new";
	* Escolher "Recurso do hub de IA"
3. Seguir o wizard de criação do projeto
	* Mantive nome de projeto default
	* Escolher uma assinatura
	* Região = Brazil South (suponho que usará o servidor mais próximo)
4. Na aba esquerda acessar "Playgrounds"
    * Escolher o playground de idiomas

## Explorando o playground de idiomas
    * Colar um texto de exemplo e clicar em "executar"

    - Na frase  The Royal Hotel, London, United Kingdom
        * "Hotel" foi identificado como organização. Poderia ter sido "Royal Hotel"
        * "London, United" foi identificado como enderço. Poderia ter sido "London, United Kingdom"
        * 5/6/2018 foi classificado como data
        * a palavra "now" foi classificada como datetime
    * A resposta pode ser visualizada como texto ou JSON. O formato Json é interessante para usar diretamente em algum código.
