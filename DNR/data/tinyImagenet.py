import numpy as np
import torch
from data.datasets import load_dataset, load_dataset_linear_eval


class tinyImagenet_full:
    def __init__(self, cfg):

        if cfg.cs_kd:
            sampler_type = 'pair'
        else:
            sampler_type = 'default'

        if cfg.eval_linear:
            trainloader, valloader = load_dataset_linear_eval('tinyImagenet_full',
                                                              cfg.data,
                                                              sampler_type, batch_size=cfg.linear_batch_size)
        else:
            trainloader, valloader = load_dataset('tinyImagenet_full',
                                                              cfg.data,
                                                              sampler_type, batch_size=cfg.batch_size)


        self.num_classes = trainloader.dataset.num_classes

        self.train_loader = trainloader
        self.tst_loader = valloader
        self.val_loader = valloader


class tinyImagenet_val:
    def __init__(self, cfg):

        if cfg.cs_kd:
            sampler_type = 'pair'
        else:
            sampler_type = 'default'

        trainloader, valloader = load_dataset('tinyImagenet_val',
                                                cfg.data,
                                                sampler_type, batch_size=cfg.batch_size)
        self.num_classes = trainloader.dataset.num_classes

        self.train_loader = trainloader
        self.tst_loader = valloader
        self.val_loader = valloader