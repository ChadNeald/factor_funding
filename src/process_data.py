import pandas as pd


def process_raw_data(input_file, output, num_sheets=27):
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
