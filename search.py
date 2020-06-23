def plusonestr(string):
  if(len(string) == 1): return ''
  else: return string[1:]

def match(pattern, string):
  if(len(pattern) == 0 and len(string) == 0):
    return True

  if(len(pattern) == 0 and len(string) != 0):
    return False
    
  if(pattern[0] == '*'):
    if len(pattern) != 1 and len(string) == 0: return False
    elif len(string) == 0: return True

  if(pattern[0] == '?' or pattern[0] == string[0]):
    return match(plusonestr(pattern), plusonestr(string))

  if(pattern[0] == '*'):
    return match(plusonestr(pattern), string) or match(pattern, plusonestr(string))

  return False