#!/usr/bin/python3
# coding=utf-8

import math
import os
import pickle
import platform
import shutil
import time
import requests
from io import StringIO, BytesIO

import psutil
from PIL import Image


class Base:
    separator = "/"

    # 根据操作系统类型，确定使用不同的分隔符
    def __init__(self):
        if Base.get_os_type().lower() == 'windows':
            Base.separator = '\\'
        elif Base.get_os_type().lower() == 'linux':
            Base.separator = '/'
        else:
            Base.separator = '/'

    # 输入文件路径
    # 返回文件是否存在
    @staticmethod
    def is_file_exist(filepath):
        return os.path.exists(filepath)

    # 输入目录路径
    # 返回目录是否存在
    @staticmethod
    def is_path_exist(path):
        return os.path.exists(path)

    # 输入文件全路径获得文件名称，不包含点和后缀名
    @staticmethod
    def get_file_name_without_extand_dot(filepath):
        return str(filepath).strip(Base.separator).split(Base.separator)[-1].split('.')[0]

    # 输入文件路径
    # 返回文件扩展名, 包含了点
    @staticmethod
    def get_file_ext_name_with_dot(filepath):
        return os.path.splitext(filepath)[1]

    # 输入文件路径
    # 返回文件扩展名, 不包含点
    @staticmethod
    def get_file_ext_name_without_dot(filepath):
        return os.path.splitext(filepath)[1].strip('.')

    # 输入文件路径
    # 返回文件路径, 不包括后缀名
    @staticmethod
    def get_file_path_without_dot_and_ext(filepath):
        return os.path.splitext(filepath)[0]

    # 输入文件路径
    # 获得文件目录
    @staticmethod
    def get_file_path(filepath):

        if Base.is_file_exist(filepath):
            filepath = filepath[0:filepath.rindex(Base.separator)]
            return filepath
        else:
            print("file is not exist [get_file_path]")
            return ""

    # 输入目录路径
    # 用来创建单个目录
    # 目录不存在, 则创建目录, 创建目录成功, 返回True
    @staticmethod
    def make_dir(dirpath):
        if not Base.is_path_exist(dirpath):
            try:
                os.mkdir(dirpath)
                return True
            except Exception as e:
                raise e
        else:
            return False

    # 输入目录路径
    # 用来创建多级目录
    # 目录不存在, 则创建目录, 创建目录成功, 返回True
    @staticmethod
    def make_dirs(dirpath):
        if not Base.is_path_exist(dirpath):
            try:
                os.makedirs(dirpath)
                return True
            except Exception as e:
                raise e
        else:
            return False

    # 输入源文件和目的文件路径
    # 目的地址, 不存在的话, 则自动创建响应的目录
    @staticmethod
    def copy_file(srcfilepath, dstfilepath):
        if Base.is_file_exist(srcfilepath):
            dirpath = Base.get_file_path(dstfilepath)
            if not Base.is_path_exist(dirpath):
                Base.make_dirs(dirpath)
            try:
                shutil.copy(srcfilepath, dstfilepath)
            except Exception as e:
                raise e

    # 输入目录
    # 返回文件和目录
    @staticmethod
    def list_files_and_folders(dirpath):
        if not os.path.isdir(dirpath):
            print('所提供路径不是目录, 或目录不存在')
            return []
        return os.listdir(dirpath)

    # 输入目录
    # 返回文件
    @staticmethod
    def list_files(dirpath):
        if not os.path.isdir(dirpath):
            print('所提供路径不是目录, 或目录不存在')
            return []
        return [x for x in os.listdir(dirpath) if (os.path.isfile(dirpath + '\\' + x))]

    # 输入目录
    # 返回指定后缀名的文件
    @staticmethod
    def list_files_by_ext_type(dirpath, exttype):
        if not os.path.isdir(dirpath):
            print('所提供路径不是目录, 或目录不存在')
            return []
        return [x for x in os.listdir(dirpath) if
                (os.path.isfile(dirpath + '\\' + x)) and (os.path.splitext(x)[1] == '.' + exttype)]

    # 输入目录
    # 返回目录
    @staticmethod
    def list_folders(dirpath):
        if not os.path.isdir(dirpath):
            print('所提供路径不是目录, 或目录不存在')
            return []
        return [x for x in os.listdir(os.path.abspath(dirpath)) if (os.path.isdir(dirpath + '\\' + x))]

    # 获取当前文件的路径
    @staticmethod
    def get_current_dir():
        return os.getcwd()
        # return os.path.abspath('.')

    # 获取当前文件的上级路径
    @staticmethod
    def get_current_parent_dir(dirpath):
        return os.path.abspath(os.path.dirname(dirpath) + os.path.sep + '.')

    # 获取当前文件的上上级路径
    @staticmethod
    def get_current_parent_x2_dir(dirpath):
        return os.path.abspath(os.path.dirname(dirpath) + os.path.sep + '..')

    # 返回当前全时间 2018/03/02 16:32:56
    @staticmethod
    def get_current_datetime():
        return time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))

    # 返回当前日期 2018/03/02
    @staticmethod
    def get_current_date():
        return time.strftime('%Y/%m/%d', time.localtime(time.time()))

    # 返回当前时间 16:32:56 24小时制
    @staticmethod
    def get_current_time():
        return time.strftime('%H:%M:%S', time.localtime(time.time()))

    # 创建StringIO
    # 返回StringIO()
    @staticmethod
    def create_stringio(*info):
        f = StringIO()
        for s in info:
            f.write(s)
        return f

    # 创建BytesIO
    # 返回BytesIO()
    @staticmethod
    def create_bytesio(*info):
        f = BytesIO()
        for s in info:
            f.write(s)
        return f

    # 输入bin文件路径
    # 返回bin读取内容 bytes
    @staticmethod
    def bin_reader(binpath):
        with open(binpath, 'rb') as f:
            return f.read()

    # 输入bin文件路径, 和要写入的相关内容 bytes
    # 写入bin文件
    @staticmethod
    def bin_writer(binpath, bcontent):
        with open(binpath, 'wb') as f:
            try:
                f.write(bcontent)
                return True
            except Exception as e:
                raise e

    # 文件读取, 文字编码按照UTF8
    # 返回文件读取内容
    @staticmethod
    def file_reader_by_utf8(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()

    # 文件读取, 文字编码默认
    # 返回文件读取内容
    @staticmethod
    def file_reader(filepath):
        with open(filepath, 'r') as f:
            return f.read()

    # 序列化, 加密过程
    # bytes -> bytes
    # 返回序列化(加密)之后的内容
    @staticmethod
    def enpickle_bytes_to_bytes(bytescontent):
        return pickle.dumps(bytescontent)

    # 序列化, 加密过程
    # file -> bytes
    # 返回序列化(加密)之后的内容
    @staticmethod
    def enpickle_file_to_bytes(filepath):
        with open(filepath, 'rb') as f:
            return pickle.dumps(f.read())

    # 输入要加密的文件路径和输出文件路径
    # file -> file
    # 直接将要序列化的文件进行序列化操作, 得到加密文件
    @staticmethod
    def enpickle_file_to_file(filepath, fileoutpath):
        with open(filepath, 'rb') as f:
            with open(fileoutpath, 'wb') as fout:
                pickle.dump(f.read(), fout)

    # 输入要加密的相关内容bytes和输出文件路径
    # bytes -> file
    # 直接将要序列化的内容进行序列化操作, 生成序列化之后的文件
    @staticmethod
    def enpickle_bytes_to_file(bytescontent, fileoutpath):
        with open(fileoutpath, 'wb') as fout:
            pickle.dump(bytescontent, fout)

    # 返序列化, 解密过程
    # bytes -> bytes
    # 返回解密后的内容 bytes
    @staticmethod
    def depickle_bytes_to_bytes(bytescontent):
        return pickle.loads(bytescontent)

    # 输入要解密的文件路径
    # file -> bytes
    # 直接将要反序列化的文件进行反序列化操作, 得到解密文件
    @staticmethod
    def depickle_file_to_bytes(filepath):
        with open(filepath, 'rb') as f:
            return pickle.loads(f.read())

    # 输入要解密的文件路径和输出文件路径
    # file -> file
    # 直接将要反序列化的文件进行反序列化操作, 得到解密文件
    @staticmethod
    def depickle_file_to_file(filepath, fileoutpath):
        with open(filepath, 'rb') as f:
            with open(fileoutpath, 'wb') as fout:
                fout.write(pickle.load(f))

    # 输入要解密的bytes和输出文件路径
    # bytes -> file
    # 直接将要反序列化的文件进行反序列化操作, 得到解密文件
    @staticmethod
    def depickle_bytes_to_file(bytescontent, fileoutpath):
        with open(fileoutpath, 'wb') as fout:
            fout.write(pickle.loads(bytescontent))

    # 获取操作系统类型
    # 返回值Windows + Linux
    @staticmethod
    def get_os_type():
        return platform.system()

    # 输入全路径和附件的名字，获得新文件的全路径
    @staticmethod
    def rename_file_by_appand_name(filepath, *appandname):

        if Base.is_file_exist(filepath):
            if len(appandname) == 1:
                return Base.get_file_path(filepath) + Base.separator + Base.get_file_name_without_extand_dot(
                    filepath) + str(appandname[0]) + Base.get_file_ext_name_with_dot(filepath)
            else:
                return Base.get_file_path(filepath) + Base.separator + Base.get_file_name_without_extand_dot(
                    filepath) + '_notset' + Base.get_file_ext_name_with_dot(filepath)
        else:
            print("file is not exist")

    # 用来缩小图片大小
    # 参数中可以设置输出参数，也可以不设置输出参数
    @staticmethod
    def zoom_out_image(filepath, *fileoutpath):
        if Base.is_path_exist(filepath):
            appandname = '_small'
            if len(fileoutpath) == 1:
                fileoutpath = Base.rename_file_by_appand_name(filepath, fileoutpath[0])
            else:
                fileoutpath = Base.rename_file_by_appand_name(filepath, appandname)

            im = Image.open(filepath)
            w, h = im.size
            im.thumbnail((w / 2, h / 2))  # 缩小到二分之一
            im.save(fileoutpath)
        else:
            print("file is not exist [zoom_out_image]")

    # 获取内存信息：返回结果取整 单位M
    @staticmethod
    def get_memory_total_by_m():
        mem = psutil.virtual_memory()
        return math.ceil(mem.total / 1024 / 1024)

    # 获取内存信息：返回结果取整 单位G
    @staticmethod
    def get_memory_total_by_g_and_result_is_int():
        mem = psutil.virtual_memory()
        return math.ceil(mem.total / 1024 / 1024 / 1024)

    # 获取内存信息：返回结果保留2位小数点，且四舍五入 单位G
    @staticmethod
    def get_memory_total_by_g():
        mem = psutil.virtual_memory()
        return round(mem.total / 1024 / 1024 / 1024, 2)

    # 获取可用内存 单位M
    @staticmethod
    def get_memory_available_by_m():
        mem = psutil.virtual_memory()
        return math.ceil(mem.available / 1024 / 1024)

    # 获取可用内存 单位G
    @staticmethod
    def get_memory_available_by_g():
        mem = psutil.virtual_memory()
        return round(mem.available / 1024 / 1024 / 1024, 2)

    # 获取使用率
    @staticmethod
    def get_memory_usage_rate():
        mem = psutil.virtual_memory()
        return mem.percent

    # 获取可用内存 单位M
    @staticmethod
    def get_memory_used_by_m():
        mem = psutil.virtual_memory()
        return math.ceil(mem.used / 1024 / 1024)

    # 获取可用内存 单位G
    @staticmethod
    def get_memory_used_by_g():
        mem = psutil.virtual_memory()
        return round(mem.used / 1024 / 1024 / 1024, 2)

    @staticmethod
    def get_cpu_cores():
        cpu = psutil.cpu_count()
        return cpu

    @staticmethod
    def get_cpu_physics_cores():
        cpu = psutil.cpu_count(logical=False)
        return cpu

    # 获取硬盘分区 mountpoint
    @staticmethod
    def get_disk_partitions():
        disk = psutil.disk_partitions()
        ds = []
        for d in disk:
            i = str(d).find('mountpoint=')
            ds.append(str(d)[i + len('mountpoint=') + 1: str(d).find('fstype=') - 3])
        return ds

    # 获取硬盘的等待时间：读 单位毫秒
    @staticmethod
    def get_disk_read_wait_time():
        dtime = psutil.disk_io_counters()
        return dtime.read_time

    # 获取硬盘的等待时间：写 单位毫秒
    @staticmethod
    def get_disk_write_wait_time():
        dtime = psutil.disk_io_counters()
        return dtime.write_time

class Http:

    separator = "/"

    # 根据操作系统类型，确定使用不同的分隔符
    def __init__(self):
        if Base.get_os_type().lower() == 'windows':
            Base.separator = '\\'
        elif Base.get_os_type().lower() == 'linux':
            Base.separator = '/'
        else:
            Base.separator = '/'

    @staticmethod
    def http_req_es_stat(url, *auth):
        pass