<script>
	import Player from './player.svelte';
	// import './../js/dash.all.min.js';
	export let videoName = "Alice";
	export let imgusuario = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFqZMMWnIwg5s5uicldr-MVKpmu_2e1KWaIm2wNzp-Oqs4uyaqRGY8TFhBHIdWOMFMYPs&usqp=CAU";
	export let online = false;
	export let nomeStreamer = "Default_Name";
	export let org = "Default_Org"
</script>
	<div>
		<div class="player px-4 py-4">
			<video
			class="player"
			data-dashjs-player
			autoplay
			controls
			muted
			src="https://alice.dcomp.ufsj.edu.br/dash/{videoName}.mpd"/>
		</div>

		<div class="player-info mx-3 py-2 is-flex is-flex-direction-row is-align-items-center">
			<figure class="mx-3 image is-48x48 ">
				{#if online == true}
				<img 
					class="is-rounded"
					src="{imgusuario}" 
					style="border: 3px solid #3a9e2b;"
				/>
				{:else}
				<img 
					class="is-rounded"
					src="{imgusuario}" 
					style="border: 0px solid #3a9e2b;"
				/>
				{/if}
			</figure>

			<div>
				<h1 class="mx-4 has-text-white-bis is-size-4 has-text-weight-semibold">{nomeStreamer}</h1>
				<h2 class="mx-4 has-text-white-bis is-size-7 has-text-weight-light">{org}</h2>
			</div>
			
		</div>
	</div>
	
<style>

	video {
	/* width: 100%; */
	/* border: 2px solid #ccc; */
		border-radius: 15px;
	}

	video::-webkit-media-controls {
	background-color: hsl(0, 0%, 14%);
	}

	video::-webkit-media-controls-play-button {
	color: #fff;
	}
	.player{
		width: 100%;
		height: 100%;
		/* background-color: aqua; */
	}
	.player-info{
		border-radius: 15px;
		background-color: #0b1a33;
	}
</style>
