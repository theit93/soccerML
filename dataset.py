import json
import pandas
from pandas.io.json import json_normalize

def build_statistic_classifier(team_id):
    # https://api-football-v1.p.mashape.com/statistics/{league_id}/{team_id}
    with open('./data/statistic.json') as f:
        d = json.load(f)

        df = json_normalize(d['api']['stats'])

        print(df)
        # TODO build classifier


def build_h2h_classifier(homeTeamId, awayTeamId):
    with open('./data/fixturesH2H.json') as f:
        d = json.load(f)
        
        df = json_normalize(d['api']['fixtures'])
        
        print(df)
        # TODO build classfier


def main():
    # look for games in the upcoming day
    # https://api-football-v1.p.mashape.com/fixtures/date/{tomorrow}

    with open('./data/fixturesByNextMatches.json') as f:
        d = json.load(f)

    df = pandas.DataFrame.from_dict(d['api']['fixtures'])

    # process each game and calculate probability
    # 1. Bundesliga: league 8
    for gameIdx in df:
        game = df[gameIdx]

        homeTeamId = game['homeTeam_id']
        build_statistic_classifier(homeTeamId)

        awayTeamId = game['awayTeam_id']
        build_h2h_classifier(homeTeamId, awayTeamId)
        

if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main=main)