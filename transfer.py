import yaml
import os
import sys

from datetime import datetime
from shutil import rmtree
from smb.SMBConnection import SMBConnection

config = yaml.safe_load(open(os.path.join(sys.path[0], 'config.yml')))
today_dir = '/Attendance/' + datetime.now().strftime('%Y') + '/' + datetime.now().strftime('%Y-%m-%d')
pics_dir = os.path.join(sys.path[0], 'pics-' + datetime.now().strftime('%Y-%m-%d') + '/')

conn = SMBConnection(config['UserID'], config['password'], config['client_machine_name'], config['server_name'])
assert conn.connect(config['server_ip'])

try:
    conn.listPath('Data', today_dir)
except:
    conn.createDirectory('Data', today_dir)

for picfile in os.listdir(pics_dir):
    with open(pics_dir + picfile, 'rb') as jpgfile:
        file_stored = conn.storeFile('Data', today_dir + '/' + picfile, jpgfile)

print('File transfer complete!')
conn.close()

if config['delete_pics']:
    rmtree(pics_dir)
