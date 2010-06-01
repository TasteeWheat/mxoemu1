--== Disasm ==--
00000008 CODE:
             argcount:
00000009         LONG: 0L (00 00 00 00)
             nlocals:
0000000D         LONG: 0L (00 00 00 00)
             stacksize:
00000011         LONG: 7L (07 00 00 00)
             flags:
00000015         LONG: 64L (40 00 00 00)
                 (NOFREE)
             code:
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x01\x00k\x02\x00l\x03\x00Z\x03\x00\x01d\x00\x00k\x04\x00Z\x04\x00d\x02\x00\x84\x00\x00Z\x05\x00d\x03\x00\x84\x00\x00Z\x06\x00d\x04\x00f\x00\x00d\x05\x00\x84\x00\x00\x83\x00\x00YZ\x07\x00d\x06\x00d\x07\x00e\x08\x00e\x08\x00d\x08\x00\x84\x04\x00Z\t\x00d\x06\x00d\x07\x00e\x08\x00e\x08\x00d\t\x00\x84\x04\x00Z\n\x00d\n\x00\x84\x00\x00Z\x0b\x00d\x0b\x00\x84\x00\x00Z\x0c\x00d\x0c\x00\x84\x00\x00Z\r\x00d\r\x00\x84\x00\x00Z\x0e\x00e\x0f\x00i\x10\x00i\x11\x00e\x0f\x00i\x12\x00i\x13\x00d\x0e\x00d\x0e\x00d\x0e\x00d\x0e\x00d\x0f\x00\x84\x06\x00Z\x14\x00d\x10\x00\x84\x00\x00Z\x15\x00d\x11\x00\x84\x00\x00Z\x16\x00e\x01\x00i\x01\x00\x83\x00\x00Z\x17\x00h\x00\x00Z\x18\x00d\x12\x00Z\x19\x00e\x1a\x00i\x1b\x00e\x19\x00\x83\x01\x00\x01e\x1a\x00i\x1c\x00e\x19\x00\x83\x01\x00\x01d\x00\x00S' (0A 01 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 01 00 6B 02 00 6C 03 00 5A 03 00 01 64 00 00 6B 04 00 5A 04 00 64 02 00 84 00 00 5A 05 00 64 03 00 84 00 00 5A 06 00 64 04 00 66 00 00 64 05 00 84 00 00 83 00 00 59 5A 07 00 64 06 00 64 07 00 65 08 00 65 08 00 64 08 00 84 04 00 5A 09 00 64 06 00 64 07 00 65 08 00 65 08 00 64 09 00 84 04 00 5A 0A 00 64 0A 00 84 00 00 5A 0B 00 64 0B 00 84 00 00 5A 0C 00 64 0C 00 84 00 00 5A 0D 00 64 0D 00 84 00 00 5A 0E 00 65 0F 00 69 10 00 69 11 00 65 0F 00 69 12 00 69 13 00 64 0E 00 64 0E 00 64 0E 00 64 0E 00 64 0F 00 84 06 00 5A 14 00 64 10 00 84 00 00 5A 15 00 64 11 00 84 00 00 5A 16 00 65 01 00 69 01 00 83 00 00 5A 17 00 68 00 00 5A 18 00 64 12 00 5A 19 00 65 1A 00 69 1B 00 65 19 00 83 01 00 01 65 1A 00 69 1C 00 65 19 00 83 01 00 01 64 00 00 53)
                 00000000     64 - LOAD_CONST          None
                 00000003     6B - IMPORT_NAME         'traceback'
                 00000006     5A - STORE_NAME          'traceback'
                 00000009     64 - LOAD_CONST          None
                 0000000C     6B - IMPORT_NAME         'RewardSelection'
                 0000000F     5A - STORE_NAME          'RewardSelection'
                 00000012     64 - LOAD_CONST          ('randint')
                 00000015     6B - IMPORT_NAME         'whrandom'
                 00000018     6C - IMPORT_FROM         'randint'
                 0000001B     5A - STORE_NAME          'randint'
                 0000001E     01 - POP_TOP             
                 0000001F     64 - LOAD_CONST          None
                 00000022     6B - IMPORT_NAME         'getopt'
                 00000025     5A - STORE_NAME          'getopt'
                 00000028     64 - LOAD_CONST          CODE('exceptionCB')
                 0000002B     84 - MAKE_FUNCTION       r0000
                 0000002E     5A - STORE_NAME          'exceptionCB'
                 00000031     64 - LOAD_CONST          CODE('ComputeHackConstructOutcome')
                 00000034     84 - MAKE_FUNCTION       r0000
                 00000037     5A - STORE_NAME          'ComputeHackConstructOutcome'
                 0000003A     64 - LOAD_CONST          'FakeGameObject'
                 0000003D     66 - BUILD_TUPLE         r0000
                 00000040     64 - LOAD_CONST          CODE('FakeGameObject')
                 00000043     84 - MAKE_FUNCTION       r0000
                 00000046     83 - CALL_FUNCTION       r0000
                 00000049     59 - BUILD_CLASS         
                 0000004A     5A - STORE_NAME          'FakeGameObject'
                 0000004D     64 - LOAD_CONST          'DefaultRewardRule'
                 00000050     64 - LOAD_CONST          'Table1'
                 00000053     65 - LOAD_NAME           'None'
                 00000056     65 - LOAD_NAME           'None'
                 00000059     64 - LOAD_CONST          CODE('MakeAndEncodeReward')
                 0000005C     84 - MAKE_FUNCTION       r0004
                 0000005F     5A - STORE_NAME          'MakeAndEncodeReward'
                 00000062     64 - LOAD_CONST          'DefaultRewardRule'
                 00000065     64 - LOAD_CONST          'Table1'
                 00000068     65 - LOAD_NAME           'None'
                 0000006B     65 - LOAD_NAME           'None'
                 0000006E     64 - LOAD_CONST          CODE('MakeRewardRoll')
                 00000071     84 - MAKE_FUNCTION       r0004
                 00000074     5A - STORE_NAME          'MakeRewardRoll'
                 00000077     64 - LOAD_CONST          CODE('GetRewardItemID')
                 0000007A     84 - MAKE_FUNCTION       r0000
                 0000007D     5A - STORE_NAME          'GetRewardItemID'
                 00000080     64 - LOAD_CONST          CODE('ReloadRewardSelection')
                 00000083     84 - MAKE_FUNCTION       r0000
                 00000086     5A - STORE_NAME          'ReloadRewardSelection'
                 00000089     64 - LOAD_CONST          CODE('FindMissionModule')
                 0000008C     84 - MAKE_FUNCTION       r0000
                 0000008F     5A - STORE_NAME          'FindMissionModule'
                 00000092     64 - LOAD_CONST          CODE('ParseMissionArgs')
                 00000095     84 - MAKE_FUNCTION       r0000
                 00000098     5A - STORE_NAME          'ParseMissionArgs'
                 0000009B     65 - LOAD_NAME           'constants'
                 0000009E     69 - LOAD_ATTR           'OrgPointType'
                 000000A1     69 - LOAD_ATTR           'OrgPointTypeInvalid'
                 000000A4     65 - LOAD_NAME           'constants'
                 000000A7     69 - LOAD_ATTR           'Organization'
                 000000AA     69 - LOAD_ATTR           'Invalid'
                 000000AD     64 - LOAD_CONST          0
                 000000B0     64 - LOAD_CONST          0
                 000000B3     64 - LOAD_CONST          0
                 000000B6     64 - LOAD_CONST          0
                 000000B9     64 - LOAD_CONST          CODE('HandleInvokeOrgEvent')
                 000000BC     84 - MAKE_FUNCTION       r0006
                 000000BF     5A - STORE_NAME          'HandleInvokeOrgEvent'
                 000000C2     64 - LOAD_CONST          CODE('HandleNeoCorpseEvents')
                 000000C5     84 - MAKE_FUNCTION       r0000
                 000000C8     5A - STORE_NAME          'HandleNeoCorpseEvents'
                 000000CB     64 - LOAD_CONST          CODE('HandleEvent2Events')
                 000000CE     84 - MAKE_FUNCTION       r0000
                 000000D1     5A - STORE_NAME          'HandleEvent2Events'
                 000000D4     65 - LOAD_NAME           'RewardSelection'
                 000000D7     69 - LOAD_ATTR           'RewardSelection'
                 000000DA     83 - CALL_FUNCTION       r0000
                 000000DD     5A - STORE_NAME          'rewardselection'
                 000000E0     68 - BUILD_MAP           r0000
                 000000E3     5A - STORE_NAME          'Missions'
                 000000E6     64 - LOAD_CONST          '-- Loaded TRGS.py'
                 000000E9     5A - STORE_NAME          'start_msg'
                 000000EC     65 - LOAD_NAME           'discovery'
                 000000EF     69 - LOAD_ATTR           'outputDebugString'
                 000000F2     65 - LOAD_NAME           'start_msg'
                 000000F5     83 - CALL_FUNCTION       r0001
                 000000F8     01 - POP_TOP             
                 000000F9     65 - LOAD_NAME           'discovery'
                 000000FC     69 - LOAD_ATTR           'serverPrint'
                 000000FF     65 - LOAD_NAME           'start_msg'
                 00000102     83 - CALL_FUNCTION       r0001
                 00000105     01 - POP_TOP             
                 00000106     64 - LOAD_CONST          None
                 00000109     53 - RETURN_VALUE        
             consts:
