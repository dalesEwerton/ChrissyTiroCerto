import math

def ofensiveCap(makeHomeMean, makeVisitorMean, makeLeagueHomeMean, makeLeagueVisitorMean):
    return [('Home',makeHomeMean/makeLeagueHomeMean), ('Visitor', makeVisitorMean/makeLeagueVisitorMean)]

def defensiveCap(takeHomeMean, takeVisitorMean, takeLeagueHomeMean, takeLeagueVisitorMean):
    return [('Home', takeHomeMean/takeLeagueHomeMean), ('Visitor', takeVisitorMean/takeLeagueVisitorMean)]

def predictHomeGoalsLambda(ofensiveHomeCap, defensiveVisitorCap, makeLeagueHomeMean):
    return ('Number of Goals', ofensiveHomeCap * defensiveVisitorCap * makeLeagueHomeMean)

def predictVisitorGoalsLambda(ofensiveVisitorCap, defensiveHomeCap, takeLeagueVisitorMean):
    return ('Number of Goals', ofensiveVisitorCap * defensiveHomeCap * takeLeagueVisitorMean)

def generatePoisonProbabilitiesForGoals(predictLambda):
    predicts = []
    for i in range(6):
        value = ( (math.exp(-predictLambda)) * (predictLambda ** i) ) / math.factorial(i)
        predicts.append((i, value * 100))
    return predicts

#TESTES

print("Tests of ConstantGenerator module.")
print(ofensiveCap(10,3,8,4))
print(defensiveCap(10,3,8,4))

print(predictHomeGoalsLambda(1.235, 0.881, 1.492))
print(predictVisitorGoalsLambda(1.235, 0.881, 1.492))

print(generatePoisonProbabilitiesForGoals(1.623))
