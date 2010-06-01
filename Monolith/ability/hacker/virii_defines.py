--== Disasm ==--
00000008 CODE:
             argcount:
00000009         LONG: 0L (00 00 00 00)
             nlocals:
0000000D         LONG: 0L (00 00 00 00)
             stacksize:
00000011         LONG: 3L (03 00 00 00)
             flags:
00000015         LONG: 64L (40 00 00 00)
                 (NOFREE)
             code:
00000019         STR: 'd\x00\x00k\x00\x00i\x01\x00Z\x02\x00d\x00\x00k\x03\x00Z\x03\x00d\x00\x00k\x04\x00Z\x04\x00d\x01\x00k\x05\x00Td\x00\x00k\x06\x00Z\x07\x00d\x02\x00Z\x08\x00d\x03\x00Z\t\x00d\x04\x00Z\n\x00e\n\x00Z\x0b\x00d\x05\x00Z\x0c\x00d\x06\x00Z\r\x00d\x07\x00Z\x0e\x00d\x08\x00Z\x0f\x00d\t\x00Z\x10\x00d\n\x00Z\x11\x00d\x0b\x00Z\x12\x00d\x0b\x00Z\x13\x00d\x0b\x00Z\x14\x00e\x15\x00f\x00\x00d\x0c\x00\x84\x02\x00Z\x16\x00e\x17\x00d\r\x00\x84\x01\x00Z\x18\x00d\x0e\x00\x84\x00\x00Z\x19\x00d\x0f\x00\x84\x00\x00Z\x1a\x00d\x10\x00\x84\x00\x00Z\x1b\x00d\x11\x00\x84\x00\x00Z\x1c\x00d\x12\x00\x84\x00\x00Z\x1d\x00d\x13\x00\x84\x00\x00Z\x1e\x00d\x14\x00\x84\x00\x00Z\x1f\x00d\x15\x00\x84\x00\x00Z \x00e\x15\x00d\x16\x00\x84\x01\x00Z!\x00d\x17\x00\x84\x00\x00Z"\x00d\x00\x00S' (F8 00 00 00 64 00 00 6B 00 00 69 01 00 5A 02 00 64 00 00 6B 03 00 5A 03 00 64 00 00 6B 04 00 5A 04 00 64 01 00 6B 05 00 54 64 00 00 6B 06 00 5A 07 00 64 02 00 5A 08 00 64 03 00 5A 09 00 64 04 00 5A 0A 00 65 0A 00 5A 0B 00 64 05 00 5A 0C 00 64 06 00 5A 0D 00 64 07 00 5A 0E 00 64 08 00 5A 0F 00 64 09 00 5A 10 00 64 0A 00 5A 11 00 64 0B 00 5A 12 00 64 0B 00 5A 13 00 64 0B 00 5A 14 00 65 15 00 66 00 00 64 0C 00 84 02 00 5A 16 00 65 17 00 64 0D 00 84 01 00 5A 18 00 64 0E 00 84 00 00 5A 19 00 64 0F 00 84 00 00 5A 1A 00 64 10 00 84 00 00 5A 1B 00 64 11 00 84 00 00 5A 1C 00 64 12 00 84 00 00 5A 1D 00 64 13 00 84 00 00 5A 1E 00 64 14 00 84 00 00 5A 1F 00 64 15 00 84 00 00 5A 20 00 65 15 00 64 16 00 84 01 00 5A 21 00 64 17 00 84 00 00 5A 22 00 64 00 00 53)
                 00000000     64 - LOAD_CONST          None
                 00000003     6B - IMPORT_NAME         'ability.utility'
                 00000006     69 - LOAD_ATTR           'utility'
                 00000009     5A - STORE_NAME          'Utility'
                 0000000C     64 - LOAD_CONST          None
                 0000000F     6B - IMPORT_NAME         'random'
                 00000012     5A - STORE_NAME          'random'
                 00000015     64 - LOAD_CONST          None
                 00000018     6B - IMPORT_NAME         'traceback'
                 0000001B     5A - STORE_NAME          'traceback'
                 0000001E     64 - LOAD_CONST          ('*')
                 00000021     6B - IMPORT_NAME         'ability.defines'
                 00000024     54 - IMPORT_STAR         
                 00000025     64 - LOAD_CONST          None
                 00000028     6B - IMPORT_NAME         'stringtable_client'
                 0000002B     5A - STORE_NAME          'StringTable'
                 0000002E     64 - LOAD_CONST          10.0
                 00000031     5A - STORE_NAME          'VIRII_LEVEL_1_DURATION'
                 00000034     64 - LOAD_CONST          15.0
                 00000037     5A - STORE_NAME          'VIRII_LEVEL_2_DURATION'
                 0000003A     64 - LOAD_CONST          25.0
                 0000003D     5A - STORE_NAME          'VIRII_LEVEL_3_DURATION'
                 00000040     65 - LOAD_NAME           'VIRII_LEVEL_3_DURATION'
                 00000043     5A - STORE_NAME          'VIRII_MULTI_DURATION'
                 00000046     64 - LOAD_CONST          -10
                 00000049     5A - STORE_NAME          'VIRII_LEVEL_1_DEBUFF'
                 0000004C     64 - LOAD_CONST          -20
                 0000004F     5A - STORE_NAME          'VIRII_LEVEL_2_DEBUFF'
                 00000052     64 - LOAD_CONST          -30
                 00000055     5A - STORE_NAME          'VIRII_LEVEL_3_DEBUFF'
                 00000058     64 - LOAD_CONST          10
                 0000005B     5A - STORE_NAME          'VIRII_LEVEL_1_BUFF'
                 0000005E     64 - LOAD_CONST          20
                 00000061     5A - STORE_NAME          'VIRII_LEVEL_2_BUFF'
                 00000064     64 - LOAD_CONST          30
                 00000067     5A - STORE_NAME          'VIRII_LEVEL_3_BUFF'
                 0000006A     64 - LOAD_CONST          5000.0
                 0000006D     5A - STORE_NAME          'VIRII_LEVEL_1_RANGE'
                 00000070     64 - LOAD_CONST          5000.0
                 00000073     5A - STORE_NAME          'VIRII_LEVEL_2_RANGE'
                 00000076     64 - LOAD_CONST          5000.0
                 00000079     5A - STORE_NAME          'VIRII_LEVEL_3_RANGE'
                 0000007C     65 - LOAD_NAME           'True'
                 0000007F     66 - BUILD_TUPLE         r0000
                 00000082     64 - LOAD_CONST          CODE('SendVirusResultToAll')
                 00000085     84 - MAKE_FUNCTION       r0002
                 00000088     5A - STORE_NAME          'SendVirusResultToAll'
                 0000008B     65 - LOAD_NAME           'False'
                 0000008E     64 - LOAD_CONST          CODE('VirusSuccessCheck')
                 00000091     84 - MAKE_FUNCTION       r0001
                 00000094     5A - STORE_NAME          'VirusSuccessCheck'
                 00000097     64 - LOAD_CONST          CODE('ProgramLauncherCheck')
                 0000009A     84 - MAKE_FUNCTION       r0000
                 0000009D     5A - STORE_NAME          'ProgramLauncherCheck'
                 000000A0     64 - LOAD_CONST          CODE('VaccinationCheck')
                 000000A3     84 - MAKE_FUNCTION       r0000
                 000000A6     5A - STORE_NAME          'VaccinationCheck'
                 000000A9     64 - LOAD_CONST          CODE('ReflectionCheck')
                 000000AC     84 - MAKE_FUNCTION       r0000
                 000000AF     5A - STORE_NAME          'ReflectionCheck'
                 000000B2     64 - LOAD_CONST          CODE('CalcDifficultyValue')
                 000000B5     84 - MAKE_FUNCTION       r0000
                 000000B8     5A - STORE_NAME          'CalcDifficultyValue'
                 000000BB     64 - LOAD_CONST          CODE('CalcSuccessRating')
                 000000BE     84 - MAKE_FUNCTION       r0000
                 000000C1     5A - STORE_NAME          'CalcSuccessRating'
                 000000C4     64 - LOAD_CONST          CODE('SingleSuccessRating')
                 000000C7     84 - MAKE_FUNCTION       r0000
                 000000CA     5A - STORE_NAME          'SingleSuccessRating'
                 000000CD     64 - LOAD_CONST          CODE('MultiSuccessRating')
                 000000D0     84 - MAKE_FUNCTION       r0000
                 000000D3     5A - STORE_NAME          'MultiSuccessRating'
                 000000D6     64 - LOAD_CONST          CODE('DifficultyCheck')
                 000000D9     84 - MAKE_FUNCTION       r0000
                 000000DC     5A - STORE_NAME          'DifficultyCheck'
                 000000DF     65 - LOAD_NAME           'True'
                 000000E2     64 - LOAD_CONST          CODE('MultiDifficultyCheck')
                 000000E5     84 - MAKE_FUNCTION       r0001
                 000000E8     5A - STORE_NAME          'MultiDifficultyCheck'
                 000000EB     64 - LOAD_CONST          CODE('MultVirusSuccessCheck')
                 000000EE     84 - MAKE_FUNCTION       r0000
                 000000F1     5A - STORE_NAME          'MultVirusSuccessCheck'
                 000000F4     64 - LOAD_CONST          None
                 000000F7     53 - RETURN_VALUE        
             consts:
