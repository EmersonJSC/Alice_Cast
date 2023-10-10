<script>
	import { onMount } from 'svelte';
	let websocket;
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
	let sorteio = Math.floor(Math.random() * possibleNames.length);
	let nome = possibleNames[sorteio];

	const sendMessage = () => {
		console.log(`${nome}: ${message}`);
		websocket.send(`${nome}: ${message}`);
		message = '';
	};

	const connectWebSocket = () => {
		websocket = new WebSocket('ws://alice.dcomp.ufsj.edu.br:33001');

		websocket.onmessage = (event) => {
			const receivedMessage = event.data;
			console.log(receivedMessage);
			historico = [...historico, receivedMessage];
		};
	};
	onMount(() => {
		connectWebSocket();
	});
</script>

<div class="chat has-background-dark">
	<div class="title-box title is-flex is-align-items-center is-justify-content-center">
		<h1 class="title is-5 has-text-white-bis has-text-centered">Chat da transmissão</h1>
	</div>
	<div class="containerChat">
		{#each historico as msg}
			<div class="lineChat mx-3">
				<p class="msg has-text-white-ter">
					{msg}
				</p>
			</div>
		{/each}
	</div>
	<div
		class="sendMsg mt-5 mx-4 is-flex is-align-items-center is-justify-content-center is-flex-direction-column k"
	>
		<form on:submit|preventDefault={sendMessage}>
			<input
				class="textarea has-fixed-size has-background-dark"
				placeholder="Interaja com os usuarios aqui."
				bind:value={message}
			/>
			<div class="sideMsg is-flex is-align-items-center is-justify-content-end mt-2">
				<button class="button Bchat">Chat</button>
				<input type="submit" hidden />
			</div>
		</form>
	</div>
</div>

<style>
	.chat {
		height: 94vh;
		width: 600px;
		border: 1px solid #8b8b8b;
	}
	.title-box {
		border-bottom: 1px solid #8b8b8b;
		height: 60px;
	}
	h1 {
		font-family: 'Roboto', sans-serif;
		font-weight: 300;
	}
	.containerChat {
		/* background-color: #8b8b8b; */
		height: 70%;
		width: 100%;

		overflow-y: auto;
	}
	.lineChat {
		padding: 0.5rem 0.2rem;
	}
	.nome {
		font-family: 'Roboto', sans-serif;
		font-weight: 900;
	}
	.msg {
		font-family: 'Roboto', sans-serif;
		font-weight: 300;
	}
	form {
		width: 100%;
		height: 100%;
	}
	.textarea {
		/* border: 1px solid #000; */
		width: 90%;
		color: #fff;
	}
	.textarea::placeholder {
		color: #fff;
	}
	.sideMsg {
		width: 100%;
	}
	.Bchat {
		background-color: #9fecf8;
	}
</style>
