import dis
dis.dis(compile("(23, 'a', 'b', 'c')", '', 'eval'))
'''
Will print
  1       0 LOAD_CONST           4 ((23, 'a', 'b', 'c'))
          3 RETURN_VALUE
'''
dis.dis(compile("[23, 'a', 'b', 'c']", '', 'eval'))
'''
Will print:
  1       0 LOAD_CONST           0 (23)
          3 LOAD_CONST           1 ('a')
          6 LOAD_CONST           2 ('b')
          9 LOAD_CONST           3 ('c')
         12 BUILD_LIST           4
         15 RETURN_VALUE
'''

# Loading of tuple is faster and it takes up less memory