00000116         TUPLE: (
0000011B             None (4E),
0000011C             TUPLE: (
00000121                 STR: '*' (01 00 00 00 2A)
                     ),
00000127             FLOAT: 10.0 (04 31 30 2E 30),
0000012D             FLOAT: 15.0 (04 31 35 2E 30),
00000133             FLOAT: 25.0 (04 32 35 2E 30),
00000139             INT: -10 (F6 FF FF FF),
0000013E             INT: -20 (EC FF FF FF),
00000143             INT: -30 (E2 FF FF FF),
00000148             INT: 10 (0A 00 00 00),
0000014D             INT: 20 (14 00 00 00),
00000152             INT: 30 (1E 00 00 00),
00000157             FLOAT: 5000.0 (06 35 30 30 30 2E 30),
0000015F             CODE:
                         argcount:
00000160                     LONG: 6L (06 00 00 00)
                         nlocals:
00000164                     LONG: 6L (06 00 00 00)
                         stacksize:
00000168                     LONG: 6L (06 00 00 00)
                         flags:
0000016C                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000170                     STR: '|\x04\x00t\x01\x00j\x02\x00o\x08\x00\x01d\x00\x00Sn\x01\x00\x01|\x00\x00t\x03\x00j\x02\x00o \x00\x01t\x04\x00i\x05\x00t\x06\x00i\x07\x00|\x01\x00|\x02\x00|\x03\x00|\x05\x00\x83\x05\x00\x01n[\x00\x01|\x00\x00t\x0c\x00j\x02\x00o \x00\x01t\x04\x00i\x05\x00t\x06\x00i\r\x00|\x01\x00|\x02\x00|\x03\x00|\x05\x00\x83\x05\x00\x01n.\x00\x01|\x00\x00t\x0e\x00j\x02\x00o \x00\x01t\x04\x00i\x05\x00t\x06\x00i\x0f\x00|\x01\x00|\x02\x00|\x03\x00|\x05\x00\x83\x05\x00\x01n\x01\x00\x01d\x00\x00S' (A0 00 00 00 7C 04 00 74 01 00 6A 02 00 6F 08 00 01 64 00 00 53 6E 01 00 01 7C 00 00 74 03 00 6A 02 00 6F 20 00 01 74 04 00 69 05 00 74 06 00 69 07 00 7C 01 00 7C 02 00 7C 03 00 7C 05 00 83 05 00 01 6E 5B 00 01 7C 00 00 74 0C 00 6A 02 00 6F 20 00 01 74 04 00 69 05 00 74 06 00 69 0D 00 7C 01 00 7C 02 00 7C 03 00 7C 05 00 83 05 00 01 6E 2E 00 01 7C 00 00 74 0E 00 6A 02 00 6F 20 00 01 74 04 00 69 05 00 74 06 00 69 0F 00 7C 01 00 7C 02 00 7C 03 00 7C 05 00 83 05 00 01 6E 01 00 01 64 00 00 53)
                             00000000     7C - LOAD_FAST           'send_message'
                             00000003     74 - LOAD_GLOBAL         'False'
                             00000006     6A - COMPARE_OP          "=="
                             00000009     6F - JUMP_IF_FALSE       -> 00000014
                             0000000C     01 - POP_TOP             
                             0000000D     64 - LOAD_CONST          None
                             00000010     53 - RETURN_VALUE        
                             00000011     6E - JUMP_FORWARD        -> 00000015
                             00000014     01 - POP_TOP             
                             00000015     7C - LOAD_FAST           'result'
                             00000018     74 - LOAD_GLOBAL         'SUCCESS'
                             0000001B     6A - COMPARE_OP          "=="
                             0000001E     6F - JUMP_IF_FALSE       -> 00000041
                             00000021     01 - POP_TOP             
                             00000022     74 - LOAD_GLOBAL         'Utility'
                             00000025     69 - LOAD_ATTR           'SendAbilityOutputToAll'
                             00000028     74 - LOAD_GLOBAL         'StringTable'
                             0000002B     69 - LOAD_ATTR           'ID_CLIENT_ABILITY_VIRUS_HIT'
                             0000002E     7C - LOAD_FAST           'virus'
                             00000031     7C - LOAD_FAST           'subject'
                             00000034     7C - LOAD_FAST           'directobject'
                             00000037     7C - LOAD_FAST           'exValues'
                             0000003A     83 - CALL_FUNCTION       r0005
                             0000003D     01 - POP_TOP             
                             0000003E     6E - JUMP_FORWARD        -> 0000009C
                             00000041     01 - POP_TOP             
                             00000042     7C - LOAD_FAST           'result'
                             00000045     74 - LOAD_GLOBAL         'DEFLECTED'
                             00000048     6A - COMPARE_OP          "=="
                             0000004B     6F - JUMP_IF_FALSE       -> 0000006E
                             0000004E     01 - POP_TOP             
                             0000004F     74 - LOAD_GLOBAL         'Utility'
                             00000052     69 - LOAD_ATTR           'SendAbilityOutputToAll'
                             00000055     74 - LOAD_GLOBAL         'StringTable'
                             00000058     69 - LOAD_ATTR           'ID_CLIENT_ABILITY_VIRUS_DEFLECTED'
                             0000005B     7C - LOAD_FAST           'virus'
                             0000005E     7C - LOAD_FAST           'subject'
                             00000061     7C - LOAD_FAST           'directobject'
                             00000064     7C - LOAD_FAST           'exValues'
                             00000067     83 - CALL_FUNCTION       r0005
                             0000006A     01 - POP_TOP             
                             0000006B     6E - JUMP_FORWARD        -> 0000009C
                             0000006E     01 - POP_TOP             
                             0000006F     7C - LOAD_FAST           'result'
                             00000072     74 - LOAD_GLOBAL         'REFLECTED'
                             00000075     6A - COMPARE_OP          "=="
                             00000078     6F - JUMP_IF_FALSE       -> 0000009B
                             0000007B     01 - POP_TOP             
                             0000007C     74 - LOAD_GLOBAL         'Utility'
                             0000007F     69 - LOAD_ATTR           'SendAbilityOutputToAll'
                             00000082     74 - LOAD_GLOBAL         'StringTable'
                             00000085     69 - LOAD_ATTR           'ID_CLIENT_ABILITY_VIRUS_REFLECTED'
                             00000088     7C - LOAD_FAST           'virus'
                             0000008B     7C - LOAD_FAST           'subject'
                             0000008E     7C - LOAD_FAST           'directobject'
                             00000091     7C - LOAD_FAST           'exValues'
                             00000094     83 - CALL_FUNCTION       r0005
                             00000097     01 - POP_TOP             
                             00000098     6E - JUMP_FORWARD        -> 0000009C
                             0000009B     01 - POP_TOP             
                             0000009C     64 - LOAD_CONST          None
                             0000009F     53 - RETURN_VALUE        
                         consts:
00000215                     TUPLE: (
0000021A                         None (4E)
                             )
                         names:
0000021B                     TUPLE: (
00000220                         STR: 'send_message' (0C 00 00 00 73 65 6E 64 5F 6D 65 73 73 61 67 65),
00000231                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
0000023B                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00000246                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00000252                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
0000025E                         STR: 'SendAbilityOutputToAll' (16 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 41 6C 6C),
00000279                         STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00000289                         STR: 'ID_CLIENT_ABILITY_VIRUS_HIT' (1B 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 41 42 49 4C 49 54 59 5F 56 49 52 55 53 5F 48 49 54),
000002A9                         STR: 'virus' (05 00 00 00 76 69 72 75 73),
000002B3                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000002BF                         STR: 'directobject' (0C 00 00 00 64 69 72 65 63 74 6F 62 6A 65 63 74),
000002D0                         STR: 'exValues' (08 00 00 00 65 78 56 61 6C 75 65 73),
000002DD                         STR: 'DEFLECTED' (09 00 00 00 44 45 46 4C 45 43 54 45 44),
000002EB                         STR: 'ID_CLIENT_ABILITY_VIRUS_DEFLECTED' (21 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 41 42 49 4C 49 54 59 5F 56 49 52 55 53 5F 44 45 46 4C 45 43 54 45 44),
00000311                         STR: 'REFLECTED' (09 00 00 00 52 45 46 4C 45 43 54 45 44),
0000031F                         STR: 'ID_CLIENT_ABILITY_VIRUS_REFLECTED' (21 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 41 42 49 4C 49 54 59 5F 56 49 52 55 53 5F 52 45 46 4C 45 43 54 45 44)
                             )
                         varnames:
00000345                     TUPLE: (
0000034A                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00000355                         STR: 'virus' (05 00 00 00 76 69 72 75 73),
0000035F                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000036B                         STR: 'directobject' (0C 00 00 00 64 69 72 65 63 74 6F 62 6A 65 63 74),
0000037C                         STR: 'send_message' (0C 00 00 00 73 65 6E 64 5F 6D 65 73 73 61 67 65),
0000038D                         STR: 'exValues' (08 00 00 00 65 78 56 61 6C 75 65 73)
                             )
                         freevars:
0000039A                     TUPLE: ()
                         cellvars:
0000039F                     TUPLE: ()
                         filename:
000003A4                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\virii_defines.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 76 69 72 69 69 5F 64 65 66 69 6E 65 73 2E 70 79)
                         name:
000003FD                     STR: 'SendVirusResultToAll' (14 00 00 00 53 65 6E 64 56 69 72 75 73 52 65 73 75 6C 74 54 6F 41 6C 6C)
                         firslineno:
00000416                     LONG: 33L (21 00 00 00)
                         lnotab:
0000041A                     STR: '\x00\x01\r\x01\x08\x02\r\x01 \x01\r\x01 \x01\r\x01' (10 00 00 00 00 01 0D 01 08 02 0D 01 20 01 0D 01 20 01 0D 01),
0000042F             CODE:
                         argcount:
00000430                     LONG: 4L (04 00 00 00)
                         nlocals:
00000434                     LONG: 7L (07 00 00 00)
                         stacksize:
00000438                     LONG: 7L (07 00 00 00)
                         flags:
