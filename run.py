shipsdir='/home/hongy0a/work/shipsdata/'
ptaorepo='/home/hongy0a/work/ships/TAO/build/install/'
import sys
sys.path.append(ptaorepo+"/python")
import ptao
# algo type choice, LM, SLM, SGD, Adam
algo_type = ptao.learn.Algo_type
ptao.la.Context.create([],[0])
learn = ptao.learn.lapack.LearnSlopeBased(shipsdir+"config_test.json",sys_file=shipsdir+"sysParams.json", \
 atm_file = shipsdir+"atmParams.json", dev = [0], data_file = shipsdir+"sys-input.fits")
learn.update_target_cmm("tomo")
learn.update_atm(shipsdir+"atminit.json")
score = learn.score()
print("score value is ", score)
#learn.fit()
