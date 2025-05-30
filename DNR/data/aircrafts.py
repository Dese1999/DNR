import numpy as np
import torch
from data.datasets import load_dataset, load_dataset_linear_eval


class Aircrafts:
    def __init__(self, cfg):

        if cfg.cs_kd:
            sampler_type = 'pair'
        else:
            sampler_type = 'default'
        if cfg.eval_linear:
            trainloader, valloader, testloader = load_dataset_linear_eval('Aircrafts',
                                              cfg.data,
                                              sampler_type, batch_size=cfg.linear_batch_size)
        else:
            trainloader, valloader, testloader = load_dataset('Aircrafts',
                                                              cfg.data,
                                                              sampler_type, batch_size=cfg.batch_size)

        self.num_classes = trainloader.dataset.num_classes

        self.train_loader = trainloader
        self.tst_loader = testloader
        self.val_loader = valloader