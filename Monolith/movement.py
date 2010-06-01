--== Disasm ==--
00000008 CODE:
             argcount:
00000009         LONG: 0L (00 00 00 00)
             nlocals:
0000000D         LONG: 0L (00 00 00 00)
             stacksize:
00000011         LONG: 26L (1A 00 00 00)
             flags:
00000015         LONG: 64L (40 00 00 00)
                 (NOFREE)
             code:
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x01\x00d\x02\x00d\x03\x00d\x04\x00d\x05\x00d\x06\x00d\x07\x00d\x08\x00d\t\x00d\n\x00d\x0b\x00d\x0c\x00d\r\x00d\x0e\x00d\x0f\x00d\x10\x00d\x11\x00d\x12\x00d\x13\x00d\x14\x00d\x15\x00d\x16\x00d\x17\x00d\x18\x00d\x19\x00d\x1a\x00g\x1a\x00Z\x01\x00d\x1b\x00\x84\x00\x00Z\x02\x00e\x02\x00\x83\x00\x00\x01d\x1c\x00\x84\x00\x00Z\x03\x00d\x00\x00S' (7A 00 00 00 64 00 00 6B 00 00 5A 00 00 64 01 00 64 02 00 64 03 00 64 04 00 64 05 00 64 06 00 64 07 00 64 08 00 64 09 00 64 0A 00 64 0B 00 64 0C 00 64 0D 00 64 0E 00 64 0F 00 64 10 00 64 11 00 64 12 00 64 13 00 64 14 00 64 15 00 64 16 00 64 17 00 64 18 00 64 19 00 64 1A 00 67 1A 00 5A 01 00 64 1B 00 84 00 00 5A 02 00 65 02 00 83 00 00 01 64 1C 00 84 00 00 5A 03 00 64 00 00 53)
                 00000000     64 - LOAD_CONST          None
                 00000003     6B - IMPORT_NAME         'traceback'
                 00000006     5A - STORE_NAME          'traceback'
                 00000009     64 - LOAD_CONST          'None'
                 0000000C     64 - LOAD_CONST          'Confused'
                 0000000F     64 - LOAD_CONST          'Stunned'
                 00000012     64 - LOAD_CONST          'Enraged'
                 00000015     64 - LOAD_CONST          'Blind'
                 00000018     64 - LOAD_CONST          'Powerless'
                 0000001B     64 - LOAD_CONST          'Dazed'
                 0000001E     64 - LOAD_CONST          'Staggered'
                 00000021     64 - LOAD_CONST          'OffBalance'
                 00000024     64 - LOAD_CONST          'Sexy'
                 00000027     64 - LOAD_CONST          'Sultry'
                 0000002A     64 - LOAD_CONST          'Shy'
                 0000002D     64 - LOAD_CONST          'Shifty'
                 00000030     64 - LOAD_CONST          'Regal'
                 00000033     64 - LOAD_CONST          'Cocky'
                 00000036     64 - LOAD_CONST          'Stoic'
                 00000039     64 - LOAD_CONST          'Fidgety'
                 0000003C     64 - LOAD_CONST          'Sly'
                 0000003F     64 - LOAD_CONST          'Cautious'
                 00000042     64 - LOAD_CONST          'Aggressive'
                 00000045     64 - LOAD_CONST          'Bouncy'
                 00000048     64 - LOAD_CONST          'Casual'
                 0000004B     64 - LOAD_CONST          'Drunk'
                 0000004E     64 - LOAD_CONST          'Hurt'
                 00000051     64 - LOAD_CONST          'Cold'
                 00000054     64 - LOAD_CONST          'Umbrella'
                 00000057     67 - BUILD_LIST          r001A
                 0000005A     5A - STORE_NAME          'demeanors'
                 0000005D     64 - LOAD_CONST          CODE('Init')
                 00000060     84 - MAKE_FUNCTION       r0000
                 00000063     5A - STORE_NAME          'Init'
                 00000066     65 - LOAD_NAME           'Init'
                 00000069     83 - CALL_FUNCTION       r0000
                 0000006C     01 - POP_TOP             
                 0000006D     64 - LOAD_CONST          CODE('GetDemeanorList')
                 00000070     84 - MAKE_FUNCTION       r0000
                 00000073     5A - STORE_NAME          'GetDemeanorList'
                 00000076     64 - LOAD_CONST          None
                 00000079     53 - RETURN_VALUE        
             consts:
