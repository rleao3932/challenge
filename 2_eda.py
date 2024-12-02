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

    st.subheader(':red[Exploração e Insights]')

    tab1, tab2 = st.tabs(['Prophet', 'Power BI'])

    with tab1:
        st.subheader(':gray[Modelo de Machine Learning para Previsão Diária dos Preços do Pretróleo Brent]', divider='red')

        st.markdown('''
                    O Prophet é uma ferramenta avançada de modelagem de séries temporais desenvolvida pelo Facebook, projetada para prever dados com padrões sazonais e tendências que podem ser complexos ou não-lineares. Ele é particularmente eficaz em lidar com dados que apresentam variações sazonais e feriados, sendo amplamente utilizado para previsões em uma ampla gama de áreas, como finanças, vendas, ou até previsão de demanda.\n

                    Para entender como o Prophet funciona, podemos usar a analogia de prever o tempo. Imagine que você quer prever a previsão do tempo para os próximos dias, com base nos padrões históricos observados (como clima mais quente no verão ou mais frio no inverno). O Prophet faz algo semelhante, analisando os dados passados para identificar tendências e sazonalidades, e em seguida, utiliza esse conhecimento para fazer previsões futuras. Ele leva em consideração não só os dados históricos, mas também a possibilidade de eventos futuros, como feriados ou outros fatores externos, que podem alterar o comportamento das séries temporais.\n

                    Ao contrário de modelos tradicionais de séries temporais, que podem exigir ajustes complexos e especificação detalhada de tendências e sazonalidades, o Prophet é uma ferramenta automática, fácil de usar e que requer pouca intervenção. Ele utiliza uma abordagem baseada em decomposição, que separa os componentes da série temporal em tendência, sazonalidade e efeitos de feriados. A partir disso, é possível ajustar essas componentes para gerar previsões precisas e robustas, mesmo com dados ruidosos ou com lacunas.\n

                    Por essa razão, o Prophet é altamente eficaz em tarefas onde as séries temporais exibem variações sazonais ou outros efeitos recorrentes, como vendas sazonais, tráfego de sites, e demandas de produtos. Ele é capaz de lidar com datas ausentes, mudanças abruptas na tendência, e adaptar-se de maneira flexível às peculiaridades de diferentes tipos de dados temporais, tornando-se uma ferramenta poderosa para analistas e cientistas de dados que buscam previsões rápidas e precisas. \n
                    ''')
    

    with tab2:
        st.subheader(':gray[Eventos e Insights Analisados com Power BI]', divider='red')

        st.markdown('''
                    O mercado global de petróleo é profundamente influenciado por uma série de fatores interligados, como conflitos geopolíticos, variações na oferta e demanda, oscilações no valor do dólar e decisões estratégicas dos grandes produtores. Esses elementos tornam o preço do petróleo Brent altamente volátil, refletindo tanto mudanças econômicas quanto políticas. Conflitos em regiões produtoras, avanços tecnológicos na extração de combustíveis fósseis e choques econômicos globais desempenham um papel crucial na determinação dos preços. Analisando os últimos anos, é possível destacar períodos específicos em que essas forças resultaram em grandes oscilações no valor do Brent. \n

                    A análise dos dados do preço do petróleo brent, foi composta a partir dos dados de 1987 ate os dias atuais (2024). Para tanto foram utilizados os dados do IPEA, conforme gráfico abaixo: \n
                    ''')
        
        st.image("assets/img/preco_brent_anos.png", caption='Gráfico compondo os preços do petróleo Brent ao longo dos anos')

        st.subheader(':red[Análise dos eventos e seus impactos]')

        st.markdown('''
                    :one: **Incertezas no Oriente Médio** \n
                    Em 2007, os preços do petróleo Brent estavam em alta devido a incertezas sobre a oferta, provocadas por conflitos e tensões no Oriente Médio, uma região crucial para a produção de petróleo mundial. A instabilidade política e a ameaça de interrupções no fornecimento impulsionaram a especulação nos mercados e elevaram os preços. Esse cenário refletia a dependência global do petróleo e a vulnerabilidade do mercado às questões geopolíticas. \n

                    :two: **Crise Financeira Global** \n
                    O ano de 2008 marcou uma reviravolta com a crise financeira global, que resultou em uma queda abrupta dos preços do petróleo. Antes da crise, o Brent alcançou níveis recordes devido à demanda robusta e ao crescimento econômico global. No entanto, com a recessão desencadeada pela crise, a atividade econômica desacelerou rapidamente, reduzindo a demanda por petróleo. Os preços caíram de forma drástica, refletindo não apenas o excesso de oferta, mas também as expectativas pessimistas quanto à recuperação econômica. \n
                    ''')
        
        st.image("assets/img/queda_brent_2008.png", caption='Gráfico demonstrando a queda dos preços do petróleo Brent em 2008')

        st.markdown('''
                    :three: **Alta Oferta e Baixa Demanda** \n
                    Entre 2011 e 2014, os preços do Brent mantiveram relativa estabilidade, em torno de US$ 100 por barril, graças a um equilíbrio entre oferta e demanda. Contudo, em 2014, o mercado entrou em colapso com uma queda acentuada nos preços, causada por um excesso de oferta, em grande parte devido à expansão da produção de petróleo de xisto nos Estados Unidos, combinada com uma demanda mais fraca por conta da estagnação econômica global. Essa estagnação resultava de um crescimento mais lento em economias emergentes, como a China, e de políticas econômicas conservadoras nos países desenvolvidos. \n

                    :four: **Impactos da Pandemia do COVID-19** \n  
                    A pandemia global de COVID-19, em 2020, trouxe uma das quedas mais dramáticas da história dos preços do petróleo Brent. O confinamento mundial, o fechamento de fronteiras e a redução significativa do transporte e da atividade industrial resultaram em uma queda abrupta da demanda. Em abril, os preços chegaram a níveis negativos nos contratos futuros de petróleo nos EUA, refletindo a falta de armazenamento e o desequilíbrio extremo entre oferta e demanda. \n

                    :five: **Conflito Rússia-Ucrânia e Altas Históricas** \n
                    Em 2022, o conflito entre Rússia e Ucrânia reacendeu a volatilidade do mercado de petróleo. As sanções econômicas impostas à Rússia, um dos maiores exportadores globais de petróleo, e o anúncio dos Estados Unidos de interromper as importações de petróleo russo geraram uma forte pressão nos preços do Brent, que dispararam. A incerteza sobre o fornecimento global e a reorganização das cadeias de suprimento contribuíram para o aumento significativo dos preços, intensificando o impacto nos mercados globais de energia. \n
                    ''')
        
        st.image("assets/img/queda_e_aumento_2020_2022.png", caption='Gráfico representando a queda ocasionada pela COVID e aumento ocasionado pelo conflito entre Rússia e Ucrânia')


        st.subheader(':red[Importância da Análise de Eventos]')

        st.markdown('''
                    Reconhecer e compreender esses eventos é fundamental para antecipar flutuações nos preços do petróleo. Investidores, autoridades governamentais e corporações do setor energético baseiam-se nessas avaliações para tomar decisões estratégicas, mitigar riscos e planejar o futuro. O acompanhamento constante e a análise minuciosa dos eventos e seus efeitos possibilitam uma abordagem antecipada diante das mudanças no mercado, promovendo a estabilidade econômica e assegurando a continuidade do fornecimento energético. \n

                    Olhando para esses anos marcantes, é possível identificar padrões e fatores que frequentemente influenciam os preços do petróleo Brent. Tensões políticas entre países produtores continuam sendo um dos principais elementos de risco. Conflitos armados, sanções econômicas e instabilidades regionais podem interromper a oferta e criar volatilidade nos preços. Além disso, a saúde da economia global desempenha um papel crucial: períodos de crescimento econômico aquecido tendem a aumentar a demanda por petróleo, enquanto recessões, como a de 2008 e a crise da COVID-19 em 2020, resultam em quedas significativas. \n

                    Outro ponto em comum é o impacto das decisões estratégicas dos grandes produtores, como a Organização dos Países Exportadores de Petróleo (OPEP) e a expansão da produção em países fora do cartel, como os Estados Unidos, que, em 2014, inundaram o mercado com petróleo de xisto. A interação entre oferta e demanda, muitas vezes combinada com avanços tecnológicos na extração e armazenamento, pode causar tanto estabilidade quanto desequilíbrios severos. Além disso, as oscilações cambiais, especialmente no valor do dólar, moeda na qual o petróleo é cotado, afetam diretamente os preços globais. \n

                    Esses fatores sublinham a importância de monitorar atentamente a geopolítica, as condições econômicas e os movimentos estratégicos dos grandes players do setor. A história mostra que mesmo mudanças localizadas em um desses elementos podem desencadear impactos globais, ressaltando a natureza interconectada do mercado de petróleo. \n
                             
                    O futuro do petróleo é incerto. A transição para uma economia de baixo carbono é um processo em curso, e as fontes de energia renovável estão ganhando cada vez mais espaço. No entanto, o petróleo ainda desempenha um papel fundamental na matriz energética mundial e sua importância deve diminuir gradualmente nas próximas décadas.
                    ''')
        
main()  