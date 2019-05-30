import pandas as pd
import numpy as np
import pickle
import sys
from tqdm import tqdm

Drugbank_path = '/home/junyoung/workspace/MOA/DrugBank/moa_20190207(approved_cid)_action_merge(40)_fingerprintmatching.csv'

df = pd.read_csv(Drugbank_path)

##generate entity
CID = list(df['CID'])
CID_unique = list(df['CID'].unique())
CID_id = list(range(len(CID_unique)))  ##CID 1080개
mol = list(df['mol_id'])
mol_unique = list(df['mol_id'].unique())

entity = CID_unique + mol_unique
entity_id = list(range(len(entity)))

all_entity = pd.DataFrame(np.column_stack([entity, entity_id]), columns=['entity', 'id'])

##generate relation
action_unique = list(df['action'].unique())
action_id = list(range(len(action_unique)))

all_action = pd.DataFrame(np.column_stack([action_unique, action_id])
                          , columns=['action', 'id'])

##gernerate triple set
triple_set = df[['CID', 'mol_id', 'action']]

#triple_set['CID_id'] = pd.merge(triple_set, all_entity)
only_CID = all_entity[0:len(CID_unique)]
only_CID.rename(columns={'entity': 'CID','id': 'CID_id'}, inplace = True)
only_mol = all_entity[len(CID_unique):len(all_entity)]
only_mol.rename(columns={'entity': 'mol_id','id':'mol_id_id'}, inplace = True)

triple_set = pd.merge(triple_set,only_CID)
triple_set = pd.merge(triple_set,only_mol)
triple_set = pd.merge(triple_set,all_action)

##Save
all_entity.to_csv('/home/junyoung/workspace/MOA/DrugBank/entity2id_2.csv')
all_action.to_csv('/home/junyoung/workspace/MOA/DrugBank/relation2id_2.csv')
triple_set.to_csv('/home/junyoung/workspace/MOA/DrugBank/total_id_2.csv')
