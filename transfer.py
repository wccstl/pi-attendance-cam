import yaml
import tempfile
import os
import sys

from datetime import datetime
from smb.SMBConnection import SMBConnection

config = yaml.safe_load(open(os.path.join(sys.path[0], "config.yml")))

conn = SMBConnection(config['UserID'], config['password'], config['client_machine_name'], config['server_name'])
assert conn.connect(config['server_ip'])

file_obj = tempfile.NamedTemporaryFile(delete=False)
file_attributes, filesize = conn.retrieveFile('Data', '/Group.jpg', file_obj)

file_obj.close()
