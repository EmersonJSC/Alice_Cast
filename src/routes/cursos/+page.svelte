<script>

	import Layout from 'Layout/Layout.svelte';
	import Header from 'CursosComponents/header.svelte'
	import Tags from 'CursosComponents/tags.svelte';
	import Card from 'CursosComponents/Card.svelte';
	
	// import CursosDB from 'Database/JsonDB/Cursos.json'
</script>

<Layout>

	<Tags />
	<Header />

	<div class="is-flex is-flex-wrap-wrap is-align-content-stretch is-justify-content-space-between mx-6">
		<!-- {#each CursosDB as cursos}
			<div class="Cards-container my-1">
				<Card data={cursos} />
			</div>
		{/each} -->
	</div>

</Layout>

<style>
	.dropdown{
		border-color: #fff !important;
	}
	.card{
		width: 300px;
		/* height: 200px; */
	}
	.is-fullheight{
		height: 100%;
	}
	.is-width{
		width: 100%;
	}
	.Cards-container{
		height: 500px;
		width: 400px;
	}
</style>