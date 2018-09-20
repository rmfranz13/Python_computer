import chapter1 as ch1
	
class HalfAdder:
	def __init__(self, a, b, carry=0, Sum=0):
		self.a = a
		self.b = b 
		self.carry = carry 
		self.Sum = Sum 
		return(None)
		
	def update(self):
		and_1 = ch1.And(self.a,self.b)
		and_1.update()
		xor_1 = ch1.Xor(self.a,self.b)
		xor_1.update()
		self.carry = and_1.x 
		self.Sum = xor_1.x 
		return(self.carry,self.Sum)

class FullAdder:
	def __init__(self, a, b, c, carry=0, Sum=0):
		self.a = a 
		self.b = b 
		self.c = c 
		self.carry = carry 
		self.Sum = Sum 
		return(None)
		
	def update(self):
		not_a = ch1.Not(self.a)
		not_a.update()
		not_b = ch1.Not(self.b)
		not_b.update()
		not_c = ch1.Not(self.c)
		not_c.update()
		and_1 = ch1.And3Way(not_a.x,not_b.x,self.c)
		and_1.update()
		and_2 = ch1.And3Way(not_a.x,self.b,not_c.x)
		and_2.update()
		and_3 = ch1.And3Way(not_a.x,self.b,self.c)
		and_3.update()
		and_4 = ch1.And3Way(self.a,not_b.x,not_c.x)
		and_4.update()
		and_5 = ch1.And3Way(self.a,not_b.x,self.c)
		and_5.update()
		and_6 = ch1.And3Way(self.a,self.b,not_c.x)
		and_6.update()
		and_7 = ch1.And3Way(self.a,self.b,self.c)
		and_7.update()
		or_1 = ch1.Or4Way(and_1.x,and_2.x,and_4.x,and_7.x)
		or_1.update()
		or_2 = ch1.Or4Way(and_3.x,and_5.x,and_6.x,and_7.x)
		or_2.update()
		self.Sum = or_1.x 
		self.carry = or_2.x
		return(self.carry,self.Sum)
		
class Add16:
	def __init__(self, a16, b16, sum16=[0 for i in range(16)]):
		self.a16 = a16 
		self.b16 = b16 
		self.sum16 = sum16 
		return(None) 
		
	def update(self):
		adder_1 = FullAdder(self.a16[15],self.b16[15],0)
		adder_1.update()
		adder_2 = FullAdder(self.a16[14],self.b16[14],adder_1.carry)
		adder_2.update()
		adder_3 = FullAdder(self.a16[13],self.b16[13],adder_2.carry)
		adder_3.update()
		adder_4 = FullAdder(self.a16[12],self.b16[12],adder_3.carry)
		adder_4.update()
		adder_5 = FullAdder(self.a16[11],self.b16[11],adder_4.carry)
		adder_5.update()
		adder_6 = FullAdder(self.a16[10],self.b16[10],adder_5.carry)
		adder_6.update()
		adder_7 = FullAdder(self.a16[9],self.b16[9],adder_6.carry)
		adder_7.update()
		adder_8 = FullAdder(self.a16[8],self.b16[8],adder_7.carry)
		adder_8.update()
		adder_9 = FullAdder(self.a16[7],self.b16[7],adder_8.carry)
		adder_9.update()
		adder_10 = FullAdder(self.a16[6],self.b16[6],adder_9.carry)
		adder_10.update()
		adder_11 = FullAdder(self.a16[5],self.b16[5],adder_10.carry)
		adder_11.update()
		adder_12 = FullAdder(self.a16[4],self.b16[4],adder_11.carry)
		adder_12.update()
		adder_13 = FullAdder(self.a16[3],self.b16[3],adder_12.carry)
		adder_13.update()
		adder_14 = FullAdder(self.a16[2],self.b16[2],adder_13.carry)
		adder_14.update()
		adder_15 = FullAdder(self.a16[1],self.b16[1],adder_14.carry)
		adder_15.update()
		adder_16 = FullAdder(self.a16[0],self.b16[0],adder_15.carry)
		adder_16.update()
		self.sum16[15] = adder_1.Sum 
		self.sum16[14] = adder_2.Sum 
		self.sum16[13] = adder_3.Sum 
		self.sum16[12] = adder_4.Sum 
		self.sum16[11] = adder_5.Sum 
		self.sum16[10] = adder_6.Sum 
		self.sum16[9] = adder_7.Sum 
		self.sum16[8] = adder_8.Sum 
		self.sum16[7] = adder_9.Sum 
		self.sum16[6] = adder_10.Sum 
		self.sum16[5] = adder_11.Sum 
		self.sum16[4] = adder_12.Sum 
		self.sum16[3] = adder_13.Sum 
		self.sum16[2] = adder_14.Sum 
		self.sum16[1] = adder_15.Sum 
		self.sum16[0] = adder_16.Sum 
		return(self.sum16)
		
class Inc16:
	def __init__(self, a16, sum16=[0 for i in range(16)]):
		self.a16 = a16
		self.sum16 = sum16 
		self.b16 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
		return(None)
		
	def update(self):
		add_16 = Add16(self.a16,self.b16)
		add_16.update()
		self.sum16 = add_16.sum16 
		return(self.sum16)
		
		
class ALU:
	def __init__(self, a16, b16, zx, nx, zy, ny, f, no, out16 = [0 for i in range(16)]):
		self.a16 = a16 
		self.b16 = b16 
		self.zx = zx 
		self.nx = nx 
		self.zy = zy 
		self.ny = ny 
		self.f = f 
		self.no = no 
		self.zeros = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		return(None)
		
	def update(self): 
		mux16_1 = ch1.Mux16(self.a16,self.zeros,[self.zx for i in range(16)])
		mux16_1.update()
		not16_1 = ch1.Not16(mux16_1.x16)
		not16_1.update()
		mux16_2 = ch1.Mux16(mux16_1.x16,not16_1.x16,[self.nx for i in range(16)])
		mux16_2.update()
		mux16_3 = ch1.Mux16(self.b16,self.zeros,[self.zy for i in range(16)])
		mux16_3.update()
		not16_2 = ch1.Not16(mux16_3.x16)
		not16_2.update()
		mux16_4 = ch1.Mux16(mux16_3.x16,not16_2.x16,[self.ny for i in range(16)])
		mux16_4.update()
		adder_1 = Add16(mux16_2.x16,mux16_4.x16)
		adder_1.update()
		and_1 = ch1.And16(mux16_2.x16,mux16_4.x16)
		and_1.update()
		out_0 = ch1.Mux16(and_1.x16,adder_1.sum16,[self.f for i in range(16)])
		out_0.update()
		out_1 = ch1.Not16(out_0.x16)
		out_1.update()
		out = ch1.Mux16(out_0.x16,out_1.x16,[self.no for i in range(16)])
		out.update()
		self.out16 = out.x16
		return(self.out16)
		