0000043C                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000440                     STR: 't\x00\x00|\x00\x00i\x02\x00\x83\x01\x00t\x03\x00j\x02\x00o$\x00\x01t\x04\x00i\x05\x00t\x06\x00i\x07\x00|\x01\x00|\x00\x00\x83\x03\x00\x01t\x03\x00d\x01\x00f\x02\x00Sn\x01\x00\x01t\t\x00|\x00\x00i\n\x00|\x02\x00\x83\x02\x00t\x0c\x00j\x02\x00oE\x00\x01t\x04\x00i\r\x00|\x02\x00\x83\x01\x00}\x06\x00t\x04\x00i\x0f\x00t\x06\x00i\x10\x00|\x01\x00|\x00\x00i\x02\x00i\x11\x00|\x00\x00i\n\x00i\x11\x00|\x06\x00\x83\x05\x00\x01t\x0c\x00d\x01\x00f\x02\x00Sn\x01\x00\x01t\x12\x00|\x00\x00i\n\x00\x83\x01\x00}\x05\x00t\x14\x00|\x00\x00i\x02\x00\x83\x01\x00}\x04\x00t\x16\x00|\x01\x00|\x00\x00i\x02\x00i\x11\x00|\x00\x00i\n\x00i\x11\x00|\x04\x00|\x05\x00|\x03\x00\x83\x06\x00Sd\x00\x00S' (DF 00 00 00 74 00 00 7C 00 00 69 02 00 83 01 00 74 03 00 6A 02 00 6F 24 00 01 74 04 00 69 05 00 74 06 00 69 07 00 7C 01 00 7C 00 00 83 03 00 01 74 03 00 64 01 00 66 02 00 53 6E 01 00 01 74 09 00 7C 00 00 69 0A 00 7C 02 00 83 02 00 74 0C 00 6A 02 00 6F 45 00 01 74 04 00 69 0D 00 7C 02 00 83 01 00 7D 06 00 74 04 00 69 0F 00 74 06 00 69 10 00 7C 01 00 7C 00 00 69 02 00 69 11 00 7C 00 00 69 0A 00 69 11 00 7C 06 00 83 05 00 01 74 0C 00 64 01 00 66 02 00 53 6E 01 00 01 74 12 00 7C 00 00 69 0A 00 83 01 00 7D 05 00 74 14 00 7C 00 00 69 02 00 83 01 00 7D 04 00 74 16 00 7C 01 00 7C 00 00 69 02 00 69 11 00 7C 00 00 69 0A 00 69 11 00 7C 04 00 7C 05 00 7C 03 00 83 06 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'ProgramLauncherCheck'
                             00000003     7C - LOAD_FAST           'sentence'
                             00000006     69 - LOAD_ATTR           'subject'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     74 - LOAD_GLOBAL         'FAILURE'
                             0000000F     6A - COMPARE_OP          "=="
                             00000012     6F - JUMP_IF_FALSE       -> 00000039
                             00000015     01 - POP_TOP             
                             00000016     74 - LOAD_GLOBAL         'Utility'
                             00000019     69 - LOAD_ATTR           'SendAbilityOutputToCasterSentence'
                             0000001C     74 - LOAD_GLOBAL         'StringTable'
                             0000001F     69 - LOAD_ATTR           'ID_CLIENT_ABILITY_PROGRAM_LAUNCHER_NOT_EQUIPPED'
                             00000022     7C - LOAD_FAST           'virus'
                             00000025     7C - LOAD_FAST           'sentence'
                             00000028     83 - CALL_FUNCTION       r0003
                             0000002B     01 - POP_TOP             
                             0000002C     74 - LOAD_GLOBAL         'FAILURE'
                             0000002F     64 - LOAD_CONST          0
                             00000032     66 - BUILD_TUPLE         r0002
                             00000035     53 - RETURN_VALUE        
                             00000036     6E - JUMP_FORWARD        -> 0000003A
                             00000039     01 - POP_TOP             
                             0000003A     74 - LOAD_GLOBAL         'VaccinationCheck'
                             0000003D     7C - LOAD_FAST           'sentence'
                             00000040     69 - LOAD_ATTR           'directObject'
                             00000043     7C - LOAD_FAST           'vaccination'
                             00000046     83 - CALL_FUNCTION       r0002
                             00000049     74 - LOAD_GLOBAL         'DEFLECTED'
                             0000004C     6A - COMPARE_OP          "=="
                             0000004F     6F - JUMP_IF_FALSE       -> 00000097
                             00000052     01 - POP_TOP             
                             00000053     74 - LOAD_GLOBAL         'Utility'
                             00000056     69 - LOAD_ATTR           'GetAbilityInfoID'
                             00000059     7C - LOAD_FAST           'vaccination'
                             0000005C     83 - CALL_FUNCTION       r0001
                             0000005F     7D - STORE_FAST          'vaccination_name_id'
                             00000062     74 - LOAD_GLOBAL         'Utility'
                             00000065     69 - LOAD_ATTR           'SendAbilityOutputToAll'
                             00000068     74 - LOAD_GLOBAL         'StringTable'
                             0000006B     69 - LOAD_ATTR           'ID_CLIENT_ABILITY_VIRUS_VACCINATED'
                             0000006E     7C - LOAD_FAST           'virus'
                             00000071     7C - LOAD_FAST           'sentence'
                             00000074     69 - LOAD_ATTR           'subject'
                             00000077     69 - LOAD_ATTR           'locator'
                             0000007A     7C - LOAD_FAST           'sentence'
                             0000007D     69 - LOAD_ATTR           'directObject'
                             00000080     69 - LOAD_ATTR           'locator'
                             00000083     7C - LOAD_FAST           'vaccination_name_id'
                             00000086     83 - CALL_FUNCTION       r0005
                             00000089     01 - POP_TOP             
                             0000008A     74 - LOAD_GLOBAL         'DEFLECTED'
                             0000008D     64 - LOAD_CONST          0
                             00000090     66 - BUILD_TUPLE         r0002
                             00000093     53 - RETURN_VALUE        
                             00000094     6E - JUMP_FORWARD        -> 00000098
                             00000097     01 - POP_TOP             
                             00000098     74 - LOAD_GLOBAL         'CalcDifficultyValue'
                             0000009B     7C - LOAD_FAST           'sentence'
                             0000009E     69 - LOAD_ATTR           'directObject'
                             000000A1     83 - CALL_FUNCTION       r0001
                             000000A4     7D - STORE_FAST          'difficultyRating'
                             000000A7     74 - LOAD_GLOBAL         'SingleSuccessRating'
                             000000AA     7C - LOAD_FAST           'sentence'
                             000000AD     69 - LOAD_ATTR           'subject'
                             000000B0     83 - CALL_FUNCTION       r0001
                             000000B3     7D - STORE_FAST          'successChance'
                             000000B6     74 - LOAD_GLOBAL         'DifficultyCheck'
                             000000B9     7C - LOAD_FAST           'virus'
                             000000BC     7C - LOAD_FAST           'sentence'
                             000000BF     69 - LOAD_ATTR           'subject'
                             000000C2     69 - LOAD_ATTR           'locator'
                             000000C5     7C - LOAD_FAST           'sentence'
                             000000C8     69 - LOAD_ATTR           'directObject'
                             000000CB     69 - LOAD_ATTR           'locator'
                             000000CE     7C - LOAD_FAST           'successChance'
                             000000D1     7C - LOAD_FAST           'difficultyRating'
                             000000D4     7C - LOAD_FAST           'allow_success_msg'
                             000000D7     83 - CALL_FUNCTION       r0006
                             000000DA     53 - RETURN_VALUE        
                             000000DB     64 - LOAD_CONST          None
                             000000DE     53 - RETURN_VALUE        
                         consts:
00000524                     TUPLE: (
00000529                         None (4E),
0000052A                         INT: 0 (00 00 00 00)
                             )
                         names:
0000052F                     TUPLE: (
00000534                         STR: 'ProgramLauncherCheck' (14 00 00 00 50 72 6F 67 72 61 6D 4C 61 75 6E 63 68 65 72 43 68 65 63 6B),
0000054D                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65),
0000055A                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000566                         STR: 'FAILURE' (07 00 00 00 46 41 49 4C 55 52 45),
00000572                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
0000057E                         STR: 'SendAbilityOutputToCasterSentence' (21 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 43 61 73 74 65 72 53 65 6E 74 65 6E 63 65),
000005A4                         STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
000005B4                         STR: 'ID_CLIENT_ABILITY_PROGRAM_LAUNCHER_NOT_EQUIPPED' (2F 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 41 42 49 4C 49 54 59 5F 50 52 4F 47 52 41 4D 5F 4C 41 55 4E 43 48 45 52 5F 4E 4F 54 5F 45 51 55 49 50 50 45 44),
000005E8                         STR: 'virus' (05 00 00 00 76 69 72 75 73),
000005F2                         STR: 'VaccinationCheck' (10 00 00 00 56 61 63 63 69 6E 61 74 69 6F 6E 43 68 65 63 6B),
00000607                         STR: 'directObject' (0C 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74),
00000618                         STR: 'vaccination' (0B 00 00 00 76 61 63 63 69 6E 61 74 69 6F 6E),
00000628                         STR: 'DEFLECTED' (09 00 00 00 44 45 46 4C 45 43 54 45 44),
00000636                         STR: 'GetAbilityInfoID' (10 00 00 00 47 65 74 41 62 69 6C 69 74 79 49 6E 66 6F 49 44),
0000064B                         STR: 'vaccination_name_id' (13 00 00 00 76 61 63 63 69 6E 61 74 69 6F 6E 5F 6E 61 6D 65 5F 69 64),
00000663                         STR: 'SendAbilityOutputToAll' (16 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 41 6C 6C),
0000067E                         STR: 'ID_CLIENT_ABILITY_VIRUS_VACCINATED' (22 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 41 42 49 4C 49 54 59 5F 56 49 52 55 53 5F 56 41 43 43 49 4E 41 54 45 44),
000006A5                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
000006B1                         STR: 'CalcDifficultyValue' (13 00 00 00 43 61 6C 63 44 69 66 66 69 63 75 6C 74 79 56 61 6C 75 65),
000006C9                         STR: 'difficultyRating' (10 00 00 00 64 69 66 66 69 63 75 6C 74 79 52 61 74 69 6E 67),
000006DE                         STR: 'SingleSuccessRating' (13 00 00 00 53 69 6E 67 6C 65 53 75 63 63 65 73 73 52 61 74 69 6E 67),
000006F6                         STR: 'successChance' (0D 00 00 00 73 75 63 63 65 73 73 43 68 61 6E 63 65),
00000708                         STR: 'DifficultyCheck' (0F 00 00 00 44 69 66 66 69 63 75 6C 74 79 43 68 65 63 6B),
0000071C                         STR: 'allow_success_msg' (11 00 00 00 61 6C 6C 6F 77 5F 73 75 63 63 65 73 73 5F 6D 73 67)
                             )
                         varnames:
00000732                     TUPLE: (
00000737                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65),
00000744                         STR: 'virus' (05 00 00 00 76 69 72 75 73),
0000074E                         STR: 'vaccination' (0B 00 00 00 76 61 63 63 69 6E 61 74 69 6F 6E),
0000075E                         STR: 'allow_success_msg' (11 00 00 00 61 6C 6C 6F 77 5F 73 75 63 63 65 73 73 5F 6D 73 67),
00000774                         STR: 'successChance' (0D 00 00 00 73 75 63 63 65 73 73 43 68 61 6E 63 65),
00000786                         STR: 'difficultyRating' (10 00 00 00 64 69 66 66 69 63 75 6C 74 79 52 61 74 69 6E 67),
0000079B                         STR: 'vaccination_name_id' (13 00 00 00 76 61 63 63 69 6E 61 74 69 6F 6E 5F 6E 61 6D 65 5F 69 64)
                             )
                         freevars:
000007B3                     TUPLE: ()
                         cellvars:
000007B8                     TUPLE: ()
                         filename:
000007BD                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\virii_defines.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 76 69 72 69 69 5F 64 65 66 69 6E 65 73 2E 70 79)
                         name:
00000816                     STR: 'VirusSuccessCheck' (11 00 00 00 56 69 72 75 73 53 75 63 63 65 73 73 43 68 65 63 6B)
                         firslineno:
0000082C                     LONG: 47L (2F 00 00 00)
                         lnotab:
00000830                     STR: '\x00\x03\x16\x01\x16\x01\x0e\x03\x19\x01\x0f\x01\x0f\x01\x19\x01\x0e\x04\x0f\x03\x0f\x03' (16 00 00 00 00 03 16 01 16 01 0E 03 19 01 0F 01 0F 01 19 01 0E 04 0F 03 0F 03),
0000084B             CODE:
                         argcount:
0000084C                     LONG: 1L (01 00 00 00)
                         nlocals:
00000850                     LONG: 1L (01 00 00 00)
                         stacksize:
00000854                     LONG: 2L (02 00 00 00)
                         flags:
00000858                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000085C                     STR: 't\x00\x00i\x01\x00|\x00\x00\x83\x01\x00t\x03\x00j\x02\x00o\x08\x00\x01t\x03\x00Sn\x01\x00\x01t\x04\x00Sd\x00\x00S' (26 00 00 00 74 00 00 69 01 00 7C 00 00 83 01 00 74 03 00 6A 02 00 6F 08 00 01 74 03 00 53 6E 01 00 01 74 04 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'IsProgramLauncherEquipped'
                             00000006     7C - LOAD_FAST           'player'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     74 - LOAD_GLOBAL         'FAILURE'
                             0000000F     6A - COMPARE_OP          "=="
                             00000012     6F - JUMP_IF_FALSE       -> 0000001D
                             00000015     01 - POP_TOP             
                             00000016     74 - LOAD_GLOBAL         'FAILURE'
                             00000019     53 - RETURN_VALUE        
                             0000001A     6E - JUMP_FORWARD        -> 0000001E
                             0000001D     01 - POP_TOP             
                             0000001E     74 - LOAD_GLOBAL         'SUCCESS'
                             00000021     53 - RETURN_VALUE        
                             00000022     64 - LOAD_CONST          None
                             00000025     53 - RETURN_VALUE        
                         consts:
00000887                     TUPLE: (
0000088C                         None (4E)
                             )
                         names:
0000088D                     TUPLE: (
00000892                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
0000089E                         STR: 'IsProgramLauncherEquipped' (19 00 00 00 49 73 50 72 6F 67 72 61 6D 4C 61 75 6E 63 68 65 72 45 71 75 69 70 70 65 64),
000008BC                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
000008C7                         STR: 'FAILURE' (07 00 00 00 46 41 49 4C 55 52 45),
000008D3                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53)
                             )
                         varnames:
000008DF                     TUPLE: (
000008E4                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72)
                             )
                         freevars:
000008EF                     TUPLE: ()
                         cellvars:
000008F4                     TUPLE: ()
                         filename:
000008F9                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\virii_defines.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 76 69 72 69 69 5F 64 65 66 69 6E 65 73 2E 70 79)
                         name:
00000952                     STR: 'ProgramLauncherCheck' (14 00 00 00 50 72 6F 67 72 61 6D 4C 61 75 6E 63 68 65 72 43 68 65 63 6B)
                         firslineno:
0000096B                     LONG: 75L (4B 00 00 00)
                         lnotab:
0000096F                     STR: '\x00\x01\x16\x01\x08\x01' (06 00 00 00 00 01 16 01 08 01),
0000097A             CODE:
                         argcount:
0000097B                     LONG: 2L (02 00 00 00)
                         nlocals:
0000097F                     LONG: 2L (02 00 00 00)
                         stacksize:
00000983                     LONG: 2L (02 00 00 00)
                         flags:
