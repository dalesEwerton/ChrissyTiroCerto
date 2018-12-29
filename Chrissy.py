import ChampionashipStatus as CS
import ConstantGenerator as CG

def predictCalcioSerieA(makeHomeMean, takeHomeMean, makeVisitorMean, takeVisitorMean):
    homeMeanC = CS.getCalcioSerieA()[0][1]
    visitorMeanC = CS.getCalcioSerieA()[1][1]
    ofensive = CG.ofensiveCap(makeHomeMean, makeVisitorMean, homeMeanC, visitorMeanC)
    defensive = CG.defensiveCap(takeHomeMean, takeVisitorMean, visitorMeanC, homeMeanC)
    homeGoals = CG.predictHomeGoalsLambda(ofensive[0][1], defensive[1][1], homeMeanC)
    visitorGoals = CG.predictVisitorGoalsLambda(ofensive[1][1], defensive[0][1],visitorMeanC)
    chrissyConstant = homeGoals[1] - visitorGoals[1]
    homeGoals = CG.generatePoisonProbabilitiesForGoals(homeGoals[1])
    visitorGoals = CG.generatePoisonProbabilitiesForGoals(visitorGoals[1])
    draw = CG.generateDrawnProb(homeGoals, visitorGoals)
    homeV = CG.generateVictoryProb(homeGoals, visitorGoals)
    homeL = CG.generateLooseProb(homeGoals, visitorGoals)
    print("Vitoria da Casa - "  + str(homeV*100) + " %")
    print("Empate - " + str(draw*100) + " %")
    print("Vitoria Visitante - " + str(homeL*100) + " %")
    print("Chrissy Constant - " + str(chrissyConstant))


print("Juventus - Sampdoria")
predictCalcioSerieA(7/4,1/4,8/4,9/4)

print("Chievo - Frosinone Calcio")
predictCalcioSerieA(4/4,6/4,1/4,8/4)

print("Empoli - Inter Milan")
predictCalcioSerieA(9/4,8/4,4/4,8/4)

print("Genoa - Fiorentina")
predictCalcioSerieA(6/4,5/4,5/4,4/4)

print("Lazio - Torino")
predictCalcioSerieA(10/4,5/4,5/4,2/4)   

print("Parma - Roma")
predictCalcioSerieA(3/4,2/4,3/4,5/4)

print("Sassuolo - Atalanta")
predictCalcioSerieA(5/4,5/4,8/4,8/4)

print("Udinese - Cagliari")
predictCalcioSerieA(3/4,5/4,5/4,9/4)


