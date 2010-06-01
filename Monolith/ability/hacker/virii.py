--== Disasm ==--
00000008 CODE:
             argcount:
00000009         LONG: 0L (00 00 00 00)
             nlocals:
0000000D         LONG: 0L (00 00 00 00)
             stacksize:
00000011         LONG: 2L (02 00 00 00)
             flags:
00000015         LONG: 64L (40 00 00 00)
                 (NOFREE)
             code:
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00Z\x02\x00d\x00\x00k\x03\x00Z\x04\x00d\x00\x00k\x05\x00Z\x06\x00d\x00\x00k\x07\x00Z\x08\x00d\x00\x00k\t\x00Z\n\x00d\x00\x00k\x0b\x00i\x0c\x00Z\r\x00d\x01\x00k\x0b\x00l\x0e\x00Z\x0e\x00\x01d\x02\x00k\x0f\x00Td\x00\x00k\x10\x00Z\x11\x00d\x00\x00k\x12\x00i\x13\x00Z\x14\x00d\x00\x00k\x15\x00Z\x16\x00e\x16\x00i\x17\x00Z\x18\x00e\x16\x00i\x19\x00Z\x1a\x00e\x16\x00i\x1b\x00Z\x1c\x00e\x16\x00i\x17\x00Z\x1d\x00e\x16\x00i\x19\x00Z\x1e\x00e\x16\x00i\x19\x00Z\x1f\x00d\x03\x00Z \x00d\x04\x00Z!\x00d\x05\x00Z"\x00d\x06\x00Z#\x00d\x07\x00\x84\x00\x00Z$\x00d\x08\x00\x84\x00\x00Z%\x00d\t\x00\x84\x00\x00Z&\x00d\x00\x00S' (EA 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 5A 02 00 64 00 00 6B 03 00 5A 04 00 64 00 00 6B 05 00 5A 06 00 64 00 00 6B 07 00 5A 08 00 64 00 00 6B 09 00 5A 0A 00 64 00 00 6B 0B 00 69 0C 00 5A 0D 00 64 01 00 6B 0B 00 6C 0E 00 5A 0E 00 01 64 02 00 6B 0F 00 54 64 00 00 6B 10 00 5A 11 00 64 00 00 6B 12 00 69 13 00 5A 14 00 64 00 00 6B 15 00 5A 16 00 65 16 00 69 17 00 5A 18 00 65 16 00 69 19 00 5A 1A 00 65 16 00 69 1B 00 5A 1C 00 65 16 00 69 17 00 5A 1D 00 65 16 00 69 19 00 5A 1E 00 65 16 00 69 19 00 5A 1F 00 64 03 00 5A 20 00 64 04 00 5A 21 00 64 05 00 5A 22 00 64 06 00 5A 23 00 64 07 00 84 00 00 5A 24 00 64 08 00 84 00 00 5A 25 00 64 09 00 84 00 00 5A 26 00 64 00 00 53)
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
                 00000027     6B - IMPORT_NAME         'missionvalidate'
                 0000002A     5A - STORE_NAME          'mv'
                 0000002D     64 - LOAD_CONST          None
                 00000030     6B - IMPORT_NAME         'combatvalidate'
                 00000033     5A - STORE_NAME          'cv'
                 00000036     64 - LOAD_CONST          None
                 00000039     6B - IMPORT_NAME         'stringtable_client'
                 0000003C     5A - STORE_NAME          'StringTable'
                 0000003F     64 - LOAD_CONST          None
                 00000042     6B - IMPORT_NAME         'ability.utility'
                 00000045     69 - LOAD_ATTR           'utility'
                 00000048     5A - STORE_NAME          'Utility'
                 0000004B     64 - LOAD_CONST          ('getAbilityName')
                 0000004E     6B - IMPORT_NAME         'ability.utility'
                 00000051     6C - IMPORT_FROM         'getAbilityName'
                 00000054     5A - STORE_NAME          'getAbilityName'
                 00000057     01 - POP_TOP             
                 00000058     64 - LOAD_CONST          ('*')
                 0000005B     6B - IMPORT_NAME         'ability.defines'
                 0000005E     54 - IMPORT_STAR         
                 0000005F     64 - LOAD_CONST          None
                 00000062     6B - IMPORT_NAME         'ltfxmap'
                 00000065     5A - STORE_NAME          'FX'
                 00000068     64 - LOAD_CONST          None
                 0000006B     6B - IMPORT_NAME         'ability.effects'
                 0000006E     69 - LOAD_ATTR           'effects'
                 00000071     5A - STORE_NAME          'EFFECTS'
                 00000074     64 - LOAD_CONST          None
                 00000077     6B - IMPORT_NAME         'virii_defines'
                 0000007A     5A - STORE_NAME          'VIRII'
                 0000007D     65 - LOAD_NAME           'VIRII'
                 00000080     69 - LOAD_ATTR           'VIRII_LEVEL_1_DURATION'
                 00000083     5A - STORE_NAME          'AFFECTVISION1_TIME'
                 00000086     65 - LOAD_NAME           'VIRII'
                 00000089     69 - LOAD_ATTR           'VIRII_LEVEL_2_DURATION'
                 0000008C     5A - STORE_NAME          'AFFECTVISION2_TIME'
                 0000008F     65 - LOAD_NAME           'VIRII'
                 00000092     69 - LOAD_ATTR           'VIRII_LEVEL_3_DURATION'
                 00000095     5A - STORE_NAME          'AFFECTVISION3_TIME'
                 00000098     65 - LOAD_NAME           'VIRII'
                 0000009B     69 - LOAD_ATTR           'VIRII_LEVEL_1_DURATION'
                 0000009E     5A - STORE_NAME          'MOVEMENTDISRUPT1_TIME'
                 000000A1     65 - LOAD_NAME           'VIRII'
                 000000A4     69 - LOAD_ATTR           'VIRII_LEVEL_2_DURATION'
                 000000A7     5A - STORE_NAME          'MOVEMENTDISRUPT2_TIME'
                 000000AA     65 - LOAD_NAME           'VIRII'
                 000000AD     69 - LOAD_ATTR           'VIRII_LEVEL_2_DURATION'
                 000000B0     5A - STORE_NAME          'MOVEMENTDISRUPT3_TIME'
                 000000B3     64 - LOAD_CONST          500
                 000000B6     5A - STORE_NAME          'DISABLEABILITY1_TIME'
                 000000B9     64 - LOAD_CONST          25
                 000000BC     5A - STORE_NAME          'MOVEMENTDISRUPT1_EFFECT'
                 000000BF     64 - LOAD_CONST          50
                 000000C2     5A - STORE_NAME          'MOVEMENTDISRUPT2_EFFECT'
                 000000C5     64 - LOAD_CONST          75
                 000000C8     5A - STORE_NAME          'MOVEMENTDISRUPT3_EFFECT'
                 000000CB     64 - LOAD_CONST          CODE('DeflectBullets1Effect_DirectObject')
                 000000CE     84 - MAKE_FUNCTION       r0000
                 000000D1     5A - STORE_NAME          'DeflectBullets1Effect_DirectObject'
                 000000D4     64 - LOAD_CONST          CODE('DeflectVirus1Effect_DirectObject')
                 000000D7     84 - MAKE_FUNCTION       r0000
                 000000DA     5A - STORE_NAME          'DeflectVirus1Effect_DirectObject'
                 000000DD     64 - LOAD_CONST          CODE('GenericCorruption')
                 000000E0     84 - MAKE_FUNCTION       r0000
                 000000E3     5A - STORE_NAME          'GenericCorruption'
                 000000E6     64 - LOAD_CONST          None
                 000000E9     53 - RETURN_VALUE        
             consts:
