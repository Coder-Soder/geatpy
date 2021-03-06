# -*- coding: utf-8 -*-
from operators.mutation.Mutation import Mutation
from mutbin import mutbin

class Mutbin(Mutation):
    """
    Mutbin - class : 一个用于调用内核中的变异函数mutbin(二进制变异)的变异算子类，
                     该类的各成员属性与内核中的对应函数的同名参数含义一致，
                     可利用help(mutbin)查看各参数的详细含义及用法。
    """
    def __init__(self, Pm = 1):
        self.Pm = Pm
    
    def do(self, Encoding, OldChrom, FieldDR, *args): # 执行变异
        return mutbin(Encoding, OldChrom, Pm = self.Pm)
    
    def getHelp(self): # 查看内核中的变异算子的API文档
        help(mutbin)
    