# 🤖 Buscador de Empresas

Aplicativo desktop com interface gráfica para automação de busca de dados de empresas via raiz de CNPJ ou CACEAL.

---

## 🧠 Funcionalidades

* ✔️ Busca automatizada nos navegadores Chrome e Firefox
* ✔️ Suporte a busca em lote importando arquivo Excel (.xlsx)
* ✔️ Busca segmentada pelas seguintes cidades disponíveis:
  * 🏙️ Limoeiro de Anadia
  * 🏙️ Taquarana
  * 🏙️ Arapiraca
  * 🏙️ Giral do Ponciano
* ✔️ Exportação dos resultados detalhados (Responsável, Empresa, Local, Email) para Excel
* ✔️ Interface amigável 

---

## 🛠️ Tecnologias

* Python
* Tkinter & ttkbootstrap (Interface Gráfica)
* Selenium & webdriver-manager (Automação Web)
* Pandas, openpyxl & XlsxWriter (Processamento de Dados)

---

## ⚙️ Como usar

```bash
# Clonar repositório
git clone https://github.com/JockaMt/EmpresasEmDefices.git

# Entrar no diretório
cd EmpresasEmDefices

# Instalar dependências
pip install openpyxl pandas selenium ttkbootstrap webdriver-manager XlsxWriter

# Rodar o aplicativo
python main.py
```

---

## 📸 Demonstração

(prints do aplicativo funcionando e planilhas geradas)

---

## 🎯 Objetivo

Projeto desenvolvido para automatizar a busca e extração de informações de empresas em plataformas governamentais utilizando automação de navegadores.

---

## 💡 Melhorias futuras

* [ ] Suporte a execução em segundo plano (Headless mode)
* [ ] Adicionar mais cidades para pesquisa
* [ ] Barra de progresso para acompanhamento em tempo real
* [ ] Refatoração para arquitetura MVC ou POO

---

## 📄 Licença

MIT
