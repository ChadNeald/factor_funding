import pandas as pd


def process_factor_data(input_file, output, num_sheets=27):
    """
    This function imports the raw FACTOR data as a .xlsx file, cleans it,
    and exports it as a csv file.

    Parameters
    ----------
    input_file : str
        The .xlsx file containing the raw data.
    output : str
        The directory and name of the processed .csv file that will be output.
    num_sheets : int
        The number of sheets to read in from the raw data file. There is a total of 27 sheets.
        Default: 27 

    """

    temp_data = pd.DataFrame()
    combined_data = pd.DataFrame()

    # Combine all sheets into one dataframe for cleaning and export
    for i in range(num_sheets):
        temp_data = pd.read_excel(input_file, sheet_name=i)
        combined_data = pd.concat([combined_data, temp_data])

    combined_data = combined_data.drop(columns="Offer")

    combined_data = combined_data.rename(columns={
        "Program": "grant_type",
        "Fiscal Year": "year",
        "Applicant": "applicant",
        "Artist/Project": "artist",
        "Applicant Province": "applicant_province",
        "Artist Province": "artist_province",
        "Offer": "offer",
        "Unnamed: 7": "offer"
    })

    # Convert the "offer" column to numeric
    combined_data = combined_data.reset_index(drop=True)
    combined_data["offer"] = combined_data["offer"].str.replace(",", "")
    combined_data["offer"] = pd.to_numeric(combined_data["offer"])

    combined_data.to_csv(output, encoding="utf-8", index=False)


def process_population_data(factor_processed_input_file, pop_input_file, pop_output_file):
    """
    This function processes the raw population data as a .csv file, cleans it,
    and exports it as a csv file.

    Parameters
    ----------
    factor_processed_input_file : str
        The .csv file containing the processed FACTOR data.
    pop_input_file : str
        The .csv file containing the raw population data.
    pop_output_file : str
        The name of the output .csv file for the processed population data. 

    """

    # Read in FACTOR data
    factor_data = pd.read_csv(factor_processed_input_file)

    # Read in the provincial population estimates
    pop_data = pd.read_csv(pop_input_file)

    # Clean the population data into the same form as the FACTOR data
    pop_data = pop_data[['GEO', "VALUE"]][1:]
    pop_data = pop_data.rename(
        columns={"GEO": "applicant_province", "VALUE": "population"})
    pop_data = pop_data.replace("Quebec", "Québec")
    pop_data['population'] = pd.to_numeric(pop_data["population"])

    # Find the offer sum for each province
    province_offer_sums = pd.DataFrame(
        factor_data.groupby("applicant_province")["offer"].sum())
    province_offer_sums = province_offer_sums.reset_index()
    province_offer_sums = province_offer_sums.rename(
        columns={'offer': 'offer_sum'})

    # Combine the provincial offer sum data with the population data
    province_offer_pop = province_offer_sums.merge(pop_data)

    # Calculate the ratio of offer to population
    province_offer_pop['offer_pop_ratio'] = province_offer_pop['offer_sum'] / \
        province_offer_pop['population']

    # Export to CSV
    province_offer_pop.to_csv(pop_output_file, index=False)
