<script>
    export const prerender = true;
    import Layout from 'Layout/Layout.svelte'

    let categoriaCurso = "__categoria__";
    let nomeCurso =  "__nome__";
    let conteudo = "__conteudo__";

    let Assets = '/__assets__';

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
            <div>
                <a class="box is-flex is-justify-content-center is-align-items-center my-4" href={`${Assets}/dowloads.zip`}>
                    <i class="fa-solid fa-download fa-xl mx-3"></i>
                    <h1 class="is-size-5">Baixar arquivos do curso</h1>
                </a>
            </div>
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