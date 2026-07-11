import seaborn as sns 

datasets = sns.get_dataset_names() #return all data sets 

for item in datasets:
    print(item)

choice = input("""Enter dataset name (anagrams,anscombe,attention,brain_networks,car_crashes,diamonds,dots,dowjones,exercise,flights,fmri,geyser,glue,healthexp,iris,mpg,penguins,planets,seaice,taxis,tips,titanic)""")
if choice in datasets:
    data = sns.load_dataset(choice)
    print(data.head(1))
'''
anagrams
anscombe
attention
brain_networks
car_crashes
diamonds
dots
dowjones
exercise
flights
fmri
geyser
glue
healthexp
iris
mpg
penguins
planets
seaice
taxis
tips
titanic
'''