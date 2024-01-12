import json



with open("operations.json", encoding='utf-8') as f:
    result = json.load(f)



result_2 = result[:5]

new_line = []
for dict_ in result_2:
    for k in dict_:
        if dict_['state'] == 'EXECUTED':
            user = {'дата':dict_['date'], 'описание перевода': dict_['description'],
                    'откуда': dict_.get('from', 'Неизвестно'),  'куда': dict_['to'],
                    'сумма': dict_['operationAmount']['amount'], 'валюта': dict_['operationAmount']['currency']['name'],
            }
        else:
            continue
    new_line.append(user)
new_line.sort(key=lambda x: x.get('дата'), reverse=True)





new_list = []

for i in new_line:
        k = ([i['дата'], i['описание перевода'],
        i['откуда'], '-->', i['куда'],
        i['сумма'], i['валюта']])
        new_list.append(k)





for n in new_list:
    print('\n',n[0] [:10], n[1],'\n',n[2][:17] + '*' * 6, n[3], n[4][:5] + '*' * 2, n[4][21:],'\n', n[5], n[6],'\n\n')

