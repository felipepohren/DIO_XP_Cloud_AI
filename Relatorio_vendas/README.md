# Desafio Insights de relatório de vendas 

## Modelos utilizados

* gemini 2.5 pro (preview)
    * a planilha teve que ser convertida para "csv" e salvo em "txt" pois o modelo não tem suporte diretamente para "xlsx"
---
## estrutura de entrega 

- Os dados de entrada tratados, construídos durante as aulas estão armazenados na pasta "data\processed_data".
- Na pasta "prompts" estão armazenados os prompts utilizados para conversa com o modelo
- Os resultados obtidos estão na pasta "insights".

---

## A estratégia utilizada:

1. Fornecer o arquivo de dados ao modelo;
2. Criar uma contextualização;
3. criar uma lista de questões a serem respondidas; 
4. Fornecer informações e requisitos a respeito dos dados;
5. Solicitar a analise dos dados;
6. Gerar conclusões.

A técnica utilizada é a de cadeia de pensamento onde são fornecidas instruções detalhadas para que o modelo execute passo a passo e consiga interpretar de forma clara.

---
## Prompt utilizado no projeto

### Contextualização:
* A Meganium é uma empresa fabricante de videogames, responsável pela fabricação e distribuição;
* A venda dos produtos ao consumidor final é de responsabilidade das revendas;
* A fabricante tem dificuldade em planejar a produção e logística de distribuição;
* A fabricante requer uma análise de dados das revendas para estimar a fabricação e logística;
* A análise deve ser feita a partir das perguntas a serem respondidas;
* Para a análise é fornecida uma planilha consolidada com dados de vendas fornecidos pelas revendas.

### Questões 
* Qual modelo de produto é mais vendido por filial?
* Qual modelo de produto é mais vendido por país?
* Qual modelo de produto é mais vendido por idade do comprador?
* Qual filial fornece o maior desconto?
* Qual idade média do comprador que obtem maior desconto?
* Qual o valor médio de invoice por país e por idade do comprador?
* Qual época do ano (1Q, 2Q, 3Q ou 4Q) representa maior volume de vendas?

### Dados de entrada:
* Os códigos entre chaves "{ }" representam o nome da coluna onde o dado referido está contido;
* Os arquivos fornecidos são dados de vendas de 3 revendas {site} da fabricante de nome Meganium;
* Os dados financeiros estão estão apresentados em diferentes moedas {currency} e devem ser convertidos para dolar com a ultima cotação disponível para correta comparação;

### Dados de saída:
* As respostas devem ser feitas exclusivamente com base nos dados, com exceção da conversão monetária para os valores financeiros;
* Responda as perguntas feitas no tópico "Questões" com base no contexto e nos dados de entrada;
* As respostas devem ser objetivas e sucintas, podem conter pequenos textos, valores e tabelas de resumo;
* Além das perguntas, pode sugerir alguma outra informação relevante para o objetivo;
* Com base nas respostas obtidas, gerar uma lista de Insights relevantes para o objetivo. 

---
## Conclusões

* O modelo entendeu bem os dados e executou conforme foi solicitado;
* Além de responder as questões o modelo gerou insights e sugeriu ações a serem tomadas para obter melhorias na produção e logística;
* Perguntas adicionais sobre a estrategia de descontos da Shopee foram respondidas com instruções para tomada de ações devido a falta de dadso de custo de produção;
* O modelo manteve o contexto em perguntas adicionais.

