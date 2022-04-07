# -*- coding = utf-8 -*-
# @Time : 2022/4/6 22:52
# @Author : 戎昱
# @File : KFPN.py
# @Software : PyCharm
# @Contact : sekirorong@gmail.com
# @github : https://github.com/SekiroRong
import sys, os
file = open('KFPN.tex','w')
file.close()

sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks import *

layer_size = [32,26,18,10]

arch = [
    to_head('..'),
    to_cor(),
    to_begin(),

    # input
    to_input('KFPN.png',name='Input'),

    # block-001
    to_Conv( name='b1', s_filer=304, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=2, height=40, depth=40, caption="Downsample" ),
    # to_ConvRes(name='ccr_b1', s_filer=304, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=2, height=40, depth=40, opacity=0.2, caption="downsample"),
    # to_ConvConvRelu(name='ccr_b1', s_filer=304, n_filer=(64, 64), offset="(0,0,0)", to="(0,0,0)", width=(2, 2),
    #                 height=40, depth=40),
    to_Pool(name="pool_b1", offset="(0,0,0)", to="(b1-east)", width=1, height=layer_size[0], depth=layer_size[0], opacity=0.5),

    to_ConvRes(name='res1_1', s_filer='', n_filer=64, offset="(1,0,0)", to="(1,0,0)", width=2.5, height=layer_size[0], depth=layer_size[0], opacity=0.5),
    to_ConvRes(name='res1_2', s_filer=152, n_filer=64, offset="(0,0,0)", to="(res1_1-east)", width=2.5, height=layer_size[0], depth=layer_size[0], opacity=0.5),
    to_Conv( name='ds2', s_filer=76, n_filer=128, offset="(0,0,0)", to="(res1_2-east)", width=2, height=layer_size[1], depth=layer_size[1]),

    to_ConvRes(name='res2_1', s_filer='', n_filer=128, offset="(2,0,0)", to="(2,0,0)", width=3.5, height=layer_size[1], depth=layer_size[1], opacity=0.5),
    to_ConvRes(name='res2_2', s_filer=76, n_filer=128, offset="(0,0,0)", to="(res2_1-east)", width=3.5, height=layer_size[1], depth=layer_size[1], opacity=0.5),
    to_Conv( name='ds3', s_filer=38, n_filer=256, offset="(0,0,0)", to="(res2_2-east)", width=2, height=layer_size[2], depth=layer_size[2]),

    to_ConvRes(name='res3_1', s_filer='', n_filer=256, offset="(3.5,0,0)", to="(3.5,0,0)", width=4.5, height=layer_size[2], depth=layer_size[2], opacity=0.5),
    to_ConvRes(name='res3_2', s_filer=38, n_filer=256, offset="(0,0,0)", to="(res3_1-east)", width=4.5, height=layer_size[2], depth=layer_size[2], opacity=0.5),
    to_Conv( name='ds4', s_filer=19, n_filer=512, offset="(0,0,0)", to="(res3_2-east)", width=2, height=layer_size[3], depth=layer_size[3]),

    to_ConvRes(name='res4_1', s_filer='', n_filer=512, offset="(5,0,0)", to="(5,0,0)", width=4, height=layer_size[3], depth=layer_size[3], opacity=0.5),
    to_ConvRes(name='res4_2', s_filer=19, n_filer=512, offset="(0,0,0)", to="(res4_1-east)", width=4, height=layer_size[3], depth=layer_size[3], opacity=0.5),

    to_UnPool(name='us5', offset="(6,0,0)", to="(6,0,0)", width=2.5, height=layer_size[2], depth=layer_size[2], opacity=0.5, caption="Bilinear"),

    to_Sum( name='sum5', offset="(8.5,0,0)", to="(4.5,0,0)", radius=1, opacity=0.6),
    to_skip("res3_2", "sum5", pos=1.25,pos2=7.25),
    to_ConvSoftMax( name='cat5', s_filer=768, offset="(7,0,0)", to="(7,0,0)", width=3, height=layer_size[2], depth=layer_size[2]),
    to_connection('us5','cat5'),
    to_Conv( name='b5', s_filer=38, n_filer=256, offset="(0,0,0)", to="(cat5-east)", width=2, height=layer_size[2], depth=layer_size[2]),

    to_UnPool(name='us6', offset="(8,0,0)", to="(8,0,0)", width=2.5, height=layer_size[1], depth=layer_size[1], opacity=0.5, caption="Bilinear"),

    to_Sum( name='sum6', offset="(12.5,0,0)", to="(4.5,0,0)", radius=1, opacity=0.6),
    to_skip("res2_2", "sum6", pos=1.25,pos2=10.25),
    to_ConvSoftMax( name='cat6', s_filer=384, offset="(9,0,0)", to="(9,0,0)", width=3, height=layer_size[1], depth=layer_size[1]),
    to_connection('us6','cat6'),
    to_Conv( name='b6', s_filer=76, n_filer=128, offset="(0,0,0)", to="(cat6-east)", width=2, height=layer_size[1], depth=layer_size[1]),

    to_UnPool(name='us7', offset="(10,0,0)", to="(10,0,0)", width=2.5, height=layer_size[0], depth=layer_size[0], opacity=0.5, caption="Bilinear"),

    to_Sum( name='sum7', offset="(16.5,0,0)", to="(4.5,0,0)", radius=1, opacity=0.6),
    to_skip("res1_2", "sum7", pos=1.25,pos2=12.25),
    to_ConvSoftMax( name='cat7', s_filer=192, offset="(11,0,0)", to="(11,0,0)", width=3, height=layer_size[0], depth=layer_size[0]),
    to_connection('us7','cat7'),
    to_Conv( name='b7', s_filer=152, n_filer=64, offset="(0,0,0)", to="(cat7-east)", width=2, height=layer_size[0], depth=layer_size[0]),
    # *block_2ConvPool(name='b2', botton='pool_b1', top='pool_b2', s_filer=152, n_filer=64, offset="(1,0,0)",
    #                  size=(32, 32, 3.5), opacity=0.5),
    # *block_2ConvPool(name='b3', botton='pool_b2', top='pool_b3', s_filer=76, n_filer=128, offset="(1,0,0)",
    #                  size=(25, 25, 4.5), opacity=0.5),
    # *block_2ConvPool(name='b4', botton='pool_b3', top='pool_b4', s_filer=38, n_filer=256, offset="(1,0,0)",
    #                  size=(16, 16, 5.5), opacity=0.5),
    # *block_2ConvPool(name='b5', botton='pool_b4', top='pool_b5', s_filer=19, n_filer=512, offset="(1,0,0)",
    #                  size=(8, 8, 6.5), opacity=0.5),
    #
    # # Bottleneck
    # # block-005
    # to_ConvConvRelu(name='ccr_b5', s_filer=32, n_filer=(1024, 1024), offset="(2,0,0)", to="(pool_b5-east)",
    #                 width=(8, 8), height=8, depth=8, caption="Bottleneck"),
    # to_connection("pool_b4", "ccr_b5"),
    #
    # # Decoder
    # *block_Unconv(name="b6", botton="ccr_b5", top='end_b6', s_filer=64, n_filer=512, offset="(2.1,0,0)",
    #               size=(16, 16, 5.0), opacity=0.5),
    # to_skip(of='ccr_b4', to='ccr_res_b6', pos=1.25),
    # *block_Unconv(name="b7", botton="end_b6", top='end_b7', s_filer=128, n_filer=256, offset="(2.1,0,0)",
    #               size=(25, 25, 4.5), opacity=0.5),
    # to_skip(of='ccr_b3', to='ccr_res_b7', pos=1.25),
    # *block_Unconv(name="b8", botton="end_b7", top='end_b8', s_filer=256, n_filer=128, offset="(2.1,0,0)",
    #               size=(32, 32, 3.5), opacity=0.5),
    # to_skip(of='ccr_b2', to='ccr_res_b8', pos=1.25),
    #
    # *block_Unconv(name="b9", botton="end_b8", top='end_b9', s_filer=512, n_filer=64, offset="(2.1,0,0)",
    #               size=(40, 40, 2.5), opacity=0.5),
    # to_skip(of='ccr_b1', to='ccr_res_b9', pos=1.25),
    #
    # to_ConvSoftMax(name="soft1", s_filer=512, offset="(0.75,0,0)", to="(end_b9-east)", width=1, height=40, depth=40,
    #                caption="SOFT"),
    # to_connection("end_b9", "soft1"),

    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
