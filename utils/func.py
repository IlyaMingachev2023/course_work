import json

with open("../operations.json", encoding='utf-8') as f:
    result = json.load(f)

result_2 = result[:5]

def sort_list():
    """создает отсортированный список словарей"""
    new_line = []
    for dict_ in result_2:
        for k in dict_:
            if dict_['state'] == 'EXECUTED':
                new_dict = {'дата': dict_['date'], 'описание перевода': dict_['description'],
                        'откуда': dict_.get('from', 'Неизвестно'), 'куда': dict_['to'],
                        'сумма': dict_['operationAmount']['amount'],
                        'валюта': dict_['operationAmount']['currency']['name'],
                        }
            else:
                continue
        new_line.append(new_dict)
    new_line.sort(key=lambda x: x.get('дата'), reverse=True)
    return new_line

new_line = sort_list()


def sort_list_2():
    """создает список словарей с нужными значениями"""
    new_list = []
    for i in new_line:
        k = ([i['дата'], i['описание перевода'],
              i['откуда'], '-->', i['куда'],
              i['сумма'], i['валюта']])
        new_list.append(k)
    return new_list
new_list = sort_list_2()


def sort_list_3():
    """выводит построчно в нужном формате"""
    for n in new_list:
        print('\n', n[0][:10], n[1], '\n', n[2][:17] + '*' * 6, n[3], n[4][:5] + '*' * 2, n[4][21:], '\n', n[5], n[6],'\n')


new_list = sort_list_3()
print(new_list)








