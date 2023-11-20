import os
import glob
import shutil
import json

########Diretorios
dir_Static = "static"
dir_Raiz = "src"
cursos_json = 'src/routes/cursos/cursos.json'
caminho_assets = os.path.join(dir_Static, "assets")

#######Layout
Layout = 'make_exemple/curso_page/+page.svelte'

######Array para listar as pastas existentes 
pastas_assets = []

def main():
    pastas_assets = listar_pastas()
    for pasta in pastas_assets:
        caminhos = buscar_caminhos(pasta)
        if(os.path.exists(caminhos["content_json"])):
             print("[!] Erro na pasta:" + caminhos["caminho_pasta"] +"content.json não encontrad")
             continue
        verificar_images(caminhos)
        compactar_assets(caminhos)
        GerarPaginas(caminhos)
        


    




def listar_pastas():
    print("Listando pastas...")
    if os.path.exists(caminho_assets) and os.path.isdir(caminho_assets):
        pastas_assets = [pasta for pasta in os.listdir(caminho_assets) if os.path.isdir(os.path.join(caminho_assets, pasta))]
        return pastas_assets

def buscar_caminhos(caminho_pasta):
        print(f" [+]Verificando os arquivos da pasta "+ caminho_pasta +" ...")

        caminho_pasta = caminho_pasta
        caminho_imagens = os.path.join(caminho_pasta, "images")
        caminho_documentos = os.path.join(caminho_pasta, "documents")
        caminho_videos = os.path.join(caminho_pasta, "videos")
        content_json = os.path.join(caminho_pasta, "content.json")
        download = os.path.join(caminho_pasta, "documents" ,"download.zip")
        images = os.path.join(caminho_pasta, "images" ,"header.jpeg")

        caminhos = {
            "caminho_pasta": caminho_pasta,
            "caminho_imagens": caminho_imagens,
            "caminho_documentos": caminho_documentos,
            "caminho_videos": caminho_videos,
            "content_json": content_json,
            "download": download,
            "images": images
        }

        return caminhos
    
def verificar_images(caminho):
    if( not os.path.exists(caminho['images'])):
          shutil.copy("make_exemple/curso_page/header.jpeg","static/assets/"+ caminho['caminho_pasta'] +"/images")
    
def compactar_assets(caminho):
    try:
        caminho_pasta = caminho['caminho_pasta']
        # Compacta a pasta
      
        shutil.make_archive("downloads", 'zip', 'static/assets/'+ caminho['caminho_pasta'])
        
        # Move o arquivo ZIP para dentro da pasta original
        print(caminho_pasta)
        
        shutil.move("downloads.zip", 'static/assets/'+ caminho['caminho_pasta'])
        print(f"Pasta compactada e o arquivo ZIP foi colocado dentro de {caminho_pasta}")
    except Exception as e:
        print(f"Ocorreu um erro ao compactar a pasta e colocar o arquivo ZIP dentro dela: {e}")

def GerarPaginas(caminhos):
    print('static/assets/' + caminhos["content_json"])
    with open('static/assets/' + caminhos["content_json"], 'r') as arquivo_json:
        dados = json.load(arquivo_json)

    caminho_curso = os.path.join(dir_Raiz, "routes", "cursos", "curso", caminhos["caminho_pasta"])
    os.makedirs(caminho_curso.lower(), exist_ok=True)

    if os.path.exists(cursos_json):
        with open(cursos_json, 'r') as arquivo_json:
            lista_cursos = json.load(arquivo_json)
    else:    
        lista_cursos = []
    
    novo_curso = {
        "nome": dados["nome"],
        "assets": "assets/"+ caminhos["caminho_pasta"],
        "categoria": dados["categoria"],
        "autor": dados["autor"],
        "caminho": caminhos["caminho_pasta"],
        "header": caminhos["images"]
    }
     
    if novo_curso not in lista_cursos:
        lista_cursos.append(novo_curso)
    
    with open(cursos_json, 'w') as arquivo_json:
        json.dump(lista_cursos, arquivo_json, indent=2)


    print(caminhos["caminho_pasta"][len("static/")])
    exit
    with open(os.path.join(caminho_curso.lower(), "+page.svelte"), "w") as arquivo_svelte:
               with open(Layout, 'r') as arquivo:
                    conteudo = arquivo.read()
                    conteudo = conteudo.replace('__categoria__', str(dados["categoria"]))
                    conteudo = conteudo.replace('__nome__', str(dados["nome"]))
                    conteudo = conteudo.replace('__assets__', str(os.path.join(caminhos["caminho_pasta"][len("static/")])))
                    conteudo = conteudo.replace('__conteudo__',  str(dados["conteudo"]))
                    conteudo = conteudo.replace('__download__',  str(caminhos["download"]))
                    arquivo_svelte.write(conteudo)



if __name__ == "__main__":
    main()
    print("Pronto")