00000987                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000098B                     STR: "|\x01\x00o'\x00\x01|\x00\x00i\x02\x00|\x01\x00\x19o\x15\x00\x01t\x03\x00i\x04\x00d\x01\x00\x83\x01\x00\x01t\x05\x00Sq.\x00\x01n\x01\x00\x01t\x06\x00Sd\x00\x00S" (36 00 00 00 7C 01 00 6F 27 00 01 7C 00 00 69 02 00 7C 01 00 19 6F 15 00 01 74 03 00 69 04 00 64 01 00 83 01 00 01 74 05 00 53 71 2E 00 01 6E 01 00 01 74 06 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'vaccination'
                             00000003     6F - JUMP_IF_FALSE       -> 0000002D
                             00000006     01 - POP_TOP             
                             00000007     7C - LOAD_FAST           'player'
                             0000000A     69 - LOAD_ATTR           'hasAbility'
                             0000000D     7C - LOAD_FAST           'vaccination'
                             00000010     19 - BINARY_SUBSCR       
                             00000011     6F - JUMP_IF_FALSE       -> 00000029
                             00000014     01 - POP_TOP             
                             00000015     74 - LOAD_GLOBAL         'Utility'
                             00000018     69 - LOAD_ATTR           'outputAbilityDebug'
                             0000001B     64 - LOAD_CONST          'VaccinationCheck: Player deflected due to vaccinate!'
                             0000001E     83 - CALL_FUNCTION       r0001
                             00000021     01 - POP_TOP             
                             00000022     74 - LOAD_GLOBAL         'DEFLECTED'
                             00000025     53 - RETURN_VALUE        
                             00000026     71 - JUMP_ABSOLUTE       -> 0000002E
                             00000029     01 - POP_TOP             
                             0000002A     6E - JUMP_FORWARD        -> 0000002E
                             0000002D     01 - POP_TOP             
                             0000002E     74 - LOAD_GLOBAL         'SUCCESS'
                             00000031     53 - RETURN_VALUE        
                             00000032     64 - LOAD_CONST          None
                             00000035     53 - RETURN_VALUE        
                         consts:
000009C6                     TUPLE: (
000009CB                         None (4E),
000009CC                         STR: 'VaccinationCheck: Player deflected due to vaccinate!' (34 00 00 00 56 61 63 63 69 6E 61 74 69 6F 6E 43 68 65 63 6B 3A 20 50 6C 61 79 65 72 20 64 65 66 6C 65 63 74 65 64 20 64 75 65 20 74 6F 20 76 61 63 63 69 6E 61 74 65 21)
                             )
                         names:
00000A05                     TUPLE: (
00000A0A                         STR: 'vaccination' (0B 00 00 00 76 61 63 63 69 6E 61 74 69 6F 6E),
00000A1A                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00000A25                         STR: 'hasAbility' (0A 00 00 00 68 61 73 41 62 69 6C 69 74 79),
00000A34                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000A40                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000A57                         STR: 'DEFLECTED' (09 00 00 00 44 45 46 4C 45 43 54 45 44),
00000A65                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53)
                             )
                         varnames:
00000A71                     TUPLE: (
00000A76                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00000A81                         STR: 'vaccination' (0B 00 00 00 76 61 63 63 69 6E 61 74 69 6F 6E)
                             )
                         freevars:
00000A91                     TUPLE: ()
                         cellvars:
00000A96                     TUPLE: ()
                         filename:
00000A9B                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\virii_defines.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 76 69 72 69 69 5F 64 65 66 69 6E 65 73 2E 70 79)
                         name:
00000AF4                     STR: 'VaccinationCheck' (10 00 00 00 56 61 63 63 69 6E 61 74 69 6F 6E 43 68 65 63 6B)
                         firslineno:
00000B09                     LONG: 84L (54 00 00 00)
                         lnotab:
00000B0D                     STR: '\x00\x03\x07\x03\x0e\x01\r\x01\x0c\x02' (0A 00 00 00 00 03 07 03 0E 01 0D 01 0C 02),
00000B1C             CODE:
                         argcount:
00000B1D                     LONG: 2L (02 00 00 00)
                         nlocals:
00000B21                     LONG: 3L (03 00 00 00)
                         stacksize:
00000B25                     LONG: 2L (02 00 00 00)
                         flags:
00000B29                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000B2D                     STR: '|\x00\x00i\x01\x00|\x01\x00\x19oN\x00\x01t\x03\x00i\x04\x00d\x01\x00\x83\x01\x00}\x02\x00|\x00\x00i\x01\x00t\x06\x00\x19o-\x00\x01|\x00\x00i\x07\x00t\x06\x00\x19|\x02\x00j\x05\x00o\x15\x00\x01t\x08\x00i\t\x00d\x02\x00\x83\x01\x00\x01t\n\x00SqX\x00\x01q\\\x00\x01n\x01\x00\x01t\x0b\x00Sd\x00\x00S' (64 00 00 00 7C 00 00 69 01 00 7C 01 00 19 6F 4E 00 01 74 03 00 69 04 00 64 01 00 83 01 00 7D 02 00 7C 00 00 69 01 00 74 06 00 19 6F 2D 00 01 7C 00 00 69 07 00 74 06 00 19 7C 02 00 6A 05 00 6F 15 00 01 74 08 00 69 09 00 64 02 00 83 01 00 01 74 0A 00 53 71 58 00 01 71 5C 00 01 6E 01 00 01 74 0B 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'subject'
                             00000003     69 - LOAD_ATTR           'hasAbility'
                             00000006     7C - LOAD_FAST           'reflection'
                             00000009     19 - BINARY_SUBSCR       
                             0000000A     6F - JUMP_IF_FALSE       -> 0000005B
                             0000000D     01 - POP_TOP             
                             0000000E     74 - LOAD_GLOBAL         'random'
                             00000011     69 - LOAD_ATTR           'randrange'
                             00000014     64 - LOAD_CONST          100
                             00000017     83 - CALL_FUNCTION       r0001
                             0000001A     7D - STORE_FAST          'randomRoll'
                             0000001D     7C - LOAD_FAST           'subject'
                             00000020     69 - LOAD_ATTR           'hasAbility'
                             00000023     74 - LOAD_GLOBAL         'HackerAbility'
                             00000026     19 - BINARY_SUBSCR       
                             00000027     6F - JUMP_IF_FALSE       -> 00000057
                             0000002A     01 - POP_TOP             
                             0000002B     7C - LOAD_FAST           'subject'
                             0000002E     69 - LOAD_ATTR           'abilities'
                             00000031     74 - LOAD_GLOBAL         'HackerAbility'
                             00000034     19 - BINARY_SUBSCR       
                             00000035     7C - LOAD_FAST           'randomRoll'
                             00000038     6A - COMPARE_OP          ">="
                             0000003B     6F - JUMP_IF_FALSE       -> 00000053
                             0000003E     01 - POP_TOP             
                             0000003F     74 - LOAD_GLOBAL         'Utility'
                             00000042     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000045     64 - LOAD_CONST          'Relection Check : virus reflected! '
                             00000048     83 - CALL_FUNCTION       r0001
                             0000004B     01 - POP_TOP             
                             0000004C     74 - LOAD_GLOBAL         'REFLECTED'
                             0000004F     53 - RETURN_VALUE        
                             00000050     71 - JUMP_ABSOLUTE       -> 00000058
                             00000053     01 - POP_TOP             
                             00000054     71 - JUMP_ABSOLUTE       -> 0000005C
                             00000057     01 - POP_TOP             
                             00000058     6E - JUMP_FORWARD        -> 0000005C
                             0000005B     01 - POP_TOP             
                             0000005C     74 - LOAD_GLOBAL         'SUCCESS'
                             0000005F     53 - RETURN_VALUE        
                             00000060     64 - LOAD_CONST          None
                             00000063     53 - RETURN_VALUE        
                         consts:
00000B96                     TUPLE: (
00000B9B                         None (4E),
00000B9C                         INT: 100 (64 00 00 00),
00000BA1                         STR: 'Relection Check : virus reflected! ' (23 00 00 00 52 65 6C 65 63 74 69 6F 6E 20 43 68 65 63 6B 20 3A 20 76 69 72 75 73 20 72 65 66 6C 65 63 74 65 64 21 20)
                             )
                         names:
00000BC9                     TUPLE: (
00000BCE                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000BDA                         STR: 'hasAbility' (0A 00 00 00 68 61 73 41 62 69 6C 69 74 79),
00000BE9                         STR: 'reflection' (0A 00 00 00 72 65 66 6C 65 63 74 69 6F 6E),
00000BF8                         STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00000C03                         STR: 'randrange' (09 00 00 00 72 61 6E 64 72 61 6E 67 65),
00000C11                         STR: 'randomRoll' (0A 00 00 00 72 61 6E 64 6F 6D 52 6F 6C 6C),
00000C20                         STR: 'HackerAbility' (0D 00 00 00 48 61 63 6B 65 72 41 62 69 6C 69 74 79),
00000C32                         STR: 'abilities' (09 00 00 00 61 62 69 6C 69 74 69 65 73),
00000C40                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000C4C                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000C63                         STR: 'REFLECTED' (09 00 00 00 52 45 46 4C 45 43 54 45 44),
00000C71                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53)
                             )
                         varnames:
00000C7D                     TUPLE: (
00000C82                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000C8E                         STR: 'reflection' (0A 00 00 00 72 65 66 6C 65 63 74 69 6F 6E),
00000C9D                         STR: 'randomRoll' (0A 00 00 00 72 61 6E 64 6F 6D 52 6F 6C 6C)
                             )
                         freevars:
00000CAC                     TUPLE: ()
                         cellvars:
00000CB1                     TUPLE: ()
                         filename:
00000CB6                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\virii_defines.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 76 69 72 69 69 5F 64 65 66 69 6E 65 73 2E 70 79)
                         name:
00000D0F                     STR: 'ReflectionCheck' (0F 00 00 00 52 65 66 6C 65 63 74 69 6F 6E 43 68 65 63 6B)
                         firslineno:
00000D23                     LONG: 99L (63 00 00 00)
                         lnotab:
00000D27                     STR: '\x00\x02\x0e\x01\x0f\x01\x0e\x02\x14\x01\r\x01\x10\x02' (0E 00 00 00 00 02 0E 01 0F 01 0E 02 14 01 0D 01 10 02),
00000D3A             CODE:
                         argcount:
00000D3B                     LONG: 1L (01 00 00 00)
                         nlocals:
00000D3F                     LONG: 2L (02 00 00 00)
                         stacksize:
00000D43                     LONG: 5L (05 00 00 00)
                         flags:
