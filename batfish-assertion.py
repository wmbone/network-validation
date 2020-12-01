import pandas as pd
from pybatfish.client.commands import *
from pybatfish.datamodel import Edge, Interface
from pybatfish.datamodel.answer import TableAnswer
from pybatfish.datamodel.flow import (HeaderConstraints, PathConstraints)
from pybatfish.question import bfq, load_questions


# batfish host
bf_session.host = "localhost"
load_questions()


bf_set_network('neteng-lab')
bf_init_snapshot('/home/lab/repos/network-ci-pipeline/batfish-snapshots', name='neteng-lab', overwrite=True)


pd.set_option('display.min_rows', 400)
pd.set_option('display.max_rows', 400)


bgpSessStat = bfq.bgpSessionStatus(nodes='vmx-01', remoteNodes='vmx-02', status='Established').answer().frame()
print(bgpSessStat)


bgpSessStat[bgpSessStat.Established_Status == "ESTABLISHED"]
assert len(bgpSessStat[bgpSessStat.Established_Status == "ESTABLISHED"]) == 1, "BGP session Down"
        