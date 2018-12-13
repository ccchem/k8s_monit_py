from k8s.model import Pod, Container

def parse_pods(data):
  pods = []
  
  for i in data['items']:
    p = Pod()

    # Metadata
    p.name = i['metadata']['name']
    p.node = i['spec']['nodeName']

    # Pod stats
    stat = i['status']
    p.phase = stat['phase']
    p.ip = stat['podIP']
    p.start = stat['startTime']
    p.ready, p.lastTransition = parse_pod_ready(stat)

    # Init containers stats
    if 'initContainerStatuses' in stat:
      icStats = stat['initContainerStatuses']
      p.initConts = parse_containers(icStats)

    # Regular containers stats
    cStats = stat['containerStatuses']
    p.conts = parse_containers(cStats)

    pods.append(p)

  return pods


############################################################


def parse_pod_ready(status):
  lstTran = ""
  ready = False

  for i in status['conditions']:
    lstTran = i['lastTransitionTime']

    if i['type'] == "Ready":
      ready = (i['status'].lower() == 'true')
      return (ready, lstTran)
  
  return (ready, lstTran)


############################################################


def parse_containers(data):
  conts = []

  for i in data:
    c = Container()

    c.name = i['name']
    c.restarts = i['restartCount']
    c.ready = i['ready']
    c.state, c.lastTransition = parse_cont_state(i['state'])
    if c.lastTransition == '':
      tmp, c.lastTransition = parse_cont_state(i['lastState'])

    conts.append(c)

  return conts


############################################################


def parse_cont_state(state):
  lst = list(state)
  if not lst:
    return ("", "")

  stKey = lst[0]
  val = state[stKey]

  stName = stKey.capitalize()
  if 'reason' in val:
    stName = "{} ({})".format(stName, val['reason'])

  lstTran = ""
  if 'finishedAt' in val:
    lstTran = val['finishedAt']
  elif 'startedAt' in val:
    lstTran = val['startedAt']

  return (stName, lstTran)

