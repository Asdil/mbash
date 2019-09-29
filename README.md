# mbash
使用python3多进程运行.sh脚本
注意:需要安装python3
## 安装流程
```
   1. 复制./mbash.py 到任意路径比如: /software/mbash.py
   2. 修改~/.bashrc,添加下面的语句:
      alias mbash='python /software/mbash.py'
   3. source ~/.bashrc
```
## 运行命令
```
  假设你有一个test.sh文件,内容如下:
        touch 1.txt
        touch 2.txt
        touch 3.txt
  mbash -p test.sh (基本用法)
  mbash -p test.sh -t 8 (进程数)
```
