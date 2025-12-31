import pandas as pd
def convert_sqft_to_int(area):
    tokens = area.split('-')
    if len(tokens) == 2:
        return (float(area.split('-')[0]) + float(area.split('-')[1]))//2
    try:
        return float(area)
    except:
        return None

def convert_to_bhk(size):
    try:
        bhk = int(size.split(' ')[0])
        return bhk
    except:
        return 0

def remove_pps_outliers(df):
    cleaned_df = pd.DataFrame()
    
    for location, group in df.groupby('location'):
        mean = group['price_rupees_per_sqft'].mean()
        std = group['price_rupees_per_sqft'].std()
        
        # Keep only rows where price_rupees_per_sqft is within one std deviation from mean
        filtered = group[(group['price_rupees_per_sqft'] > (mean - std)) & 
                         (group['price_rupees_per_sqft'] <= (mean + std))]
        
        cleaned_df = pd.concat([cleaned_df, filtered], ignore_index=True)
    
    return cleaned_df


def remove_bhk_outliers(df):
    indices_to_remove = []  # Store indexes of outliers

    # Group data by each location
    for location, location_df in df.groupby('location'):
        # Create a dictionary to store price stats for each BHK level
        bhk_price_stats = {}

        # Loop through each BHK group in that location
        for bhk, bhk_df in location_df.groupby('bhk'):
            bhk_price_stats[bhk] = {
                'mean_price': bhk_df['price_rupees_per_sqft'].mean(),
                'std_dev': bhk_df['price_rupees_per_sqft'].std(),
                'count': bhk_df.shape[0]
            }

        # Now check if a higher BHK is priced less than the lower BHK's average
        for bhk, bhk_df in location_df.groupby('bhk'):
            lower_bhk_stats = bhk_price_stats.get(bhk - 1)
            if lower_bhk_stats and lower_bhk_stats['count'] > 5:
                # If this BHK is priced less than the previous BHK's average → outlier
                bad_bhk = bhk_df[bhk_df['price_rupees_per_sqft'] < lower_bhk_stats['mean_price']]
                indices_to_remove.extend(bad_bhk.index)

    # Drop all detected outliers
    return df.drop(indices_to_remove, axis='index')