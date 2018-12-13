
class Pod:

#---------------------------------------------------------------

  def __init__(self):
    self.name = ""
    self.ready = False
    self.phase = ""
    self.ip = ""
    self.node = ""
    self.start = ""
    self.lastTransition = ""
    self.initConts = []
    self.conts = []

#---------------------------------------------------------------

  def __repr__(self):
    return "[{}, {}, {}, {}, {}, {}]".format(self.name, self.ready, 
      self.ip, self.node, self.start, self.lastTransition)

#---------------------------------------------------------------

  def getReady(self):
    total = len(self.initConts) + len(self.conts)
    ready = 0

    for i in self.initConts:
      if i.ready:
        ready += 1

    for i in self.conts:
      if i.ready:
        ready += 1

    return "{}/{}".format(ready, total)

#---------------------------------------------------------------

  def getLastTransition(self):
    return self.lastTransition[:-1].replace('T', ' ')

#---------------------------------------------------------------

  def getStatus(self):
    return "Ready" if self.ready else "Not Ready ({})".format(self.phase)

#---------------------------------------------------------------

  def getRestarts(self):
    rr = 0

    for i in self.initConts:
      rr += i.restarts

    for i in self.conts:
      rr += i.restarts

    return rr

#---------------------------------------------------------------


##############################################################

class Container:

#---------------------------------------------------------------

  def __init__(self):
    self.name = ""
    self.state = ""
    self.ready = False
    self.restarts = 0
    self.lastTransition = ""

#---------------------------------------------------------------

  def __repr__(self):
    return "[{}, {}, {}, {}, {}]".format(self.name, self.ready, 
      self.state, self.restarts, self.lastTransition)

#---------------------------------------------------------------

  def getLastTransition(self):
    return self.lastTransition[:-1].replace('T', ' ')

#---------------------------------------------------------------


