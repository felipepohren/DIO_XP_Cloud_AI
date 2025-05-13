

# Resumo sobre computação em nuvem com Microsoft Azure

## 1. Conceitos de Nuvem

### Modelos de Serviço
- **IaaS (Infraestrutura como Serviço):**  
  Possibilita alugar servidores, armazenamento e redes. Ex: Máquinas Virtuais.
- **PaaS (Plataforma como Serviço):**  
  Fornece ambiente de desenvolvimento completo na nuvem. Ex: Azure App Service.
- **SaaS (Software como Serviço):**  
  Softwares prontos para uso via internet. Ex: Microsoft 365, Outlook Web.

### Modelos de Implantação
- **Nuvem Pública:** Infraestrutura da Microsoft (Azure), compartilhada com outros clientes.
- **Nuvem Privada:** Recursos dedicados a uma única empresa, localmente ou via parceiro. (On-premises).
- **Nuvem Híbrida:** Combina nuvem pública e privada com integração entre ambas.

### Benefícios da Computação em Nuvem
- **Alta disponibilidade:** Garantia de funcionamento contínuo.
- **Escalabilidade:** Ajuste de recursos de forma automática ou manual.
- **Elasticidade:** Cresce ou diminui conforme a carga.
- **Agilidade:** Criação rápida de soluções.
- **Pay-as-you-go:** Pagamento somente pelo que for utilizado.

---

## 2. Serviços Principais do Azure 

- **Máquinas Virtuais (Azure VMs):**  
  Infraestrutura sob demanda com Windows ou Linux, usada para hospedagem, testes e execução de sistemas.

- **Azure App Services:**  
  Hospedagem de aplicativos web, APIs ou mobile com gerenciamento simplificado de infraestrutura.

- **Azure Functions:**  
  Execução de pequenos blocos de código (event-driven) sem precisar manter servidores.

- **Azure Blob Storage:**  
  Serviço para armazenar grandes volumes de dados não estruturados como imagens, vídeos e backups.

- **Azure SQL Database:**  
  Banco de dados relacional como serviço (PaaS) baseado no SQL Server, com alta disponibilidade automática.

---

## 3. Soluções e Ferramentas de Gerenciamento 

- **Azure Portal:**  
  Interface web gráfica para gerenciar recursos do Azure.

- **Azure CLI (Command Line Interface):**  
  Ferramenta de linha de comando para criar e gerenciar recursos usando comandos em shell/bash.

- **PowerShell para Azure:**  
  Automação e gerenciamento via scripts no Windows PowerShell.

- **Azure Resource Manager (ARM):**  
  Sistema de provisionamento que organiza recursos em grupos lógicos com templates JSON.

- **Azure Monitor:**  
  Monitora o desempenho e a integridade dos recursos, envia alertas e logs.

- **Log Analytics:**  
  Consulta e análise de logs gerados por aplicativos, máquinas virtuais e outros serviços.

---

## 4. Segurança, Conformidade e Privacidade 

- **Azure Security Center:**  
  Painel central para gerenciamento da postura de segurança, proteção contra ameaças e recomendações.

- **Network Security Groups (NSGs):**  
  Listas de regras que controlam o tráfego de rede de entrada e saída.

- **Azure Policy:**  
  Aplica regras e padrões de conformidade automaticamente nos recursos.

- **Blueprints:**  
  Templates reutilizáveis para implantar ambientes com políticas, RBAC e recursos pré-definidos.

- **Microsoft Defender for Cloud:**  
  Sistema de detecção e resposta para ameaças em recursos do Azure e ambientes híbridos.

- **Compliance Manager:**  
  Ferramenta que ajuda a monitorar e manter a conformidade com padrões regulatórios (ISO, GDPR, etc.).

---

## 5. Identidade, Governança e Privacidade

- **Azure Active Directory (Azure AD):**  
  Serviço de gerenciamento de identidades para autenticação e controle de acesso a apps e serviços.

- **RBAC (Role-Based Access Control):**  
  Permissões atribuídas com base em funções, controlando o que cada usuário pode fazer.

- **MFA (Multi-Factor Authentication):**  
  Autenticação com duas ou mais etapas (senha + celular, por exemplo).

- **Assinaturas (Subscriptions):**  
  Container lógico que organiza os recursos do Azure e define limites de faturamento e controle.

- **Grupos de Gerenciamento:**  
  Organizam várias assinaturas para facilitar governança e políticas em larga escala.

---

## 6. Custos e SLAs 

- **Calculadora de Preços:**  
  Ferramenta para estimar custos mensais de recursos e serviços no Azure.  
  Link: https://azure.microsoft.com/pt-br/pricing/calculator/

- **TCO Calculator:**  
  Estima a economia ao migrar da infraestrutura local para a nuvem (Total Cost of Ownership).

- **SLAs (Service Level Agreements):**  
  Garantias de tempo de funcionamento dos serviços. Ex: 99,9%, 99,99% etc. Quanto maior o número, menor é o tempo de indisponibilidade do serviço.
  Se o SLA não é respeitado, não há reembolso, é feito um crédito para uso futuro.

- **Zonas de Disponibilidade:**  
  Conjuntos de datacenters físicos separados geograficamente dentro de uma região para garantir resiliência.

---
