import FWCore.ParameterSet.Config as cms
from UHH2.core.ntuple_generator import generate_process  # use CMSSW type path for CRAB
from UHH2.core.optionsParse import setup_opts, parse_apply_opts


"""NTuple config for Run3 Data datasets.

You should try and put any centralised changes in generate_process(), not here.
"""

print("before process")
process = generate_process(year="2023", useData=True)
print("after process")

# Please do not commit changes to source filenames - used for consistency testing
process.source.fileNames = cms.untracked.vstring([
    '/store/data/Run2023C/JetMET0/MINIAOD/PromptReco-v1/000/367/515/00000/fe66957b-00da-49be-9e1f-42f88cf70345.root' 
])

# Do this after setting process.source.fileNames, since we want the ability to override it on the commandline
options = setup_opts()
parse_apply_opts(process, options)

with open('pydump_data_2023.py', 'w') as f:
    f.write(process.dumpPython())
