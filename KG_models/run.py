import sys
sys.path.append('/home/junyoung/workspace/MOA/OpenKE')
import config
import models

data_path = '/home/junyoung/workspace/MOA/dataset3/'
result_path = '/home/junyoung/workspace/MOA/result/'
log_path = result_path + 'res_tranH/log3.log'
model_name = 'TransH'
pre_trained = False
con = config.Config(log_path, model_name,pre_trained)
con.set_in_path(data_path)

con.set_work_threads(4)
con.set_train_times(1000)
con.set_nbatches(50)
con.set_alpha(0.001)
con.set_margin(1.0)
con.set_bern(0)
con.set_dimension(2048)
con.set_ent_neg_rate(1)
con.set_rel_neg_rate(0)
con.set_opt_method("adam")
#con.set_early_stopping((30,0.5))

# #train
# #TranE
# #Models will be exported via tf.Saver() automatically.
# con.set_log_path(result_path + 'res_tranE/log.log')
# con.set_model_name('TransE')
# con.set_export_files(result_path + "res_tranE/model_1.vec.tf", 0)
# #Model parameters will be exported to json files automatically.
# con.set_out_files(result_path + "res_tranE/embedding_1.vec.json")
# #Initialize experimental settings.
# con.init()
# #Set the knowledge embedding model
# con.set_model(models.TransE)
# #Train the model.
# con.run()

#TranH
#con.set_log_path(result_path + 'res_tranH/log.log')
con.set_export_files(result_path + "res_tranH/model_3.vec.tf", 0)
#con.set_model_name('TransH')
con.set_out_files(result_path + "res_tranH/embedding_3.vec.json")
con.init()
con.set_model(models.TransH)
con.run()

#
# #HoIE
# con.set_log_path(result_path + 'res_tranH/log.log')
# con.set_export_files(result_path + "res_HolE/model_1.vec.tf", 0)
# con.set_out_files(result_path + "res_HoIE/embedding_1.vec.json")
# con.init()
# con.set_model(models.HolE)
# con.run()
#
# #ComplEx
# con.set_export_files(result_path + "res_ComplEx/model_1.vec.tf", 0)
# con.set_out_files(result_path + "res_ComplEx/embedding_1.vec.json")
# con.init()
# con.set_model(models.ComplEx)
# con.run()
#
# #TranD
# con.set_export_files(result_path + "res_TransD/model_1.vec.tf", 0)
# con.set_out_files(result_path + "res_TransD/embedding_1.vec.json")
# con.init()
# con.set_model(models.TransD)
# con.run()
#
# #TranR
# con.set_export_files(result_path + "res_TransR/model_1.vec.tf", 0)
# con.set_out_files(result_path + "res_TransR/embedding_1.vec.json")
# con.init()
# con.set_model(models.TransR)
# con.run()
#
# #DisMult
# con.set_export_files(result_path + "res_DisMult/model_1.vec.tf", 0)
# con.set_out_files(result_path + "res_DisMult/embedding_1.vec.json")
# con.init()
# con.set_model(models.DisMult)
# con.run()
#
# #RESCAL
# con.set_export_files(result_path + "res_RESCAL/model_1.vec.tf", 0)
# con.set_out_files(result_path + "res_RESCAL/embedding_1.vec.json")
# con.init()
# con.set_model(models.RESCAL)
# con.run()




# con.set_in_path(data_path)
# con.set_test_flag(True)
# con.set_work_threads(4)
# con.set_dimension(100)
# con.set_import_files("./res_1/model_1.vec.pt")
# con.init()
# con.set_model(models.TransE)
# icon.test()
#


# ### test
# con.test()
# con.predict_head_entity(152, 9, 5)
# con.predict_tail_entity(151, 9, 5)
# con.predict_relation(151, 152, 5)
# con.predict_triple(151, 152, 9)
# con.predict_triple(151, 152, 8)
# #con.show_link_prediction(2,1)
# #con.show_triple_classification(2,1,3)