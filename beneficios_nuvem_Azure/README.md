# Resumo: Criação de Máquina Virtual no Azure
Criar uma VM no Azure permite executar sistemas operacionais e aplicativos como se fossem servidores físicos, mas hospedados na nuvem. O Azure oferece flexibilidade para configurar, escalar e gerenciar essas VMs de forma prática.

## Etapas da Criação de uma VM no Azure (via Portal)
1. Acessar o Azure Portal
URL: https://portal.azure.com

Acesse com sua conta e vá até “Máquinas Virtuais” → “Criar”.

2. Informações Básicas
Assinatura: Seleciona a conta de cobrança.

Grupo de Recursos: Contêiner lógico onde os recursos são agrupados.

Nome da VM: Identificador da máquina.

Região: Define o datacenter (ex: Brazil South).

3. Imagem (SO)
Escolha o sistema operacional: Windows Server, Ubuntu, Debian, etc.

Você pode usar imagens customizadas ou do Azure Marketplace.

4. Tamanho da VM
Escolha conforme CPU, RAM e carga de trabalho.

Ex: B1s (uso leve), D2s_v3 (uso intermediário).

5. Conta de Administrador
Nome de usuário e senha ou chave SSH (para Linux).

6. Discos
Disco do sistema: SSD padrão, SSD premium ou HDD.

Pode-se adicionar discos de dados posteriormente.

7. Rede
Criação/seleção de uma Virtual Network (VNet).

Azure criará um IP público, interface de rede e sub-rede.

8. Portas de Entrada
Configure portas como RDP (3389 para Windows) ou SSH (22 para Linux).

9. Revisar + Criar
Verifique o resumo das configurações.

Clique em “Criar”. O processo leva alguns minutos.

## Configurações Pós-Criação
Acesso à VM:

* Windows: via Remote Desktop (RDP)

* Linux: via SSH

* Instalação de aplicativos: conforme sua necessidade.

* Monitoramento: Configure Azure Monitor e Alertas.

* Backup: Configure o Azure Backup.

* NSG (Network Security Group): refine as regras de acesso à rede.

