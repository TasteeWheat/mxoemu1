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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x01\x00Z\x02\x00d\x02\x00Z\x03\x00d\x03\x00\x84\x00\x00Z\x04\x00d\x04\x00\x84\x00\x00Z\x05\x00d\x05\x00\x84\x00\x00Z\x06\x00d\x06\x00\x84\x00\x00Z\x07\x00d\x07\x00\x84\x00\x00Z\x08\x00d\x08\x00\x84\x00\x00Z\t\x00d\t\x00\x84\x00\x00Z\n\x00d\x00\x00S' (61 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 01 00 5A 02 00 64 02 00 5A 03 00 64 03 00 84 00 00 5A 04 00 64 04 00 84 00 00 5A 05 00 64 05 00 84 00 00 5A 06 00 64 06 00 84 00 00 5A 07 00 64 07 00 84 00 00 5A 08 00 64 08 00 84 00 00 5A 09 00 64 09 00 84 00 00 5A 0A 00 64 00 00 53)
                 00000000     64 - LOAD_CONST          None
                 00000003     6B - IMPORT_NAME         'random'
                 00000006     5A - STORE_NAME          'random'
                 00000009     64 - LOAD_CONST          None
                 0000000C     6B - IMPORT_NAME         'traceback'
                 0000000F     5A - STORE_NAME          'traceback'
                 00000012     64 - LOAD_CONST          0L
                 00000015     5A - STORE_NAME          'EMPTY_MISSION_KEY'
                 00000018     64 - LOAD_CONST          4294967295L
                 0000001B     5A - STORE_NAME          'NON_ASSIGNABLE_MISSIONKEY'
                 0000001E     64 - LOAD_CONST          CODE('MissionKeyBase')
                 00000021     84 - MAKE_FUNCTION       r0000
                 00000024     5A - STORE_NAME          'MissionKeyBase'
                 00000027     64 - LOAD_CONST          CODE('MissionKeyPart')
                 0000002A     84 - MAKE_FUNCTION       r0000
                 0000002D     5A - STORE_NAME          'MissionKeyPart'
                 00000030     64 - LOAD_CONST          CODE('ValidMissionKeyMatch')
                 00000033     84 - MAKE_FUNCTION       r0000
                 00000036     5A - STORE_NAME          'ValidMissionKeyMatch'
                 00000039     64 - LOAD_CONST          CODE('ValidMissionKeyBaseMatch')
                 0000003C     84 - MAKE_FUNCTION       r0000
                 0000003F     5A - STORE_NAME          'ValidMissionKeyBaseMatch'
                 00000042     64 - LOAD_CONST          CODE('IsMissionTeamMember')
                 00000045     84 - MAKE_FUNCTION       r0000
                 00000048     5A - STORE_NAME          'IsMissionTeamMember'
                 0000004B     64 - LOAD_CONST          CODE('IsPvPOpponent')
                 0000004E     84 - MAKE_FUNCTION       r0000
                 00000051     5A - STORE_NAME          'IsPvPOpponent'
                 00000054     64 - LOAD_CONST          CODE('IsNonReservedMatchingKey')
                 00000057     84 - MAKE_FUNCTION       r0000
                 0000005A     5A - STORE_NAME          'IsNonReservedMatchingKey'
                 0000005D     64 - LOAD_CONST          None
                 00000060     53 - RETURN_VALUE        
             consts:
