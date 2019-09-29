# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     setup
   Description :
   Author :        Asdil
   date：          2018/10/26
-------------------------------------------------
   Change Activity:
                   2019/5/21:
    version = 1.7.2.9
-------------------------------------------------
"""
import os
import subprocess
from multiprocessing import Pool
from argparse import ArgumentParser
from datetime import datetime
def mt(cmd):
    subprocess.check_call(cmd, shell=True)
def main():
    parser = ArgumentParser(description='多进程')
    parser.add_argument('-p', help='脚本路径',type=str, required=True)
    parser.add_argument('-t', help='并发数',type=int, default=8)
    args = parser.parse_args()

    star = datetime.now()

    # 检测文件是否存在
    assert os.path.exists(args.p), f'{args.p} 文件不存在'
    with open(args.p, 'r') as f:
        cmds = f.read().strip().split('\n')

    pool = Pool(args.t)
    pool.map(mt, cmds)
    pool.close()
    pool.join()
    end = datetime.now()
    print('开始时间: {star}')
    print('结束: {end}')
    print(f'一共{len(cmds)}条命令')

if __name__ == '__main__':
    main()
