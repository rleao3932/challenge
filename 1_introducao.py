import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet
from datetime import timedelta
import base64
import numpy as np


def background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def main():
    main_bg = "Base de Dados\sample_3.png"

    # background(main_bg)
    
    st.title('FIAP PÓS TECH - DATA ANALYTICS')
    
    tab1, tab2= st.tabs(['Introdução', 'Objetivo'])

    with tab1:
        st.subheader(':gray[Conhecendo o Mercado do Petróleo]', divider='red')

        st.markdown('''
                    O petróleo, um recurso natural de extrema importância para a sociedade moderna, possui uma história rica e complexa que se estende por milênios. \n

                    Há milhões de anos, restos de pequenos seres marinhos e vegetais ficaram soterrados no fundo dos oceanos e, com o tempo, passaram por transformações químicas e físicas que deram origem ao petróleo. Essa substância, uma complexa mistura de hidrocarbonetos, permaneceu oculta no subsolo até que a humanidade começasse a descobri-la e explorá-la. \n

                    Desde as civilizações antigas, como os sumérios e babilônios, já se conheciam algumas aplicações do petróleo, ainda que de forma rudimentar. Ele era usado em impermeabilizações, tratamentos de feridas e até em rituais religiosos. Mas foi no século XIX, em meio à efervescência da Revolução Industrial, que o petróleo começou a ganhar destaque.\n

                    Um evento marcante dessa época foi o trabalho de Edwin Drake, que em 1859 perfurou o primeiro poço de petróleo na Pensilvânia, nos Estados Unidos. Esse feito é lembrado como o ponto de partida da indústria petrolífera moderna. A partir daí, o mundo mudou de forma irreversível.\n

                    O século XX consolidou o papel do petróleo como um dos recursos mais valiosos do planeta. Com a invenção do automóvel e a expansão da indústria automobilística, a demanda por gasolina disparou. Ele também passou a ser essencial em diversos setores, desde a produção de plásticos até a geração de energia.\n

                    No entanto, o papel do petróleo no cenário global está longe de ser simples. Seu impacto vai além das questões ambientais, influenciando também a geopolítica, a economia e a sociedade. Compreender o mercado de petróleo exige uma análise profunda de sua cadeia produtiva, desde a exploração e extração até a distribuição e comercialização. Estudar como a oferta e a demanda, os avanços tecnológicos e as oscilações políticas moldam essa indústria pode revelar muito sobre o futuro da energia e da economia mundial. O petróleo, mais do que um recurso, é um motor de mudanças e um tema crucial para quem deseja entender os rumos do planeta.
    	            ''')

        st.subheader(':gray[Petróleo Brent]', divider='red')

        st.markdown('''
                    O petróleo Brent foi batizado assim porque era extraído de uma base da Shell chamada Brent. Atualmente, a palavra Brent designa todo o petróleo extraído no Mar do Norte e comercializado na Bolsa de Londres. \n

                    A exploração de petróleo  é realizada em águas profundas e ultra profundas  sendo  uma atividade complexa que enfrenta diversos desafios técnicos, ambientais e operacionais. A perfuração de poços, o vazamento de óleo e a liberação de produtos químicos podem causar danos significativos aos ecossistemas marinhos e à vida selvagem. As operações em águas profundas são caras e complexas, e exigem um planejamento cuidadoso e uma gestão eficiente dos recursos. Além disso, as empresas enfrentam desafios logísticos, como o transporte de equipamentos e suprimentos para as plataformas offshore e a manutenção das operações em condições remotas e isoladas. Apesar dos desafios, a exploração de petróleo em águas profundas oferece oportunidades significativas para as empresas petrolíferas. As reservas de petróleo nessas áreas podem ser vastas e significativas, e a produção de petróleo em águas profundas pode desempenhar um papel importante no fornecimento de energia global. \n
                    ''')
                    
        st.subheader(':gray[Geopolítica do Petróleo]', divider='red')

        st.markdown('''
                    A importância do petróleo reside no fato de a humanidade ser, em sua maior parte, dependente do uso de seus derivados, principalmente como fonte de energia. A Agência Internacional de Energia estima que cerca de 60% \\da produção energética mundial advenha desse recurso. Assim, considerando que o nível de consumo de um país está diretamente relacionado ao seu poderio econômico, podemos dizer que quanto mais desenvolvido for um Estado, mais dependente do petróleo ele tornar-se-á. Podemos dizer que, de modo geral, os principais atores na Geopolítica do Petróleo são aqueles países que possuem amplas reservas desse recurso e também aqueles que o consomem em grande quantidade. Assim, os membros da OPEP (Organização dos Países Exportadores de Petróleo) fazem parte dessa dinâmica, além de outras nações como os Estados Unidos e China, que estão entre os maiores consumidores da atualidade. O Petróleo, dessa forma, continua sendo um dos protagonistas nas disputas geopolíticas internacionais, mesmo com as recentes adoções de fontes de energias alternativas, outro campo que o Brasil vem ganhando cada vez maior importância. \n
                    ''')
        
        st.subheader(':gray[Crise econômica]', divider='red')

        st.markdown('''
                    A economia global sofreu um abalo em 2022. No início do ano, as instituições financeiras já projetavam um crescimento mais tímido como parte das consequências da pandemia que afetou as cadeias globais de comércio. \n

                    As principais crises que grande parte dos países enfrentam, principalmente os ocidentais, surgiram em decorrência da guerra, uma vez que o conflito afetou os preços dos combustíveis, de energia e, consequentemente, gerou um efeito inflacionário global. No entanto, a guerra da Ucrânia, que começou em 24 de fevereiro, aprofundou problemas de demanda, gerou mais desafios econômicos para o mundo e trouxe urgência para debates que seguiam um curso gradativo entre as lideranças e nações. \n

                    Em março de 2022, os preços do petróleo atingiram o nível mais alto desde 2008 por conta dos primeiros desdobramentos da guerra e negociações entre Estados Unidos e Irã. A volatilidade que a guerra trouxe à commodity é um dos principais fatores que explicam, por exemplo, o aumento dos preços dos combustíveis no Brasil e no mundo. \n
                    Assim que a guerra foi declarada o petróleo saltou muito, isso alterou completamente os preços. Com o aumento nos preços dos combustíveis, uma das categorias mais afetadas foram os alimentos. A guerra na Ucrânia também exerceu grande influência, uma vez que o país eslavo tem papel importante nas exportações de grãos para os países Ocidentais. \n

                    Logo em março, os preços atingiram recorde no mundo. O Índice de Preços de Alimentos da Organização das Nações Unidas para Agricultura e Alimentação (FAO) alcançou média de 159,3 pontos naquele mês, alta de 17,9 pontos (12,6%) ante fevereiro. O maior nível já alcançado desde o início da avaliação, em 1990. \n

                    A Rússia é a grande fornecedora de petróleo. O país era a grande impulsionadora de todo o parque industrial europeu com seu gás natural. As sanções anunciadas pelos países ocidentais acentuaram a crise, uma vez que a Rússia retalhou ao interromper parte do fornecimento para os europeus. Após a paralisação da venda de gás natural russo aos países do continente, muitas nações foram obrigadas a aumentar o uso de combustíveis fósseis para garantir energia para a população. Com isso, os preços da energia dispararam. O Reino Unido, por exemplo, um dos países que mais sofreram com o aumento dos custos de energia, se deparou com o dilema da necessidade de preservação ambiental ao mesmo tempo em que era preciso fornecer energia para a população. Contudo, não existiam muitas escolhas para o curto prazo. Com isso, o país aprovou sua primeira nova mina de carvão profundo em décadas para produzir o combustível altamente poluente para uso na siderurgia. A decisão atraiu críticas de oponentes que dizem que isso prejudicará as metas climáticas. As emissões de gases de efeito estufa provenientes da queima de carvão –como nas usinas de aço e de energia– são o maior fator de contribuição para as mudanças climáticas, e a independência dos países do carvão é considerada vital para atingir as metas climáticas globais. \n

                    A Organização para a Cooperação e Desenvolvimento Econômico (OCDE), classificou esta como a pior crise energética desde os anos 1970 e que, a partir dela, se desencadeará uma forte desaceleração, com a Europa sendo a mais afetada.
                    ''')


    with tab2:
        st.subheader('Dashboard interativo com Storytelling e Machine Learning, utilizando Streamlit e Prophet.', divider='red')
        st.markdown('''
                    O propósito deste desafio é criar um dashboard interativo que combine narrativa visual com um modelo de machine learning para prever os preços diários do petróleo. O objetivo é desenvolver uma ferramenta que seja tanto informativa quanto envolvente, oferecendo informações valiosas sobre as flutuações do preço do petróleo, influenciadas por fatores como questões geopolíticas, crises econômicas, a demanda global por energia e inovações tecnológicas.
                    ''')
main()  