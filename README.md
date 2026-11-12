# Radar Previdenciário

Painel de notícias previdenciárias em alta, com ganchos e roteiros de 45 s para vídeo, estático e stories. Uso interno; conteúdo a revisar com o jurídico e com as regras de publicidade da OAB.

- `data/noticias.json`: as notícias (edite ou acrescente linhas aqui)
- `template.html` + `build.py`: geram o `index.html` (`python3 build.py`)
- `index.html`: o site publicado pelo GitHub Pages

## Hospedagem

- Vercel: projeto ligado a este repositório; cada push em `main` publica o `index.html` já gerado (sem etapa de build).
- Rotina: copiar o JSON novo para `data/noticias.json`, rodar `python3 build.py`, commit e push.
