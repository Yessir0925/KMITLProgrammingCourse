usrinp = input(" - ")
usrinp = float(f"{int(usrinp):f}")
total = float(0)
taxxed = int(0)
taxxedamount = usrinp
if 3000000 <= usrinp <= 5000000:
    taxxed = 30
    taxxedamount = taxxedamount - 3000000
    total = total + (taxxedamount * (taxxed/100))
if 1000000 < usrinp <= 2000000:
    taxxed = 25
    taxxedamount = taxxedamount - 1000000
    total = total + (taxxedamount * (taxxed/100))
if 850000 < usrinp <= 1000000:
    taxxed = 20
    taxxedamount = taxxedamount - 250000
    total = total + (taxxedamount * (taxxed/100))
if 550000 < usrinp <= 850000:
    taxxed = 15
    taxxedamount = taxxedamount - 30000
    total = total + (taxxedamount * (taxxed/100))
if 300000 < usrinp <= 550000:
    taxxed = 10
    taxxedamount = taxxedamount - 250000
    total = total + (taxxedamount * (taxxed/100))
if 150000 < usrinp <= 300000:
    taxxed = 5
    taxxedamount = taxxedamount - 250000
    total = total + (taxxedamount * (taxxed/100))
if usrinp <= 150000:
    taxxed = 0

print(total)
taxxedperc = (total/usrinp) * 100   
print(taxxedperc)

#5M,2M,1M,750,500,250,150