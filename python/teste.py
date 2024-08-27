import scrapy

class SenadoSpider(scrapy.Spider):
    name = "senado"
    start_urls = ["https://www.senado.leg.br/atividade/baseshist/bh.asp#/"]

    def parse(self, response):
        # Preencha o formulário de pesquisa
        yield scrapy.FormRequest.from_response(
            response,
            formdata={"seleciona": "True", "consulta": "Alvim"},
            callback=self.parse_results
        )

    def parse_results(self, response):
        # Extraia as informações das cartas na página de resultados
        for carta in response.css('div[class^="resultado"'):
            carta_info = {
                'identificacao': carta.css('div:contains("IDENTIFICAÇÃO") + div::text').get(),
                'nome': carta.css('div:contains("NOME") + div::text').get(),
                'endereco': carta.css('div:contains("ENDEREÇO") + div::text').get(),
                'localizacao': carta.css('div:contains("LOCALIZAÇÃO") + div::text').get(),
                'dados_pessoais': {
                    'sexo': carta.css('div:contains("SEXO") + div::text').get(),
                    'morador': carta.css('div:contains("MORADOR") + div::text').get(),
                    'instrucao': carta.css('div:contains("INSTRUÇÃO") + div::text').get(),
                    'estado_civil': carta.css('div:contains("ESTADO CIVIL") + div::text').get(),
                    'faixa_etaria': carta.css('div:contains("FAIXA ETÁRIA") + div::text').get(),
                    'faixa_renda': carta.css('div:contains("FAIXA RENDA") + div::text').get(),
                    'atividade': carta.css('div:contains("ATIVIDADE") + div::text').get(),
                },
                'catalogo': carta.css('div:contains("CATÁLOGO") + div::text').get(),
                'sugestao': carta.css('div:contains("SUGESTÃO") + div::text').get(),
            }
            yield carta_info

        # Lidar com a paginação, se houver
        next_page = response.css('a.proxima-pagina::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse_results)
