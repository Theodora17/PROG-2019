secs_str = input("Input seconds: ") # do not change this line

secs_int = int(secs_str)

seconds = secs_int % (24 * 3600)
hours = secs_int // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print(hours,":",minutes,":",seconds) # do not change this line