### FACTOR Funding

Author: Chad Neald

FACTOR is the Foundation Assisting Canadian Talent on Recordings. Every year Canadian music organizations and artists apply to receive one of the many grants available through FACTOR. This is a brief investigation into the money allocated during the 2019-2020 and 2020-2021 fiscal years. 

Python is used to process the data while Tableau is used to visualize the data and present the findings.

The final results of this investigation are presented in a public Tableau story available [here](https://public.tableau.com/app/profile/chad6383/viz/FACTORFundingChadN/FACTORStory). 

![Tableau Overview](/images/tableau_overview.gif)
### The Data

The raw FACTOR data used for this project can be found in the form of a pdf [here](https://www.factor.ca/factorfunded/recipients/). To convert this data to a .xlsx excel file the following conversion website was used https://www.cleverpdf.com/pdf-to-excel. This data contains information regarding the artists who received the grants, the grant type, the amount, the year, the applicant, the applicant province, and the artist province.

Additionally, the raw provincial Canadian population data can be found on Statistics Canada's website [here](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901&cubeTimeFrame.startMonth=01&cubeTimeFrame.startYear=2020&cubeTimeFrame.endMonth=01&cubeTimeFrame.endYear=2020&referencePeriods=20200101%2C20200101).

### Data Processing

The raw data for this project is already processed and saved in this repository under the /data/processed/ directory. If you wish to repeat the data processing yourself however, begin by cloning the repo and move into the root of the project. Run the following command from your terminal to set up a new conda environment with the necessary packages installed:

`conda env create -f env.yaml`

Once the above command is finished executing, open up the "pipeline.ipynb" notebook and run it from top to bottom. Please note however, that in order to run the Spotify section of this notebook you will need to obtain your own "Spotify for Developers" credentials, which includes both a client ID and a client secret, and input those values into the appropriate function call. Create an account [here](https://developer.spotify.com/dashboard/login) to acquire these credentials.

After the notebook finishes running, all of the processed CSV files should now be updated.

### Tableau Public

All of the visualization work was done in Tableau Public 2021.2 and is not reproduced through this repo. The software however is free to use and can be downloaded at this [link](https://public.tableau.com/en-us/s/download).
 