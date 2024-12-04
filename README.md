# Projeto de Detecção de Emoções com OpenCV e DeepFace para Descobrir a Cor Favorita

## Descrição

Este projeto tem como objetivo implementar um sistema que captura imagens de uma webcam e detecta emoções faciais, alterando a cor de um quadrado na tela com base nas emoções identificadas. A cor favorita da pessoa é determinada pela emoção mais predominante durante o processo.

## Universidade Federal do Paraná

- **Setor de Educação Profissional e Tecnológica**
- **Alunos:** Fernando Guilherme Gorski e Hygor Adriano Tristão
- **Professor:** Dr. Luiz Antônio Pereira Neves

## Pré-requisitos

Antes de começar, verifique se você tem os seguintes requisitos instalados:

- Python 3.x
- OpenCV
- DeepFace
- Numpy

Para instalar o Python, acesse o [Link](https://www.python.org/downloads/).

Você pode instalar as dependências necessárias com o seguinte comando:

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

