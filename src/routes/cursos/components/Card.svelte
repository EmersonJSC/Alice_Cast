<script>
    export let data;
    console.log(data);
    let titulo  = data.nome;
    let autor  = data.autor;
    let assets = data.assets;

</script>

<div class="card mx-1 my-1">
    <div class="card-image">
        <img src="static/assetsGlobal/header.jpeg" alt="Placeholder image">
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