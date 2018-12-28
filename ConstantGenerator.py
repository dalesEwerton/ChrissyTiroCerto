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
        predicts.append((i, value))
    return predicts

def generateDrawnProb(probabilitiesForHome, probabilitiesForVisitor):
    result = (probabilitiesForHome[0][1] * probabilitiesForVisitor[0][1]) + (probabilitiesForHome[1][1] * probabilitiesForVisitor[1][1]) + (probabilitiesForHome[2][1] * probabilitiesForVisitor[2][1]) +(probabilitiesForHome[3][1] * probabilitiesForVisitor[3][1]) +(probabilitiesForHome[4][1] * probabilitiesForVisitor[4][1]) +(probabilitiesForHome[5][1] * probabilitiesForVisitor[5][1])
    return result

def generateVictoryProb(probabilitiesForHome, probabilitiesForVisitor):
    winResult = 0
    for i in range(1,6):
        j = 0
        while(j < i):
            winResult = winResult + (probabilitiesForHome[i][1] * probabilitiesForVisitor[j][1])
            j = j + 1
    return winResult

def generateLooseProb(probabilitiesForHome, probabilitiesForVisitor):
    looseResult = 0
    for i in range(5):
        j = 5
        while(j > i):
            looseResult = looseResult + (probabilitiesForHome[i][1] * probabilitiesForVisitor[j][1])
            j = j-1
    return looseResult

#TESTES

print("Tests of ConstantGenerator module.")
print(ofensiveCap(10,3,8,4))
print(defensiveCap(10,3,8,4))

print(predictHomeGoalsLambda(1.235, 0.881, 1.492))
print(predictVisitorGoalsLambda(1.235, 0.881, 1.492))

print(generatePoisonProbabilitiesForGoals(1.623))

print("Empate " + str(generateDrawnProb(generatePoisonProbabilitiesForGoals(1.623), generatePoisonProbabilitiesForGoals(0.823))))

print("Vitoria " + str(generateVictoryProb(generatePoisonProbabilitiesForGoals(1.623), generatePoisonProbabilitiesForGoals(0.823))))

print("Derrota " + str(generateLooseProb(generatePoisonProbabilitiesForGoals(1.623), generatePoisonProbabilitiesForGoals(0.823))))
