def missing_char(str, n):
  newStr = ""
  newStr = str[0:n] + str[n+1 : len(str)]
  return newStr