00000D47                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000D4B                     STR: '|\x00\x00i\x01\x00}\x01\x00|\x00\x00i\x03\x00t\x04\x00\x19|\x01\x00j\x04\x00o\x11\x00\x01|\x00\x00i\x03\x00t\x04\x00\x19}\x01\x00n\x01\x00\x01|\x01\x00d\x01\x007}\x01\x00d\x01\x00d\x02\x00t\x05\x00i\x06\x00|\x00\x00\x83\x01\x00|\x00\x00i\x03\x00t\x04\x00\x19\x17\x14\x17}\x01\x00|\x01\x00Sd\x00\x00S' (62 00 00 00 7C 00 00 69 01 00 7D 01 00 7C 00 00 69 03 00 74 04 00 19 7C 01 00 6A 04 00 6F 11 00 01 7C 00 00 69 03 00 74 04 00 19 7D 01 00 6E 01 00 01 7C 01 00 64 01 00 37 7D 01 00 64 01 00 64 02 00 74 05 00 69 06 00 7C 00 00 83 01 00 7C 00 00 69 03 00 74 04 00 19 17 14 17 7D 01 00 7C 01 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'player'
                             00000003     69 - LOAD_ATTR           'Level'
                             00000006     7D - STORE_FAST          'difficulty'
                             00000009     7C - LOAD_FAST           'player'
                             0000000C     69 - LOAD_ATTR           'abilities'
                             0000000F     74 - LOAD_GLOBAL         'ResistVirusesAbility'
                             00000012     19 - BINARY_SUBSCR       
                             00000013     7C - LOAD_FAST           'difficulty'
                             00000016     6A - COMPARE_OP          ">"
                             00000019     6F - JUMP_IF_FALSE       -> 0000002D
                             0000001C     01 - POP_TOP             
                             0000001D     7C - LOAD_FAST           'player'
                             00000020     69 - LOAD_ATTR           'abilities'
                             00000023     74 - LOAD_GLOBAL         'ResistVirusesAbility'
                             00000026     19 - BINARY_SUBSCR       
                             00000027     7D - STORE_FAST          'difficulty'
                             0000002A     6E - JUMP_FORWARD        -> 0000002E
                             0000002D     01 - POP_TOP             
                             0000002E     7C - LOAD_FAST           'difficulty'
                             00000031     64 - LOAD_CONST          50
                             00000034     37 - INPLACE_ADD         
                             00000035     7D - STORE_FAST          'difficulty'
                             00000038     64 - LOAD_CONST          50
                             0000003B     64 - LOAD_CONST          4
                             0000003E     74 - LOAD_GLOBAL         'Utility'
                             00000041     69 - LOAD_ATTR           'Get_HPAL_Level'
                             00000044     7C - LOAD_FAST           'player'
                             00000047     83 - CALL_FUNCTION       r0001
                             0000004A     7C - LOAD_FAST           'player'
                             0000004D     69 - LOAD_ATTR           'abilities'
                             00000050     74 - LOAD_GLOBAL         'ResistVirusesAbility'
                             00000053     19 - BINARY_SUBSCR       
                             00000054     17 - BINARY_ADD          
                             00000055     14 - BINARY_MULTIPLY     
                             00000056     17 - BINARY_ADD          
                             00000057     7D - STORE_FAST          'difficulty'
                             0000005A     7C - LOAD_FAST           'difficulty'
                             0000005D     53 - RETURN_VALUE        
                             0000005E     64 - LOAD_CONST          None
                             00000061     53 - RETURN_VALUE        
                         consts:
00000DB2                     TUPLE: (
00000DB7                         None (4E),
00000DB8                         INT: 50 (32 00 00 00),
00000DBD                         INT: 4 (04 00 00 00)
                             )
                         names:
00000DC2                     TUPLE: (
00000DC7                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00000DD2                         STR: 'Level' (05 00 00 00 4C 65 76 65 6C),
00000DDC                         STR: 'difficulty' (0A 00 00 00 64 69 66 66 69 63 75 6C 74 79),
00000DEB                         STR: 'abilities' (09 00 00 00 61 62 69 6C 69 74 69 65 73),
00000DF9                         STR: 'ResistVirusesAbility' (14 00 00 00 52 65 73 69 73 74 56 69 72 75 73 65 73 41 62 69 6C 69 74 79),
00000E12                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000E1E                         STR: 'Get_HPAL_Level' (0E 00 00 00 47 65 74 5F 48 50 41 4C 5F 4C 65 76 65 6C)
                             )
                         varnames:
00000E31                     TUPLE: (
00000E36                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00000E41                         STR: 'difficulty' (0A 00 00 00 64 69 66 66 69 63 75 6C 74 79)
                             )
                         freevars:
00000E50                     TUPLE: ()
                         cellvars:
00000E55                     TUPLE: ()
                         filename:
00000E5A                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\virii_defines.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 76 69 72 69 69 5F 64 65 66 69 6E 65 73 2E 70 79)
                         name:
00000EB3                     STR: 'CalcDifficultyValue' (13 00 00 00 43 61 6C 63 44 69 66 66 69 63 75 6C 74 79 56 61 6C 75 65)
                         firslineno:
00000ECB                     LONG: 116L (74 00 00 00)
                         lnotab:
00000ECF                     STR: '\x00\x03\t\x01\x14\x01\x11\x03\n\x02"\x02' (0C 00 00 00 00 03 09 01 14 01 11 03 0A 02 22 02),
00000EE0             CODE:
                         argcount:
00000EE1                     LONG: 1L (01 00 00 00)
                         nlocals:
00000EE5                     LONG: 2L (02 00 00 00)
                         stacksize:
00000EE9                     LONG: 3L (03 00 00 00)
                         flags:
00000EED                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000EF1                     STR: 'd\x01\x00t\x00\x00t\x01\x00\x17\x14}\x01\x00|\x00\x00i\x04\x00t\x05\x00\x19}\x01\x00|\x00\x00i\x04\x00t\x06\x00\x19o\x15\x00\x01|\x01\x00|\x00\x00i\x04\x00t\x06\x00\x197}\x01\x00n\x01\x00\x01|\x01\x00d\x01\x009}\x01\x00|\x01\x00Sd\x00\x00S' (50 00 00 00 64 01 00 74 00 00 74 01 00 17 14 7D 01 00 7C 00 00 69 04 00 74 05 00 19 7D 01 00 7C 00 00 69 04 00 74 06 00 19 6F 15 00 01 7C 01 00 7C 00 00 69 04 00 74 06 00 19 37 7D 01 00 6E 01 00 01 7C 01 00 64 01 00 39 7D 01 00 7C 01 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          4
                             00000003     74 - LOAD_GLOBAL         'TransmitVirus'
                             00000006     74 - LOAD_GLOBAL         'ExecuteProgram'
                             00000009     17 - BINARY_ADD          
                             0000000A     14 - BINARY_MULTIPLY     
                             0000000B     7D - STORE_FAST          'success_chance'
                             0000000E     7C - LOAD_FAST           'player'
                             00000011     69 - LOAD_ATTR           'abilities'
                             00000014     74 - LOAD_GLOBAL         'TransmitVirusAbility'
                             00000017     19 - BINARY_SUBSCR       
                             00000018     7D - STORE_FAST          'success_chance'
                             0000001B     7C - LOAD_FAST           'player'
                             0000001E     69 - LOAD_ATTR           'abilities'
                             00000021     74 - LOAD_GLOBAL         'ExecuteProgramAbility'
                             00000024     19 - BINARY_SUBSCR       
                             00000025     6F - JUMP_IF_FALSE       -> 0000003D
                             00000028     01 - POP_TOP             
                             00000029     7C - LOAD_FAST           'success_chance'
                             0000002C     7C - LOAD_FAST           'player'
                             0000002F     69 - LOAD_ATTR           'abilities'
                             00000032     74 - LOAD_GLOBAL         'ExecuteProgramAbility'
                             00000035     19 - BINARY_SUBSCR       
                             00000036     37 - INPLACE_ADD         
                             00000037     7D - STORE_FAST          'success_chance'
                             0000003A     6E - JUMP_FORWARD        -> 0000003E
                             0000003D     01 - POP_TOP             
                             0000003E     7C - LOAD_FAST           'success_chance'
                             00000041     64 - LOAD_CONST          4
                             00000044     39 - INPLACE_MULTIPLY    
                             00000045     7D - STORE_FAST          'success_chance'
                             00000048     7C - LOAD_FAST           'success_chance'
                             0000004B     53 - RETURN_VALUE        
                             0000004C     64 - LOAD_CONST          None
                             0000004F     53 - RETURN_VALUE        
                         consts:
00000F46                     TUPLE: (
00000F4B                         None (4E),
00000F4C                         INT: 4 (04 00 00 00)
                             )
                         names:
00000F51                     TUPLE: (
00000F56                         STR: 'TransmitVirus' (0D 00 00 00 54 72 61 6E 73 6D 69 74 56 69 72 75 73),
00000F68                         STR: 'ExecuteProgram' (0E 00 00 00 45 78 65 63 75 74 65 50 72 6F 67 72 61 6D),
00000F7B                         STR: 'success_chance' (0E 00 00 00 73 75 63 63 65 73 73 5F 63 68 61 6E 63 65),
00000F8E                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00000F99                         STR: 'abilities' (09 00 00 00 61 62 69 6C 69 74 69 65 73),
00000FA7                         STR: 'TransmitVirusAbility' (14 00 00 00 54 72 61 6E 73 6D 69 74 56 69 72 75 73 41 62 69 6C 69 74 79),
00000FC0                         STR: 'ExecuteProgramAbility' (15 00 00 00 45 78 65 63 75 74 65 50 72 6F 67 72 61 6D 41 62 69 6C 69 74 79)
                             )
                         varnames:
00000FDA                     TUPLE: (
00000FDF                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00000FEA                         STR: 'success_chance' (0E 00 00 00 73 75 63 63 65 73 73 5F 63 68 61 6E 63 65)
                             )
                         freevars:
00000FFD                     TUPLE: ()
                         cellvars:
00001002                     TUPLE: ()
                         filename:
00001007                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\virii_defines.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 76 69 72 69 69 5F 64 65 66 69 6E 65 73 2E 70 79)
                         name:
00001060                     STR: 'CalcSuccessRating' (11 00 00 00 43 61 6C 63 53 75 63 63 65 73 73 52 61 74 69 6E 67)
                         firslineno:
00001076                     LONG: 134L (86 00 00 00)
                         lnotab:
0000107A                     STR: '\x00\x02\x0e\x01\r\x01\x0e\x01\x15\x01\n\x02' (0C 00 00 00 00 02 0E 01 0D 01 0E 01 15 01 0A 02),
0000108B             CODE:
                         argcount:
0000108C                     LONG: 1L (01 00 00 00)
                         nlocals:
00001090                     LONG: 2L (02 00 00 00)
                         stacksize:
00001094                     LONG: 3L (03 00 00 00)
                         flags:
00001098                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000109C                     STR: 't\x00\x00|\x00\x00\x83\x01\x00}\x01\x00|\x01\x00t\x03\x00i\x04\x00d\x01\x00\x83\x01\x007}\x01\x00|\x01\x00Sd\x00\x00S' (27 00 00 00 74 00 00 7C 00 00 83 01 00 7D 01 00 7C 01 00 74 03 00 69 04 00 64 01 00 83 01 00 37 7D 01 00 7C 01 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CalcSuccessRating'
                             00000003     7C - LOAD_FAST           'player'
                             00000006     83 - CALL_FUNCTION       r0001
                             00000009     7D - STORE_FAST          'success_chance'
                             0000000C     7C - LOAD_FAST           'success_chance'
                             0000000F     74 - LOAD_GLOBAL         'random'
                             00000012     69 - LOAD_ATTR           'randrange'
                             00000015     64 - LOAD_CONST          100
                             00000018     83 - CALL_FUNCTION       r0001
                             0000001B     37 - INPLACE_ADD         
                             0000001C     7D - STORE_FAST          'success_chance'
                             0000001F     7C - LOAD_FAST           'success_chance'
                             00000022     53 - RETURN_VALUE        
                             00000023     64 - LOAD_CONST          None
                             00000026     53 - RETURN_VALUE        
                         consts:
000010C8                     TUPLE: (
000010CD                         None (4E),
000010CE                         INT: 100 (64 00 00 00)
                             )
                         names:
000010D3                     TUPLE: (
000010D8                         STR: 'CalcSuccessRating' (11 00 00 00 43 61 6C 63 53 75 63 63 65 73 73 52 61 74 69 6E 67),
000010EE                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
000010F9                         STR: 'success_chance' (0E 00 00 00 73 75 63 63 65 73 73 5F 63 68 61 6E 63 65),
0000110C                         STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00001117                         STR: 'randrange' (09 00 00 00 72 61 6E 64 72 61 6E 67 65)
                             )
                         varnames:
00001125                     TUPLE: (
0000112A                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00001135                         STR: 'success_chance' (0E 00 00 00 73 75 63 63 65 73 73 5F 63 68 61 6E 63 65)
                             )
                         freevars:
00001148                     TUPLE: ()
                         cellvars:
0000114D                     TUPLE: ()
                         filename:
00001152                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\virii_defines.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 76 69 72 69 69 5F 64 65 66 69 6E 65 73 2E 70 79)
                         name:
000011AB                     STR: 'SingleSuccessRating' (13 00 00 00 53 69 6E 67 6C 65 53 75 63 63 65 73 73 52 61 74 69 6E 67)
                         firslineno:
000011C3                     LONG: 144L (90 00 00 00)
                         lnotab:
000011C7                     STR: '\x00\x01\x0c\x02\x13\x01' (06 00 00 00 00 01 0C 02 13 01),
000011D2             CODE:
                         argcount:
000011D3                     LONG: 1L (01 00 00 00)
                         nlocals:
000011D7                     LONG: 1L (01 00 00 00)
                         stacksize:
000011DB                     LONG: 2L (02 00 00 00)
                         flags:
