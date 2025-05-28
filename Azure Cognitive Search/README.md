# Resumo do lab. Explorando o Azure AI Search


Link do tutorial do laboratório:
    https://microsoftlearning.github.io/mslearn-ai-fundamentals/Instructions/Labs/11-ai-search.html


## Etapas:

* Criação do recurso Azure AI Search
* Criação do recurso Azure AI Services
* Criação do storage account e container de dados
* Upload dos dados de review dos clientes
* Configuração do Azure AI Search para criação de insights a partir dos dados
    * Localização
    * Palavras-chave
    * Detecção de sentimento
    * Geração de imagens
* Visualização dos insights no search explorer
* Visualização das imagens geradas


## Resultados:

### Search explorer:

* Filtrando por sentimento positivo foram encontrados 5 registros.
* Filtrando por sentimento negativo foi encontrado 1 registro conforme previu o tutorial:
    {
    "@odata.context": "https://aisearch3444.search.windows.net/indexes('coffee-index')/$metadata#docs(*)",
    "@odata.count": 1,
    "value": [
        {
        "@search.score": 1.89712,
        "content": "Review: Today I was truly disappointed with how long I had to wait for the pastries I ordered ahead of time. When I got my box, some of the pastries seemed stale. Terrible experience!  \nDate: October 23, 2018\nLocation: Chicago, Illinois \n\n",
        "metadata_storage_path": "aHR0cHM6Ly9tZXVhcm1hemVuYW1lbnRvNTg2NzQ4LmJsb2IuY29yZS53aW5kb3dzLm5ldC9maWxlcy9yZXZpZXctOC5kb2N4",
        "locations": [
            "Chicago",
            "Illinois"
        ],
        "keyphrases": [
            "Terrible experience",
            "Review",
            "pastries",
            "time",
            "box",
            "Date",
            "October",
            "Location",
            "Chicago",
            "Illinois"
        ],
        "sentiment": "[\"negative\"]",
        "merged_content": "Review: Today I was truly disappointed with how long I had to wait for the pastries I ordered ahead of time. When I got my box, some of the pastries seemed stale. Terrible experience!  \nDate: October 23, 2018\nLocation: Chicago, Illinois \n\n",
        "text": [],
        "layoutText": [],
        "imageTags": [],
        "imageCaption": []
        }
    ]
    }


### Knoledge store:

Foi possível visualizar as imagens geradas, todas referentes a cafeterias.
Verificar pasta "imagens"