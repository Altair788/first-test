# СКОЛЬКО Я ЗАРАБОТАЮ В ПРОЦЕНТАХ, если куплю сейчас эту ОФЗ (какая будет доходность?)?
def determine_bond_yield(sum, pricenow, middle_price, kuponza_1ofz, ostat_kol_kuponnih_viplat, nkd, komissiya):
    kd_all = float(ostat_kol_kuponnih_viplat * kuponza_1ofz * sum)
    clear_kd = (kd_all - (kd_all * 0.13))  # 13% тут пишется как 0.13
    pribil_ot_ofz_gryaznaya = (nominal * sum) - (middle_price * sum)  # # теперь высчитываем прибыль от продажи ОФЗ
    # по цене номинала до уплаты налогов
    # теперь высчитываем прибыль от продажи ОФЗ по цене номинала после уплаты налогов
    if pribil_ot_ofz_gryaznaya > 0:
        clear_pribil_ot_ofz = (pribil_ot_ofz_gryaznaya - (pribil_ot_ofz_gryaznaya * 0.13))
    else:
        clear_pribil_ot_ofz = pribil_ot_ofz_gryaznaya
    # теперь высчитываем итоговый чистый доход (купоны + доход от разницы цены покупки и продажи ОФЗ)
    clear_income = clear_kd + clear_pribil_ot_ofz - nkd - komissiya
    # так какая будет доходность, если я сейчас куплю эти ОФЗ?
    doxod = clear_income / (nominal * sum) * 100
    return ('Доходность такой покупки составит', round(doxod, 1), '%')


sum = int(input(''Введите количество офз '))
pricenow = float(input('Введите текущую стоимость ОФЗ за 1 штуку '))
middle_price = float(input('введите среднюю цену покупки '))
kuponza_1ofz = float(input("Введите размер купона за 1 офз "))
ostat_kol_kuponnih_viplat = int(input('Введите количество оставшихся купонных выплат '))
nominal = 1000  # цена номинала, по которому ОФЗ будет погашена в конце срока
nkd = float(input('Какой НКД необходимо будет уплатить прежнему владельцу? '))
komissiya = float(input('какую комиссию необходимо уплатить бирже? '))

print(determine_bond_yield(sum, pricenow, middle_price, kuponza_1ofz, ostat_kol_kuponnih_viplat, nkd, komissiya))
