def extract_values(values):
    values=values.strip().split()
    return (int(values[0]),int(values[1]))

'''strip() returns a copy of the string in which all chars 
have been stripped from the beginning and the end of the string 
(default whitespace characters).

str = "0000000this is string example....wow!!!0000000";
print str.strip( '0' )
this is string example....wow!!!'''

def calc_ratios(values):
    if values[1]==0:
        return None
    return float(values[0])/values[1]
