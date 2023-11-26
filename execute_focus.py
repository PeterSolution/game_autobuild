class focus:
    def __init__(self):
        self.focusOrder=[]
    def  addfocus(self,focus):
        self.focusOrder.append(focus)
    def resetfocus(self):
        for i in self.focusOrder:
            self.focusOrder[i]=""
    def returnfocus(self):
        return self.focusOrder