from datetime import datetime, timedelta
import pandas as pd


def calcula_pascoa(y: int) -> list:
    '''
        Recebe um ano e retorna a data da pascoa. A partir da pascoa é calculado
        o carnaval, corpus christi e sexta-feira da paixão
        param: y: ano
        return: data_pascoa, data_carnaval, data_corpus_christi
        carnaval -> 47 dias antes da páscoa
        paixao de cristo -> 2 dias antes da páscoa
        corpus christi -> 60 dias apos a pascoa

    '''
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25

    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    n = ((h + l - 7) * (m + 114)) // 31
    o = ((h + l - 7 * m + 114) % 31) + 1

    pascoa = datetime(y, 4, o)
    paixao_cristo = pascoa - timedelta(days=2)
    corpus_christi = pascoa + timedelta(days=60)
    carnaval = pascoa - timedelta(days=47)

    # retorna feriados nacionais fixos e moveis
    # caso haja intervencao do governo o calculo pode apresentar datas
    # divergentes
    feriados_nacionais = [
        {'feriado': 'ano_novo', 'data': datetime(y, 1, 1).strftime('%Y-%m-%d')},
        {'feriado': 'carnaval', 'data': carnaval.strftime('%Y-%m-%d')},
        {'feriado': 'tiradentes', 'data': datetime(y, 4, 21).strftime('%Y-%m-%d')},
        {'feriado': 'paixao_de_cristo', 'data': paixao_cristo.strftime('%Y-%m-%d')},
        {'feriado': 'pascoa', 'data': pascoa.strftime('%Y-%m-%d')},
        {'feriado': 'dia_do_trabalho', 'data': datetime(y, 5, 1).strftime('%Y-%m-%d')},
        {'feriado': 'corpus_christi', 'data': corpus_christi.strftime('%Y-%m-%d')},
        {'feriado': 'independencia', 'data': datetime(y, 9, 7).strftime('%Y-%m-%d')},
        {'feriado': 'nossa_senhora_aparecida', 'data': datetime(y, 10, 12).strftime('%Y-%m-%d')},
        {'feriado': 'finados', 'data': datetime(y, 11, 2).strftime('%Y-%m-%d')},
        {'feriado': 'proclamacao_da_republica', 'data': datetime(y, 11, 15).strftime('%Y-%m-%d')},
        {'feriado': 'natal', 'data': datetime(y, 12, 25).strftime('%Y-%m-%d')}
    ]
    return feriados_nacionais


if __name__ == '__main__':
    datas = calcula_pascoa(2023)
    df = pd.DataFrame(datas)
    print(df)
