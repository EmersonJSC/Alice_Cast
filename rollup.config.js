import svelte from 'rollup-plugin-svelte';
import alias from '@rollup/plugin-alias';

export default {
  input: 'src/main.js', // Substitua 'src/main.js' pelo seu ponto de entrada
  output: {
    file: 'public/build/bundle.js', // Substitua o caminho de saída desejado
    format: 'iife'
  },
  plugins: [
    svelte(), // Adicione outros plugins conforme necessário
    alias({
        entries: [
          { find: 'components', replacement: './src/Components' },
        //   { find: 'utils', replacement: './src/utils' },
          // Adicione mais entradas conforme necessário
        ]
      })
  ]
};