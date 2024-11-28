# Exposição Virtual de Coleções com Django

Este projeto foi desenvolvido como parte da atividade **"Exposição Virtual de Coleções, Autenticação e Testes Automatizados"**. Ele apresenta uma plataforma para gerenciar coleções virtuais, com funcionalidades de autenticação de usuários e testes automatizados para garantir a qualidade do sistema.

## Nomes dos Componentes da Dupla

- **Francisco José dos Santos Lima**  
- **João Vitor Silva Novais**

## Funcionalidades

- **Autenticação de Usuários:** Sistema de login e logout integrado com o Django.
- **Gerenciamento de Coleções:** Permite o cadastro, edição, exclusão e visualização de coleções virtuais.
- **Exposição Virtual:** Organize itens e informações em coleções apresentadas virtualmente.
- **Testes Automatizados:** Arquivo `test.py` criado para garantir a funcionalidade e estabilidade da aplicação.

---

## Sobre o Arquivo `test.py`

O arquivo `test.py` contém os testes automatizados do projeto. Ele foi desenvolvido para validar os principais aspectos da aplicação, como autenticação, gerenciamento de coleções e regras de negócio.  

### O que é testado?

1. **Autenticação:**
   - Verifica se o login e logout funcionam corretamente.
   - Testa se as permissões de acesso são aplicadas corretamente (ex.: páginas restritas a usuários logados).

2. **Funcionalidades de CRUD:**
   - Testa a criação, edição e exclusão de coleções.
   - Verifica se as coleções são exibidas corretamente para os usuários.

3. **Regras de Negócio:**
   - Garante que os itens cadastrados sigam as restrições configuradas, como campos obrigatórios.

### Como Executar os Testes

1. Certifique-se de que o ambiente virtual está ativado e que as dependências estão instaladas.
2. Use o comando abaixo para rodar os testes:
   ```bash
   python manage.py test
