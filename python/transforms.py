import base64
import mammoth
from bs4 import BeautifulSoup

docx_path = 'documento.docx'  # Substitua pelo caminho do seu arquivo DOCX
html_path = 'output.html'     # Substitua pelo caminho do seu arquivo HTML de saída

header_senado = """
<div class="sf-wrapper">
    <div class="js-sidebar-mountpoint" data-url="https://www12.senado.leg.br/hpsenado/wssidebar.json"></div>
  </div><!-- Fim - sidebar-comum.html - todas as formas de utilização -->
  <div class="sf-wrapper">
    <nav class="Triad navbar_global">
      <div>
        <button class="btn btn-lg btn-secondary js-sidebar-action" id="jstoggle" type="button">
          <i class="fas fa-bars"></i><span class="u-hideLower title-n">
            Menu</span>
        </button>
      </div>
      <div>
        <a class="navbar_global-brand" href="https://www.senado.leg.br" title="Senado Federal"><img
            src="https://www.senado.leg.br/noticias/essencial/images/senado.svg" alt="Senado Federal"></a>
      </div>
      <div>
        <div class="Rail Rail--fenced u-hideLower">
          <a class="js-vlibras" role="button" title="acessibilidade">
            <img src="https://www.senado.leg.br/noticias/essencial/images/hands.svg" width="25px"></a>
          <a class="link link-deep"
            href="https://www12.senado.leg.br/institucional/responsabilidade-social/acessibilidade/pages/acessibilidade-no-portal-do-senado">Acessibilidade</a><a
            class="link link-deep" href="http://www12.senado.gov.br/institucional/falecomosenado">Fale
            com o Senado</a>
        </div><a class="btn btn-lg btn-secondary u-hideUpper"
          href="http://www12.senado.gov.br/institucional/falecomosenado"><i class="fas fa-phone"></i></a>
      </div>
    </nav>
  </div>
  <!-- Fim - Cabeçalho padrão -->
  <div class="sf-wrapper">
    <div class="menu-local">
      <div class="pt-2"><a class="nav_control-title d-none" href="#" title="Logo Portal"><img class="img-fluid" src="?"
            alt="Logo Portal"></a>
        <div class="nav_control-title">
          <h1 class="titulo-pagina"><a href="https://www12.senado.leg.br/transparencia">Institucional</a>
            <svg xmlns="http://www.w3.org/2000/svg" style="fill: white;" height="24" viewBox="0 -960 960 960" width="24"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>
            <span
              style="font-size: 30px">DataSenado</span></h1>
        </div>
      </div>
      <button class="btn_control-res btn btn-tertiary btn-lg" type="button" data-toggle="collapse.se"
        data-target="#menu-local__form" aria-controls="menu-local__form" aria-expanded="false"
        aria-label="Exibe busca"><i class="fas fa-search"></i></button>
      <form class="menu-local__form collapse" id="menu-local__form" method="GET"
        action="https://www6g.senado.leg.br/busca/">
        <input type="hidden" name="portal" value="Transparência">
        <div class="search-wrapper">
          <input class="form-control search-out" type="search" name="q" placeholder="Buscar">
          <button class="search-btn" type="submit"><i class="fas fa-search"></i></button>
        </div>
      </form>
    </div>
  </div>
  <div class="sf-wrapper">
    <nav class="navbar navbar_control navbar-expand-lg navbar--sf mb-0">
      <div class="navbar-toggler navbar-toggler--sf" role="button" data-toggle="collapse.se"
        data-target="#sfMenuLocalDropdown" aria-controls="sfMenuLocalDropdown" aria-expanded="false"
        aria-label="Exibe navegação">
        <button class="btn btn-secondary"><i class="fas fa-bars"></i></button>
        <div class="ml-2">MENU DESTA SEÇÃO</div>
      </div>
      <div class="collapse navbar-collapse-se" id="sfMenuLocalDropdown">
        <ul class="navbar-nav navbar-nav--sf">
          <li class="nav-item">
            <a class="link link--nav" href="https://www12.senado.leg.br/institucional/datasenado/sobre">Sobre</a>
          </li>
          <li class="nav-item">
            <a class="link link--nav"
              href="https://www12.senado.leg.br/institucional/datasenado/pesquisasrealizadas">Pesquisas</a>
          </li>
          <li class="nav-item">
            <a class="link link--nav"
              href="https://www12.senado.leg.br/institucional/datasenado/enquetesrealizadas">Enquetes</a>
          </li>
          <li class="nav-item">
            <a class="link link--nav"
              href="https://www12.senado.leg.br/institucional/datasenado/publicacoesdatasenado">Publicações</a>
          </li>
          <li class="nav-item">
            <a class="link link--nav"
              href="https://www12.senado.leg.br/institucional/datasenado/datasenado-na-midia">DataSenado na Mídia</a>
          </li>
          <li class="nav-item">
            <a class="link link--nav" href="https://www12.senado.leg.br/institucional/datasenado/metodo">Método</a>
          </li>
          <li class="nav-item">
            <a class="link link--nav" href="https://www12.senado.leg.br/institucional/datasenado/videos">Vídeos</a>
          </li>
          <li class="nav-item dropdown">
            <a class="link link--nav dropdown-toggle" href="https://www25.senado.leg.br/web/atividade/mais"
                data-toggle="dropdown.se" aria-haspopup="true" aria-expanded="false">
                Mais
            </a>
            <div class="dropdown-menu dropdown-menu--sf" aria-labelledby="js-menu-1">
                <a class="dropdown-item" role="presentation"
                    href="https://www.senado.leg.br/institucional/datasenado/paineis_dados/#/?pesquisa=violencia_domestica_familiar">Painel Violência Domestica e Familiar contra a Mulher</a>
                <a class="dropdown-item" role="presentation"
                    href="https://www.senado.leg.br/institucional/datasenado/panorama/#/">Panorama Legislativo Municipal</a>
                <a class="dropdown-item" role="presentation"
                    href="https://www12.senado.leg.br/institucional/omv">Observatório da Mulher</a>
                <a class="dropdown-item" role="presentation"
                    href="https://www12.senado.leg.br/perguntas-frequentes">Perguntas Frequentes</a>
            </div>
        </li>
        </ul>
      </div>
    </nav>
  </div>
"""

