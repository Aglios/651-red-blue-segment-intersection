#case0: botHi>topLo and botHi>topHi
#case1: botHi>topLo and botHi<topHi
#case2: botHi<topLo

#input: flag,bundlelist
#output: new intersections
def procFlag(flag,bl):
        intsec=[]
        [botLo,botHi,topLo,topHi]=bl.findLoHi(flag)
        botLo.prt()
        botHi.prt()
        topLo.prt()
        topHi.prt()
        if topHi.isEmpty():
                topHi=topLo
#               print("empty split")
        case=bl.checkCase(botLo,botHi,topLo,topHi)
        print('case',case)
        if case==0:
                if flag.type==0:
                        bl.procStart0(flag,topLo,topHi)
                else:
                        bl.procEnd(flag,botHi,topLo,topHi)
        elif case==1:
                if flag.type==0:
                        bl.procStart1(flag,botHi,topLo)
                else:
                        bl.procEnd(flag,botHi,topLo,topHi)
        else:
                [botHi,topLo]=bl.swapBotHi(botHi,topLo,intsec)
                assert bl.checkCase(botLo,botHi,topLo,topHi)==1
                if flag.type==0:
                        bl.procStart1(flag,botHi,topLo)
                else:
                        bl.procEnd(flag,botHi,topLo,topHi)
        assert bl.checkColor()
        return intsec

