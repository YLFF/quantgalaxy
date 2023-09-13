
import logging
import argparse

class Config:
    def __init__(self) :
        self._config={}
        self.data_sources = {
            'wind': {'api_key': 'your_api_key', 'endpoint': 'some_endpoint'},
            'ths': {'username': 'your_username', 'password': 'your_password'}
        }
        self._parse_args()
    def _parse_args(self):
        parser=argparse.ArgumentParser()
        
        parser.add_argument('--debug',action='store_true',help='debug mode',default=True)
        parser.add_argument('--active_data_source',type=str,help='激活的数据源',choices=self.data_sources.keys(),default='ths')
        
        '''other args'''
        
        args=parser.parse_args()
        
        self._config['debug']=args.debug
        self._config['active_data_source']={'name':args.active_data_source,'config':self.data_sources[args.active_data_source]}
        
    def get(self,key):
        return self._config.get(key,None)
    def set(self,key,value):
        self._config[key]=value
    def show_config(self):
        config_logger=logging.getLogger(__name__)
        config_logger.info('config:')
        for k,v in self._config.items():
            #print(f"{k}:{v}")
                
    
            config_logger.info(f"{k}:{v}")
        

config_instance=Config()
