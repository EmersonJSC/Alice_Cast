<script>

	import Layout from 'Layout/Layout.svelte';
	import Header from 'CursosComponents/header.svelte'
	import Tags from 'CursosComponents/tags.svelte';
	import Card from 'CursosComponents/Card.svelte';
	import { onMount } from 'svelte';

	import Cursos from './cursos.json'; //json do curso

	const pesquisar = (termo) =>{
		if (termoPesquisa === '') {
			return Cursos; // Se a pesquisa for vazia, exibir todos os cursos
		} else {
			return resultados = Cursos.filter(curso =>
				curso.nome.toLowerCase().includes(termoPesquisa.toLowerCase())
			);
		}
	};

	console.log();
</script>

<Layout>

	<Tags />
	<Header />

	<div class="main is-flex is-flex-wrap is-align-content-stretch is-justify-content-flex-start mx-6">
		{#each Cursos as curso}
			<div class="Cards-container my-3 mx-6">
				<Card data={curso} />
			</div>
		{/each}
	</div>

</Layout>

<style>
	.main{
		flex-wrap: wrap;
	}
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