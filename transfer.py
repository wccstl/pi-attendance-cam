import yaml
import os
import sys

from datetime import datetime
from smb import smb_structs
from smb.SMBConnection import SMBConnection

config = yaml.safe_load(open(os.path.join(sys.path[0], 'config.yml')))
today_dir = '/Attendance/' + datetime.now().strftime('%Y') + '/' + \
            datetime.now().strftime('%Y-%m-%d')
pics_dir = os.path.join(sys.path[0],
                        'pics-' + datetime.now().strftime('%Y-%m-%d') + '/')
try_again = []


def store_files_on_server(dir):
    for picfile in os.listdir(dir):
        picfile_location = dir + picfile
        with open(picfile_location, 'rb') as jpgdata:
            bytes_stored = conn.storeFile('Data',
                                          today_dir + '/' + picfile,
                                          jpgdata)
            if bytes_stored == os.path.getsize(picfile_location):
                # File sizes are the same. Delete file, if configured to do so.
                if config['delete_pics']:
                    os.remove(picfile_location)
            else:
                # File sizes are different. Add to try_again[]
                try_again.append(picfile)


conn = SMBConnection(config['UserID'],
                     config['password'],
                     config['client_machine_name'],
                     config['server_name'])
assert conn.connect(config['server_ip'])

try:
    conn.listPath('Data', today_dir)
except smb_structs.OperationFailure:
    conn.createDirectory('Data', today_dir)

store_files_on_server(pics_dir)

if len(try_again) == 0:
    print('File transfer complete!')
    conn.close()
    if config['delete_pics']:
        os.rmdir(pics_dir)
else:
    print('File transfer incomplete! Attempting to transfer %d files...'
          % (len(try_again)))
    try_again = []
    store_files_on_server(pics_dir)