000011DF                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000011E3                     STR: 't\x00\x00|\x00\x00\x83\x01\x00Sd\x00\x00S' (0E 00 00 00 74 00 00 7C 00 00 83 01 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CalcSuccessRating'
                             00000003     7C - LOAD_FAST           'player'
                             00000006     83 - CALL_FUNCTION       r0001
                             00000009     53 - RETURN_VALUE        
                             0000000A     64 - LOAD_CONST          None
                             0000000D     53 - RETURN_VALUE        
                         consts:
000011F6                     TUPLE: (
000011FB                         None (4E)
                             )
                         names:
000011FC                     TUPLE: (
00001201                         STR: 'CalcSuccessRating' (11 00 00 00 43 61 6C 63 53 75 63 63 65 73 73 52 61 74 69 6E 67),
00001217                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72)
                             )
                         varnames:
00001222                     TUPLE: (
00001227                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72)
                             )
                         freevars:
00001232                     TUPLE: ()
                         cellvars:
00001237                     TUPLE: ()
                         filename:
0000123C                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\virii_defines.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 76 69 72 69 69 5F 64 65 66 69 6E 65 73 2E 70 79)
                         name:
00001295                     STR: 'MultiSuccessRating' (12 00 00 00 4D 75 6C 74 69 53 75 63 63 65 73 73 52 61 74 69 6E 67)
                         firslineno:
000012AC                     LONG: 150L (96 00 00 00)
                         lnotab:
000012B0                     STR: '\x00\x01' (02 00 00 00 00 01),
000012B7             CODE:
                         argcount:
000012B8                     LONG: 6L (06 00 00 00)
                         nlocals:
000012BC                     LONG: 7L (07 00 00 00)
                         stacksize:
000012C0                     LONG: 7L (07 00 00 00)
                         flags:
