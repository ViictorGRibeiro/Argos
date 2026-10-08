# Argos Backend - TDE 2

Backend da aplicação **Argos** estruturado utilizando:
- **Vertical Slice Architecture** (Organização por features: Auth, Transactions, Dashboard)
- **Clean Architecture** (Separação estricta entre Domínio, Casos de Uso, Adaptadores e Frameworks)
- **Princípios SOLID** (SRP, OCP, LSP, ISP, DIP)

## Estrutura do Projeto
```text
src/
├── features/
│   ├── auth/
│   │   ├── controllers/AuthController.ts
│   │   ├── use-cases/AuthenticateUserUseCase.ts
│   │   └── repositories/UserRepository.ts
│   └── transactions/
│       ├── controllers/TransactionController.ts
│       ├── use-cases/CreateTransactionUseCase.ts
│       └── repositories/TransactionRepository.ts
└── server.ts
```
