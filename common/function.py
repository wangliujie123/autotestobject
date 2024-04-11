import os, configparser

#获取项目路径
def project_path():
    #print(os.path.split(os.path.realpath(__file__))[0])
    return os.path.split(os.path.realpath(__file__))[0].split('\\c')[0]

#返回config.ini文件的testurl
def config_url():
    config = configparser.ConfigParser()
    config.read(project_path()+"/config.ini")
    return config.get('testurl', 'url')

if __name__ == '__main__':
    print(project_path())
    print(config_url())