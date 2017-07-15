#!/usr/bin/env python

APPNAME = 'broadcast-encryption'

top = '.'
out = 'build'

def options(opt):
  opt.load(['compiler_c', 'compiler_cxx'])
  opt.load(['boost'], tooldir=['.waf-tools'])

def configure(conf):
  conf.load(['compiler_c', 'compiler_cxx'])
  conf.check_boost(lib='system iostreams regex')
  conf.check_cfg(package='libndn-cxx', args=['--cflags', '--libs'],
                 uselib_store='NDN_CXX', mandatory=True)

def build(bld):
  #bld.read_shlib('gmp', paths=['/usr/local/lib'])
  #bld.read_shlib('pbc', paths=['/usr/local/lib'])
  bld.shlib(source='src/client/ndn-consumer-bce.cpp src/client/statistics-collector.cpp src/client/tracer.cpp src/server/ndn-producer-bce.cpp src/server/tracer.cpp', target='bce', use='NDN_CXX')
  bld.program(source='example/consumer.cpp', target='consumer', use='bce', includes="src/client")
  bld.program(source='example/producer.cpp', target='producer', use='bce', includes="src/server")
  #bld.shlib(source='src/bce.c', target='bce', use='gmp pbc')
  #bld.program(source='tests/testbce.c', target='test', use='gmp pbc bce', includes="src")

