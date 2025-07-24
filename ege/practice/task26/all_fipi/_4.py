buy_list = []
with open("_4.txt") as f:
    for x in f:
        buy_list.append(int(x))
buy_list  = sorted(buy_list, reverse=True)
exp_half_price = buy_list[0:2500]
exp_full_price = buy_list[2500:10000]
buy_list  = sorted(buy_list)
real_half_price = buy_list[0:2500]
real_full_price = buy_list[2500:10000]
su_exp, su_real = 0, 0
for x in exp_full_price:
    su_exp+=x
for x in exp_half_price:
    su_exp+=x/2
for x in real_full_price:
    su_real+=x
for x in real_half_price:
    su_real+=x/2
print(su_exp, su_real)
