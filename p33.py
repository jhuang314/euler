#problem 33
fracs = []
for i in range(10,100):
    if i %11==0 or i%10==0:
        continue
    for j in range(i+1,100):
        frac = float(i)/j
        a = list(str(i))
        b = list(str(j))
        if j%11==0 or i%10==0:
            continue
        for c in range(0,2):
            for d in range(0,2):
                if int(b[d])!=0 and round(float(int(a[c]))/int(b[d]),5)==round(frac,5):
                    if frac not in fracs:
                        fracs.append(frac)
                        print "f="+str(i)+"/"+str(j)+"="+a[c]+"/"+b[d]
fracs.sort()
for f in fracs:
    print f