footer_senado = """
<div class="sf-wrapper">
    <footer class="Footer">
        <div class="container">
            <div class="Triad Triad--stackable">
                <div class="Rail gamma my-2"><a class="link link-deep--facebook"
                        href="https://www.facebook.com/SenadoFederal" title="Facebook" target="_blank"><i
                            class="fab fa-facebook"></i></a><a class="link link-deep--twitter"
                        href="https://twitter.com/senadofederal" title="Twitter" target="_blank"><i
                            class="fab fa-twitter"></i></a><a class="link link-deep--instagram"
                        href="https://www.instagram.com/senadofederal" title="Instagram" target="_blank"><i
                            class="fab fa-instagram"></i></a><a class="link link-deep--youtube"
                        href="https://www.youtube.com/user/TVSenadoOficial" title="Youtube" target="_blank"><i
                            class="fab fa-youtube"></i></a></div>
                <div class="Rail my-2"><a href="https://www.camara.leg.br" title="Câmara dos Deputados"
                        target="_blank"><img
                            src="https://www.senado.leg.br/noticias/essencial/images/icon-camara.svg"
                            alt="Câmara dos Deputados"></a><a href="https://www.congressonacional.leg.br"
                        title="Congresso Nacional" target="_blank"><img
                            src="https://www.senado.leg.br/noticias/essencial/images/icon-congresso.svg"
                            alt="Congresso Nacional"></a><a href="https://www.tcu.gov.br"
                        title="Tribunal de Contas da União" target="_blank"><img
                            src="https://www.senado.leg.br/noticias/essencial/images/icon-tcu.svg"
                            alt="Tribunal de Contas da União"></a></div>
                <div class="Rail Rail--fenced my-2"><a class="link link-deep"
                        href="https://www12.senado.leg.br/institucional/carta-de-servicos/en/carta-de-servicos">ENGLISH</a><a
                        class="link link-deep"
                        href="https://www12.senado.leg.br/institucional/carta-de-servicos/es/carta-de-servicos">ESPAÑOL</a><a
                        class="link link-deep"
                        href="https://www12.senado.leg.br/institucional/carta-de-servicos/fr/carta-de-servicos">FRANÇAIS</a>
                </div>
            </div>
            <div class="divider my-2"></div>
            <div class="Triad Triad--stackable">
                <div class="my-2"><a class="link link-deep" href="https://intranet.senado.leg.br"
                        title="Intranet"><i class="fas fa-lock mr-1"></i> Intranet</a></div>
                <div class="Rail Rail--fenced Rail--stackable my-2"><a class="link link-deep"
                        href="https://www12.senado.leg.br/institucional/pessoas/pessoas">Servidor efetivo</a><a
                        class="link link-deep"
                        href="https://www12.senado.leg.br/institucional/pessoas/pessoas">Servidor comissionado</a><a
                        class="link link-deep"
                        href="https://www12.senado.leg.br/institucional/pessoas/pessoas">Servidor aposentado</a><a
                        class="link link-deep"
                        href="https://www12.senado.leg.br/institucional/pessoas/pessoas">Pensionista</a></div>
                <div class="my-2"><a class="link link-deep"
                        href="https://www12.senado.leg.br/institucional/falecomosenado" title="fale com o Senado"><i
                            class="fas fa-phone u-flip-x mr-1"></i> Fale com o Senado</a></div>
            </div>
            <div class="divider my-2"></div>
            <div class="d-flex justify-content-xl-center"><span class="my-2">Senado Federal - Praça dos Três Poderes
                    - Brasília DF - CEP 70165-900 | <span class="text-nowrap">Telefone: 0800 0 61 2211</span></span>
            </div>
        </div>
    </footer>
</div>
"""

