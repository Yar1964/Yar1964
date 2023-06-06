money = 99900
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit_ТКБ = money*5.6/100
deposit_СКБ = money*5.9/100
deposit_ВТБ = money*4.28/100
deposit_СБЕР = money*4.0/100
deposit = [round(deposit_ТКБ), round(deposit_СКБ), round(deposit_ВТБ), round(deposit_СБЕР)]
print("Депозит = ", deposit)
max_deposit = max(deposit)
print("Максимальная сумма, которую вы можете заработать -", max_deposit)