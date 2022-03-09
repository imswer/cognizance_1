import pandas as pd
  
# Create the series
st = pd.Series(['amrita', 'school', 'of', 'engineering' 'chennai' , 'campus'])

st = [st.capitalize() for st in st]
# Print the series
print(st)
s = pd.Series(st)
print(' ')
# Converting into string
t = ' '.join(map(str,s))


print(t)

