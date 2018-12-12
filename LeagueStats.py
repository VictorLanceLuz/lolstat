#Author: Victor Luz
#Date: Tue Dec 11 2018

import requests

def main():
    region = "NA1"
    summonerName = "Vertlance"
    APIKey = "RGAPI-84d4b3a6-10a1-4c58-9a68-1feae8bea957"
    #Proxy for Intel Corporation
    proxy = {"https" : "http://proxy-chain.intel.com:911"}
    patch = "6.24.1"


    #Summoner Statistics
    summonerData = requestSummonerData(region, summonerName, APIKey, proxy)
    summonerID = summonerData['id']
    print summonerID

    #Ranked Statistics
    #0 for Flex; 1 for Solo
    rankedQueue = 0
    rankedStats = requestRankedStats(region, summonerID, APIKey, proxy)
    rankedRank = rankedStats[rankedQueue]['tier'] + " " + rankedStats[rankedQueue]['rank']
    rankedWins = rankedStats[rankedQueue]['wins']
    rankedLosses = rankedStats[rankedQueue]['losses']
    rankedWinRate = str(round(float(rankedWins) * 100 / (float(rankedWins) + float(rankedLosses)) , 2)) + "%"
    
    #Champion Mastery Statistics (top three)
    championMasteries = requestChampionMasteries(region, summonerID, APIKey, proxy)
    
    top     = championMasteries[0]
    second  = championMasteries[1]
    third   = championMasteries[2]
    
    summonerSummary(rankedWinRate, summonerName, rankedRank)
    championData = requestChampionData(patch, proxy)
    
def championMastery(champion):
    championID      = champion[1]
    championLevel   = champion[2]
    championPoints  = champion[3]
    

def requestSummonerData(region, summonerName, APIKey, proxy):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    response = requests.get(URL, proxies=proxy)
    return response.json()

def requestRankedStats(region, summonerID, APIKey, proxy):
    URL = "https://" + region + ".api.riotgames.com/lol/league/v3/positions/by-summoner/" + str(summonerID) + "?api_key=" + APIKey
    response = requests.get(URL, proxies=proxy)
    return response.json()

def requestChampionMasteries(region, summonerID, APIKey, proxy):
    URL = "https://" + region + ".api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/" + str(summonerID) + "?api_key=" + APIKey
    response = requests.get(URL, proxies=proxy)
    return response.json()

def requestChampionData(patch, proxy):
    URL = "https://ddragon.leagueoflegends.com/cdn/" + patch + "/data/en_US/champion.json"
    response = requests.get(URL, proxies=proxy)
    return response.json()

def summonerSummary(rankedWinRate, summonerName, rankedRank):
    print summonerName + " has ranked stats " + rankedRank + " with a " + rankedWinRate + " win rate."
    
if __name__ == "__main__":
    main()
