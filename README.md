# 🛡️ Spring Secure Gate

[![GitHub Release](https://img.shields.io/github/v/release/Lourencobrah/spring-security-gate-action?style=flat-square&color=green)](https://github.com/Lourencobrah/spring-security-gate-action/releases)
[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-Spring--Secure--Gate-blue?logo=github&style=flat-square)](https://github.com/marketplace/actions/spring-secure-gate)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

**Spring Secure Gate** é uma GitHub Action focada em segurança (SCA - Software Composition Analysis) projetada especificamente para o ecossistema Java/Spring. Ela atua como uma barreira de segurança (*Quality Gate*) no seu pipeline de CI/CD, impedindo que dependências vulneráveis cheguem à produção.

---

## 🚀 Por que usar o Spring Secure Gate?

Diferente de scanners genéricos, esta Action foi desenhada para o fluxo de trabalho de desenvolvedores e engenheiros de AppSec:

- 🔥 **Inteligência de Severidade:**  
  Defina limiares (*thresholds*) personalizados. Só falhe o build se encontrar riscos que realmente importam para o seu negócio (ex: `Critical` ou `High`).

- 📊 **Relatórios Visuais:**  
  Gera tabelas detalhadas diretamente no log do console e no **Job Summary** do GitHub.

- 🛡️ **Powered by OSV-Scanner:**  
  Utiliza a base de dados de vulnerabilidades open-source do Google para máxima precisão.

---

## 📦 Como utilizar

Basta adicionar este passo ao seu arquivo de workflow (ex: `.github/workflows/main.yml`):

```yaml
steps:
  - name: Checkout Code
    uses: actions/checkout@v4

  - name: Security Scan (Spring Secure Gate)
    uses: Lourencobrah/spring-security-gate-action@v1
    with:
      severity_threshold: 'high' # Opções: low, medium, high, critical
      directory: '.'             # Diretório raiz do projeto Java
```

---

## ⚙️ Configurações (Inputs)

| Parâmetro             | Descrição                                                                 | Padrão |
|----------------------|---------------------------------------------------------------------------|---------|
| `severity_threshold` | Nível mínimo de severidade para falhar o build (`low`, `medium`, `high`, `critical`) | `high` |
| `directory`          | Caminho do diretório que contém os arquivos `pom.xml` ou `build.gradle` | `.` |

---

## 📊 Visualizando os Resultados

A ferramenta fornece feedback imediato de duas formas:

### 1. Terminal Output

Uma tabela limpa e formatada no log do GitHub Actions para depuração rápida.

### 2. Job Summary (Markdown)

Um relatório detalhado que aparece na página inicial da execução do workflow, ideal para auditorias rápidas.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11** → Lógica de processamento e parsing de dados.
- **Docker** → Garantia de ambiente isolado e imutável.
- **OSV-Scanner** → Motor de análise de vulnerabilidades do Google.
- **GitHub Actions API** → Integração nativa para relatórios de CI/CD.

---

## 👨‍💻 Autor

Desenvolvido por **Guilherme Lourenço**  
*Application Security Engineer (AppSec) | DevSecOps | Java Backend (Spring Boot) | APIs & Microservices*

- 🔗 LinkedIn: [https://www.linkedin.com/in/lourencovicente/](#)
- 💻 Portfólio: [https://github.com/Lourencobrah](#)

---

## 📜 Objetivo do Projeto

Este projeto foi criado com o objetivo de fortalecer a cultura de **DevSecOps** em aplicações Java.
