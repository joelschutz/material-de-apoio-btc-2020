<div align="center">
  <img width="20%" src="https://maratona.dev/static/icons/3-wd.png" alt="Desafio #3 | FIAP" />

</div>

# Desafio 3

O desafio consiste em criar uma ferramenta capaz de acelerar e dinamizar os processos de aprendizagem, ajudando estudantes a encontrar outras fontes de pesquisa, novos conteúdos, exemplos e modelos para seus estudos. Utilizando linguagem natural a ferramenta será capaz de buscar e sugerir conteúdos alternativos, como vídeos, podcasts, e-books e demais fontes de informações, para que estudantes possam aprofundar seus estudos a partir de indicações de texto do próprio estudante.

- [Repositório do Desafio 3](https://github.com/maratonadev-br/desafio-3-2020)

## Objetivo principal

Criar um modelo capaz de recomendar artigos ou vídeos baseados no interesse do usuário. Sua tarefa será estruturar documentos e treinar diversas buscas para esses documentos no serviço.

## Ferramentas

- [Watson Discovery](https://cloud.ibm.com/catalog/services/discovery)

## Dicas

1. Use o [`webscraper.py`](./webscraper.py) para criar todos o seu JSON
2. Procure e extraia **palavras-chave** em cada vídeo/artigo (além do título)
3. Use-as como `queries` e classifique o que for `Revelevant` e `Not Revelevant`
  3.1. Apenas tome cuidado para ter o mínimo de documentos possível por query
4. Treine uma `query negativa`, ou seja, algo que não seja relacionado com os documentos dispostos.

*Dica para intância do serviço:*

1. Tente usar a região de Seoul
2. Sempre tenha cuidado ao número de `queries relevants`
3. De preferência, espere o treinamento das `queries` mínimas (49) para colocar mais

## Desenvolvimento

Durante o desafio, você irá enfrentar dois problemas comuns de um cientista de dados, que são o da estruturação de dados e o da curadoria de modelos de aprendizado de máquina. O primeiro será encontrado ao extrair informações das páginas web listadas abaixo, e o segundo será encontrado ao testar o modelo de Watson Discovery com perguntas customizadas. Oferecemos algumas perguntas de exemplo, mas você terá que pensar em mais perguntas relacionadas aos documentos para treiná-lo, de modo que o número de perguntas totalize em no mínimo 49.

As páginas para as quais pedimos a extração de documentos são de dois tipos diferentes de conteúdo: `article` (artigo) e `video` (vídeo). As de conteúdos em vídeo são de palestras Ted Talks, em que as transcrições em português das falas já estão disponíveis, enquanto as de artigo são de alguns artigos relacionados a tecnologia e inteligência artificial disponíveis em diversos _websites_. Abaixo está a lista de URLs para as quais pedimos a extração:

- <https://www.ted.com/talks/helen_czerski_the_fascinating_physics_of_everyday_life/transcript?language=pt-br#t-81674>
- <https://www.ted.com/talks/kevin_kelly_how_ai_can_bring_on_a_second_industrial_revolution/transcript?language=pt-br>
- <https://www.ted.com/talks/sarah_parcak_help_discover_ancient_ruins_before_it_s_too_late/transcript?language=pt-br>
- <https://www.ted.com/talks/sylvain_duranton_how_humans_and_ai_can_work_together_to_create_better_businesses/transcript?language=pt-br>
- <https://www.ted.com/talks/chieko_asakawa_how_new_technology_helps_blind_people_explore_the_world/transcript?language=pt-br>
- <https://www.ted.com/talks/pierre_barreau_how_ai_could_compose_a_personalized_soundtrack_to_your_life/transcript?language=pt-br>
- <https://www.ted.com/talks/tom_gruber_how_ai_can_enhance_our_memory_work_and_social_lives/transcript?language=pt-br>
- <https://olhardigital.com.br/colunistas/wagner_sanchez/post/o_futuro_cada_vez_mais_perto/78972>
- <https://olhardigital.com.br/colunistas/wagner_sanchez/post/os_riscos_do_machine_learning/80584>
- <https://olhardigital.com.br/ciencia-e-espaco/noticia/nova-teoria-diz-que-passado-presente-e-futuro-coexistem/97786>
- <https://olhardigital.com.br/noticia/inteligencia-artificial-da-ibm-consegue-prever-cancer-de-mama/87030>
- <https://olhardigital.com.br/ciencia-e-espaco/noticia/inteligencia-artificial-ajuda-a-nasa-a-projetar-novos-trajes-espaciais/102772>
- <https://olhardigital.com.br/colunistas/jorge_vargas_neto/post/como_a_inteligencia_artificial_pode_mudar_o_cenario_de_oferta_de_credito/78999>
- <https://olhardigital.com.br/ciencia-e-espaco/noticia/cientistas-criam-programa-poderoso-que-aprimora-deteccao-de-galaxias/100683>
- <https://www.startse.com/noticia/startups/mobtech/deep-learning-o-cerebro-dos-carros-autonomos>

A partir dessas URLs, pedimos que você monte documentos JSON contendo as seguintes chaves e valores:

```json
{
  "author": "Autor/Autora do conteúdo",
  "body": "Corpo do conteúdo (transcrição da palestra ou todo o corpo de um artigo)",
  "title": "Título da palestra ou artigo",
  "type": "Tipo do conteúdo (deve ser exatamente article ou video)",
  "url": "URL onde o conteúdo foi acessado"
}
```

**Os nomes das chaves devem ser exatamente esses para garantir que o seu modelo consiga ser bem avaliado. Na chave "type", o valor deverá ser sempre `article`, no caso de um artigo, ou `video`, no caso de um vídeo.** O nome do arquivo não é relevante para o treinamento.

Após a criação dos documentos, você deverá criar uma coleção no Watson Discovery e inseri-los na sua coleção. Após o carregamento dos documentos, você deverá treinar as respostas do modelo a algumas perguntas, identificando quais documentos são relevantes para tal resposta e quais não são. O seu modelo deve ter no mínimo **49 _queries_** treinadas, cada uma com pelo menos um documento marcado como relevante ou não relevante, para que possa ser treinado. Disponibilizamos alguns exemplos de _queries_ para iniciar o treinamento (note que algumas perguntas não têm relação com nenhum dos documentos, para essas, todas as sugestões devem ser marcadas como não relevantes):

- "Gostaria de um artigo que falasse sobre inteligência artificial e carros autônomos
- "Os riscos do Machine Learning"
- "Artigo sobre as teorias sobre o tempo"
- "Vídeo sobre estatística avançada"
- "História do Brasil"

_Dica: a etapa do carregamento dos documentos no Watson Discovery pode demorar alguns minutos e às vezes falhar. É recomendado que seja feito o upload de apenas um documento por vez para garantir que não haja nenhuma falha._
