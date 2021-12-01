def target_shift(jam_kerja,cavity,ct):
	return 3600*jam_kerja*cavity/ct

def totalProd(ok,ng,after,before):
	return ok+ng+after-before

def workTime(ok,ng,af,be,ct,cav):
	hasil = totalProd(ok,ng,af,be)*ct/3600/cav
	hasil = str(hasil)
	mnt = '0' + hasil[1::1]
	mnt = float(mnt)*60
	return hasil[0] + ' Jam, ' + str (int(mnt)) + ' Menit'

ok = 6500
ng = 19
after = 506
before = 365
ct = 12.30
cav = 4

print(workTime(ok,ng,after,before,ct ,cav))
