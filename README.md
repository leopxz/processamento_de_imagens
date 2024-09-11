# Processamento de Imagens

Este repositório contém um projeto de **Processamento de Imagens** que utiliza técnicas e bibliotecas populares para manipulação e análise de imagens. O projeto inclui diversas funcionalidades de processamento, como detecção de bordas, ajustes de brilho e contraste, e aplicação de filtros.

## Funcionalidades

- Leitura e exibição de imagens.
- Aplicação de filtros de suavização e detecção de bordas.
- Ajustes de brilho, contraste e saturação.
- Redimensionamento e rotação de imagens.
- Conversão de imagens para escala de cinza.

## Tecnologias Utilizadas

- **Python 3.x**
- **OpenCV**: Biblioteca utilizada para operações de processamento de imagens.
- **NumPy**: Manipulação de arrays para operações matemáticas eficientes.
- **Matplotlib**: Exibição gráfica de imagens e resultados.

## Estrutura do Projeto
<br>
├── image-processing/ <br>
├── tests/<br>
└── __init.py__<br>
└── test_processing.py<br>
 |<br>
├── .gitgnore<br>
├── LICENSE <br>
├── README.md <br>
├── __init.py__<br>
├── requirements.txt<br>
└── setup.py<br>


## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/leopxz/processamento_de_imagens.git
   cd processamento_de_imagens

## Exemplos de Uso
**Aplicar Filtro de Borda**

from src.filtros import aplicar_filtro_borda
imagem_filtrada = aplicar_filtro_borda('imagens/exemplo.jpg')

**Ajustar Brilho**

from src.ajustes import ajustar_brilho
imagem_ajustada = ajustar_brilho('imagens/exemplo.jpg', brilho=1.5)

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar um problema.

## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações. 
Você pode adaptar as funcionalidades e detalhes técnicos conforme o que realmente está implementado no projeto.
