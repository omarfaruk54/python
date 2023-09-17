class studentIDcard:
    name       = ""
    roll       = ""
    depertment = ""
    session    = ""
    def display (self):
        print(f"name:{self.name}\nRoll:{self .roll}\ndepertment:{self.depertment}\nsession:{self.session}")
obi = studentIDcard()
obi.name ="omar"
obi.roll = 483784
obi.depertment = "cmt"
obi.session = "19-20"
obi.display()
