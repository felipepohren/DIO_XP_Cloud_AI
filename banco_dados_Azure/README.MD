 # Resumo: Configuração de Banco de Dados no Microsoft Azure
O Azure oferece serviços de bancos de dados gerenciados, o que significa que você não precisa se preocupar com infraestrutura, backups, atualizações ou alta disponibilidade — tudo isso é gerenciado pela plataforma.

## Etapas para Criar um Banco de Dados no Azure (ex: Azure SQL Database)
1. Acessar o Azure Portal
URL: https://portal.azure.com

Navegue até "Banco de Dados SQL" → "Criar"

2. Informações Básicas
Assinatura: Conta de cobrança.

Grupo de Recursos: Onde o banco e servidor lógico ficarão organizados.

Nome do Banco de Dados: Defina um nome único.

Servidor:

Criar novo ou usar existente.

Inclui nome, login de administrador e localização (região).

Este “servidor lógico” será o ponto de acesso ao banco.

3. Configuração de Computação e Preço
Modelo de compra:

DTU-based (modelo antigo)

vCore-based (modelo atual — mais flexível e previsível)

Camada de serviço:

Basic / Standard / Premium (DTU)

General Purpose / Business Critical / Hyperscale (vCore)

Escalabilidade:

Pode ser ajustada verticalmente (CPU/memória) e horizontalmente (instâncias replicadas).

4. Configurações de Backup e Redundância
Backups automáticos: configuráveis (retenção padrão de 7 a 35 dias).

Redundância de armazenamento:

Local (LRS), geográfica (GRS), ou zona (ZRS).

5. Regras de Firewall e Acesso
Defina IPs permitidos para conexão.

Pode permitir o acesso do seu IP atual.

Integração com Azure Active Directory para controle de acesso baseado em identidade.

6. Configurações Adicionais
Importar banco existente: usar arquivo .bacpac.

Colação: define ordenação e sensibilidade de caracteres.

Versão do SQL Server: selecione se for compatível com versões anteriores.

7. Revisar + Criar
Analise o resumo da instância.

Clique em “Criar”. O provisionamento leva alguns minutos.

## Configurações Pós-Criação
Conexão com ferramentas externas:

Ex: Azure Data Studio, SQL Server Management Studio (SSMS), Visual Studio, aplicativos.

String de Conexão: Disponível no painel da instância.

Consultas SQL via portal: Há um editor SQL online embutido.

Monitoramento: Use o Azure Monitor ou Query Performance Insight.

Failover automático: Incluído em instâncias premium.

Geo-replicação: Para alta disponibilidade entre regiões.

