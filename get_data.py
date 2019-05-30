import pandas as pd
import pickle
import sys
import time
from multiprocessing.pool import Pool
from rdkit import Chem
from rdkit.Chem.rdmolops import RDKFingerprint
import pubchempy as pcp
from tqdm import tqdm


protein_protvec_embedding_path = '/home/junyoung/workspace/BioAssay/data/provec_embedding_norm.pkl'
Drugbank_path = '/home/junyoung/workspace/MOA/DrugBank/moa_20190207(approved_cid)_action_merge(40).csv'
fingerprint_path = '/dataset/virtual_screening/compounds/compound_fp_dicts.pkl'

with open(protein_protvec_embedding_path, 'rb') as f:
    protvec_embedding = pickle.load(f)
protvec_key = list(protvec_embedding.keys())

with open(fingerprint_path, 'rb') as f:
    fingerprint = pickle.load(f)

fingerprint_key = list(fingerprint.keys())

df_drugbank = pd.read_csv(Drugbank_path)

mol_id_unique = list(df_drugbank['mol_id'].unique())
CID = list(df_drugbank['CID'])
CID_unique = list(df_drugbank['CID'].unique())
match_mol = set(mol_id_unique) & set(protvec_key)
match_CID = set(CID_unique) & set(fingerprint_key)

print('mol_id', len(mol_id_unique))
print('CID', len(CID))
print('matching_mol_id', len(match_mol))
print('matching_CID', len(match_CID))


fingerprint_key = set(fingerprint_key)
match_index = [i for i, item in enumerate(CID) if item in fingerprint_key]
match_item = [item for i, item in enumerate(CID_unique) if item in fingerprint_key]
print(len(match_index))
##Truly, total data is 4533, but # of fingerprint that we have is 4052

df_drugbank_cid = df_drugbank.iloc[match_index]
CID_match = list(df_drugbank_cid['CID'].unique())

df_drugbank_cid.to_csv('/home/junyoung/workspace/MOA/DrugBank/moa_20190207(approved_cid)_action_merge(40)_fingerprintmatching.csv')

fingerprint_drugbank = {}
for k,v in tqdm(fingerprint.items()):
    if k in CID_match:
        fingerprint_drugbank[k] = v

##Save
with open('/dataset/virtual_screening/compounds/compound_fp_dicts_Drugbank.pkl', 'wb') as f:
    pickle.dump(fingerprint_drugbank, f)
df_drugbank_cid.to_csv('/home/junyoung/workspace/MOA/DrugBank/moa_20190207(approved_cid)_action_merge(40)_fingerprintmatching.csv')







##get fingerprint##
#But Pumchempy doesn't have smiles in Drugbank.

# def get_smiles(cid):
#     no_error = True
#     while no_error:
#         try:
#             _smiles = pcp.Compound.from_cid(int(cid)).to_dict()['canonical_smiles']
#             print(cid, _smiles)
#             return cid, _smiles
#         except Exception as e:
#             #print(e, cid)
#             time.sleep(3)
#             no_error = False
#
# if __name__ == '__main__':
#     pool = Pool(processes=20)
#     smiles_dict = {}
#     for p in pool.imap(get_smiles, CID):
#         if len(smiles_dict) % 20 == 0:
#             sys.stdout.write('\r %d / %d' % (len(smiles_dict), len(CID)))
#         print(p)
#         try:
#             cid, smiles = p
#             smiles_dict[cid] = smiles
#         except:
#             continue
#     #for cid in CID:
#     #    get_smiles(cid)
#
#
#     print(len(smiles_dict))
#     with open('/dataset/virtual_screening/compounds/canonical_smiles/smiles_dict_Drugbank.pkl', 'wb') as f:
#         pickle.dump(obj=smiles_dict, file=f)
#
#
#
#     strings = {}
#     for k, v in tqdm(smiles_dict.items()):
#         try:
#             ms = Chem.MolFromSmiles(v)
#             fp = RDKFingerprint(ms, minSize=2048, fpSize=2048)
#             strings[k] = fp.ToBitString()
#         except:
#             continue
#
# #print(len(strings))
#
#     with open('/dataset/virtual_screening/compounds/compound_fp_dicts_Drugbank.pkl', 'wb') as f:
#         pickle.dump(strings, f)