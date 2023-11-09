import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	resolve: {
		alias: {
			'Layout': '/src/Layout',
			'Globaiscomponents': '/src/Components',
			'playerComponents': '/src/routes/player/components',
			'CursosComponents': '/src/routes/cursos/components',
			'Database':'/src/database',
			

		//   'utils': '/src/utils',
		  // Adicione mais aliases conforme necessário
		},
	  },
});
