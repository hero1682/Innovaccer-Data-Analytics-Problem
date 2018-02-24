import pandas as pd
df = pd.read_csv("input.csv")
df_ln = df.ln.str.split(' ',expand = True)
df_fn = df.fn.str.split(' ',expand = True)
full_name = df_fn[0] + ' ' + df_ln[0]
df_full = df.join(full_name)
list_drop = ['fn', 'ln']
df_full.drop(list_drop, axis=1, inplace=True)
output = df_full.drop_duplicates()
output.columns = ["dob", "gn", "Full name"]
output.index = pd.RangeIndex(len(output.index))
output.to_csv('output.csv')