<script>
    export const prerender = true;
    import Layout from 'Layout/Layout.svelte'

    let categoriaCurso = "Curso";
    let nomeCurso =  "Nome_do_Curso";
    let conteudo = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vitae consequat enim, non suscipit libero. Quisque faucibus, velit at vulputate ultricies, diam tortor ultrices diam, nec consectetur dui erat et est. Aliquam iaculis, turpis sagittis dictum accumsan, purus quam luctus urna, id accumsan elit tortor vitae sapien. Nullam lacus turpis, pretium eget elit eu, ultrices tincidunt enim. Suspendisse sagittis iaculis elementum. Morbi sollicitudin gravida metus, aliquam vulputate quam ullamcorper sed. Ut imperdiet massa purus, vitae viverra enim volutpat vel. Duis pretium condimentum faucibus. Morbi ac aliquet lorem. Aenean in leo luctus, pulvinar tortor sed, sagittis ante. Mauris ac convallis nibh. Nulla tincidunt aliquet tincidunt. Sed sodales, felis sed dignissim efficitur, nunc sapien dignissim tortor, sed tincidunt elit metus at diam. Sed vitae elit quis magna molestie viverra ut et sapien. Curabitur in fermentum sapien, id mattis urna. Duis pretium porta lectus, ut pellentesque magna scelerisque ultricies. Vivamus tristique neque eu ex interdum sollicitudin. Aenean eget ante sem. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Mauris convallis nibh ac suscipit elementum.";

    let Assets = '/assets/nome_do_curso';

</script>

<div>
    <Layout caminho=false>

        <div class="path has-text-primary-light spacing-page">  
            <h1 class="is-size-6 has-text-grey">INICIO/{categoriaCurso.toUpperCase()}/{nomeCurso.toUpperCase()}</h1>
        </div>
        <div class="content spacing-page">
            <div class="category">
                <h1 class="is-size-7 has-text-grey-darker mx-1">{categoriaCurso.toUpperCase()}</h1>
            </div>
            <div class="title">
                <h1 class="title has-text-grey-darker is-size-1">{nomeCurso}</h1>
            </div>
            {#if false}
            <div>
                <a class="box is-flex is-justify-content-center is-align-items-center my-4" href={`${Assets}/documents/doc.zip`}>
                    <i class="fa-solid fa-download fa-xl mx-3"></i>
                    <h1 class="is-size-5">Baixar arquivos do curso</h1>
                </a>
            </div>
            {/if}
            <div class="conteudo">
                <p>     
                    {conteudo}
                </p>
            </div>

            <div class="player my-3">
                <video 
                class="player"
                controls
                muted
                poster="https://th.bing.com/th/id/OIG.CmLs7pBcHDlZ32VQ5Oa8?pid=ImgGn">
                </video>
            </div>

        </div>
    </Layout>
</div>


<style>
    .path{
        font-weight: 100;
        letter-spacing: 3px;
    }
    .content{

    }
    .spacing-page{
        margin: 2% 10% 0px 10%;   
    }
    .category{

    }
    .box{
        height: auto;
        width: 300px;
    }
    .player{
        background-color: aliceblue;
        width: 100%;
        height: 600px;
        object-fit: cover;
    }

    .player video{
        width: 100%;
        height: 100%;
    }


</style>