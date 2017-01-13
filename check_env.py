# Script Name   : check_env.py
# Author        : Yuan Chao
# Created       : 13th January 2017
# Last Modified	: 13th January 2017
# Version       : 1.0.0


# Description   : This script will check to see if all of the environment variables I require are set  (检查配置文件中所给的环境变量是否已经设置了)
import os

def env_check(config_path):
    '''
    Check to see if the environment variables have benn set
    '''
    with open(config_path) as file:
        for env_name in file:
            env_name = env_name.strip()
            env = os.getenv(env_name)    
            if env is None:
                print('[{}] is not set'.format(env_name))
            else:
                print('Current Setting for {}={}\n'.format(env_name, env))

def main():
    '''
    Call the main method
    '''
    config_path = r'C:\Users\okieM\testdir\env.conf'
    env_check(config_path)

if __name__ == '__main__':
    main()
