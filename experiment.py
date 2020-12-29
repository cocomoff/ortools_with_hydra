import os
import hydra
from solver import main
from omegaconf import OmegaConf

@hydra.main(config_name="conf/default.yaml")
def run_experiment(cfg):
    print(OmegaConf.to_yaml(cfg))
    ds, td, tl = main(cfg.solver.penalty, cfg.solver.num_vehicle)
    print("Dropped nodes  :", ds)
    print("Total distance :", td)
    print("Total load     :", tl)
    
    # output
    # print(f'Current working directory: {os.getcwd()}')
    # print(f'Orig working directory : {hydra.utils.get_original_cwd()}')
    # print(f'to_absolute_path("foo") : {hydra.utils.to_absolute_path("foo")}')
    # print(f'to_absolute_path("/foo") : {hydra.utils.to_absolute_path("/foo")}')

if __name__ == '__main__':
    run_experiment()