"""
The goal of these scripts are to implement a computer based on the book
"The Elements of Computer Systems"... Thus creating a virtual computer from
python built-ins
"""
import fundamentals as fd

def Not(a):
    x=fd.nand(a, a)
    return(x)

def And(a, b):
    x=fd.nand(a, b)
    x=Not(x)
    return(x)

def Or(a, b):
    x1=Not(a)
    x2=Not(b)
    x =fd.nand(x1,x2)
    return(x)

def Xor(a, b):
    x1=a
    x2=Not(b)
    x3=b
    x4=Not(a)
    y1=And(x1,x2)
    y2=And(x3,x4)
    x=Or(y1,y2)
    return(x)

def Mux(a, b, sel):
    x1=And(a,And(Not(b),Not(sel)))
    x2=And(a,And(b,Not(sel)))
    x3=And(Not(a),And(b,sel))
    x4=And(a,And(b,sel))
    x=Or(Or(x1,x2),Or(x3,x4))
    return(x)

def DMux(x, sel):
    a=And(x,Not(sel))
    b=And(x,sel)
    return(a,b)

def Not16(a):
    x0=Not(a[0])
    x1=Not(a[1])
    x2=Not(a[2])
    x3=Not(a[3])
    x4=Not(a[4])
    x5=Not(a[5])
    x6=Not(a[6])
    x7=Not(a[7])
    x8=Not(a[8])
    x9=Not(a[9])
    x10=Not(a[10])
    x11=Not(a[11])
    x12=Not(a[12])
    x13=Not(a[13])
    x14=Not(a[14])
    x15=Not(a[15])
    x=[x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15]
    return(x)

def And16(a, b):
    x0=And(a[0],b[0])
    x1=And(a[1],b[1])
    x2=And(a[2],b[2])
    x3=And(a[3],b[3])
    x4=And(a[4],b[4])
    x5=And(a[5],b[5])
    x6=And(a[6],b[6])
    x7=And(a[7],b[7])
    x8=And(a[8],b[8])
    x9=And(a[9],b[9])
    x10=And(a[10],b[10])
    x11=And(a[11],b[11])
    x12=And(a[12],b[12])
    x13=And(a[13],b[13])
    x14=And(a[14],b[14])
    x15=And(a[15],b[15])
    x=[x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15]
    return(x)

def Or16(a, b):
    x0=Or(a[0],b[0])
    x1=Or(a[1],b[1])
    x2=Or(a[2],b[2])
    x3=Or(a[3],b[3])
    x4=Or(a[4],b[4])
    x5=Or(a[5],b[5])
    x6=Or(a[6],b[6])
    x7=Or(a[7],b[7])
    x8=Or(a[8],b[8])
    x9=Or(a[9],b[9])
    x10=Or(a[10],b[10])
    x11=Or(a[11],b[11])
    x12=Or(a[12],b[12])
    x13=Or(a[13],b[13])
    x14=Or(a[14],b[14])
    x15=Or(a[15],b[15])
    x=[x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15]
    return(x)

def Mux16(a, b, sel):
    x0=Mux(a[0],b[0],sel)
    x1=Mux(a[1],b[1],sel)
    x2=Mux(a[2],b[2],sel)
    x3=Mux(a[3],b[3],sel)
    x4=Mux(a[4],b[4],sel)
    x5=Mux(a[5],b[5],sel)
    x6=Mux(a[6],b[6],sel)
    x7=Mux(a[7],b[7],sel)
    x8=Mux(a[8],b[8],sel)
    x9=Mux(a[9],b[9],sel)
    x10=Mux(a[10],b[10],sel)
    x11=Mux(a[11],b[11],sel)
    x12=Mux(a[12],b[12],sel)
    x13=Mux(a[13],b[13],sel)
    x14=Mux(a[14],b[14],sel)
    x15=Mux(a[15],b[15],sel)
    x=[x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15]
    return(x)

def Or8Way(a):
    x = Or(Or(Or(a[0],a[1]),
              Or(a[2],a[3])),
           Or(Or(a[4],a[5]),
              Or(a[6],a[7])))
    return(x)

def Mux4Way16(a,b,c,d,sel):
    x1=Mux16(a,b,sel[1])
    x2=Mux16(c,d,sel[1])
    x=Mux16(x1,x2,sel[0])
    return(x)

def Mux8Way16(a,b,c,d,e,f,g,h,sel):
    x1=Mux16(a,b,sel[2])
    x2=Mux16(c,d,sel[2])
    x3=Mux16(e,f,sel[2])
    x4=Mux16(g,h,sel[2])
    y1=Mux16(x1,x2,sel[1])
    y2=Mux16(x3,x4,sel[1])
    x=Mux16(y1,y2,sel[0])
    return(x)

def DMux4Way(x,sel):
    a1,b1=DMux(x,sel[0])
    a,b=DMux(a1, sel[1])
    c,d=DMux(b1, sel[1])
    return(a,b,c,d)

def DMux8Way(x,sel):
    a1,b1=DMux(x,sel[0])
    a2,b2=DMux(a1,sel[1])
    c2,d2=DMux(b1,sel[1])
    a,b=DMux(a2,sel[2])
    c,d=DMux(b2,sel[2])
    e,f=DMux(c2,sel[2])
    g,h=DMux(d2,sel[2])
    return(a,b,c,d,e,f,g,h)
    
