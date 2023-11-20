<script>
	import logo from "../img/AliceCastRed.png"

	const menu = [{ nome:"Home", icone:"fa-house", link:"#" }, { nome:"Sala Zoo", icone:"fa-video", link:"/player" }, { nome:"Cursos", icone:"fa-graduation-cap", link:"/cursos" }]
</script>

<div class="SideBar full background is-flex is-flex-direction-column">
	<div>
		<div class="top-sidebar is-flex is-justify-content-center is-align-items-center">
			<img
				src="{logo}"
				class="image logo"
			/>
		</div>
	</div>
	
	<div>
		<aside class="menu"> 
			<!-- <p class="menu-label px-2 has-text-white-bis  menu-txt">Menu</p> -->
			{#each menu as item}
			<ul class="menu-list">
				<li>
					<a class="item-menu has-text-white-ter" href="{item.link}"><i class="fa-solid {item.icone} mx-4" /><span class="menu-txt">{item.nome}</span></a>
				</li>
			</ul>
			{/each}
		</aside>
	</div>
	
</div>

<style>
	@media only screen and (min-width: 720px) {
		
		.SideBar {
			/* background-color: black; */
			height: 100%;
			width: 200px;
			z-index: 1000;
			overflow: hidden;
			padding-top: 10px;
		}
	}
	@media screen and (max-width: 1080px) {
		.SideBar {
			/* background-color: black; */
			height: 100vh;
			width: 70px;
			z-index: 1000;
			overflow: hidden;
			padding-top: 40px;
		}
		.menu-txt{
			display: none;
		}
	}
	.menu{
			margin-top: 20px;
		}
	.top-sidebar {
		/* height: 10px; */
		width: 100%;
	}
	.item-menu:hover {
		background-color: #b4f2ff;
	}
	.active {
		background-color: #5ce1f4;
	}
	.background {
		background-color: #0b1a33;
	}
	.logo{
		width: 50%;
		/* margin-top: 80px; */
	}

</style>
