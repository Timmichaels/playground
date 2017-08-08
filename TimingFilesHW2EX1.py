#load the module
import pandas as pd
import numpy as np
#create a DataFrame from a tab-delimited file
df = pd.read_table('/Users/timmichaels/Documents/UConn/BIRC/WedJuly26/Non-Linear/playground/sub_03_timing.txt',skiprows=1, sep='\t')

df['OnsetTime'] = (df[['onset']].min(1)) 


#df['OnsetTime'] = ( df[['stimSound.OnsetTime', 'stimSoundDuration.OnsetTime', 'stimText.OnsetTime']].min(1)- df['TriggerWait.RTTime'] ) / 1000.0

for ttype in df['trial_type'].unique():
	df2 = df[df['trial_type'] == ttype]
	#convert the OnsetTime Series into a DataFrame and Transpose
	times = pd.DataFrame(df2['OnsetTime']).T
	#write tab delimited
	#don't number rows or print headers
	times.to_csv(ttype + '.1D', index=False, header=False, sep='\t')

#for ttype in df['Procedure[Trial]'].unique():
#	for iscatch in df['CatchTrial'].unique():
#		for iscongruent in df['Congruent'].unique():
#			df2 = df[(df['Procedure[Trial]'] == ttype) & (df['Congruent'] == iscongruent) & (df['CatchTrial'] == iscatch)]
#			if df2.shape[0]>0:
#				times = pd.DataFrame(df2['OnsetTime']).T
#				times.to_csv(ttype + '_con-' + str(iscongruent) + '_catch-' + str(iscatch) + '.1D', index=False, header=False, sep='\t')