000012C4                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000012C8                     STR: '|\x03\x00|\x04\x00\x18}\x06\x00|\x06\x00d\x01\x00j\x04\x00o>\x00\x01t\x03\x00t\x04\x00|\x00\x00|\x01\x00|\x02\x00|\x05\x00|\x06\x00\x83\x06\x00\x01t\t\x00i\n\x00d\x02\x00|\x03\x00|\x04\x00f\x02\x00\x16\x83\x01\x00\x01t\x04\x00|\x06\x00f\x02\x00Sn;\x00\x01t\x03\x00t\x0b\x00|\x00\x00|\x01\x00|\x02\x00|\x05\x00|\x06\x00\x83\x06\x00\x01t\t\x00i\n\x00d\x03\x00|\x03\x00|\x04\x00f\x02\x00\x16\x83\x01\x00\x01t\x0c\x00|\x06\x00f\x02\x00Sd\x00\x00S' (93 00 00 00 7C 03 00 7C 04 00 18 7D 06 00 7C 06 00 64 01 00 6A 04 00 6F 3E 00 01 74 03 00 74 04 00 7C 00 00 7C 01 00 7C 02 00 7C 05 00 7C 06 00 83 06 00 01 74 09 00 69 0A 00 64 02 00 7C 03 00 7C 04 00 66 02 00 16 83 01 00 01 74 04 00 7C 06 00 66 02 00 53 6E 3B 00 01 74 03 00 74 0B 00 7C 00 00 7C 01 00 7C 02 00 7C 05 00 7C 06 00 83 06 00 01 74 09 00 69 0A 00 64 03 00 7C 03 00 7C 04 00 66 02 00 16 83 01 00 01 74 0C 00 7C 06 00 66 02 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'success_chance'
                             00000003     7C - LOAD_FAST           'difficulty_rating'
                             00000006     18 - BINARY_SUBTRACT     
                             00000007     7D - STORE_FAST          'diff'
                             0000000A     7C - LOAD_FAST           'diff'
                             0000000D     64 - LOAD_CONST          0
                             00000010     6A - COMPARE_OP          ">"
                             00000013     6F - JUMP_IF_FALSE       -> 00000054
                             00000016     01 - POP_TOP             
                             00000017     74 - LOAD_GLOBAL         'SendVirusResultToAll'
                             0000001A     74 - LOAD_GLOBAL         'SUCCESS'
                             0000001D     7C - LOAD_FAST           'virus'
                             00000020     7C - LOAD_FAST           'subjectLocator'
                             00000023     7C - LOAD_FAST           'directobjectLocator'
                             00000026     7C - LOAD_FAST           'allow_success_msg'
                             00000029     7C - LOAD_FAST           'diff'
                             0000002C     83 - CALL_FUNCTION       r0006
                             0000002F     01 - POP_TOP             
                             00000030     74 - LOAD_GLOBAL         'Utility'
                             00000033     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000036     64 - LOAD_CONST          'DifficultyCheck: SUCCEEDED: %d > %d'
                             00000039     7C - LOAD_FAST           'success_chance'
                             0000003C     7C - LOAD_FAST           'difficulty_rating'
                             0000003F     66 - BUILD_TUPLE         r0002
                             00000042     16 - BINARY_MODULO       
                             00000043     83 - CALL_FUNCTION       r0001
                             00000046     01 - POP_TOP             
                             00000047     74 - LOAD_GLOBAL         'SUCCESS'
                             0000004A     7C - LOAD_FAST           'diff'
                             0000004D     66 - BUILD_TUPLE         r0002
                             00000050     53 - RETURN_VALUE        
                             00000051     6E - JUMP_FORWARD        -> 0000008F
                             00000054     01 - POP_TOP             
                             00000055     74 - LOAD_GLOBAL         'SendVirusResultToAll'
                             00000058     74 - LOAD_GLOBAL         'FAILURE'
                             0000005B     7C - LOAD_FAST           'virus'
                             0000005E     7C - LOAD_FAST           'subjectLocator'
                             00000061     7C - LOAD_FAST           'directobjectLocator'
                             00000064     7C - LOAD_FAST           'allow_success_msg'
                             00000067     7C - LOAD_FAST           'diff'
                             0000006A     83 - CALL_FUNCTION       r0006
                             0000006D     01 - POP_TOP             
                             0000006E     74 - LOAD_GLOBAL         'Utility'
                             00000071     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000074     64 - LOAD_CONST          'DifficultyCheck: DEFLECTED: %d > %d'
                             00000077     7C - LOAD_FAST           'success_chance'
                             0000007A     7C - LOAD_FAST           'difficulty_rating'
                             0000007D     66 - BUILD_TUPLE         r0002
                             00000080     16 - BINARY_MODULO       
                             00000081     83 - CALL_FUNCTION       r0001
                             00000084     01 - POP_TOP             
                             00000085     74 - LOAD_GLOBAL         'DEFLECTED'
                             00000088     7C - LOAD_FAST           'diff'
                             0000008B     66 - BUILD_TUPLE         r0002
                             0000008E     53 - RETURN_VALUE        
                             0000008F     64 - LOAD_CONST          None
                             00000092     53 - RETURN_VALUE        
                         consts:
00001360                     TUPLE: (
00001365                         None (4E),
00001366                         INT: 0 (00 00 00 00),
0000136B                         STR: 'DifficultyCheck: SUCCEEDED: %d > %d' (23 00 00 00 44 69 66 66 69 63 75 6C 74 79 43 68 65 63 6B 3A 20 53 55 43 43 45 45 44 45 44 3A 20 25 64 20 3E 20 25 64),
00001393                         STR: 'DifficultyCheck: DEFLECTED: %d > %d' (23 00 00 00 44 69 66 66 69 63 75 6C 74 79 43 68 65 63 6B 3A 20 44 45 46 4C 45 43 54 45 44 3A 20 25 64 20 3E 20 25 64)
                             )
                         names:
000013BB                     TUPLE: (
000013C0                         STR: 'success_chance' (0E 00 00 00 73 75 63 63 65 73 73 5F 63 68 61 6E 63 65),
000013D3                         STR: 'difficulty_rating' (11 00 00 00 64 69 66 66 69 63 75 6C 74 79 5F 72 61 74 69 6E 67),
000013E9                         STR: 'diff' (04 00 00 00 64 69 66 66),
000013F2                         STR: 'SendVirusResultToAll' (14 00 00 00 53 65 6E 64 56 69 72 75 73 52 65 73 75 6C 74 54 6F 41 6C 6C),
0000140B                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00001417                         STR: 'virus' (05 00 00 00 76 69 72 75 73),
00001421                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00001434                         STR: 'directobjectLocator' (13 00 00 00 64 69 72 65 63 74 6F 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
0000144C                         STR: 'allow_success_msg' (11 00 00 00 61 6C 6C 6F 77 5F 73 75 63 63 65 73 73 5F 6D 73 67),
00001462                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
0000146E                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00001485                         STR: 'FAILURE' (07 00 00 00 46 41 49 4C 55 52 45),
00001491                         STR: 'DEFLECTED' (09 00 00 00 44 45 46 4C 45 43 54 45 44)
                             )
                         varnames:
0000149F                     TUPLE: (
000014A4                         STR: 'virus' (05 00 00 00 76 69 72 75 73),
000014AE                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
000014C1                         STR: 'directobjectLocator' (13 00 00 00 64 69 72 65 63 74 6F 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
000014D9                         STR: 'success_chance' (0E 00 00 00 73 75 63 63 65 73 73 5F 63 68 61 6E 63 65),
000014EC                         STR: 'difficulty_rating' (11 00 00 00 64 69 66 66 69 63 75 6C 74 79 5F 72 61 74 69 6E 67),
00001502                         STR: 'allow_success_msg' (11 00 00 00 61 6C 6C 6F 77 5F 73 75 63 63 65 73 73 5F 6D 73 67),
00001518                         STR: 'diff' (04 00 00 00 64 69 66 66)
                             )
                         freevars:
00001521                     TUPLE: ()
                         cellvars:
00001526                     TUPLE: ()
                         filename:
0000152B                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\virii_defines.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 76 69 72 69 69 5F 64 65 66 69 6E 65 73 2E 70 79)
                         name:
00001584                     STR: 'DifficultyCheck' (0F 00 00 00 44 69 66 66 69 63 75 6C 74 79 43 68 65 63 6B)
                         firslineno:
00001598                     LONG: 158L (9E 00 00 00)
                         lnotab:
0000159C                     STR: '\x00\x02\n\x02\r\x01\x19\x02\x17\x01\x0e\x02\x19\x02\x17\x01' (10 00 00 00 00 02 0A 02 0D 01 19 02 17 01 0E 02 19 02 17 01),
000015B1             CODE:
                         argcount:
000015B2                     LONG: 7L (07 00 00 00)
                         nlocals:
000015B6                     LONG: 8L (08 00 00 00)
                         stacksize:
000015BA                     LONG: 7L (07 00 00 00)
                         flags:
000015BE                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000015C2                     STR: 't\x00\x00|\x03\x00|\x01\x00\x83\x02\x00t\x03\x00j\x02\x00oG\x00\x01t\x04\x00i\x05\x00|\x01\x00\x83\x01\x00}\x07\x00|\x06\x00o#\x00\x01t\x04\x00i\x08\x00t\t\x00i\n\x00|\x00\x00|\x02\x00|\x03\x00i\r\x00|\x07\x00\x83\x05\x00\x01n\x01\x00\x01t\x03\x00d\x01\x00f\x02\x00Sn\x01\x00\x01|\x04\x00t\x0f\x00i\x10\x00d\x02\x00\x83\x01\x007}\x04\x00t\x11\x00|\x00\x00|\x02\x00|\x03\x00i\r\x00|\x04\x00|\x05\x00|\x06\x00\x83\x06\x00Sd\x00\x00S' (90 00 00 00 74 00 00 7C 03 00 7C 01 00 83 02 00 74 03 00 6A 02 00 6F 47 00 01 74 04 00 69 05 00 7C 01 00 83 01 00 7D 07 00 7C 06 00 6F 23 00 01 74 04 00 69 08 00 74 09 00 69 0A 00 7C 00 00 7C 02 00 7C 03 00 69 0D 00 7C 07 00 83 05 00 01 6E 01 00 01 74 03 00 64 01 00 66 02 00 53 6E 01 00 01 7C 04 00 74 0F 00 69 10 00 64 02 00 83 01 00 37 7D 04 00 74 11 00 7C 00 00 7C 02 00 7C 03 00 69 0D 00 7C 04 00 7C 05 00 7C 06 00 83 06 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'VaccinationCheck'
                             00000003     7C - LOAD_FAST           'directobject'
                             00000006     7C - LOAD_FAST           'vaccination'
                             00000009     83 - CALL_FUNCTION       r0002
                             0000000C     74 - LOAD_GLOBAL         'DEFLECTED'
                             0000000F     6A - COMPARE_OP          "=="
                             00000012     6F - JUMP_IF_FALSE       -> 0000005C
                             00000015     01 - POP_TOP             
                             00000016     74 - LOAD_GLOBAL         'Utility'
                             00000019     69 - LOAD_ATTR           'GetAbilityInfoID'
                             0000001C     7C - LOAD_FAST           'vaccination'
                             0000001F     83 - CALL_FUNCTION       r0001
                             00000022     7D - STORE_FAST          'vaccination_name_id'
                             00000025     7C - LOAD_FAST           'allow_success_msg'
                             00000028     6F - JUMP_IF_FALSE       -> 0000004E
                             0000002B     01 - POP_TOP             
                             0000002C     74 - LOAD_GLOBAL         'Utility'
                             0000002F     69 - LOAD_ATTR           'SendAbilityOutputToAll'
                             00000032     74 - LOAD_GLOBAL         'StringTable'
                             00000035     69 - LOAD_ATTR           'ID_CLIENT_ABILITY_VIRUS_VACCINATED'
                             00000038     7C - LOAD_FAST           'virus'
                             0000003B     7C - LOAD_FAST           'subjectLocator'
                             0000003E     7C - LOAD_FAST           'directobject'
                             00000041     69 - LOAD_ATTR           'locator'
                             00000044     7C - LOAD_FAST           'vaccination_name_id'
                             00000047     83 - CALL_FUNCTION       r0005
                             0000004A     01 - POP_TOP             
                             0000004B     6E - JUMP_FORWARD        -> 0000004F
                             0000004E     01 - POP_TOP             
                             0000004F     74 - LOAD_GLOBAL         'DEFLECTED'
                             00000052     64 - LOAD_CONST          0
                             00000055     66 - BUILD_TUPLE         r0002
                             00000058     53 - RETURN_VALUE        
                             00000059     6E - JUMP_FORWARD        -> 0000005D
                             0000005C     01 - POP_TOP             
                             0000005D     7C - LOAD_FAST           'success_chance'
                             00000060     74 - LOAD_GLOBAL         'random'
                             00000063     69 - LOAD_ATTR           'randrange'
                             00000066     64 - LOAD_CONST          100
                             00000069     83 - CALL_FUNCTION       r0001
                             0000006C     37 - INPLACE_ADD         
                             0000006D     7D - STORE_FAST          'success_chance'
                             00000070     74 - LOAD_GLOBAL         'DifficultyCheck'
                             00000073     7C - LOAD_FAST           'virus'
                             00000076     7C - LOAD_FAST           'subjectLocator'
                             00000079     7C - LOAD_FAST           'directobject'
                             0000007C     69 - LOAD_ATTR           'locator'
                             0000007F     7C - LOAD_FAST           'success_chance'
                             00000082     7C - LOAD_FAST           'difficulty_rating'
                             00000085     7C - LOAD_FAST           'allow_success_msg'
                             00000088     83 - CALL_FUNCTION       r0006
                             0000008B     53 - RETURN_VALUE        
                             0000008C     64 - LOAD_CONST          None
                             0000008F     53 - RETURN_VALUE        
                         consts:
00001657                     TUPLE: (
0000165C                         None (4E),
0000165D                         INT: 0 (00 00 00 00),
00001662                         INT: 100 (64 00 00 00)
                             )
                         names:
00001667                     TUPLE: (
0000166C                         STR: 'VaccinationCheck' (10 00 00 00 56 61 63 63 69 6E 61 74 69 6F 6E 43 68 65 63 6B),
00001681                         STR: 'directobject' (0C 00 00 00 64 69 72 65 63 74 6F 62 6A 65 63 74),
00001692                         STR: 'vaccination' (0B 00 00 00 76 61 63 63 69 6E 61 74 69 6F 6E),
000016A2                         STR: 'DEFLECTED' (09 00 00 00 44 45 46 4C 45 43 54 45 44),
000016B0                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000016BC                         STR: 'GetAbilityInfoID' (10 00 00 00 47 65 74 41 62 69 6C 69 74 79 49 6E 66 6F 49 44),
000016D1                         STR: 'vaccination_name_id' (13 00 00 00 76 61 63 63 69 6E 61 74 69 6F 6E 5F 6E 61 6D 65 5F 69 64),
000016E9                         STR: 'allow_success_msg' (11 00 00 00 61 6C 6C 6F 77 5F 73 75 63 63 65 73 73 5F 6D 73 67),
000016FF                         STR: 'SendAbilityOutputToAll' (16 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 41 6C 6C),
0000171A                         STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
0000172A                         STR: 'ID_CLIENT_ABILITY_VIRUS_VACCINATED' (22 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 41 42 49 4C 49 54 59 5F 56 49 52 55 53 5F 56 41 43 43 49 4E 41 54 45 44),
00001751                         STR: 'virus' (05 00 00 00 76 69 72 75 73),
0000175B                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
0000176E                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
0000177A                         STR: 'success_chance' (0E 00 00 00 73 75 63 63 65 73 73 5F 63 68 61 6E 63 65),
0000178D                         STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00001798                         STR: 'randrange' (09 00 00 00 72 61 6E 64 72 61 6E 67 65),
000017A6                         STR: 'DifficultyCheck' (0F 00 00 00 44 69 66 66 69 63 75 6C 74 79 43 68 65 63 6B),
000017BA                         STR: 'difficulty_rating' (11 00 00 00 64 69 66 66 69 63 75 6C 74 79 5F 72 61 74 69 6E 67)
                             )
                         varnames:
000017D0                     TUPLE: (
000017D5                         STR: 'virus' (05 00 00 00 76 69 72 75 73),
000017DF                         STR: 'vaccination' (0B 00 00 00 76 61 63 63 69 6E 61 74 69 6F 6E),
000017EF                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00001802                         STR: 'directobject' (0C 00 00 00 64 69 72 65 63 74 6F 62 6A 65 63 74),
00001813                         STR: 'success_chance' (0E 00 00 00 73 75 63 63 65 73 73 5F 63 68 61 6E 63 65),
00001826                         STR: 'difficulty_rating' (11 00 00 00 64 69 66 66 69 63 75 6C 74 79 5F 72 61 74 69 6E 67),
0000183C                         STR: 'allow_success_msg' (11 00 00 00 61 6C 6C 6F 77 5F 73 75 63 63 65 73 73 5F 6D 73 67),
00001852                         STR: 'vaccination_name_id' (13 00 00 00 76 61 63 63 69 6E 61 74 69 6F 6E 5F 6E 61 6D 65 5F 69 64)
                             )
                         freevars:
0000186A                     TUPLE: ()
                         cellvars:
0000186F                     TUPLE: ()
                         filename:
00001874                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\virii_defines.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 76 69 72 69 69 5F 64 65 66 69 6E 65 73 2E 70 79)
                         name:
000018CD                     STR: 'MultiDifficultyCheck' (14 00 00 00 4D 75 6C 74 69 44 69 66 66 69 63 75 6C 74 79 43 68 65 63 6B)
                         firslineno:
000018E6                     LONG: 176L (B0 00 00 00)
                         lnotab:
000018EA                     STR: '\x00\x03\x16\x01\x0f\x01\x07\x01\x0f\x01\t\x01\x0b\x01\x0e\x03\x13\x02' (12 00 00 00 00 03 16 01 0F 01 07 01 0F 01 09 01 0B 01 0E 03 13 02),
00001901             CODE:
                         argcount:
00001902                     LONG: 3L (03 00 00 00)
                         nlocals:
00001906                     LONG: 3L (03 00 00 00)
                         stacksize:
0000190A                     LONG: 4L (04 00 00 00)
                         flags:
0000190E                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001912                     STR: 't\x00\x00|\x00\x00i\x02\x00\x83\x01\x00t\x03\x00j\x02\x00o-\x00\x01t\x04\x00i\x05\x00t\x06\x00i\x07\x00|\x01\x00|\x00\x00\x83\x03\x00\x01t\x03\x00|\x00\x00_\t\x00t\x03\x00d\x01\x00f\x02\x00Sn\x01\x00\x01t\n\x00|\x00\x00i\x02\x00\x83\x01\x00|\x00\x00_\t\x00t\x0b\x00d\x01\x00f\x02\x00Sd\x00\x00S' (63 00 00 00 74 00 00 7C 00 00 69 02 00 83 01 00 74 03 00 6A 02 00 6F 2D 00 01 74 04 00 69 05 00 74 06 00 69 07 00 7C 01 00 7C 00 00 83 03 00 01 74 03 00 7C 00 00 5F 09 00 74 03 00 64 01 00 66 02 00 53 6E 01 00 01 74 0A 00 7C 00 00 69 02 00 83 01 00 7C 00 00 5F 09 00 74 0B 00 64 01 00 66 02 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'ProgramLauncherCheck'
                             00000003     7C - LOAD_FAST           'sentence'
                             00000006     69 - LOAD_ATTR           'subject'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     74 - LOAD_GLOBAL         'FAILURE'
                             0000000F     6A - COMPARE_OP          "=="
                             00000012     6F - JUMP_IF_FALSE       -> 00000042
                             00000015     01 - POP_TOP             
                             00000016     74 - LOAD_GLOBAL         'Utility'
                             00000019     69 - LOAD_ATTR           'SendAbilityOutputToCasterSentence'
                             0000001C     74 - LOAD_GLOBAL         'StringTable'
                             0000001F     69 - LOAD_ATTR           'ID_CLIENT_ABILITY_PROGRAM_LAUNCHER_NOT_EQUIPPED'
                             00000022     7C - LOAD_FAST           'virus'
                             00000025     7C - LOAD_FAST           'sentence'
                             00000028     83 - CALL_FUNCTION       r0003
                             0000002B     01 - POP_TOP             
                             0000002C     74 - LOAD_GLOBAL         'FAILURE'
                             0000002F     7C - LOAD_FAST           'sentence'
                             00000032     5F - STORE_ATTR          'result'
                             00000035     74 - LOAD_GLOBAL         'FAILURE'
                             00000038     64 - LOAD_CONST          0
                             0000003B     66 - BUILD_TUPLE         r0002
                             0000003E     53 - RETURN_VALUE        
                             0000003F     6E - JUMP_FORWARD        -> 00000043
                             00000042     01 - POP_TOP             
                             00000043     74 - LOAD_GLOBAL         'MultiSuccessRating'
                             00000046     7C - LOAD_FAST           'sentence'
                             00000049     69 - LOAD_ATTR           'subject'
                             0000004C     83 - CALL_FUNCTION       r0001
                             0000004F     7C - LOAD_FAST           'sentence'
                             00000052     5F - STORE_ATTR          'result'
                             00000055     74 - LOAD_GLOBAL         'SUCCESS'
                             00000058     64 - LOAD_CONST          0
                             0000005B     66 - BUILD_TUPLE         r0002
                             0000005E     53 - RETURN_VALUE        
                             0000005F     64 - LOAD_CONST          None
                             00000062     53 - RETURN_VALUE        
                         consts:
0000197A                     TUPLE: (
0000197F                         None (4E),
00001980                         INT: 0 (00 00 00 00)
                             )
                         names:
00001985                     TUPLE: (
0000198A                         STR: 'ProgramLauncherCheck' (14 00 00 00 50 72 6F 67 72 61 6D 4C 61 75 6E 63 68 65 72 43 68 65 63 6B),
000019A3                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65),
000019B0                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000019BC                         STR: 'FAILURE' (07 00 00 00 46 41 49 4C 55 52 45),
000019C8                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000019D4                         STR: 'SendAbilityOutputToCasterSentence' (21 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 43 61 73 74 65 72 53 65 6E 74 65 6E 63 65),
000019FA                         STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00001A0A                         STR: 'ID_CLIENT_ABILITY_PROGRAM_LAUNCHER_NOT_EQUIPPED' (2F 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 41 42 49 4C 49 54 59 5F 50 52 4F 47 52 41 4D 5F 4C 41 55 4E 43 48 45 52 5F 4E 4F 54 5F 45 51 55 49 50 50 45 44),
00001A3E                         STR: 'virus' (05 00 00 00 76 69 72 75 73),
00001A48                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00001A53                         STR: 'MultiSuccessRating' (12 00 00 00 4D 75 6C 74 69 53 75 63 63 65 73 73 52 61 74 69 6E 67),
00001A6A                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53)
                             )
                         varnames:
00001A76                     TUPLE: (
00001A7B                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65),
00001A88                         STR: 'virus' (05 00 00 00 76 69 72 75 73),
00001A92                         STR: 'vaccination' (0B 00 00 00 76 61 63 63 69 6E 61 74 69 6F 6E)
                             )
                         freevars:
