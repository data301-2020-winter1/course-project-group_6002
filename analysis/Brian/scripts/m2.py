def load_and_process(filePath):
    import pandas as pd

    dfClean = (
        pd.read_csv(filePath,
        usecols = ["Rank", "Name", "Genre", "Global_Sales", "Year", "Platform"]) # So far our only focus of work
        .sort_values(by= "Global_Sales", ascending = False) # Cash money check
        .dropna(axis = 1) # Drop any NA values completely
        .reset_index(drop=True) # Reset index so we don't mess up orders
    )
    dfClean

    dfWii = (
        dfClean
        .loc[lambda x: x["Platform"] == "Wii"] # We love Wii only wanna play Wii
        #.loc[lambda x: x["Year"] <= 2000] # Check for only recent games
        # Does not run with Year in it, Python returns a key error when the function runs properly outside the chaining
        .loc[lambda x: x["Rank"] <= 2500] # Nothing ranked lower than 2500
        .assign(Averaged_Sales = lambda x: x["Global_Sales"]/4) # Average out sales
        .sort_values(by= "Global_Sales", ascending = False) # Re-sort in case any vales got changed
        .reset_index(drop = True) # Order things nicely
    )
    return dfWii

load_and_process("D:/acer/Documents/Academia/UBCO/Y4/DATA301/Labs/course-project-group_6002/data/raw/Video_game_sales_db.csv")
