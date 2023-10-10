<script>
	// import Index from './../components/index.svelte';
	import SideBar from './../components/sideBar.svelte';
	import TopBar from './../components/topBar.svelte';
	import Player from './../components/player.svelte';
	import Chat from './../components/chat.svelte';

	let count = 0;
</script>

<div class="body is-flex is-flex-direction-row">
	<SideBar />
	<div class="is-flex is-flex-direction-column fullcontainer">
		<TopBar />
		<div class="is-flex is-flex-direction-row fullcontainer">
			<Player />
			<Chat />
		</div>
	</div>
</div>

<style>
	.body {
		height: 100vh;
		width: 99vw;
	}
	.fullcontainer {
		height: 100%;
		width: 100%;
	}
</style>
