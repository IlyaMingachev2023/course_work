import json

with open("../operations.json", encoding='utf-8') as f:
    result = json.load(f)


def new_list():
    """создает новый список словарей"""
    new_line = []
    for dict_ in result:
        for k in dict_:
            if not dict_.get('from'):
                continue
            elif dict_['state'] == 'EXECUTED':
                new_dict = {'дата': dict_['date'], 'описание перевода': dict_['description'],
                        'откуда': dict_['from'], 'куда': dict_['to'],
                        'сумма': dict_['operationAmount']['amount'],
                        'валюта': dict_['operationAmount']['currency']['name'],
                        }

            else:
                continue
        new_line.append(new_dict)
    new_line = new_line[:5]
    return new_line

new_line = new_list()


def new_list_2():
    """создает список словарей с нужными значениями"""
    new_list = []
    for i in new_line:
        k = ([i['дата'], i['описание перевода'],
              i['откуда'], '-->', i['куда'],
              i['сумма'], i['валюта']])
        new_list.append(k)
    return new_list

new_list = new_list_2()


def outline():
    """выводит построчно в нужном формате"""
    for n in new_list:
        print('\n', n[0][:10], n[1], '\n', n[2][:14] + '** *****'+ n[2][-4:], n[3], n[4][:5] + '*' * 2, n[4][21:], '\n', n[5], n[6],'\n\n')


new_list = outline()
print(new_list)