00000098         TUPLE: (
0000009D             None (4E),
0000009E             STR: 'None' (04 00 00 00 4E 6F 6E 65),
000000A7             STR: 'Confused' (08 00 00 00 43 6F 6E 66 75 73 65 64),
000000B4             STR: 'Stunned' (07 00 00 00 53 74 75 6E 6E 65 64),
000000C0             STR: 'Enraged' (07 00 00 00 45 6E 72 61 67 65 64),
000000CC             STR: 'Blind' (05 00 00 00 42 6C 69 6E 64),
000000D6             STR: 'Powerless' (09 00 00 00 50 6F 77 65 72 6C 65 73 73),
000000E4             STR: 'Dazed' (05 00 00 00 44 61 7A 65 64),
000000EE             STR: 'Staggered' (09 00 00 00 53 74 61 67 67 65 72 65 64),
000000FC             STR: 'OffBalance' (0A 00 00 00 4F 66 66 42 61 6C 61 6E 63 65),
0000010B             STR: 'Sexy' (04 00 00 00 53 65 78 79),
00000114             STR: 'Sultry' (06 00 00 00 53 75 6C 74 72 79),
0000011F             STR: 'Shy' (03 00 00 00 53 68 79),
00000127             STR: 'Shifty' (06 00 00 00 53 68 69 66 74 79),
00000132             STR: 'Regal' (05 00 00 00 52 65 67 61 6C),
0000013C             STR: 'Cocky' (05 00 00 00 43 6F 63 6B 79),
00000146             STR: 'Stoic' (05 00 00 00 53 74 6F 69 63),
00000150             STR: 'Fidgety' (07 00 00 00 46 69 64 67 65 74 79),
0000015C             STR: 'Sly' (03 00 00 00 53 6C 79),
00000164             STR: 'Cautious' (08 00 00 00 43 61 75 74 69 6F 75 73),
00000171             STR: 'Aggressive' (0A 00 00 00 41 67 67 72 65 73 73 69 76 65),
00000180             STR: 'Bouncy' (06 00 00 00 42 6F 75 6E 63 79),
0000018B             STR: 'Casual' (06 00 00 00 43 61 73 75 61 6C),
00000196             STR: 'Drunk' (05 00 00 00 44 72 75 6E 6B),
000001A0             STR: 'Hurt' (04 00 00 00 48 75 72 74),
000001A9             STR: 'Cold' (04 00 00 00 43 6F 6C 64),
000001B2             STR: 'Umbrella' (08 00 00 00 55 6D 62 72 65 6C 6C 61),
000001BF             CODE:
                         argcount:
000001C0                     LONG: 0L (00 00 00 00)
                         nlocals:
000001C4                     LONG: 3L (03 00 00 00)
                         stacksize:
000001C8                     LONG: 4L (04 00 00 00)
                         flags:
000001CC                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000001D0                     STR: 't\x00\x00\x83\x00\x00}\x00\x00d\x01\x00}\x02\x00xP\x00t\x03\x00D]H\x00}\x01\x00|\x01\x00i\x05\x00d\x02\x00d\x03\x00\x83\x02\x00}\x01\x00|\x01\x00i\x05\x00d\x04\x00d\x03\x00\x83\x02\x00}\x01\x00d\x05\x00|\x01\x00\x17}\x01\x00|\x02\x00|\x00\x00|\x01\x00<|\x02\x00d\x06\x007}\x02\x00q\x16\x00Wd\x00\x00S' (66 00 00 00 74 00 00 83 00 00 7D 00 00 64 01 00 7D 02 00 78 50 00 74 03 00 44 5D 48 00 7D 01 00 7C 01 00 69 05 00 64 02 00 64 03 00 83 02 00 7D 01 00 7C 01 00 69 05 00 64 04 00 64 03 00 83 02 00 7D 01 00 64 05 00 7C 01 00 17 7D 01 00 7C 02 00 7C 00 00 7C 01 00 3C 7C 02 00 64 06 00 37 7D 02 00 71 16 00 57 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'globals'
                             00000003     83 - CALL_FUNCTION       r0000
                             00000006     7D - STORE_FAST          'globs'
                             00000009     64 - LOAD_CONST          0
                             0000000C     7D - STORE_FAST          'offset'
                             0000000F     78 - SETUP_LOOP          -> 00000062
                             00000012     74 - LOAD_GLOBAL         'demeanors'
                             00000015     44 - GET_ITER            
                             00000016     5D - FOR_ITER            -> 00000061
                             00000019     7D - STORE_FAST          'name'
                             0000001C     7C - LOAD_FAST           'name'
                             0000001F     69 - LOAD_ATTR           'replace'
                             00000022     64 - LOAD_CONST          ' '
                             00000025     64 - LOAD_CONST          ''
                             00000028     83 - CALL_FUNCTION       r0002
                             0000002B     7D - STORE_FAST          'name'
                             0000002E     7C - LOAD_FAST           'name'
                             00000031     69 - LOAD_ATTR           'replace'
                             00000034     64 - LOAD_CONST          '-'
                             00000037     64 - LOAD_CONST          ''
                             0000003A     83 - CALL_FUNCTION       r0002
                             0000003D     7D - STORE_FAST          'name'
                             00000040     64 - LOAD_CONST          'Demeanor_'
                             00000043     7C - LOAD_FAST           'name'
                             00000046     17 - BINARY_ADD          
                             00000047     7D - STORE_FAST          'name'
                             0000004A     7C - LOAD_FAST           'offset'
                             0000004D     7C - LOAD_FAST           'globs'
                             00000050     7C - LOAD_FAST           'name'
                             00000053     3C - STORE_SUBSCR        
                             00000054     7C - LOAD_FAST           'offset'
                             00000057     64 - LOAD_CONST          1
                             0000005A     37 - INPLACE_ADD         
                             0000005B     7D - STORE_FAST          'offset'
                             0000005E     71 - JUMP_ABSOLUTE       -> 00000016
                             00000061     57 - POP_BLOCK           
                             00000062     64 - LOAD_CONST          None
                             00000065     53 - RETURN_VALUE        
                         consts:
0000023B                     TUPLE: (
00000240                         None (4E),
00000241                         INT: 0 (00 00 00 00),
00000246                         STR: ' ' (01 00 00 00 20),
0000024C                         STR: '' (00 00 00 00),
00000251                         STR: '-' (01 00 00 00 2D),
00000257                         STR: 'Demeanor_' (09 00 00 00 44 65 6D 65 61 6E 6F 72 5F),
00000265                         INT: 1 (01 00 00 00)
                             )
                         names:
0000026A                     TUPLE: (
0000026F                         STR: 'globals' (07 00 00 00 67 6C 6F 62 61 6C 73),
0000027B                         STR: 'globs' (05 00 00 00 67 6C 6F 62 73),
00000285                         STR: 'offset' (06 00 00 00 6F 66 66 73 65 74),
00000290                         STR: 'demeanors' (09 00 00 00 64 65 6D 65 61 6E 6F 72 73),
0000029E                         STR: 'name' (04 00 00 00 6E 61 6D 65),
000002A7                         STR: 'replace' (07 00 00 00 72 65 70 6C 61 63 65)
                             )
                         varnames:
000002B3                     TUPLE: (
000002B8                         STR: 'globs' (05 00 00 00 67 6C 6F 62 73),
000002C2                         STR: 'name' (04 00 00 00 6E 61 6D 65),
000002CB                         STR: 'offset' (06 00 00 00 6F 66 66 73 65 74)
                             )
                         freevars:
000002D6                     TUPLE: ()
                         cellvars:
000002DB                     TUPLE: ()
                         filename:
000002E0                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\movement.py' (40 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6D 6F 76 65 6D 65 6E 74 2E 70 79)
                         name:
00000325                     STR: 'Init' (04 00 00 00 49 6E 69 74)
                         firslineno:
0000032E                     LONG: 38L (26 00 00 00)
                         lnotab:
00000332                     STR: '\x00\x02\t\x01\x06\x01\x07\x00\x06\x01\x12\x01\x12\x01\n\x02\n\x02' (12 00 00 00 00 02 09 01 06 01 07 00 06 01 12 01 12 01 0A 02 0A 02),
00000349             CODE:
                         argcount:
0000034A                     LONG: 0L (00 00 00 00)
                         nlocals:
0000034E                     LONG: 0L (00 00 00 00)
                         stacksize:
00000352                     LONG: 1L (01 00 00 00)
                         flags:
00000356                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000035A                     STR: 't\x00\x00Sd\x00\x00S' (08 00 00 00 74 00 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'demeanors'
                             00000003     53 - RETURN_VALUE        
                             00000004     64 - LOAD_CONST          None
                             00000007     53 - RETURN_VALUE        
                         consts:
00000367                     TUPLE: (
0000036C                         None (4E)
                             )
                         names:
0000036D                     TUPLE: (
00000372                         STR: 'demeanors' (09 00 00 00 64 65 6D 65 61 6E 6F 72 73)
                             )
                         varnames:
00000380                     TUPLE: ()
                         freevars:
00000385                     TUPLE: ()
                         cellvars:
0000038A                     TUPLE: ()
                         filename:
0000038F                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\movement.py' (40 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6D 6F 76 65 6D 65 6E 74 2E 70 79)
                         name:
000003D4                     STR: 'GetDemeanorList' (0F 00 00 00 47 65 74 44 65 6D 65 61 6E 6F 72 4C 69 73 74)
                         firslineno:
000003E8                     LONG: 58L (3A 00 00 00)
                         lnotab:
000003EC                     STR: '\x00\x01' (02 00 00 00 00 01)
                 )
             names:
000003F3         TUPLE: (
000003F8             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00000406             STR: 'demeanors' (09 00 00 00 64 65 6D 65 61 6E 6F 72 73),
00000414             STR: 'Init' (04 00 00 00 49 6E 69 74),
0000041D             STR: 'GetDemeanorList' (0F 00 00 00 47 65 74 44 65 6D 65 61 6E 6F 72 4C 69 73 74)
                 )
             varnames:
00000431         TUPLE: (
00000436             STR: 'demeanors' (09 00 00 00 64 65 6D 65 61 6E 6F 72 73),
00000444             STR: 'Init' (04 00 00 00 49 6E 69 74),
0000044D             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
0000045B             STR: 'GetDemeanorList' (0F 00 00 00 47 65 74 44 65 6D 65 61 6E 6F 72 4C 69 73 74)
                 )
             freevars:
0000046F         TUPLE: ()
             cellvars:
00000474         TUPLE: ()
             filename:
00000479         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\movement.py' (40 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6D 6F 76 65 6D 65 6E 74 2E 70 79)
             name:
000004BE         STR: '?' (01 00 00 00 3F)
             firslineno:
000004C4         LONG: 2L (02 00 00 00)
             lnotab:
000004C8         STR: '\t\x05T\x1f\t\r\x07\x07' (08 00 00 00 09 05 54 1F 09 0D 07 07)

