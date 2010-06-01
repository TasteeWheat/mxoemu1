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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00Z\x02\x00d\x00\x00k\x03\x00Z\x04\x00d\x00\x00k\x05\x00Z\x05\x00d\x00\x00k\x06\x00Z\x07\x00d\x01\x00\x84\x00\x00Z\x08\x00d\x02\x00\x84\x00\x00Z\t\x00d\x03\x00\x84\x00\x00Z\n\x00d\x04\x00\x84\x00\x00Z\x0b\x00d\x05\x00\x84\x00\x00Z\x0c\x00d\x00\x00S' (67 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 5A 02 00 64 00 00 6B 03 00 5A 04 00 64 00 00 6B 05 00 5A 05 00 64 00 00 6B 06 00 5A 07 00 64 01 00 84 00 00 5A 08 00 64 02 00 84 00 00 5A 09 00 64 03 00 84 00 00 5A 0A 00 64 04 00 84 00 00 5A 0B 00 64 05 00 84 00 00 5A 0C 00 64 00 00 53)
                 00000000     64 - LOAD_CONST          None
                 00000003     6B - IMPORT_NAME         'random'
                 00000006     5A - STORE_NAME          'random'
                 00000009     64 - LOAD_CONST          None
                 0000000C     6B - IMPORT_NAME         'traceback'
                 0000000F     5A - STORE_NAME          'traceback'
                 00000012     64 - LOAD_CONST          None
                 00000015     6B - IMPORT_NAME         'obj'
                 00000018     5A - STORE_NAME          'obj'
                 0000001B     64 - LOAD_CONST          None
                 0000001E     6B - IMPORT_NAME         'combat_defines'
                 00000021     5A - STORE_NAME          'CD'
                 00000024     64 - LOAD_CONST          None
                 00000027     6B - IMPORT_NAME         'math'
                 0000002A     5A - STORE_NAME          'math'
                 0000002D     64 - LOAD_CONST          None
                 00000030     6B - IMPORT_NAME         'combat_utility'
                 00000033     5A - STORE_NAME          'CU'
                 00000036     64 - LOAD_CONST          CODE('calcInnerStrengthWithSelfDefense')
                 00000039     84 - MAKE_FUNCTION       r0000
                 0000003C     5A - STORE_NAME          'calcInnerStrengthWithSelfDefense'
                 0000003F     64 - LOAD_CONST          CODE('calcInnerStrengthWithMartialArt')
                 00000042     84 - MAKE_FUNCTION       r0000
                 00000045     5A - STORE_NAME          'calcInnerStrengthWithMartialArt'
                 00000048     64 - LOAD_CONST          CODE('calcInnerStrengthWithGun')
                 0000004B     84 - MAKE_FUNCTION       r0000
                 0000004E     5A - STORE_NAME          'calcInnerStrengthWithGun'
                 00000051     64 - LOAD_CONST          CODE('calcInnerStrengthForWinner')
                 00000054     84 - MAKE_FUNCTION       r0000
                 00000057     5A - STORE_NAME          'calcInnerStrengthForWinner'
                 0000005A     64 - LOAD_CONST          CODE('calcInnerStrengthForLoser')
                 0000005D     84 - MAKE_FUNCTION       r0000
                 00000060     5A - STORE_NAME          'calcInnerStrengthForLoser'
                 00000063     64 - LOAD_CONST          None
                 00000066     53 - RETURN_VALUE        
             consts:
