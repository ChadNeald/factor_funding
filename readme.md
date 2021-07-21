### Overview

This repo performs a brief exploratory analysis of the FACTOR Canada music grants given out over the last two fiscal years (2019-2020 and 2020-2021). The results are presented in a public Tableau story available [here](https://public.tableau.com/app/profile/chad6383/viz/FACTORFundingChadN/FACTORStory). 

![Tableau Overview](/images/tableau_overview.gif)
### The Data

The raw FACTOR data can be found in the form of a pdf [here](https://www.factor.ca/factorfunded/recipients/). To convert this data to a .xlsx excel file the following conversion website can be used https://www.cleverpdf.com/pdf-to-excel.

The raw provincial Canadian population data can be found on Statistics Canada's website [here](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901&cubeTimeFrame.startMonth=01&cubeTimeFrame.startYear=2020&cubeTimeFrame.endMonth=01&cubeTimeFrame.endYear=2020&referencePeriods=20200101%2C20200101).

### Data Processing

The raw data for this project is already processed and saved in this repository under the /data/processed/ directory. If you wish to repeat the data processing yourself however, begin by cloning the repo and move into the root of the project. Run the following command from your terminal to set up a new conda environment with the necessary packages installed:

`conda env create -f env.yaml`

Once the above command is finished executing, open up the "pipeline.ipynb" notebook and run it from top to bottom. The exported processed CSV files should now all be updated.

All of the visualization work was done in Tableau Public.
 