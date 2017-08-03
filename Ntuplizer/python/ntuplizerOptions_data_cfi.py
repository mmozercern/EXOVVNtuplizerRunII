
import FWCore.ParameterSet.Config as cms

config = dict()

#--------- general ----------#
config["SPRING16"] = True
config["RUNONMC"] = False
config["USEJSON"] = True
config["JSONFILE"] = "Cert_294927-299042_13TeV_PromptReco_Collisions17_JSON.txt"
#config["JSONFILE"] = "JSON/Cert_246908-258750_13TeV_PromptReco_Collisions15_25ns_JSON.txt"
config["FILTEREVENTS"] = False
config["BUNCHSPACING"] = 25
config["USENOHF"] = False

#--------- basic sequences ----------#
config["DOGENPARTICLES"] = False
config["DOGENJETS"] = False
config["DOGENEVENT"] = False
config["DOPILEUP"] = False
config["DOELECTRONS"] = False
config["DOMUONS"] = True
config["DOTAUS"] = True
config["DOAK8JETS"] = True
config["DOAK4JETS"] = True
config["DOVERTICES"] = True
config["DOTRIGGERDECISIONS"] = True
config["DOTRIGGEROBJECTS"] = True
config["DOHLTFILTERS"] = True
config["DOMISSINGET"] = True
config["DOTAUSBOOSTED"] = True
config["DOMETSVFIT"] = False
config["DOMVAMET"] = False

#--------- AK8 jets reclustering ----------#
config["ADDAK8GENJETS"] = False #! Add AK8 gen jet collection with pruned and softdrop mass
config["DOAK8RECLUSTERING"] =False
config["DOAK8PRUNEDRECLUSTERING"] = False #! To add pruned jet and pruned subjet collection (not in MINIAOD)
config["DOAK8PUPPI"] = True
config["DOAK10TRIMMEDRECLUSTERING"] = False #ATLAS sequence
config["DOHBBTAG"] = False #Higgs-tagger
config["DOAK8PUPPIRECLUSTERING"] = False
config["UpdateJetCollection"] = False #needed for Higgs-tagger in 80X

#--------- MET reclustering ----------#
config["DOMETRECLUSTERING"] = False

#--------- JEC ----------#
config["CORRJETSONTHEFLY"] = False #JEC not available yet
config["CORRMETONTHEFLY"] = False #JEC not available yet
config["GETJECFROMDBFILE"] = False # If not yet in global tag, but db file available
