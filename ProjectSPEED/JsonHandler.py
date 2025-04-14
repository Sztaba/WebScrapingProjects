import json

class JsonHandler:
    def extractGameUrls(jsonData: dict) -> list:
        def returnIdForGame(game):
            return game["url"]
        return list(map(returnIdForGame, jsonData["props"]["pageProps"]["mainGames"]["gameList"]))