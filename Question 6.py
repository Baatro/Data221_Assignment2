#note to self -- DO NOT LEAVE ALL UR ASSIGNMENTS TO DO WITHIN 2 DAYS OF THE DEADLINE AGAIN.
import pandas as pd

crimes_df = pd.read_csv('crime.csv')

# Create a new colmun "risk" based on ViolentCrimesPerPop
def assign_risk_level(violent_crimes_per_pop):
    if  violent_crimes_per_pop >= 0.5:
        return 'HighCrime'
    else:
        return "LowCrime"

crimes_df['risk'] = crimes_df['ViolentCrimesPerPop'].apply(assign_risk_level)
# Create new df grouped by risk and calculate the average of unemployment
risk_summary = crimes_df.groupby('risk').agg(
    average_unemployment=('PctUnemployed', 'mean')
).reset_index()

# calculate high & low unemployment percentages
filtered_high_df = crimes_df[crimes_df['risk'] == 'HighCrime']
filtered_low_df = crimes_df[crimes_df['risk'] == 'LowCrime']

average_unemployment_high = round(filtered_high_df['PctUnemployed'].mean(), 2) #idk why it prints as a long decimal but it doesnt really affect the code so...
average_unemployment_low = round(filtered_low_df['PctUnemployed'].mean(), 2)

print(f"Average unemployment for HighCrime areas: {average_unemployment_high * 100}%")
print(f"Average unemployment for LowCrime areas: {average_unemployment_low*100}%")

# Save to CSV to not interfere with original crime.csv file
risk_summary.to_csv('crime_risk_summary.csv', index=False)


