"""Gera index.html a partir de data/noticias.json e template.html.
Uso: python3 build.py"""
import json, datetime
rows = json.load(open('data/noticias.json', encoding='utf-8'))
tpl = open('template.html', encoding='utf-8').read()
data = json.dumps(rows, ensure_ascii=False).replace('</', '<\\/')
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
open('index.html', 'w', encoding='utf-8').write(tpl.replace('__DATA__', data).replace('__BUILT__', now))
print(len(rows), 'notícias')