0000007F         TUPLE: (
00000084             None (4E),
00000085             LONG: 0L (),
0000008A             LONG: 4294967295L (FF 7F FF 7F 03 00),
00000095             CODE:
                         argcount:
00000096                     LONG: 1L (01 00 00 00)
                         nlocals:
0000009A                     LONG: 1L (01 00 00 00)
                         stacksize:
0000009E                     LONG: 2L (02 00 00 00)
                         flags:
000000A2                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000000A6                     STR: '|\x00\x00d\x01\x00@d\x02\x00?Sd\x00\x00S' (10 00 00 00 7C 00 00 64 01 00 40 64 02 00 3F 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'key'
                             00000003     64 - LOAD_CONST          -256
                             00000006     40 - BINARY_AND          
                             00000007     64 - LOAD_CONST          8
                             0000000A     3F - BINARY_RSHIFT       
                             0000000B     53 - RETURN_VALUE        
                             0000000C     64 - LOAD_CONST          None
                             0000000F     53 - RETURN_VALUE        
                         consts:
000000BB                     TUPLE: (
000000C0                         None (4E),
000000C1                         INT: -256 (00 FF FF FF),
000000C6                         INT: 8 (08 00 00 00)
                             )
                         names:
000000CB                     TUPLE: (
000000D0                         STR: 'key' (03 00 00 00 6B 65 79)
                             )
                         varnames:
000000D8                     TUPLE: (
000000DD                         STR: 'key' (03 00 00 00 6B 65 79)
                             )
                         freevars:
000000E5                     TUPLE: ()
                         cellvars:
000000EA                     TUPLE: ()
                         filename:
000000EF                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\missionvalidate.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6D 69 73 73 69 6F 6E 76 61 6C 69 64 61 74 65 2E 70 79)
                         name:
0000013B                     STR: 'MissionKeyBase' (0E 00 00 00 4D 69 73 73 69 6F 6E 4B 65 79 42 61 73 65)
                         firslineno:
0000014E                     LONG: 15L (0F 00 00 00)
                         lnotab:
00000152                     STR: '\x00\x01' (02 00 00 00 00 01),
00000159             CODE:
                         argcount:
0000015A                     LONG: 1L (01 00 00 00)
                         nlocals:
0000015E                     LONG: 1L (01 00 00 00)
                         stacksize:
00000162                     LONG: 2L (02 00 00 00)
                         flags:
00000166                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000016A                     STR: '|\x00\x00d\x01\x00@Sd\x00\x00S' (0C 00 00 00 7C 00 00 64 01 00 40 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'key'
                             00000003     64 - LOAD_CONST          255
                             00000006     40 - BINARY_AND          
                             00000007     53 - RETURN_VALUE        
                             00000008     64 - LOAD_CONST          None
                             0000000B     53 - RETURN_VALUE        
                         consts:
0000017B                     TUPLE: (
00000180                         None (4E),
00000181                         INT: 255 (FF 00 00 00)
                             )
                         names:
00000186                     TUPLE: (
0000018B                         STR: 'key' (03 00 00 00 6B 65 79)
                             )
                         varnames:
00000193                     TUPLE: (
00000198                         STR: 'key' (03 00 00 00 6B 65 79)
                             )
                         freevars:
000001A0                     TUPLE: ()
                         cellvars:
000001A5                     TUPLE: ()
                         filename:
000001AA                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\missionvalidate.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6D 69 73 73 69 6F 6E 76 61 6C 69 64 61 74 65 2E 70 79)
                         name:
000001F6                     STR: 'MissionKeyPart' (0E 00 00 00 4D 69 73 73 69 6F 6E 4B 65 79 50 61 72 74)
                         firslineno:
00000209                     LONG: 18L (12 00 00 00)
                         lnotab:
0000020D                     STR: '\x00\x01' (02 00 00 00 00 01),
00000214             CODE:
                         argcount:
00000215                     LONG: 2L (02 00 00 00)
                         nlocals:
00000219                     LONG: 2L (02 00 00 00)
                         stacksize:
0000021D                     LONG: 3L (03 00 00 00)
                         flags:
00000221                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000225                     STR: '|\x00\x00\x0co\x08\x00\x01t\x01\x00Sn\x01\x00\x01|\x01\x00\x0co\x08\x00\x01t\x03\x00Sn\x01\x00\x01t\x04\x00|\x00\x00\x83\x01\x00d\x01\x00j\x03\x00o\x0e\x00\x01|\x00\x00|\x01\x00j\x02\x00Sn\x01\x00\x01t\x05\x00|\x00\x00\x83\x01\x00t\x05\x00|\x01\x00\x83\x01\x00j\x02\x00Sd\x00\x00S' (5B 00 00 00 7C 00 00 0C 6F 08 00 01 74 01 00 53 6E 01 00 01 7C 01 00 0C 6F 08 00 01 74 03 00 53 6E 01 00 01 74 04 00 7C 00 00 83 01 00 64 01 00 6A 03 00 6F 0E 00 01 7C 00 00 7C 01 00 6A 02 00 53 6E 01 00 01 74 05 00 7C 00 00 83 01 00 74 05 00 7C 01 00 83 01 00 6A 02 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'm1'
                             00000003     0C - UNARY_NOT           
                             00000004     6F - JUMP_IF_FALSE       -> 0000000F
                             00000007     01 - POP_TOP             
                             00000008     74 - LOAD_GLOBAL         'True'
                             0000000B     53 - RETURN_VALUE        
                             0000000C     6E - JUMP_FORWARD        -> 00000010
                             0000000F     01 - POP_TOP             
                             00000010     7C - LOAD_FAST           'm2'
                             00000013     0C - UNARY_NOT           
                             00000014     6F - JUMP_IF_FALSE       -> 0000001F
                             00000017     01 - POP_TOP             
                             00000018     74 - LOAD_GLOBAL         'False'
                             0000001B     53 - RETURN_VALUE        
                             0000001C     6E - JUMP_FORWARD        -> 00000020
                             0000001F     01 - POP_TOP             
                             00000020     74 - LOAD_GLOBAL         'MissionKeyPart'
                             00000023     7C - LOAD_FAST           'm1'
                             00000026     83 - CALL_FUNCTION       r0001
                             00000029     64 - LOAD_CONST          0
                             0000002C     6A - COMPARE_OP          "!="
                             0000002F     6F - JUMP_IF_FALSE       -> 00000040
                             00000032     01 - POP_TOP             
                             00000033     7C - LOAD_FAST           'm1'
                             00000036     7C - LOAD_FAST           'm2'
                             00000039     6A - COMPARE_OP          "=="
                             0000003C     53 - RETURN_VALUE        
                             0000003D     6E - JUMP_FORWARD        -> 00000041
                             00000040     01 - POP_TOP             
                             00000041     74 - LOAD_GLOBAL         'MissionKeyBase'
                             00000044     7C - LOAD_FAST           'm1'
                             00000047     83 - CALL_FUNCTION       r0001
                             0000004A     74 - LOAD_GLOBAL         'MissionKeyBase'
                             0000004D     7C - LOAD_FAST           'm2'
                             00000050     83 - CALL_FUNCTION       r0001
                             00000053     6A - COMPARE_OP          "=="
                             00000056     53 - RETURN_VALUE        
                             00000057     64 - LOAD_CONST          None
                             0000005A     53 - RETURN_VALUE        
                         consts:
00000285                     TUPLE: (
0000028A                         None (4E),
0000028B                         INT: 0 (00 00 00 00)
                             )
                         names:
00000290                     TUPLE: (
00000295                         STR: 'm1' (02 00 00 00 6D 31),
0000029C                         STR: 'True' (04 00 00 00 54 72 75 65),
000002A5                         STR: 'm2' (02 00 00 00 6D 32),
000002AC                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
000002B6                         STR: 'MissionKeyPart' (0E 00 00 00 4D 69 73 73 69 6F 6E 4B 65 79 50 61 72 74),
000002C9                         STR: 'MissionKeyBase' (0E 00 00 00 4D 69 73 73 69 6F 6E 4B 65 79 42 61 73 65)
                             )
                         varnames:
000002DC                     TUPLE: (
000002E1                         STR: 'm1' (02 00 00 00 6D 31),
000002E8                         STR: 'm2' (02 00 00 00 6D 32)
                             )
                         freevars:
000002EF                     TUPLE: ()
                         cellvars:
000002F4                     TUPLE: ()
                         filename:
000002F9                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\missionvalidate.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6D 69 73 73 69 6F 6E 76 61 6C 69 64 61 74 65 2E 70 79)
                         name:
00000345                     STR: 'ValidMissionKeyMatch' (14 00 00 00 56 61 6C 69 64 4D 69 73 73 69 6F 6E 4B 65 79 4D 61 74 63 68)
                         firslineno:
0000035E                     LONG: 27L (1B 00 00 00)
                         lnotab:
00000362                     STR: '\x00\x04\x08\x01\x08\x02\x08\x01\x08\x02\x13\x01\x0e\x02' (0E 00 00 00 00 04 08 01 08 02 08 01 08 02 13 01 0E 02),
00000375             CODE:
                         argcount:
00000376                     LONG: 2L (02 00 00 00)
                         nlocals:
0000037A                     LONG: 2L (02 00 00 00)
                         stacksize:
0000037E                     LONG: 3L (03 00 00 00)
                         flags:
00000382                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000386                     STR: '|\x00\x00\x0co\x08\x00\x01t\x01\x00Sn\x01\x00\x01|\x01\x00\x0co\x08\x00\x01t\x03\x00Sn\x01\x00\x01t\x04\x00|\x00\x00\x83\x01\x00t\x04\x00|\x01\x00\x83\x01\x00j\x02\x00Sd\x00\x00S' (3A 00 00 00 7C 00 00 0C 6F 08 00 01 74 01 00 53 6E 01 00 01 7C 01 00 0C 6F 08 00 01 74 03 00 53 6E 01 00 01 74 04 00 7C 00 00 83 01 00 74 04 00 7C 01 00 83 01 00 6A 02 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'm1'
                             00000003     0C - UNARY_NOT           
                             00000004     6F - JUMP_IF_FALSE       -> 0000000F
                             00000007     01 - POP_TOP             
                             00000008     74 - LOAD_GLOBAL         'True'
                             0000000B     53 - RETURN_VALUE        
                             0000000C     6E - JUMP_FORWARD        -> 00000010
                             0000000F     01 - POP_TOP             
                             00000010     7C - LOAD_FAST           'm2'
                             00000013     0C - UNARY_NOT           
                             00000014     6F - JUMP_IF_FALSE       -> 0000001F
                             00000017     01 - POP_TOP             
                             00000018     74 - LOAD_GLOBAL         'False'
                             0000001B     53 - RETURN_VALUE        
                             0000001C     6E - JUMP_FORWARD        -> 00000020
                             0000001F     01 - POP_TOP             
                             00000020     74 - LOAD_GLOBAL         'MissionKeyBase'
                             00000023     7C - LOAD_FAST           'm1'
                             00000026     83 - CALL_FUNCTION       r0001
                             00000029     74 - LOAD_GLOBAL         'MissionKeyBase'
                             0000002C     7C - LOAD_FAST           'm2'
                             0000002F     83 - CALL_FUNCTION       r0001
                             00000032     6A - COMPARE_OP          "=="
                             00000035     53 - RETURN_VALUE        
                             00000036     64 - LOAD_CONST          None
                             00000039     53 - RETURN_VALUE        
                         consts:
000003C5                     TUPLE: (
000003CA                         None (4E)
                             )
                         names:
000003CB                     TUPLE: (
000003D0                         STR: 'm1' (02 00 00 00 6D 31),
000003D7                         STR: 'True' (04 00 00 00 54 72 75 65),
000003E0                         STR: 'm2' (02 00 00 00 6D 32),
000003E7                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
000003F1                         STR: 'MissionKeyBase' (0E 00 00 00 4D 69 73 73 69 6F 6E 4B 65 79 42 61 73 65)
                             )
                         varnames:
00000404                     TUPLE: (
00000409                         STR: 'm1' (02 00 00 00 6D 31),
00000410                         STR: 'm2' (02 00 00 00 6D 32)
                             )
                         freevars:
00000417                     TUPLE: ()
                         cellvars:
0000041C                     TUPLE: ()
                         filename:
00000421                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\missionvalidate.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6D 69 73 73 69 6F 6E 76 61 6C 69 64 61 74 65 2E 70 79)
                         name:
0000046D                     STR: 'ValidMissionKeyBaseMatch' (18 00 00 00 56 61 6C 69 64 4D 69 73 73 69 6F 6E 4B 65 79 42 61 73 65 4D 61 74 63 68)
                         firslineno:
0000048A                     LONG: 49L (31 00 00 00)
                         lnotab:
0000048E                     STR: '\x00\x04\x08\x01\x08\x02\x08\x01\x08\x02' (0A 00 00 00 00 04 08 01 08 02 08 01 08 02),
0000049D             CODE:
                         argcount:
0000049E                     LONG: 2L (02 00 00 00)
                         nlocals:
000004A2                     LONG: 2L (02 00 00 00)
                         stacksize:
000004A6                     LONG: 2L (02 00 00 00)
                         flags:
000004AA                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000004AE                     STR: '|\x00\x00\x0cp\x05\x00\x01|\x01\x00\x0co\x08\x00\x01t\x02\x00Sn\x01\x00\x01|\x00\x00|\x01\x00j\x02\x00o\x08\x00\x01t\x03\x00Sn\x01\x00\x01t\x02\x00Sd\x00\x00S' (35 00 00 00 7C 00 00 0C 70 05 00 01 7C 01 00 0C 6F 08 00 01 74 02 00 53 6E 01 00 01 7C 00 00 7C 01 00 6A 02 00 6F 08 00 01 74 03 00 53 6E 01 00 01 74 02 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'missionKey1'
                             00000003     0C - UNARY_NOT           
                             00000004     70 - JUMP_IF_TRUE        -> 0000000C
                             00000007     01 - POP_TOP             
                             00000008     7C - LOAD_FAST           'missionKey2'
                             0000000B     0C - UNARY_NOT           
                             0000000C     6F - JUMP_IF_FALSE       -> 00000017
                             0000000F     01 - POP_TOP             
                             00000010     74 - LOAD_GLOBAL         'False'
                             00000013     53 - RETURN_VALUE        
                             00000014     6E - JUMP_FORWARD        -> 00000018
                             00000017     01 - POP_TOP             
                             00000018     7C - LOAD_FAST           'missionKey1'
                             0000001B     7C - LOAD_FAST           'missionKey2'
                             0000001E     6A - COMPARE_OP          "=="
                             00000021     6F - JUMP_IF_FALSE       -> 0000002C
                             00000024     01 - POP_TOP             
                             00000025     74 - LOAD_GLOBAL         'True'
                             00000028     53 - RETURN_VALUE        
                             00000029     6E - JUMP_FORWARD        -> 0000002D
                             0000002C     01 - POP_TOP             
                             0000002D     74 - LOAD_GLOBAL         'False'
                             00000030     53 - RETURN_VALUE        
                             00000031     64 - LOAD_CONST          None
                             00000034     53 - RETURN_VALUE        
                         consts:
000004E8                     TUPLE: (
000004ED                         None (4E)
                             )
                         names:
000004EE                     TUPLE: (
000004F3                         STR: 'missionKey1' (0B 00 00 00 6D 69 73 73 69 6F 6E 4B 65 79 31),
00000503                         STR: 'missionKey2' (0B 00 00 00 6D 69 73 73 69 6F 6E 4B 65 79 32),
00000513                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
0000051D                         STR: 'True' (04 00 00 00 54 72 75 65)
                             )
                         varnames:
00000526                     TUPLE: (
0000052B                         STR: 'missionKey1' (0B 00 00 00 6D 69 73 73 69 6F 6E 4B 65 79 31),
0000053B                         STR: 'missionKey2' (0B 00 00 00 6D 69 73 73 69 6F 6E 4B 65 79 32)
                             )
                         freevars:
0000054B                     TUPLE: ()
                         cellvars:
00000550                     TUPLE: ()
                         filename:
00000555                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\missionvalidate.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6D 69 73 73 69 6F 6E 76 61 6C 69 64 61 74 65 2E 70 79)
                         name:
000005A1                     STR: 'IsMissionTeamMember' (13 00 00 00 49 73 4D 69 73 73 69 6F 6E 54 65 61 6D 4D 65 6D 62 65 72)
                         firslineno:
000005B9                     LONG: 64L (40 00 00 00)
                         lnotab:
000005BD                     STR: '\x00\x02\x10\x01\x08\x03\r\x01\x08\x02' (0A 00 00 00 00 02 10 01 08 03 0D 01 08 02),
000005CC             CODE:
                         argcount:
000005CD                     LONG: 2L (02 00 00 00)
                         nlocals:
000005D1                     LONG: 2L (02 00 00 00)
                         stacksize:
000005D5                     LONG: 3L (03 00 00 00)
                         flags:
000005D9                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000005DD                     STR: '|\x00\x00\x0cp\x05\x00\x01|\x01\x00\x0co\x08\x00\x01t\x02\x00Sn\x01\x00\x01t\x03\x00|\x00\x00\x83\x01\x00t\x03\x00|\x01\x00\x83\x01\x00j\x02\x00o\x16\x00\x01t\x04\x00|\x00\x00\x83\x01\x00t\x04\x00|\x01\x00\x83\x01\x00j\x03\x00o\x08\x00\x01t\x05\x00Sn\x01\x00\x01t\x02\x00Sd\x00\x00S' (5A 00 00 00 7C 00 00 0C 70 05 00 01 7C 01 00 0C 6F 08 00 01 74 02 00 53 6E 01 00 01 74 03 00 7C 00 00 83 01 00 74 03 00 7C 01 00 83 01 00 6A 02 00 6F 16 00 01 74 04 00 7C 00 00 83 01 00 74 04 00 7C 01 00 83 01 00 6A 03 00 6F 08 00 01 74 05 00 53 6E 01 00 01 74 02 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'missionKey1'
                             00000003     0C - UNARY_NOT           
                             00000004     70 - JUMP_IF_TRUE        -> 0000000C
                             00000007     01 - POP_TOP             
                             00000008     7C - LOAD_FAST           'missionKey2'
                             0000000B     0C - UNARY_NOT           
                             0000000C     6F - JUMP_IF_FALSE       -> 00000017
                             0000000F     01 - POP_TOP             
                             00000010     74 - LOAD_GLOBAL         'False'
                             00000013     53 - RETURN_VALUE        
                             00000014     6E - JUMP_FORWARD        -> 00000018
                             00000017     01 - POP_TOP             
                             00000018     74 - LOAD_GLOBAL         'MissionKeyBase'
                             0000001B     7C - LOAD_FAST           'missionKey1'
                             0000001E     83 - CALL_FUNCTION       r0001
                             00000021     74 - LOAD_GLOBAL         'MissionKeyBase'
                             00000024     7C - LOAD_FAST           'missionKey2'
                             00000027     83 - CALL_FUNCTION       r0001
                             0000002A     6A - COMPARE_OP          "=="
                             0000002D     6F - JUMP_IF_FALSE       -> 00000046
                             00000030     01 - POP_TOP             
                             00000031     74 - LOAD_GLOBAL         'MissionKeyPart'
                             00000034     7C - LOAD_FAST           'missionKey1'
                             00000037     83 - CALL_FUNCTION       r0001
                             0000003A     74 - LOAD_GLOBAL         'MissionKeyPart'
                             0000003D     7C - LOAD_FAST           'missionKey2'
                             00000040     83 - CALL_FUNCTION       r0001
                             00000043     6A - COMPARE_OP          "!="
                             00000046     6F - JUMP_IF_FALSE       -> 00000051
                             00000049     01 - POP_TOP             
                             0000004A     74 - LOAD_GLOBAL         'True'
                             0000004D     53 - RETURN_VALUE        
                             0000004E     6E - JUMP_FORWARD        -> 00000052
                             00000051     01 - POP_TOP             
                             00000052     74 - LOAD_GLOBAL         'False'
                             00000055     53 - RETURN_VALUE        
                             00000056     64 - LOAD_CONST          None
                             00000059     53 - RETURN_VALUE        
                         consts:
0000063C                     TUPLE: (
00000641                         None (4E)
                             )
                         names:
00000642                     TUPLE: (
00000647                         STR: 'missionKey1' (0B 00 00 00 6D 69 73 73 69 6F 6E 4B 65 79 31),
00000657                         STR: 'missionKey2' (0B 00 00 00 6D 69 73 73 69 6F 6E 4B 65 79 32),
00000667                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
00000671                         STR: 'MissionKeyBase' (0E 00 00 00 4D 69 73 73 69 6F 6E 4B 65 79 42 61 73 65),
00000684                         STR: 'MissionKeyPart' (0E 00 00 00 4D 69 73 73 69 6F 6E 4B 65 79 50 61 72 74),
00000697                         STR: 'True' (04 00 00 00 54 72 75 65)
                             )
                         varnames:
000006A0                     TUPLE: (
000006A5                         STR: 'missionKey1' (0B 00 00 00 6D 69 73 73 69 6F 6E 4B 65 79 31),
000006B5                         STR: 'missionKey2' (0B 00 00 00 6D 69 73 73 69 6F 6E 4B 65 79 32)
                             )
                         freevars:
000006C5                     TUPLE: ()
                         cellvars:
000006CA                     TUPLE: ()
                         filename:
000006CF                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\missionvalidate.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6D 69 73 73 69 6F 6E 76 61 6C 69 64 61 74 65 2E 70 79)
                         name:
0000071B                     STR: 'IsPvPOpponent' (0D 00 00 00 49 73 50 76 50 4F 70 70 6F 6E 65 6E 74)
                         firslineno:
0000072D                     LONG: 78L (4E 00 00 00)
                         lnotab:
00000731                     STR: '\x00\x02\x10\x01\x08\x032\x01\x08\x02' (0A 00 00 00 00 02 10 01 08 03 32 01 08 02),
00000740             CODE:
                         argcount:
00000741                     LONG: 2L (02 00 00 00)
                         nlocals:
00000745                     LONG: 2L (02 00 00 00)
                         stacksize:
00000749                     LONG: 3L (03 00 00 00)
                         flags:
0000074D                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000751                     STR: '|\x00\x00\x0co\x08\x00\x01t\x01\x00Sn\x01\x00\x01|\x01\x00\x0co\x08\x00\x01t\x01\x00Sn\x01\x00\x01t\x03\x00|\x00\x00|\x01\x00\x83\x02\x00\x0co\x08\x00\x01t\x01\x00Sn\x01\x00\x01t\x04\x00|\x00\x00\x83\x01\x00d\x01\x00j\x02\x00o\x08\x00\x01t\x01\x00Sn\x01\x00\x01t\x04\x00|\x01\x00\x83\x01\x00d\x01\x00j\x02\x00o\x08\x00\x01t\x01\x00Sn\x01\x00\x01t\x05\x00Sd\x00\x00S' (77 00 00 00 7C 00 00 0C 6F 08 00 01 74 01 00 53 6E 01 00 01 7C 01 00 0C 6F 08 00 01 74 01 00 53 6E 01 00 01 74 03 00 7C 00 00 7C 01 00 83 02 00 0C 6F 08 00 01 74 01 00 53 6E 01 00 01 74 04 00 7C 00 00 83 01 00 64 01 00 6A 02 00 6F 08 00 01 74 01 00 53 6E 01 00 01 74 04 00 7C 01 00 83 01 00 64 01 00 6A 02 00 6F 08 00 01 74 01 00 53 6E 01 00 01 74 05 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'missionKey1'
                             00000003     0C - UNARY_NOT           
                             00000004     6F - JUMP_IF_FALSE       -> 0000000F
                             00000007     01 - POP_TOP             
                             00000008     74 - LOAD_GLOBAL         'False'
                             0000000B     53 - RETURN_VALUE        
                             0000000C     6E - JUMP_FORWARD        -> 00000010
                             0000000F     01 - POP_TOP             
                             00000010     7C - LOAD_FAST           'missionKey2'
                             00000013     0C - UNARY_NOT           
                             00000014     6F - JUMP_IF_FALSE       -> 0000001F
                             00000017     01 - POP_TOP             
                             00000018     74 - LOAD_GLOBAL         'False'
                             0000001B     53 - RETURN_VALUE        
                             0000001C     6E - JUMP_FORWARD        -> 00000020
                             0000001F     01 - POP_TOP             
                             00000020     74 - LOAD_GLOBAL         'ValidMissionKeyBaseMatch'
                             00000023     7C - LOAD_FAST           'missionKey1'
                             00000026     7C - LOAD_FAST           'missionKey2'
                             00000029     83 - CALL_FUNCTION       r0002
                             0000002C     0C - UNARY_NOT           
                             0000002D     6F - JUMP_IF_FALSE       -> 00000038
                             00000030     01 - POP_TOP             
                             00000031     74 - LOAD_GLOBAL         'False'
                             00000034     53 - RETURN_VALUE        
                             00000035     6E - JUMP_FORWARD        -> 00000039
                             00000038     01 - POP_TOP             
                             00000039     74 - LOAD_GLOBAL         'MissionKeyPart'
                             0000003C     7C - LOAD_FAST           'missionKey1'
                             0000003F     83 - CALL_FUNCTION       r0001
                             00000042     64 - LOAD_CONST          255
                             00000045     6A - COMPARE_OP          "=="
                             00000048     6F - JUMP_IF_FALSE       -> 00000053
                             0000004B     01 - POP_TOP             
                             0000004C     74 - LOAD_GLOBAL         'False'
                             0000004F     53 - RETURN_VALUE        
                             00000050     6E - JUMP_FORWARD        -> 00000054
                             00000053     01 - POP_TOP             
                             00000054     74 - LOAD_GLOBAL         'MissionKeyPart'
                             00000057     7C - LOAD_FAST           'missionKey2'
                             0000005A     83 - CALL_FUNCTION       r0001
                             0000005D     64 - LOAD_CONST          255
                             00000060     6A - COMPARE_OP          "=="
                             00000063     6F - JUMP_IF_FALSE       -> 0000006E
                             00000066     01 - POP_TOP             
                             00000067     74 - LOAD_GLOBAL         'False'
                             0000006A     53 - RETURN_VALUE        
                             0000006B     6E - JUMP_FORWARD        -> 0000006F
                             0000006E     01 - POP_TOP             
                             0000006F     74 - LOAD_GLOBAL         'True'
                             00000072     53 - RETURN_VALUE        
                             00000073     64 - LOAD_CONST          None
                             00000076     53 - RETURN_VALUE        
                         consts:
000007CD                     TUPLE: (
000007D2                         None (4E),
000007D3                         INT: 255 (FF 00 00 00)
                             )
                         names:
000007D8                     TUPLE: (
000007DD                         STR: 'missionKey1' (0B 00 00 00 6D 69 73 73 69 6F 6E 4B 65 79 31),
000007ED                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
000007F7                         STR: 'missionKey2' (0B 00 00 00 6D 69 73 73 69 6F 6E 4B 65 79 32),
00000807                         STR: 'ValidMissionKeyBaseMatch' (18 00 00 00 56 61 6C 69 64 4D 69 73 73 69 6F 6E 4B 65 79 42 61 73 65 4D 61 74 63 68),
00000824                         STR: 'MissionKeyPart' (0E 00 00 00 4D 69 73 73 69 6F 6E 4B 65 79 50 61 72 74),
00000837                         STR: 'True' (04 00 00 00 54 72 75 65)
                             )
                         varnames:
00000840                     TUPLE: (
00000845                         STR: 'missionKey1' (0B 00 00 00 6D 69 73 73 69 6F 6E 4B 65 79 31),
00000855                         STR: 'missionKey2' (0B 00 00 00 6D 69 73 73 69 6F 6E 4B 65 79 32)
                             )
                         freevars:
00000865                     TUPLE: ()
                         cellvars:
0000086A                     TUPLE: ()
                         filename:
0000086F                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\missionvalidate.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6D 69 73 73 69 6F 6E 76 61 6C 69 64 61 74 65 2E 70 79)
                         name:
000008BB                     STR: 'IsNonReservedMatchingKey' (18 00 00 00 49 73 4E 6F 6E 52 65 73 65 72 76 65 64 4D 61 74 63 68 69 6E 67 4B 65 79)
                         firslineno:
000008D8                     LONG: 92L (5C 00 00 00)
                         lnotab:
000008DC                     STR: '\x00\x03\x08\x01\x08\x02\x08\x01\x08\x03\x11\x01\x08\x03\x13\x01\x08\x02\x13\x01\x08\x02' (16 00 00 00 00 03 08 01 08 02 08 01 08 03 11 01 08 03 13 01 08 02 13 01 08 02)
                 )
             names:
