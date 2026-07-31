medida = float(input('Uma distância em metros: '))
km = medida/1000
hm = medida/100
dam = medida/10
dm = medida * 100
cm = medida * 100
mm = medida * 1000

print('A medida de {}m convertida é . \n {:.0f}km \n {:.0f}hm \n {:.0f}dam \n {:.0f}dm \n {:.0f}cm \n {:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))