00000128         TUPLE: (
0000012D             None (4E),
0000012E             TUPLE: (
00000133                 STR: 'randint' (07 00 00 00 72 61 6E 64 69 6E 74)
                     ),
0000013F             CODE:
                         argcount:
00000140                     LONG: 3L (03 00 00 00)
                         nlocals:
00000144                     LONG: 5L (05 00 00 00)
                         stacksize:
00000148                     LONG: 5L (05 00 00 00)
                         flags:
0000014C                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000150                     STR: 'y\xb9\x00t\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01t\x00\x00i\x01\x00d\x02\x00\x83\x01\x00\x01t\x00\x00i\x01\x00|\x00\x00\r\x83\x01\x00\x01t\x00\x00i\x01\x00|\x01\x00\r\x83\x01\x00\x01t\x00\x00i\x01\x00d\x03\x00\x83\x01\x00\x01|\x02\x00oT\x00\x01t\x05\x00i\x06\x00|\x02\x00\x83\x01\x00}\x03\x00|\x03\x00i\x08\x00\x83\x00\x00\x01x8\x00|\x03\x00D],\x00}\x04\x00t\x00\x00i\x01\x00d\x04\x00|\x04\x00d\x05\x00 \x16\x83\x01\x00\x01t\x00\x00i\x01\x00|\x04\x00d\x05\x00\x19\x83\x01\x00\x01qm\x00Wn\x01\x00\x01t\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01t\x05\x00i\n\x00\x83\x00\x00\x01Wn\x11\x00\x01\x01\x01t\x05\x00i\n\x00\x83\x00\x00\x01n\x01\x00Xd\x00\x00S' (D1 00 00 00 79 B9 00 74 00 00 69 01 00 64 01 00 83 01 00 01 74 00 00 69 01 00 64 02 00 83 01 00 01 74 00 00 69 01 00 7C 00 00 0D 83 01 00 01 74 00 00 69 01 00 7C 01 00 0D 83 01 00 01 74 00 00 69 01 00 64 03 00 83 01 00 01 7C 02 00 6F 54 00 01 74 05 00 69 06 00 7C 02 00 83 01 00 7D 03 00 7C 03 00 69 08 00 83 00 00 01 78 38 00 7C 03 00 44 5D 2C 00 7D 04 00 74 00 00 69 01 00 64 04 00 7C 04 00 64 05 00 20 16 83 01 00 01 74 00 00 69 01 00 7C 04 00 64 05 00 19 83 01 00 01 71 6D 00 57 6E 01 00 01 74 00 00 69 01 00 64 01 00 83 01 00 01 74 05 00 69 0A 00 83 00 00 01 57 6E 11 00 01 01 01 74 05 00 69 0A 00 83 00 00 01 6E 01 00 58 64 00 00 53)
                             00000000     79 - SETUP_EXCEPT        -> 000000BC
                             00000003     74 - LOAD_GLOBAL         'discovery'
                             00000006     69 - LOAD_ATTR           'errorPrint'
                             00000009     64 - LOAD_CONST          '****************************************'
                             0000000C     83 - CALL_FUNCTION       r0001
                             0000000F     01 - POP_TOP             
                             00000010     74 - LOAD_GLOBAL         'discovery'
                             00000013     69 - LOAD_ATTR           'errorPrint'
                             00000016     64 - LOAD_CONST          'Rule Exception'
                             00000019     83 - CALL_FUNCTION       r0001
                             0000001C     01 - POP_TOP             
                             0000001D     74 - LOAD_GLOBAL         'discovery'
                             00000020     69 - LOAD_ATTR           'errorPrint'
                             00000023     7C - LOAD_FAST           'obj'
                             00000026     0D - UNARY_CONVERT       
                             00000027     83 - CALL_FUNCTION       r0001
                             0000002A     01 - POP_TOP             
                             0000002B     74 - LOAD_GLOBAL         'discovery'
                             0000002E     69 - LOAD_ATTR           'errorPrint'
                             00000031     7C - LOAD_FAST           'data'
                             00000034     0D - UNARY_CONVERT       
                             00000035     83 - CALL_FUNCTION       r0001
                             00000038     01 - POP_TOP             
                             00000039     74 - LOAD_GLOBAL         'discovery'
                             0000003C     69 - LOAD_ATTR           'errorPrint'
                             0000003F     64 - LOAD_CONST          '** traceback **'
                             00000042     83 - CALL_FUNCTION       r0001
                             00000045     01 - POP_TOP             
                             00000046     7C - LOAD_FAST           'tb'
                             00000049     6F - JUMP_IF_FALSE       -> 000000A0
                             0000004C     01 - POP_TOP             
                             0000004D     74 - LOAD_GLOBAL         'traceback'
                             00000050     69 - LOAD_ATTR           'extract_tb'
                             00000053     7C - LOAD_FAST           'tb'
                             00000056     83 - CALL_FUNCTION       r0001
                             00000059     7D - STORE_FAST          'stackTrace'
                             0000005C     7C - LOAD_FAST           'stackTrace'
                             0000005F     69 - LOAD_ATTR           'reverse'
                             00000062     83 - CALL_FUNCTION       r0000
                             00000065     01 - POP_TOP             
                             00000066     78 - SETUP_LOOP          -> 000000A1
                             00000069     7C - LOAD_FAST           'stackTrace'
                             0000006C     44 - GET_ITER            
                             0000006D     5D - FOR_ITER            -> 0000009C
                             00000070     7D - STORE_FAST          'tuple'
                             00000073     74 - LOAD_GLOBAL         'discovery'
                             00000076     69 - LOAD_ATTR           'errorPrint'
                             00000079     64 - LOAD_CONST          'File: %s (%d) Function: %s'
                             0000007C     7C - LOAD_FAST           'tuple'
                             0000007F     64 - LOAD_CONST          3
                             00000082     20 - SLICE+2             
                             00000083     16 - BINARY_MODULO       
                             00000084     83 - CALL_FUNCTION       r0001
                             00000087     01 - POP_TOP             
                             00000088     74 - LOAD_GLOBAL         'discovery'
                             0000008B     69 - LOAD_ATTR           'errorPrint'
                             0000008E     7C - LOAD_FAST           'tuple'
                             00000091     64 - LOAD_CONST          3
                             00000094     19 - BINARY_SUBSCR       
                             00000095     83 - CALL_FUNCTION       r0001
                             00000098     01 - POP_TOP             
                             00000099     71 - JUMP_ABSOLUTE       -> 0000006D
                             0000009C     57 - POP_BLOCK           
                             0000009D     6E - JUMP_FORWARD        -> 000000A1
                             000000A0     01 - POP_TOP             
                             000000A1     74 - LOAD_GLOBAL         'discovery'
                             000000A4     69 - LOAD_ATTR           'errorPrint'
                             000000A7     64 - LOAD_CONST          '****************************************'
                             000000AA     83 - CALL_FUNCTION       r0001
                             000000AD     01 - POP_TOP             
                             000000AE     74 - LOAD_GLOBAL         'traceback'
                             000000B1     69 - LOAD_ATTR           'print_exc'
                             000000B4     83 - CALL_FUNCTION       r0000
                             000000B7     01 - POP_TOP             
                             000000B8     57 - POP_BLOCK           
                             000000B9     6E - JUMP_FORWARD        -> 000000CD
                             000000BC     01 - POP_TOP             
                             000000BD     01 - POP_TOP             
                             000000BE     01 - POP_TOP             
                             000000BF     74 - LOAD_GLOBAL         'traceback'
                             000000C2     69 - LOAD_ATTR           'print_exc'
                             000000C5     83 - CALL_FUNCTION       r0000
                             000000C8     01 - POP_TOP             
                             000000C9     6E - JUMP_FORWARD        -> 000000CD
                             000000CC     58 - END_FINALLY         
                             000000CD     64 - LOAD_CONST          None
                             000000D0     53 - RETURN_VALUE        
                         consts:
00000226                     TUPLE: (
0000022B                         None (4E),
0000022C                         STR: '****************************************' (28 00 00 00 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A 2A),
00000259                         STR: 'Rule Exception' (0E 00 00 00 52 75 6C 65 20 45 78 63 65 70 74 69 6F 6E),
0000026C                         STR: '** traceback **' (0F 00 00 00 2A 2A 20 74 72 61 63 65 62 61 63 6B 20 2A 2A),
00000280                         STR: 'File: %s (%d) Function: %s' (1A 00 00 00 46 69 6C 65 3A 20 25 73 20 28 25 64 29 20 46 75 6E 63 74 69 6F 6E 3A 20 25 73),
0000029F                         INT: 3 (03 00 00 00)
                             )
                         names:
000002A4                     TUPLE: (
000002A9                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
000002B7                         STR: 'errorPrint' (0A 00 00 00 65 72 72 6F 72 50 72 69 6E 74),
000002C6                         STR: 'obj' (03 00 00 00 6F 62 6A),
000002CE                         STR: 'data' (04 00 00 00 64 61 74 61),
000002D7                         STR: 'tb' (02 00 00 00 74 62),
000002DE                         STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
000002EC                         STR: 'extract_tb' (0A 00 00 00 65 78 74 72 61 63 74 5F 74 62),
000002FB                         STR: 'stackTrace' (0A 00 00 00 73 74 61 63 6B 54 72 61 63 65),
0000030A                         STR: 'reverse' (07 00 00 00 72 65 76 65 72 73 65),
00000316                         STR: 'tuple' (05 00 00 00 74 75 70 6C 65),
00000320                         STR: 'print_exc' (09 00 00 00 70 72 69 6E 74 5F 65 78 63)
                             )
                         varnames:
0000032E                     TUPLE: (
00000333                         STR: 'obj' (03 00 00 00 6F 62 6A),
0000033B                         STR: 'data' (04 00 00 00 64 61 74 61),
00000344                         STR: 'tb' (02 00 00 00 74 62),
0000034B                         STR: 'stackTrace' (0A 00 00 00 73 74 61 63 6B 54 72 61 63 65),
0000035A                         STR: 'tuple' (05 00 00 00 74 75 70 6C 65)
                             )
                         freevars:
00000364                     TUPLE: ()
                         cellvars:
00000369                     TUPLE: ()
                         filename:
0000036E                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\trgs.py' (3C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 74 72 67 73 2E 70 79)
                         name:
000003AF                     STR: 'exceptionCB' (0B 00 00 00 65 78 63 65 70 74 69 6F 6E 43 42)
                         firslineno:
000003BF                     LONG: 16L (10 00 00 00)
                         lnotab:
000003C3                     STR: '\x00\x01\x03\x01\r\x01\r\x01\x0e\x01\x0e\x01\r\x02\x07\x01\x0f\x01\n\x01\x07\x00\x06\x01\x15\x01\x19\x02\r\x02\x0e\x01\x03\x01' (22 00 00 00 00 01 03 01 0D 01 0D 01 0E 01 0E 01 0D 02 07 01 0F 01 0A 01 07 00 06 01 15 01 19 02 0D 02 0E 01 03 01),
000003EA             CODE:
                         argcount:
000003EB                     LONG: 2L (02 00 00 00)
                         nlocals:
000003EF                     LONG: 2L (02 00 00 00)
                         stacksize:
000003F3                     LONG: 2L (02 00 00 00)
                         flags:
000003F7                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000003FB                     STR: 'd\x01\x00GHd\x02\x00G|\x00\x00Gd\x03\x00G|\x01\x00GH|\x00\x00t\x02\x00j\x08\x00o\x08\x00\x01d\x04\x00Sn\x01\x00\x01|\x00\x00|\x01\x00j\x04\x00o\r\x00\x01d\x05\x00GHd\x06\x00Sn\x01\x00\x01d\x07\x00GHd\x04\x00Sd\x00\x00S' (52 00 00 00 64 01 00 47 48 64 02 00 47 7C 00 00 47 64 03 00 47 7C 01 00 47 48 7C 00 00 74 02 00 6A 08 00 6F 08 00 01 64 04 00 53 6E 01 00 01 7C 00 00 7C 01 00 6A 04 00 6F 0D 00 01 64 05 00 47 48 64 06 00 53 6E 01 00 01 64 07 00 47 48 64 04 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          'TRGS - ComputeHackConstructOutcome()'
                             00000003     47 - PRINT_ITEM          
                             00000004     48 - PRINT_NEWLINE       
                             00000005     64 - LOAD_CONST          'abilityLevel = '
                             00000008     47 - PRINT_ITEM          
                             00000009     7C - LOAD_FAST           'abilityLevel'
                             0000000C     47 - PRINT_ITEM          
                             0000000D     64 - LOAD_CONST          'firewall defense = '
                             00000010     47 - PRINT_ITEM          
                             00000011     7C - LOAD_FAST           'constructDefense'
                             00000014     47 - PRINT_ITEM          
                             00000015     48 - PRINT_NEWLINE       
                             00000016     7C - LOAD_FAST           'abilityLevel'
                             00000019     74 - LOAD_GLOBAL         'None'
                             0000001C     6A - COMPARE_OP          "is"
                             0000001F     6F - JUMP_IF_FALSE       -> 0000002A
                             00000022     01 - POP_TOP             
                             00000023     64 - LOAD_CONST          0
                             00000026     53 - RETURN_VALUE        
                             00000027     6E - JUMP_FORWARD        -> 0000002B
                             0000002A     01 - POP_TOP             
                             0000002B     7C - LOAD_FAST           'abilityLevel'
                             0000002E     7C - LOAD_FAST           'constructDefense'
                             00000031     6A - COMPARE_OP          ">"
                             00000034     6F - JUMP_IF_FALSE       -> 00000044
                             00000037     01 - POP_TOP             
                             00000038     64 - LOAD_CONST          'TRGS - Hack construct succeeded!'
                             0000003B     47 - PRINT_ITEM          
                             0000003C     48 - PRINT_NEWLINE       
                             0000003D     64 - LOAD_CONST          1
                             00000040     53 - RETURN_VALUE        
                             00000041     6E - JUMP_FORWARD        -> 00000045
                             00000044     01 - POP_TOP             
                             00000045     64 - LOAD_CONST          'TRGS - Hack construct failed.'
                             00000048     47 - PRINT_ITEM          
                             00000049     48 - PRINT_NEWLINE       
                             0000004A     64 - LOAD_CONST          0
                             0000004D     53 - RETURN_VALUE        
                             0000004E     64 - LOAD_CONST          None
                             00000051     53 - RETURN_VALUE        
                         consts:
00000452                     TUPLE: (
00000457                         None (4E),
00000458                         STR: 'TRGS - ComputeHackConstructOutcome()' (24 00 00 00 54 52 47 53 20 2D 20 43 6F 6D 70 75 74 65 48 61 63 6B 43 6F 6E 73 74 72 75 63 74 4F 75 74 63 6F 6D 65 28 29),
00000481                         STR: 'abilityLevel = ' (0F 00 00 00 61 62 69 6C 69 74 79 4C 65 76 65 6C 20 3D 20),
00000495                         STR: 'firewall defense = ' (13 00 00 00 66 69 72 65 77 61 6C 6C 20 64 65 66 65 6E 73 65 20 3D 20),
000004AD                         INT: 0 (00 00 00 00),
000004B2                         STR: 'TRGS - Hack construct succeeded!' (20 00 00 00 54 52 47 53 20 2D 20 48 61 63 6B 20 63 6F 6E 73 74 72 75 63 74 20 73 75 63 63 65 65 64 65 64 21),
000004D7                         INT: 1 (01 00 00 00),
000004DC                         STR: 'TRGS - Hack construct failed.' (1D 00 00 00 54 52 47 53 20 2D 20 48 61 63 6B 20 63 6F 6E 73 74 72 75 63 74 20 66 61 69 6C 65 64 2E)
                             )
                         names:
000004FE                     TUPLE: (
00000503                         STR: 'abilityLevel' (0C 00 00 00 61 62 69 6C 69 74 79 4C 65 76 65 6C),
00000514                         STR: 'constructDefense' (10 00 00 00 63 6F 6E 73 74 72 75 63 74 44 65 66 65 6E 73 65),
00000529                         STR: 'None' (04 00 00 00 4E 6F 6E 65)
                             )
                         varnames:
00000532                     TUPLE: (
00000537                         STR: 'abilityLevel' (0C 00 00 00 61 62 69 6C 69 74 79 4C 65 76 65 6C),
00000548                         STR: 'constructDefense' (10 00 00 00 63 6F 6E 73 74 72 75 63 74 44 65 66 65 6E 73 65)
                             )
                         freevars:
0000055D                     TUPLE: ()
                         cellvars:
00000562                     TUPLE: ()
                         filename:
00000567                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\trgs.py' (3C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 74 72 67 73 2E 70 79)
                         name:
000005A8                     STR: 'ComputeHackConstructOutcome' (1B 00 00 00 43 6F 6D 70 75 74 65 48 61 63 6B 43 6F 6E 73 74 72 75 63 74 4F 75 74 63 6F 6D 65)
                         firslineno:
000005C8                     LONG: 41L (29 00 00 00)
                         lnotab:
000005CC                     STR: '\x00\x01\x05\x02\x11\x03\r\x01\x08\x03\r\x01\x05\x01\x08\x02\x05\x01' (12 00 00 00 00 01 05 02 11 03 0D 01 08 03 0D 01 05 01 08 02 05 01),
000005E3             STR: 'FakeGameObject' (0E 00 00 00 46 61 6B 65 47 61 6D 65 4F 62 6A 65 63 74),
000005F6             CODE:
                         argcount:
000005F7                     LONG: 0L (00 00 00 00)
                         nlocals:
000005FB                     LONG: 0L (00 00 00 00)
                         stacksize:
000005FF                     LONG: 1L (01 00 00 00)
                         flags:
00000603                     LONG: 66L (42 00 00 00)
                             (NEWLOCALS, NOFREE)
                         code:
00000607                     STR: 't\x00\x00Z\x01\x00d\x01\x00\x84\x00\x00Z\x02\x00RS' (11 00 00 00 74 00 00 5A 01 00 64 01 00 84 00 00 5A 02 00 52 53)
                             00000000     74 - LOAD_GLOBAL         '__name__'
                             00000003     5A - STORE_NAME          '__module__'
                             00000006     64 - LOAD_CONST          CODE('__init__')
                             00000009     84 - MAKE_FUNCTION       r0000
                             0000000C     5A - STORE_NAME          '__init__'
                             0000000F     52 - LOAD_LOCALS         
                             00000010     53 - RETURN_VALUE        
                         consts:
0000061D                     TUPLE: (
00000622                         None (4E),
00000623                         CODE:
                                     argcount:
00000624                                 LONG: 2L (02 00 00 00)
                                     nlocals:
00000628                                 LONG: 3L (03 00 00 00)
                                     stacksize:
0000062C                                 LONG: 4L (04 00 00 00)
                                     flags:
00000630                                 LONG: 67L (43 00 00 00)
                                         (OPTIMIZED, NEWLOCALS, NOFREE)
                                     code:
00000634                                 STR: '|\x01\x00t\x01\x00j\x08\x00o\x08\x00\x01d\x00\x00Sn\x01\x00\x01x\x1f\x00|\x01\x00D]\x17\x00}\x02\x00|\x01\x00|\x02\x00\x19|\x00\x00i\x04\x00|\x02\x00<q\x1c\x00Wd\x00\x00S' (3B 00 00 00 7C 01 00 74 01 00 6A 08 00 6F 08 00 01 64 00 00 53 6E 01 00 01 78 1F 00 7C 01 00 44 5D 17 00 7D 02 00 7C 01 00 7C 02 00 19 7C 00 00 69 04 00 7C 02 00 3C 71 1C 00 57 64 00 00 53)
                                         00000000     7C - LOAD_FAST           'props'
                                         00000003     74 - LOAD_GLOBAL         'None'
                                         00000006     6A - COMPARE_OP          "is"
                                         00000009     6F - JUMP_IF_FALSE       -> 00000014
                                         0000000C     01 - POP_TOP             
                                         0000000D     64 - LOAD_CONST          None
                                         00000010     53 - RETURN_VALUE        
                                         00000011     6E - JUMP_FORWARD        -> 00000015
                                         00000014     01 - POP_TOP             
                                         00000015     78 - SETUP_LOOP          -> 00000037
                                         00000018     7C - LOAD_FAST           'props'
                                         0000001B     44 - GET_ITER            
                                         0000001C     5D - FOR_ITER            -> 00000036
                                         0000001F     7D - STORE_FAST          'prop'
                                         00000022     7C - LOAD_FAST           'props'
                                         00000025     7C - LOAD_FAST           'prop'
                                         00000028     19 - BINARY_SUBSCR       
                                         00000029     7C - LOAD_FAST           'self'
                                         0000002C     69 - LOAD_ATTR           '__dict__'
                                         0000002F     7C - LOAD_FAST           'prop'
                                         00000032     3C - STORE_SUBSCR        
                                         00000033     71 - JUMP_ABSOLUTE       -> 0000001C
                                         00000036     57 - POP_BLOCK           
                                         00000037     64 - LOAD_CONST          None
                                         0000003A     53 - RETURN_VALUE        
                                     consts:
00000674                                 TUPLE: (
00000679                                     None (4E)
                                         )
                                     names:
0000067A                                 TUPLE: (
0000067F                                     STR: 'props' (05 00 00 00 70 72 6F 70 73),
00000689                                     STR: 'None' (04 00 00 00 4E 6F 6E 65),
00000692                                     STR: 'prop' (04 00 00 00 70 72 6F 70),
0000069B                                     STR: 'self' (04 00 00 00 73 65 6C 66),
000006A4                                     STR: '__dict__' (08 00 00 00 5F 5F 64 69 63 74 5F 5F)
                                         )
                                     varnames:
000006B1                                 TUPLE: (
000006B6                                     STR: 'self' (04 00 00 00 73 65 6C 66),
000006BF                                     STR: 'props' (05 00 00 00 70 72 6F 70 73),
000006C9                                     STR: 'prop' (04 00 00 00 70 72 6F 70)
                                         )
                                     freevars:
000006D2                                 TUPLE: ()
                                     cellvars:
000006D7                                 TUPLE: ()
                                     filename:
000006DC                                 STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\trgs.py' (3C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 74 72 67 73 2E 70 79)
                                     name:
0000071D                                 STR: '__init__' (08 00 00 00 5F 5F 69 6E 69 74 5F 5F)
                                     firslineno:
0000072A                                 LONG: 62L (3E 00 00 00)
                                     lnotab:
0000072E                                 STR: '\x00\x01\r\x01\x08\x02\x07\x00\x06\x01' (0A 00 00 00 00 01 0D 01 08 02 07 00 06 01)
                             )
                         names:
0000073D                     TUPLE: (
00000742                         STR: '__name__' (08 00 00 00 5F 5F 6E 61 6D 65 5F 5F),
0000074F                         STR: '__module__' (0A 00 00 00 5F 5F 6D 6F 64 75 6C 65 5F 5F),
0000075E                         STR: '__init__' (08 00 00 00 5F 5F 69 6E 69 74 5F 5F)
                             )
                         varnames:
0000076B                     TUPLE: ()
                         freevars:
00000770                     TUPLE: ()
                         cellvars:
00000775                     TUPLE: ()
                         filename:
0000077A                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\trgs.py' (3C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 74 72 67 73 2E 70 79)
                         name:
000007BB                     STR: 'FakeGameObject' (0E 00 00 00 46 61 6B 65 47 61 6D 65 4F 62 6A 65 63 74)
                         firslineno:
000007CE                     LONG: 61L (3D 00 00 00)
                         lnotab:
000007D2                     STR: '\x06\x01' (02 00 00 00 06 01),
000007D9             STR: 'DefaultRewardRule' (11 00 00 00 44 65 66 61 75 6C 74 52 65 77 61 72 64 52 75 6C 65),
000007EF             STR: 'Table1' (06 00 00 00 54 61 62 6C 65 31),
000007FA             CODE:
                         argcount:
000007FB                     LONG: 4L (04 00 00 00)
                         nlocals:
000007FF                     LONG: 6L (06 00 00 00)
                         stacksize:
00000803                     LONG: 5L (05 00 00 00)
                         flags:
00000807                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000080B                     STR: 't\x00\x00|\x02\x00\x83\x01\x00}\x04\x00t\x03\x00i\x04\x00|\x00\x00|\x01\x00|\x03\x00|\x04\x00\x83\x04\x00}\x05\x00|\x05\x00Sd\x00\x00S' (2C 00 00 00 74 00 00 7C 02 00 83 01 00 7D 04 00 74 03 00 69 04 00 7C 00 00 7C 01 00 7C 03 00 7C 04 00 83 04 00 7D 05 00 7C 05 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'FakeGameObject'
                             00000003     7C - LOAD_FAST           'dict'
                             00000006     83 - CALL_FUNCTION       r0001
                             00000009     7D - STORE_FAST          'fgo'
                             0000000C     74 - LOAD_GLOBAL         'rewardselection'
                             0000000F     69 - LOAD_ATTR           'DetermineEncodedReward'
                             00000012     7C - LOAD_FAST           'rule'
                             00000015     7C - LOAD_FAST           'table'
                             00000018     7C - LOAD_FAST           'args'
                             0000001B     7C - LOAD_FAST           'fgo'
                             0000001E     83 - CALL_FUNCTION       r0004
                             00000021     7D - STORE_FAST          'loot'
                             00000024     7C - LOAD_FAST           'loot'
                             00000027     53 - RETURN_VALUE        
                             00000028     64 - LOAD_CONST          None
                             0000002B     53 - RETURN_VALUE        
                         consts:
0000083C                     TUPLE: (
00000841                         None (4E)
                             )
                         names:
00000842                     TUPLE: (
00000847                         STR: 'FakeGameObject' (0E 00 00 00 46 61 6B 65 47 61 6D 65 4F 62 6A 65 63 74),
0000085A                         STR: 'dict' (04 00 00 00 64 69 63 74),
00000863                         STR: 'fgo' (03 00 00 00 66 67 6F),
0000086B                         STR: 'rewardselection' (0F 00 00 00 72 65 77 61 72 64 73 65 6C 65 63 74 69 6F 6E),
0000087F                         STR: 'DetermineEncodedReward' (16 00 00 00 44 65 74 65 72 6D 69 6E 65 45 6E 63 6F 64 65 64 52 65 77 61 72 64),
0000089A                         STR: 'rule' (04 00 00 00 72 75 6C 65),
000008A3                         STR: 'table' (05 00 00 00 74 61 62 6C 65),
000008AD                         STR: 'args' (04 00 00 00 61 72 67 73),
000008B6                         STR: 'loot' (04 00 00 00 6C 6F 6F 74)
                             )
                         varnames:
000008BF                     TUPLE: (
000008C4                         STR: 'rule' (04 00 00 00 72 75 6C 65),
000008CD                         STR: 'table' (05 00 00 00 74 61 62 6C 65),
000008D7                         STR: 'dict' (04 00 00 00 64 69 63 74),
000008E0                         STR: 'args' (04 00 00 00 61 72 67 73),
000008E9                         STR: 'fgo' (03 00 00 00 66 67 6F),
000008F1                         STR: 'loot' (04 00 00 00 6C 6F 6F 74)
                             )
                         freevars:
000008FA                     TUPLE: ()
                         cellvars:
000008FF                     TUPLE: ()
                         filename:
00000904                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\trgs.py' (3C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 74 72 67 73 2E 70 79)
                         name:
00000945                     STR: 'MakeAndEncodeReward' (13 00 00 00 4D 61 6B 65 41 6E 64 45 6E 63 6F 64 65 52 65 77 61 72 64)
                         firslineno:
0000095D                     LONG: 69L (45 00 00 00)
                         lnotab:
00000961                     STR: '\x00\x01\x0c\x01\x18\x01' (06 00 00 00 00 01 0C 01 18 01),
0000096C             CODE:
                         argcount:
0000096D                     LONG: 4L (04 00 00 00)
                         nlocals:
00000971                     LONG: 6L (06 00 00 00)
                         stacksize:
00000975                     LONG: 5L (05 00 00 00)
                         flags:
00000979                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000097D                     STR: 't\x00\x00|\x02\x00\x83\x01\x00}\x04\x00t\x03\x00i\x04\x00|\x00\x00|\x01\x00|\x03\x00|\x04\x00\x83\x04\x00}\x05\x00|\x05\x00Sd\x00\x00S' (2C 00 00 00 74 00 00 7C 02 00 83 01 00 7D 04 00 74 03 00 69 04 00 7C 00 00 7C 01 00 7C 03 00 7C 04 00 83 04 00 7D 05 00 7C 05 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'FakeGameObject'
                             00000003     7C - LOAD_FAST           'dict'
                             00000006     83 - CALL_FUNCTION       r0001
                             00000009     7D - STORE_FAST          'fgo'
                             0000000C     74 - LOAD_GLOBAL         'rewardselection'
                             0000000F     69 - LOAD_ATTR           'DetermineReward'
                             00000012     7C - LOAD_FAST           'rule'
                             00000015     7C - LOAD_FAST           'table'
                             00000018     7C - LOAD_FAST           'args'
                             0000001B     7C - LOAD_FAST           'fgo'
                             0000001E     83 - CALL_FUNCTION       r0004
                             00000021     7D - STORE_FAST          'loot'
                             00000024     7C - LOAD_FAST           'loot'
                             00000027     53 - RETURN_VALUE        
                             00000028     64 - LOAD_CONST          None
                             0000002B     53 - RETURN_VALUE        
                         consts:
000009AE                     TUPLE: (
000009B3                         None (4E)
                             )
                         names:
000009B4                     TUPLE: (
000009B9                         STR: 'FakeGameObject' (0E 00 00 00 46 61 6B 65 47 61 6D 65 4F 62 6A 65 63 74),
000009CC                         STR: 'dict' (04 00 00 00 64 69 63 74),
000009D5                         STR: 'fgo' (03 00 00 00 66 67 6F),
000009DD                         STR: 'rewardselection' (0F 00 00 00 72 65 77 61 72 64 73 65 6C 65 63 74 69 6F 6E),
000009F1                         STR: 'DetermineReward' (0F 00 00 00 44 65 74 65 72 6D 69 6E 65 52 65 77 61 72 64),
00000A05                         STR: 'rule' (04 00 00 00 72 75 6C 65),
00000A0E                         STR: 'table' (05 00 00 00 74 61 62 6C 65),
00000A18                         STR: 'args' (04 00 00 00 61 72 67 73),
00000A21                         STR: 'loot' (04 00 00 00 6C 6F 6F 74)
                             )
                         varnames:
00000A2A                     TUPLE: (
00000A2F                         STR: 'rule' (04 00 00 00 72 75 6C 65),
00000A38                         STR: 'table' (05 00 00 00 74 61 62 6C 65),
00000A42                         STR: 'dict' (04 00 00 00 64 69 63 74),
00000A4B                         STR: 'args' (04 00 00 00 61 72 67 73),
00000A54                         STR: 'fgo' (03 00 00 00 66 67 6F),
00000A5C                         STR: 'loot' (04 00 00 00 6C 6F 6F 74)
                             )
                         freevars:
00000A65                     TUPLE: ()
                         cellvars:
00000A6A                     TUPLE: ()
                         filename:
00000A6F                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\trgs.py' (3C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 74 72 67 73 2E 70 79)
                         name:
00000AB0                     STR: 'MakeRewardRoll' (0E 00 00 00 4D 61 6B 65 52 65 77 61 72 64 52 6F 6C 6C)
                         firslineno:
00000AC3                     LONG: 74L (4A 00 00 00)
                         lnotab:
00000AC7                     STR: '\x00\x01\x0c\x01\x18\x01' (06 00 00 00 00 01 0C 01 18 01),
00000AD2             CODE:
                         argcount:
00000AD3                     LONG: 1L (01 00 00 00)
                         nlocals:
00000AD7                     LONG: 3L (03 00 00 00)
                         stacksize:
00000ADB                     LONG: 4L (04 00 00 00)
                         flags:
00000ADF                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000AE3                     STR: 'd\x01\x00}\x01\x00y,\x00t\x01\x00i\x02\x00|\x00\x00\x83\x01\x00}\x02\x00t\x05\x00t\x01\x00i\x06\x00|\x02\x00d\x01\x00\x19\x83\x01\x00\x83\x01\x00}\x01\x00Wn\x07\x00\x01\x01\x01n\x01\x00X|\x01\x00Sd\x00\x00S' (44 00 00 00 64 01 00 7D 01 00 79 2C 00 74 01 00 69 02 00 7C 00 00 83 01 00 7D 02 00 74 05 00 74 01 00 69 06 00 7C 02 00 64 01 00 19 83 01 00 83 01 00 7D 01 00 57 6E 07 00 01 01 01 6E 01 00 58 7C 01 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          0
                             00000003     7D - STORE_FAST          'itemID'
                             00000006     79 - SETUP_EXCEPT        -> 00000035
                             00000009     74 - LOAD_GLOBAL         'rewardselection'
                             0000000C     69 - LOAD_ATTR           'Decode_Reward'
                             0000000F     7C - LOAD_FAST           'reward'
                             00000012     83 - CALL_FUNCTION       r0001
                             00000015     7D - STORE_FAST          'item'
                             00000018     74 - LOAD_GLOBAL         'int'
                             0000001B     74 - LOAD_GLOBAL         'rewardselection'
                             0000001E     69 - LOAD_ATTR           'Get_Item'
                             00000021     7C - LOAD_FAST           'item'
                             00000024     64 - LOAD_CONST          0
                             00000027     19 - BINARY_SUBSCR       
                             00000028     83 - CALL_FUNCTION       r0001
                             0000002B     83 - CALL_FUNCTION       r0001
                             0000002E     7D - STORE_FAST          'itemID'
                             00000031     57 - POP_BLOCK           
                             00000032     6E - JUMP_FORWARD        -> 0000003C
                             00000035     01 - POP_TOP             
                             00000036     01 - POP_TOP             
                             00000037     01 - POP_TOP             
                             00000038     6E - JUMP_FORWARD        -> 0000003C
                             0000003B     58 - END_FINALLY         
                             0000003C     7C - LOAD_FAST           'itemID'
                             0000003F     53 - RETURN_VALUE        
                             00000040     64 - LOAD_CONST          None
                             00000043     53 - RETURN_VALUE        
                         consts:
00000B2C                     TUPLE: (
00000B31                         None (4E),
00000B32                         INT: 0 (00 00 00 00)
                             )
                         names:
00000B37                     TUPLE: (
00000B3C                         STR: 'itemID' (06 00 00 00 69 74 65 6D 49 44),
00000B47                         STR: 'rewardselection' (0F 00 00 00 72 65 77 61 72 64 73 65 6C 65 63 74 69 6F 6E),
00000B5B                         STR: 'Decode_Reward' (0D 00 00 00 44 65 63 6F 64 65 5F 52 65 77 61 72 64),
00000B6D                         STR: 'reward' (06 00 00 00 72 65 77 61 72 64),
00000B78                         STR: 'item' (04 00 00 00 69 74 65 6D),
00000B81                         STR: 'int' (03 00 00 00 69 6E 74),
00000B89                         STR: 'Get_Item' (08 00 00 00 47 65 74 5F 49 74 65 6D)
                             )
                         varnames:
00000B96                     TUPLE: (
00000B9B                         STR: 'reward' (06 00 00 00 72 65 77 61 72 64),
00000BA6                         STR: 'itemID' (06 00 00 00 69 74 65 6D 49 44),
00000BB1                         STR: 'item' (04 00 00 00 69 74 65 6D)
                             )
                         freevars:
00000BBA                     TUPLE: ()
                         cellvars:
00000BBF                     TUPLE: ()
                         filename:
00000BC4                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\trgs.py' (3C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 74 72 67 73 2E 70 79)
                         name:
00000C05                     STR: 'GetRewardItemID' (0F 00 00 00 47 65 74 52 65 77 61 72 64 49 74 65 6D 49 44)
                         firslineno:
00000C19                     LONG: 79L (4F 00 00 00)
                         lnotab:
00000C1D                     STR: '\x00\x01\x06\x01\x03\x01\x0f\x01\x1d\x01\x03\x01\x04\x01' (0E 00 00 00 00 01 06 01 03 01 0F 01 1D 01 03 01 04 01),
00000C30             CODE:
                         argcount:
00000C31                     LONG: 0L (00 00 00 00)
                         nlocals:
00000C35                     LONG: 0L (00 00 00 00)
                         stacksize:
00000C39                     LONG: 1L (01 00 00 00)
                         flags:
00000C3D                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000C41                     STR: 't\x00\x00i\x01\x00\x83\x00\x00\x01d\x00\x00S' (0E 00 00 00 74 00 00 69 01 00 83 00 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'rewardselection'
                             00000003     69 - LOAD_ATTR           'ReloadRewardSelection'
                             00000006     83 - CALL_FUNCTION       r0000
                             00000009     01 - POP_TOP             
                             0000000A     64 - LOAD_CONST          None
                             0000000D     53 - RETURN_VALUE        
                         consts:
00000C54                     TUPLE: (
00000C59                         None (4E)
                             )
                         names:
00000C5A                     TUPLE: (
00000C5F                         STR: 'rewardselection' (0F 00 00 00 72 65 77 61 72 64 73 65 6C 65 63 74 69 6F 6E),
00000C73                         STR: 'ReloadRewardSelection' (15 00 00 00 52 65 6C 6F 61 64 52 65 77 61 72 64 53 65 6C 65 63 74 69 6F 6E)
                             )
                         varnames:
00000C8D                     TUPLE: ()
                         freevars:
00000C92                     TUPLE: ()
                         cellvars:
00000C97                     TUPLE: ()
                         filename:
00000C9C                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\trgs.py' (3C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 74 72 67 73 2E 70 79)
                         name:
00000CDD                     STR: 'ReloadRewardSelection' (15 00 00 00 52 65 6C 6F 61 64 52 65 77 61 72 64 53 65 6C 65 63 74 69 6F 6E)
                         firslineno:
00000CF7                     LONG: 88L (58 00 00 00)
                         lnotab:
00000CFB                     STR: '\x00\x01' (02 00 00 00 00 01),
00000D02             CODE:
                         argcount:
00000D03                     LONG: 1L (01 00 00 00)
                         nlocals:
00000D07                     LONG: 5L (05 00 00 00)
                         stacksize:
00000D0B                     LONG: 3L (03 00 00 00)
                         flags:
00000D0F                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000D13                     STR: 'd\x01\x00t\x00\x00|\x00\x00\x83\x01\x00\x17}\x04\x00t\x03\x00i\x04\x00|\x04\x00\x83\x01\x00\x0coT\x00\x01y<\x00t\x05\x00d\x02\x00|\x04\x00\x17\x83\x01\x00}\x01\x00t\x07\x00|\x01\x00|\x04\x00\x83\x02\x00}\x03\x00t\x07\x00|\x03\x00|\x04\x00\x83\x02\x00}\x02\x00|\x02\x00t\x03\x00|\x04\x00<Wqu\x00\x01\x01\x01t\n\x00t\x03\x00|\x04\x00<qu\x00Xn\x01\x00\x01t\x03\x00|\x04\x00\x19t\n\x00j\x08\x00o\x08\x00\x01t\n\x00Sn\x0c\x00\x01t\x03\x00|\x04\x00\x19\x83\x00\x00Sd\x00\x00S' (9D 00 00 00 64 01 00 74 00 00 7C 00 00 83 01 00 17 7D 04 00 74 03 00 69 04 00 7C 04 00 83 01 00 0C 6F 54 00 01 79 3C 00 74 05 00 64 02 00 7C 04 00 17 83 01 00 7D 01 00 74 07 00 7C 01 00 7C 04 00 83 02 00 7D 03 00 74 07 00 7C 03 00 7C 04 00 83 02 00 7D 02 00 7C 02 00 74 03 00 7C 04 00 3C 57 71 75 00 01 01 01 74 0A 00 74 03 00 7C 04 00 3C 71 75 00 58 6E 01 00 01 74 03 00 7C 04 00 19 74 0A 00 6A 08 00 6F 08 00 01 74 0A 00 53 6E 0C 00 01 74 03 00 7C 04 00 19 83 00 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          'Mission'
                             00000003     74 - LOAD_GLOBAL         'str'
                             00000006     7C - LOAD_FAST           'missionid'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     17 - BINARY_ADD          
                             0000000D     7D - STORE_FAST          'classname'
                             00000010     74 - LOAD_GLOBAL         'Missions'
                             00000013     69 - LOAD_ATTR           'has_key'
                             00000016     7C - LOAD_FAST           'classname'
                             00000019     83 - CALL_FUNCTION       r0001
                             0000001C     0C - UNARY_NOT           
                             0000001D     6F - JUMP_IF_FALSE       -> 00000074
                             00000020     01 - POP_TOP             
                             00000021     79 - SETUP_EXCEPT        -> 00000060
                             00000024     74 - LOAD_GLOBAL         '__import__'
                             00000027     64 - LOAD_CONST          'Missions.'
                             0000002A     7C - LOAD_FAST           'classname'
                             0000002D     17 - BINARY_ADD          
                             0000002E     83 - CALL_FUNCTION       r0001
                             00000031     7D - STORE_FAST          'package'
                             00000034     74 - LOAD_GLOBAL         'getattr'
                             00000037     7C - LOAD_FAST           'package'
                             0000003A     7C - LOAD_FAST           'classname'
                             0000003D     83 - CALL_FUNCTION       r0002
                             00000040     7D - STORE_FAST          'module'
                             00000043     74 - LOAD_GLOBAL         'getattr'
                             00000046     7C - LOAD_FAST           'module'
                             00000049     7C - LOAD_FAST           'classname'
                             0000004C     83 - CALL_FUNCTION       r0002
                             0000004F     7D - STORE_FAST          'classobj'
                             00000052     7C - LOAD_FAST           'classobj'
                             00000055     74 - LOAD_GLOBAL         'Missions'
                             00000058     7C - LOAD_FAST           'classname'
                             0000005B     3C - STORE_SUBSCR        
                             0000005C     57 - POP_BLOCK           
                             0000005D     71 - JUMP_ABSOLUTE       -> 00000075
                             00000060     01 - POP_TOP             
                             00000061     01 - POP_TOP             
                             00000062     01 - POP_TOP             
                             00000063     74 - LOAD_GLOBAL         'None'
                             00000066     74 - LOAD_GLOBAL         'Missions'
                             00000069     7C - LOAD_FAST           'classname'
                             0000006C     3C - STORE_SUBSCR        
                             0000006D     71 - JUMP_ABSOLUTE       -> 00000075
                             00000070     58 - END_FINALLY         
                             00000071     6E - JUMP_FORWARD        -> 00000075
                             00000074     01 - POP_TOP             
                             00000075     74 - LOAD_GLOBAL         'Missions'
                             00000078     7C - LOAD_FAST           'classname'
                             0000007B     19 - BINARY_SUBSCR       
                             0000007C     74 - LOAD_GLOBAL         'None'
                             0000007F     6A - COMPARE_OP          "is"
                             00000082     6F - JUMP_IF_FALSE       -> 0000008D
                             00000085     01 - POP_TOP             
                             00000086     74 - LOAD_GLOBAL         'None'
                             00000089     53 - RETURN_VALUE        
                             0000008A     6E - JUMP_FORWARD        -> 00000099
                             0000008D     01 - POP_TOP             
                             0000008E     74 - LOAD_GLOBAL         'Missions'
                             00000091     7C - LOAD_FAST           'classname'
                             00000094     19 - BINARY_SUBSCR       
                             00000095     83 - CALL_FUNCTION       r0000
                             00000098     53 - RETURN_VALUE        
                             00000099     64 - LOAD_CONST          None
                             0000009C     53 - RETURN_VALUE        
                         consts:
00000DB5                     TUPLE: (
00000DBA                         None (4E),
00000DBB                         STR: 'Mission' (07 00 00 00 4D 69 73 73 69 6F 6E),
00000DC7                         STR: 'Missions.' (09 00 00 00 4D 69 73 73 69 6F 6E 73 2E)
                             )
                         names:
00000DD5                     TUPLE: (
00000DDA                         STR: 'str' (03 00 00 00 73 74 72),
00000DE2                         STR: 'missionid' (09 00 00 00 6D 69 73 73 69 6F 6E 69 64),
00000DF0                         STR: 'classname' (09 00 00 00 63 6C 61 73 73 6E 61 6D 65),
00000DFE                         STR: 'Missions' (08 00 00 00 4D 69 73 73 69 6F 6E 73),
00000E0B                         STR: 'has_key' (07 00 00 00 68 61 73 5F 6B 65 79),
00000E17                         STR: '__import__' (0A 00 00 00 5F 5F 69 6D 70 6F 72 74 5F 5F),
00000E26                         STR: 'package' (07 00 00 00 70 61 63 6B 61 67 65),
00000E32                         STR: 'getattr' (07 00 00 00 67 65 74 61 74 74 72),
00000E3E                         STR: 'module' (06 00 00 00 6D 6F 64 75 6C 65),
00000E49                         STR: 'classobj' (08 00 00 00 63 6C 61 73 73 6F 62 6A),
00000E56                         STR: 'None' (04 00 00 00 4E 6F 6E 65)
                             )
                         varnames:
00000E5F                     TUPLE: (
00000E64                         STR: 'missionid' (09 00 00 00 6D 69 73 73 69 6F 6E 69 64),
00000E72                         STR: 'package' (07 00 00 00 70 61 63 6B 61 67 65),
00000E7E                         STR: 'classobj' (08 00 00 00 63 6C 61 73 73 6F 62 6A),
00000E8B                         STR: 'module' (06 00 00 00 6D 6F 64 75 6C 65),
00000E96                         STR: 'classname' (09 00 00 00 63 6C 61 73 73 6E 61 6D 65)
                             )
                         freevars:
00000EA4                     TUPLE: ()
                         cellvars:
00000EA9                     TUPLE: ()
                         filename:
00000EAE                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\trgs.py' (3C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 74 72 67 73 2E 70 79)
                         name:
00000EEF                     STR: 'FindMissionModule' (11 00 00 00 46 69 6E 64 4D 69 73 73 69 6F 6E 4D 6F 64 75 6C 65)
                         firslineno:
00000F05                     LONG: 94L (5E 00 00 00)
                         lnotab:
00000F09                     STR: '\x00\x01\x10\x02\x11\x01\x03\x01\x10\x01\x0f\x01\x0f\x01\x0e\x01\x03\x01\x12\x02\x11\x01\x08\x02' (18 00 00 00 00 01 10 02 11 01 03 01 10 01 0F 01 0F 01 0E 01 03 01 12 02 11 01 08 02),
00000F26             CODE:
                         argcount:
00000F27                     LONG: 1L (01 00 00 00)
                         nlocals:
00000F2B                     LONG: 13L (0D 00 00 00)
                         stacksize:
00000F2F                     LONG: 6L (06 00 00 00)
                         flags:
00000F33                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000F37                     STR: 'y\xaa\x01d\x01\x00}\x08\x00d\x02\x00}\x07\x00g\x00\x00}\x03\x00g\x00\x00}\x0c\x00g\x00\x00}\x04\x00|\x00\x00i\x06\x00\x83\x00\x00}\x00\x00t\x07\x00i\x07\x00|\x00\x00d\x03\x00\x83\x02\x00\\\x02\x00}\x06\x00}\x02\x00x-\x01|\x06\x00D]%\x01\\\x02\x00}\x01\x00}\t\x00|\x01\x00d\x04\x00j\x02\x00o\n\x00\x01d\x05\x00}\x08\x00qL\x00\x01|\x01\x00d\x06\x00j\x02\x00o\x10\x00\x01t\x0c\x00|\t\x00\x83\x01\x00}\x07\x00qL\x00\x01|\x01\x00d\x07\x00j\x02\x00o\xd8\x00\x01|\t\x00i\x06\x00d\x08\x00\x83\x01\x00}\x05\x00x\xc6\x00|\x05\x00D]\xba\x00}\n\x00|\n\x00i\x06\x00d\t\x00\x83\x01\x00}\x0b\x00t\x10\x00|\x0b\x00\x83\x01\x00d\n\x00j\x02\x00o2\x00\x01|\x03\x00i\x11\x00t\x0c\x00|\x0b\x00d\x01\x00\x19\x83\x01\x00\x83\x01\x00\x01|\x0c\x00i\x11\x00t\x0c\x00|\x0b\x00d\x05\x00\x19\x83\x01\x00\x83\x01\x00\x01q\xaf\x00\x01t\x10\x00|\x0b\x00\x83\x01\x00d\x0b\x00j\x02\x00oI\x00\x01|\x03\x00i\x11\x00t\x0c\x00|\x0b\x00d\x01\x00\x19\x83\x01\x00\x83\x01\x00\x01|\x0c\x00i\x11\x00t\x0c\x00|\x0b\x00d\x05\x00\x19\x83\x01\x00\x83\x01\x00\x01|\x04\x00i\x11\x00t\x0c\x00|\x0b\x00d\n\x00\x19\x83\x01\x00\x83\x01\x00\x01q\xaf\x00\x01t\x12\x00Sq\xaf\x00WqL\x00\x01qL\x00Wt\x10\x00|\x03\x00\x83\x01\x00t\x10\x00|\x0c\x00\x83\x01\x00j\x03\x00o\x08\x00\x01t\x12\x00Sn\x01\x00\x01|\x08\x00|\x07\x00|\x03\x00|\x0c\x00|\x04\x00f\x05\x00SWn\x0b\x00\x01\x01\x01t\x12\x00Sn\x01\x00Xd\x00\x00S' (BC 01 00 00 79 AA 01 64 01 00 7D 08 00 64 02 00 7D 07 00 67 00 00 7D 03 00 67 00 00 7D 0C 00 67 00 00 7D 04 00 7C 00 00 69 06 00 83 00 00 7D 00 00 74 07 00 69 07 00 7C 00 00 64 03 00 83 02 00 5C 02 00 7D 06 00 7D 02 00 78 2D 01 7C 06 00 44 5D 25 01 5C 02 00 7D 01 00 7D 09 00 7C 01 00 64 04 00 6A 02 00 6F 0A 00 01 64 05 00 7D 08 00 71 4C 00 01 7C 01 00 64 06 00 6A 02 00 6F 10 00 01 74 0C 00 7C 09 00 83 01 00 7D 07 00 71 4C 00 01 7C 01 00 64 07 00 6A 02 00 6F D8 00 01 7C 09 00 69 06 00 64 08 00 83 01 00 7D 05 00 78 C6 00 7C 05 00 44 5D BA 00 7D 0A 00 7C 0A 00 69 06 00 64 09 00 83 01 00 7D 0B 00 74 10 00 7C 0B 00 83 01 00 64 0A 00 6A 02 00 6F 32 00 01 7C 03 00 69 11 00 74 0C 00 7C 0B 00 64 01 00 19 83 01 00 83 01 00 01 7C 0C 00 69 11 00 74 0C 00 7C 0B 00 64 05 00 19 83 01 00 83 01 00 01 71 AF 00 01 74 10 00 7C 0B 00 83 01 00 64 0B 00 6A 02 00 6F 49 00 01 7C 03 00 69 11 00 74 0C 00 7C 0B 00 64 01 00 19 83 01 00 83 01 00 01 7C 0C 00 69 11 00 74 0C 00 7C 0B 00 64 05 00 19 83 01 00 83 01 00 01 7C 04 00 69 11 00 74 0C 00 7C 0B 00 64 0A 00 19 83 01 00 83 01 00 01 71 AF 00 01 74 12 00 53 71 AF 00 57 71 4C 00 01 71 4C 00 57 74 10 00 7C 03 00 83 01 00 74 10 00 7C 0C 00 83 01 00 6A 03 00 6F 08 00 01 74 12 00 53 6E 01 00 01 7C 08 00 7C 07 00 7C 03 00 7C 0C 00 7C 04 00 66 05 00 53 57 6E 0B 00 01 01 01 74 12 00 53 6E 01 00 58 64 00 00 53)
                             00000000     79 - SETUP_EXCEPT        -> 000001AD
                             00000003     64 - LOAD_CONST          0
                             00000006     7D - STORE_FAST          'autostart'
                             00000009     64 - LOAD_CONST          -1
                             0000000C     7D - STORE_FAST          'difficulty'
                             0000000F     67 - BUILD_LIST          r0000
                             00000012     7D - STORE_FAST          'sectors'
                             00000015     67 - BUILD_LIST          r0000
                             00000018     7D - STORE_FAST          'areas'
                             0000001B     67 - BUILD_LIST          r0000
                             0000001E     7D - STORE_FAST          'permutations'
                             00000021     7C - LOAD_FAST           'missionargs'
                             00000024     69 - LOAD_ATTR           'split'
                             00000027     83 - CALL_FUNCTION       r0000
                             0000002A     7D - STORE_FAST          'missionargs'
                             0000002D     74 - LOAD_GLOBAL         'getopt'
                             00000030     69 - LOAD_ATTR           'getopt'
                             00000033     7C - LOAD_FAST           'missionargs'
                             00000036     64 - LOAD_CONST          'ad:m:'
                             00000039     83 - CALL_FUNCTION       r0002
                             0000003C     5C - UNPACK_SEQUENCE     r0002
                             0000003F     7D - STORE_FAST          'optlist'
                             00000042     7D - STORE_FAST          'args'
                             00000045     78 - SETUP_LOOP          -> 00000175
                             00000048     7C - LOAD_FAST           'optlist'
                             0000004B     44 - GET_ITER            
                             0000004C     5D - FOR_ITER            -> 00000174
                             0000004F     5C - UNPACK_SEQUENCE     r0002
                             00000052     7D - STORE_FAST          'opt'
                             00000055     7D - STORE_FAST          'arg'
                             00000058     7C - LOAD_FAST           'opt'
                             0000005B     64 - LOAD_CONST          '-a'
                             0000005E     6A - COMPARE_OP          "=="
                             00000061     6F - JUMP_IF_FALSE       -> 0000006E
                             00000064     01 - POP_TOP             
                             00000065     64 - LOAD_CONST          1
                             00000068     7D - STORE_FAST          'autostart'
                             0000006B     71 - JUMP_ABSOLUTE       -> 0000004C
                             0000006E     01 - POP_TOP             
                             0000006F     7C - LOAD_FAST           'opt'
                             00000072     64 - LOAD_CONST          '-d'
                             00000075     6A - COMPARE_OP          "=="
                             00000078     6F - JUMP_IF_FALSE       -> 0000008B
                             0000007B     01 - POP_TOP             
                             0000007C     74 - LOAD_GLOBAL         'int'
                             0000007F     7C - LOAD_FAST           'arg'
                             00000082     83 - CALL_FUNCTION       r0001
                             00000085     7D - STORE_FAST          'difficulty'
                             00000088     71 - JUMP_ABSOLUTE       -> 0000004C
                             0000008B     01 - POP_TOP             
                             0000008C     7C - LOAD_FAST           'opt'
                             0000008F     64 - LOAD_CONST          '-m'
                             00000092     6A - COMPARE_OP          "=="
                             00000095     6F - JUMP_IF_FALSE       -> 00000170
                             00000098     01 - POP_TOP             
                             00000099     7C - LOAD_FAST           'arg'
                             0000009C     69 - LOAD_ATTR           'split'
                             0000009F     64 - LOAD_CONST          ':'
                             000000A2     83 - CALL_FUNCTION       r0001
                             000000A5     7D - STORE_FAST          'phaselist'
                             000000A8     78 - SETUP_LOOP          -> 00000171
                             000000AB     7C - LOAD_FAST           'phaselist'
                             000000AE     44 - GET_ITER            
                             000000AF     5D - FOR_ITER            -> 0000016C
                             000000B2     7D - STORE_FAST          'phase'
                             000000B5     7C - LOAD_FAST           'phase'
                             000000B8     69 - LOAD_ATTR           'split'
                             000000BB     64 - LOAD_CONST          '.'
                             000000BE     83 - CALL_FUNCTION       r0001
                             000000C1     7D - STORE_FAST          'parsed'
                             000000C4     74 - LOAD_GLOBAL         'len'
                             000000C7     7C - LOAD_FAST           'parsed'
                             000000CA     83 - CALL_FUNCTION       r0001
                             000000CD     64 - LOAD_CONST          2
                             000000D0     6A - COMPARE_OP          "=="
                             000000D3     6F - JUMP_IF_FALSE       -> 00000108
                             000000D6     01 - POP_TOP             
                             000000D7     7C - LOAD_FAST           'sectors'
                             000000DA     69 - LOAD_ATTR           'append'
                             000000DD     74 - LOAD_GLOBAL         'int'
                             000000E0     7C - LOAD_FAST           'parsed'
                             000000E3     64 - LOAD_CONST          0
                             000000E6     19 - BINARY_SUBSCR       
                             000000E7     83 - CALL_FUNCTION       r0001
                             000000EA     83 - CALL_FUNCTION       r0001
                             000000ED     01 - POP_TOP             
                             000000EE     7C - LOAD_FAST           'areas'
                             000000F1     69 - LOAD_ATTR           'append'
                             000000F4     74 - LOAD_GLOBAL         'int'
                             000000F7     7C - LOAD_FAST           'parsed'
                             000000FA     64 - LOAD_CONST          1
                             000000FD     19 - BINARY_SUBSCR       
                             000000FE     83 - CALL_FUNCTION       r0001
                             00000101     83 - CALL_FUNCTION       r0001
                             00000104     01 - POP_TOP             
                             00000105     71 - JUMP_ABSOLUTE       -> 000000AF
                             00000108     01 - POP_TOP             
                             00000109     74 - LOAD_GLOBAL         'len'
                             0000010C     7C - LOAD_FAST           'parsed'
                             0000010F     83 - CALL_FUNCTION       r0001
                             00000112     64 - LOAD_CONST          3
                             00000115     6A - COMPARE_OP          "=="
                             00000118     6F - JUMP_IF_FALSE       -> 00000164
                             0000011B     01 - POP_TOP             
                             0000011C     7C - LOAD_FAST           'sectors'
                             0000011F     69 - LOAD_ATTR           'append'
                             00000122     74 - LOAD_GLOBAL         'int'
                             00000125     7C - LOAD_FAST           'parsed'
                             00000128     64 - LOAD_CONST          0
                             0000012B     19 - BINARY_SUBSCR       
                             0000012C     83 - CALL_FUNCTION       r0001
                             0000012F     83 - CALL_FUNCTION       r0001
                             00000132     01 - POP_TOP             
                             00000133     7C - LOAD_FAST           'areas'
                             00000136     69 - LOAD_ATTR           'append'
                             00000139     74 - LOAD_GLOBAL         'int'
                             0000013C     7C - LOAD_FAST           'parsed'
                             0000013F     64 - LOAD_CONST          1
                             00000142     19 - BINARY_SUBSCR       
                             00000143     83 - CALL_FUNCTION       r0001
                             00000146     83 - CALL_FUNCTION       r0001
                             00000149     01 - POP_TOP             
                             0000014A     7C - LOAD_FAST           'permutations'
                             0000014D     69 - LOAD_ATTR           'append'
                             00000150     74 - LOAD_GLOBAL         'int'
                             00000153     7C - LOAD_FAST           'parsed'
                             00000156     64 - LOAD_CONST          2
                             00000159     19 - BINARY_SUBSCR       
                             0000015A     83 - CALL_FUNCTION       r0001
                             0000015D     83 - CALL_FUNCTION       r0001
                             00000160     01 - POP_TOP             
                             00000161     71 - JUMP_ABSOLUTE       -> 000000AF
                             00000164     01 - POP_TOP             
                             00000165     74 - LOAD_GLOBAL         'None'
                             00000168     53 - RETURN_VALUE        
                             00000169     71 - JUMP_ABSOLUTE       -> 000000AF
                             0000016C     57 - POP_BLOCK           
                             0000016D     71 - JUMP_ABSOLUTE       -> 0000004C
                             00000170     01 - POP_TOP             
                             00000171     71 - JUMP_ABSOLUTE       -> 0000004C
                             00000174     57 - POP_BLOCK           
                             00000175     74 - LOAD_GLOBAL         'len'
                             00000178     7C - LOAD_FAST           'sectors'
                             0000017B     83 - CALL_FUNCTION       r0001
                             0000017E     74 - LOAD_GLOBAL         'len'
                             00000181     7C - LOAD_FAST           'areas'
                             00000184     83 - CALL_FUNCTION       r0001
                             00000187     6A - COMPARE_OP          "!="
                             0000018A     6F - JUMP_IF_FALSE       -> 00000195
                             0000018D     01 - POP_TOP             
                             0000018E     74 - LOAD_GLOBAL         'None'
                             00000191     53 - RETURN_VALUE        
                             00000192     6E - JUMP_FORWARD        -> 00000196
                             00000195     01 - POP_TOP             
                             00000196     7C - LOAD_FAST           'autostart'
                             00000199     7C - LOAD_FAST           'difficulty'
                             0000019C     7C - LOAD_FAST           'sectors'
                             0000019F     7C - LOAD_FAST           'areas'
                             000001A2     7C - LOAD_FAST           'permutations'
                             000001A5     66 - BUILD_TUPLE         r0005
                             000001A8     53 - RETURN_VALUE        
                             000001A9     57 - POP_BLOCK           
                             000001AA     6E - JUMP_FORWARD        -> 000001B8
                             000001AD     01 - POP_TOP             
                             000001AE     01 - POP_TOP             
                             000001AF     01 - POP_TOP             
                             000001B0     74 - LOAD_GLOBAL         'None'
                             000001B3     53 - RETURN_VALUE        
                             000001B4     6E - JUMP_FORWARD        -> 000001B8
                             000001B7     58 - END_FINALLY         
                             000001B8     64 - LOAD_CONST          None
                             000001BB     53 - RETURN_VALUE        
                         consts:
000010F8                     TUPLE: (
000010FD                         None (4E),
000010FE                         INT: 0 (00 00 00 00),
00001103                         INT: -1 (FF FF FF FF),
00001108                         STR: 'ad:m:' (05 00 00 00 61 64 3A 6D 3A),
00001112                         STR: '-a' (02 00 00 00 2D 61),
00001119                         INT: 1 (01 00 00 00),
0000111E                         STR: '-d' (02 00 00 00 2D 64),
00001125                         STR: '-m' (02 00 00 00 2D 6D),
0000112C                         STR: ':' (01 00 00 00 3A),
00001132                         STR: '.' (01 00 00 00 2E),
00001138                         INT: 2 (02 00 00 00),
0000113D                         INT: 3 (03 00 00 00)
                             )
                         names:
00001142                     TUPLE: (
00001147                         STR: 'autostart' (09 00 00 00 61 75 74 6F 73 74 61 72 74),
00001155                         STR: 'difficulty' (0A 00 00 00 64 69 66 66 69 63 75 6C 74 79),
00001164                         STR: 'sectors' (07 00 00 00 73 65 63 74 6F 72 73),
00001170                         STR: 'areas' (05 00 00 00 61 72 65 61 73),
0000117A                         STR: 'permutations' (0C 00 00 00 70 65 72 6D 75 74 61 74 69 6F 6E 73),
0000118B                         STR: 'missionargs' (0B 00 00 00 6D 69 73 73 69 6F 6E 61 72 67 73),
0000119B                         STR: 'split' (05 00 00 00 73 70 6C 69 74),
000011A5                         STR: 'getopt' (06 00 00 00 67 65 74 6F 70 74),
000011B0                         STR: 'optlist' (07 00 00 00 6F 70 74 6C 69 73 74),
000011BC                         STR: 'args' (04 00 00 00 61 72 67 73),
000011C5                         STR: 'opt' (03 00 00 00 6F 70 74),
000011CD                         STR: 'arg' (03 00 00 00 61 72 67),
000011D5                         STR: 'int' (03 00 00 00 69 6E 74),
000011DD                         STR: 'phaselist' (09 00 00 00 70 68 61 73 65 6C 69 73 74),
000011EB                         STR: 'phase' (05 00 00 00 70 68 61 73 65),
000011F5                         STR: 'parsed' (06 00 00 00 70 61 72 73 65 64),
00001200                         STR: 'len' (03 00 00 00 6C 65 6E),
00001208                         STR: 'append' (06 00 00 00 61 70 70 65 6E 64),
00001213                         STR: 'None' (04 00 00 00 4E 6F 6E 65)
                             )
                         varnames:
0000121C                     TUPLE: (
00001221                         STR: 'missionargs' (0B 00 00 00 6D 69 73 73 69 6F 6E 61 72 67 73),
00001231                         STR: 'opt' (03 00 00 00 6F 70 74),
00001239                         STR: 'args' (04 00 00 00 61 72 67 73),
00001242                         STR: 'sectors' (07 00 00 00 73 65 63 74 6F 72 73),
0000124E                         STR: 'permutations' (0C 00 00 00 70 65 72 6D 75 74 61 74 69 6F 6E 73),
0000125F                         STR: 'phaselist' (09 00 00 00 70 68 61 73 65 6C 69 73 74),
0000126D                         STR: 'optlist' (07 00 00 00 6F 70 74 6C 69 73 74),
00001279                         STR: 'difficulty' (0A 00 00 00 64 69 66 66 69 63 75 6C 74 79),
00001288                         STR: 'autostart' (09 00 00 00 61 75 74 6F 73 74 61 72 74),
00001296                         STR: 'arg' (03 00 00 00 61 72 67),
0000129E                         STR: 'phase' (05 00 00 00 70 68 61 73 65),
000012A8                         STR: 'parsed' (06 00 00 00 70 61 72 73 65 64),
000012B3                         STR: 'areas' (05 00 00 00 61 72 65 61 73)
                             )
                         freevars:
000012BD                     TUPLE: ()
                         cellvars:
000012C2                     TUPLE: ()
                         filename:
000012C7                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\trgs.py' (3C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 74 72 67 73 2E 70 79)
                         name:
00001308                     STR: 'ParseMissionArgs' (10 00 00 00 50 61 72 73 65 4D 69 73 73 69 6F 6E 41 72 67 73)
                         firslineno:
0000131D                     LONG: 114L (72 00 00 00)
                         lnotab:
00001321                     STR: '\x00\x02\x03\x01\x06\x01\x06\x02\x06\x01\x06\x01\x06\x02\x0c\x02\x18\x02\x07\x00\x0c\x01\r\x01\n\x01\r\x01\x10\x01\r\x02\x0f\x02\x07\x00\x06\x02\x0f\x02\x13\x01\x17\x01\x1b\x01\x13\x01\x17\x01\x17\x01\x1b\x02\x10\x02\x19\x01\x08\x02\x17\x02\x03\x01' (40 00 00 00 00 02 03 01 06 01 06 02 06 01 06 01 06 02 0C 02 18 02 07 00 0C 01 0D 01 0A 01 0D 01 10 01 0D 02 0F 02 07 00 06 02 0F 02 13 01 17 01 1B 01 13 01 17 01 17 01 1B 02 10 02 19 01 08 02 17 02 03 01),
00001366             INT: 0 (00 00 00 00),
0000136B             CODE:
                         argcount:
0000136C                     LONG: 7L (07 00 00 00)
                         nlocals:
00001370                     LONG: 8L (08 00 00 00)
                         stacksize:
00001374                     LONG: 5L (05 00 00 00)
                         flags:
00001378                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000137C                     STR: '|\x01\x00t\x01\x00i\x02\x00i\x03\x00j\x02\x00o:\x00\x01t\x04\x00|\x01\x00|\x02\x00\x83\x02\x00}\x07\x00|\x07\x00t\x07\x00j\t\x00o\x1a\x00\x01t\x08\x00i\t\x00|\x00\x00|\x07\x00|\x04\x00|\x04\x00\x83\x04\x00\x01qM\x00\x01n\x01\x00\x01|\x01\x00t\x01\x00i\x02\x00i\x0c\x00j\x02\x00o:\x00\x01t\r\x00|\x01\x00|\x02\x00\x83\x02\x00}\x07\x00|\x07\x00t\x07\x00j\t\x00o\x1a\x00\x01t\x08\x00i\t\x00|\x00\x00|\x07\x00|\x04\x00|\x04\x00\x83\x04\x00\x01q\x9a\x00\x01n\x01\x00\x01|\x01\x00t\x01\x00i\x02\x00i\x0e\x00j\x02\x00o\x1e\x00\x01t\x0f\x00i\x10\x00d\x01\x00\x83\x01\x00o\x0e\x00\x01t\x0f\x00i\x10\x00d\x02\x00\x83\x01\x00\x0co\x1a\x00\x01t\x08\x00i\t\x00|\x00\x00d\x03\x00|\x04\x00|\x04\x00\x83\x04\x00\x01n\x01\x00\x01d\x00\x00S' (EC 00 00 00 7C 01 00 74 01 00 69 02 00 69 03 00 6A 02 00 6F 3A 00 01 74 04 00 7C 01 00 7C 02 00 83 02 00 7D 07 00 7C 07 00 74 07 00 6A 09 00 6F 1A 00 01 74 08 00 69 09 00 7C 00 00 7C 07 00 7C 04 00 7C 04 00 83 04 00 01 71 4D 00 01 6E 01 00 01 7C 01 00 74 01 00 69 02 00 69 0C 00 6A 02 00 6F 3A 00 01 74 0D 00 7C 01 00 7C 02 00 83 02 00 7D 07 00 7C 07 00 74 07 00 6A 09 00 6F 1A 00 01 74 08 00 69 09 00 7C 00 00 7C 07 00 7C 04 00 7C 04 00 83 04 00 01 71 9A 00 01 6E 01 00 01 7C 01 00 74 01 00 69 02 00 69 0E 00 6A 02 00 6F 1E 00 01 74 0F 00 69 10 00 64 01 00 83 01 00 6F 0E 00 01 74 0F 00 69 10 00 64 02 00 83 01 00 0C 6F 1A 00 01 74 08 00 69 09 00 7C 00 00 64 03 00 7C 04 00 7C 04 00 83 04 00 01 6E 01 00 01 64 00 00 53)
                             00000000     7C - LOAD_FAST           'event'
                             00000003     74 - LOAD_GLOBAL         'constants'
                             00000006     69 - LOAD_ATTR           'OrgPointType'
                             00000009     69 - LOAD_ATTR           'OrgPointTypeNeoFragments'
                             0000000C     6A - COMPARE_OP          "=="
                             0000000F     6F - JUMP_IF_FALSE       -> 0000004C
                             00000012     01 - POP_TOP             
                             00000013     74 - LOAD_GLOBAL         'HandleNeoCorpseEvents'
                             00000016     7C - LOAD_FAST           'event'
                             00000019     7C - LOAD_FAST           'org'
                             0000001C     83 - CALL_FUNCTION       r0002
                             0000001F     7D - STORE_FAST          'ability'
                             00000022     7C - LOAD_FAST           'ability'
                             00000025     74 - LOAD_GLOBAL         'None'
                             00000028     6A - COMPARE_OP          "is not"
                             0000002B     6F - JUMP_IF_FALSE       -> 00000048
                             0000002E     01 - POP_TOP             
                             0000002F     74 - LOAD_GLOBAL         'discovery'
                             00000032     69 - LOAD_ATTR           'sendApplyAbilityToSelf'
                             00000035     7C - LOAD_FAST           'locator'
                             00000038     7C - LOAD_FAST           'ability'
                             0000003B     7C - LOAD_FAST           'level'
                             0000003E     7C - LOAD_FAST           'level'
                             00000041     83 - CALL_FUNCTION       r0004
                             00000044     01 - POP_TOP             
                             00000045     71 - JUMP_ABSOLUTE       -> 0000004D
                             00000048     01 - POP_TOP             
                             00000049     6E - JUMP_FORWARD        -> 0000004D
                             0000004C     01 - POP_TOP             
                             0000004D     7C - LOAD_FAST           'event'
                             00000050     74 - LOAD_GLOBAL         'constants'
                             00000053     69 - LOAD_ATTR           'OrgPointType'
                             00000056     69 - LOAD_ATTR           'OrgPointTypeEvent2Clues'
                             00000059     6A - COMPARE_OP          "=="
                             0000005C     6F - JUMP_IF_FALSE       -> 00000099
                             0000005F     01 - POP_TOP             
                             00000060     74 - LOAD_GLOBAL         'HandleEvent2Events'
                             00000063     7C - LOAD_FAST           'event'
                             00000066     7C - LOAD_FAST           'org'
                             00000069     83 - CALL_FUNCTION       r0002
                             0000006C     7D - STORE_FAST          'ability'
                             0000006F     7C - LOAD_FAST           'ability'
                             00000072     74 - LOAD_GLOBAL         'None'
                             00000075     6A - COMPARE_OP          "is not"
                             00000078     6F - JUMP_IF_FALSE       -> 00000095
                             0000007B     01 - POP_TOP             
                             0000007C     74 - LOAD_GLOBAL         'discovery'
                             0000007F     69 - LOAD_ATTR           'sendApplyAbilityToSelf'
                             00000082     7C - LOAD_FAST           'locator'
                             00000085     7C - LOAD_FAST           'ability'
                             00000088     7C - LOAD_FAST           'level'
                             0000008B     7C - LOAD_FAST           'level'
                             0000008E     83 - CALL_FUNCTION       r0004
                             00000091     01 - POP_TOP             
                             00000092     71 - JUMP_ABSOLUTE       -> 0000009A
                             00000095     01 - POP_TOP             
                             00000096     6E - JUMP_FORWARD        -> 0000009A
                             00000099     01 - POP_TOP             
                             0000009A     7C - LOAD_FAST           'event'
                             0000009D     74 - LOAD_GLOBAL         'constants'
                             000000A0     69 - LOAD_ATTR           'OrgPointType'
                             000000A3     69 - LOAD_ATTR           'OrgPointTypeHalloween'
                             000000A6     6A - COMPARE_OP          "=="
                             000000A9     6F - JUMP_IF_FALSE       -> 000000CA
                             000000AC     01 - POP_TOP             
                             000000AD     74 - LOAD_GLOBAL         'worldevent'
                             000000B0     69 - LOAD_ATTR           'isEventActive'
                             000000B3     64 - LOAD_CONST          '2008 Halloween Event Begins'
                             000000B6     83 - CALL_FUNCTION       r0001
                             000000B9     6F - JUMP_IF_FALSE       -> 000000CA
                             000000BC     01 - POP_TOP             
                             000000BD     74 - LOAD_GLOBAL         'worldevent'
                             000000C0     69 - LOAD_ATTR           'isEventActive'
                             000000C3     64 - LOAD_CONST          '2008 Halloween Event Ends'
                             000000C6     83 - CALL_FUNCTION       r0001
                             000000C9     0C - UNARY_NOT           
                             000000CA     6F - JUMP_IF_FALSE       -> 000000E7
                             000000CD     01 - POP_TOP             
                             000000CE     74 - LOAD_GLOBAL         'discovery'
                             000000D1     69 - LOAD_ATTR           'sendApplyAbilityToSelf'
                             000000D4     7C - LOAD_FAST           'locator'
                             000000D7     64 - LOAD_CONST          1004
                             000000DA     7C - LOAD_FAST           'level'
                             000000DD     7C - LOAD_FAST           'level'
                             000000E0     83 - CALL_FUNCTION       r0004
                             000000E3     01 - POP_TOP             
                             000000E4     6E - JUMP_FORWARD        -> 000000E8
                             000000E7     01 - POP_TOP             
                             000000E8     64 - LOAD_CONST          None
                             000000EB     53 - RETURN_VALUE        
                         consts:
0000146D                     TUPLE: (
00001472                         None (4E),
00001473                         STR: '2008 Halloween Event Begins' (1B 00 00 00 32 30 30 38 20 48 61 6C 6C 6F 77 65 65 6E 20 45 76 65 6E 74 20 42 65 67 69 6E 73),
00001493                         STR: '2008 Halloween Event Ends' (19 00 00 00 32 30 30 38 20 48 61 6C 6C 6F 77 65 65 6E 20 45 76 65 6E 74 20 45 6E 64 73),
000014B1                         INT: 1004 (EC 03 00 00)
                             )
                         names:
000014B6                     TUPLE: (
000014BB                         STR: 'event' (05 00 00 00 65 76 65 6E 74),
000014C5                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
000014D3                         STR: 'OrgPointType' (0C 00 00 00 4F 72 67 50 6F 69 6E 74 54 79 70 65),
000014E4                         STR: 'OrgPointTypeNeoFragments' (18 00 00 00 4F 72 67 50 6F 69 6E 74 54 79 70 65 4E 65 6F 46 72 61 67 6D 65 6E 74 73),
00001501                         STR: 'HandleNeoCorpseEvents' (15 00 00 00 48 61 6E 64 6C 65 4E 65 6F 43 6F 72 70 73 65 45 76 65 6E 74 73),
0000151B                         STR: 'org' (03 00 00 00 6F 72 67),
00001523                         STR: 'ability' (07 00 00 00 61 62 69 6C 69 74 79),
0000152F                         STR: 'None' (04 00 00 00 4E 6F 6E 65),
00001538                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
00001546                         STR: 'sendApplyAbilityToSelf' (16 00 00 00 73 65 6E 64 41 70 70 6C 79 41 62 69 6C 69 74 79 54 6F 53 65 6C 66),
00001561                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
0000156D                         STR: 'level' (05 00 00 00 6C 65 76 65 6C),
00001577                         STR: 'OrgPointTypeEvent2Clues' (17 00 00 00 4F 72 67 50 6F 69 6E 74 54 79 70 65 45 76 65 6E 74 32 43 6C 75 65 73),
00001593                         STR: 'HandleEvent2Events' (12 00 00 00 48 61 6E 64 6C 65 45 76 65 6E 74 32 45 76 65 6E 74 73),
000015AA                         STR: 'OrgPointTypeHalloween' (15 00 00 00 4F 72 67 50 6F 69 6E 74 54 79 70 65 48 61 6C 6C 6F 77 65 65 6E),
000015C4                         STR: 'worldevent' (0A 00 00 00 77 6F 72 6C 64 65 76 65 6E 74),
000015D3                         STR: 'isEventActive' (0D 00 00 00 69 73 45 76 65 6E 74 41 63 74 69 76 65)
                             )
                         varnames:
000015E5                     TUPLE: (
000015EA                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
000015F6                         STR: 'event' (05 00 00 00 65 76 65 6E 74),
00001600                         STR: 'org' (03 00 00 00 6F 72 67),
00001608                         STR: 'reputation' (0A 00 00 00 72 65 70 75 74 61 74 69 6F 6E),
00001617                         STR: 'level' (05 00 00 00 6C 65 76 65 6C),
00001621                         STR: 'faction' (07 00 00 00 66 61 63 74 69 6F 6E),
0000162D                         STR: 'crew' (04 00 00 00 63 72 65 77),
00001636                         STR: 'ability' (07 00 00 00 61 62 69 6C 69 74 79)
                             )
                         freevars:
00001642                     TUPLE: ()
                         cellvars:
00001647                     TUPLE: ()
                         filename:
0000164C                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\trgs.py' (3C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 74 72 67 73 2E 70 79)
                         name:
0000168D                     STR: 'HandleInvokeOrgEvent' (14 00 00 00 48 61 6E 64 6C 65 49 6E 76 6F 6B 65 4F 72 67 45 76 65 6E 74)
                         firslineno:
000016A6                     LONG: 159L (9F 00 00 00)
                         lnotab:
000016AA                     STR: '\x00\x01\x13\x01\x0f\x01\r\x01\x1e\x02\x13\x01\x0f\x01\r\x01\x1e\x024\x03' (14 00 00 00 00 01 13 01 0F 01 0D 01 1E 02 13 01 0F 01 0D 01 1E 02 34 03),
000016C3             CODE:
                         argcount:
000016C4                     LONG: 2L (02 00 00 00)
                         nlocals:
000016C8                     LONG: 10L (0A 00 00 00)
                         stacksize:
000016CC                     LONG: 5L (05 00 00 00)
                         flags:
000016D0                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000016D4                     STR: 't\x00\x00t\x01\x00j\x08\x00o\x08\x00\x01d\x00\x00Sn\x01\x00\x01t\x00\x00i\x02\x00d\x01\x00\x83\x01\x00\x0co\x08\x00\x01d\x00\x00Sn\x01\x00\x01t\x00\x00i\x02\x00d\x02\x00\x83\x01\x00o\x08\x00\x01d\x00\x00Sn\x01\x00\x01t\x00\x00i\x02\x00d\x03\x00\x83\x01\x00}\x02\x00t\x00\x00i\x04\x00|\x00\x00\x83\x01\x00}\x04\x00g\x00\x00\x04i\x07\x00}\x06\x00t\t\x00t\n\x00|\x04\x00\x83\x01\x00\x83\x01\x00D]\x1a\x00}\x03\x00|\x06\x00|\x04\x00|\x03\x00\x19|\x03\x00f\x02\x00\x83\x01\x00\x01q~\x00~\x06\x00}\x04\x00|\x04\x00i\x0c\x00\x83\x00\x00\x01|\x04\x00i\r\x00\x83\x00\x00\x01g\x00\x00\x04i\x07\x00}\x06\x00|\x04\x00D]\x14\x00}\x08\x00|\x06\x00|\x08\x00d\x04\x00\x19\x83\x01\x00\x01q\xc3\x00~\x06\x00}\t\x00t\x10\x00|\t\x00i\x11\x00|\x01\x00\x83\x01\x00d\x05\x00\x83\x02\x00}\x07\x00|\x02\x00o)\x00\x01|\x07\x00d\x06\x00j\x02\x00o\x0e\x00\x01t\x14\x00i\x15\x00i\x16\x00SqQ\x01\x01t\x14\x00i\x15\x00i\x17\x00Sn*\x00\x01t\x14\x00i\x15\x00i\x18\x00t\x14\x00i\x15\x00i\x19\x00t\x14\x00i\x15\x00i\x1a\x00g\x03\x00}\x05\x00|\x05\x00|\x07\x00\x19Sd\x00\x00S' (55 01 00 00 74 00 00 74 01 00 6A 08 00 6F 08 00 01 64 00 00 53 6E 01 00 01 74 00 00 69 02 00 64 01 00 83 01 00 0C 6F 08 00 01 64 00 00 53 6E 01 00 01 74 00 00 69 02 00 64 02 00 83 01 00 6F 08 00 01 64 00 00 53 6E 01 00 01 74 00 00 69 02 00 64 03 00 83 01 00 7D 02 00 74 00 00 69 04 00 7C 00 00 83 01 00 7D 04 00 67 00 00 04 69 07 00 7D 06 00 74 09 00 74 0A 00 7C 04 00 83 01 00 83 01 00 44 5D 1A 00 7D 03 00 7C 06 00 7C 04 00 7C 03 00 19 7C 03 00 66 02 00 83 01 00 01 71 7E 00 7E 06 00 7D 04 00 7C 04 00 69 0C 00 83 00 00 01 7C 04 00 69 0D 00 83 00 00 01 67 00 00 04 69 07 00 7D 06 00 7C 04 00 44 5D 14 00 7D 08 00 7C 06 00 7C 08 00 64 04 00 19 83 01 00 01 71 C3 00 7E 06 00 7D 09 00 74 10 00 7C 09 00 69 11 00 7C 01 00 83 01 00 64 05 00 83 02 00 7D 07 00 7C 02 00 6F 29 00 01 7C 07 00 64 06 00 6A 02 00 6F 0E 00 01 74 14 00 69 15 00 69 16 00 53 71 51 01 01 74 14 00 69 15 00 69 17 00 53 6E 2A 00 01 74 14 00 69 15 00 69 18 00 74 14 00 69 15 00 69 19 00 74 14 00 69 15 00 69 1A 00 67 03 00 7D 05 00 7C 05 00 7C 07 00 19 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'worldevent'
                             00000003     74 - LOAD_GLOBAL         'None'
                             00000006     6A - COMPARE_OP          "is"
                             00000009     6F - JUMP_IF_FALSE       -> 00000014
                             0000000C     01 - POP_TOP             
                             0000000D     64 - LOAD_CONST          None
                             00000010     53 - RETURN_VALUE        
                             00000011     6E - JUMP_FORWARD        -> 00000015
                             00000014     01 - POP_TOP             
                             00000015     74 - LOAD_GLOBAL         'worldevent'
                             00000018     69 - LOAD_ATTR           'isEventActive'
                             0000001B     64 - LOAD_CONST          'Neo Corpse Begins'
                             0000001E     83 - CALL_FUNCTION       r0001
                             00000021     0C - UNARY_NOT           
                             00000022     6F - JUMP_IF_FALSE       -> 0000002D
                             00000025     01 - POP_TOP             
                             00000026     64 - LOAD_CONST          None
                             00000029     53 - RETURN_VALUE        
                             0000002A     6E - JUMP_FORWARD        -> 0000002E
                             0000002D     01 - POP_TOP             
                             0000002E     74 - LOAD_GLOBAL         'worldevent'
                             00000031     69 - LOAD_ATTR           'isEventActive'
                             00000034     64 - LOAD_CONST          'Neo Corpse Buff Ends'
                             00000037     83 - CALL_FUNCTION       r0001
                             0000003A     6F - JUMP_IF_FALSE       -> 00000045
                             0000003D     01 - POP_TOP             
                             0000003E     64 - LOAD_CONST          None
                             00000041     53 - RETURN_VALUE        
                             00000042     6E - JUMP_FORWARD        -> 00000046
                             00000045     01 - POP_TOP             
                             00000046     74 - LOAD_GLOBAL         'worldevent'
                             00000049     69 - LOAD_ATTR           'isEventActive'
                             0000004C     64 - LOAD_CONST          'Neo Corpse Ends'
                             0000004F     83 - CALL_FUNCTION       r0001
                             00000052     7D - STORE_FAST          'bIsAfterCollection'
                             00000055     74 - LOAD_GLOBAL         'worldevent'
                             00000058     69 - LOAD_ATTR           'getNormalizedOrgPoints'
                             0000005B     7C - LOAD_FAST           'event'
                             0000005E     83 - CALL_FUNCTION       r0001
                             00000061     7D - STORE_FAST          'normalizedPoints'
                             00000064     67 - BUILD_LIST          r0000
                             00000067     04 - DUP_TOP             
                             00000068     69 - LOAD_ATTR           'append'
                             0000006B     7D - STORE_FAST          '_[1]'
                             0000006E     74 - LOAD_GLOBAL         'range'
                             00000071     74 - LOAD_GLOBAL         'len'
                             00000074     7C - LOAD_FAST           'normalizedPoints'
                             00000077     83 - CALL_FUNCTION       r0001
                             0000007A     83 - CALL_FUNCTION       r0001
                             0000007D     44 - GET_ITER            
                             0000007E     5D - FOR_ITER            -> 0000009B
                             00000081     7D - STORE_FAST          'i'
                             00000084     7C - LOAD_FAST           '_[1]'
                             00000087     7C - LOAD_FAST           'normalizedPoints'
                             0000008A     7C - LOAD_FAST           'i'
                             0000008D     19 - BINARY_SUBSCR       
                             0000008E     7C - LOAD_FAST           'i'
                             00000091     66 - BUILD_TUPLE         r0002
                             00000094     83 - CALL_FUNCTION       r0001
                             00000097     01 - POP_TOP             
                             00000098     71 - JUMP_ABSOLUTE       -> 0000007E
                             0000009B     7E - DELETE_FAST         '_[1]'
                             0000009E     7D - STORE_FAST          'normalizedPoints'
                             000000A1     7C - LOAD_FAST           'normalizedPoints'
                             000000A4     69 - LOAD_ATTR           'sort'
                             000000A7     83 - CALL_FUNCTION       r0000
                             000000AA     01 - POP_TOP             
                             000000AB     7C - LOAD_FAST           'normalizedPoints'
                             000000AE     69 - LOAD_ATTR           'reverse'
                             000000B1     83 - CALL_FUNCTION       r0000
                             000000B4     01 - POP_TOP             
                             000000B5     67 - BUILD_LIST          r0000
                             000000B8     04 - DUP_TOP             
                             000000B9     69 - LOAD_ATTR           'append'
                             000000BC     7D - STORE_FAST          '_[1]'
                             000000BF     7C - LOAD_FAST           'normalizedPoints'
                             000000C2     44 - GET_ITER            
                             000000C3     5D - FOR_ITER            -> 000000DA
                             000000C6     7D - STORE_FAST          'pair'
                             000000C9     7C - LOAD_FAST           '_[1]'
                             000000CC     7C - LOAD_FAST           'pair'
                             000000CF     64 - LOAD_CONST          1
                             000000D2     19 - BINARY_SUBSCR       
                             000000D3     83 - CALL_FUNCTION       r0001
                             000000D6     01 - POP_TOP             
                             000000D7     71 - JUMP_ABSOLUTE       -> 000000C3
                             000000DA     7E - DELETE_FAST         '_[1]'
                             000000DD     7D - STORE_FAST          'orgOrder'
                             000000E0     74 - LOAD_GLOBAL         'min'
                             000000E3     7C - LOAD_FAST           'orgOrder'
                             000000E6     69 - LOAD_ATTR           'index'
                             000000E9     7C - LOAD_FAST           'org'
                             000000EC     83 - CALL_FUNCTION       r0001
                             000000EF     64 - LOAD_CONST          2
                             000000F2     83 - CALL_FUNCTION       r0002
                             000000F5     7D - STORE_FAST          'orgPlace'
                             000000F8     7C - LOAD_FAST           'bIsAfterCollection'
                             000000FB     6F - JUMP_IF_FALSE       -> 00000127
                             000000FE     01 - POP_TOP             
                             000000FF     7C - LOAD_FAST           'orgPlace'
                             00000102     64 - LOAD_CONST          0
                             00000105     6A - COMPARE_OP          "=="
                             00000108     6F - JUMP_IF_FALSE       -> 00000119
                             0000010B     01 - POP_TOP             
                             0000010C     74 - LOAD_GLOBAL         'constants'
                             0000010F     69 - LOAD_ATTR           'Ability'
                             00000112     69 - LOAD_ATTR           'Event1_1Neo5Ability'
                             00000115     53 - RETURN_VALUE        
                             00000116     71 - JUMP_ABSOLUTE       -> 00000151
                             00000119     01 - POP_TOP             
                             0000011A     74 - LOAD_GLOBAL         'constants'
                             0000011D     69 - LOAD_ATTR           'Ability'
                             00000120     69 - LOAD_ATTR           'Event1_1Neo4Ability'
                             00000123     53 - RETURN_VALUE        
                             00000124     6E - JUMP_FORWARD        -> 00000151
                             00000127     01 - POP_TOP             
                             00000128     74 - LOAD_GLOBAL         'constants'
                             0000012B     69 - LOAD_ATTR           'Ability'
                             0000012E     69 - LOAD_ATTR           'Event1_1Neo3Ability'
                             00000131     74 - LOAD_GLOBAL         'constants'
                             00000134     69 - LOAD_ATTR           'Ability'
                             00000137     69 - LOAD_ATTR           'Event1_1Neo2Ability'
                             0000013A     74 - LOAD_GLOBAL         'constants'
                             0000013D     69 - LOAD_ATTR           'Ability'
                             00000140     69 - LOAD_ATTR           'Event1_1Neo1Ability'
                             00000143     67 - BUILD_LIST          r0003
                             00000146     7D - STORE_FAST          'aAbility'
                             00000149     7C - LOAD_FAST           'aAbility'
                             0000014C     7C - LOAD_FAST           'orgPlace'
                             0000014F     19 - BINARY_SUBSCR       
                             00000150     53 - RETURN_VALUE        
                             00000151     64 - LOAD_CONST          None
                             00000154     53 - RETURN_VALUE        
                         consts:
0000182E                     TUPLE: (
00001833                         None (4E),
00001834                         STR: 'Neo Corpse Begins' (11 00 00 00 4E 65 6F 20 43 6F 72 70 73 65 20 42 65 67 69 6E 73),
0000184A                         STR: 'Neo Corpse Buff Ends' (14 00 00 00 4E 65 6F 20 43 6F 72 70 73 65 20 42 75 66 66 20 45 6E 64 73),
00001863                         STR: 'Neo Corpse Ends' (0F 00 00 00 4E 65 6F 20 43 6F 72 70 73 65 20 45 6E 64 73),
00001877                         INT: 1 (01 00 00 00),
0000187C                         INT: 2 (02 00 00 00),
00001881                         INT: 0 (00 00 00 00)
                             )
                         names:
00001886                     TUPLE: (
0000188B                         STR: 'worldevent' (0A 00 00 00 77 6F 72 6C 64 65 76 65 6E 74),
0000189A                         STR: 'None' (04 00 00 00 4E 6F 6E 65),
000018A3                         STR: 'isEventActive' (0D 00 00 00 69 73 45 76 65 6E 74 41 63 74 69 76 65),
000018B5                         STR: 'bIsAfterCollection' (12 00 00 00 62 49 73 41 66 74 65 72 43 6F 6C 6C 65 63 74 69 6F 6E),
000018CC                         STR: 'getNormalizedOrgPoints' (16 00 00 00 67 65 74 4E 6F 72 6D 61 6C 69 7A 65 64 4F 72 67 50 6F 69 6E 74 73),
000018E7                         STR: 'event' (05 00 00 00 65 76 65 6E 74),
000018F1                         STR: 'normalizedPoints' (10 00 00 00 6E 6F 72 6D 61 6C 69 7A 65 64 50 6F 69 6E 74 73),
00001906                         STR: 'append' (06 00 00 00 61 70 70 65 6E 64),
00001911                         STR: '_[1]' (04 00 00 00 5F 5B 31 5D),
0000191A                         STR: 'range' (05 00 00 00 72 61 6E 67 65),
00001924                         STR: 'len' (03 00 00 00 6C 65 6E),
0000192C                         STR: 'i' (01 00 00 00 69),
00001932                         STR: 'sort' (04 00 00 00 73 6F 72 74),
0000193B                         STR: 'reverse' (07 00 00 00 72 65 76 65 72 73 65),
00001947                         STR: 'pair' (04 00 00 00 70 61 69 72),
00001950                         STR: 'orgOrder' (08 00 00 00 6F 72 67 4F 72 64 65 72),
0000195D                         STR: 'min' (03 00 00 00 6D 69 6E),
00001965                         STR: 'index' (05 00 00 00 69 6E 64 65 78),
0000196F                         STR: 'org' (03 00 00 00 6F 72 67),
00001977                         STR: 'orgPlace' (08 00 00 00 6F 72 67 50 6C 61 63 65),
00001984                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00001992                         STR: 'Ability' (07 00 00 00 41 62 69 6C 69 74 79),
0000199E                         STR: 'Event1_1Neo5Ability' (13 00 00 00 45 76 65 6E 74 31 5F 31 4E 65 6F 35 41 62 69 6C 69 74 79),
000019B6                         STR: 'Event1_1Neo4Ability' (13 00 00 00 45 76 65 6E 74 31 5F 31 4E 65 6F 34 41 62 69 6C 69 74 79),
000019CE                         STR: 'Event1_1Neo3Ability' (13 00 00 00 45 76 65 6E 74 31 5F 31 4E 65 6F 33 41 62 69 6C 69 74 79),
000019E6                         STR: 'Event1_1Neo2Ability' (13 00 00 00 45 76 65 6E 74 31 5F 31 4E 65 6F 32 41 62 69 6C 69 74 79),
000019FE                         STR: 'Event1_1Neo1Ability' (13 00 00 00 45 76 65 6E 74 31 5F 31 4E 65 6F 31 41 62 69 6C 69 74 79),
00001A16                         STR: 'aAbility' (08 00 00 00 61 41 62 69 6C 69 74 79)
                             )
                         varnames:
00001A23                     TUPLE: (
00001A28                         STR: 'event' (05 00 00 00 65 76 65 6E 74),
00001A32                         STR: 'org' (03 00 00 00 6F 72 67),
00001A3A                         STR: 'bIsAfterCollection' (12 00 00 00 62 49 73 41 66 74 65 72 43 6F 6C 6C 65 63 74 69 6F 6E),
00001A51                         STR: 'i' (01 00 00 00 69),
00001A57                         STR: 'normalizedPoints' (10 00 00 00 6E 6F 72 6D 61 6C 69 7A 65 64 50 6F 69 6E 74 73),
00001A6C                         STR: 'aAbility' (08 00 00 00 61 41 62 69 6C 69 74 79),
00001A79                         STR: '_[1]' (04 00 00 00 5F 5B 31 5D),
00001A82                         STR: 'orgPlace' (08 00 00 00 6F 72 67 50 6C 61 63 65),
00001A8F                         STR: 'pair' (04 00 00 00 70 61 69 72),
00001A98                         STR: 'orgOrder' (08 00 00 00 6F 72 67 4F 72 64 65 72)
                             )
                         freevars:
00001AA5                     TUPLE: ()
                         cellvars:
00001AAA                     TUPLE: ()
                         filename:
00001AAF                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\trgs.py' (3C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 74 72 67 73 2E 70 79)
                         name:
00001AF0                     STR: 'HandleNeoCorpseEvents' (15 00 00 00 48 61 6E 64 6C 65 4E 65 6F 43 6F 72 70 73 65 45 76 65 6E 74 73)
                         firslineno:
00001B0A                     LONG: 175L (AF 00 00 00)
                         lnotab:
00001B0E                     STR: '\x00\x01\r\x01\x08\x02\x11\x01\x08\x02\x10\x01\x08\x02\x0f\x02\x0f\x02=\x02\n\x03\n\x02+\x02\x18\x02\x07\x01\r\x02\x0e\x03\x0e\x03!\x04' (26 00 00 00 00 01 0D 01 08 02 11 01 08 02 10 01 08 02 0F 02 0F 02 3D 02 0A 03 0A 02 2B 02 18 02 07 01 0D 02 0E 03 0E 03 21 04),
00001B39             CODE:
                         argcount:
00001B3A                     LONG: 2L (02 00 00 00)
                         nlocals:
00001B3E                     LONG: 11L (0B 00 00 00)
                         stacksize:
00001B42                     LONG: 5L (05 00 00 00)
                         flags:
00001B46                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001B4A                     STR: 't\x00\x00t\x01\x00j\x08\x00o\x08\x00\x01d\x00\x00Sn\x01\x00\x01t\x00\x00i\x02\x00d\x01\x00\x83\x01\x00\x0co\x08\x00\x01d\x00\x00Sn\x01\x00\x01t\x00\x00i\x02\x00d\x02\x00\x83\x01\x00o\x08\x00\x01d\x00\x00Sn\x01\x00\x01t\x00\x00i\x02\x00d\x03\x00\x83\x01\x00}\x02\x00t\x00\x00i\x04\x00|\x00\x00\x83\x01\x00}\x04\x00g\x00\x00\x04i\x07\x00}\x06\x00t\t\x00t\n\x00|\x04\x00\x83\x01\x00\x83\x01\x00D]\x1a\x00}\x03\x00|\x06\x00|\x04\x00|\x03\x00\x19|\x03\x00f\x02\x00\x83\x01\x00\x01q~\x00~\x06\x00}\x04\x00|\x04\x00i\x0c\x00\x83\x00\x00\x01|\x04\x00i\r\x00\x83\x00\x00\x01g\x00\x00\x04i\x07\x00}\x06\x00|\x04\x00D]\x14\x00}\t\x00|\x06\x00|\t\x00d\x04\x00\x19\x83\x01\x00\x01q\xc3\x00~\x06\x00}\n\x00t\x10\x00|\n\x00i\x11\x00|\x01\x00\x83\x01\x00d\x05\x00\x83\x02\x00}\x07\x00t\x14\x00t\x10\x00|\x01\x00d\x06\x00\x83\x02\x00d\x04\x00\x83\x02\x00d\x04\x00\x18}\x08\x00|\x02\x00oo\x00\x01t\x16\x00i\x17\x00i\x18\x00t\x16\x00i\x17\x00i\x19\x00t\x16\x00i\x17\x00i\x1a\x00g\x03\x00t\x16\x00i\x17\x00i\x1b\x00t\x16\x00i\x17\x00i\x1c\x00t\x16\x00i\x17\x00i\x1d\x00g\x03\x00g\x02\x00}\x05\x00|\x07\x00d\x07\x00j\x02\x00o\x10\x00\x01|\x05\x00d\x04\x00\x19|\x08\x00\x19Sq\xf6\x01\x01|\x05\x00d\x07\x00\x19|\x08\x00\x19Snm\x00\x01t\x16\x00i\x17\x00i\x1f\x00t\x16\x00i\x17\x00i \x00t\x16\x00i\x17\x00i!\x00g\x03\x00t\x16\x00i\x17\x00i\x18\x00t\x16\x00i\x17\x00i\x19\x00t\x16\x00i\x17\x00i\x1a\x00g\x03\x00t\x16\x00i\x17\x00i"\x00t\x16\x00i\x17\x00i#\x00t\x16\x00i\x17\x00i$\x00g\x03\x00g\x03\x00}\x05\x00|\x05\x00|\x07\x00\x19|\x08\x00\x19Sd\x00\x00S' (FA 01 00 00 74 00 00 74 01 00 6A 08 00 6F 08 00 01 64 00 00 53 6E 01 00 01 74 00 00 69 02 00 64 01 00 83 01 00 0C 6F 08 00 01 64 00 00 53 6E 01 00 01 74 00 00 69 02 00 64 02 00 83 01 00 6F 08 00 01 64 00 00 53 6E 01 00 01 74 00 00 69 02 00 64 03 00 83 01 00 7D 02 00 74 00 00 69 04 00 7C 00 00 83 01 00 7D 04 00 67 00 00 04 69 07 00 7D 06 00 74 09 00 74 0A 00 7C 04 00 83 01 00 83 01 00 44 5D 1A 00 7D 03 00 7C 06 00 7C 04 00 7C 03 00 19 7C 03 00 66 02 00 83 01 00 01 71 7E 00 7E 06 00 7D 04 00 7C 04 00 69 0C 00 83 00 00 01 7C 04 00 69 0D 00 83 00 00 01 67 00 00 04 69 07 00 7D 06 00 7C 04 00 44 5D 14 00 7D 09 00 7C 06 00 7C 09 00 64 04 00 19 83 01 00 01 71 C3 00 7E 06 00 7D 0A 00 74 10 00 7C 0A 00 69 11 00 7C 01 00 83 01 00 64 05 00 83 02 00 7D 07 00 74 14 00 74 10 00 7C 01 00 64 06 00 83 02 00 64 04 00 83 02 00 64 04 00 18 7D 08 00 7C 02 00 6F 6F 00 01 74 16 00 69 17 00 69 18 00 74 16 00 69 17 00 69 19 00 74 16 00 69 17 00 69 1A 00 67 03 00 74 16 00 69 17 00 69 1B 00 74 16 00 69 17 00 69 1C 00 74 16 00 69 17 00 69 1D 00 67 03 00 67 02 00 7D 05 00 7C 07 00 64 07 00 6A 02 00 6F 10 00 01 7C 05 00 64 04 00 19 7C 08 00 19 53 71 F6 01 01 7C 05 00 64 07 00 19 7C 08 00 19 53 6E 6D 00 01 74 16 00 69 17 00 69 1F 00 74 16 00 69 17 00 69 20 00 74 16 00 69 17 00 69 21 00 67 03 00 74 16 00 69 17 00 69 18 00 74 16 00 69 17 00 69 19 00 74 16 00 69 17 00 69 1A 00 67 03 00 74 16 00 69 17 00 69 22 00 74 16 00 69 17 00 69 23 00 74 16 00 69 17 00 69 24 00 67 03 00 67 03 00 7D 05 00 7C 05 00 7C 07 00 19 7C 08 00 19 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'worldevent'
                             00000003     74 - LOAD_GLOBAL         'None'
                             00000006     6A - COMPARE_OP          "is"
                             00000009     6F - JUMP_IF_FALSE       -> 00000014
                             0000000C     01 - POP_TOP             
                             0000000D     64 - LOAD_CONST          None
                             00000010     53 - RETURN_VALUE        
                             00000011     6E - JUMP_FORWARD        -> 00000015
                             00000014     01 - POP_TOP             
                             00000015     74 - LOAD_GLOBAL         'worldevent'
                             00000018     69 - LOAD_ATTR           'isEventActive'
                             0000001B     64 - LOAD_CONST          'Flymen - Buff Stage 1'
                             0000001E     83 - CALL_FUNCTION       r0001
                             00000021     0C - UNARY_NOT           
                             00000022     6F - JUMP_IF_FALSE       -> 0000002D
                             00000025     01 - POP_TOP             
                             00000026     64 - LOAD_CONST          None
                             00000029     53 - RETURN_VALUE        
                             0000002A     6E - JUMP_FORWARD        -> 0000002E
                             0000002D     01 - POP_TOP             
                             0000002E     74 - LOAD_GLOBAL         'worldevent'
                             00000031     69 - LOAD_ATTR           'isEventActive'
                             00000034     64 - LOAD_CONST          'Flymen - Buff Ends'
                             00000037     83 - CALL_FUNCTION       r0001
                             0000003A     6F - JUMP_IF_FALSE       -> 00000045
                             0000003D     01 - POP_TOP             
                             0000003E     64 - LOAD_CONST          None
                             00000041     53 - RETURN_VALUE        
                             00000042     6E - JUMP_FORWARD        -> 00000046
                             00000045     01 - POP_TOP             
                             00000046     74 - LOAD_GLOBAL         'worldevent'
                             00000049     69 - LOAD_ATTR           'isEventActive'
                             0000004C     64 - LOAD_CONST          'Flymen - Buff Stage 2'
                             0000004F     83 - CALL_FUNCTION       r0001
                             00000052     7D - STORE_FAST          'bIsAfterCollection'
                             00000055     74 - LOAD_GLOBAL         'worldevent'
                             00000058     69 - LOAD_ATTR           'getNormalizedOrgPoints'
                             0000005B     7C - LOAD_FAST           'event'
                             0000005E     83 - CALL_FUNCTION       r0001
                             00000061     7D - STORE_FAST          'normalizedPoints'
                             00000064     67 - BUILD_LIST          r0000
                             00000067     04 - DUP_TOP             
                             00000068     69 - LOAD_ATTR           'append'
                             0000006B     7D - STORE_FAST          '_[1]'
                             0000006E     74 - LOAD_GLOBAL         'range'
                             00000071     74 - LOAD_GLOBAL         'len'
                             00000074     7C - LOAD_FAST           'normalizedPoints'
                             00000077     83 - CALL_FUNCTION       r0001
                             0000007A     83 - CALL_FUNCTION       r0001
                             0000007D     44 - GET_ITER            
                             0000007E     5D - FOR_ITER            -> 0000009B
                             00000081     7D - STORE_FAST          'i'
                             00000084     7C - LOAD_FAST           '_[1]'
                             00000087     7C - LOAD_FAST           'normalizedPoints'
                             0000008A     7C - LOAD_FAST           'i'
                             0000008D     19 - BINARY_SUBSCR       
                             0000008E     7C - LOAD_FAST           'i'
                             00000091     66 - BUILD_TUPLE         r0002
                             00000094     83 - CALL_FUNCTION       r0001
                             00000097     01 - POP_TOP             
                             00000098     71 - JUMP_ABSOLUTE       -> 0000007E
                             0000009B     7E - DELETE_FAST         '_[1]'
                             0000009E     7D - STORE_FAST          'normalizedPoints'
                             000000A1     7C - LOAD_FAST           'normalizedPoints'
                             000000A4     69 - LOAD_ATTR           'sort'
                             000000A7     83 - CALL_FUNCTION       r0000
                             000000AA     01 - POP_TOP             
                             000000AB     7C - LOAD_FAST           'normalizedPoints'
                             000000AE     69 - LOAD_ATTR           'reverse'
                             000000B1     83 - CALL_FUNCTION       r0000
                             000000B4     01 - POP_TOP             
                             000000B5     67 - BUILD_LIST          r0000
                             000000B8     04 - DUP_TOP             
                             000000B9     69 - LOAD_ATTR           'append'
                             000000BC     7D - STORE_FAST          '_[1]'
                             000000BF     7C - LOAD_FAST           'normalizedPoints'
                             000000C2     44 - GET_ITER            
                             000000C3     5D - FOR_ITER            -> 000000DA
                             000000C6     7D - STORE_FAST          'pair'
                             000000C9     7C - LOAD_FAST           '_[1]'
                             000000CC     7C - LOAD_FAST           'pair'
                             000000CF     64 - LOAD_CONST          1
                             000000D2     19 - BINARY_SUBSCR       
                             000000D3     83 - CALL_FUNCTION       r0001
                             000000D6     01 - POP_TOP             
                             000000D7     71 - JUMP_ABSOLUTE       -> 000000C3
                             000000DA     7E - DELETE_FAST         '_[1]'
                             000000DD     7D - STORE_FAST          'orgOrder'
                             000000E0     74 - LOAD_GLOBAL         'min'
                             000000E3     7C - LOAD_FAST           'orgOrder'
                             000000E6     69 - LOAD_ATTR           'index'
                             000000E9     7C - LOAD_FAST           'org'
                             000000EC     83 - CALL_FUNCTION       r0001
                             000000EF     64 - LOAD_CONST          2
                             000000F2     83 - CALL_FUNCTION       r0002
                             000000F5     7D - STORE_FAST          'orgPlace'
                             000000F8     74 - LOAD_GLOBAL         'max'
                             000000FB     74 - LOAD_GLOBAL         'min'
                             000000FE     7C - LOAD_FAST           'org'
                             00000101     64 - LOAD_CONST          3
                             00000104     83 - CALL_FUNCTION       r0002
                             00000107     64 - LOAD_CONST          1
                             0000010A     83 - CALL_FUNCTION       r0002
                             0000010D     64 - LOAD_CONST          1
                             00000110     18 - BINARY_SUBTRACT     
                             00000111     7D - STORE_FAST          'orgNum'
                             00000114     7C - LOAD_FAST           'bIsAfterCollection'
                             00000117     6F - JUMP_IF_FALSE       -> 00000189
                             0000011A     01 - POP_TOP             
                             0000011B     74 - LOAD_GLOBAL         'constants'
                             0000011E     69 - LOAD_ATTR           'Ability'
                             00000121     69 - LOAD_ATTR           'Event2_0Zion2Ability'
                             00000124     74 - LOAD_GLOBAL         'constants'
                             00000127     69 - LOAD_ATTR           'Ability'
                             0000012A     69 - LOAD_ATTR           'Event2_0Machine2Ability'
                             0000012D     74 - LOAD_GLOBAL         'constants'
                             00000130     69 - LOAD_ATTR           'Ability'
                             00000133     69 - LOAD_ATTR           'Event2_0Merv2Ability'
                             00000136     67 - BUILD_LIST          r0003
                             00000139     74 - LOAD_GLOBAL         'constants'
                             0000013C     69 - LOAD_ATTR           'Ability'
                             0000013F     69 - LOAD_ATTR           'Event2_0Zion4Ability'
                             00000142     74 - LOAD_GLOBAL         'constants'
                             00000145     69 - LOAD_ATTR           'Ability'
                             00000148     69 - LOAD_ATTR           'Event2_0Machine4Ability'
                             0000014B     74 - LOAD_GLOBAL         'constants'
                             0000014E     69 - LOAD_ATTR           'Ability'
                             00000151     69 - LOAD_ATTR           'Event2_0Merv4Ability'
                             00000154     67 - BUILD_LIST          r0003
                             00000157     67 - BUILD_LIST          r0002
                             0000015A     7D - STORE_FAST          'aAbility'
                             0000015D     7C - LOAD_FAST           'orgPlace'
                             00000160     64 - LOAD_CONST          0
                             00000163     6A - COMPARE_OP          "=="
                             00000166     6F - JUMP_IF_FALSE       -> 00000179
                             00000169     01 - POP_TOP             
                             0000016A     7C - LOAD_FAST           'aAbility'
                             0000016D     64 - LOAD_CONST          1
                             00000170     19 - BINARY_SUBSCR       
                             00000171     7C - LOAD_FAST           'orgNum'
                             00000174     19 - BINARY_SUBSCR       
                             00000175     53 - RETURN_VALUE        
                             00000176     71 - JUMP_ABSOLUTE       -> 000001F6
                             00000179     01 - POP_TOP             
                             0000017A     7C - LOAD_FAST           'aAbility'
                             0000017D     64 - LOAD_CONST          0
                             00000180     19 - BINARY_SUBSCR       
                             00000181     7C - LOAD_FAST           'orgNum'
                             00000184     19 - BINARY_SUBSCR       
                             00000185     53 - RETURN_VALUE        
                             00000186     6E - JUMP_FORWARD        -> 000001F6
                             00000189     01 - POP_TOP             
                             0000018A     74 - LOAD_GLOBAL         'constants'
                             0000018D     69 - LOAD_ATTR           'Ability'
                             00000190     69 - LOAD_ATTR           'Event2_0Zion3Ability'
                             00000193     74 - LOAD_GLOBAL         'constants'
                             00000196     69 - LOAD_ATTR           'Ability'
                             00000199     69 - LOAD_ATTR           'Event2_0Machine3Ability'
                             0000019C     74 - LOAD_GLOBAL         'constants'
                             0000019F     69 - LOAD_ATTR           'Ability'
                             000001A2     69 - LOAD_ATTR           'Event2_0Merv3Ability'
                             000001A5     67 - BUILD_LIST          r0003
                             000001A8     74 - LOAD_GLOBAL         'constants'
                             000001AB     69 - LOAD_ATTR           'Ability'
                             000001AE     69 - LOAD_ATTR           'Event2_0Zion2Ability'
                             000001B1     74 - LOAD_GLOBAL         'constants'
                             000001B4     69 - LOAD_ATTR           'Ability'
                             000001B7     69 - LOAD_ATTR           'Event2_0Machine2Ability'
                             000001BA     74 - LOAD_GLOBAL         'constants'
                             000001BD     69 - LOAD_ATTR           'Ability'
                             000001C0     69 - LOAD_ATTR           'Event2_0Merv2Ability'
                             000001C3     67 - BUILD_LIST          r0003
                             000001C6     74 - LOAD_GLOBAL         'constants'
                             000001C9     69 - LOAD_ATTR           'Ability'
                             000001CC     69 - LOAD_ATTR           'Event2_0Zion1Ability'
                             000001CF     74 - LOAD_GLOBAL         'constants'
                             000001D2     69 - LOAD_ATTR           'Ability'
                             000001D5     69 - LOAD_ATTR           'Event2_0Machine1Ability'
                             000001D8     74 - LOAD_GLOBAL         'constants'
                             000001DB     69 - LOAD_ATTR           'Ability'
                             000001DE     69 - LOAD_ATTR           'Event2_0Merv1Ability'
                             000001E1     67 - BUILD_LIST          r0003
                             000001E4     67 - BUILD_LIST          r0003
                             000001E7     7D - STORE_FAST          'aAbility'
                             000001EA     7C - LOAD_FAST           'aAbility'
                             000001ED     7C - LOAD_FAST           'orgPlace'
                             000001F0     19 - BINARY_SUBSCR       
                             000001F1     7C - LOAD_FAST           'orgNum'
                             000001F4     19 - BINARY_SUBSCR       
                             000001F5     53 - RETURN_VALUE        
                             000001F6     64 - LOAD_CONST          None
                             000001F9     53 - RETURN_VALUE        
                         consts:
00001D49                     TUPLE: (
00001D4E                         None (4E),
00001D4F                         STR: 'Flymen - Buff Stage 1' (15 00 00 00 46 6C 79 6D 65 6E 20 2D 20 42 75 66 66 20 53 74 61 67 65 20 31),
00001D69                         STR: 'Flymen - Buff Ends' (12 00 00 00 46 6C 79 6D 65 6E 20 2D 20 42 75 66 66 20 45 6E 64 73),
00001D80                         STR: 'Flymen - Buff Stage 2' (15 00 00 00 46 6C 79 6D 65 6E 20 2D 20 42 75 66 66 20 53 74 61 67 65 20 32),
00001D9A                         INT: 1 (01 00 00 00),
00001D9F                         INT: 2 (02 00 00 00),
00001DA4                         INT: 3 (03 00 00 00),
00001DA9                         INT: 0 (00 00 00 00)
                             )
                         names:
00001DAE                     TUPLE: (
00001DB3                         STR: 'worldevent' (0A 00 00 00 77 6F 72 6C 64 65 76 65 6E 74),
00001DC2                         STR: 'None' (04 00 00 00 4E 6F 6E 65),
00001DCB                         STR: 'isEventActive' (0D 00 00 00 69 73 45 76 65 6E 74 41 63 74 69 76 65),
00001DDD                         STR: 'bIsAfterCollection' (12 00 00 00 62 49 73 41 66 74 65 72 43 6F 6C 6C 65 63 74 69 6F 6E),
00001DF4                         STR: 'getNormalizedOrgPoints' (16 00 00 00 67 65 74 4E 6F 72 6D 61 6C 69 7A 65 64 4F 72 67 50 6F 69 6E 74 73),
00001E0F                         STR: 'event' (05 00 00 00 65 76 65 6E 74),
00001E19                         STR: 'normalizedPoints' (10 00 00 00 6E 6F 72 6D 61 6C 69 7A 65 64 50 6F 69 6E 74 73),
00001E2E                         STR: 'append' (06 00 00 00 61 70 70 65 6E 64),
00001E39                         STR: '_[1]' (04 00 00 00 5F 5B 31 5D),
00001E42                         STR: 'range' (05 00 00 00 72 61 6E 67 65),
00001E4C                         STR: 'len' (03 00 00 00 6C 65 6E),
00001E54                         STR: 'i' (01 00 00 00 69),
00001E5A                         STR: 'sort' (04 00 00 00 73 6F 72 74),
00001E63                         STR: 'reverse' (07 00 00 00 72 65 76 65 72 73 65),
00001E6F                         STR: 'pair' (04 00 00 00 70 61 69 72),
00001E78                         STR: 'orgOrder' (08 00 00 00 6F 72 67 4F 72 64 65 72),
00001E85                         STR: 'min' (03 00 00 00 6D 69 6E),
00001E8D                         STR: 'index' (05 00 00 00 69 6E 64 65 78),
00001E97                         STR: 'org' (03 00 00 00 6F 72 67),
00001E9F                         STR: 'orgPlace' (08 00 00 00 6F 72 67 50 6C 61 63 65),
00001EAC                         STR: 'max' (03 00 00 00 6D 61 78),
00001EB4                         STR: 'orgNum' (06 00 00 00 6F 72 67 4E 75 6D),
00001EBF                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00001ECD                         STR: 'Ability' (07 00 00 00 41 62 69 6C 69 74 79),
00001ED9                         STR: 'Event2_0Zion2Ability' (14 00 00 00 45 76 65 6E 74 32 5F 30 5A 69 6F 6E 32 41 62 69 6C 69 74 79),
00001EF2                         STR: 'Event2_0Machine2Ability' (17 00 00 00 45 76 65 6E 74 32 5F 30 4D 61 63 68 69 6E 65 32 41 62 69 6C 69 74 79),
00001F0E                         STR: 'Event2_0Merv2Ability' (14 00 00 00 45 76 65 6E 74 32 5F 30 4D 65 72 76 32 41 62 69 6C 69 74 79),
00001F27                         STR: 'Event2_0Zion4Ability' (14 00 00 00 45 76 65 6E 74 32 5F 30 5A 69 6F 6E 34 41 62 69 6C 69 74 79),
00001F40                         STR: 'Event2_0Machine4Ability' (17 00 00 00 45 76 65 6E 74 32 5F 30 4D 61 63 68 69 6E 65 34 41 62 69 6C 69 74 79),
00001F5C                         STR: 'Event2_0Merv4Ability' (14 00 00 00 45 76 65 6E 74 32 5F 30 4D 65 72 76 34 41 62 69 6C 69 74 79),
00001F75                         STR: 'aAbility' (08 00 00 00 61 41 62 69 6C 69 74 79),
00001F82                         STR: 'Event2_0Zion3Ability' (14 00 00 00 45 76 65 6E 74 32 5F 30 5A 69 6F 6E 33 41 62 69 6C 69 74 79),
00001F9B                         STR: 'Event2_0Machine3Ability' (17 00 00 00 45 76 65 6E 74 32 5F 30 4D 61 63 68 69 6E 65 33 41 62 69 6C 69 74 79),
00001FB7                         STR: 'Event2_0Merv3Ability' (14 00 00 00 45 76 65 6E 74 32 5F 30 4D 65 72 76 33 41 62 69 6C 69 74 79),
00001FD0                         STR: 'Event2_0Zion1Ability' (14 00 00 00 45 76 65 6E 74 32 5F 30 5A 69 6F 6E 31 41 62 69 6C 69 74 79),
00001FE9                         STR: 'Event2_0Machine1Ability' (17 00 00 00 45 76 65 6E 74 32 5F 30 4D 61 63 68 69 6E 65 31 41 62 69 6C 69 74 79),
00002005                         STR: 'Event2_0Merv1Ability' (14 00 00 00 45 76 65 6E 74 32 5F 30 4D 65 72 76 31 41 62 69 6C 69 74 79)
                             )
                         varnames:
0000201E                     TUPLE: (
00002023                         STR: 'event' (05 00 00 00 65 76 65 6E 74),
0000202D                         STR: 'org' (03 00 00 00 6F 72 67),
00002035                         STR: 'bIsAfterCollection' (12 00 00 00 62 49 73 41 66 74 65 72 43 6F 6C 6C 65 63 74 69 6F 6E),
0000204C                         STR: 'i' (01 00 00 00 69),
00002052                         STR: 'normalizedPoints' (10 00 00 00 6E 6F 72 6D 61 6C 69 7A 65 64 50 6F 69 6E 74 73),
00002067                         STR: 'aAbility' (08 00 00 00 61 41 62 69 6C 69 74 79),
00002074                         STR: '_[1]' (04 00 00 00 5F 5B 31 5D),
0000207D                         STR: 'orgPlace' (08 00 00 00 6F 72 67 50 6C 61 63 65),
0000208A                         STR: 'orgNum' (06 00 00 00 6F 72 67 4E 75 6D),
00002095                         STR: 'pair' (04 00 00 00 70 61 69 72),
0000209E                         STR: 'orgOrder' (08 00 00 00 6F 72 67 4F 72 64 65 72)
                             )
                         freevars:
000020AB                     TUPLE: ()
                         cellvars:
000020B0                     TUPLE: ()
                         filename:
000020B5                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\trgs.py' (3C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 74 72 67 73 2E 70 79)
                         name:
000020F6                     STR: 'HandleEvent2Events' (12 00 00 00 48 61 6E 64 6C 65 45 76 65 6E 74 32 45 76 65 6E 74 73)
                         firslineno:
0000210D                     LONG: 216L (D8 00 00 00)
                         lnotab:
00002111                     STR: '\x00\x01\r\x01\x08\x02\x11\x01\x08\x02\x10\x01\x08\x02\x0f\x02\x0f\x02=\x02\n\x03\n\x02+\x02\x18\x02\x1c\x02\x07\x01B\x06\r\x02\x10\x03\x10\x03`\t' (2A 00 00 00 00 01 0D 01 08 02 11 01 08 02 10 01 08 02 0F 02 0F 02 3D 02 0A 03 0A 02 2B 02 18 02 1C 02 07 01 42 06 0D 02 10 03 10 03 60 09),
00002140             STR: '-- Loaded TRGS.py' (11 00 00 00 2D 2D 20 4C 6F 61 64 65 64 20 54 52 47 53 2E 70 79)
                 )
             names:
00002156         TUPLE: (
0000215B             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00002169             STR: 'RewardSelection' (0F 00 00 00 52 65 77 61 72 64 53 65 6C 65 63 74 69 6F 6E),
0000217D             STR: 'whrandom' (08 00 00 00 77 68 72 61 6E 64 6F 6D),
0000218A             STR: 'randint' (07 00 00 00 72 61 6E 64 69 6E 74),
00002196             STR: 'getopt' (06 00 00 00 67 65 74 6F 70 74),
000021A1             STR: 'exceptionCB' (0B 00 00 00 65 78 63 65 70 74 69 6F 6E 43 42),
000021B1             STR: 'ComputeHackConstructOutcome' (1B 00 00 00 43 6F 6D 70 75 74 65 48 61 63 6B 43 6F 6E 73 74 72 75 63 74 4F 75 74 63 6F 6D 65),
000021D1             STR: 'FakeGameObject' (0E 00 00 00 46 61 6B 65 47 61 6D 65 4F 62 6A 65 63 74),
000021E4             STR: 'None' (04 00 00 00 4E 6F 6E 65),
000021ED             STR: 'MakeAndEncodeReward' (13 00 00 00 4D 61 6B 65 41 6E 64 45 6E 63 6F 64 65 52 65 77 61 72 64),
00002205             STR: 'MakeRewardRoll' (0E 00 00 00 4D 61 6B 65 52 65 77 61 72 64 52 6F 6C 6C),
00002218             STR: 'GetRewardItemID' (0F 00 00 00 47 65 74 52 65 77 61 72 64 49 74 65 6D 49 44),
0000222C             STR: 'ReloadRewardSelection' (15 00 00 00 52 65 6C 6F 61 64 52 65 77 61 72 64 53 65 6C 65 63 74 69 6F 6E),
00002246             STR: 'FindMissionModule' (11 00 00 00 46 69 6E 64 4D 69 73 73 69 6F 6E 4D 6F 64 75 6C 65),
0000225C             STR: 'ParseMissionArgs' (10 00 00 00 50 61 72 73 65 4D 69 73 73 69 6F 6E 41 72 67 73),
00002271             STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
0000227F             STR: 'OrgPointType' (0C 00 00 00 4F 72 67 50 6F 69 6E 74 54 79 70 65),
00002290             STR: 'OrgPointTypeInvalid' (13 00 00 00 4F 72 67 50 6F 69 6E 74 54 79 70 65 49 6E 76 61 6C 69 64),
000022A8             STR: 'Organization' (0C 00 00 00 4F 72 67 61 6E 69 7A 61 74 69 6F 6E),
000022B9             STR: 'Invalid' (07 00 00 00 49 6E 76 61 6C 69 64),
000022C5             STR: 'HandleInvokeOrgEvent' (14 00 00 00 48 61 6E 64 6C 65 49 6E 76 6F 6B 65 4F 72 67 45 76 65 6E 74),
000022DE             STR: 'HandleNeoCorpseEvents' (15 00 00 00 48 61 6E 64 6C 65 4E 65 6F 43 6F 72 70 73 65 45 76 65 6E 74 73),
000022F8             STR: 'HandleEvent2Events' (12 00 00 00 48 61 6E 64 6C 65 45 76 65 6E 74 32 45 76 65 6E 74 73),
0000230F             STR: 'rewardselection' (0F 00 00 00 72 65 77 61 72 64 73 65 6C 65 63 74 69 6F 6E),
00002323             STR: 'Missions' (08 00 00 00 4D 69 73 73 69 6F 6E 73),
00002330             STR: 'start_msg' (09 00 00 00 73 74 61 72 74 5F 6D 73 67),
0000233E             STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
0000234C             STR: 'outputDebugString' (11 00 00 00 6F 75 74 70 75 74 44 65 62 75 67 53 74 72 69 6E 67),
00002362             STR: 'serverPrint' (0B 00 00 00 73 65 72 76 65 72 50 72 69 6E 74)
                 )
             varnames:
00002372         TUPLE: (
00002377             STR: 'FakeGameObject' (0E 00 00 00 46 61 6B 65 47 61 6D 65 4F 62 6A 65 63 74),
0000238A             STR: 'exceptionCB' (0B 00 00 00 65 78 63 65 70 74 69 6F 6E 43 42),
0000239A             STR: 'ParseMissionArgs' (10 00 00 00 50 61 72 73 65 4D 69 73 73 69 6F 6E 41 72 67 73),
000023AF             STR: 'HandleInvokeOrgEvent' (14 00 00 00 48 61 6E 64 6C 65 49 6E 76 6F 6B 65 4F 72 67 45 76 65 6E 74),
000023C8             STR: 'GetRewardItemID' (0F 00 00 00 47 65 74 52 65 77 61 72 64 49 74 65 6D 49 44),
000023DC             STR: 'randint' (07 00 00 00 72 61 6E 64 69 6E 74),
000023E8             STR: 'MakeAndEncodeReward' (13 00 00 00 4D 61 6B 65 41 6E 64 45 6E 63 6F 64 65 52 65 77 61 72 64),
00002400             STR: 'HandleNeoCorpseEvents' (15 00 00 00 48 61 6E 64 6C 65 4E 65 6F 43 6F 72 70 73 65 45 76 65 6E 74 73),
0000241A             STR: 'start_msg' (09 00 00 00 73 74 61 72 74 5F 6D 73 67),
00002428             STR: 'getopt' (06 00 00 00 67 65 74 6F 70 74),
00002433             STR: 'rewardselection' (0F 00 00 00 72 65 77 61 72 64 73 65 6C 65 63 74 69 6F 6E),
00002447             STR: 'MakeRewardRoll' (0E 00 00 00 4D 61 6B 65 52 65 77 61 72 64 52 6F 6C 6C),
0000245A             STR: 'Missions' (08 00 00 00 4D 69 73 73 69 6F 6E 73),
00002467             STR: 'HandleEvent2Events' (12 00 00 00 48 61 6E 64 6C 65 45 76 65 6E 74 32 45 76 65 6E 74 73),
0000247E             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
0000248C             STR: 'ReloadRewardSelection' (15 00 00 00 52 65 6C 6F 61 64 52 65 77 61 72 64 53 65 6C 65 63 74 69 6F 6E),
000024A6             STR: 'ComputeHackConstructOutcome' (1B 00 00 00 43 6F 6D 70 75 74 65 48 61 63 6B 43 6F 6E 73 74 72 75 63 74 4F 75 74 63 6F 6D 65),
000024C6             STR: 'FindMissionModule' (11 00 00 00 46 69 6E 64 4D 69 73 73 69 6F 6E 4D 6F 64 75 6C 65),
000024DC             STR: 'RewardSelection' (0F 00 00 00 52 65 77 61 72 64 53 65 6C 65 63 74 69 6F 6E)
                 )
             freevars:
000024F0         TUPLE: ()
             cellvars:
000024F5         TUPLE: ()
             filename:
000024FA         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\trgs.py' (3C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 74 72 67 73 2E 70 79)
             name:
0000253B         STR: '?' (01 00 00 00 3F)
             firslineno:
00002541         LONG: 8L (08 00 00 00)
             lnotab:
00002545         STR: "\t\x01\t\x01\r\x01\t\x05\t\x19\t\x14\x13\x08\x15\x05\x15\x05\t\t\t\x06\t\x14\t-'\x10\t)\t9\x0c\x01\x06\x02\x06\x02\r\x01" (28 00 00 00 09 01 09 01 0D 01 09 05 09 19 09 14 13 08 15 05 15 05 09 09 09 06 09 14 09 2D 27 10 09 29 09 39 0C 01 06 02 06 02 0D 01)

