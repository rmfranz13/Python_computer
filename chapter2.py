import chapter1 as ch1

def HalfAdder(a, b):
    carry=(ch1.And(a,b))
    Sum=ch1.Xor(a,b)
    return(carry,Sum)

def FullAdder(a,b,c):
    carry0=ch1.And(ch1.Not(a),
                   ch1.And(b,c))
    carry1=ch1.And(a,
                   ch1.And(ch1.Not(b),c))
    carry2=ch1.And(a,
                   ch1.And(b,ch1.Not(c)))
    carry3=ch1.And(a,
                   ch1.And(b,c))
    sum0=ch1.And(ch1.Not(a),
                 ch1.And(ch1.Not(b),c))
    sum1=ch1.And(ch1.Not(a),
                 ch1.And(b,ch1.Not(c)))
    sum2=ch1.And(a,
                 ch1.And(ch1.Not(b),ch1.Not(c)))
    sum3=ch1.And(a,
                 ch1.And(b,c))
    carry_data = [carry0,carry1,carry2,carry3,0,0,0,0]
    sum_data = [sum0,sum1,sum2,sum3,0,0,0,0]
    carry=ch1.Or8Way(carry_data)
    Sum = ch1.Or8Way(sum_data)
    return(carry,Sum)

def Add16(a, b):
    carry0,sum0=FullAdder(a[15],b[15],0)
    carry1,sum1=FullAdder(a[14],b[14],carry0)
    carry2,sum2=FullAdder(a[13],b[13],carry1)
    carry3,sum3=FullAdder(a[12],b[12],carry2)
    carry4,sum4=FullAdder(a[11],b[11],carry3)
    carry5,sum5=FullAdder(a[10],b[10],carry4)
    carry6,sum6=FullAdder(a[9],b[9],carry5)
    carry7,sum7=FullAdder(a[8],b[8],carry6)
    carry8,sum8=FullAdder(a[7],b[7],carry7)
    carry9,sum9=FullAdder(a[6],b[6],carry8)
    carry10,sum10=FullAdder(a[5],b[5],carry9)
    carry11,sum11=FullAdder(a[4],b[4],carry10)
    carry12,sum12=FullAdder(a[3],b[3],carry11)
    carry13,sum13=FullAdder(a[2],b[2],carry12)
    carry14,sum14=FullAdder(a[1],b[1],carry13)
    carry15,sum15=FullAdder(a[0],b[0],carry14)
    Sum=[sum15,sum14,sum13,sum12,sum11,sum10,sum9,sum8,sum7,sum6,sum5,
         sum4,sum3,sum2,sum1,sum0]
    return(Sum)

def Inc16(a):
    b=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
    Sum=Add16(a, b)
    return(Sum)

def ALU(a, b, zx,nx,zy,ny,f,no):
    zeroes=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    a1=ch1.Mux16(a,zeroes,zx)
    a2=ch1.Not16(a1)
    a3=ch1.Mux16(a1,a2,nx)
    b1=ch1.Mux16(b,zeroes,zy)
    b2=ch1.Not16(b1)
    b3=ch1.Mux16(b1,b2,ny)
    a5=Add16(a3,b3)
    b5=ch1.And16(a3,b3)
    out0=ch1.Mux16(b5,a5,f)
    out1=ch1.Not16(out0)
    out=ch1.Mux16(out0,out1,no)
    return(out)