000008F7         TUPLE: (
000008FC             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00000907             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00000915             STR: 'EMPTY_MISSION_KEY' (11 00 00 00 45 4D 50 54 59 5F 4D 49 53 53 49 4F 4E 5F 4B 45 59),
0000092B             STR: 'NON_ASSIGNABLE_MISSIONKEY' (19 00 00 00 4E 4F 4E 5F 41 53 53 49 47 4E 41 42 4C 45 5F 4D 49 53 53 49 4F 4E 4B 45 59),
00000949             STR: 'MissionKeyBase' (0E 00 00 00 4D 69 73 73 69 6F 6E 4B 65 79 42 61 73 65),
0000095C             STR: 'MissionKeyPart' (0E 00 00 00 4D 69 73 73 69 6F 6E 4B 65 79 50 61 72 74),
0000096F             STR: 'ValidMissionKeyMatch' (14 00 00 00 56 61 6C 69 64 4D 69 73 73 69 6F 6E 4B 65 79 4D 61 74 63 68),
00000988             STR: 'ValidMissionKeyBaseMatch' (18 00 00 00 56 61 6C 69 64 4D 69 73 73 69 6F 6E 4B 65 79 42 61 73 65 4D 61 74 63 68),
000009A5             STR: 'IsMissionTeamMember' (13 00 00 00 49 73 4D 69 73 73 69 6F 6E 54 65 61 6D 4D 65 6D 62 65 72),
000009BD             STR: 'IsPvPOpponent' (0D 00 00 00 49 73 50 76 50 4F 70 70 6F 6E 65 6E 74),
000009CF             STR: 'IsNonReservedMatchingKey' (18 00 00 00 49 73 4E 6F 6E 52 65 73 65 72 76 65 64 4D 61 74 63 68 69 6E 67 4B 65 79)
                 )
             varnames:
