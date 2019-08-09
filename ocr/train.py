import torch.nn as nn
import torch.nn.functional as F 
import torch.optim as optim
import torch


def train(n_epochs,dataloader,net):
        
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.SGD(net.parameters(),lr = 0.001, momentum=0.9)
        running_loss = 0.0
        for epoch in range(n_epochs):
            for i, (inp, lables) in enumerate(dataloader, 0):
        #         inp = inp.to(device)
        #         lab = lab.to(device)
                
                # clear the gradients 
                optimizer.zero_grad()
                # forward pass
                outs = net(inp)
                # batch loss
                loss = criterion(outs, lables)
                # backward pass
                loss.backward()
                # perform optimization(parameter update)
                optimizer.step()

                running_loss += loss.item()
                if 50 % i == 49:
                    print(f'epoch : {epoch + 1}/{n_epochs}| data {i+1} | loss: {running_loss}')
                    running_loss = 0.0

        print('finished')
        torch.save(net.state_dict(),"mod.pt")