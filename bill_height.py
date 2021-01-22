h_bill = 0.11 * 0.001
n_bills = 1
h_bills = h_bill
days = 1
h_sears = 442
while (h_bills <= h_sears):
    n_bills = n_bills * 2
    days = days + 1
    h_bills = h_bill * n_bills
print(days)