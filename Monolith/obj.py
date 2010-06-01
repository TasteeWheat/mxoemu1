--== Disasm ==--
00000008 CODE:
             argcount:
00000009         LONG: 0L (00 00 00 00)
             nlocals:
0000000D         LONG: 0L (00 00 00 00)
             stacksize:
00000011         LONG: 1L (01 00 00 00)
             flags:
00000015         LONG: 64L (40 00 00 00)
                 (NOFREE)
             code:
00000019         STR: 'h\x00\x00Z\x00\x00d\x00\x00\x84\x00\x00Z\x01\x00d\x01\x00\x84\x00\x00Z\x02\x00e\x01\x00\x83\x00\x00\x01d\x02\x00S' (23 00 00 00 68 00 00 5A 00 00 64 00 00 84 00 00 5A 01 00 64 01 00 84 00 00 5A 02 00 65 01 00 83 00 00 01 64 02 00 53)
                 00000000     68 - BUILD_MAP           r0000
                 00000003     5A - STORE_NAME          'gObjectTypeInfo'
                 00000006     64 - LOAD_CONST          CODE('Init')
                 00000009     84 - MAKE_FUNCTION       r0000
                 0000000C     5A - STORE_NAME          'Init'
                 0000000F     64 - LOAD_CONST          CODE('GetTypeInfo')
                 00000012     84 - MAKE_FUNCTION       r0000
                 00000015     5A - STORE_NAME          'GetTypeInfo'
                 00000018     65 - LOAD_NAME           'Init'
                 0000001B     83 - CALL_FUNCTION       r0000
                 0000001E     01 - POP_TOP             
                 0000001F     64 - LOAD_CONST          None
                 00000022     53 - RETURN_VALUE        
             consts:
