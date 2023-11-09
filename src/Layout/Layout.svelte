<script>
	import SideBar from './SideBar.svelte';
	import TopBar from './TopBar.svelte';
	export let content;
	export let caminho = false;
</script>

<div class="is-flex is-flex-direction-row fullheight">
	<div class="is-flex-grow-0">
		<SideBar />
		
	</div>
	<div class="is-flex-grow-5 is-flex is-flex-direction-column">
		<TopBar caminho=false />
		<slot></slot>
	</div>
</div>

<style>
	.fullheight{
		height: 100vh;
	}
</style>