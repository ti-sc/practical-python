# mortgage.py

principal = 500000.0
rate = 0.05


payment_regular = 2684.11
payment_extra = 1000
payment = payment_regular
total_paid = 0.0

month = 0
month_extrapay_start = 61
month_extrapay_end = 108


while principal > 0:
    if ((month >= month_extrapay_start)&(month <= month_extrapay_end)):
        payment = payment_regular + payment_extra
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    month = month +1
    payment = payment_regular



print('Total paid', round(total_paid,2), 'month it took:', month)
