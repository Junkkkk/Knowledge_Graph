setwd("C://Users//PARK//PycharmProjects//DOAI//MOA//DrugBank")

data = read.csv("moa_20190207(approved_cid)_action_merge(40).csv")

table(data$action)

##Generate entities
length(table(data$CID))
length(table(data$mol_id))



intersect(data$CID, data$mol_id)

CID <- unique(data$CID)
CID <- paste0("CID_",CID)

mol <- unique(data$mol_id)
mol <- paste0("mol_",mol)

entities <- c(CID,mol)
entities_id <- c(1:length(entities))-1

all_entities <- data.frame(entities, entities_id)

write.csv(all_entities,"entities2id_2.csv")

##Generate relations
length(table(data$action))

action <- unique(data$action)
action_id <- c(1:length(action))-1

all_action <- data.frame(action, action_id)

write.csv(all_action,"relationid_2.csv")

##Generate (e1,e2,r)
tri_set <- data.frame(data$CID,data$mol_id,data$action)
colnames(tri_set) <- c("CID","mol","action")

CID <- unique(data$CID)
CID_id <- c(1:length(CID))-1
all_CID <- data.frame(CID,CID_id)

mol <- unique(data$mol)
mol_id <- c(1233:2044)
all_mol <- data.frame(mol,mol_id)



base_CID <- merge(all_CID, tri_set, by = 'CID')
base_CID_mol <- merge(all_mol, base_CID, by = 'mol')
base_CID_mol_action <- merge(all_action, base_CID_mol, by = "action")
train_id <- base_CID_mol_action[,c('CID_id','mol_id','action_id')]


write.csv(train_id,'train_id_2.csv')


##Split Train / Test
setwd("C://Users//PARK//PycharmProjects//DOAI//MOA//DrugBank")

set <- read.csv('train_id_2.csv')
set <- set[,-1]

smp_size <- floor(0.9 * nrow(set))
set.seed(123)
train_ind <- sample(seq_len(nrow(set)), size = smp_size)

train <- set[train_ind, ]
test <- set[-train_ind,]

smp_size <- floor(0.9 * nrow(train))
set.seed(120)
train_ind <- sample(seq_len(nrow(train)), size = smp_size)
train <- set[train_ind, ]
valid <- set[-train_ind,]

write.csv(train,'train_id_1.csv')
write.csv(valid,'valid_id_1.csv')
write.csv(test,'test_id_1.csv')


