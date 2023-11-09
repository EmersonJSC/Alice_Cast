<script>
	import { onMount } from 'svelte';
	let websocket;
	let views, usuarios;
	let historico = [];
	let message = '';
	let possibleNames = [
		'Alice',
		'Gato Risonho',
		'Coelho Branco',
		'Coelho Branco',
		'Coelho Branco',
		'Lagarta',
		'Rainha de Copas',
		'Arganaz'
	];
	let chatMessages; // Referência para a div de mensagens
	// Randomic
	let sorteio = Math.floor(Math.random() * possibleNames.length);
	var randomColor = Math.floor(Math.random() * 16777215).toString(16);
	let nome = possibleNames[sorteio];

	let socketParam = { nome: nome, mensagem: message, cor: randomColor };

	const sendMessage = () => {
		socketParam = { nome: nome, mensagem: message, cor: randomColor };
		// console.log(socketParam);
		websocket.send(JSON.stringify(socketParam));
		message = '';
	};

	const connectWebSocket = () => {
		
	
		// views = new WebSocket('wss://alice.dcomp.ufsj.edu.br/chat/views');
		
		// views.onmessage = (event) => {
		// 	usuarios = event.data;
		// 	console.log(usuarios);
		// }
		
		websocket = new WebSocket('ws://alice.dcomp.ufsj.edu.br:33003/chat');
		websocket.onmessage = (event) => {
			const receivedMessage = event.data;
			socketParam = JSON.parse(event.data);
			console.log(socketParam.mensagem);
			historico = [...historico, socketParam];
			chatMessages.scrollTop = chatMessages.scrollHeight;
		};
	};

	onMount(() => {
		connectWebSocket();
	});
</script>

<div class="chat is-flex is-flex-direction-column is-align-items-center is-justify-content-flex-center">
	<div class="chat-container px-4"> 
		<div class="chat-info is-flex is-flex-direction-row is-align-items-center is-justify-content-flex-center">
			<div>
				<h1 class="is-size-6 has-text-weight-semibold">Live Chat</h1>
			</div>
			<div class="chat-views ml-4 is-flex is-flex-direction-row is-size-7 is-align-items-center is-justify-content-flex-center has-text-grey-light">
				<i class="fa-solid fa-users"></i>
				<h4 class="ml-2"> 679 pessoas online</h4>
			</div>
		</div>

		<div class="chat-lines"  bind:this={chatMessages}>
			{#each historico as msg}
			<div class="chat-line is-flex is-align-items-center is-justify-content-flex-center py-0 px-1">
				<p><span class="mr-3" style="color: #{msg.cor}; ">{msg.nome}:</span>{msg.mensagem}</p>
			</div>
			{/each}
		</div>
		
		<div class="chat-input is-flex is-align-items-center is-justify-content-flex-center">
			<form on:submit|preventDefault={sendMessage} class="chat-input mt-4">
				<input class="input chat-enter" placeholder="Converse com o chat aqui" bind:value={message}/>
				<!-- <button class="button">Chat</button> -->
				<input type="submit" hidden />
			</form>
		</div>

	</div>
</div>

<style>
	@media only screen and (min-width: 720px) {
		.chat {
			height: 90vh;
			width: 25vw;

			background-color: #0b1a33;
			z-index: 1000;
			overflow: auto;
			/* width: 30%; */
			/* border: 1px solid #8b8b8b; */
		}
	}
	@media screen and (max-width: 1080px) {
		.chat {
			height: 100vh;
			width: 100vw !important ;

			background-color: #0b1a33;
			width: 200px;
			overflow: hidden;
			
			/* width: 30%; */
			/* border: 1px solid #8b8b8b; */
		}
	}
	.chat-container{
		background: #122951;
		width: 90%;
		height: 85vh;
		border-radius: 15px;
		overflow-y: hidden;

	}
	.chat-info{
		width: 100%;
		height: 10%;
		border-radius: 15px 15px 0 0;
		margin: 0px 0 0 0;

		padding: 0% 5% 0% 5%;

		/* background-color: antiquewhite; */
		font-family: 'Roboto', sans-serif;
		font-weight: bold;
		color: #fff;
	}
	.chat-views{
		/* color: #ff19005b; */
		opacity: 0.5;
	}
	.chat-lines{
		width: 100%;
		height: 65vh;
		overflow-y: auto;

		/* background-color: antiquewhite; */
	}
	.chat-line{
		/* width: 100%; */
		/* height: 10%; */

		margin: 1px 0 0 0;

		/* background-color: aliceblue; */
	}
	.chat-input{
		width: 100%;
		height: 80px;

		/* background-color: #fff; */
	}
	.chat-enter{
		background-color: #0b1a33;
		border-color: #747474;
		color: #fff;
	}
	.chat-enter::placeholder{
		color: #fff;
	}
	.chat-line p{
		color: #fff;
		font-family: 'Roboto', sans-serif;
		padding: 0% 3% 0% 5%;

	}
	.chat-line p span{
		color: #fff;
		font-family: 'Roboto', sans-serif;
		font-weight: 900;
	}
</style>
