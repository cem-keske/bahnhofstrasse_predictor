import torch
import torch.nn as nn
import lightning as L

class RegressorModule(L.LightningModule):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(17, 128, dtype=torch.float64),
            nn.ReLU(),
            nn.Linear(128, 32, dtype=torch.float64),
            nn.ReLU(),
            nn.Linear(32, 4, dtype=torch.float64),
            nn.ReLU(),
            nn.Linear(4, 1, dtype=torch.float64),
        )
        self.loss = nn.MSELoss()

    def training_step(self, batch, batch_idx):
            x, y = batch
            # print(x.dtype, y.dtype)
            y_hat = self.layers(x)
            # print(y_hat.dtype)
            l = self.loss(y_hat, y)
            self.log('train_loss', l, on_epoch=True, prog_bar=True)
            return l

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=1e-3)
        return optimizer
