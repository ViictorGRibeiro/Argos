# RELATÓRIO TDE 2: APLICAÇÃO ARGOS - CLEAN ARCHITECTURE, VERTICAL SLICE E SOLID

## 1. Identificação dos Alunos e Atribuições

| Aluno | Matrícula / RA | Papel na Tarefa | Descrição das Atividades Realizadas |
| :--- | :--- | :--- | :--- |
| **Victor Gustavo** | 20260101 | Tech Lead / Arquiteto de Software | Concepção da arquitetura, estruturação do Clean Architecture + Vertical Slice, definição de contratos de interfaces e injeção de dependência (SOLID). |
| **Equipe / Colaborador 2** | 20260102 | Desenvolvedor Backend | Implementação dos Casos de Uso (Use Cases), Handlers das Features (Autenticação e Transações) e repositórios de persistência. |
| **Equipe / Colaborador 3** | 20260103 | Engenheiro de Qualidade / DevOps | Configuração do ambiente Git, criação da nova branch no GitHub, validação dos princípios SOLID e elaboração dos diagramas. |

---

## 2. Repositório GitHub e Branch

* **Repositório Oficial:** [https://github.com/ViictorGRibeiro/Argos](https://github.com/ViictorGRibeiro/Argos)
* **Branch Utilizada:** `feature/clean-architecture-vertical-slice`

---

## 3. Prompts Utilizados com a IA Generativa

1. **Prompt 1 (Arquitetura Inicial):**
   > *"Atue como Arquiteto de Software Sênior. Preciso reestruturar o backend da aplicação Argos (sistema de finanças e transações) utilizando Clean Architecture combinada com Vertical Slice Architecture. Proponha a estrutura de pastas e a divisão dos módulos principais (Autenticação, Dashboard e Transações)."*

2. **Prompt 2 (Aplicação de SOLID):**
   > *"Com base na estrutura proposta, refatore o módulo de transações aplicando rigorosamente os princípios SOLID. Garanta que cada Use Case tenha uma única responsabilidade (SRP), que as interfaces de repositório sejam segregadas (ISP) e que os manipuladores recebam dependências via inversão de controle (DIP)."*

3. **Prompt 3 (Geração de Diagramas):**
   > *"Gere diagramas UML de Componentes e de Classes em sintaxe Mermaid para o backend da aplicação Argos, demonstrando claramente as camadas da Clean Architecture (Entities, Use Cases, Adapters, Frameworks) organizadas em Slices verticais."*

---

## 4. Diagramas do Backend (Markdown / Mermaid)

### 4.1. Diagrama de Componentes (Clean Architecture + Vertical Slice)
```mermaid
componentDiagram
    package "API / Frameworks (Drivers)" {
        [Express Server] --> [Auth Controller]
        [Express Server] --> [Transactions Controller]
    }
    package "Vertical Slices / Interface Adapters" {
        [Auth Controller] --> [Authenticate User Use Case]
        [Transactions Controller] --> [Create Transaction Use Case]
    }
    package "Use Cases (Application Core)" {
        [Authenticate User Use Case] --> [User Domain Entity]
        [Create Transaction Use Case] --> [Transaction Domain Entity]
    }
    package "Infrastructure & Gateways" {
        [Authenticate User Use Case] --> [Prisma UserRepository]
        [Create Transaction Use Case] --> [Prisma TransactionRepository]
    }
```
