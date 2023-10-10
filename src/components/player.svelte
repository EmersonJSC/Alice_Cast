<script>
	// import './../js/dash.all.min.js';
	import { onMount } from 'svelte';

	var videoName;
	onMount(() => {
		let urlAtual = window.location.href;
		var urlClass = new URL(urlAtual);
		videoName = urlClass.searchParams.get('stream');

		console.log(videoName);
	});
</script>

<div class="playerBox fullcontainer">
	<div class="player">
		<video
			class="fullcontainer"
			data-dashjs-player
			autoplay
			controls
			muted
			src="https://alice.dcomp.ufsj.edu.br/dash/{videoName}.mpd"
		/>
	</div>
</div>

<style>
	.fullcontainer {
		height: 100%;
		width: 100%;
	}
	.player {
		width: 100%;
	}
</style>
