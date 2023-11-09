<script>
    export let data;
    let titulo  = data.Curso_Name
    let autor  = data.Autor
    let nomeDaImagem = "Exemple"
    // import CardImagem from 'Database/Cursos/curso/nome_do_curso/header.jpeg'
    let database = null;

    // import * as arquivos from `../../../database/Cursos/${data.Curso_Name}`

    import(`../../../database/Cursos/${nomeDaImagem}/*.jpeg`)
        .then((module) => {
            database = module;
        })
        .catch((error) => {
            console.error('Erro ao carregar a imagem', error);
        });
    
</script>

<div class="card mx-1 my-1">
    <div class="card-image">
        <!-- <img src={CardImagem} alt="Placeholder image"> -->
    </div>
    <div class="card-content">
        <div class="content">
            <h1 class="title is-size-4">{titulo}</h1>
            <h3 class="subtitle is-size-6">{autor}</h3>
        </div>
    </div>
</div>

<style>
	.card{
		width: 100%;
        height: 100%;
        /* min-width: 100px; */
        /* max-width: 200px; */
		/* height: 200px; */
	}

</style>