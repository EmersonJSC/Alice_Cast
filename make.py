import os
import glob
import shutil
import json

# diretorio static
dir_Static = "static"
dir_Raiz = "src"

cursos_json = 'src/routes/cursos/cursos.json'

Layout = 'make_exemple/curso_page/+page.svelte'


pastas_assets = []

caminho_assets = os.path.join(dir_Static, "assets")

print("Listando pastas...")
if os.path.exists(caminho_assets) and os.path.isdir(caminho_assets):
     pastas_assets = [pasta for pasta in os.listdir(caminho_assets) if os.path.isdir(os.path.join(caminho_assets, pasta))]

# Verifique a existência de pastas e arquivos em cada pasta encontrada
for pasta in pastas_assets:
     print(f" [+]Verificando os arquivos da pasta "+ pasta +" ...")
     caminho_pasta = os.path.join(caminho_assets, pasta)
     caminho_imagens = os.path.join(caminho_pasta, "images")
     caminho_documentos = os.path.join(caminho_pasta, "documents")
     caminho_videos = os.path.join(caminho_pasta, "videos")
     content_json = os.path.join(caminho_pasta, "content.json")
     
     download = os.path.join(caminho_pasta, "documents" ,"download.zip")
     images = os.path.join(caminho_pasta, "images" ,"header.jpeg")
     
     if (os.path.exists(download)):
          download = 'true'
     else:
          download = 'false'
          
     if (os.path.exists(images)):
          images = 'true'
     else:
          images = 'false'
          

     if (os.path.exists(caminho_imagens) and os.path.exists(caminho_documentos) and os.path.exists(caminho_videos) and os.path.exists(content_json)):
          dados = None
          with open(content_json, 'r') as arquivo_json:
                dados = json.load(arquivo_json)

          caminho_curso = os.path.join(dir_Raiz, "routes", "cursos", "curso", pasta)
          os.makedirs(caminho_curso.lower(), exist_ok=True)

          
          if os.path.exists(cursos_json):
               with open(cursos_json, 'r') as arquivo_json:
                    lista_cursos = json.load(arquivo_json)
          else:    
               lista_cursos = []
          
          novo_curso = {
               "nome": dados["nome"],
               "assets": "assets/"+ pasta,
               "categoria": dados["categoria"],
               "autor": dados["autor"],
               "caminho": pasta,
               "header": images
          }
          
          if novo_curso not in lista_cursos:
               lista_cursos.append(novo_curso)

          with open(cursos_json, 'w') as arquivo_json:
               json.dump(lista_cursos, arquivo_json, indent=2)
     
          with open(os.path.join(caminho_curso.lower(), "+page.svelte"), "w") as arquivo_svelte:
               with open(Layout, 'r') as arquivo:
                    conteudo = arquivo.read()
                    conteudo = conteudo.replace('__categoria__', str(dados["categoria"]))
                    conteudo = conteudo.replace('__nome__', str(dados["nome"]))
                    conteudo = conteudo.replace('__assets__', os.path.join(caminho_pasta[len("static/"):]))
                    conteudo = conteudo.replace('__conteudo__',  str(dados["conteudo"]))
                    conteudo = conteudo.replace('__download__',  str(download))
                    arquivo_svelte.write(conteudo)
               

     else:
          print(f"[+] Erro na pasta: {pasta}")
          print("Você precisa separar os arquvis em 'images', 'documents', 'videos', 'contet.json' ")          


