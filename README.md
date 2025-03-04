# README - Projeto de Computação Gráfica

## Sobre o Projeto
Este projeto contém implementações de diferentes algoritmos de rasterização, recorte e preenchimento de primitivas gráficas, organizados nas seguintes categorias:

1. **Rasterização de Retas** - Algoritmos para desenhar retas pixel a pixel.
2. **Rasterização de Circunferências** - Métodos para desenhar circunferências de forma eficiente.
3. **Preenchimento de Polígonos** - Técnicas para preencher polígonos com diferentes estratégias.
4. **Rasterização de Curvas** - Técnicas para desenhar retas com pontos gerando curvas.
5. **Recorte de Poligonos** - Algoritmo para recortar polígonos.

Cada categoria contém códigos específicos para a sua respectiva função.

---

## Estrutura de Diretórios
Dentro do diretório **CG**, temos as seguintes pastas:

```
CG/
│-- Circunferencia/
│   │-- Bresenham.py
│   │-- Paramétrica.py
│   │-- Simetria.py
│   │-- Rasterização de Circunferências.pdf
|
│-- Curva/
│   │-- Casteljau.py
│   │-- Paramétrica.py
│   │-- Curva de Bezier.pdf
|
│-- Preechimento/
│   │-- Flood.py
│   │-- Geometrica.py
│   │-- Preechimento de Poligonos.pdf
│
│-- Recorte/
│   │-- Sutherland.py
│   │-- Algoritmo de Recorte.pdf
|
│-- Reta/
│   │-- Analítico.py
│   │-- Bresenham.py
│   │-- DDA.py
│   │-- Rasterização de Retas.pdf
```
Cada pasta contém os códigos de implementação e um relatório explicativo em PDF.

---

## Como Executar os Códigos

### 1. **Requisitos**
Antes de rodar os códigos, certifique-se de ter instalado:
- **Python 3.6+**
- **Bibliotecas necessárias:**
  ```bash
  pip install pygame numpy matplotlib
  ```

### 2. **Rodando os Códigos**
Para rodar qualquer um dos algoritmos, basta acessar a pasta correspondente e executar o script Python desejado. Por exemplo:

#### **Rasterização de Retas**
```bash
cd Reta
python Bresenham.py
```

#### **Rasterização de Circunferências**
```bash
cd Circunferencia
python Simetria.py
```

#### **Preenchimento de Polígonos**
```bash
cd Preechimento
python Flood.py
```

#### **Rasterização de Curvas**
```bash
cd Curva
python Casteljau.py
```

#### **Recorte de Polígonos**
```bash
cd Recorte
python Sutherland.py
```

Os scripts abrirão uma janela utilizando **Pygame** para exibir os resultados gráficos.

---

### ⚠️ Observações
- Certifique-se de executar os scripts em um ambiente Python adequado.
- Para visualizar corretamente os resultados, a biblioteca **Pygame** precisa estar instalada.
- Alguns scripts possuem entrada interativa, como o **Flood.py**, que permite clicar para iniciar o preenchimento.

---

### Licença
Este projeto é de uso acadêmico e pode ser modificado conforme necessário.