00000085         TUPLE: (
0000008A             None (4E),
0000008B             CODE:
                         argcount:
0000008C                     LONG: 1L (01 00 00 00)
                         nlocals:
00000090                     LONG: 1L (01 00 00 00)
                         stacksize:
00000094                     LONG: 2L (02 00 00 00)
                         flags:
00000098                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000009C                     STR: '|\x00\x00t\x01\x00i\x02\x00i\x03\x00j\x02\x00o\x08\x00\x01d\x01\x00SnR\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x04\x00j\x02\x00o\x08\x00\x01d\x02\x00Sn7\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x05\x00j\x02\x00o\x08\x00\x01d\x02\x00Sn\x1c\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x06\x00j\x02\x00o\x08\x00\x01d\x03\x00Sn\x01\x00\x01d\x04\x00Sd\x00\x00S' (74 00 00 00 7C 00 00 74 01 00 69 02 00 69 03 00 6A 02 00 6F 08 00 01 64 01 00 53 6E 52 00 01 7C 00 00 74 01 00 69 02 00 69 04 00 6A 02 00 6F 08 00 01 64 02 00 53 6E 37 00 01 7C 00 00 74 01 00 69 02 00 69 05 00 6A 02 00 6F 08 00 01 64 02 00 53 6E 1C 00 01 7C 00 00 74 01 00 69 02 00 69 06 00 6A 02 00 6F 08 00 01 64 03 00 53 6E 01 00 01 64 04 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'tactical_setting'
                             00000003     74 - LOAD_GLOBAL         'constants'
                             00000006     69 - LOAD_ATTR           'combat'
                             00000009     69 - LOAD_ATTR           'POWER'
                             0000000C     6A - COMPARE_OP          "=="
                             0000000F     6F - JUMP_IF_FALSE       -> 0000001A
                             00000012     01 - POP_TOP             
                             00000013     64 - LOAD_CONST          -20
                             00000016     53 - RETURN_VALUE        
                             00000017     6E - JUMP_FORWARD        -> 0000006C
                             0000001A     01 - POP_TOP             
                             0000001B     7C - LOAD_FAST           'tactical_setting'
                             0000001E     74 - LOAD_GLOBAL         'constants'
                             00000021     69 - LOAD_ATTR           'combat'
                             00000024     69 - LOAD_ATTR           'SPEED'
                             00000027     6A - COMPARE_OP          "=="
                             0000002A     6F - JUMP_IF_FALSE       -> 00000035
                             0000002D     01 - POP_TOP             
                             0000002E     64 - LOAD_CONST          -10
                             00000031     53 - RETURN_VALUE        
                             00000032     6E - JUMP_FORWARD        -> 0000006C
                             00000035     01 - POP_TOP             
                             00000036     7C - LOAD_FAST           'tactical_setting'
                             00000039     74 - LOAD_GLOBAL         'constants'
                             0000003C     69 - LOAD_ATTR           'combat'
                             0000003F     69 - LOAD_ATTR           'DEFENSE'
                             00000042     6A - COMPARE_OP          "=="
                             00000045     6F - JUMP_IF_FALSE       -> 00000050
                             00000048     01 - POP_TOP             
                             00000049     64 - LOAD_CONST          -10
                             0000004C     53 - RETURN_VALUE        
                             0000004D     6E - JUMP_FORWARD        -> 0000006C
                             00000050     01 - POP_TOP             
                             00000051     7C - LOAD_FAST           'tactical_setting'
                             00000054     74 - LOAD_GLOBAL         'constants'
                             00000057     69 - LOAD_ATTR           'combat'
                             0000005A     69 - LOAD_ATTR           'BLOCK'
                             0000005D     6A - COMPARE_OP          "=="
                             00000060     6F - JUMP_IF_FALSE       -> 0000006B
                             00000063     01 - POP_TOP             
                             00000064     64 - LOAD_CONST          10
                             00000067     53 - RETURN_VALUE        
                             00000068     6E - JUMP_FORWARD        -> 0000006C
                             0000006B     01 - POP_TOP             
                             0000006C     64 - LOAD_CONST          0
                             0000006F     53 - RETURN_VALUE        
                             00000070     64 - LOAD_CONST          None
                             00000073     53 - RETURN_VALUE        
                         consts:
00000115                     TUPLE: (
0000011A                         None (4E),
0000011B                         INT: -20 (EC FF FF FF),
00000120                         INT: -10 (F6 FF FF FF),
00000125                         INT: 10 (0A 00 00 00),
0000012A                         INT: 0 (00 00 00 00)
                             )
                         names:
0000012F                     TUPLE: (
00000134                         STR: 'tactical_setting' (10 00 00 00 74 61 63 74 69 63 61 6C 5F 73 65 74 74 69 6E 67),
00000149                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00000157                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
00000162                         STR: 'POWER' (05 00 00 00 50 4F 57 45 52),
0000016C                         STR: 'SPEED' (05 00 00 00 53 50 45 45 44),
00000176                         STR: 'DEFENSE' (07 00 00 00 44 45 46 45 4E 53 45),
00000182                         STR: 'BLOCK' (05 00 00 00 42 4C 4F 43 4B)
                             )
                         varnames:
0000018C                     TUPLE: (
00000191                         STR: 'tactical_setting' (10 00 00 00 74 61 63 74 69 63 61 6C 5F 73 65 74 74 69 6E 67)
                             )
                         freevars:
000001A6                     TUPLE: ()
                         cellvars:
000001AB                     TUPLE: ()
                         filename:
000001B0                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_innerstrength.py' (56 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 69 6E 6E 65 72 73 74 72 65 6E 67 74 68 2E 70 79)
                         name:
0000020B                     STR: 'calcInnerStrengthWithSelfDefense' (20 00 00 00 63 61 6C 63 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 57 69 74 68 53 65 6C 66 44 65 66 65 6E 73 65)
                         firslineno:
00000230                     LONG: 9L (09 00 00 00)
                         lnotab:
00000234                     STR: '\x00\x01\x13\x01\x08\x01\x13\x01\x08\x01\x13\x01\x08\x01\x13\x01\x08\x02' (12 00 00 00 00 01 13 01 08 01 13 01 08 01 13 01 08 01 13 01 08 02),
0000024B             CODE:
                         argcount:
0000024C                     LONG: 1L (01 00 00 00)
                         nlocals:
00000250                     LONG: 1L (01 00 00 00)
                         stacksize:
00000254                     LONG: 2L (02 00 00 00)
                         flags:
00000258                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000025C                     STR: '|\x00\x00t\x01\x00i\x02\x00i\x03\x00j\x02\x00o\x08\x00\x01d\x01\x00SnR\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x04\x00j\x02\x00o\x08\x00\x01d\x02\x00Sn7\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x05\x00j\x02\x00o\x08\x00\x01d\x03\x00Sn\x1c\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x06\x00j\x02\x00o\x08\x00\x01d\x04\x00Sn\x01\x00\x01d\x05\x00Sd\x00\x00S' (74 00 00 00 7C 00 00 74 01 00 69 02 00 69 03 00 6A 02 00 6F 08 00 01 64 01 00 53 6E 52 00 01 7C 00 00 74 01 00 69 02 00 69 04 00 6A 02 00 6F 08 00 01 64 02 00 53 6E 37 00 01 7C 00 00 74 01 00 69 02 00 69 05 00 6A 02 00 6F 08 00 01 64 03 00 53 6E 1C 00 01 7C 00 00 74 01 00 69 02 00 69 06 00 6A 02 00 6F 08 00 01 64 04 00 53 6E 01 00 01 64 05 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'tactical_setting'
                             00000003     74 - LOAD_GLOBAL         'constants'
                             00000006     69 - LOAD_ATTR           'combat'
                             00000009     69 - LOAD_ATTR           'POWER'
                             0000000C     6A - COMPARE_OP          "=="
                             0000000F     6F - JUMP_IF_FALSE       -> 0000001A
                             00000012     01 - POP_TOP             
                             00000013     64 - LOAD_CONST          -20
                             00000016     53 - RETURN_VALUE        
                             00000017     6E - JUMP_FORWARD        -> 0000006C
                             0000001A     01 - POP_TOP             
                             0000001B     7C - LOAD_FAST           'tactical_setting'
                             0000001E     74 - LOAD_GLOBAL         'constants'
                             00000021     69 - LOAD_ATTR           'combat'
                             00000024     69 - LOAD_ATTR           'SPEED'
                             00000027     6A - COMPARE_OP          "=="
                             0000002A     6F - JUMP_IF_FALSE       -> 00000035
                             0000002D     01 - POP_TOP             
                             0000002E     64 - LOAD_CONST          -10
                             00000031     53 - RETURN_VALUE        
                             00000032     6E - JUMP_FORWARD        -> 0000006C
                             00000035     01 - POP_TOP             
                             00000036     7C - LOAD_FAST           'tactical_setting'
                             00000039     74 - LOAD_GLOBAL         'constants'
                             0000003C     69 - LOAD_ATTR           'combat'
                             0000003F     69 - LOAD_ATTR           'DEFENSE'
                             00000042     6A - COMPARE_OP          "=="
                             00000045     6F - JUMP_IF_FALSE       -> 00000050
                             00000048     01 - POP_TOP             
                             00000049     64 - LOAD_CONST          -5
                             0000004C     53 - RETURN_VALUE        
                             0000004D     6E - JUMP_FORWARD        -> 0000006C
                             00000050     01 - POP_TOP             
                             00000051     7C - LOAD_FAST           'tactical_setting'
                             00000054     74 - LOAD_GLOBAL         'constants'
                             00000057     69 - LOAD_ATTR           'combat'
                             0000005A     69 - LOAD_ATTR           'BLOCK'
                             0000005D     6A - COMPARE_OP          "=="
                             00000060     6F - JUMP_IF_FALSE       -> 0000006B
                             00000063     01 - POP_TOP             
                             00000064     64 - LOAD_CONST          10
                             00000067     53 - RETURN_VALUE        
                             00000068     6E - JUMP_FORWARD        -> 0000006C
                             0000006B     01 - POP_TOP             
                             0000006C     64 - LOAD_CONST          0
                             0000006F     53 - RETURN_VALUE        
                             00000070     64 - LOAD_CONST          None
                             00000073     53 - RETURN_VALUE        
                         consts:
000002D5                     TUPLE: (
000002DA                         None (4E),
000002DB                         INT: -20 (EC FF FF FF),
000002E0                         INT: -10 (F6 FF FF FF),
000002E5                         INT: -5 (FB FF FF FF),
000002EA                         INT: 10 (0A 00 00 00),
000002EF                         INT: 0 (00 00 00 00)
                             )
                         names:
000002F4                     TUPLE: (
000002F9                         STR: 'tactical_setting' (10 00 00 00 74 61 63 74 69 63 61 6C 5F 73 65 74 74 69 6E 67),
0000030E                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
0000031C                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
00000327                         STR: 'POWER' (05 00 00 00 50 4F 57 45 52),
00000331                         STR: 'SPEED' (05 00 00 00 53 50 45 45 44),
0000033B                         STR: 'DEFENSE' (07 00 00 00 44 45 46 45 4E 53 45),
00000347                         STR: 'BLOCK' (05 00 00 00 42 4C 4F 43 4B)
                             )
                         varnames:
00000351                     TUPLE: (
00000356                         STR: 'tactical_setting' (10 00 00 00 74 61 63 74 69 63 61 6C 5F 73 65 74 74 69 6E 67)
                             )
                         freevars:
0000036B                     TUPLE: ()
                         cellvars:
00000370                     TUPLE: ()
                         filename:
00000375                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_innerstrength.py' (56 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 69 6E 6E 65 72 73 74 72 65 6E 67 74 68 2E 70 79)
                         name:
000003D0                     STR: 'calcInnerStrengthWithMartialArt' (1F 00 00 00 63 61 6C 63 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 57 69 74 68 4D 61 72 74 69 61 6C 41 72 74)
                         firslineno:
000003F4                     LONG: 21L (15 00 00 00)
                         lnotab:
000003F8                     STR: '\x00\x01\x13\x01\x08\x01\x13\x01\x08\x01\x13\x01\x08\x01\x13\x01\x08\x02' (12 00 00 00 00 01 13 01 08 01 13 01 08 01 13 01 08 01 13 01 08 02),
0000040F             CODE:
                         argcount:
00000410                     LONG: 1L (01 00 00 00)
                         nlocals:
00000414                     LONG: 1L (01 00 00 00)
                         stacksize:
00000418                     LONG: 2L (02 00 00 00)
                         flags:
0000041C                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000420                     STR: '|\x00\x00t\x01\x00i\x02\x00i\x03\x00j\x02\x00o\x08\x00\x01d\x01\x00SnR\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x04\x00j\x02\x00o\x08\x00\x01d\x02\x00Sn7\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x05\x00j\x02\x00o\x08\x00\x01d\x02\x00Sn\x1c\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x06\x00j\x02\x00o\x08\x00\x01d\x03\x00Sn\x01\x00\x01d\x04\x00Sd\x00\x00S' (74 00 00 00 7C 00 00 74 01 00 69 02 00 69 03 00 6A 02 00 6F 08 00 01 64 01 00 53 6E 52 00 01 7C 00 00 74 01 00 69 02 00 69 04 00 6A 02 00 6F 08 00 01 64 02 00 53 6E 37 00 01 7C 00 00 74 01 00 69 02 00 69 05 00 6A 02 00 6F 08 00 01 64 02 00 53 6E 1C 00 01 7C 00 00 74 01 00 69 02 00 69 06 00 6A 02 00 6F 08 00 01 64 03 00 53 6E 01 00 01 64 04 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'tactical_setting'
                             00000003     74 - LOAD_GLOBAL         'constants'
                             00000006     69 - LOAD_ATTR           'combat'
                             00000009     69 - LOAD_ATTR           'POWER'
                             0000000C     6A - COMPARE_OP          "=="
                             0000000F     6F - JUMP_IF_FALSE       -> 0000001A
                             00000012     01 - POP_TOP             
                             00000013     64 - LOAD_CONST          -20
                             00000016     53 - RETURN_VALUE        
                             00000017     6E - JUMP_FORWARD        -> 0000006C
                             0000001A     01 - POP_TOP             
                             0000001B     7C - LOAD_FAST           'tactical_setting'
                             0000001E     74 - LOAD_GLOBAL         'constants'
                             00000021     69 - LOAD_ATTR           'combat'
                             00000024     69 - LOAD_ATTR           'SPEED'
                             00000027     6A - COMPARE_OP          "=="
                             0000002A     6F - JUMP_IF_FALSE       -> 00000035
                             0000002D     01 - POP_TOP             
                             0000002E     64 - LOAD_CONST          -10
                             00000031     53 - RETURN_VALUE        
                             00000032     6E - JUMP_FORWARD        -> 0000006C
                             00000035     01 - POP_TOP             
                             00000036     7C - LOAD_FAST           'tactical_setting'
                             00000039     74 - LOAD_GLOBAL         'constants'
                             0000003C     69 - LOAD_ATTR           'combat'
                             0000003F     69 - LOAD_ATTR           'DEFENSE'
                             00000042     6A - COMPARE_OP          "=="
                             00000045     6F - JUMP_IF_FALSE       -> 00000050
                             00000048     01 - POP_TOP             
                             00000049     64 - LOAD_CONST          -10
                             0000004C     53 - RETURN_VALUE        
                             0000004D     6E - JUMP_FORWARD        -> 0000006C
                             00000050     01 - POP_TOP             
                             00000051     7C - LOAD_FAST           'tactical_setting'
                             00000054     74 - LOAD_GLOBAL         'constants'
                             00000057     69 - LOAD_ATTR           'combat'
                             0000005A     69 - LOAD_ATTR           'BLOCK'
                             0000005D     6A - COMPARE_OP          "=="
                             00000060     6F - JUMP_IF_FALSE       -> 0000006B
                             00000063     01 - POP_TOP             
                             00000064     64 - LOAD_CONST          10
                             00000067     53 - RETURN_VALUE        
                             00000068     6E - JUMP_FORWARD        -> 0000006C
                             0000006B     01 - POP_TOP             
                             0000006C     64 - LOAD_CONST          0
                             0000006F     53 - RETURN_VALUE        
                             00000070     64 - LOAD_CONST          None
                             00000073     53 - RETURN_VALUE        
                         consts:
00000499                     TUPLE: (
0000049E                         None (4E),
0000049F                         INT: -20 (EC FF FF FF),
000004A4                         INT: -10 (F6 FF FF FF),
000004A9                         INT: 10 (0A 00 00 00),
000004AE                         INT: 0 (00 00 00 00)
                             )
                         names:
000004B3                     TUPLE: (
000004B8                         STR: 'tactical_setting' (10 00 00 00 74 61 63 74 69 63 61 6C 5F 73 65 74 74 69 6E 67),
000004CD                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
000004DB                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
000004E6                         STR: 'POWER' (05 00 00 00 50 4F 57 45 52),
000004F0                         STR: 'SPEED' (05 00 00 00 53 50 45 45 44),
000004FA                         STR: 'DEFENSE' (07 00 00 00 44 45 46 45 4E 53 45),
00000506                         STR: 'BLOCK' (05 00 00 00 42 4C 4F 43 4B)
                             )
                         varnames:
00000510                     TUPLE: (
00000515                         STR: 'tactical_setting' (10 00 00 00 74 61 63 74 69 63 61 6C 5F 73 65 74 74 69 6E 67)
                             )
                         freevars:
0000052A                     TUPLE: ()
                         cellvars:
0000052F                     TUPLE: ()
                         filename:
00000534                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_innerstrength.py' (56 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 69 6E 6E 65 72 73 74 72 65 6E 67 74 68 2E 70 79)
                         name:
0000058F                     STR: 'calcInnerStrengthWithGun' (18 00 00 00 63 61 6C 63 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 57 69 74 68 47 75 6E)
                         firslineno:
000005AC                     LONG: 33L (21 00 00 00)
                         lnotab:
000005B0                     STR: '\x00\x01\x13\x01\x08\x01\x13\x01\x08\x01\x13\x01\x08\x01\x13\x01\x08\x02' (12 00 00 00 00 01 13 01 08 01 13 01 08 01 13 01 08 01 13 01 08 02),
000005C7             CODE:
                         argcount:
000005C8                     LONG: 1L (01 00 00 00)
                         nlocals:
000005CC                     LONG: 2L (02 00 00 00)
                         stacksize:
000005D0                     LONG: 3L (03 00 00 00)
                         flags:
000005D4                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000005D8                     STR: 'd\x01\x00}\x01\x00t\x01\x00i\x02\x00|\x00\x00i\x04\x00\x83\x01\x00o\x17\x00\x01|\x01\x00t\x05\x00|\x00\x00i\x06\x00\x83\x01\x007}\x01\x00n>\x00\x01t\x01\x00i\x07\x00|\x00\x00i\x08\x00\x83\x01\x00o\x17\x00\x01|\x01\x00t\t\x00|\x00\x00i\x06\x00\x83\x01\x007}\x01\x00n\x14\x00\x01|\x01\x00t\n\x00|\x00\x00i\x06\x00\x83\x01\x007}\x01\x00|\x01\x00Sd\x00\x00S' (75 00 00 00 64 01 00 7D 01 00 74 01 00 69 02 00 7C 00 00 69 04 00 83 01 00 6F 17 00 01 7C 01 00 74 05 00 7C 00 00 69 06 00 83 01 00 37 7D 01 00 6E 3E 00 01 74 01 00 69 07 00 7C 00 00 69 08 00 83 01 00 6F 17 00 01 7C 01 00 74 09 00 7C 00 00 69 06 00 83 01 00 37 7D 01 00 6E 14 00 01 7C 01 00 74 0A 00 7C 00 00 69 06 00 83 01 00 37 7D 01 00 7C 01 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          0
                             00000003     7D - STORE_FAST          'innerstrength_amount'
                             00000006     74 - LOAD_GLOBAL         'CU'
                             00000009     69 - LOAD_ATTR           'isUsingWeapon'
                             0000000C     7C - LOAD_FAST           'tactic'
                             0000000F     69 - LOAD_ATTR           'itemID'
                             00000012     83 - CALL_FUNCTION       r0001
                             00000015     6F - JUMP_IF_FALSE       -> 0000002F
                             00000018     01 - POP_TOP             
                             00000019     7C - LOAD_FAST           'innerstrength_amount'
                             0000001C     74 - LOAD_GLOBAL         'calcInnerStrengthWithGun'
                             0000001F     7C - LOAD_FAST           'tactic'
                             00000022     69 - LOAD_ATTR           'tacticalSetting'
                             00000025     83 - CALL_FUNCTION       r0001
                             00000028     37 - INPLACE_ADD         
                             00000029     7D - STORE_FAST          'innerstrength_amount'
                             0000002C     6E - JUMP_FORWARD        -> 0000006D
                             0000002F     01 - POP_TOP             
                             00000030     74 - LOAD_GLOBAL         'CU'
                             00000033     69 - LOAD_ATTR           'isAbilityMartialArt'
                             00000036     7C - LOAD_FAST           'tactic'
                             00000039     69 - LOAD_ATTR           'martialArt'
                             0000003C     83 - CALL_FUNCTION       r0001
                             0000003F     6F - JUMP_IF_FALSE       -> 00000059
                             00000042     01 - POP_TOP             
                             00000043     7C - LOAD_FAST           'innerstrength_amount'
                             00000046     74 - LOAD_GLOBAL         'calcInnerStrengthWithMartialArt'
                             00000049     7C - LOAD_FAST           'tactic'
                             0000004C     69 - LOAD_ATTR           'tacticalSetting'
                             0000004F     83 - CALL_FUNCTION       r0001
                             00000052     37 - INPLACE_ADD         
                             00000053     7D - STORE_FAST          'innerstrength_amount'
                             00000056     6E - JUMP_FORWARD        -> 0000006D
                             00000059     01 - POP_TOP             
                             0000005A     7C - LOAD_FAST           'innerstrength_amount'
                             0000005D     74 - LOAD_GLOBAL         'calcInnerStrengthWithSelfDefense'
                             00000060     7C - LOAD_FAST           'tactic'
                             00000063     69 - LOAD_ATTR           'tacticalSetting'
                             00000066     83 - CALL_FUNCTION       r0001
                             00000069     37 - INPLACE_ADD         
                             0000006A     7D - STORE_FAST          'innerstrength_amount'
                             0000006D     7C - LOAD_FAST           'innerstrength_amount'
                             00000070     53 - RETURN_VALUE        
                             00000071     64 - LOAD_CONST          None
                             00000074     53 - RETURN_VALUE        
                         consts:
00000652                     TUPLE: (
00000657                         None (4E),
00000658                         INT: 0 (00 00 00 00)
                             )
                         names:
0000065D                     TUPLE: (
00000662                         STR: 'innerstrength_amount' (14 00 00 00 69 6E 6E 65 72 73 74 72 65 6E 67 74 68 5F 61 6D 6F 75 6E 74),
0000067B                         STR: 'CU' (02 00 00 00 43 55),
00000682                         STR: 'isUsingWeapon' (0D 00 00 00 69 73 55 73 69 6E 67 57 65 61 70 6F 6E),
00000694                         STR: 'tactic' (06 00 00 00 74 61 63 74 69 63),
0000069F                         STR: 'itemID' (06 00 00 00 69 74 65 6D 49 44),
000006AA                         STR: 'calcInnerStrengthWithGun' (18 00 00 00 63 61 6C 63 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 57 69 74 68 47 75 6E),
000006C7                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
000006DB                         STR: 'isAbilityMartialArt' (13 00 00 00 69 73 41 62 69 6C 69 74 79 4D 61 72 74 69 61 6C 41 72 74),
000006F3                         STR: 'martialArt' (0A 00 00 00 6D 61 72 74 69 61 6C 41 72 74),
00000702                         STR: 'calcInnerStrengthWithMartialArt' (1F 00 00 00 63 61 6C 63 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 57 69 74 68 4D 61 72 74 69 61 6C 41 72 74),
00000726                         STR: 'calcInnerStrengthWithSelfDefense' (20 00 00 00 63 61 6C 63 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 57 69 74 68 53 65 6C 66 44 65 66 65 6E 73 65)
                             )
                         varnames:
0000074B                     TUPLE: (
00000750                         STR: 'tactic' (06 00 00 00 74 61 63 74 69 63),
0000075B                         STR: 'innerstrength_amount' (14 00 00 00 69 6E 6E 65 72 73 74 72 65 6E 67 74 68 5F 61 6D 6F 75 6E 74)
                             )
                         freevars:
00000774                     TUPLE: ()
                         cellvars:
00000779                     TUPLE: ()
                         filename:
0000077E                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_innerstrength.py' (56 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 69 6E 6E 65 72 73 74 72 65 6E 67 74 68 2E 70 79)
                         name:
000007D9                     STR: 'calcInnerStrengthForWinner' (1A 00 00 00 63 61 6C 63 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 46 6F 72 57 69 6E 6E 65 72)
                         firslineno:
000007F8                     LONG: 45L (2D 00 00 00)
                         lnotab:
000007FC                     STR: '\x00\x01\x06\x02\x13\x01\x17\x01\x13\x01\x17\x02\x13\x02' (0E 00 00 00 00 01 06 02 13 01 17 01 13 01 17 02 13 02),
0000080F             CODE:
                         argcount:
00000810                     LONG: 1L (01 00 00 00)
                         nlocals:
00000814                     LONG: 2L (02 00 00 00)
                         stacksize:
00000818                     LONG: 3L (03 00 00 00)
                         flags:
0000081C                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000820                     STR: 'd\x01\x00}\x01\x00t\x01\x00i\x02\x00|\x00\x00i\x04\x00\x83\x01\x00o\x17\x00\x01|\x01\x00t\x05\x00|\x00\x00i\x06\x00\x83\x01\x007}\x01\x00n>\x00\x01t\x01\x00i\x07\x00|\x00\x00i\x08\x00\x83\x01\x00o\x17\x00\x01|\x01\x00t\t\x00|\x00\x00i\x06\x00\x83\x01\x007}\x01\x00n\x14\x00\x01|\x01\x00t\n\x00|\x00\x00i\x06\x00\x83\x01\x007}\x01\x00|\x01\x00Sd\x00\x00S' (75 00 00 00 64 01 00 7D 01 00 74 01 00 69 02 00 7C 00 00 69 04 00 83 01 00 6F 17 00 01 7C 01 00 74 05 00 7C 00 00 69 06 00 83 01 00 37 7D 01 00 6E 3E 00 01 74 01 00 69 07 00 7C 00 00 69 08 00 83 01 00 6F 17 00 01 7C 01 00 74 09 00 7C 00 00 69 06 00 83 01 00 37 7D 01 00 6E 14 00 01 7C 01 00 74 0A 00 7C 00 00 69 06 00 83 01 00 37 7D 01 00 7C 01 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          0
                             00000003     7D - STORE_FAST          'innerstrength_amount'
                             00000006     74 - LOAD_GLOBAL         'CU'
                             00000009     69 - LOAD_ATTR           'isUsingWeapon'
                             0000000C     7C - LOAD_FAST           'tactic'
                             0000000F     69 - LOAD_ATTR           'itemID'
                             00000012     83 - CALL_FUNCTION       r0001
                             00000015     6F - JUMP_IF_FALSE       -> 0000002F
                             00000018     01 - POP_TOP             
                             00000019     7C - LOAD_FAST           'innerstrength_amount'
                             0000001C     74 - LOAD_GLOBAL         'calcInnerStrengthWithGun'
                             0000001F     7C - LOAD_FAST           'tactic'
                             00000022     69 - LOAD_ATTR           'tacticalSetting'
                             00000025     83 - CALL_FUNCTION       r0001
                             00000028     37 - INPLACE_ADD         
                             00000029     7D - STORE_FAST          'innerstrength_amount'
                             0000002C     6E - JUMP_FORWARD        -> 0000006D
                             0000002F     01 - POP_TOP             
                             00000030     74 - LOAD_GLOBAL         'CU'
                             00000033     69 - LOAD_ATTR           'isAbilityMartialArt'
                             00000036     7C - LOAD_FAST           'tactic'
                             00000039     69 - LOAD_ATTR           'martialArt'
                             0000003C     83 - CALL_FUNCTION       r0001
                             0000003F     6F - JUMP_IF_FALSE       -> 00000059
                             00000042     01 - POP_TOP             
                             00000043     7C - LOAD_FAST           'innerstrength_amount'
                             00000046     74 - LOAD_GLOBAL         'calcInnerStrengthWithMartialArt'
                             00000049     7C - LOAD_FAST           'tactic'
                             0000004C     69 - LOAD_ATTR           'tacticalSetting'
                             0000004F     83 - CALL_FUNCTION       r0001
                             00000052     37 - INPLACE_ADD         
                             00000053     7D - STORE_FAST          'innerstrength_amount'
                             00000056     6E - JUMP_FORWARD        -> 0000006D
                             00000059     01 - POP_TOP             
                             0000005A     7C - LOAD_FAST           'innerstrength_amount'
                             0000005D     74 - LOAD_GLOBAL         'calcInnerStrengthWithSelfDefense'
                             00000060     7C - LOAD_FAST           'tactic'
                             00000063     69 - LOAD_ATTR           'tacticalSetting'
                             00000066     83 - CALL_FUNCTION       r0001
                             00000069     37 - INPLACE_ADD         
                             0000006A     7D - STORE_FAST          'innerstrength_amount'
                             0000006D     7C - LOAD_FAST           'innerstrength_amount'
                             00000070     53 - RETURN_VALUE        
                             00000071     64 - LOAD_CONST          None
                             00000074     53 - RETURN_VALUE        
                         consts:
0000089A                     TUPLE: (
0000089F                         None (4E),
000008A0                         INT: 0 (00 00 00 00)
                             )
                         names:
000008A5                     TUPLE: (
000008AA                         STR: 'innerstrength_amount' (14 00 00 00 69 6E 6E 65 72 73 74 72 65 6E 67 74 68 5F 61 6D 6F 75 6E 74),
000008C3                         STR: 'CU' (02 00 00 00 43 55),
000008CA                         STR: 'isUsingWeapon' (0D 00 00 00 69 73 55 73 69 6E 67 57 65 61 70 6F 6E),
000008DC                         STR: 'tactic' (06 00 00 00 74 61 63 74 69 63),
000008E7                         STR: 'itemID' (06 00 00 00 69 74 65 6D 49 44),
000008F2                         STR: 'calcInnerStrengthWithGun' (18 00 00 00 63 61 6C 63 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 57 69 74 68 47 75 6E),
0000090F                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
00000923                         STR: 'isAbilityMartialArt' (13 00 00 00 69 73 41 62 69 6C 69 74 79 4D 61 72 74 69 61 6C 41 72 74),
0000093B                         STR: 'martialArt' (0A 00 00 00 6D 61 72 74 69 61 6C 41 72 74),
0000094A                         STR: 'calcInnerStrengthWithMartialArt' (1F 00 00 00 63 61 6C 63 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 57 69 74 68 4D 61 72 74 69 61 6C 41 72 74),
0000096E                         STR: 'calcInnerStrengthWithSelfDefense' (20 00 00 00 63 61 6C 63 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 57 69 74 68 53 65 6C 66 44 65 66 65 6E 73 65)
                             )
                         varnames:
00000993                     TUPLE: (
00000998                         STR: 'tactic' (06 00 00 00 74 61 63 74 69 63),
000009A3                         STR: 'innerstrength_amount' (14 00 00 00 69 6E 6E 65 72 73 74 72 65 6E 67 74 68 5F 61 6D 6F 75 6E 74)
                             )
                         freevars:
000009BC                     TUPLE: ()
                         cellvars:
000009C1                     TUPLE: ()
                         filename:
000009C6                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_innerstrength.py' (56 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 69 6E 6E 65 72 73 74 72 65 6E 67 74 68 2E 70 79)
                         name:
00000A21                     STR: 'calcInnerStrengthForLoser' (19 00 00 00 63 61 6C 63 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 46 6F 72 4C 6F 73 65 72)
                         firslineno:
00000A3F                     LONG: 57L (39 00 00 00)
                         lnotab:
00000A43                     STR: '\x00\x01\x06\x02\x13\x01\x17\x01\x13\x01\x17\x02\x13\x02' (0E 00 00 00 00 01 06 02 13 01 17 01 13 01 17 02 13 02)
                 )
             names:
00000A56         TUPLE: (
00000A5B             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00000A66             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00000A74             STR: 'obj' (03 00 00 00 6F 62 6A),
00000A7C             STR: 'combat_defines' (0E 00 00 00 63 6F 6D 62 61 74 5F 64 65 66 69 6E 65 73),
00000A8F             STR: 'CD' (02 00 00 00 43 44),
00000A96             STR: 'math' (04 00 00 00 6D 61 74 68),
00000A9F             STR: 'combat_utility' (0E 00 00 00 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79),
00000AB2             STR: 'CU' (02 00 00 00 43 55),
00000AB9             STR: 'calcInnerStrengthWithSelfDefense' (20 00 00 00 63 61 6C 63 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 57 69 74 68 53 65 6C 66 44 65 66 65 6E 73 65),
00000ADE             STR: 'calcInnerStrengthWithMartialArt' (1F 00 00 00 63 61 6C 63 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 57 69 74 68 4D 61 72 74 69 61 6C 41 72 74),
00000B02             STR: 'calcInnerStrengthWithGun' (18 00 00 00 63 61 6C 63 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 57 69 74 68 47 75 6E),
00000B1F             STR: 'calcInnerStrengthForWinner' (1A 00 00 00 63 61 6C 63 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 46 6F 72 57 69 6E 6E 65 72),
00000B3E             STR: 'calcInnerStrengthForLoser' (19 00 00 00 63 61 6C 63 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 46 6F 72 4C 6F 73 65 72)
                 )
             varnames:
00000B5C         TUPLE: (
00000B61             STR: 'calcInnerStrengthWithMartialArt' (1F 00 00 00 63 61 6C 63 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 57 69 74 68 4D 61 72 74 69 61 6C 41 72 74),
00000B85             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00000B93             STR: 'obj' (03 00 00 00 6F 62 6A),
00000B9B             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00000BA6             STR: 'CD' (02 00 00 00 43 44),
00000BAD             STR: 'calcInnerStrengthWithSelfDefense' (20 00 00 00 63 61 6C 63 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 57 69 74 68 53 65 6C 66 44 65 66 65 6E 73 65),
00000BD2             STR: 'math' (04 00 00 00 6D 61 74 68),
00000BDB             STR: 'calcInnerStrengthWithGun' (18 00 00 00 63 61 6C 63 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 57 69 74 68 47 75 6E),
00000BF8             STR: 'calcInnerStrengthForLoser' (19 00 00 00 63 61 6C 63 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 46 6F 72 4C 6F 73 65 72),
00000C16             STR: 'calcInnerStrengthForWinner' (1A 00 00 00 63 61 6C 63 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 46 6F 72 57 69 6E 6E 65 72),
00000C35             STR: 'CU' (02 00 00 00 43 55)
                 )
             freevars:
00000C3C         TUPLE: ()
             cellvars:
00000C41         TUPLE: ()
             filename:
00000C46         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_innerstrength.py' (56 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 69 6E 6E 65 72 73 74 72 65 6E 67 74 68 2E 70 79)
             name:
00000CA1         STR: '?' (01 00 00 00 3F)
             firslineno:
00000CA7         LONG: 1L (01 00 00 00)
             lnotab:
00000CAB         STR: '\t\x01\t\x01\t\x01\t\x01\t\x01\t\x03\t\x0c\t\x0c\t\x0c\t\x0c' (14 00 00 00 09 01 09 01 09 01 09 01 09 01 09 03 09 0C 09 0C 09 0C 09 0C)