00000108         TUPLE: (
0000010D             None (4E),
0000010E             TUPLE: (
00000113                 STR: 'getAbilityName' (0E 00 00 00 67 65 74 41 62 69 6C 69 74 79 4E 61 6D 65)
                     ),
00000126             TUPLE: (
0000012B                 STR: '*' (01 00 00 00 2A)
                     ),
00000131             INT: 500 (F4 01 00 00),
00000136             INT: 25 (19 00 00 00),
0000013B             INT: 50 (32 00 00 00),
00000140             INT: 75 (4B 00 00 00),
00000145             CODE:
                         argcount:
00000146                     LONG: 2L (02 00 00 00)
                         nlocals:
0000014A                     LONG: 3L (03 00 00 00)
                         stacksize:
0000014E                     LONG: 8L (08 00 00 00)
                         flags:
00000152                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000156                     STR: 't\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01d\x02\x00d\x03\x00d\x02\x00d\x02\x00f\x04\x00}\x02\x00|\x00\x00i\x04\x00i\x05\x00|\x02\x00t\x06\x00t\x06\x00d\x04\x00d\x05\x00d\x05\x00t\x07\x00i\x08\x00\x83\x07\x00\x01d\x00\x00S' (48 00 00 00 74 00 00 69 01 00 64 01 00 83 01 00 01 64 02 00 64 03 00 64 02 00 64 02 00 66 04 00 7D 02 00 7C 00 00 69 04 00 69 05 00 7C 02 00 74 06 00 74 06 00 64 04 00 64 05 00 64 05 00 74 07 00 69 08 00 83 07 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'DeflectBullets1: DirectObject'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     01 - POP_TOP             
                             0000000D     64 - LOAD_CONST          ''
                             00000010     64 - LOAD_CONST          'PlayFX'
                             00000013     64 - LOAD_CONST          ''
                             00000016     64 - LOAD_CONST          ''
                             00000019     66 - BUILD_TUPLE         r0004
                             0000001C     7D - STORE_FAST          'procs'
                             0000001F     7C - LOAD_FAST           'subject'
                             00000022     69 - LOAD_ATTR           'AbilityInv'
                             00000025     69 - LOAD_ATTR           'addTempModProcs'
                             00000028     7C - LOAD_FAST           'procs'
                             0000002B     74 - LOAD_GLOBAL         'DeflectBullets1Ability'
                             0000002E     74 - LOAD_GLOBAL         'DeflectBullets1Ability'
                             00000031     64 - LOAD_CONST          0.20000000000000001
                             00000034     64 - LOAD_CONST          0
                             00000037     64 - LOAD_CONST          0
                             0000003A     74 - LOAD_GLOBAL         'FX'
                             0000003D     69 - LOAD_ATTR           'FX_VIRUSCAST_SPLIT_DEFLECT_BULLETS_DEFLECTBULLETS1'
                             00000040     83 - CALL_FUNCTION       r0007
                             00000043     01 - POP_TOP             
                             00000044     64 - LOAD_CONST          None
                             00000047     53 - RETURN_VALUE        
                         consts:
000001A3                     TUPLE: (
000001A8                         None (4E),
000001A9                         STR: 'DeflectBullets1: DirectObject' (1D 00 00 00 44 65 66 6C 65 63 74 42 75 6C 6C 65 74 73 31 3A 20 44 69 72 65 63 74 4F 62 6A 65 63 74),
000001CB                         STR: '' (00 00 00 00),
000001D0                         STR: 'PlayFX' (06 00 00 00 50 6C 61 79 46 58),
000001DB                         FLOAT: 0.20000000000000001 (13 30 2E 32 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 31),
000001F0                         INT: 0 (00 00 00 00)
                             )
                         names:
000001F5                     TUPLE: (
000001FA                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000206                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
0000021D                         STR: 'procs' (05 00 00 00 70 72 6F 63 73),
00000227                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000233                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
00000242                         STR: 'addTempModProcs' (0F 00 00 00 61 64 64 54 65 6D 70 4D 6F 64 50 72 6F 63 73),
00000256                         STR: 'DeflectBullets1Ability' (16 00 00 00 44 65 66 6C 65 63 74 42 75 6C 6C 65 74 73 31 41 62 69 6C 69 74 79),
00000271                         STR: 'FX' (02 00 00 00 46 58),
00000278                         STR: 'FX_VIRUSCAST_SPLIT_DEFLECT_BULLETS_DEFLECTBULLETS1' (32 00 00 00 46 58 5F 56 49 52 55 53 43 41 53 54 5F 53 50 4C 49 54 5F 44 45 46 4C 45 43 54 5F 42 55 4C 4C 45 54 53 5F 44 45 46 4C 45 43 54 42 55 4C 4C 45 54 53 31)
                             )
                         varnames:
000002AF                     TUPLE: (
000002B4                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000002C0                         STR: 'msg' (03 00 00 00 6D 73 67),
000002C8                         STR: 'procs' (05 00 00 00 70 72 6F 63 73)
                             )
                         freevars:
000002D2                     TUPLE: ()
                         cellvars:
000002D7                     TUPLE: ()
                         filename:
000002DC                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\virii.py' (4C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 76 69 72 69 69 2E 70 79)
                         name:
0000032D                     STR: 'DeflectBullets1Effect_DirectObject' (22 00 00 00 44 65 66 6C 65 63 74 42 75 6C 6C 65 74 73 31 45 66 66 65 63 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000354                     LONG: 47L (2F 00 00 00)
                         lnotab:
00000358                     STR: '\x00\x01\r\x02\x12\x01' (06 00 00 00 00 01 0D 02 12 01),
00000363             CODE:
                         argcount:
00000364                     LONG: 2L (02 00 00 00)
                         nlocals:
00000368                     LONG: 3L (03 00 00 00)
                         stacksize:
0000036C                     LONG: 8L (08 00 00 00)
                         flags:
00000370                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000374                     STR: 't\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01d\x02\x00d\x03\x00d\x02\x00d\x02\x00f\x04\x00}\x02\x00|\x00\x00i\x04\x00i\x05\x00|\x02\x00t\x06\x00t\x06\x00d\x04\x00d\x05\x00d\x05\x00t\x07\x00i\x08\x00\x83\x07\x00\x01d\x00\x00S' (48 00 00 00 74 00 00 69 01 00 64 01 00 83 01 00 01 64 02 00 64 03 00 64 02 00 64 02 00 66 04 00 7D 02 00 7C 00 00 69 04 00 69 05 00 7C 02 00 74 06 00 74 06 00 64 04 00 64 05 00 64 05 00 74 07 00 69 08 00 83 07 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'DeflectVirus1: DirectObject'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     01 - POP_TOP             
                             0000000D     64 - LOAD_CONST          ''
                             00000010     64 - LOAD_CONST          'PlayFX'
                             00000013     64 - LOAD_CONST          ''
                             00000016     64 - LOAD_CONST          ''
                             00000019     66 - BUILD_TUPLE         r0004
                             0000001C     7D - STORE_FAST          'procs'
                             0000001F     7C - LOAD_FAST           'subject'
                             00000022     69 - LOAD_ATTR           'AbilityInv'
                             00000025     69 - LOAD_ATTR           'addTempModProcs'
                             00000028     7C - LOAD_FAST           'procs'
                             0000002B     74 - LOAD_GLOBAL         'DeflectVirus1Ability'
                             0000002E     74 - LOAD_GLOBAL         'DeflectVirus1Ability'
                             00000031     64 - LOAD_CONST          0.20000000000000001
                             00000034     64 - LOAD_CONST          0
                             00000037     64 - LOAD_CONST          0
                             0000003A     74 - LOAD_GLOBAL         'FX'
                             0000003D     69 - LOAD_ATTR           'FX_VIRUSCAST_SPLIT_DEFLECT_VIRUS_DEFLECTVIRUS1'
                             00000040     83 - CALL_FUNCTION       r0007
                             00000043     01 - POP_TOP             
                             00000044     64 - LOAD_CONST          None
                             00000047     53 - RETURN_VALUE        
                         consts:
000003C1                     TUPLE: (
000003C6                         None (4E),
000003C7                         STR: 'DeflectVirus1: DirectObject' (1B 00 00 00 44 65 66 6C 65 63 74 56 69 72 75 73 31 3A 20 44 69 72 65 63 74 4F 62 6A 65 63 74),
000003E7                         STR: '' (00 00 00 00),
000003EC                         STR: 'PlayFX' (06 00 00 00 50 6C 61 79 46 58),
000003F7                         FLOAT: 0.20000000000000001 (13 30 2E 32 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 31),
0000040C                         INT: 0 (00 00 00 00)
                             )
                         names:
00000411                     TUPLE: (
00000416                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000422                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000439                         STR: 'procs' (05 00 00 00 70 72 6F 63 73),
00000443                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000044F                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
0000045E                         STR: 'addTempModProcs' (0F 00 00 00 61 64 64 54 65 6D 70 4D 6F 64 50 72 6F 63 73),
00000472                         STR: 'DeflectVirus1Ability' (14 00 00 00 44 65 66 6C 65 63 74 56 69 72 75 73 31 41 62 69 6C 69 74 79),
0000048B                         STR: 'FX' (02 00 00 00 46 58),
00000492                         STR: 'FX_VIRUSCAST_SPLIT_DEFLECT_VIRUS_DEFLECTVIRUS1' (2E 00 00 00 46 58 5F 56 49 52 55 53 43 41 53 54 5F 53 50 4C 49 54 5F 44 45 46 4C 45 43 54 5F 56 49 52 55 53 5F 44 45 46 4C 45 43 54 56 49 52 55 53 31)
                             )
                         varnames:
000004C5                     TUPLE: (
000004CA                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000004D6                         STR: 'msg' (03 00 00 00 6D 73 67),
000004DE                         STR: 'procs' (05 00 00 00 70 72 6F 63 73)
                             )
                         freevars:
000004E8                     TUPLE: ()
                         cellvars:
000004ED                     TUPLE: ()
                         filename:
000004F2                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\virii.py' (4C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 76 69 72 69 69 2E 70 79)
                         name:
00000543                     STR: 'DeflectVirus1Effect_DirectObject' (20 00 00 00 44 65 66 6C 65 63 74 56 69 72 75 73 31 45 66 66 65 63 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000568                     LONG: 53L (35 00 00 00)
                         lnotab:
0000056C                     STR: '\x00\x01\r\x02\x12\x01' (06 00 00 00 00 01 0D 02 12 01),
00000577             CODE:
                         argcount:
00000578                     LONG: 2L (02 00 00 00)
                         nlocals:
0000057C                     LONG: 9L (09 00 00 00)
                         stacksize:
00000580                     LONG: 5L (05 00 00 00)
                         flags:
00000584                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000588                     STR: 'd\x01\x00d\x01\x00f\x02\x00}\x05\x00d\x01\x00}\x04\x00t\x02\x00i\x03\x00|\x00\x00\x83\x01\x00o=\x00\x01|\x00\x00i\x05\x00i\x06\x00\x83\x00\x00}\x03\x00|\x03\x00o\x19\x00\x01|\x00\x00i\x05\x00i\x06\x00\x83\x00\x00d\x02\x00f\x02\x00}\x05\x00q\xfd\x00\x01t\x08\x00d\x01\x00f\x02\x00Sn\x9f\x00\x01g\x00\x00}\x06\x00t\x02\x00i\n\x00|\x00\x00\x83\x01\x00}\x05\x00|\x05\x00o\x1d\x00\x01d\x02\x00}\x07\x00|\x06\x00i\x0c\x00|\x05\x00|\x07\x00f\x02\x00\x83\x01\x00\x01n\x01\x00\x01t\x02\x00i\r\x00|\x00\x00\x83\x01\x00}\x05\x00|\x05\x00o\x1d\x00\x01d\x03\x00}\x07\x00|\x06\x00i\x0c\x00|\x05\x00|\x07\x00f\x02\x00\x83\x01\x00\x01n\x01\x00\x01|\x06\x00\x0co\x1b\x00\x01t\x02\x00i\x0e\x00d\x04\x00\x83\x01\x00\x01t\x08\x00d\x01\x00f\x02\x00Sn\x01\x00\x01t\x02\x00i\x0f\x00|\x06\x00\x83\x01\x00}\x05\x00t\x02\x00i\x03\x00|\x00\x00\x83\x01\x00o\x0e\x00\x01|\x05\x00d\x01\x00\x19}\x04\x00n\x0e\x00\x01|\x05\x00d\x01\x00\x19i\x10\x00}\x04\x00t\x11\x00i\x12\x00d\x05\x00d\x06\x00\x83\x02\x00}\x08\x00t\x02\x00i\x0e\x00d\x07\x00|\x08\x00\r\x17d\x08\x00\x17\x83\x01\x00\x01|\x08\x00|\x01\x00j\x04\x00o1\x00\x01t\x02\x00i\x0e\x00d\t\x00|\x01\x00\r\x17d\n\x00\x17|\x05\x00d\x05\x00\x19\r\x17d\x0b\x00\x17\x83\x01\x00\x01t\x15\x00|\x04\x00f\x02\x00Sn\x01\x00\x01t\x16\x00i\x17\x00|\x00\x00|\x05\x00d\x01\x00\x19|\x05\x00d\x05\x00\x19\x83\x03\x00}\x02\x00|\x02\x00|\x04\x00f\x02\x00Sd\x00\x00S' (B9 01 00 00 64 01 00 64 01 00 66 02 00 7D 05 00 64 01 00 7D 04 00 74 02 00 69 03 00 7C 00 00 83 01 00 6F 3D 00 01 7C 00 00 69 05 00 69 06 00 83 00 00 7D 03 00 7C 03 00 6F 19 00 01 7C 00 00 69 05 00 69 06 00 83 00 00 64 02 00 66 02 00 7D 05 00 71 FD 00 01 74 08 00 64 01 00 66 02 00 53 6E 9F 00 01 67 00 00 7D 06 00 74 02 00 69 0A 00 7C 00 00 83 01 00 7D 05 00 7C 05 00 6F 1D 00 01 64 02 00 7D 07 00 7C 06 00 69 0C 00 7C 05 00 7C 07 00 66 02 00 83 01 00 01 6E 01 00 01 74 02 00 69 0D 00 7C 00 00 83 01 00 7D 05 00 7C 05 00 6F 1D 00 01 64 03 00 7D 07 00 7C 06 00 69 0C 00 7C 05 00 7C 07 00 66 02 00 83 01 00 01 6E 01 00 01 7C 06 00 0C 6F 1B 00 01 74 02 00 69 0E 00 64 04 00 83 01 00 01 74 08 00 64 01 00 66 02 00 53 6E 01 00 01 74 02 00 69 0F 00 7C 06 00 83 01 00 7D 05 00 74 02 00 69 03 00 7C 00 00 83 01 00 6F 0E 00 01 7C 05 00 64 01 00 19 7D 04 00 6E 0E 00 01 7C 05 00 64 01 00 19 69 10 00 7D 04 00 74 11 00 69 12 00 64 05 00 64 06 00 83 02 00 7D 08 00 74 02 00 69 0E 00 64 07 00 7C 08 00 0D 17 64 08 00 17 83 01 00 01 7C 08 00 7C 01 00 6A 04 00 6F 31 00 01 74 02 00 69 0E 00 64 09 00 7C 01 00 0D 17 64 0A 00 17 7C 05 00 64 05 00 19 0D 17 64 0B 00 17 83 01 00 01 74 15 00 7C 04 00 66 02 00 53 6E 01 00 01 74 16 00 69 17 00 7C 00 00 7C 05 00 64 01 00 19 7C 05 00 64 05 00 19 83 03 00 7D 02 00 7C 02 00 7C 04 00 66 02 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          0
                             00000003     64 - LOAD_CONST          0
                             00000006     66 - BUILD_TUPLE         r0002
                             00000009     7D - STORE_FAST          'item'
                             0000000C     64 - LOAD_CONST          0
                             0000000F     7D - STORE_FAST          'destoryed_item_ID'
                             00000012     74 - LOAD_GLOBAL         'Utility'
                             00000015     69 - LOAD_ATTR           'IsAnNPC'
                             00000018     7C - LOAD_FAST           'directobject'
                             0000001B     83 - CALL_FUNCTION       r0001
                             0000001E     6F - JUMP_IF_FALSE       -> 0000005E
                             00000021     01 - POP_TOP             
                             00000022     7C - LOAD_FAST           'directobject'
                             00000025     69 - LOAD_ATTR           'AI'
                             00000028     69 - LOAD_ATTR           'getWeapon'
                             0000002B     83 - CALL_FUNCTION       r0000
                             0000002E     7D - STORE_FAST          'weapon'
                             00000031     7C - LOAD_FAST           'weapon'
                             00000034     6F - JUMP_IF_FALSE       -> 00000050
                             00000037     01 - POP_TOP             
                             00000038     7C - LOAD_FAST           'directobject'
                             0000003B     69 - LOAD_ATTR           'AI'
                             0000003E     69 - LOAD_ATTR           'getWeapon'
                             00000041     83 - CALL_FUNCTION       r0000
                             00000044     64 - LOAD_CONST          109
                             00000047     66 - BUILD_TUPLE         r0002
                             0000004A     7D - STORE_FAST          'item'
                             0000004D     71 - JUMP_ABSOLUTE       -> 000000FD
                             00000050     01 - POP_TOP             
                             00000051     74 - LOAD_GLOBAL         'FAILURE'
                             00000054     64 - LOAD_CONST          0
                             00000057     66 - BUILD_TUPLE         r0002
                             0000005A     53 - RETURN_VALUE        
                             0000005B     6E - JUMP_FORWARD        -> 000000FD
                             0000005E     01 - POP_TOP             
                             0000005F     67 - BUILD_LIST          r0000
                             00000062     7D - STORE_FAST          'itemList'
                             00000065     74 - LOAD_GLOBAL         'Utility'
                             00000068     69 - LOAD_ATTR           'GetEquippedWeapon'
                             0000006B     7C - LOAD_FAST           'directobject'
                             0000006E     83 - CALL_FUNCTION       r0001
                             00000071     7D - STORE_FAST          'item'
                             00000074     7C - LOAD_FAST           'item'
                             00000077     6F - JUMP_IF_FALSE       -> 00000097
                             0000007A     01 - POP_TOP             
                             0000007B     64 - LOAD_CONST          109
                             0000007E     7D - STORE_FAST          'nSlot'
                             00000081     7C - LOAD_FAST           'itemList'
                             00000084     69 - LOAD_ATTR           'append'
                             00000087     7C - LOAD_FAST           'item'
                             0000008A     7C - LOAD_FAST           'nSlot'
                             0000008D     66 - BUILD_TUPLE         r0002
                             00000090     83 - CALL_FUNCTION       r0001
                             00000093     01 - POP_TOP             
                             00000094     6E - JUMP_FORWARD        -> 00000098
                             00000097     01 - POP_TOP             
                             00000098     74 - LOAD_GLOBAL         'Utility'
                             0000009B     69 - LOAD_ATTR           'GetEquippedHackerItem'
                             0000009E     7C - LOAD_FAST           'directobject'
                             000000A1     83 - CALL_FUNCTION       r0001
                             000000A4     7D - STORE_FAST          'item'
                             000000A7     7C - LOAD_FAST           'item'
                             000000AA     6F - JUMP_IF_FALSE       -> 000000CA
                             000000AD     01 - POP_TOP             
                             000000AE     64 - LOAD_CONST          110
                             000000B1     7D - STORE_FAST          'nSlot'
                             000000B4     7C - LOAD_FAST           'itemList'
                             000000B7     69 - LOAD_ATTR           'append'
                             000000BA     7C - LOAD_FAST           'item'
                             000000BD     7C - LOAD_FAST           'nSlot'
                             000000C0     66 - BUILD_TUPLE         r0002
                             000000C3     83 - CALL_FUNCTION       r0001
                             000000C6     01 - POP_TOP             
                             000000C7     6E - JUMP_FORWARD        -> 000000CB
                             000000CA     01 - POP_TOP             
                             000000CB     7C - LOAD_FAST           'itemList'
                             000000CE     0C - UNARY_NOT           
                             000000CF     6F - JUMP_IF_FALSE       -> 000000ED
                             000000D2     01 - POP_TOP             
                             000000D3     74 - LOAD_GLOBAL         'Utility'
                             000000D6     69 - LOAD_ATTR           'outputAbilityDebug'
                             000000D9     64 - LOAD_CONST          'GenericCorruption: Subject has no items to destroy.'
                             000000DC     83 - CALL_FUNCTION       r0001
                             000000DF     01 - POP_TOP             
                             000000E0     74 - LOAD_GLOBAL         'FAILURE'
                             000000E3     64 - LOAD_CONST          0
                             000000E6     66 - BUILD_TUPLE         r0002
                             000000E9     53 - RETURN_VALUE        
                             000000EA     6E - JUMP_FORWARD        -> 000000EE
                             000000ED     01 - POP_TOP             
                             000000EE     74 - LOAD_GLOBAL         'Utility'
                             000000F1     69 - LOAD_ATTR           'GetRandomListEntry'
                             000000F4     7C - LOAD_FAST           'itemList'
                             000000F7     83 - CALL_FUNCTION       r0001
                             000000FA     7D - STORE_FAST          'item'
                             000000FD     74 - LOAD_GLOBAL         'Utility'
                             00000100     69 - LOAD_ATTR           'IsAnNPC'
                             00000103     7C - LOAD_FAST           'directobject'
                             00000106     83 - CALL_FUNCTION       r0001
                             00000109     6F - JUMP_IF_FALSE       -> 0000011A
                             0000010C     01 - POP_TOP             
                             0000010D     7C - LOAD_FAST           'item'
                             00000110     64 - LOAD_CONST          0
                             00000113     19 - BINARY_SUBSCR       
                             00000114     7D - STORE_FAST          'destoryed_item_ID'
                             00000117     6E - JUMP_FORWARD        -> 00000128
                             0000011A     01 - POP_TOP             
                             0000011B     7C - LOAD_FAST           'item'
                             0000011E     64 - LOAD_CONST          0
                             00000121     19 - BINARY_SUBSCR       
                             00000122     69 - LOAD_ATTR           'type'
                             00000125     7D - STORE_FAST          'destoryed_item_ID'
                             00000128     74 - LOAD_GLOBAL         'random'
                             0000012B     69 - LOAD_ATTR           'randrange'
                             0000012E     64 - LOAD_CONST          1
                             00000131     64 - LOAD_CONST          100
                             00000134     83 - CALL_FUNCTION       r0002
                             00000137     7D - STORE_FAST          'roll'
                             0000013A     74 - LOAD_GLOBAL         'Utility'
                             0000013D     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000140     64 - LOAD_CONST          'GenericCorruption: Corruption chance roll = '
                             00000143     7C - LOAD_FAST           'roll'
                             00000146     0D - UNARY_CONVERT       
                             00000147     17 - BINARY_ADD          
                             00000148     64 - LOAD_CONST          '.'
                             0000014B     17 - BINARY_ADD          
                             0000014C     83 - CALL_FUNCTION       r0001
                             0000014F     01 - POP_TOP             
                             00000150     7C - LOAD_FAST           'roll'
                             00000153     7C - LOAD_FAST           'chanceValue'
                             00000156     6A - COMPARE_OP          ">"
                             00000159     6F - JUMP_IF_FALSE       -> 0000018D
                             0000015C     01 - POP_TOP             
                             0000015D     74 - LOAD_GLOBAL         'Utility'
                             00000160     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000163     64 - LOAD_CONST          "GenericCorruption: Corruption's "
                             00000166     7C - LOAD_FAST           'chanceValue'
                             00000169     0D - UNARY_CONVERT       
                             0000016A     17 - BINARY_ADD          
                             0000016B     64 - LOAD_CONST          ' failed on item('
                             0000016E     17 - BINARY_ADD          
                             0000016F     7C - LOAD_FAST           'item'
                             00000172     64 - LOAD_CONST          1
                             00000175     19 - BINARY_SUBSCR       
                             00000176     0D - UNARY_CONVERT       
                             00000177     17 - BINARY_ADD          
                             00000178     64 - LOAD_CONST          ').'
                             0000017B     17 - BINARY_ADD          
                             0000017C     83 - CALL_FUNCTION       r0001
                             0000017F     01 - POP_TOP             
                             00000180     74 - LOAD_GLOBAL         'DEFLECTED'
                             00000183     7C - LOAD_FAST           'destoryed_item_ID'
                             00000186     66 - BUILD_TUPLE         r0002
                             00000189     53 - RETURN_VALUE        
                             0000018A     6E - JUMP_FORWARD        -> 0000018E
                             0000018D     01 - POP_TOP             
                             0000018E     74 - LOAD_GLOBAL         'EFFECTS'
                             00000191     69 - LOAD_ATTR           'DestroyItem'
                             00000194     7C - LOAD_FAST           'directobject'
                             00000197     7C - LOAD_FAST           'item'
                             0000019A     64 - LOAD_CONST          0
                             0000019D     19 - BINARY_SUBSCR       
                             0000019E     7C - LOAD_FAST           'item'
                             000001A1     64 - LOAD_CONST          1
                             000001A4     19 - BINARY_SUBSCR       
                             000001A5     83 - CALL_FUNCTION       r0003
                             000001A8     7D - STORE_FAST          'destoryed'
                             000001AB     7C - LOAD_FAST           'destoryed'
                             000001AE     7C - LOAD_FAST           'destoryed_item_ID'
                             000001B1     66 - BUILD_TUPLE         r0002
                             000001B4     53 - RETURN_VALUE        
                             000001B5     64 - LOAD_CONST          None
                             000001B8     53 - RETURN_VALUE        
                         consts:
00000746                     TUPLE: (
0000074B                         None (4E),
0000074C                         INT: 0 (00 00 00 00),
00000751                         INT: 109 (6D 00 00 00),
00000756                         INT: 110 (6E 00 00 00),
0000075B                         STR: 'GenericCorruption: Subject has no items to destroy.' (33 00 00 00 47 65 6E 65 72 69 63 43 6F 72 72 75 70 74 69 6F 6E 3A 20 53 75 62 6A 65 63 74 20 68 61 73 20 6E 6F 20 69 74 65 6D 73 20 74 6F 20 64 65 73 74 72 6F 79 2E),
00000793                         INT: 1 (01 00 00 00),
00000798                         INT: 100 (64 00 00 00),
0000079D                         STR: 'GenericCorruption: Corruption chance roll = ' (2C 00 00 00 47 65 6E 65 72 69 63 43 6F 72 72 75 70 74 69 6F 6E 3A 20 43 6F 72 72 75 70 74 69 6F 6E 20 63 68 61 6E 63 65 20 72 6F 6C 6C 20 3D 20),
000007CE                         STR: '.' (01 00 00 00 2E),
000007D4                         STR: "GenericCorruption: Corruption's " (20 00 00 00 47 65 6E 65 72 69 63 43 6F 72 72 75 70 74 69 6F 6E 3A 20 43 6F 72 72 75 70 74 69 6F 6E 27 73 20),
000007F9                         STR: ' failed on item(' (10 00 00 00 20 66 61 69 6C 65 64 20 6F 6E 20 69 74 65 6D 28),
0000080E                         STR: ').' (02 00 00 00 29 2E)
                             )
                         names:
00000815                     TUPLE: (
0000081A                         STR: 'item' (04 00 00 00 69 74 65 6D),
00000823                         STR: 'destoryed_item_ID' (11 00 00 00 64 65 73 74 6F 72 79 65 64 5F 69 74 65 6D 5F 49 44),
00000839                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000845                         STR: 'IsAnNPC' (07 00 00 00 49 73 41 6E 4E 50 43),
00000851                         STR: 'directobject' (0C 00 00 00 64 69 72 65 63 74 6F 62 6A 65 63 74),
00000862                         STR: 'AI' (02 00 00 00 41 49),
00000869                         STR: 'getWeapon' (09 00 00 00 67 65 74 57 65 61 70 6F 6E),
00000877                         STR: 'weapon' (06 00 00 00 77 65 61 70 6F 6E),
00000882                         STR: 'FAILURE' (07 00 00 00 46 41 49 4C 55 52 45),
0000088E                         STR: 'itemList' (08 00 00 00 69 74 65 6D 4C 69 73 74),
0000089B                         STR: 'GetEquippedWeapon' (11 00 00 00 47 65 74 45 71 75 69 70 70 65 64 57 65 61 70 6F 6E),
000008B1                         STR: 'nSlot' (05 00 00 00 6E 53 6C 6F 74),
000008BB                         STR: 'append' (06 00 00 00 61 70 70 65 6E 64),
000008C6                         STR: 'GetEquippedHackerItem' (15 00 00 00 47 65 74 45 71 75 69 70 70 65 64 48 61 63 6B 65 72 49 74 65 6D),
000008E0                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
000008F7                         STR: 'GetRandomListEntry' (12 00 00 00 47 65 74 52 61 6E 64 6F 6D 4C 69 73 74 45 6E 74 72 79),
0000090E                         STR: 'type' (04 00 00 00 74 79 70 65),
00000917                         STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00000922                         STR: 'randrange' (09 00 00 00 72 61 6E 64 72 61 6E 67 65),
00000930                         STR: 'roll' (04 00 00 00 72 6F 6C 6C),
00000939                         STR: 'chanceValue' (0B 00 00 00 63 68 61 6E 63 65 56 61 6C 75 65),
00000949                         STR: 'DEFLECTED' (09 00 00 00 44 45 46 4C 45 43 54 45 44),
00000957                         STR: 'EFFECTS' (07 00 00 00 45 46 46 45 43 54 53),
00000963                         STR: 'DestroyItem' (0B 00 00 00 44 65 73 74 72 6F 79 49 74 65 6D),
00000973                         STR: 'destoryed' (09 00 00 00 64 65 73 74 6F 72 79 65 64)
                             )
                         varnames:
00000981                     TUPLE: (
00000986                         STR: 'directobject' (0C 00 00 00 64 69 72 65 63 74 6F 62 6A 65 63 74),
00000997                         STR: 'chanceValue' (0B 00 00 00 63 68 61 6E 63 65 56 61 6C 75 65),
000009A7                         STR: 'destoryed' (09 00 00 00 64 65 73 74 6F 72 79 65 64),
000009B5                         STR: 'weapon' (06 00 00 00 77 65 61 70 6F 6E),
000009C0                         STR: 'destoryed_item_ID' (11 00 00 00 64 65 73 74 6F 72 79 65 64 5F 69 74 65 6D 5F 49 44),
000009D6                         STR: 'item' (04 00 00 00 69 74 65 6D),
000009DF                         STR: 'itemList' (08 00 00 00 69 74 65 6D 4C 69 73 74),
000009EC                         STR: 'nSlot' (05 00 00 00 6E 53 6C 6F 74),
000009F6                         STR: 'roll' (04 00 00 00 72 6F 6C 6C)
                             )
                         freevars:
000009FF                     TUPLE: ()
                         cellvars:
00000A04                     TUPLE: ()
                         filename:
00000A09                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\virii.py' (4C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 76 69 72 69 69 2E 70 79)
                         name:
00000A5A                     STR: 'GenericCorruption' (11 00 00 00 47 65 6E 65 72 69 63 43 6F 72 72 75 70 74 69 6F 6E)
                         firslineno:
00000A70                     LONG: 91L (5B 00 00 00)
                         lnotab:
00000A74                     STR: '\x00\x02\x0c\x01\x06\x01\x10\x01\x0f\x01\x07\x01\x19\x02\x0e\x03\x06\x01\x0f\x01\x07\x01\x06\x01\x17\x01\x0f\x01\x07\x01\x06\x01\x17\x03\x08\x01\r\x01\x0e\x03\x0f\x04\x10\x01\x0e\x02\r\x02\x12\x01\x16\x01\r\x01#\x01\x0e\x03\x1d\x01' (3C 00 00 00 00 02 0C 01 06 01 10 01 0F 01 07 01 19 02 0E 03 06 01 0F 01 07 01 06 01 17 01 0F 01 07 01 06 01 17 03 08 01 0D 01 0E 03 0F 04 10 01 0E 02 0D 02 12 01 16 01 0D 01 23 01 0E 03 1D 01)
                 )
             names:
00000AB5         TUPLE: (
00000ABA             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00000AC5             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00000AD3             STR: 'obj' (03 00 00 00 6F 62 6A),
00000ADB             STR: 'combat_defines' (0E 00 00 00 63 6F 6D 62 61 74 5F 64 65 66 69 6E 65 73),
00000AEE             STR: 'CD' (02 00 00 00 43 44),
00000AF5             STR: 'missionvalidate' (0F 00 00 00 6D 69 73 73 69 6F 6E 76 61 6C 69 64 61 74 65),
00000B09             STR: 'mv' (02 00 00 00 6D 76),
00000B10             STR: 'combatvalidate' (0E 00 00 00 63 6F 6D 62 61 74 76 61 6C 69 64 61 74 65),
00000B23             STR: 'cv' (02 00 00 00 63 76),
00000B2A             STR: 'stringtable_client' (12 00 00 00 73 74 72 69 6E 67 74 61 62 6C 65 5F 63 6C 69 65 6E 74),
00000B41             STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00000B51             STR: 'ability.utility' (0F 00 00 00 61 62 69 6C 69 74 79 2E 75 74 69 6C 69 74 79),
00000B65             STR: 'utility' (07 00 00 00 75 74 69 6C 69 74 79),
00000B71             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000B7D             STR: 'getAbilityName' (0E 00 00 00 67 65 74 41 62 69 6C 69 74 79 4E 61 6D 65),
00000B90             STR: 'ability.defines' (0F 00 00 00 61 62 69 6C 69 74 79 2E 64 65 66 69 6E 65 73),
00000BA4             STR: 'ltfxmap' (07 00 00 00 6C 74 66 78 6D 61 70),
00000BB0             STR: 'FX' (02 00 00 00 46 58),
00000BB7             STR: 'ability.effects' (0F 00 00 00 61 62 69 6C 69 74 79 2E 65 66 66 65 63 74 73),
00000BCB             STR: 'effects' (07 00 00 00 65 66 66 65 63 74 73),
00000BD7             STR: 'EFFECTS' (07 00 00 00 45 46 46 45 43 54 53),
00000BE3             STR: 'virii_defines' (0D 00 00 00 76 69 72 69 69 5F 64 65 66 69 6E 65 73),
00000BF5             STR: 'VIRII' (05 00 00 00 56 49 52 49 49),
00000BFF             STR: 'VIRII_LEVEL_1_DURATION' (16 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 31 5F 44 55 52 41 54 49 4F 4E),
00000C1A             STR: 'AFFECTVISION1_TIME' (12 00 00 00 41 46 46 45 43 54 56 49 53 49 4F 4E 31 5F 54 49 4D 45),
00000C31             STR: 'VIRII_LEVEL_2_DURATION' (16 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 32 5F 44 55 52 41 54 49 4F 4E),
00000C4C             STR: 'AFFECTVISION2_TIME' (12 00 00 00 41 46 46 45 43 54 56 49 53 49 4F 4E 32 5F 54 49 4D 45),
00000C63             STR: 'VIRII_LEVEL_3_DURATION' (16 00 00 00 56 49 52 49 49 5F 4C 45 56 45 4C 5F 33 5F 44 55 52 41 54 49 4F 4E),
00000C7E             STR: 'AFFECTVISION3_TIME' (12 00 00 00 41 46 46 45 43 54 56 49 53 49 4F 4E 33 5F 54 49 4D 45),
00000C95             STR: 'MOVEMENTDISRUPT1_TIME' (15 00 00 00 4D 4F 56 45 4D 45 4E 54 44 49 53 52 55 50 54 31 5F 54 49 4D 45),
00000CAF             STR: 'MOVEMENTDISRUPT2_TIME' (15 00 00 00 4D 4F 56 45 4D 45 4E 54 44 49 53 52 55 50 54 32 5F 54 49 4D 45),
00000CC9             STR: 'MOVEMENTDISRUPT3_TIME' (15 00 00 00 4D 4F 56 45 4D 45 4E 54 44 49 53 52 55 50 54 33 5F 54 49 4D 45),
00000CE3             STR: 'DISABLEABILITY1_TIME' (14 00 00 00 44 49 53 41 42 4C 45 41 42 49 4C 49 54 59 31 5F 54 49 4D 45),
00000CFC             STR: 'MOVEMENTDISRUPT1_EFFECT' (17 00 00 00 4D 4F 56 45 4D 45 4E 54 44 49 53 52 55 50 54 31 5F 45 46 46 45 43 54),
00000D18             STR: 'MOVEMENTDISRUPT2_EFFECT' (17 00 00 00 4D 4F 56 45 4D 45 4E 54 44 49 53 52 55 50 54 32 5F 45 46 46 45 43 54),
00000D34             STR: 'MOVEMENTDISRUPT3_EFFECT' (17 00 00 00 4D 4F 56 45 4D 45 4E 54 44 49 53 52 55 50 54 33 5F 45 46 46 45 43 54),
00000D50             STR: 'DeflectBullets1Effect_DirectObject' (22 00 00 00 44 65 66 6C 65 63 74 42 75 6C 6C 65 74 73 31 45 66 66 65 63 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00000D77             STR: 'DeflectVirus1Effect_DirectObject' (20 00 00 00 44 65 66 6C 65 63 74 56 69 72 75 73 31 45 66 66 65 63 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00000D9C             STR: 'GenericCorruption' (11 00 00 00 47 65 6E 65 72 69 63 43 6F 72 72 75 70 74 69 6F 6E)
                 )
             varnames:
00000DB2         TUPLE: (
00000DB7             STR: 'FX' (02 00 00 00 46 58),
00000DBE             STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00000DCE             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00000DD9             STR: 'GenericCorruption' (11 00 00 00 47 65 6E 65 72 69 63 43 6F 72 72 75 70 74 69 6F 6E),
00000DEF             STR: 'cv' (02 00 00 00 63 76),
00000DF6             STR: 'getAbilityName' (0E 00 00 00 67 65 74 41 62 69 6C 69 74 79 4E 61 6D 65),
00000E09             STR: 'DeflectBullets1Effect_DirectObject' (22 00 00 00 44 65 66 6C 65 63 74 42 75 6C 6C 65 74 73 31 45 66 66 65 63 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00000E30             STR: 'VIRII' (05 00 00 00 56 49 52 49 49),
00000E3A             STR: 'MOVEMENTDISRUPT3_EFFECT' (17 00 00 00 4D 4F 56 45 4D 45 4E 54 44 49 53 52 55 50 54 33 5F 45 46 46 45 43 54),
00000E56             STR: 'MOVEMENTDISRUPT2_EFFECT' (17 00 00 00 4D 4F 56 45 4D 45 4E 54 44 49 53 52 55 50 54 32 5F 45 46 46 45 43 54),
00000E72             STR: 'MOVEMENTDISRUPT2_TIME' (15 00 00 00 4D 4F 56 45 4D 45 4E 54 44 49 53 52 55 50 54 32 5F 54 49 4D 45),
00000E8C             STR: 'MOVEMENTDISRUPT1_EFFECT' (17 00 00 00 4D 4F 56 45 4D 45 4E 54 44 49 53 52 55 50 54 31 5F 45 46 46 45 43 54),
00000EA8             STR: 'CD' (02 00 00 00 43 44),
00000EAF             STR: 'AFFECTVISION3_TIME' (12 00 00 00 41 46 46 45 43 54 56 49 53 49 4F 4E 33 5F 54 49 4D 45),
00000EC6             STR: 'MOVEMENTDISRUPT3_TIME' (15 00 00 00 4D 4F 56 45 4D 45 4E 54 44 49 53 52 55 50 54 33 5F 54 49 4D 45),
00000EE0             STR: 'AFFECTVISION2_TIME' (12 00 00 00 41 46 46 45 43 54 56 49 53 49 4F 4E 32 5F 54 49 4D 45),
00000EF7             STR: 'obj' (03 00 00 00 6F 62 6A),
00000EFF             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00000F0D             STR: 'DISABLEABILITY1_TIME' (14 00 00 00 44 49 53 41 42 4C 45 41 42 49 4C 49 54 59 31 5F 54 49 4D 45),
00000F26             STR: 'DeflectVirus1Effect_DirectObject' (20 00 00 00 44 65 66 6C 65 63 74 56 69 72 75 73 31 45 66 66 65 63 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00000F4B             STR: 'mv' (02 00 00 00 6D 76),
00000F52             STR: 'EFFECTS' (07 00 00 00 45 46 46 45 43 54 53),
00000F5E             STR: 'AFFECTVISION1_TIME' (12 00 00 00 41 46 46 45 43 54 56 49 53 49 4F 4E 31 5F 54 49 4D 45),
00000F75             STR: 'MOVEMENTDISRUPT1_TIME' (15 00 00 00 4D 4F 56 45 4D 45 4E 54 44 49 53 52 55 50 54 31 5F 54 49 4D 45),
00000F8F             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79)
                 )
             freevars:
00000F9B         TUPLE: ()
             cellvars:
00000FA0         TUPLE: ()
             filename:
00000FA5         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\virii.py' (4C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 76 69 72 69 69 2E 70 79)
             name:
00000FF6         STR: '?' (01 00 00 00 3F)
             firslineno:
00000FFC         LONG: 2L (02 00 00 00)
             lnotab:
00001000         STR: '\t\x01\t\x01\t\x01\t\x03\t\x01\t\x01\t\x01\x0c\x01\r\x03\x07\x04\t\x01\x0c\x02\t\x06\t\x01\t\x01\t\x02\t\x01\t\x01\t\x02\x06\x07\x06\x01\x06\x01\x06\x02\t\x06\t&' (32 00 00 00 09 01 09 01 09 01 09 03 09 01 09 01 09 01 0C 01 0D 03 07 04 09 01 0C 02 09 06 09 01 09 01 09 02 09 01 09 01 09 02 06 07 06 01 06 01 06 02 09 06 09 26)

