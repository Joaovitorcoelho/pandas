import pandas 
import matplotlib.pyplot as plt

def tabelaDeDados():
    fonte = "https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true"
    dados = pandas.read_csv(fonte)
    return dados

def informaçãoDeIdadeSexo():
    return tabelaDeDados()[["NU_IDADE","TP_SEXO"]]

def valoresUnicosDeIdades():
    return tabelaDeDados()["NU_IDADE"].unique()

def inscritosDeCidadesDiferentes():
    return len(tabelaDeDados()["NO_MUNICIPIO_RESIDENCIA"].unique())

def quantidadeDeInscritosDeCadaIdade():
    return tabelaDeDados()["NU_IDADE"].value_counts()

def graficoPorUF():
    graficoDeColuna = tabelaDeDados()["SG_UF_RESIDENCIA"].hist(bins = 20,figsize = (10,8))
    plt.show()
    plt.close()
    return graficoDeColuna

def graficoDePizzaPorIdade():
    graficoDePizza = tabelaDeDados()["NU_IDADE"].value_counts().plot.pie(figsize=(10,8))
    plt.show()
    plt.close()
    return graficoDePizza

def main():
    print(tabelaDeDados())

    print(informaçãoDeIdadeSexo())

    print(valoresUnicosDeIdades())

    print(inscritosDeCidadesDiferentes())

    print(quantidadeDeInscritosDeCadaIdade())

    print(graficoPorUF())

    print(graficoDePizzaPorIdade())

if __name__ == '__main__':
    main()
