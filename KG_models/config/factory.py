import numpy as np
import tensorflow as tf
import pickle

class Factory(object):
    def __init__(self, config):
        self.config = config
        self.fingerprint_path = self.config.fingerprint_path
        self.entity_path = self.config.entity_path

    def embedding_def(self):

        with open(self.fingerprint_path, 'rb') as f:
            fingerprint_embedding = pickle.load(f)

        with open(self.entity_path, 'r') as f:
            id = f.read().split('\n')
        ids = []
        for i in id:
            ids.append(int(i.split('\t')[0]))
            cid_ids = ids[1:1081]  #only CID not mol_id

        cid_embedding = []
        for i in cid_ids:
            for k, v in fingerprint_embedding.items():
                if k == i:
                    cid_embedding.append(fingerprint_embedding[k])
        cid_embedding = np.array(cid_embedding)

        #Initializing mol_embedding
        mol_embedding = np.zeros((750, 2048)) # 750 = # of mol_id / 2048 = fingerprint shape

        ent_embedding = np.concatenate((cid_embedding,mol_embedding))

        #convert np to tensor
        sess = tf.Session()
        with sess.as_default():
            tensor = tf.constant(ent_embedding, name="ent_embeddings", dtype= tf.float32)
        return tensor


    # def load_fingerprint(self):
    #     with open(self.fingerprint_path, 'rb') as f:
    #         self.fingerprint_embedding = pickle.load(f)
    #     return self.fingerprint_embedding
    #
    # def get_cid_entity_id(self):
    #     with open(self.entity_path, 'r') as f:
    #         self.id = f.read().split('\n')
    #     self.ids = []
    #     for i in self.id:
    #         self.ids.append(int(i.split('\t')[0]))
    #         self.cid_ids = self.ids[1:1081]
    #     return self.cid_ids  #return only cid entity_id
    #
    # def embedding_def(self):
    #     self.cid_embedding = []
    #     for i in self.cid_ids:
    #         for k, v in self.fingerprint_embedding.items():
    #             if k == i:
    #                 self.cid_embedding.append(self.fingerprint_embedding[k])
    #     self.cid_embedding = np.array(self.cid_embedding)
    #     self.mol_embedding = np.zeros((750,2048))# 750 = # of mol_id / 2048 = fingerprint shape
    #     self.ent_embeeding = np.concatenate((self.cid_embedding,self.mol_embedding))
    #     sess = tf.Session()
    #     with sess.as_default():
    #         self.tensor = tf.constant(self.ent_embedding, name="ent_embeddings")
    #     return self.tensor