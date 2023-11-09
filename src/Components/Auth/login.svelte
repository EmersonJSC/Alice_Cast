<script>
	import { onMount } from 'svelte';
	let websocket;
    let socketParam;

    let usuario;
    let senha;

    const connectWebSocket = () => {
        websocket = new WebSocket('ws://alice.dcomp.ufsj.edu.br:33003/auth');
		websocket.onmessage = (event) => {
			const receivedMessage = event.data;
			socketParam = JSON.parse(event.data);
			console.log(socketParam.mensagem);
			historico = [...historico, socketParam];
			chatMessages.scrollTop = chatMessages.scrollHeight;
		};
    }

    const sendAuth = () => {
		socketParam = { "process": "Login", "data": { "usuario": `${usuario}`, "senha":`${senha}` } };
		console.log(socketParam);
		websocket.send(JSON.stringify(socketParam));

	};

    onMount(() => {
		connectWebSocket();
	});
</script>

<div class="auth-conteiner is-flex is-align-items-center is-justify-content-center">
    <div class="box">
        <h1 class="has-text-centered is-size-4 has-text-weight-semibold mb-6">Entrar no AliceCast</h1>
        <form on:submit|preventDefault={sendAuth}>
            <label>Login:</label>
            <input class="input my-3" bind:value={usuario}>
            <label>Senha:</label>
            <input class="input my-3" bind:value={senha}>

            <button class="button is-fullwidth mt-4">Logar</button>
        </form>
        <p class="mt-4">Esqueceu sua senha? <a>Lembre-se aqui</a>  </p>
    </div>
    
</div>

<style>
    .auth-conteiner{
        position: absolute;
        top: 0%;
        right: 0%;

        width: 100%;
        height: 100%;

        font-family: 'Roboto', sans-serif;
    }
    .box{
        width: 20vw;
    }
</style>