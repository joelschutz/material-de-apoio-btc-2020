<div align="center">
  <img width="20%" src="https://maratona.dev/static/icons/4-ws.png" alt="Desafio #3 | AlgarTech" />

</div>

# Desafio 4
Este desafio é muito parecido com o [Desafio 2](https://github.com/joelschutz/material-de-apoio-btc-2020/blob/master/Desafio%202/desafio-2.md), ele consiste em identificar dentro de uma lista de candidatos da Algar quais foram contratados para a vaga ou não. Este porém vem com os seus próprios desafios visto que a quantidade de amostras é menor e a de features é maior que a do desafio anterior.

- [Repositório do Desafio 4](https://github.com/maratonadev-br/desafio-4-2020)
- [Relatório do dataset](https://github.com/joelschutz/material-de-apoio-btc-2020/blob/master/Desafio%204/Relat%C3%B3rio-Desafio-4.html)
- Minha solução (Em progresso)

## Onde começar?
Por se tratar de um problema de classificação, revisar as técnicas utilizadas no Desafio 2 mais ser de grante ajuda. Além disso, pela grande quantidade de features, uma análise mais profunda do comportamento e corelação dessas features pode ajudar bastante no resultado.  
Confira esses links:
- [Material do Desafio 2](https://github.com/joelschutz/material-de-apoio-btc-2020/blob/master/Desafio%202/desafio-2.md)
- [Relatório do dataset do Desafio 4](https://github.com/joelschutz/material-de-apoio-btc-2020/blob/master/Desafio%204/Relat%C3%B3rio-Desafio-4.html)

### Encontre variáveis inúteis
Cada análise é diferente, dependendo do que está sendo pesquisado, ou que tipo de informação estamos tentando extrair do dataset, certas features vai contribuir ou atrapalhar nossa análise. Em um problema de classificação, procure excluir features que não apresentam distinção entre as classes pesquisadas, como:
- Features com valores contantes.  
    Se todos os candidatos, independente se foram contratados ou não, apresentam a mesma idade, por exemplo, não faz sentido utilizar essa informação na hora da análise. Muito provavelmente este valor está presenta no dataset pois serve para algum tipo de controle interno, mas não nos interessa na classificação.
- Features explicativas ou de controle.
    Algumas colunas estão presentes apenas para fins de controle ou referência e não servem para a a classificação. Bons exemplos são Matrículas ou Gênero. Retirar essas colunas pode ajudar nosso modelo não apenas a melhorar suas predições como também evita vícios no modelo. Imagine que o modelo encontre relação entre o CEP da pessoa e as chances de ela ser contratada, quando este modelo for para a produção ele pode acabar excluíndo pessoas por motivos que não são relevantes.

### Encontre as variáveis que tem alta correlação entre sí
Quando as variáveis do nosso dataset possuem uma grande correlação o nosso modelo pode ficar confuso e não perceber qual delas é mais relevante na hora da análise. Precisamos sempre observar a matriz de correlação para identificar esses casos.  
![Matriz de Corelação](https://github.com/joelschutz/material-de-apoio-btc-2020/raw/master/Desafio%204/matriz-de-corelacao.png)
Os pontos mais escuros(vermelhos ou azuis) indicam alta correlação entre duas variáveis. A imagem acima é a matriz de correlação do dataset do Desafio 4 e as linhas pretas são as variáveis constantes.  
Algumas formas de lidar com esse problema:
- Eliminar uma das variáveis
    Em casos onde duas variáveis passam informações muito parecidas ou sinônimas a eliminação de uma delas pode ser interessante.
- Combinar as variáveis em uma
    Caso não seja possível eliminar uma das variáveis é possível combiná-las em uma composta que represente os dois valores.

## Para onde ir agora?
Uma boa prática para qualquer trabalho de Data Science é fazer um bom pré-processamento e entender que tipo de métrica utilizar. Seguem alguns links que podem ajudar:
- [Um guia completo para o pré-processamento de dados em machine learning](https://medium.com/@caiquecoelho/um-guia-completo-para-o-pr%C3%A9-processamento-de-dados-em-machine-learning-f860fbadabe1) por [Caíque Coelho](https://medium.com/@caiquecoelho)
- [Label Encoder vs. One Hot Encoder in Machine Learning](https://medium.com/@contactsunny/label-encoder-vs-one-hot-encoder-in-machine-learning-3fc273365621) por [Sunny Srinidhi](https://medium.com/@contactsunny)
- [Why is accuracy not the best measure for assessing classification models?](https://stats.stackexchange.com/questions/312780/why-is-accuracy-not-the-best-measure-for-assessing-classification-models)
- [F1-Score](https://en.m.wikipedia.org/wiki/F1_score)
- [Precison and Recall](https://en.m.wikipedia.org/wiki/Precision_and_recall)