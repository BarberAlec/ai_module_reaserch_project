import torch
from torch.nn import Linear, ReLU, CrossEntropyLoss, Sequential, Conv2d, MaxPool2d, MaxUnpool2d, Module, Softmax, BatchNorm2d, Dropout
from Othello import othello
class OthelloCNN(othello.ai):
    def __init__(self,marker):
        self.name = "CNN_ai"
        self.marker = marker
        # Presuming pkl file is in current directory
        self.learner = load_learner('.', file = 'model.pkl')

        self.conv1 = Sequential(
            Conv2d(2, 64, kernel_size=3, padding=0, stride=1),
            BatchNorm2d(64),
            ReLU() )

        self.conv2 = Sequential(
            Conv2d(64, 64, kernel_size=3, padding=0, stride=1),
            BatchNorm2d(64),
            ReLU())

        self.conv3 = Sequential(
            Conv2d(64, 128, kernel_size=3, padding=0, stride=1),
            BatchNorm2d(128),
            ReLU())

        self.conv4 = Sequential(
            Conv2d(128, 128, kernel_size=3, padding=0, stride=1),
            BatchNorm2d(128),
            ReLU())

        self.conv5 = Sequential(
            Conv2d(128, 256, kernel_size=3, padding=0, stride=1),
            BatchNorm2d(256),
            ReLU())

        self.conv6 = Sequential(
            Conv2d(254, 256, kernel_size=3, padding=0, stride=1),
            BatchNorm2d(256),
            ReLU())

        self.conv7 = Sequential(
            Conv2d(256, 256, kernel_size=3, padding=0, stride=1),
            BatchNorm2d(256),
            ReLU())

        self.fc1 = Linear( 256 * 8 * 8, 128 )

        self.fc2 = Linear( 128, 60 )

    def forward(self, x):

        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.conv5(x)
        x = self.conv6(x)
        x = self.conv7(x)
        x = self.fc1(x)
        x = self.fc2(x)

        return x

    def getMove(self, board):
        move = self.learner.predict(board)
        return [move[0],move[1]]