# Estilos CSS e scripts 
pacotes_auxiliares = """
<style>
@import "https://www.senado.leg.br/inc/essencial-2020/css/essencial.css";
@import "https://www.senado.leg.br/inc/essencial-2020/css/essencial-fix-bs2.css";
    body {
        font-family: 'Roboto', sans-serif !important;
        margin: 0px !important;
        padding: 0px !important;
    }
    h1 {
        font-size: 34px !important;
    }
    p {
        font-size: 17px !important;
    }
    .container {
        max-width: 1200px !important; /* Define a largura máxima do conteúdo */
        margin: 0 auto !important; /* Centraliza o conteúdo */
        padding: 15px !important; /* Adiciona padding */
    }
    table {
        width: 100%;
        border-collapse: collapse !important;
        margin-bottom: 20px !important;
    }
    th, td {
        border: 1px solid #d3d3d3 !important;  /* Cor das bordas das células */
        padding: 8px !important;
        text-align: center !important;         /* Alinhamento central das células */
    }
    .center-left {
        text-align: left !important;           /* Alinhamento à esquerda para as células centrais */
    }
    .center-right {
        text-align: right !important;          /* Alinhamento à direita para as células centrais */
    }
    tr th:first-child, tr td:first-child {
        border-left: none !important;          /* Remove a borda esquerda das primeiras colunas */
    }
    tr th:last-child, tr td:last-child {
        border-right: none !important;         /* Remove a borda direita das últimas colunas */
    }
    img {
        max-width: 100% !important; /* Torna as imagens responsivas */
        height: auto !important;    /* Mantém a proporção das imagens */
    }
    .titulo-azul {
        color: rgba(60, 145, 196, 1.00) !important;
    }
</style>



<!-- Bootstrap -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>

<!-- Scripts Js para thema-2020 Senado-->
<script src="https://code.jquery.com/jquery-2.2.4.js" integrity="sha256-iT6Q9iMJYuQiMWNd9lDyBUStIq/8PuOW33aOqmvFpqI=" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://www.senado.leg.br/inc/essencial-2020/js/essencial.js"></script>
"""

# Função para converter imagens em base64
def convert_image(image):
    with image.open() as image_bytes:
        encoded_image = base64.b64encode(image_bytes.read()).decode("utf-8")
    return {
        "src": f"data:{image.content_type};base64,{encoded_image}",
        "alt": image.alt_text if image.alt_text else ""
    }

# Conversão do documento DOCX para HTML usando mammoth
with open(docx_path, "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file, convert_image=mammoth.images.img_element(convert_image))
    html = result.value
    if not html.strip():
        raise ValueError("O HTML gerado está vazio ou malformado.")


# Criação da estrutura básica do documento HTML
html_template = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documento Convertido</title>
    {pacotes_auxiliares}
</head>
<body>
    {header_senado}
    <div class="container">
        {html}
    </div>
    {footer_senado}
</body>
</html>
"""

# Análise e formatação do HTML usando BeautifulSoup
soup = BeautifulSoup(html_template, "html.parser")

# Salvar o HTML modificado
with open(html_path, "w", encoding="utf-8") as html_file:
    html_file.write(str(soup.prettify()))

print("Conversão concluída. Verifique o arquivo output.html.")