00001AA2                     TUPLE: ()
                         cellvars:
00001AA7                     TUPLE: ()
                         filename:
00001AAC                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\virii_defines.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 76 69 72 69 69 5F 64 65 66 69 6E 65 73 2E 70 79)
                         name:
00001B05                     STR: 'MultVirusSuccessCheck' (15 00 00 00 4D 75 6C 74 56 69 72 75 73 53 75 63 63 65 73 73 43 68 65 63 6B)
                         firslineno:
00001B1F                     LONG: 198L (C6 00 00 00)
                         lnotab:
00001B23                     STR: '\x00\x03\x16\x01\x16\x01\t\x01\x0e\x03\x12\x01' (0C 00 00 00 00 03 16 01 16 01 09 01 0E 03 12 01)
                 )
             names:
00001B34         TUPLE: (
00001B39             STR: 'ability.utility' (0F 00 00 00 61 62 69 6C 69 74 79 2E 75 74 69 6C 69 74 79),
00001B4D             STR: 'utility' (07 00 00 00 75 74 69 6C 69 74 79),
00001B59             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00001B65             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00001B70             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00001B7E             STR: 'ability.defines' (0F 00 00 00 61 62 69 6C 69 74 79 2E 64 65 66 69 6E 65 73),
00001B92             STR: 'stringtable_client' (12 00 00 00 73 74 72 69 6E 67 74 61 62 6C 65 5F 63 6C 69 65 6E 74),
00001BA9             STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00001BB9             STR: 'VIRII_LEVEL_1_DURATION' (16 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 31 5F 44 55 52 41 54 49 4F 4E),
00001BD4             STR: 'VIRII_LEVEL_2_DURATION' (16 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 32 5F 44 55 52 41 54 49 4F 4E),
00001BEF             STR: 'VIRII_LEVEL_3_DURATION' (16 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 33 5F 44 55 52 41 54 49 4F 4E),
00001C0A             STR: 'VIRII_MULTI_DURATION' (14 00 00 00 56 49 52 49 49 5F 4D 55 4C 54 49 5F 44 55 52 41 54 49 4F 4E),
00001C23             STR: 'VIRII_LEVEL_1_DEBUFF' (14 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 31 5F 44 45 42 55 46 46),
00001C3C             STR: 'VIRII_LEVEL_2_DEBUFF' (14 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 32 5F 44 45 42 55 46 46),
00001C55             STR: 'VIRII_LEVEL_3_DEBUFF' (14 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 33 5F 44 45 42 55 46 46),
00001C6E             STR: 'VIRII_LEVEL_1_BUFF' (12 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 31 5F 42 55 46 46),
00001C85             STR: 'VIRII_LEVEL_2_BUFF' (12 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 32 5F 42 55 46 46),
00001C9C             STR: 'VIRII_LEVEL_3_BUFF' (12 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 33 5F 42 55 46 46),
00001CB3             STR: 'VIRII_LEVEL_1_RANGE' (13 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 31 5F 52 41 4E 47 45),
00001CCB             STR: 'VIRII_LEVEL_2_RANGE' (13 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 32 5F 52 41 4E 47 45),
00001CE3             STR: 'VIRII_LEVEL_3_RANGE' (13 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 33 5F 52 41 4E 47 45),
00001CFB             STR: 'True' (04 00 00 00 54 72 75 65),
00001D04             STR: 'SendVirusResultToAll' (14 00 00 00 53 65 6E 64 56 69 72 75 73 52 65 73 75 6C 74 54 6F 41 6C 6C),
00001D1D             STR: 'False' (05 00 00 00 46 61 6C 73 65),
00001D27             STR: 'VirusSuccessCheck' (11 00 00 00 56 69 72 75 73 53 75 63 63 65 73 73 43 68 65 63 6B),
00001D3D             STR: 'ProgramLauncherCheck' (14 00 00 00 50 72 6F 67 72 61 6D 4C 61 75 6E 63 68 65 72 43 68 65 63 6B),
00001D56             STR: 'VaccinationCheck' (10 00 00 00 56 61 63 63 69 6E 61 74 69 6F 6E 43 68 65 63 6B),
00001D6B             STR: 'ReflectionCheck' (0F 00 00 00 52 65 66 6C 65 63 74 69 6F 6E 43 68 65 63 6B),
00001D7F             STR: 'CalcDifficultyValue' (13 00 00 00 43 61 6C 63 44 69 66 66 69 63 75 6C 74 79 56 61 6C 75 65),
00001D97             STR: 'CalcSuccessRating' (11 00 00 00 43 61 6C 63 53 75 63 63 65 73 73 52 61 74 69 6E 67),
00001DAD             STR: 'SingleSuccessRating' (13 00 00 00 53 69 6E 67 6C 65 53 75 63 63 65 73 73 52 61 74 69 6E 67),
00001DC5             STR: 'MultiSuccessRating' (12 00 00 00 4D 75 6C 74 69 53 75 63 63 65 73 73 52 61 74 69 6E 67),
00001DDC             STR: 'DifficultyCheck' (0F 00 00 00 44 69 66 66 69 63 75 6C 74 79 43 68 65 63 6B),
00001DF0             STR: 'MultiDifficultyCheck' (14 00 00 00 4D 75 6C 74 69 44 69 66 66 69 63 75 6C 74 79 43 68 65 63 6B),
00001E09             STR: 'MultVirusSuccessCheck' (15 00 00 00 4D 75 6C 74 56 69 72 75 73 53 75 63 63 65 73 73 43 68 65 63 6B)
                 )
             varnames:
00001E23         TUPLE: (
00001E28             STR: 'VIRII_LEVEL_3_DEBUFF' (14 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 33 5F 44 45 42 55 46 46),
00001E41             STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00001E51             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00001E5C             STR: 'VIRII_LEVEL_2_RANGE' (13 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 32 5F 52 41 4E 47 45),
00001E74             STR: 'VIRII_LEVEL_3_DURATION' (16 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 33 5F 44 55 52 41 54 49 4F 4E),
00001E8F             STR: 'ProgramLauncherCheck' (14 00 00 00 50 72 6F 67 72 61 6D 4C 61 75 6E 63 68 65 72 43 68 65 63 6B),
00001EA8             STR: 'VIRII_LEVEL_2_BUFF' (12 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 32 5F 42 55 46 46),
00001EBF             STR: 'ReflectionCheck' (0F 00 00 00 52 65 66 6C 65 63 74 69 6F 6E 43 68 65 63 6B),
00001ED3             STR: 'DifficultyCheck' (0F 00 00 00 44 69 66 66 69 63 75 6C 74 79 43 68 65 63 6B),
00001EE7             STR: 'MultiSuccessRating' (12 00 00 00 4D 75 6C 74 69 53 75 63 63 65 73 73 52 61 74 69 6E 67),
00001EFE             STR: 'SingleSuccessRating' (13 00 00 00 53 69 6E 67 6C 65 53 75 63 63 65 73 73 52 61 74 69 6E 67),
00001F16             STR: 'SendVirusResultToAll' (14 00 00 00 53 65 6E 64 56 69 72 75 73 52 65 73 75 6C 74 54 6F 41 6C 6C),
00001F2F             STR: 'MultVirusSuccessCheck' (15 00 00 00 4D 75 6C 74 56 69 72 75 73 53 75 63 63 65 73 73 43 68 65 63 6B),
00001F49             STR: 'VIRII_LEVEL_2_DEBUFF' (14 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 32 5F 44 45 42 55 46 46),
00001F62             STR: 'CalcDifficultyValue' (13 00 00 00 43 61 6C 63 44 69 66 66 69 63 75 6C 74 79 56 61 6C 75 65),
00001F7A             STR: 'VIRII_LEVEL_1_DEBUFF' (14 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 31 5F 44 45 42 55 46 46),
00001F93             STR: 'VIRII_LEVEL_1_RANGE' (13 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 31 5F 52 41 4E 47 45),
00001FAB             STR: 'VirusSuccessCheck' (11 00 00 00 56 69 72 75 73 53 75 63 63 65 73 73 43 68 65 63 6B),
00001FC1             STR: 'VIRII_LEVEL_3_BUFF' (12 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 33 5F 42 55 46 46),
00001FD8             STR: 'VIRII_LEVEL_1_BUFF' (12 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 31 5F 42 55 46 46),
00001FEF             STR: 'VIRII_MULTI_DURATION' (14 00 00 00 56 49 52 49 49 5F 4D 55 4C 54 49 5F 44 55 52 41 54 49 4F 4E),
00002008             STR: 'CalcSuccessRating' (11 00 00 00 43 61 6C 63 53 75 63 63 65 73 73 52 61 74 69 6E 67),
0000201E             STR: 'VaccinationCheck' (10 00 00 00 56 61 63 63 69 6E 61 74 69 6F 6E 43 68 65 63 6B),
00002033             STR: 'MultiDifficultyCheck' (14 00 00 00 4D 75 6C 74 69 44 69 66 66 69 63 75 6C 74 79 43 68 65 63 6B),
0000204C             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
0000205A             STR: 'VIRII_LEVEL_3_RANGE' (13 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 33 5F 52 41 4E 47 45),
00002072             STR: 'VIRII_LEVEL_2_DURATION' (16 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 32 5F 44 55 52 41 54 49 4F 4E),
0000208D             STR: 'VIRII_LEVEL_1_DURATION' (16 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 31 5F 44 55 52 41 54 49 4F 4E),
000020A8             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79)
                 )
             freevars:
000020B4         TUPLE: ()
             cellvars:
000020B9         TUPLE: ()
             filename:
000020BE         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\virii_defines.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 76 69 72 69 69 5F 64 65 66 69 6E 65 73 2E 70 79)
             name:
00002117         STR: '?' (01 00 00 00 3F)
             firslineno:
0000211D         LONG: 1L (01 00 00 00)
             lnotab:
00002121         STR: '\x0c\x01\t\x01\t\x01\x07\x01\t\x03\x06\x01\x06\x01\x06\x03\x06\x03\x06\x01\x06\x01\x06\x03\x06\x01\x06\x01\x06\x03\x06\x01\x06\x01\x06\x05\x0f\x0e\x0c\x1c\t\t\t\x0f\t\x11\t\x12\t\n\t\x06\t\x08\t\x12\x0c\x16' (3A 00 00 00 0C 01 09 01 09 01 07 01 09 03 06 01 06 01 06 03 06 03 06 01 06 01 06 03 06 01 06 01 06 03 06 01 06 01 06 05 0F 0E 0C 1C 09 09 09 0F 09 11 09 12 09 0A 09 06 09 08 09 12 0C 16)

