# -*- coding = utf-8 -*-
# @Time : 2022/4/7 12:40
# @Author : 戎昱
# @File : DetectionHead.py
# @Software : PyCharm
# @Contact : sekirorong@gmail.com
# @github : https://github.com/SekiroRong
import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
# to_SoftMax( name, s_filer=10, offset="(0,0,0)", to="(0,0,0)", width=1.5, height=3, depth=25, opacity=0.8, caption=" " ),
#     to_SoftMax( name='b1', s_filer='', offset="(0,0,0)", to="(0,0,0)", width=2, height=40, depth=40, caption="Main Center" ),
#     to_SoftMax( name='b2', s_filer='', offset="(4,0,0)", to="(0,0,0)", width=2, height=40, depth=40, caption="Center Offset" ),
#     to_SoftMax( name='b3', s_filer='', offset="(8,0,0)", to="(0,0,0)", width=2, height=40, depth=40, caption="Rotate Angle" ),
#     to_SoftMax( name='b4', s_filer='', offset="(12,0,0)", to="(0,0,0)", width=2, height=40, depth=40, caption="Dimension" ),
#     to_SoftMax( name='b5', s_filer='', offset="(16,0,0)", to="(0,0,0)", width=2, height=40, depth=40, caption="Height" ),
    to_Plus( name='sum6', offset="(2,0,0)", to="(1,0,0)", radius=1, opacity=0.6),
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()