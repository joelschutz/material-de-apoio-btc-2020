# Material de Apoio - BTC-2020
Este repositório contém materiais de apoio para a Maratona Behind The Code 2020

## Onde começar?
Um bom lugar para começar é se familiarizando com as ferramentas.
As principais bibliotecas utilizadas em Data Science são:
### Pandas
Utilizada para ler, armazenar e manipular datasets. Os dois conceitos básicos para utilizar essa biblioteca são:
- DataFrame: Pode ser pensado como uma tabela onde cada coluna é uma Series e cada linha tem um index.
- Series: Pode ser pensado como uma coluna ou um conjunto de valores de uma dimensão apenas. Cada linha também possui seu próprio index.
- Links: 
    - [Data Analysis com Python Pandas](https://imasters.com.br/back-end/data-analysis-com-python-pandas-o-inicio), por [Rafael Novello](https://imasters.com.br/perfil/rafael-j-r-novello)
    - [Seus primeiros passos como Data Scientist: Introdução ao Pandas!](https://medium.com/data-hackers/uma-introdu%C3%A7%C3%A3o-simples-ao-pandas-1e15eea37fa1) por [Vinícius Figueiredo](https://medium.com/@vinciusaguiar_14084)
    - [Pandas in 10 minutes | Walkthrough](https://www.youtube.com/watch?v=_T8LGqJtuGc) por [Wes McKinney](https://wesmckinney.com/)(Video em inglês)
    - [Documentação Oficial](https://pandas.pydata.org/docs/)
- Livros:
    - Python for Data Analysis por Wes McKinney
    - Learning Pandas por Michael Heydt
    - Python for Data Science For Dummies - Luca Massaron e John Paul Mueller

### Seaborn
Existem diferentes bibliotecas para Data Visualization, cada uma com suas limitações e facilidades, Seaborn é com certeza uma das mais fáceis para iniciantes. Essa biblioteca é utilizada para gerar gráficos que irão te auxiliar na análise do seu dataset.  
Os conceitos fundamentais:
- Tipos de plotagem: Essa biblioteca disponibiliza dezenas de gráfico diferentes com parametros e objetivos distintos. Sempre confira a documentação para ter certeza que está utilizando a ferramenta corretamente.
- Estilos e Paletas: É possível customizar a sua visualização utilizando diferentes paletas de cores e estilos de gráfico para melhorar a estética e compreenção dos seus dados. Na hora de alterar esses parametros leve sempre em conta a legibilidade dos dados.
- Integração com Pandas: Você não precisa fazer conversões para plotar os seus dados. A bibliteca aceita DataFrames e Series do Pandas como input e é capaz até de trabalhar com variáveis categóricas. Podem ser necessários porém outros tipos de pré-processamento a depender do plot desejado, confira a documentação específica.
- Links:
    - [Visualização de dados com Seaborn](https://dev.to/giselyalves13/visualizacao-de-dados-com-seaborn-2892) por [Gisely Alves](https://dev.to/giselyalves13)
    - [Tutorial Completo de Como Trabalhar com a Biblioteca Seaborn](https://minerandodados.com.br/tutorial-completo-de-como-trabalhar-com-a-biblioteca-seaborn/) por [Rodrigo Santana](https://minerandodados.com.br/author/rodrigodb28/)
    - [Documentação Oficial](https://seaborn.pydata.org/)
- Livros:
    - [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook) por Jake VanderPlas

### Scikit-Learn
Na hora de criar modelos de Machine Learning existem diversos algorítmos, métricas, pré-processamentos e outras técnicas utilizadas para tratar os dados, treinar e avaliar modelos. Uma das bibliotecas mais utilizada para esse propósito é o Scikit-Learn que reúne várias ferramentas num único pacote. Alguns conceitos básicos:
- Estimator API: Com o intúito de facilitar a utilização dos modelos, essa biblioteca instituiu um padrão que todo modelo deve seguir, de forma que uma vez entendendo como usar um modelo os outros são praticamente idênticos. Os passos são:
    - Importe a classe do modelo: ex.`from sklearn.linear_model import LinearRegression`
    - Instancie o modelo com parâmetros desejados. Caso não especifique parâmetros, valores padrão serão utilizados: ex `model = LinearRegression(fit_intercept=True`)
    - Ajuste o modelo a seus dados utilizando o método `fit()`(Esse passo também é conhecido como treino): ex. `model.fit(X, y)`
    - Utilize o modelo para fazer predições utilizando o método `predict()`: ex. `y_desconhecido = model.predict(X_desconhecido)`
- Segregação dos dados: Para que possamos treinar e validar nossos modelos precisamos separar nosso dataset em partes distintas:
    - *features*(X) e *target*(y): A primeira divisão que precisamos fazer é entre os dados que queremos prever(*target* ou y) e os dados de entrada(*features* ou X). Dessa forma podemos indicar para o modelo que dados queremos extrair e que dados serão o input. ex. 
    ```python
    dados = pd.DataFrame(meus_dados)

    X = dados[['var1', 'var2', 'var3', 'var4']]
    y = dados['var_target']
    ```
    - *train* e *test*: Como queremos ter certeza que o nosso modelo irá perfromar bem na vida real precisamos testá-lo utilizando dados que ele nunca viu antes. Para isso criamos amostras aleatórias dos dados de treino(`train`) e de teste(`test`), onde o primeiro servirá de para fazer o `fit()` do modelo e o segundo será utilizado para avaliar o `predict()` do modelo. Existe uma função buit-in to Scikit-Learn para esse propósito chamada `train_test_split()`. ex.
    ```python
    from sklearn.model_selection import train_test_split

    # O random_state serve como uma seed permitindo que repita a amostragem aleatória.
    # O test_size define qual a proporção do dataset deve ser reservada para os testes. Deve ser um número entre 0 e 1
    Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=1, test_size=0.3)
    ```
- *pipeline*: Para automatizar o tratamento do dataset para treino o Scikit-Learn disponibiliza uma estrutura de *pipeline* que deve ser utilizada na hora do deploy do desafio BTC-2020. Para utilizar essa ferramenta:
    - Crie uma etapa: Basta criar uma classe que herde de BaseEstimator e TransformerMixin. Essa classe deve implementar os métodos `fit()` e `transform()`.
    ```python
    from sklearn.base import BaseEstimator, TransformerMixin


    class EtapaDaPipeline(BaseEstimator, TransformerMixin):
        def fit(self, X, y=None):
            return self
        
        def transform(self, X):
            # Primeiro realizamos a cópia do dataframe 'X' de entrada
            data = X.copy()

            # A sua transformação vai aqui            

            # É necessário retornar o dataframe após a transformação
            return data
    ```
    - Definir etapas: Uma vez criadas classes é só passá-las para a *pipeline*. Note que no notebook da Etapa 2 existem etapas que são obrigatórias e que as classes que criou devem ser salvas em um pacote Python antes de serem declarados na pipeline.
    ```python
    from sklearn.pipeline import Pipeline
    
    my_pipeline = Pipeline(
    steps=[
        ('remove_cols', rm_columns), # Exemple da parte 2
        ('imputer', si), # Exemple da parte 2
        ('minha_etapa', EtapaDaPipeline()),
        ('dtc', DecisionTreeClassifier()), # Exemple da parte 2
    ]
    )
    ```
- Links:
    - [Introdução a Machine Learning com Scikit-Learn](https://minerandodados.com.br/cafe-com-codigo-06-introducao-machine-learning-com-scikit-learn/) por [Felipe Santana](https://minerandodados.com.br/author/felipesf05/)
    - [Como criar seu primeiro aplicativo de Machine Learning](https://paulovasconcellos.com.br/como-criar-seu-primeiro-aplicativo-de-machine-learning-7b6af291ba11) por [Paulo Vasconcellos](https://paulovasconcellos.com.br/)
    - [Documentação Oficial](https://scikit-learn.org/)
- Livros:
    - [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook) por Jake VanderPlas
    - Hands-On Machine Learning with Scikit-Learn and TensorFlow por Aurélien Géron
    - scikit-learn Cookbook por Julian Avila e Trent Hauck

## Como melhoro acuracidade do meu modelo?
Por mais avançadas que sejam as técnicas utilizadas, nem sempre os nossos modelos vão entregar bons resultados de predição. O grade desafio em Data Science é exatamente identificar quais modificações podem ser feitas para extrair as informações desejadas do dataset analisado. Aqui vão algumas dicas:
### Faça uma limpeza de qualidade nos dados
Dificilmente um dataset chegará as nossas mãos sem nenhum problema de dados nulos ou discrepantes. Podem existir valores faltantes, erros de digitação ou até mesmo dados incorretos. Limpar nosso dataset significa retirar ou retificar esses valores para garantir que eles não causem confusão no nosso modelo. 

Algumas estratégias comuns são:
- Substituir os valores por uma constante - É a forma mais simples e rápida, mas pode introduzir deformações no comportamento das variáveis
- Substituir os valores por um valor extraido da população como média ou mediana - Faz o mesmo papel da aternativa anterior porém diminui as distorções por usar um valor conformado a população
- Interpolação - Utiliza os valores anteriores e posteriores para estimar um valor possível. É aplicável apenas quando existe alguma correlação entre as linhas do dataset
- Excluir valores nulos - Esse método pode evitar a inserção de distorções, mas pode diminuir drasticamente a quantidade de dados para treino.
- Transformações personalizadas - As melhores soluções não estão na prateleira. Conhecendo o comportamento do seu dataset, substituir valores nulos utilizando algum tipo de lógica pode dar os melhores resultados.

Felizmente existem algumas ferramentas que podem facilitar essa tarefa:
- [Scikit-learn](https://scikit-learn.org/stable/modules/impute.html)
- [Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html)

### Feature Engeneering
Para o modelo as features não passam de listas de valores, ele não sabe se aqueles valores são categóricos ou quantitativos, se tem relação entre si ou não. Escolher e modificar as features pode melhorar consideravelmente a performance do modelo. Algumas técnicas:
- *Feature Transformation*:  
Consiste em alterar os valores de uma variável para que fique mais claro para o modelo suas características. Essa transformação pode ser feota de forma automatizada ou manualmente. A técnica exata vai depender dos dados que estão sendo analisados e do output desesajado, veja algumas ferramentas para este fim:
    - [Pre-processing Scikit-learn](https://scikit-learn.org/stable/modules/preprocessing.html)
- *Feature Construction*:  
Uma outra forma de deixar as features mais claras para o modelo é criando novas a partir dos dados existentes. Essa técnica permite combinar features relacionadas em uma nova que represente essa relação. Por exemplo, caso esteja analisando as vendas de uma loja onde no data set conste apenas a data e o volume de vendas, criar uma terceira coluna que descreva o dia da semana pode auxiliar o modelo na compreensão da relação entre dia e vendas.  
Como a aplicação dessa técnica é específica para cada dataset não existem ferramentas automatizadas. Porém algumas boas ferramentas para criar essas colunas são:
    - [ScikitLearn Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)
    - [Pandas .apply()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html)
    - [Pandas .join()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html)
- *Feature Selection*:  
Nem sempre precisamos de todas as features do nosso dataset para chegarmos ao resultado esperado. Analisar features que não interferem no resultado que esperamos extrair pode consumir muito tempo de processamento e criar confusão no nosso modelo. Um exemplo seria o número de matrícula dos estudantes no dataset do Desafio 2, o modelo irá buscar alguma relação entre este número e a PERFIL, sendo que não existe nenhuma. Isso pode gerar confusões onde ele imagine que matriculas acima de certo valor tem mais chance de entrar determinado PERFIL, por exemplo.  
Algumas features podem também ter uma influência muito pequena na decisão final do modelo, desse modo, retirá-las do dataset pode ser interessante para melhorar a performance e acuracidade do seu modelo.  
Você pode encontrar várias ferramentas para esse tipo de seleção aqui:
    - [Scikit-Learn Feature Selection](https://scikit-learn.org/stable/modules/feature_selection.html#feature-selection)

## Para onde ir agora?
Os livros indicados tem material mais que suficiente para se ocupar durante as semanas da maratona. Caso novos tópicos entrem em pauta, este repositório será atualizado com materiais novos.  
Caso queira ferramentas mais avançadas para desenvolver os projetos aqui vai uma lista de bibliotecas que podem ajudar:
- [missingno](https://github.com/ResidentMario/missingno): Biblioteca para visualização de dados faltantes
- [Pandas Profiling](https://github.com/pandas-profiling/pandas-profiling): Biblioteca com relatórios detalhados para analise superficial de dados.
- [XGBoost](https://xgboost.readthedocs.io/en/latest/): Algorítmo optimizado baseado em Gradient Boosting

## Como contribuir?
Que bom saber que se interessou em contribuir com esse repositório! Para contribuir basta fazer um fork nesse repositório. Após fazer as modificações que achar necessárias faça um Pull Request e assim que o conteúdo for revisado o repositório será atualizado.

## Licença

Este projeto está sobre é considerado Domínio Público - sejo o [LICENSE.md](LICENSE.md) para mais detalhes.
