#!/usr/bin/python
# -*-coding:utf-8-*-
import sys


class webserver(object):
    def __init__(self,host,port):
        self.host =host
        self.port = port

    def start(self):
        print('server is  starting....')

    def stop(self):
        print('server is sotp......')

    def restart(self):
        self.stop()
        self.start()

def test_run(name):
    print("test runing......",name )


if __name__ == '__main__':
    server = webserver('localhost',3306)
    #print(sys.argv[1])
    # if sys.argv[1] == 'start':
    #     server.start()
    '''
    cmd_dic = {
        'start': server.start,
        'stop': server.stop,
    }
    if sys.argv[1] in cmd_dic:
        cmd_dic[sys.argv[1]]()
    
    '''
if  hasattr(server,sys.argv[1]):
    func = getattr(server,sys.argv[1])      #获取server.start 的内存地址
    func()  #server.start()

    # setattr(server,'run',test_run)
    # server.run('alex')
    # delattr(webserver,"start")
    # print(server.restart())
