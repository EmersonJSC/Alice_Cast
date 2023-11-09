<!-- PAGINA DO PLAYER -->
<script>

	import Layout from './../../Layout/Layout.svelte';
	import Player from './components/player.svelte';
	import Chat from './components/chat.svelte'

	import { onMount } from 'svelte';

	var videoName = "Alice";
	
	onMount(() => {
		let urlAtual = window.location.href;
		var urlClass = new URL(urlAtual);
		videoName = urlClass.searchParams.get('stream');

		console.log(videoName);
	});

</script>

	<Layout >
		<div class="is-flex Layout-mobile">
			<div class="player-body is-flex-grow-5">
				<Player videoName={videoName} />
			</div>
			<div class="chat">
				<Chat />
			</div>
		</div>
		
		
	</Layout>
	

<style>
	:global(html){
		overflow: hidden;
	}
	:global(html::-webkit-scrollbar) {
		width: 12px;              
		background-color: hsl(0, 0%, 29%)
	}
	:global(html::-webkit-scrollbar-track) {
		background: hsl(0, 0%, 14%);       
	}
	:global(body){
		/* background-color: hsl(0, 0%, 21%); */
		background-color: #122951;

	}
	@media only screen and (min-width: 720px) {
		.Layout-mobile{
			flex-direction: row;
		}
	}
	@media screen and (max-width: 1080px) {
		.Layout-mobile{
			flex-direction: column;
		}
	}

	.player-body{
		/* height: 70vh; */
		/* background-color: blanchedalmond; */

	}

	/* Estilizando a barra de rolagem vertical */
	.player-body::-webkit-scrollbar {
		width: 5px;
	}

	.player-body::-webkit-scrollbar-thumb {
		background: #5ce1f4; /* Cor do polegar da barra de rolagem */
		border-radius: 6px;
	}

	.player-body::-webkit-scrollbar-thumb:hover {
		background: #0056b3; /* Cor do polegar da barra de rolagem ao passar o mouse */
	}

	.player-body::-webkit-scrollbar-track {
		background: #0b1a33; /* Cor de fundo da barra de rolagem */
		border-radius: 6px;
	}

	.player-body::-webkit-scrollbar-thumb {
		width: 12px;
	}
	
	
</style>


