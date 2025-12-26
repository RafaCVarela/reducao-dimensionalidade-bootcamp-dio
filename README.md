# Projeto de Redução de Dimensionalidade em Imagens

Este projeto consiste na implementação de um algoritmo para a transformação de imagens coloridas em níveis de cinza e, posteriormente, em imagens binarizadas (preto e branco). O objetivo é demonstrar o processo de redução de dimensionalidade através da manipulação direta de pixels.

## Descrição do Projeto

Seguindo as diretrizes estabelecidas, o software realiza a conversão de uma imagem de entrada (RGB) para dois formatos distintos:

1. 
**Níveis de Cinza:** Transformação para uma escala que varia de 0 a 255.


2. 
**Imagem Binarizada:** Transformação para uma representação binária (0 e 255), resultando em uma imagem puramente preta e branca.



## Resumo da Implementação

A lógica implementada no arquivo `main.py` utiliza a biblioteca **PIL (Pillow)** para o processamento das imagens:

* **Conversão para Cinza:** A função `converterParaCinza` percorre cada pixel da imagem original e aplica a fórmula de luminância: .
* **Conversão para Preto e Branco:** A função `converterParaPretoBranco` utiliza um **limiar (threshold) de 127**. Se o valor do pixel for superior a este limite, ele é definido como branco (1); caso contrário, como preto (0).

## Entrada

**Imagem Original:** Entrada colorida em formato RGB. A imagem fornecida foi a da 'Lena.png'.

## Resultados Esperados

Com base na imagem de exemplo fornecida ("Lena"), o algoritmo gera os seguintes casos de saída:

1. 
**Imagem em Cinza:** Versão com dimensionalidade reduzida para canais de intensidade.

2. 
**Imagem Binária:** Versão final em alto contraste (preto e branco).

## 👨‍💻 Expert

<p>
    <img 
      align=left 
      margin=10 
      width=80 
      src="https://avatars.githubusercontent.com/u/48953925?v=4"
    />
    <p>&nbsp&nbsp&nbspRafael Varela<br>
    &nbsp&nbsp&nbsp
    <a href="https://github.com/RafaCVarela">
    GitHub</a>&nbsp;|&nbsp;
    <a href="https://www.linkedin.com/in/rafacvarela/">LinkedIn</a>
&nbsp;|&nbsp;
    <a href="https://www.instagram.com/varelarc_/">
    Instagram</a>
&nbsp;|&nbsp;</p>
</p>
<br/><br/>
<p>
    
------

⌨️ com 💜 por [Felipe Aguiar](https://github.com/felipeAguiarCode)
