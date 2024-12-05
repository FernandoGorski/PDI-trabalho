# Projeto de Detecção de Emoções com OpenCV e DeepFace para Descobrir o Engajamento em Vídeos

## Descrição

Este projeto tem como objetivo desenvolver um sistema que utiliza a biblioteca OpenCV e o modelo DeepFace para analisar as emoções faciais dos usuários enquanto assistem a vídeos. A aplicação será capaz de capturar imagens em tempo real por meio da webcam, identificar as expressões faciais e associar as emoções detectadas ao nível de engajamento do usuário com o conteúdo exibido.

## Universidade Federal do Paraná

- **Setor de Educação Profissional e Tecnológica**
- **Alunos:** 
- Fernando Guilherme Gorski 
- Hygor Adriano Tristão
- **Professor Orientador:** 
- Dr. Luiz Antônio Pereira Neves

## Pré-requisitos

Antes de começar, verifique se você tem os seguintes requisitos instalados:

- Python 3.x
- OpenCV
- DeepFace
- Numpy

Para instalar o Python, acesse o [Link](https://www.python.org/downloads/).

Você pode instalar as dependências necessárias com o seguinte comando (Execute uma linha por vez, na ordem abaixo):

```bashq
python -m venv myvenv 
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.\myvenv\Scripts\activate  

pip install opencv-python
pip install tf-keras
pip install deepface
pip install matplotlib
```

## Possívies Problemas

- 1. Erro de Caminho Longo no Windows

Se você estiver utilizando o Windows e encontrar um erro relacionado a "tamanho muito longo" durante a instalação, isso pode ser devido a uma limitação do sistema de arquivos. Para resolver isso, você pode seguir o tutorial disponível no link abaixo para alterar as configurações do Windows e permitir caminhos mais longos.

Resolva [Aqui](https://medium.com/@mariem.jabloun/how-to-fix-python-package-installation-long-path-support-os-error-59ab7e9bf10a).

