import logging
import os
import log
from common.doConfig import DoConfig

ROOT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class GetLog():
    """
    日志类
    """

    def __init__(self,
                 section="LEVEL",
                 coOption="coLevel",
                 outOption="outLevel",
                 formatInfo="formatInfo",
                 name="interface_test",
                 fileName=os.path.join(log,"logger.log")):

        """
        coLevel为日志收集级别,outLevel为日志输出级别,formatInfo为日志输出格式，name为日志模块名，fileName为日志输出文件名
        :param section: 日志等级
        :param coOption:
        :param outOption:
        :param formatInfo:
        :param name:
        :param fileName:
        """

        self.jd_logger = logging.getLogger(name)     # 定义日志收集模块的名字
        read=DoConfig(ROOT_PATH + '/config/' + "log.cfg")  #初始化

        if not self.jd_logger.handlers:  # 解决打印重复日志问题
            coLevel=read.get_str(section,coOption)
            self.jd_logger.setLevel(coLevel)             # 日志收集级别
            self.jd_filter = logging.StreamHandler()     # 过滤器
            outLevel=read.get_str(section,outOption)
            self.jd_filter.setLevel(outLevel)            # 日志输出级别
            #self.jd_logger.addHandler(self.jd_filter)         # 收集器与过滤器对接
            fh=logging.FileHandler(fileName,"a",encoding="utf-8")
            self.jd_logger.addHandler(fh)                    #导入收集器的日志到文件
            formatInfo=read.get_str(section,formatInfo)
            formatter = logging.Formatter(formatInfo)
            #self.jd_filter.setFormatter(formatter)           #过滤器日志输出级别处理后输出到控制台
            fh.setFormatter(formatter)                  #收集器输出级别处理后输出到文件


    def logger(self):
        return self.jd_logger


if __name__=="__main__":
    path_project = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
    log_conf_path = os.path.join(path_project, "config", "log.cfg")
    logConfFilePath=log_conf_path
    logger = GetLog().logger()

    logger.debug("test")  # 使用日志级别看自己，特别严重就用critical，一般错误就用error
    logger.info("test")
    logger.warning("test")
    logger.error("test")
    logger.critical("test")