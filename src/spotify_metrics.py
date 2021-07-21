import pandas as pd
import numpy as np
import altair as alt
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import unidecode


def process_spotify_metrics(factor_processed_input_file,
                            credentials_cid,
                            credentials_secret,
                            spotify_followers_popularity_output,
                            spotify_grant_type_output):
    """
    This function utilizes Spotify's API, through spotipy, to gather the number of followers
    and the popularity score for each artist in the FACTOR dataset and exports the results as 
    two csv files.

    Parameters
    ----------
    factor_processed_input_file : str
        The .csv file containing the processed FACTOR data.
    credentials_cid : str
        The "Spotify for Developers" id credential needed to access Spotify's API.
    credentials_secret : str
        The "Spotify for Developers" secret credential needed to access Spotify's API.
    spotify_followers_popularity_output : str
        The name of the output file that will contain the artist, followers, popularity, and offer.
    spotify_grant_type_output : str
        The name of the output file that will contain the grant_type, year, applicant, artist, 
        appicant_province, artist_province, offer, followers, and popularity.

    """
    # Read in the processed FACTOR data
    data = pd.read_csv(factor_processed_input_file)

    # A list of artists in their original names and spellings
    artists_orig = list(data['artist'].unique())

    # Spotify's API doesn't handle certain characters well so fixing a few special cases
    data_copy = data.copy()
    data_copy['artist'] = data_copy['artist'].str.replace('//', '')
    data_copy['artist'] = data_copy['artist'].str.replace('[¡!]', '')

    # A list of artists with their edited name (special characters removed)
    artists_edited = list(data_copy['artist'].unique())

    # Find the nan entry and remove it
    for i, a in enumerate(artists_orig):
        if not isinstance(a, str):
            index = i

    del artists_orig[index]
    del artists_edited[index]

    # These values will change for every user
    # Go to Spotify for developers to find your own credentials
    cid = credentials_cid
    secret = credentials_secret

    client_credentials_manager = SpotifyClientCredentials(
        client_id=cid, client_secret=secret, requests_timeout=100)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Find the number of followers and popularity of each artist through spotipy
    followers = []
    popularity = []

    for a in artists_edited:
        results = sp.search(q='artist:' + a, type='artist')
        match_found = False

        if len(results['artists']['items']) > 0:
            for i in range(len(results['artists']['items'])):
                # Replace special characters with their regular versions
                # and force to lower caps before comparing names
                if unidecode.unidecode(results['artists']['items'][i]['name']).lower() == unidecode.unidecode(a).lower():
                    followers.append(results['artists']
                                     ['items'][i]['followers']['total'])
                    popularity.append(
                        results['artists']['items'][i]['popularity'])
                    match_found = True
                    break

            # if there wasn't an artist match in the search results, append zero values
            if match_found == False:
                followers.append(0)
                popularity.append(0)

        # if no search results are returned, append zero values
        else:
            followers.append(0)
            popularity.append(0)

    data_pop_fol = pd.DataFrame(
        {'artist': artists_orig, 'followers': followers, 'popularity': popularity})

    # Combine follower/popularity data with the processed data
    data_merged = data.merge(data_pop_fol, how='inner')

    # Remove the "Collective Initiative" grants which contain organizations
    data_merged = data_merged.query("grant_type != 'Collective Initiatives'")

    data_merged = data_merged[~data_merged['offer'].isna()]

    # Manually remove the outlier James Brown because it's not the famous James Brown
    data_merged.drop(
        data_merged.index[data_merged['artist'] == 'James Brown'], inplace=True)

    # Group by artist and sum up total offer
    data_grouped = data_merged.groupby(['artist', 'followers', 'popularity'],
                                       as_index=False)['offer'].sum()

    # Export to csv
    data_grouped.to_csv(
        spotify_followers_popularity_output, index=False)
    data_merged.to_csv(
        spotify_grant_type_output, index=False)
