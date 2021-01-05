# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:48:46 2020

@author: Matt
"""
import random
class game:
    
    participantlist=[]
    
    def __init__(self,participantlist):
        self.participantlist=participantlist
    
    
    def randomize(self):
        for i in range (len(self.participantlist)):
            tempscore=self.participantlist[i].totalscore*self.participantlist[i].gamecount
            if self.participantlist[i].gamecount<3:
                self.participantlist[i].gamecount+=1
            self.participantlist[i].totalscore=(tempscore+random.randint(0, 12))/self.participantlist[i].gamecount
        
        
    def finalGames(self):
        for i in range(5):
            for i in range (len(self.participantlist)):

                tempscore=self.participantlist[i].totalscore*self.participantlist[i].gamecount
                self.participantlist[i].gamecount+=1
                self.participantlist[i].totalscore=(tempscore+random.randint(0, 12))/self.participantlist[i].gamecount
        
        
class player:
    def __init__(self,name):
        self.name=name
        self.role=None
        self.gamecount=int(0)
        self.totalscore=0
        
class tournament:
    def __init__(self,name,playerlist):
        self.name=name
        self.playerlist=playerlist
    
    def printPlayers(tournament):
            for i in range(len(tournament.playerlist)):
                print("Name :"+str(tournament.playerlist[i].name)+"\t Score: "+str(tournament.playerlist[i].totalscore)+"\t Gamecount: "+str(tournament.playerlist[i].gamecount))
    
    def playerCount(tournament):
        count=0
        for i in range(len(tournament.playerlist)):
            count+=1
        return count
    
    def dropPlayers(tournament):
        del tournament.playerlist[:10]
        
        
    def resetPlayers(tournament):
        for i in range(len(tournament.playerlist)):
            tournament.playerlist[i].gamecount=0
            tournament.playerlist[i].totalscore=0
            
    def orderRank(tournament):
        playerlist.sort(key=lambda x: x.totalscore)
    
    def printLeaderboard(tournament):
        n=len(tournament.playerlist)
        tournament.orderRank()
        print("\n\n\tThe winner is: "+tournament.playerlist[n-1].name+" with {} points\n\nThe second is: ".format(tournament.playerlist[n-1].totalscore)+tournament.playerlist[n-2].name+" with {} points\t\tThe third is: ".format(tournament.playerlist[n-2].totalscore)+tournament.playerlist[n-3].name+" with {} points".format(tournament.playerlist[n-3].totalscore))
        print("\n The remaining players are, by rank :")
        for i in range(7):
            print("\n {} Name: {}, Score: {}".format((i+4), tournament.playerlist[n-(i+4)].name,tournament.playerlist[n-(i+4)].totalscore))
    
def GamePhase(tournament):
        updatedplayerlist=[] 
        for j in range(len(tournament.playerlist)): #This will add all the player that haven't yet played to a new playerlist to continue simulating random games
                if not tournament.playerlist[j].gamecount>0:
                    updatedplayerlist.append(tournament.playerlist[j])        
        for i in range(len(tournament.playerlist)//10): #The first 10 games (1 game for each player)


            for j in range(len(updatedplayerlist)): 
                if updatedplayerlist[j].gamecount>0:
                    updatedplayerlist.remove(updatedplayerlist[j])
            playerlist1=random.choices(updatedplayerlist,k=10)
            for player in playerlist1:
                if player in updatedplayerlist:
                    updatedplayerlist.remove(player)
            game1=game(playerlist1)
            game1.randomize()
            playerlist1.clear()
        updatedplayerlist.clear()            
        
        
        for j in range(len(tournament.playerlist)): #This will add all the player that haven't yet played to a new playerlist to continue simulating random games
                if not tournament.playerlist[j].gamecount>1:
                    updatedplayerlist.append(tournament.playerlist[j])        
        for i in range(len(tournament.playerlist)//10): #The first 10 games (1 game for each player)


            for j in range(len(updatedplayerlist)): 
                if updatedplayerlist[j].gamecount>1:
                    updatedplayerlist.remove(updatedplayerlist[j])
            playerlist1=random.choices(updatedplayerlist,k=10)
            for player in playerlist1:
                if player in updatedplayerlist:
                    updatedplayerlist.remove(player)
            game1=game(playerlist1)
            game1.randomize()
            playerlist1.clear()
        
        updatedplayerlist.clear() 
        for j in range(len(tournament.playerlist)): #This will add all the player that haven't yet played to a new playerlist to continue simulating random games
                if not tournament.playerlist[j].gamecount>2:
                    updatedplayerlist.append(tournament.playerlist[j])        
        for i in range(len(tournament.playerlist)//10): #The first 10 games (1 game for each player)


            for j in range(len(updatedplayerlist)): 
                if updatedplayerlist[j].gamecount>2:
                    updatedplayerlist.remove(updatedplayerlist[j])
            playerlist1=random.choices(updatedplayerlist,k=10)
            for player in playerlist1:
                if player in updatedplayerlist:
                    updatedplayerlist.remove(player)
            game1=game(playerlist1)
            game1.randomize()
            playerlist1.clear()
        
        updatedplayerlist.clear() 
            
        playerlist.sort(key=lambda x: x.totalscore)
        

def GamePhaseByRanking(tournament): #♦Similar to GamePhase, but creating the games ny ranks.
        for i in range(len(tournament.playerlist)//10): #The first 10 games (1 game for each player)

            playerlist1=tournament.playerlist[i-1:10*i-1]
            game1=game(playerlist1)
            game1.randomize()
            playerlist1.clear()       
            tournament.orderRank()
        for i in range(len(tournament.playerlist)//10): #The second 10 games (1 game for each player)


            playerlist1=tournament.playerlist[i-1:10*i-1]
            game1=game(playerlist1)
            game1.randomize()
            playerlist1.clear()       
            tournament.orderRank()    
        
            
        for i in range(len(tournament.playerlist)//10): #The third 10 games (1 game for each player)


            playerlist1=tournament.playerlist[i-1:10*i-1]
            game1=game(playerlist1)
            game1.randomize()
            playerlist1.clear()       
            tournament.orderRank()    
        
             
#Creating a player list of 100 players

Bart=player("Bart")
Matt=player("Matt")
Tom=player("Tom")
Marc=player("Marc")
John=player("John")
Eric=player("Eric")
Chris=player("Chris")
Seb=player("Seb")
Etienne=player("Etienne")
Raf=player("Raf")    
cotreverend=player("Julien")
translatorhewn=player("Zerator")
fonbiredonnybrook=player("Jack")
disruptivejealous=player("Averell")
crecksaxophone=player("Lucky Luke")
butcherrocket=player("Batman")
togethermudblood=player("Ed")
threethorin=player("Raul")
accordingunsung=player("Jose")
mindolluinfossil=player("Margaux")
victorycompete=player("Erica")
writheformation=player("Victoire")
moolevitate=player("Jen")
brownsnape=player("Robert")
crumptonlandless=player("Sophia")
unrulyelated=player("Samuel")
bambooguarded=player("Hunter")
tectacleslivered=player("Jacob")
truthfulbitts=player("Caleb")
bowmatch=player("Kev")
subtletyluxurious=player("Jeremy")
chickweedribbit=player("Maya")
favorproposal=player("Kyle")
mayquail=player("Lorenzo")
unlikeaccused=player("Enzo")
turntbiscuits=player("Lauren")
ficketportkey=player("Laura")
lockdoomy=player("Serenity")
poetreflection=player("Peace")
crimpleforses=player("Raptor")
junkielithe=player("Shylark")
amongsteerforth=player("Aiekillu")
truckpaternal=player("Jiraya")
rokesmithhowler=player("Eivor")
ourselvessales=player("Trevor")
toastingbelief=player("Bjorn")
sardonicalive=player("Ivarr")
polishpeace=player("Ubbe")
elephantchate=player("Ragnar")
lefmourner=player("Damon")
thoorlytrail=player("Dean")
rabidpoint=player("Sam")
angrydeft=player("Crowley")
abusiveblarp=player("Castiel")
mercuryabounding=player("Yoda")
treatmentwriting=player("Mace windu")
airsprout=player("Anakin")
ferociouschottom=player("Dovahkin")
thrushereal=player("Eleanor")
chartmoose=player("Noah")
lartoonenhance=player("Liam")
fumbgrumble=player("Mason")
slovakianclinical=player("Will")
uprightnachos=player("William")
wartlasta=player("Ethan")
smashingtimberry=player("James")
moppingsleviosa=player("Alex")
cloudracket=player("Alexander")
noteworthycavalcade=player("Mike")
roomysnisps=player("Michael")
ricepsspeaker=player("Ben")
feeptortoise=player("Benjamin")
dhiskeylodestone=player("Emma")
tumleyfertile=player("Ariel")
engineerdescendo=player("Aurelien")
knipreaction=player("Harper")
langlockhalf=player("Oliver")
symbolstransport=player("Malcom")
lipmature=player("Logan")
findingsparse=player("Jericho")
broodsomething=player("Felicity")
fenchpaella=player("Kamelia")
graperecto=player("Jackson")
japanesefold=player("Jerome")
silentdisease=player("Nicolas")
lanksbuilder=player("Pierre")
chogflamboyant=player("Roger")
skinnedscullian=player("Gerard")
teenytinyfrizzy=player("Patrick")
hurriedfluid=player("Marie")
canoeaddition=player("Lola")
injurecountless=player("Camille")
fubblethole=player("Michelle")
blightgoofy=player("Barrack")
articulateseedling=player("Donald")
basketmcboon=player("Emmanuel")
chinealthough=player("François")
fickerelpakistani=player("Valerie")
varymodified=player("Nathalie")
kickstones=player("Corine")


#Creating the playerlist and tournament
playerlist=[Bart,Matt,Tom,Marc,John,Eric,Chris,Seb,Etienne,Raf,cotreverend,translatorhewn,fonbiredonnybrook,disruptivejealous,crecksaxophone,butcherrocket,togethermudblood,threethorin,accordingunsung,mindolluinfossil,victorycompete,writheformation,moolevitate,brownsnape,crumptonlandless,unrulyelated,bambooguarded,tectacleslivered,truthfulbitts,bowmatch,subtletyluxurious,chickweedribbit,favorproposal,mayquail,unlikeaccused,turntbiscuits,ficketportkey,lockdoomy,poetreflection,crimpleforses,junkielithe,amongsteerforth,truckpaternal,rokesmithhowler,ourselvessales,toastingbelief,sardonicalive,polishpeace,elephantchate,lefmourner,thoorlytrail,rabidpoint,angrydeft,abusiveblarp,mercuryabounding,treatmentwriting,airsprout,ferociouschottom,thrushereal,chartmoose,lartoonenhance,fumbgrumble,slovakianclinical,uprightnachos,wartlasta,smashingtimberry,moppingsleviosa,cloudracket,noteworthycavalcade,roomysnisps,ricepsspeaker,feeptortoise,dhiskeylodestone,tumleyfertile,engineerdescendo,knipreaction,langlockhalf,symbolstransport,lipmature,findingsparse,broodsomething,fenchpaella,graperecto,japanesefold,silentdisease,lanksbuilder,chogflamboyant,skinnedscullian,teenytinyfrizzy,hurriedfluid,canoeaddition,injurecountless,fubblethole,blightgoofy,articulateseedling,basketmcboon,chinealthough,fickerelpakistani,varymodified,kickstones]
Tournament=tournament("Premier tournoi",playerlist)
#Resolving the tournament
for i in range(9):
    print("\n\Round number %d\n\n",i+1)
    GamePhase(Tournament)
    Tournament.printPlayers()
    Tournament.dropPlayers()
    Tournament.resetPlayers()
    print("\n\nPlayers dropped\n\n")
    Tournament.printPlayers()
#Now there are only finalists, so the final may begin
print("\n\n\tFinal ranking :\n\n")
game=game(Tournament.playerlist)
game.finalGames()
Tournament.orderRank()
Tournament.printPlayers()
Tournament.printLeaderboard()