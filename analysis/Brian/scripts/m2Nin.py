def load_and_process_Nintendo(filePath):
    import pandas as pd
    dfClean = (
        pd.read_csv(filePath,
        usecols = ["Rank", "Name", "Publisher", "Platform", "Genre", "Global_Sales", "Year"]) # So far our only focus of work
        .sort_values(by= "Global_Sales", ascending = False) # Cash money check
        .dropna(axis = 0, thresh = 3) # Drop any NA values completely
        .reset_index(drop=True) # Reset index so we don't mess up orders
    )

    dfWii = (
        dfClean
        .loc[(dfClean["Publisher"] == "Nintendo")]
        #.loc[lambda x: x["Publisher"] == "Nintendo"] # We love Wii only wanna play Wii
        #.loc[lambda x: x["Platform"] == "Wii" | x["Platform"] == "DS"]
        #.loc[lambda x: x["Platform"] == "DS"]
        .loc[(dfClean["Platform"] == "Wii") | (dfClean["Platform"] == "DS")]
        .loc[lambda x: x["Year"] >= 2000] # Check for only recent games
        .loc[lambda x: x["Rank"] <= 2500] # Nothing ranked lower tan 2500
        .assign(Averaged_Sales = lambda x: x["Global_Sales"]/4) # Average out sales
        .sort_values(by= "Global_Sales", ascending = False) # Re-sort in case any vales got changed
        .reset_index(drop = True) # Order things nicely
    )
    return dfWii

load_and_process_Nintendo("../../data/raw/Video_game_sales_db.csv")