000009EC         TUPLE: (
000009F1             STR: 'EMPTY_MISSION_KEY' (11 00 00 00 45 4D 50 54 59 5F 4D 49 53 53 49 4F 4E 5F 4B 45 59),
00000A07             STR: 'MissionKeyPart' (0E 00 00 00 4D 69 73 73 69 6F 6E 4B 65 79 50 61 72 74),
00000A1A             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00000A28             STR: 'MissionKeyBase' (0E 00 00 00 4D 69 73 73 69 6F 6E 4B 65 79 42 61 73 65),
00000A3B             STR: 'IsNonReservedMatchingKey' (18 00 00 00 49 73 4E 6F 6E 52 65 73 65 72 76 65 64 4D 61 74 63 68 69 6E 67 4B 65 79),
00000A58             STR: 'IsPvPOpponent' (0D 00 00 00 49 73 50 76 50 4F 70 70 6F 6E 65 6E 74),
00000A6A             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00000A75             STR: 'NON_ASSIGNABLE_MISSIONKEY' (19 00 00 00 4E 4F 4E 5F 41 53 53 49 47 4E 41 42 4C 45 5F 4D 49 53 53 49 4F 4E 4B 45 59),
00000A93             STR: 'ValidMissionKeyBaseMatch' (18 00 00 00 56 61 6C 69 64 4D 69 73 73 69 6F 6E 4B 65 79 42 61 73 65 4D 61 74 63 68),
00000AB0             STR: 'ValidMissionKeyMatch' (14 00 00 00 56 61 6C 69 64 4D 69 73 73 69 6F 6E 4B 65 79 4D 61 74 63 68),
00000AC9             STR: 'IsMissionTeamMember' (13 00 00 00 49 73 4D 69 73 73 69 6F 6E 54 65 61 6D 4D 65 6D 62 65 72)
                 )
             freevars:
00000AE1         TUPLE: ()
             cellvars:
00000AE6         TUPLE: ()
             filename:
00000AEB         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\missionvalidate.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6D 69 73 73 69 6F 6E 76 61 6C 69 64 61 74 65 2E 70 79)
             name:
00000B37         STR: '?' (01 00 00 00 3F)
             firslineno:
00000B3D         LONG: 3L (03 00 00 00)
             lnotab:
00000B41         STR: '\t\x01\t\x08\x06\x01\x06\x02\t\x03\t\t\t\x16\t\x0f\t\x0e\t\x0e' (14 00 00 00 09 01 09 08 06 01 06 02 09 03 09 09 09 16 09 0F 09 0E 09 0E)

