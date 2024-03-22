import torch
import torch.nn as nn
import lightning as L
class RegressorModule(L.LightningModule):
    def __init__(self):
        super().__init__()
        self.l1 = nn.Linear(60, 128)
        self.l2 = nn.Linear(128, 32)
        self.l3 = nn.Linear(32, 4)
        self.l4 = nn.Linear(4, 1)
        self.loss_fn = nn.MSELoss()
    def training_step(self, batch, batch_idx):
        x = self.l1(batch)
        x = nn.functional.relu(x)
        x = self.l2(x)
        x = nn.functional.relu(x)
        x = self.l3(x)
        x = nn.functional.relu(x)
        x = self.l4(x)
        r
    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=1e-3)
        return optimizer
