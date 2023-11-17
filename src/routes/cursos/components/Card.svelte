<script>
    export let data;
    console.log(data);
    let titulo  = data.nome;
    let autor  = data.autor;
    let assets = data.assets;
   
    const imagePath = '/images/header.jpeg';
    
</script>

<a href='cursos/curso/{data.caminho.toLowerCase()}'>
    <div class="card mx-1 my-1">
        <div class="card-image">
            
            <img src="/images/header.jpeg "style="z-index: 1;" onerror="this.onerror=null; this.src='images/header.jpeg';">
           
        </div>
        <div class="card-content">
            <div class="content my-2">
                <h1 class="title is-size-4">{titulo}</h1>
                <h3 class="subtitle is-size-6">{autor}</h3>
            </div>
        </div>
    </div>
</a>

<style>
	.card{
		width: 100%;
        height: 100%;
        position: relative;
        /* min-width: 100px; */
        /* max-width: 200px; */
		/* height: 200px; */
	}
    .card-image{
        width: 100%;
        height: 75%;
    }
    .card-image img {
        position: absolute;
        /* top: 0;
        left: 0; */
        /* width: 100%;
        height: 100%; */
    }
    .placeholder {
        z-index: 0; /* Define a imagem de placeholder para estar atrás da imagem principal */
    }

</style>