# СКОЛЬКО Я ЗАРАБОТАЮ В ПРОЦЕНТАХ, если куплю сейчас эту ОФЗ (какая будет доходность?)?

sum = int(input('Введите количество офз '))
pricenow = float(input('Введите текущую стоимость ОФЗ за 1 штуку '))
middle_price = float(input('введите среднюю цену покупки '))
kuponza_1ofz = float(input("Введите размер купона за 1 офз "))
ostat_kol_kuponnih_viplat = int(input('Введите количество оставшихся купонных выплат '))

# теперь высчитываем общую сумму будущих купонов
kd_all = float(ostat_kol_kuponnih_viplat * kuponza_1ofz * sum)
print('общая сумма будущего кд до вычета налогов =', kd_all)
clear_kd = (kd_all - (kd_all * 0.13))   # 13% тут пишется как 0.13
print('общая сумма будущего кд после вычета налогов =', clear_kd)

# теперь высчитываем прибыль от продажи ОФЗ по цене номинала до уплаты налогов
nominal = 1000             # цена номинала, по которому ОФЗ будет погашена в конце срока
pribil_ot_ofz_gryaznaya = (nominal * sum) - (middle_price * sum)
print('Прибыль от продажи ОФЗ до уплаты налогов = ', pribil_ot_ofz_gryaznaya)
# теперь высчитываем прибыль от продажи ОФЗ по цене номинала после уплаты налогов
if pribil_ot_ofz_gryaznaya > 0:
    clear_pribil_ot_ofz = (pribil_ot_ofz_gryaznaya - (pribil_ot_ofz_gryaznaya * 0.13))
    print('Прибыль от продажи ОФЗ после уплаты налогов = ', clear_pribil_ot_ofz)
else:
    clear_pribil_ot_ofz = pribil_ot_ofz_gryaznaya
    print('Прибыль от продажи ОФЗ после уплаты налогов = ', pribil_ot_ofz_gryaznaya)
# теперь высчитываем итоговый чистый доход (купоны + доход от разницы цены покупки и продажи ОФЗ)
nkd = float(input('Какой НКД необходимо будет уплатить прежнему владельцу? '))
komissiya = float(input('какую комиссию необходимо уплатить бирже? '))
clear_income = clear_kd + clear_pribil_ot_ofz - nkd - komissiya
print('Чистая прибыль составляет', round(clear_income, 2), 'рублей')

# так какая будет доходность, если я сейчас куплю эти ОФЗ?
doxod = clear_income / (nominal * sum) * 100
print('Доходность такой покупки составит', round(doxod, 1), '%')
