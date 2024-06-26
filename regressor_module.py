import torch
import torch.nn as nn
import lightning as L
from torch import torchvision
class RegressorModule(L.LightningModule):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(16, 128, dtype=torch.float64),
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
    def test_step(self, batch, batch_idx):
        # this is the test loop
        x, y = batch
        x = x.view(x.size(0), -1)
        z = self.encoder(x)
        x_hat = self.decoder(z)
        test_loss = self.mse_loss(x_hat, x)
        self.log("test_loss", test_loss)