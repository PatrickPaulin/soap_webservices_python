#!/usr/bin/python3
import os
from data import Data
from webservices import SendForm
from state_machine import StateMachine

# Instances
form = SendForm()
data = Data()

class Ativacao():
    def start_transitions(self):
        if data.getFlow() == "normal":
            return "init"
        else:
            return "finish"

    def init_handler(self):
        # Send form to activation first step
        if form.sendStart() is None:
            newState = "error_state"
        else:
            newState = "check_init"
        return newState

    def check_init_handler(self):
        input("Press enter to continue:")
        return "midle"

    def midle_handler(self):
        if form.sendMidle() is None:
            newState = "error_state"
        else:
            newState = "finish"
        return newState

    def finish_handler(self):
        if form.sendFinish() is None:
            newState = "error_state"
        else:
            newState = "check_finish"
        return newState

    def check_finish_handler(self):
        return "error_state"

    def start_activation(self):
        m = StateMachine()
        m.add_state("Start", self.start_transitions)
        m.add_state("init", self.init_handler)
        m.add_state("check_init", self.check_init_handler)
        m.add_state("midle", self.midle_handler)
        m.add_state("finish", self.finish_handler)
        m.add_state("check_finish", self.check_finish_handler)
        m.add_state("error_state", None, end_state=1)
        m.set_start("Start")
        m.run()
   
    def __init__(self):
        pass