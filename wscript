#!/usr/bin/env python

APPNAME = 'broadcast-encryption'

top = '.'
out = 'build'

def options(opt):
  opt.load(['compiler_c', 'compiler_cxx'])

def configure(conf):
  conf.load(['compiler_c', 'compiler_cxx'])

def build(bld):
  bld.read_shlib('gmp', paths=['/usr/local/lib'])
  bld.read_shlib('pbc', paths=['/usr/local/lib'])
  bld.shlib(source='src/bce.c', target='bce', use='gmp pbc')
  bld.program(source='tests/testbce.c', target='test', use='gmp pbc bce', includes="src")