00000041         TUPLE: (
00000046             CODE:
                         argcount:
00000047                     LONG: 0L (00 00 00 00)
                         nlocals:
0000004B                     LONG: 4L (04 00 00 00)
                         stacksize:
0000004F                     LONG: 4L (04 00 00 00)
                         flags:
00000053                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000057                     STR: 't\x00\x00i\x01\x00\x83\x00\x00}\x01\x00t\x03\x00\x83\x00\x00}\x02\x00xH\x00|\x01\x00i\x05\x00\x83\x00\x00D]:\x00\\\x02\x00}\x00\x00}\x03\x00|\x00\x00i\x08\x00d\x01\x00d\x02\x00\x83\x02\x00}\x00\x00|\x00\x00i\x08\x00d\x03\x00d\x02\x00\x83\x02\x00}\x00\x00|\x03\x00|\x02\x00|\x00\x00<q"\x00Wd\x00\x00S' (64 00 00 00 74 00 00 69 01 00 83 00 00 7D 01 00 74 03 00 83 00 00 7D 02 00 78 48 00 7C 01 00 69 05 00 83 00 00 44 5D 3A 00 5C 02 00 7D 00 00 7D 03 00 7C 00 00 69 08 00 64 01 00 64 02 00 83 02 00 7D 00 00 7C 00 00 69 08 00 64 03 00 64 02 00 83 02 00 7D 00 00 7C 03 00 7C 02 00 7C 00 00 3C 71 22 00 57 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'discovery'
                             00000003     69 - LOAD_ATTR           'getAllObjects'
                             00000006     83 - CALL_FUNCTION       r0000
                             00000009     7D - STORE_FAST          'objnames'
                             0000000C     74 - LOAD_GLOBAL         'globals'
                             0000000F     83 - CALL_FUNCTION       r0000
                             00000012     7D - STORE_FAST          'globs'
                             00000015     78 - SETUP_LOOP          -> 00000060
                             00000018     7C - LOAD_FAST           'objnames'
                             0000001B     69 - LOAD_ATTR           'iteritems'
                             0000001E     83 - CALL_FUNCTION       r0000
                             00000021     44 - GET_ITER            
                             00000022     5D - FOR_ITER            -> 0000005F
                             00000025     5C - UNPACK_SEQUENCE     r0002
                             00000028     7D - STORE_FAST          'name'
                             0000002B     7D - STORE_FAST          'id'
                             0000002E     7C - LOAD_FAST           'name'
                             00000031     69 - LOAD_ATTR           'replace'
                             00000034     64 - LOAD_CONST          ' '
                             00000037     64 - LOAD_CONST          ''
                             0000003A     83 - CALL_FUNCTION       r0002
                             0000003D     7D - STORE_FAST          'name'
                             00000040     7C - LOAD_FAST           'name'
                             00000043     69 - LOAD_ATTR           'replace'
                             00000046     64 - LOAD_CONST          '-'
                             00000049     64 - LOAD_CONST          ''
                             0000004C     83 - CALL_FUNCTION       r0002
                             0000004F     7D - STORE_FAST          'name'
                             00000052     7C - LOAD_FAST           'id'
                             00000055     7C - LOAD_FAST           'globs'
                             00000058     7C - LOAD_FAST           'name'
                             0000005B     3C - STORE_SUBSCR        
                             0000005C     71 - JUMP_ABSOLUTE       -> 00000022
                             0000005F     57 - POP_BLOCK           
                             00000060     64 - LOAD_CONST          None
                             00000063     53 - RETURN_VALUE        
                         consts:
000000C0                     TUPLE: (
000000C5                         None (4E),
000000C6                         STR: ' ' (01 00 00 00 20),
000000CC                         STR: '' (00 00 00 00),
000000D1                         STR: '-' (01 00 00 00 2D)
                             )
                         names:
000000D7                     TUPLE: (
000000DC                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
000000EA                         STR: 'getAllObjects' (0D 00 00 00 67 65 74 41 6C 6C 4F 62 6A 65 63 74 73),
000000FC                         STR: 'objnames' (08 00 00 00 6F 62 6A 6E 61 6D 65 73),
00000109                         STR: 'globals' (07 00 00 00 67 6C 6F 62 61 6C 73),
00000115                         STR: 'globs' (05 00 00 00 67 6C 6F 62 73),
0000011F                         STR: 'iteritems' (09 00 00 00 69 74 65 72 69 74 65 6D 73),
0000012D                         STR: 'name' (04 00 00 00 6E 61 6D 65),
00000136                         STR: 'id' (02 00 00 00 69 64),
0000013D                         STR: 'replace' (07 00 00 00 72 65 70 6C 61 63 65)
                             )
                         varnames:
00000149                     TUPLE: (
0000014E                         STR: 'name' (04 00 00 00 6E 61 6D 65),
00000157                         STR: 'objnames' (08 00 00 00 6F 62 6A 6E 61 6D 65 73),
00000164                         STR: 'globs' (05 00 00 00 67 6C 6F 62 73),
0000016E                         STR: 'id' (02 00 00 00 69 64)
                             )
                         freevars:
00000175                     TUPLE: ()
                         cellvars:
0000017A                     TUPLE: ()
                         filename:
0000017F                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\obj.py' (3B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6F 62 6A 2E 70 79)
                         name:
000001BF                     STR: 'Init' (04 00 00 00 49 6E 69 74)
                         firslineno:
000001C8                     LONG: 7L (07 00 00 00)
                         lnotab:
000001CC                     STR: '\x00\x02\x0c\x02\t\x01\r\x00\x0c\x01\x12\x01\x12\x03' (0E 00 00 00 00 02 0C 02 09 01 0D 00 0C 01 12 01 12 03),
000001DF             CODE:
                         argcount:
000001E0                     LONG: 1L (01 00 00 00)
                         nlocals:
000001E4                     LONG: 1L (01 00 00 00)
                         stacksize:
000001E8                     LONG: 3L (03 00 00 00)
                         flags:
000001EC                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000001F0                     STR: '|\x00\x00t\x01\x00j\x06\x00o\x0c\x00\x01t\x01\x00|\x00\x00\x19Sn\x01\x00\x01t\x02\x00i\x03\x00|\x00\x00\x83\x01\x00t\x01\x00|\x00\x00<t\x01\x00|\x00\x00\x19Sd\x00\x00S' (38 00 00 00 7C 00 00 74 01 00 6A 06 00 6F 0C 00 01 74 01 00 7C 00 00 19 53 6E 01 00 01 74 02 00 69 03 00 7C 00 00 83 01 00 74 01 00 7C 00 00 3C 74 01 00 7C 00 00 19 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'id'
                             00000003     74 - LOAD_GLOBAL         'gObjectTypeInfo'
                             00000006     6A - COMPARE_OP          "in"
                             00000009     6F - JUMP_IF_FALSE       -> 00000018
                             0000000C     01 - POP_TOP             
                             0000000D     74 - LOAD_GLOBAL         'gObjectTypeInfo'
                             00000010     7C - LOAD_FAST           'id'
                             00000013     19 - BINARY_SUBSCR       
                             00000014     53 - RETURN_VALUE        
                             00000015     6E - JUMP_FORWARD        -> 00000019
                             00000018     01 - POP_TOP             
                             00000019     74 - LOAD_GLOBAL         'discovery'
                             0000001C     69 - LOAD_ATTR           'getTypeInfo'
                             0000001F     7C - LOAD_FAST           'id'
                             00000022     83 - CALL_FUNCTION       r0001
                             00000025     74 - LOAD_GLOBAL         'gObjectTypeInfo'
                             00000028     7C - LOAD_FAST           'id'
                             0000002B     3C - STORE_SUBSCR        
                             0000002C     74 - LOAD_GLOBAL         'gObjectTypeInfo'
                             0000002F     7C - LOAD_FAST           'id'
                             00000032     19 - BINARY_SUBSCR       
                             00000033     53 - RETURN_VALUE        
                             00000034     64 - LOAD_CONST          None
                             00000037     53 - RETURN_VALUE        
                         consts:
0000022D                     TUPLE: (
00000232                         None (4E)
                             )
                         names:
00000233                     TUPLE: (
00000238                         STR: 'id' (02 00 00 00 69 64),
0000023F                         STR: 'gObjectTypeInfo' (0F 00 00 00 67 4F 62 6A 65 63 74 54 79 70 65 49 6E 66 6F),
00000253                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
00000261                         STR: 'getTypeInfo' (0B 00 00 00 67 65 74 54 79 70 65 49 6E 66 6F)
                             )
                         varnames:
00000271                     TUPLE: (
00000276                         STR: 'id' (02 00 00 00 69 64)
                             )
                         freevars:
0000027D                     TUPLE: ()
                         cellvars:
00000282                     TUPLE: ()
                         filename:
00000287                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\obj.py' (3B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6F 62 6A 2E 70 79)
                         name:
000002C7                     STR: 'GetTypeInfo' (0B 00 00 00 47 65 74 54 79 70 65 49 6E 66 6F)
                         firslineno:
000002D7                     LONG: 20L (14 00 00 00)
                         lnotab:
000002DB                     STR: '\x00\x01\r\x01\x0c\x02\x13\x01' (08 00 00 00 00 01 0D 01 0C 02 13 01),
000002E8             None (4E)
                 )
             names:
000002E9         TUPLE: (
000002EE             STR: 'gObjectTypeInfo' (0F 00 00 00 67 4F 62 6A 65 63 74 54 79 70 65 49 6E 66 6F),
00000302             STR: 'Init' (04 00 00 00 49 6E 69 74),
0000030B             STR: 'GetTypeInfo' (0B 00 00 00 47 65 74 54 79 70 65 49 6E 66 6F)
                 )
             varnames:
0000031B         TUPLE: (
00000320             STR: 'gObjectTypeInfo' (0F 00 00 00 67 4F 62 6A 65 63 74 54 79 70 65 49 6E 66 6F),
00000334             STR: 'Init' (04 00 00 00 49 6E 69 74),
0000033D             STR: 'GetTypeInfo' (0B 00 00 00 47 65 74 54 79 70 65 49 6E 66 6F)
                 )
             freevars:
0000034D         TUPLE: ()
             cellvars:
00000352         TUPLE: ()
             filename:
00000357         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\obj.py' (3B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6F 62 6A 2E 70 79)
             name:
00000397         STR: '?' (01 00 00 00 3F)
             firslineno:
0000039D         LONG: 5L (05 00 00 00)
             lnotab:
000003A1         STR: '\x06\x02\t\r\t\x07' (06 00 00 00 06 02 09 0D 09 07)

