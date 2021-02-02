import os
import logging
import hydra
from solver import main
from omegaconf import OmegaConf, DictConfig

log = logging.getLogger(__name__)

@hydra.main(config_name="conf/conf.yaml")
def run_experiment(cfg: DictConfig) -> None:
    # print(OmegaConf.to_yaml(cfg))
    
    # read params
    p = cfg.solver.penalty
    nV = cfg.solver.num_vehicle
    num_fss = cfg.solver.first_solution_strategy.num_fss
    
    ds, td, tl = main(p, nV, num_fss)
    print("Dropped nodes  :", ds)
    print("Total distance :", td)
    print("Total load     :", tl)

    log.info("Dropped nodes  :{}".format(ds))
    log.info("Total distance :{}".format(td))
    log.info("Total load     :{}".format(tl))

if __name__ == '__main__':
    run_experiment()