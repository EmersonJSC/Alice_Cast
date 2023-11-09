<script>
	import Layout from "./../Layout/Layout.svelte";
</script>

<Layout />
<h1>Home</h1>

<style>
    :global(html){
		overflow: hidden;
		font-family: 'Roboto', sans-serif;
	}
	:global(html::-webkit-scrollbar) {
		width: 12px;              
		background-color: hsl(0, 0%, 29%)
	}
	:global(html::-webkit-scrollbar-track) {
		background: hsl(0, 0%, 14%);       
	}
	:global(body){
		height: 100vh;
		width: 100vw ;
	}
</style>