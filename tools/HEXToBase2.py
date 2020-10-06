
def hexToBase2_B(s):
	result = ""

	DIC = { "0":"0000",
			"1":"0001",
			"2":"0010",
			"3":"0011",
			"4":"0100",
			"5":"0101",
			"6":"0110",
			"7":"0111",
			"8":"1000",
			"9":"1001",
			"A":"1010",
			"B":"1011",
			"C":"1100",
			"D":"1101",
			"E":"1110",
			"F":"1111"}

	
	for i in range(0, len(s), 1):
		result = result + DIC[s[i]]

	return result


print(hexToBase2_B("0"))
print(hexToBase2_B("A12"))
print(hexToBase2_B("F"))
'''
  S = passed string parameter only containing hex characters
  HEX = ["0","1","2", . . .,"E",F"]
  BIN = ["0000","0001","0010",....,"1110","1111"]	
  RESULT = ""
  
  Loop N from S.length - 1 to 0:
  	Loop I from 0 to len(HEX) - 1:
  		if HEX[I] == S[N]
  			RESULT = BIN[I] + RESULT
		end if
	end loop
  end loop
  return RESULT