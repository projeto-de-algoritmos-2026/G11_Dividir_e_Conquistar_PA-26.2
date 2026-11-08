# G11_Dividir_e_Conquistar_PA-26.2

# DreamMatch - Recomendador DreamWorks com Contagem de Inversões

**Número da Dupla:** 11 <br>
**Conteúdo da Disciplina:** Dividir e Conquistar (*Divide and Conquer*), Contagem de Inversões (*Inversion Count / Merge and Count*). <br>

## Alunos

| Nome | Matrícula |
| :--- | :--- |
| Davi Monteiro de Negreiros | 232013971 |
| Guilherme D'Avila Rodrigues Carneiro Sampaio | 221029220 |

---

## Sobre o Projeto

O **DreamMatch** é uma aplicação interativa que calcula a afinidade de gosto cinematográfico entre usuários a partir de seus rankings pessoais dos 10 filmes mais icônicos do estúdio **DreamWorks** (como *Shrek*, *Como Treinar o Seu Dragão*, *Kung Fu Panda*, *Megamente*, *Gato de Botas 2*, entre outros).

Para determinar o grau de concordância entre duas preferências, o sistema modela os rankings como permutações ordenadas e emprega o algoritmo clássico de **Contagem de Inversões** utilizando a técnica de **Dividir e Conquistar** (*Divide and Conquer*).

### Por que Contagem de Inversões?
* Uma **inversão** ocorre quando dois elementos aparecem em ordem relativa inversa entre duas listas de preferência.
* Se dois usuários possuem preferências idênticas, o número de inversões é **0** (100% de similaridade).
* Se a ordem for perfeitamente invertida, o número de inversões atinge o máximo teórico:
  $$\text{Máximo de Inversões} = \frac{n \times (n - 1)}{2}$$
* Enquanto uma comparação ingênua de pares (força bruta) requer complexidade quadrática $O(n^2)$, a abordagem por **Dividir e Conquistar** resolve o problema em tempo ótimo de **$O(n \log n)$**, adaptando o procedimento de intercalação do *Merge Sort* (*Merge and Count*).

---

## Vídeo de Apresentação

Gravação da apresentação e demonstração do projeto:  
> 📹 **Link do Vídeo:** [link da gravação]()

---

## Screenshots

<!--p align="center">
  <i>(Adicione aqui as capturas de tela do sistema em execução)</i>
</p>
-->

---

## Instalação e Execução

### Pré-requisitos
- **Python** (versão 3.10 ou superior recomendada)
- Gerenciador de pacotes **pip**

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/projeto-de-algoritmos-2024-2/G11_Dividir_e_Conquistar_PA-26.2.git
   cd G11_Dividir_e_Conquistar_PA-26.2
   ```

2. **Crie e ative um ambiente virtual (recomendado):**
   - **Linux / macOS:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - **Windows (PowerShell):**
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```

3. **Instale as dependências do projeto:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação Streamlit:**
   ```bash
   streamlit run app.py
   ```

O navegador abrirá automaticamente no endereço local `http://localhost:8501`.

---

