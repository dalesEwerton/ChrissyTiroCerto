import ChampionashipStatus as CS
import ConstantGenerator as CG

def predictCalcioSerieA(teamHome, teamVisitor, makeHomeMean, takeHomeMean, makeVisitorMean, takeVisitorMean):
    homeMeanC = CS.getPremierLeague()[0][1]
    visitorMeanC = CS.getPremierLeague()[1][1]
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
    file_obj = open("data/results.csv", "a")
    new_line = ("\n" + teamHome + "," + teamVisitor + "," + "Premier League," + str(homeV) + "," + str(draw) + "," + str(homeL) + "," + str(chrissyConstant)+",")
    print(file_obj)
    file_obj.write(new_line)
    file_obj.close()
    print(teamHome + " x " + teamVisitor)
    print("Vitoria da Casa - "  + str(homeV*100) + " %")
    print("Empate - " + str(draw*100) + " %")
    print("Vitoria Visitante - " + str(homeL*100) + " %")
    print("Jogos - 10")
    print("Chrissy Constant - " + str(chrissyConstant))


