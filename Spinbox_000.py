from tkinter import *

def passwdgen(passVal: str):
    """
    This is a shell function that returns "spinbox deep dive".

    Args:
        passLen (int): password length - read from the spinbox

    Returns:
        string: "spinbox deep dive"
    """
    return "Passed Value: {}".format(passVal)


class GUI:
    """
    Handles the GUI interface mechanism
    """ 
    
    #####
    # def spinbox_valid(self, widget_name):
    #     """Returns whether the contents of the spinbox are valid

    #     Args:
    #         widget_name (str): the internal Tcl name of the spinbox

    #     Returns:
    #         boolean: contents are valid
    #     """
    #     try:
    #         user_input = self.passLen.get()
    #         valid = isinstance(user_input, int)
    #     except:
    #         valid = False
    #     # now that we've ensured the input is only integers, range checking!
    #     if valid:
    #         # get minimum and maximum values of the widget to be validated
    #         minval = int(self.root.nametowidget(widget_name).config('from')[4])
    #         maxval = int(self.root.nametowidget(widget_name).config('to')[4])
    #         # check if it's in range
    #         if int(user_input) not in range (minval, maxval):
    #             valid = False
    #     return valid
    #####    

    def GeneratePass(self):
        """
        Calls the function that generates a password and copies the same to the clipboard. 
        If there is an issue the password is cleared and the spinbox is reset
        """
 
        ##### Start: commented out in Spinbox_001.py
        # Call password generation function without validation
        generatedPass = passwdgen(
                self.passLen.get(), 
            )
        ##### End: commented out in Spinbox_001.py

        #####
        # Call password generation function after validation
        # if self.spinbox_valid('!spinbox'):
        #     generatedPass = passwdgen(
        #             self.passLen.get(), 
        #         )
        # else:
        #     # change focus to correct the invalid content of the spinbox
        #     generatedPass=''
        #     self.passLen.set(self.last_valid_passLen)
        #     self.root.focus()
        #####

        self.passText.set(value=generatedPass)
    
        
    #####
    # def ValidateIfNum(self, user_input, widget_name):
    #     """
    #     Args:
    #         user_input (str): The value typed into the spinbox
    #         widget_name (str): The widget name

    #     Returns:
    #         boolean: Whether the value is valid
    #     """
    #     valid = self.spinbox_valid(widget_name)
    #     if valid:
    #         self.last_valid_passLen = int(self.passLen.get())
            
    #     return valid
    #####

 
    #####
    # def reset_focus(self, event):
    #     """Validates whether the number is valid.  If it isn't it resets the value

    #     Args:
    #         event (event): Event being captured

    #     Returns:
    #         boolean: was spinbox content valid
    #     """
        
    #     valid = self.spinbox_valid('!spinbox')
        
    #     if not valid:
    #         self.passLen.set(self.last_valid_passLen)

    #     self.root.focus()
    #     return valid
    #####       


    def __init__(self, progname):
        """
        Draws the screen and sets up the GUI
        Manages the event for the Spinbox
        """        

        # Retains the last valid passLen in case it needs to be reset
        self.last_valid_passLen = 20
  
        # root window
        self.root = Tk()
        self.root.title("TKinter Spinbox Analysis - Code : {}".format(progname.split('\\')[-1]))
 
        #####
        # self.root.bind('<Return>', self.reset_focus)
        # self.root.bind('<Tab>', self.reset_focus)

        # registering validation handler
        # vldt_ifnum_cmd = (self.root.register(self.ValidateIfNum),'%P', '%W')
        #####
 
        # pass length information
        self.passTitle = Label(self.root, text = "Password Length: ").grid(row=0, column=0, padx=5, pady=5, sticky=E)
        self.passLen = IntVar(value=20)
        self.passLenSb = Spinbox(
            self.root, 
            textvariable=self.passLen, 
            from_=1, 
            to=100, 
            increment=1,
            
            #####
            # validate='focus', 
            # validatecommand=vldt_ifnum_cmd,
            #####
            
            width=5, 
            justify=CENTER, 
            bd=3
            ).grid(row=0, column=1, padx=5, pady=5)

        # pass length information
        self.genPassButton = Button(self.root, text = "Regenerate Password", command=self.GeneratePass).grid(row=8, column=0, padx=5, pady=5)
        generatedPass = passwdgen(
            self.passLen.get(), 
            )
        
        self.passText = StringVar(value=generatedPass)
        self.genPassText = Entry(self.root, width=50, bd=3, font=('Bold'), textvariable=self.passText).grid(row=8, column=1, padx=5, pady=5)


if __name__ == '__main__':
    mainwindow = GUI(__file__)
    mainloop()
    
  