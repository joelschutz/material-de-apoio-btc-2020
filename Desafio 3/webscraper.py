import requests
import re
import json
from bs4 import BeautifulSoup

def get_ted(url):
    if "ted" not in str(url):
        raise Exception("URL Inválida")

    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="lxml")
    transcript = soup("div", {"class":"Grid Grid--with-gutter d:f@md p-b:4"})
    texts = []
    for div in transcript:
        text = div("p")[0].text
        text = text.strip()
        text = text.replace("\n", " ")
        text = text.replace("\t", " ")
        text = re.sub(' +', ' ', text)
        texts.append(text)

    title_author = soup.title.text
    author = title_author.split(":")[0].strip()
    title = title_author.split(":")[1].split("|")[0].strip()
    return {
    "author": author,
    "body": " ".join(texts),
    "title": title,
    "type": "video",
    "url": url
    }

def get_olhardigital(url):
    if "olhardigital" not in str(url):
        raise Exception("URL Inválida")

    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="lxml")
    transcript = soup.find("div", {"class":"mat-txt"}).find_all('p')
    texts = []
    for p in transcript:
        text = p.text
        text = text.strip()
        text = text.replace("\n", " ")
        text = text.replace("\t", " ")
        text = re.sub(' +', ' ', text)
        texts.append(text)

    title = soup.title.text
    author = soup('span', {'class':'meta-item meta-aut'})[0].text.split(',')[0]
    return {
        "author": author,
        "body": " ".join(texts),
        "title": title,
        "type": 'article',
        "url": url
    }

def get_startse(url):
    if "startse" not in str(url):
        raise Exception("URL Inválida")

    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="lxml")
    transcript = soup.find("div", {"class":"content-single__sidebar-content__content"}).find_all(['p', 'h2'])
    texts = []
    for p in transcript:
        text = p.text
        if '*Foto' in  text or 'Compartilhe em sua rede:' in text: continue
        text = text.strip()
        text = text.replace("\n", " ")
        text = text.replace("\t", " ")
        text = re.sub(' +', ' ', text)
        texts.append(text)

    title = soup.title.text.split(' — ')[0]
    author = soup.find('h4', {'class':'title-single__info__author__about__name'}).find('a').text
    return {
        "author": author,
        "body": " ".join(texts),
        "title": title,
        "type": 'article',
        "url": url
    }

urls = [
'https://www.ted.com/talks/helen_czerski_the_fascinating_physics_of_everyday_life/transcript?language=pt-br#t-81674',
'https://www.ted.com/talks/kevin_kelly_how_ai_can_bring_on_a_second_industrial_revolution/transcript?language=pt-br',
'https://www.ted.com/talks/sarah_parcak_help_discover_ancient_ruins_before_it_s_too_late/transcript?language=pt-br',
'https://www.ted.com/talks/sylvain_duranton_how_humans_and_ai_can_work_together_to_create_better_businesses/transcript?language=pt-br',
'https://www.ted.com/talks/chieko_asakawa_how_new_technology_helps_blind_people_explore_the_world/transcript?language=pt-br',
'https://www.ted.com/talks/pierre_barreau_how_ai_could_compose_a_personalized_soundtrack_to_your_life/transcript?language=pt-br',
'https://www.ted.com/talks/tom_gruber_how_ai_can_enhance_our_memory_work_and_social_lives/transcript?language=pt-br',
'https://olhardigital.com.br/colunistas/wagner_sanchez/post/o_futuro_cada_vez_mais_perto/78972',
'https://olhardigital.com.br/colunistas/wagner_sanchez/post/os_riscos_do_machine_learning/80584',
'https://olhardigital.com.br/ciencia-e-espaco/noticia/nova-teoria-diz-que-passado-presente-e-futuro-coexistem/97786',
'https://olhardigital.com.br/noticia/inteligencia-artificial-da-ibm-consegue-prever-cancer-de-mama/87030',
'https://olhardigital.com.br/ciencia-e-espaco/noticia/inteligencia-artificial-ajuda-a-nasa-a-projetar-novos-trajes-espaciais/102772',
'https://olhardigital.com.br/colunistas/jorge_vargas_neto/post/como_a_inteligencia_artificial_pode_mudar_o_cenario_de_oferta_de_credito/78999',
'https://olhardigital.com.br/ciencia-e-espaco/noticia/cientistas-criam-programa-poderoso-que-aprimora-deteccao-de-galaxias/100683',
'https://www.startse.com/noticia/startups/mobtech/deep-learning-o-cerebro-dos-carros-autonomos',
]
documents = []
for url in urls:
    try: 
        documents.append(get_ted(url))
        print(f"Feito {url}")
    except: pass

    try: 
        documents.append(get_olhardigital(url))
        print(f"Feito {url}")
    except: pass

    try: 
        documents.append(get_startse(url))
        print(f"Feito {url}")
    except: pass

with open('documents.json', 'wt', encoding="utf-8") as file:
    print('Salvando JSON')
    json.dump(documents, file)