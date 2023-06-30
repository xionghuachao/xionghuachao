#coding=utf-8
import yaml
from common.tools import get_project_path,sep
class GetConf:
    def load_file(self,file):
        with open(file,'r',encoding='utf-8') as env_file:
            self.env=yaml.load(env_file,Loader=yaml.FullLoader)
            return self.env



if __name__=='__main__':
    print(GetConf().get_url())

