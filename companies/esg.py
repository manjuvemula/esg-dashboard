import pandas as pd

def calculate_esg_score(travel_df, utility_df):

    total_fuel = travel_df["Fuel_Liters"].sum() if "Fuel_Liters" in travel_df.columns else 0
    total_kwh = utility_df["KWH"].sum() if "KWH" in utility_df.columns else 0

    fuel_emissions = total_fuel * 2.5
    kwh_emissions = total_kwh * 0.7

    co2_emissions = fuel_emissions + kwh_emissions

    # FINAL ESG FORMULA (your requested version)
    baseline = 100000
    esg_score = max(0, 100 - (co2_emissions / baseline * 100))

    return {
        "total_fuel": total_fuel,
        "total_kwh": total_kwh,
        "co2_emissions": co2_emissions,
        "esg_score": round(esg_score, 2)
    }