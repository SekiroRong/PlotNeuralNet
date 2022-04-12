# -*- coding = utf-8 -*-
# @Time : 2022/4/10 11:09
# @Author : 戎昱
# @File : K-FPN.py
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
    to_Conv("conv1_1", 19, 512, offset="(0,0,0)", to="(0,0,0)", height=10, depth=10, width=4.5 ),
    to_Conv("conv2_1", 38, 256, offset="(0,-6,0)", to="(0,0,0)", height=18, depth=18, width=3.5 ),
    to_Conv("conv3_1", 76, 128, offset="(0,-12,0)", to="(0,0,0)", height=26, depth=26, width=2, caption='Feature Pyramid' ),

    to_UnPool("conv1_2", offset="(4,0,0)", to="(0,0,0)", height=26, depth=26, width=4.5),
    to_UnPool("conv2_2", offset="(4,-6,0)", to="(0,0,0)", height=26, depth=26, width=3.5),
    to_Conv("conv3_2", 76, 128, offset="(4,-12,0)", to="(0,0,0)", height=26, depth=26, width=2, caption='Upsampling'),
    to_connection('conv1_1','conv1_2'),
    to_connection('conv2_1','conv2_2'),

    to_Softmax_( name='softmax', offset="(6,-6,0)", to="(0,0,0)", radius=2, opacity=0),
    to_connection('conv1_2','softmax'),
    to_connection('conv2_2','softmax'),
    to_connection('conv3_2','softmax'),

    to_Conv('sss', '', '',offset="(6,-6,0)", to="(0,0,0)", height=1, depth=0, width=0),
    to_Conv("conv1_3", 76, 512, offset="(8,0,0)", to="(0,0,0)", height=26, depth=26, width=4.5 ),
    to_Conv("conv2_3", 76, 256, offset="(8,-6,0)", to="(0,0,0)", height=26, depth=26, width=3.5 ),
    to_Conv("conv3_3", 76, 128, offset="(8,-12,0)", to="(0,0,0)", height=26, depth=26, width=2, caption='Soft Weight'),

    to_Plus( name='plus', offset="(10,-6,0)", to="(0,0,0)", radius=1, opacity=0.6),

    to_skip('sss', 'plus', pos=53.5,pos2=27),
    to_connection('softmax','conv2_3'),
    to_connection('conv1_3','plus'),
    to_connection('conv2_3','plus'),
    to_connection('conv3_3','plus'),
    # to_connection('softmax', 'plus'),

    to_Conv("conv1_4", 76, 512, offset="(12,0,0)", to="(0,0,0)", height=26, depth=26, width=4.5 ),
    to_Conv("conv2_4", 76, 256, offset="(12,-6,0)", to="(0,0,0)", height=26, depth=26, width=3.5 ),
    to_Conv("conv3_4", 76, 128, offset="(12,-12,0)", to="(0,0,0)", height=26, depth=26, width=2,caption='Feature Pyramid' ),

    to_connection('plus','conv2_4'),
    to_Sum( name='sum', offset="(14,-6,0)", to="(0,0,0)", radius=1, opacity=0.6),

    to_connection("conv1_4", "sum"),
    to_connection("conv2_4", "sum"),
    to_connection("conv3_4", "sum"),

    to_SoftMax("conv2_5", s_filer='76', offset="(16,-6,0)", to="(0,0,0)", height=26, depth=26, width=5.5, caption='Output Heads'),

    to_connection("sum", "conv2_5"),
# to_SoftMax( name, s_filer=10, offset="(0,0,0)", to="(0,0,0)", width=1.5, height=3, depth=25, opacity=0.8, caption=" " ),
#     to_SoftMax( name='b1', s_filer='', offset="(0,0,0)", to="(0,0,0)", width=2, height=40, depth=40, caption="Main Center" ),
#     to_SoftMax( name='b2', s_filer='', offset="(4,0,0)", to="(0,0,0)", width=2, height=40, depth=40, caption="Center Offset" ),
#     to_SoftMax( name='b3', s_filer='', offset="(8,0,0)", to="(0,0,0)", width=2, height=40, depth=40, caption="Rotate Angle" ),
#     to_SoftMax( name='b4', s_filer='', offset="(12,0,0)", to="(0,0,0)", width=2, height=40, depth=40, caption="Dimension" ),
#     to_SoftMax( name='b5', s_filer='', offset="(16,0,0)", to="(0,0,0)", width=2, height=40, depth=40, caption="Height" ),
#     to_Sum( name='sum6', offset="(2,0,0)", to="(1,0,0)", radius=1, opacity=0.6),
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()