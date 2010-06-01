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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00Z\x02\x00d\x00\x00k\x03\x00Z\x04\x00d\x00\x00k\x05\x00Z\x05\x00d\x00\x00k\x06\x00Z\x07\x00d\x01\x00Z\x08\x00d\x02\x00\x84\x00\x00Z\t\x00d\x03\x00\x84\x00\x00Z\n\x00d\x04\x00\x84\x00\x00Z\x0b\x00d\x05\x00\x84\x00\x00Z\x0c\x00d\x06\x00\x84\x00\x00Z\r\x00d\x07\x00\x84\x00\x00Z\x0e\x00d\x08\x00\x84\x00\x00Z\x0f\x00d\t\x00\x84\x00\x00Z\x10\x00d\n\x00\x84\x00\x00Z\x11\x00d\x00\x00S' (91 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 5A 02 00 64 00 00 6B 03 00 5A 04 00 64 00 00 6B 05 00 5A 05 00 64 00 00 6B 06 00 5A 07 00 64 01 00 5A 08 00 64 02 00 84 00 00 5A 09 00 64 03 00 84 00 00 5A 0A 00 64 04 00 84 00 00 5A 0B 00 64 05 00 84 00 00 5A 0C 00 64 06 00 84 00 00 5A 0D 00 64 07 00 84 00 00 5A 0E 00 64 08 00 84 00 00 5A 0F 00 64 09 00 84 00 00 5A 10 00 64 0A 00 84 00 00 5A 11 00 64 00 00 53)
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
                 00000036     64 - LOAD_CONST          0
                 00000039     5A - STORE_NAME          '_COMBAT_PREFERRED_TACTICAL_BONUS'
                 0000003C     64 - LOAD_CONST          CODE('getTacticalMod')
                 0000003F     84 - MAKE_FUNCTION       r0000
                 00000042     5A - STORE_NAME          'getTacticalMod'
                 00000045     64 - LOAD_CONST          CODE('getTacticSpecificArmorPiercingPercent')
                 00000048     84 - MAKE_FUNCTION       r0000
                 0000004B     5A - STORE_NAME          'getTacticSpecificArmorPiercingPercent'
                 0000004E     64 - LOAD_CONST          CODE('getBaseRangedValue')
                 00000051     84 - MAKE_FUNCTION       r0000
                 00000054     5A - STORE_NAME          'getBaseRangedValue'
                 00000057     64 - LOAD_CONST          CODE('getRangedVsMeleeAttackModifier')
                 0000005A     84 - MAKE_FUNCTION       r0000
                 0000005D     5A - STORE_NAME          'getRangedVsMeleeAttackModifier'
                 00000060     64 - LOAD_CONST          CODE('getRangedVsMeleeDefenseModifier')
                 00000063     84 - MAKE_FUNCTION       r0000
                 00000066     5A - STORE_NAME          'getRangedVsMeleeDefenseModifier'
                 00000069     64 - LOAD_CONST          CODE('getOpponentCountModifier')
                 0000006C     84 - MAKE_FUNCTION       r0000
                 0000006F     5A - STORE_NAME          'getOpponentCountModifier'
                 00000072     64 - LOAD_CONST          CODE('getMultiOnOnePenalty')
                 00000075     84 - MAKE_FUNCTION       r0000
                 00000078     5A - STORE_NAME          'getMultiOnOnePenalty'
                 0000007B     64 - LOAD_CONST          CODE('getAttackerMods')
                 0000007E     84 - MAKE_FUNCTION       r0000
                 00000081     5A - STORE_NAME          'getAttackerMods'
                 00000084     64 - LOAD_CONST          CODE('getDefenderMods')
                 00000087     84 - MAKE_FUNCTION       r0000
                 0000008A     5A - STORE_NAME          'getDefenderMods'
                 0000008D     64 - LOAD_CONST          None
                 00000090     53 - RETURN_VALUE        
             consts:
000000AF         TUPLE: (
000000B4             None (4E),
000000B5             INT: 0 (00 00 00 00),
000000BA             CODE:
                         argcount:
000000BB                     LONG: 2L (02 00 00 00)
                         nlocals:
000000BF                     LONG: 2L (02 00 00 00)
                         stacksize:
000000C3                     LONG: 3L (03 00 00 00)
                         flags:
000000C7                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000000CB                     STR: 't\x00\x00i\x01\x00|\x00\x00|\x01\x00\x83\x02\x00o\x08\x00\x01t\x04\x00Sn\x05\x00\x01d\x01\x00Sd\x00\x00S' (23 00 00 00 74 00 00 69 01 00 7C 00 00 7C 01 00 83 02 00 6F 08 00 01 74 04 00 53 6E 05 00 01 64 01 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CU'
                             00000003     69 - LOAD_ATTR           'isPreferredTactical'
                             00000006     7C - LOAD_FAST           'tacticalSetting'
                             00000009     7C - LOAD_FAST           'opponentTacticalSetting'
                             0000000C     83 - CALL_FUNCTION       r0002
                             0000000F     6F - JUMP_IF_FALSE       -> 0000001A
                             00000012     01 - POP_TOP             
                             00000013     74 - LOAD_GLOBAL         '_COMBAT_PREFERRED_TACTICAL_BONUS'
                             00000016     53 - RETURN_VALUE        
                             00000017     6E - JUMP_FORWARD        -> 0000001F
                             0000001A     01 - POP_TOP             
                             0000001B     64 - LOAD_CONST          0
                             0000001E     53 - RETURN_VALUE        
                             0000001F     64 - LOAD_CONST          None
                             00000022     53 - RETURN_VALUE        
                         consts:
000000F3                     TUPLE: (
000000F8                         None (4E),
000000F9                         INT: 0 (00 00 00 00)
                             )
                         names:
000000FE                     TUPLE: (
00000103                         STR: 'CU' (02 00 00 00 43 55),
0000010A                         STR: 'isPreferredTactical' (13 00 00 00 69 73 50 72 65 66 65 72 72 65 64 54 61 63 74 69 63 61 6C),
00000122                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
00000136                         STR: 'opponentTacticalSetting' (17 00 00 00 6F 70 70 6F 6E 65 6E 74 54 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
00000152                         STR: '_COMBAT_PREFERRED_TACTICAL_BONUS' (20 00 00 00 5F 43 4F 4D 42 41 54 5F 50 52 45 46 45 52 52 45 44 5F 54 41 43 54 49 43 41 4C 5F 42 4F 4E 55 53)
                             )
                         varnames:
00000177                     TUPLE: (
0000017C                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
00000190                         STR: 'opponentTacticalSetting' (17 00 00 00 6F 70 70 6F 6E 65 6E 74 54 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67)
                             )
                         freevars:
000001AC                     TUPLE: ()
                         cellvars:
000001B1                     TUPLE: ()
                         filename:
000001B6                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_modifiers.py' (52 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 6D 6F 64 69 66 69 65 72 73 2E 70 79)
                         name:
0000020D                     STR: 'getTacticalMod' (0E 00 00 00 67 65 74 54 61 63 74 69 63 61 6C 4D 6F 64)
                         firslineno:
00000220                     LONG: 9L (09 00 00 00)
                         lnotab:
00000224                     STR: '\x00\x02\x13\x01\x08\x02' (06 00 00 00 00 02 13 01 08 02),
0000022F             CODE:
                         argcount:
00000230                     LONG: 1L (01 00 00 00)
                         nlocals:
00000234                     LONG: 1L (01 00 00 00)
                         stacksize:
00000238                     LONG: 2L (02 00 00 00)
                         flags:
0000023C                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000240                     STR: '|\x00\x00t\x01\x00i\x02\x00i\x03\x00j\x02\x00o\x08\x00\x01d\x01\x00Sn\x01\x00\x01d\x02\x00Sd\x00\x00S' (23 00 00 00 7C 00 00 74 01 00 69 02 00 69 03 00 6A 02 00 6F 08 00 01 64 01 00 53 6E 01 00 01 64 02 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'tacticalSetting'
                             00000003     74 - LOAD_GLOBAL         'constants'
                             00000006     69 - LOAD_ATTR           'combat'
                             00000009     69 - LOAD_ATTR           'POWER'
                             0000000C     6A - COMPARE_OP          "=="
                             0000000F     6F - JUMP_IF_FALSE       -> 0000001A
                             00000012     01 - POP_TOP             
                             00000013     64 - LOAD_CONST          0.5
                             00000016     53 - RETURN_VALUE        
                             00000017     6E - JUMP_FORWARD        -> 0000001B
                             0000001A     01 - POP_TOP             
                             0000001B     64 - LOAD_CONST          1.0
                             0000001E     53 - RETURN_VALUE        
                             0000001F     64 - LOAD_CONST          None
                             00000022     53 - RETURN_VALUE        
                         consts:
00000268                     TUPLE: (
0000026D                         None (4E),
0000026E                         FLOAT: 0.5 (03 30 2E 35),
00000273                         FLOAT: 1.0 (03 31 2E 30)
                             )
                         names:
00000278                     TUPLE: (
0000027D                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
00000291                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
0000029F                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
000002AA                         STR: 'POWER' (05 00 00 00 50 4F 57 45 52)
                             )
                         varnames:
000002B4                     TUPLE: (
000002B9                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67)
                             )
                         freevars:
000002CD                     TUPLE: ()
                         cellvars:
000002D2                     TUPLE: ()
                         filename:
000002D7                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_modifiers.py' (52 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 6D 6F 64 69 66 69 65 72 73 2E 70 79)
                         name:
0000032E                     STR: 'getTacticSpecificArmorPiercingPercent' (25 00 00 00 67 65 74 54 61 63 74 69 63 53 70 65 63 69 66 69 63 41 72 6D 6F 72 50 69 65 72 63 69 6E 67 50 65 72 63 65 6E 74)
                         firslineno:
00000358                     LONG: 16L (10 00 00 00)
                         lnotab:
0000035C                     STR: '\x00\x03\x13\x01\x08\x03' (06 00 00 00 00 03 13 01 08 03),
00000367             CODE:
                         argcount:
00000368                     LONG: 1L (01 00 00 00)
                         nlocals:
0000036C                     LONG: 2L (02 00 00 00)
                         stacksize:
00000370                     LONG: 2L (02 00 00 00)
                         flags:
00000374                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000378                     STR: 'd\x01\x00}\x01\x00|\x00\x00i\x02\x00t\x03\x00i\x04\x00i\x05\x00j\x02\x00p\x13\x00\x01|\x00\x00i\x02\x00t\x03\x00i\x04\x00i\x06\x00j\x02\x00o\n\x00\x01d\x02\x00}\x01\x00ne\x00\x01|\x00\x00i\x02\x00t\x03\x00i\x04\x00i\x07\x00j\x02\x00o\x0e\x00\x01t\x08\x00d\x03\x00\x83\x01\x00\x01nA\x00\x01|\x00\x00i\x02\x00t\x03\x00i\x04\x00i\t\x00j\x02\x00o\n\x00\x01d\x04\x00}\x01\x00n!\x00\x01|\x00\x00i\x02\x00t\x03\x00i\x04\x00i\n\x00j\x02\x00o\n\x00\x01d\x05\x00}\x01\x00n\x01\x00\x01|\x01\x00Sd\x00\x00S' (A8 00 00 00 64 01 00 7D 01 00 7C 00 00 69 02 00 74 03 00 69 04 00 69 05 00 6A 02 00 70 13 00 01 7C 00 00 69 02 00 74 03 00 69 04 00 69 06 00 6A 02 00 6F 0A 00 01 64 02 00 7D 01 00 6E 65 00 01 7C 00 00 69 02 00 74 03 00 69 04 00 69 07 00 6A 02 00 6F 0E 00 01 74 08 00 64 03 00 83 01 00 01 6E 41 00 01 7C 00 00 69 02 00 74 03 00 69 04 00 69 09 00 6A 02 00 6F 0A 00 01 64 04 00 7D 01 00 6E 21 00 01 7C 00 00 69 02 00 74 03 00 69 04 00 69 0A 00 6A 02 00 6F 0A 00 01 64 05 00 7D 01 00 6E 01 00 01 7C 01 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          0
                             00000003     7D - STORE_FAST          'modifier'
                             00000006     7C - LOAD_FAST           'player'
                             00000009     69 - LOAD_ATTR           'equippedItemType'
                             0000000C     74 - LOAD_GLOBAL         'constants'
                             0000000F     69 - LOAD_ATTR           'combat'
                             00000012     69 - LOAD_ATTR           'RANGED_SINGLE_PISTOL'
                             00000015     6A - COMPARE_OP          "=="
                             00000018     70 - JUMP_IF_TRUE        -> 0000002E
                             0000001B     01 - POP_TOP             
                             0000001C     7C - LOAD_FAST           'player'
                             0000001F     69 - LOAD_ATTR           'equippedItemType'
                             00000022     74 - LOAD_GLOBAL         'constants'
                             00000025     69 - LOAD_ATTR           'combat'
                             00000028     69 - LOAD_ATTR           'RANGED_DOUBLE_PISTOL'
                             0000002B     6A - COMPARE_OP          "=="
                             0000002E     6F - JUMP_IF_FALSE       -> 0000003B
                             00000031     01 - POP_TOP             
                             00000032     64 - LOAD_CONST          5
                             00000035     7D - STORE_FAST          'modifier'
                             00000038     6E - JUMP_FORWARD        -> 000000A0
                             0000003B     01 - POP_TOP             
                             0000003C     7C - LOAD_FAST           'player'
                             0000003F     69 - LOAD_ATTR           'equippedItemType'
                             00000042     74 - LOAD_GLOBAL         'constants'
                             00000045     69 - LOAD_ATTR           'combat'
                             00000048     69 - LOAD_ATTR           'RANGED_SHOTGUN'
                             0000004B     6A - COMPARE_OP          "=="
                             0000004E     6F - JUMP_IF_FALSE       -> 0000005F
                             00000051     01 - POP_TOP             
                             00000052     74 - LOAD_GLOBAL         'outputToAll'
                             00000055     64 - LOAD_CONST          'Shotgun currently not supported'
                             00000058     83 - CALL_FUNCTION       r0001
                             0000005B     01 - POP_TOP             
                             0000005C     6E - JUMP_FORWARD        -> 000000A0
                             0000005F     01 - POP_TOP             
                             00000060     7C - LOAD_FAST           'player'
                             00000063     69 - LOAD_ATTR           'equippedItemType'
                             00000066     74 - LOAD_GLOBAL         'constants'
                             00000069     69 - LOAD_ATTR           'combat'
                             0000006C     69 - LOAD_ATTR           'RANGED_MACHINE_GUN'
                             0000006F     6A - COMPARE_OP          "=="
                             00000072     6F - JUMP_IF_FALSE       -> 0000007F
                             00000075     01 - POP_TOP             
                             00000076     64 - LOAD_CONST          10
                             00000079     7D - STORE_FAST          'modifier'
                             0000007C     6E - JUMP_FORWARD        -> 000000A0
                             0000007F     01 - POP_TOP             
                             00000080     7C - LOAD_FAST           'player'
                             00000083     69 - LOAD_ATTR           'equippedItemType'
                             00000086     74 - LOAD_GLOBAL         'constants'
                             00000089     69 - LOAD_ATTR           'combat'
                             0000008C     69 - LOAD_ATTR           'RANGED_RIFLE'
                             0000008F     6A - COMPARE_OP          "=="
                             00000092     6F - JUMP_IF_FALSE       -> 0000009F
                             00000095     01 - POP_TOP             
                             00000096     64 - LOAD_CONST          15
                             00000099     7D - STORE_FAST          'modifier'
                             0000009C     6E - JUMP_FORWARD        -> 000000A0
                             0000009F     01 - POP_TOP             
                             000000A0     7C - LOAD_FAST           'modifier'
                             000000A3     53 - RETURN_VALUE        
                             000000A4     64 - LOAD_CONST          None
                             000000A7     53 - RETURN_VALUE        
                         consts:
00000425                     TUPLE: (
0000042A                         None (4E),
0000042B                         INT: 0 (00 00 00 00),
00000430                         INT: 5 (05 00 00 00),
00000435                         STR: 'Shotgun currently not supported' (1F 00 00 00 53 68 6F 74 67 75 6E 20 63 75 72 72 65 6E 74 6C 79 20 6E 6F 74 20 73 75 70 70 6F 72 74 65 64),
00000459                         INT: 10 (0A 00 00 00),
0000045E                         INT: 15 (0F 00 00 00)
                             )
                         names:
00000463                     TUPLE: (
00000468                         STR: 'modifier' (08 00 00 00 6D 6F 64 69 66 69 65 72),
00000475                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00000480                         STR: 'equippedItemType' (10 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D 54 79 70 65),
00000495                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
000004A3                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
000004AE                         STR: 'RANGED_SINGLE_PISTOL' (14 00 00 00 52 41 4E 47 45 44 5F 53 49 4E 47 4C 45 5F 50 49 53 54 4F 4C),
000004C7                         STR: 'RANGED_DOUBLE_PISTOL' (14 00 00 00 52 41 4E 47 45 44 5F 44 4F 55 42 4C 45 5F 50 49 53 54 4F 4C),
000004E0                         STR: 'RANGED_SHOTGUN' (0E 00 00 00 52 41 4E 47 45 44 5F 53 48 4F 54 47 55 4E),
000004F3                         STR: 'outputToAll' (0B 00 00 00 6F 75 74 70 75 74 54 6F 41 6C 6C),
00000503                         STR: 'RANGED_MACHINE_GUN' (12 00 00 00 52 41 4E 47 45 44 5F 4D 41 43 48 49 4E 45 5F 47 55 4E),
0000051A                         STR: 'RANGED_RIFLE' (0C 00 00 00 52 41 4E 47 45 44 5F 52 49 46 4C 45)
                             )
                         varnames:
0000052B                     TUPLE: (
00000530                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
0000053B                         STR: 'modifier' (08 00 00 00 6D 6F 64 69 66 69 65 72)
                             )
                         freevars:
00000548                     TUPLE: ()
                         cellvars:
0000054D                     TUPLE: ()
                         filename:
00000552                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_modifiers.py' (52 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 6D 6F 64 69 66 69 65 72 73 2E 70 79)
                         name:
000005A9                     STR: 'getBaseRangedValue' (12 00 00 00 67 65 74 42 61 73 65 52 61 6E 67 65 64 56 61 6C 75 65)
                         firslineno:
000005C0                     LONG: 25L (19 00 00 00)
                         lnotab:
000005C4                     STR: '\x00\x02\x06\x02,\x01\n\x01\x16\x01\x0e\x01\x16\x01\n\x01\x16\x01\n\x02' (14 00 00 00 00 02 06 02 2C 01 0A 01 16 01 0E 01 16 01 0A 01 16 01 0A 02),
000005DD             CODE:
                         argcount:
000005DE                     LONG: 3L (03 00 00 00)
                         nlocals:
000005E2                     LONG: 5L (05 00 00 00)
                         stacksize:
000005E6                     LONG: 3L (03 00 00 00)
                         flags:
000005EA                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000005EE                     STR: 't\x00\x00i\x01\x00|\x00\x00i\x03\x00\x83\x01\x00t\x04\x00j\x02\x00p\x16\x00\x01t\x00\x00i\x01\x00|\x01\x00i\x03\x00\x83\x01\x00t\x06\x00j\x02\x00o\x08\x00\x01d\x01\x00Sn\x01\x00\x01d\x01\x00}\x03\x00|\x01\x00i\x08\x00d\x02\x00j\x04\x00o(\x00\x01|\x00\x00i\t\x00o\n\x00\x01d\x03\x00}\x03\x00qx\x00\x01t\x00\x00i\n\x00d\x04\x00d\x05\x00\x83\x02\x00\x01n\x01\x00\x01t\x0b\x00|\x00\x00\x83\x01\x00}\x04\x00|\x02\x00i\x0e\x00t\x0f\x00i\x10\x00i\x11\x00j\x02\x00o6\x00\x01|\x00\x00i\x12\x00d\x01\x00j\x02\x00o\x18\x00\x01t\x00\x00i\n\x00d\x06\x00d\x05\x00\x83\x02\x00\x01|\x03\x00Sn\x01\x00\x01|\x04\x00d\x07\x00\x14}\x04\x00n)\x00\x01|\x01\x00i\x13\x00d\x01\x00j\x02\x00o\x18\x00\x01t\x00\x00i\n\x00d\x08\x00d\x05\x00\x83\x02\x00\x01|\x03\x00Sn\x01\x00\x01|\x03\x00|\x04\x00\x17Sd\x00\x00S' (04 01 00 00 74 00 00 69 01 00 7C 00 00 69 03 00 83 01 00 74 04 00 6A 02 00 70 16 00 01 74 00 00 69 01 00 7C 01 00 69 03 00 83 01 00 74 06 00 6A 02 00 6F 08 00 01 64 01 00 53 6E 01 00 01 64 01 00 7D 03 00 7C 01 00 69 08 00 64 02 00 6A 04 00 6F 28 00 01 7C 00 00 69 09 00 6F 0A 00 01 64 03 00 7D 03 00 71 78 00 01 74 00 00 69 0A 00 64 04 00 64 05 00 83 02 00 01 6E 01 00 01 74 0B 00 7C 00 00 83 01 00 7D 04 00 7C 02 00 69 0E 00 74 0F 00 69 10 00 69 11 00 6A 02 00 6F 36 00 01 7C 00 00 69 12 00 64 01 00 6A 02 00 6F 18 00 01 74 00 00 69 0A 00 64 06 00 64 05 00 83 02 00 01 7C 03 00 53 6E 01 00 01 7C 04 00 64 07 00 14 7D 04 00 6E 29 00 01 7C 01 00 69 13 00 64 01 00 6A 02 00 6F 18 00 01 74 00 00 69 0A 00 64 08 00 64 05 00 83 02 00 01 7C 03 00 53 6E 01 00 01 7C 03 00 7C 04 00 17 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CU'
                             00000003     69 - LOAD_ATTR           'isUsingWeapon'
                             00000006     7C - LOAD_FAST           'attacker'
                             00000009     69 - LOAD_ATTR           'equippedItemType'
                             0000000C     83 - CALL_FUNCTION       r0001
                             0000000F     74 - LOAD_GLOBAL         'False'
                             00000012     6A - COMPARE_OP          "=="
                             00000015     70 - JUMP_IF_TRUE        -> 0000002E
                             00000018     01 - POP_TOP             
                             00000019     74 - LOAD_GLOBAL         'CU'
                             0000001C     69 - LOAD_ATTR           'isUsingWeapon'
                             0000001F     7C - LOAD_FAST           'defender'
                             00000022     69 - LOAD_ATTR           'equippedItemType'
                             00000025     83 - CALL_FUNCTION       r0001
                             00000028     74 - LOAD_GLOBAL         'True'
                             0000002B     6A - COMPARE_OP          "=="
                             0000002E     6F - JUMP_IF_FALSE       -> 00000039
                             00000031     01 - POP_TOP             
                             00000032     64 - LOAD_CONST          0
                             00000035     53 - RETURN_VALUE        
                             00000036     6E - JUMP_FORWARD        -> 0000003A
                             00000039     01 - POP_TOP             
                             0000003A     64 - LOAD_CONST          0
                             0000003D     7D - STORE_FAST          'base_modifier'
                             00000040     7C - LOAD_FAST           'defender'
                             00000043     69 - LOAD_ATTR           'opponentCount'
                             00000046     64 - LOAD_CONST          1
                             00000049     6A - COMPARE_OP          ">"
                             0000004C     6F - JUMP_IF_FALSE       -> 00000077
                             0000004F     01 - POP_TOP             
                             00000050     7C - LOAD_FAST           'attacker'
                             00000053     69 - LOAD_ATTR           'allowFiringIntoMeleePenalty'
                             00000056     6F - JUMP_IF_FALSE       -> 00000063
                             00000059     01 - POP_TOP             
                             0000005A     64 - LOAD_CONST          -15
                             0000005D     7D - STORE_FAST          'base_modifier'
                             00000060     71 - JUMP_ABSOLUTE       -> 00000078
                             00000063     01 - POP_TOP             
                             00000064     74 - LOAD_GLOBAL         'CU'
                             00000067     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000006A     64 - LOAD_CONST          'Firing into melee penalty negated due to ability'
                             0000006D     64 - LOAD_CONST          3
                             00000070     83 - CALL_FUNCTION       r0002
                             00000073     01 - POP_TOP             
                             00000074     6E - JUMP_FORWARD        -> 00000078
                             00000077     01 - POP_TOP             
                             00000078     74 - LOAD_GLOBAL         'getBaseRangedValue'
                             0000007B     7C - LOAD_FAST           'attacker'
                             0000007E     83 - CALL_FUNCTION       r0001
                             00000081     7D - STORE_FAST          'modifier'
                             00000084     7C - LOAD_FAST           'result'
                             00000087     69 - LOAD_ATTR           'distance'
                             0000008A     74 - LOAD_GLOBAL         'constants'
                             0000008D     69 - LOAD_ATTR           'combat'
                             00000090     69 - LOAD_ATTR           'SHORT_RANGE'
                             00000093     6A - COMPARE_OP          "=="
                             00000096     6F - JUMP_IF_FALSE       -> 000000CF
                             00000099     01 - POP_TOP             
                             0000009A     7C - LOAD_FAST           'attacker'
                             0000009D     69 - LOAD_ATTR           'allowFiringAtMeleeRangePenalty'
                             000000A0     64 - LOAD_CONST          0
                             000000A3     6A - COMPARE_OP          "=="
                             000000A6     6F - JUMP_IF_FALSE       -> 000000C1
                             000000A9     01 - POP_TOP             
                             000000AA     74 - LOAD_GLOBAL         'CU'
                             000000AD     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000B0     64 - LOAD_CONST          'Firing at short range penalty negated due to ability'
                             000000B3     64 - LOAD_CONST          3
                             000000B6     83 - CALL_FUNCTION       r0002
                             000000B9     01 - POP_TOP             
                             000000BA     7C - LOAD_FAST           'base_modifier'
                             000000BD     53 - RETURN_VALUE        
                             000000BE     6E - JUMP_FORWARD        -> 000000C2
                             000000C1     01 - POP_TOP             
                             000000C2     7C - LOAD_FAST           'modifier'
                             000000C5     64 - LOAD_CONST          -1
                             000000C8     14 - BINARY_MULTIPLY     
                             000000C9     7D - STORE_FAST          'modifier'
                             000000CC     6E - JUMP_FORWARD        -> 000000F8
                             000000CF     01 - POP_TOP             
                             000000D0     7C - LOAD_FAST           'defender'
                             000000D3     69 - LOAD_ATTR           'allowMeleeAtRangedPenalty'
                             000000D6     64 - LOAD_CONST          0
                             000000D9     6A - COMPARE_OP          "=="
                             000000DC     6F - JUMP_IF_FALSE       -> 000000F7
                             000000DF     01 - POP_TOP             
                             000000E0     74 - LOAD_GLOBAL         'CU'
                             000000E3     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000E6     64 - LOAD_CONST          'Melee at ranged penalty negated by ability'
                             000000E9     64 - LOAD_CONST          3
                             000000EC     83 - CALL_FUNCTION       r0002
                             000000EF     01 - POP_TOP             
                             000000F0     7C - LOAD_FAST           'base_modifier'
                             000000F3     53 - RETURN_VALUE        
                             000000F4     6E - JUMP_FORWARD        -> 000000F8
                             000000F7     01 - POP_TOP             
                             000000F8     7C - LOAD_FAST           'base_modifier'
                             000000FB     7C - LOAD_FAST           'modifier'
                             000000FE     17 - BINARY_ADD          
                             000000FF     53 - RETURN_VALUE        
                             00000100     64 - LOAD_CONST          None
                             00000103     53 - RETURN_VALUE        
                         consts:
000006F7                     TUPLE: (
000006FC                         None (4E),
000006FD                         INT: 0 (00 00 00 00),
00000702                         INT: 1 (01 00 00 00),
00000707                         INT: -15 (F1 FF FF FF),
0000070C                         STR: 'Firing into melee penalty negated due to ability' (30 00 00 00 46 69 72 69 6E 67 20 69 6E 74 6F 20 6D 65 6C 65 65 20 70 65 6E 61 6C 74 79 20 6E 65 67 61 74 65 64 20 64 75 65 20 74 6F 20 61 62 69 6C 69 74 79),
00000741                         INT: 3 (03 00 00 00),
00000746                         STR: 'Firing at short range penalty negated due to ability' (34 00 00 00 46 69 72 69 6E 67 20 61 74 20 73 68 6F 72 74 20 72 61 6E 67 65 20 70 65 6E 61 6C 74 79 20 6E 65 67 61 74 65 64 20 64 75 65 20 74 6F 20 61 62 69 6C 69 74 79),
0000077F                         INT: -1 (FF FF FF FF),
00000784                         STR: 'Melee at ranged penalty negated by ability' (2A 00 00 00 4D 65 6C 65 65 20 61 74 20 72 61 6E 67 65 64 20 70 65 6E 61 6C 74 79 20 6E 65 67 61 74 65 64 20 62 79 20 61 62 69 6C 69 74 79)
                             )
                         names:
000007B3                     TUPLE: (
000007B8                         STR: 'CU' (02 00 00 00 43 55),
000007BF                         STR: 'isUsingWeapon' (0D 00 00 00 69 73 55 73 69 6E 67 57 65 61 70 6F 6E),
000007D1                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
000007DE                         STR: 'equippedItemType' (10 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D 54 79 70 65),
000007F3                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
000007FD                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
0000080A                         STR: 'True' (04 00 00 00 54 72 75 65),
00000813                         STR: 'base_modifier' (0D 00 00 00 62 61 73 65 5F 6D 6F 64 69 66 69 65 72),
00000825                         STR: 'opponentCount' (0D 00 00 00 6F 70 70 6F 6E 65 6E 74 43 6F 75 6E 74),
00000837                         STR: 'allowFiringIntoMeleePenalty' (1B 00 00 00 61 6C 6C 6F 77 46 69 72 69 6E 67 49 6E 74 6F 4D 65 6C 65 65 50 65 6E 61 6C 74 79),
00000857                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
00000874                         STR: 'getBaseRangedValue' (12 00 00 00 67 65 74 42 61 73 65 52 61 6E 67 65 64 56 61 6C 75 65),
0000088B                         STR: 'modifier' (08 00 00 00 6D 6F 64 69 66 69 65 72),
00000898                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
000008A3                         STR: 'distance' (08 00 00 00 64 69 73 74 61 6E 63 65),
000008B0                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
000008BE                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
000008C9                         STR: 'SHORT_RANGE' (0B 00 00 00 53 48 4F 52 54 5F 52 41 4E 47 45),
000008D9                         STR: 'allowFiringAtMeleeRangePenalty' (1E 00 00 00 61 6C 6C 6F 77 46 69 72 69 6E 67 41 74 4D 65 6C 65 65 52 61 6E 67 65 50 65 6E 61 6C 74 79),
000008FC                         STR: 'allowMeleeAtRangedPenalty' (19 00 00 00 61 6C 6C 6F 77 4D 65 6C 65 65 41 74 52 61 6E 67 65 64 50 65 6E 61 6C 74 79)
                             )
                         varnames:
0000091A                     TUPLE: (
0000091F                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
0000092C                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
00000939                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00000944                         STR: 'base_modifier' (0D 00 00 00 62 61 73 65 5F 6D 6F 64 69 66 69 65 72),
00000956                         STR: 'modifier' (08 00 00 00 6D 6F 64 69 66 69 65 72)
                             )
                         freevars:
00000963                     TUPLE: ()
                         cellvars:
00000968                     TUPLE: ()
                         filename:
0000096D                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_modifiers.py' (52 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 6D 6F 64 69 66 69 65 72 73 2E 70 79)
                         name:
000009C4                     STR: 'getRangedVsMeleeAttackModifier' (1E 00 00 00 67 65 74 52 61 6E 67 65 64 56 73 4D 65 6C 65 65 41 74 74 61 63 6B 4D 6F 64 69 66 69 65 72)
                         firslineno:
000009E7                     LONG: 40L (28 00 00 00)
                         lnotab:
000009EB                     STR: '\x00\x022\x01\x08\x03\x06\x01\x10\x01\n\x01\n\x02\x14\x02\x0c\x02\x16\x01\x10\x01\x10\x01\x08\x02\x0e\x03\x10\x01\x10\x01\x08\x02' (22 00 00 00 00 02 32 01 08 03 06 01 10 01 0A 01 0A 02 14 02 0C 02 16 01 10 01 10 01 08 02 0E 03 10 01 10 01 08 02),
00000A12             CODE:
                         argcount:
00000A13                     LONG: 3L (03 00 00 00)
                         nlocals:
00000A17                     LONG: 5L (05 00 00 00)
                         stacksize:
00000A1B                     LONG: 3L (03 00 00 00)
                         flags:
00000A1F                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000A23                     STR: 't\x00\x00i\x01\x00|\x01\x00i\x03\x00\x83\x01\x00t\x04\x00j\x02\x00p\x16\x00\x01t\x00\x00i\x01\x00|\x00\x00i\x03\x00\x83\x01\x00t\x06\x00j\x02\x00o\x08\x00\x01d\x01\x00Sn\x01\x00\x01d\x01\x00}\x03\x00|\x00\x00i\x08\x00d\x02\x00j\x04\x00o(\x00\x01|\x01\x00i\t\x00o\n\x00\x01d\x03\x00}\x03\x00qx\x00\x01t\x00\x00i\n\x00d\x04\x00d\x05\x00\x83\x02\x00\x01n\x01\x00\x01t\x0b\x00|\x01\x00\x83\x01\x00}\x04\x00|\x02\x00i\x0e\x00t\x0f\x00i\x10\x00i\x11\x00j\x02\x00o6\x00\x01|\x01\x00i\x12\x00d\x01\x00j\x02\x00o\x18\x00\x01t\x00\x00i\n\x00d\x06\x00d\x05\x00\x83\x02\x00\x01|\x03\x00Sn\x01\x00\x01|\x04\x00d\x07\x00\x14}\x04\x00n)\x00\x01|\x00\x00i\x13\x00d\x01\x00j\x02\x00o\x18\x00\x01t\x00\x00i\n\x00d\x08\x00d\x05\x00\x83\x02\x00\x01|\x03\x00Sn\x01\x00\x01|\x03\x00|\x04\x00\x17Sd\x00\x00S' (04 01 00 00 74 00 00 69 01 00 7C 01 00 69 03 00 83 01 00 74 04 00 6A 02 00 70 16 00 01 74 00 00 69 01 00 7C 00 00 69 03 00 83 01 00 74 06 00 6A 02 00 6F 08 00 01 64 01 00 53 6E 01 00 01 64 01 00 7D 03 00 7C 00 00 69 08 00 64 02 00 6A 04 00 6F 28 00 01 7C 01 00 69 09 00 6F 0A 00 01 64 03 00 7D 03 00 71 78 00 01 74 00 00 69 0A 00 64 04 00 64 05 00 83 02 00 01 6E 01 00 01 74 0B 00 7C 01 00 83 01 00 7D 04 00 7C 02 00 69 0E 00 74 0F 00 69 10 00 69 11 00 6A 02 00 6F 36 00 01 7C 01 00 69 12 00 64 01 00 6A 02 00 6F 18 00 01 74 00 00 69 0A 00 64 06 00 64 05 00 83 02 00 01 7C 03 00 53 6E 01 00 01 7C 04 00 64 07 00 14 7D 04 00 6E 29 00 01 7C 00 00 69 13 00 64 01 00 6A 02 00 6F 18 00 01 74 00 00 69 0A 00 64 08 00 64 05 00 83 02 00 01 7C 03 00 53 6E 01 00 01 7C 03 00 7C 04 00 17 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CU'
                             00000003     69 - LOAD_ATTR           'isUsingWeapon'
                             00000006     7C - LOAD_FAST           'defender'
                             00000009     69 - LOAD_ATTR           'equippedItemType'
                             0000000C     83 - CALL_FUNCTION       r0001
                             0000000F     74 - LOAD_GLOBAL         'False'
                             00000012     6A - COMPARE_OP          "=="
                             00000015     70 - JUMP_IF_TRUE        -> 0000002E
                             00000018     01 - POP_TOP             
                             00000019     74 - LOAD_GLOBAL         'CU'
                             0000001C     69 - LOAD_ATTR           'isUsingWeapon'
                             0000001F     7C - LOAD_FAST           'attacker'
                             00000022     69 - LOAD_ATTR           'equippedItemType'
                             00000025     83 - CALL_FUNCTION       r0001
                             00000028     74 - LOAD_GLOBAL         'True'
                             0000002B     6A - COMPARE_OP          "=="
                             0000002E     6F - JUMP_IF_FALSE       -> 00000039
                             00000031     01 - POP_TOP             
                             00000032     64 - LOAD_CONST          0
                             00000035     53 - RETURN_VALUE        
                             00000036     6E - JUMP_FORWARD        -> 0000003A
                             00000039     01 - POP_TOP             
                             0000003A     64 - LOAD_CONST          0
                             0000003D     7D - STORE_FAST          'base_modifier'
                             00000040     7C - LOAD_FAST           'attacker'
                             00000043     69 - LOAD_ATTR           'opponentCount'
                             00000046     64 - LOAD_CONST          1
                             00000049     6A - COMPARE_OP          ">"
                             0000004C     6F - JUMP_IF_FALSE       -> 00000077
                             0000004F     01 - POP_TOP             
                             00000050     7C - LOAD_FAST           'defender'
                             00000053     69 - LOAD_ATTR           'allowFiringIntoMeleePenalty'
                             00000056     6F - JUMP_IF_FALSE       -> 00000063
                             00000059     01 - POP_TOP             
                             0000005A     64 - LOAD_CONST          -15
                             0000005D     7D - STORE_FAST          'base_modifier'
                             00000060     71 - JUMP_ABSOLUTE       -> 00000078
                             00000063     01 - POP_TOP             
                             00000064     74 - LOAD_GLOBAL         'CU'
                             00000067     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000006A     64 - LOAD_CONST          'Firing into melee penalty negated due to ability'
                             0000006D     64 - LOAD_CONST          3
                             00000070     83 - CALL_FUNCTION       r0002
                             00000073     01 - POP_TOP             
                             00000074     6E - JUMP_FORWARD        -> 00000078
                             00000077     01 - POP_TOP             
                             00000078     74 - LOAD_GLOBAL         'getBaseRangedValue'
                             0000007B     7C - LOAD_FAST           'defender'
                             0000007E     83 - CALL_FUNCTION       r0001
                             00000081     7D - STORE_FAST          'modifier'
                             00000084     7C - LOAD_FAST           'result'
                             00000087     69 - LOAD_ATTR           'distance'
                             0000008A     74 - LOAD_GLOBAL         'constants'
                             0000008D     69 - LOAD_ATTR           'combat'
                             00000090     69 - LOAD_ATTR           'SHORT_RANGE'
                             00000093     6A - COMPARE_OP          "=="
                             00000096     6F - JUMP_IF_FALSE       -> 000000CF
                             00000099     01 - POP_TOP             
                             0000009A     7C - LOAD_FAST           'defender'
                             0000009D     69 - LOAD_ATTR           'allowFiringAtMeleeRangePenalty'
                             000000A0     64 - LOAD_CONST          0
                             000000A3     6A - COMPARE_OP          "=="
                             000000A6     6F - JUMP_IF_FALSE       -> 000000C1
                             000000A9     01 - POP_TOP             
                             000000AA     74 - LOAD_GLOBAL         'CU'
                             000000AD     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000B0     64 - LOAD_CONST          'Firing at short range penalty negated by ability'
                             000000B3     64 - LOAD_CONST          3
                             000000B6     83 - CALL_FUNCTION       r0002
                             000000B9     01 - POP_TOP             
                             000000BA     7C - LOAD_FAST           'base_modifier'
                             000000BD     53 - RETURN_VALUE        
                             000000BE     6E - JUMP_FORWARD        -> 000000C2
                             000000C1     01 - POP_TOP             
                             000000C2     7C - LOAD_FAST           'modifier'
                             000000C5     64 - LOAD_CONST          -1
                             000000C8     14 - BINARY_MULTIPLY     
                             000000C9     7D - STORE_FAST          'modifier'
                             000000CC     6E - JUMP_FORWARD        -> 000000F8
                             000000CF     01 - POP_TOP             
                             000000D0     7C - LOAD_FAST           'attacker'
                             000000D3     69 - LOAD_ATTR           'allowMeleeAtRangedPenalty'
                             000000D6     64 - LOAD_CONST          0
                             000000D9     6A - COMPARE_OP          "=="
                             000000DC     6F - JUMP_IF_FALSE       -> 000000F7
                             000000DF     01 - POP_TOP             
                             000000E0     74 - LOAD_GLOBAL         'CU'
                             000000E3     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000E6     64 - LOAD_CONST          'Melee at ranged penalty negated by ability'
                             000000E9     64 - LOAD_CONST          3
                             000000EC     83 - CALL_FUNCTION       r0002
                             000000EF     01 - POP_TOP             
                             000000F0     7C - LOAD_FAST           'base_modifier'
                             000000F3     53 - RETURN_VALUE        
                             000000F4     6E - JUMP_FORWARD        -> 000000F8
                             000000F7     01 - POP_TOP             
                             000000F8     7C - LOAD_FAST           'base_modifier'
                             000000FB     7C - LOAD_FAST           'modifier'
                             000000FE     17 - BINARY_ADD          
                             000000FF     53 - RETURN_VALUE        
                             00000100     64 - LOAD_CONST          None
                             00000103     53 - RETURN_VALUE        
                         consts:
00000B2C                     TUPLE: (
00000B31                         None (4E),
00000B32                         INT: 0 (00 00 00 00),
00000B37                         INT: 1 (01 00 00 00),
00000B3C                         INT: -15 (F1 FF FF FF),
00000B41                         STR: 'Firing into melee penalty negated due to ability' (30 00 00 00 46 69 72 69 6E 67 20 69 6E 74 6F 20 6D 65 6C 65 65 20 70 65 6E 61 6C 74 79 20 6E 65 67 61 74 65 64 20 64 75 65 20 74 6F 20 61 62 69 6C 69 74 79),
00000B76                         INT: 3 (03 00 00 00),
00000B7B                         STR: 'Firing at short range penalty negated by ability' (30 00 00 00 46 69 72 69 6E 67 20 61 74 20 73 68 6F 72 74 20 72 61 6E 67 65 20 70 65 6E 61 6C 74 79 20 6E 65 67 61 74 65 64 20 62 79 20 61 62 69 6C 69 74 79),
00000BB0                         INT: -1 (FF FF FF FF),
00000BB5                         STR: 'Melee at ranged penalty negated by ability' (2A 00 00 00 4D 65 6C 65 65 20 61 74 20 72 61 6E 67 65 64 20 70 65 6E 61 6C 74 79 20 6E 65 67 61 74 65 64 20 62 79 20 61 62 69 6C 69 74 79)
                             )
                         names:
00000BE4                     TUPLE: (
00000BE9                         STR: 'CU' (02 00 00 00 43 55),
00000BF0                         STR: 'isUsingWeapon' (0D 00 00 00 69 73 55 73 69 6E 67 57 65 61 70 6F 6E),
00000C02                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
00000C0F                         STR: 'equippedItemType' (10 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D 54 79 70 65),
00000C24                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
00000C2E                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
00000C3B                         STR: 'True' (04 00 00 00 54 72 75 65),
00000C44                         STR: 'base_modifier' (0D 00 00 00 62 61 73 65 5F 6D 6F 64 69 66 69 65 72),
00000C56                         STR: 'opponentCount' (0D 00 00 00 6F 70 70 6F 6E 65 6E 74 43 6F 75 6E 74),
00000C68                         STR: 'allowFiringIntoMeleePenalty' (1B 00 00 00 61 6C 6C 6F 77 46 69 72 69 6E 67 49 6E 74 6F 4D 65 6C 65 65 50 65 6E 61 6C 74 79),
00000C88                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
00000CA5                         STR: 'getBaseRangedValue' (12 00 00 00 67 65 74 42 61 73 65 52 61 6E 67 65 64 56 61 6C 75 65),
00000CBC                         STR: 'modifier' (08 00 00 00 6D 6F 64 69 66 69 65 72),
00000CC9                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00000CD4                         STR: 'distance' (08 00 00 00 64 69 73 74 61 6E 63 65),
00000CE1                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00000CEF                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
00000CFA                         STR: 'SHORT_RANGE' (0B 00 00 00 53 48 4F 52 54 5F 52 41 4E 47 45),
00000D0A                         STR: 'allowFiringAtMeleeRangePenalty' (1E 00 00 00 61 6C 6C 6F 77 46 69 72 69 6E 67 41 74 4D 65 6C 65 65 52 61 6E 67 65 50 65 6E 61 6C 74 79),
00000D2D                         STR: 'allowMeleeAtRangedPenalty' (19 00 00 00 61 6C 6C 6F 77 4D 65 6C 65 65 41 74 52 61 6E 67 65 64 50 65 6E 61 6C 74 79)
                             )
                         varnames:
00000D4B                     TUPLE: (
00000D50                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
00000D5D                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
00000D6A                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00000D75                         STR: 'base_modifier' (0D 00 00 00 62 61 73 65 5F 6D 6F 64 69 66 69 65 72),
00000D87                         STR: 'modifier' (08 00 00 00 6D 6F 64 69 66 69 65 72)
                             )
                         freevars:
00000D94                     TUPLE: ()
                         cellvars:
00000D99                     TUPLE: ()
                         filename:
00000D9E                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_modifiers.py' (52 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 6D 6F 64 69 66 69 65 72 73 2E 70 79)
                         name:
00000DF5                     STR: 'getRangedVsMeleeDefenseModifier' (1F 00 00 00 67 65 74 52 61 6E 67 65 64 56 73 4D 65 6C 65 65 44 65 66 65 6E 73 65 4D 6F 64 69 66 69 65 72)
                         firslineno:
00000E19                     LONG: 71L (47 00 00 00)
                         lnotab:
00000E1D                     STR: '\x00\x022\x01\x08\x03\x06\x01\x10\x01\n\x01\n\x02\x14\x03\x0c\x02\x16\x01\x10\x01\x10\x01\x08\x02\x0e\x03\x10\x01\x10\x01\x08\x02' (22 00 00 00 00 02 32 01 08 03 06 01 10 01 0A 01 0A 02 14 03 0C 02 16 01 10 01 10 01 08 02 0E 03 10 01 10 01 08 02),
00000E44             CODE:
                         argcount:
00000E45                     LONG: 1L (01 00 00 00)
                         nlocals:
00000E49                     LONG: 1L (01 00 00 00)
                         stacksize:
00000E4D                     LONG: 3L (03 00 00 00)
                         flags:
00000E51                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000E55                     STR: '|\x00\x00i\x01\x00t\x02\x00i\x03\x00j\x04\x00o8\x00\x01|\x00\x00i\x04\x00o\x0f\x00\x01|\x00\x00i\x01\x00d\x01\x00\x14SqO\x00\x01t\x05\x00i\x06\x00d\x02\x00|\x00\x00i\x07\x00\x16d\x03\x00\x83\x02\x00\x01d\x04\x00Sn\x05\x00\x01d\x04\x00Sd\x00\x00S' (53 00 00 00 7C 00 00 69 01 00 74 02 00 69 03 00 6A 04 00 6F 38 00 01 7C 00 00 69 04 00 6F 0F 00 01 7C 00 00 69 01 00 64 01 00 14 53 71 4F 00 01 74 05 00 69 06 00 64 02 00 7C 00 00 69 07 00 16 64 03 00 83 02 00 01 64 04 00 53 6E 05 00 01 64 04 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'player'
                             00000003     69 - LOAD_ATTR           'opponentCount'
                             00000006     74 - LOAD_GLOBAL         'consolevar'
                             00000009     69 - LOAD_ATTR           'CombatMultiOnOneCount'
                             0000000C     6A - COMPARE_OP          ">"
                             0000000F     6F - JUMP_IF_FALSE       -> 0000004A
                             00000012     01 - POP_TOP             
                             00000013     7C - LOAD_FAST           'player'
                             00000016     69 - LOAD_ATTR           'allowMultiOnOnePenalty'
                             00000019     6F - JUMP_IF_FALSE       -> 0000002B
                             0000001C     01 - POP_TOP             
                             0000001D     7C - LOAD_FAST           'player'
                             00000020     69 - LOAD_ATTR           'opponentCount'
                             00000023     64 - LOAD_CONST          -5
                             00000026     14 - BINARY_MULTIPLY     
                             00000027     53 - RETURN_VALUE        
                             00000028     71 - JUMP_ABSOLUTE       -> 0000004F
                             0000002B     01 - POP_TOP             
                             0000002C     74 - LOAD_GLOBAL         'CU'
                             0000002F     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000032     64 - LOAD_CONST          'Multi-on-one penalty negated due to ability for player %d'
                             00000035     7C - LOAD_FAST           'player'
                             00000038     69 - LOAD_ATTR           'slot'
                             0000003B     16 - BINARY_MODULO       
                             0000003C     64 - LOAD_CONST          3
                             0000003F     83 - CALL_FUNCTION       r0002
                             00000042     01 - POP_TOP             
                             00000043     64 - LOAD_CONST          0
                             00000046     53 - RETURN_VALUE        
                             00000047     6E - JUMP_FORWARD        -> 0000004F
                             0000004A     01 - POP_TOP             
                             0000004B     64 - LOAD_CONST          0
                             0000004E     53 - RETURN_VALUE        
                             0000004F     64 - LOAD_CONST          None
                             00000052     53 - RETURN_VALUE        
                         consts:
00000EAD                     TUPLE: (
00000EB2                         None (4E),
00000EB3                         INT: -5 (FB FF FF FF),
00000EB8                         STR: 'Multi-on-one penalty negated due to ability for player %d' (39 00 00 00 4D 75 6C 74 69 2D 6F 6E 2D 6F 6E 65 20 70 65 6E 61 6C 74 79 20 6E 65 67 61 74 65 64 20 64 75 65 20 74 6F 20 61 62 69 6C 69 74 79 20 66 6F 72 20 70 6C 61 79 65 72 20 25 64),
00000EF6                         INT: 3 (03 00 00 00),
00000EFB                         INT: 0 (00 00 00 00)
                             )
                         names:
00000F00                     TUPLE: (
00000F05                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00000F10                         STR: 'opponentCount' (0D 00 00 00 6F 70 70 6F 6E 65 6E 74 43 6F 75 6E 74),
00000F22                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
00000F31                         STR: 'CombatMultiOnOneCount' (15 00 00 00 43 6F 6D 62 61 74 4D 75 6C 74 69 4F 6E 4F 6E 65 43 6F 75 6E 74),
00000F4B                         STR: 'allowMultiOnOnePenalty' (16 00 00 00 61 6C 6C 6F 77 4D 75 6C 74 69 4F 6E 4F 6E 65 50 65 6E 61 6C 74 79),
00000F66                         STR: 'CU' (02 00 00 00 43 55),
00000F6D                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
00000F8A                         STR: 'slot' (04 00 00 00 73 6C 6F 74)
                             )
                         varnames:
00000F93                     TUPLE: (
00000F98                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72)
                             )
                         freevars:
00000FA3                     TUPLE: ()
                         cellvars:
00000FA8                     TUPLE: ()
                         filename:
00000FAD                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_modifiers.py' (52 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 6D 6F 64 69 66 69 65 72 73 2E 70 79)
                         name:
00001004                     STR: 'getOpponentCountModifier' (18 00 00 00 67 65 74 4F 70 70 6F 6E 65 6E 74 43 6F 75 6E 74 4D 6F 64 69 66 69 65 72)
                         firslineno:
00001021                     LONG: 103L (67 00 00 00)
                         lnotab:
00001025                     STR: '\x00\x01\x13\x01\n\x01\x0f\x02\x17\x01\x08\x02' (0C 00 00 00 00 01 13 01 0A 01 0F 02 17 01 08 02),
00001036             CODE:
                         argcount:
00001037                     LONG: 1L (01 00 00 00)
                         nlocals:
0000103B                     LONG: 1L (01 00 00 00)
                         stacksize:
0000103F                     LONG: 3L (03 00 00 00)
                         flags:
00001043                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001047                     STR: '|\x00\x00i\x01\x00t\x02\x00i\x03\x00j\x04\x00o[\x00\x01|\x00\x00i\x04\x00o\x0f\x00\x01|\x00\x00i\x05\x00d\x01\x00\x14Sqr\x00\x01|\x00\x00i\x05\x00d\x02\x00j\x00\x00o\x1f\x00\x01t\x06\x00i\x07\x00d\x03\x00|\x00\x00i\x08\x00\x16d\x02\x00\x83\x02\x00\x01d\x04\x00Sqr\x00\x01|\x00\x00i\x05\x00d\x05\x00\x18d\x01\x00\x14Sn\x05\x00\x01d\x04\x00Sd\x00\x00S' (76 00 00 00 7C 00 00 69 01 00 74 02 00 69 03 00 6A 04 00 6F 5B 00 01 7C 00 00 69 04 00 6F 0F 00 01 7C 00 00 69 05 00 64 01 00 14 53 71 72 00 01 7C 00 00 69 05 00 64 02 00 6A 00 00 6F 1F 00 01 74 06 00 69 07 00 64 03 00 7C 00 00 69 08 00 16 64 02 00 83 02 00 01 64 04 00 53 71 72 00 01 7C 00 00 69 05 00 64 05 00 18 64 01 00 14 53 6E 05 00 01 64 04 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'player'
                             00000003     69 - LOAD_ATTR           'opponentCount'
                             00000006     74 - LOAD_GLOBAL         'consolevar'
                             00000009     69 - LOAD_ATTR           'CombatMultiOnOneCount'
                             0000000C     6A - COMPARE_OP          ">"
                             0000000F     6F - JUMP_IF_FALSE       -> 0000006D
                             00000012     01 - POP_TOP             
                             00000013     7C - LOAD_FAST           'player'
                             00000016     69 - LOAD_ATTR           'allowMultiOnOnePenalty'
                             00000019     6F - JUMP_IF_FALSE       -> 0000002B
                             0000001C     01 - POP_TOP             
                             0000001D     7C - LOAD_FAST           'player'
                             00000020     69 - LOAD_ATTR           'opponentsFought'
                             00000023     64 - LOAD_CONST          -5
                             00000026     14 - BINARY_MULTIPLY     
                             00000027     53 - RETURN_VALUE        
                             00000028     71 - JUMP_ABSOLUTE       -> 00000072
                             0000002B     01 - POP_TOP             
                             0000002C     7C - LOAD_FAST           'player'
                             0000002F     69 - LOAD_ATTR           'opponentsFought'
                             00000032     64 - LOAD_CONST          3
                             00000035     6A - COMPARE_OP          "<"
                             00000038     6F - JUMP_IF_FALSE       -> 0000005A
                             0000003B     01 - POP_TOP             
                             0000003C     74 - LOAD_GLOBAL         'CU'
                             0000003F     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000042     64 - LOAD_CONST          'Multi-on-one penalty negated due to ability for player %d'
                             00000045     7C - LOAD_FAST           'player'
                             00000048     69 - LOAD_ATTR           'slot'
                             0000004B     16 - BINARY_MODULO       
                             0000004C     64 - LOAD_CONST          3
                             0000004F     83 - CALL_FUNCTION       r0002
                             00000052     01 - POP_TOP             
                             00000053     64 - LOAD_CONST          0
                             00000056     53 - RETURN_VALUE        
                             00000057     71 - JUMP_ABSOLUTE       -> 00000072
                             0000005A     01 - POP_TOP             
                             0000005B     7C - LOAD_FAST           'player'
                             0000005E     69 - LOAD_ATTR           'opponentsFought'
                             00000061     64 - LOAD_CONST          2
                             00000064     18 - BINARY_SUBTRACT     
                             00000065     64 - LOAD_CONST          -5
                             00000068     14 - BINARY_MULTIPLY     
                             00000069     53 - RETURN_VALUE        
                             0000006A     6E - JUMP_FORWARD        -> 00000072
                             0000006D     01 - POP_TOP             
                             0000006E     64 - LOAD_CONST          0
                             00000071     53 - RETURN_VALUE        
                             00000072     64 - LOAD_CONST          None
                             00000075     53 - RETURN_VALUE        
                         consts:
000010C2                     TUPLE: (
000010C7                         None (4E),
000010C8                         INT: -5 (FB FF FF FF),
000010CD                         INT: 3 (03 00 00 00),
000010D2                         STR: 'Multi-on-one penalty negated due to ability for player %d' (39 00 00 00 4D 75 6C 74 69 2D 6F 6E 2D 6F 6E 65 20 70 65 6E 61 6C 74 79 20 6E 65 67 61 74 65 64 20 64 75 65 20 74 6F 20 61 62 69 6C 69 74 79 20 66 6F 72 20 70 6C 61 79 65 72 20 25 64),
00001110                         INT: 0 (00 00 00 00),
00001115                         INT: 2 (02 00 00 00)
                             )
                         names:
0000111A                     TUPLE: (
0000111F                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
0000112A                         STR: 'opponentCount' (0D 00 00 00 6F 70 70 6F 6E 65 6E 74 43 6F 75 6E 74),
0000113C                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
0000114B                         STR: 'CombatMultiOnOneCount' (15 00 00 00 43 6F 6D 62 61 74 4D 75 6C 74 69 4F 6E 4F 6E 65 43 6F 75 6E 74),
00001165                         STR: 'allowMultiOnOnePenalty' (16 00 00 00 61 6C 6C 6F 77 4D 75 6C 74 69 4F 6E 4F 6E 65 50 65 6E 61 6C 74 79),
00001180                         STR: 'opponentsFought' (0F 00 00 00 6F 70 70 6F 6E 65 6E 74 73 46 6F 75 67 68 74),
00001194                         STR: 'CU' (02 00 00 00 43 55),
0000119B                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
000011B8                         STR: 'slot' (04 00 00 00 73 6C 6F 74)
                             )
                         varnames:
000011C1                     TUPLE: (
000011C6                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72)
                             )
                         freevars:
000011D1                     TUPLE: ()
                         cellvars:
000011D6                     TUPLE: ()
                         filename:
000011DB                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_modifiers.py' (52 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 6D 6F 64 69 66 69 65 72 73 2E 70 79)
                         name:
00001232                     STR: 'getMultiOnOnePenalty' (14 00 00 00 67 65 74 4D 75 6C 74 69 4F 6E 4F 6E 65 50 65 6E 61 6C 74 79)
                         firslineno:
0000124B                     LONG: 114L (72 00 00 00)
                         lnotab:
0000124F                     STR: '\x00\x01\x13\x01\n\x01\x0f\x02\x10\x01\x17\x01\x08\x02\x13\x02' (10 00 00 00 00 01 13 01 0A 01 0F 02 10 01 17 01 08 02 13 02),
00001264             CODE:
                         argcount:
00001265                     LONG: 3L (03 00 00 00)
                         nlocals:
00001269                     LONG: 6L (06 00 00 00)
                         stacksize:
0000126D                     LONG: 4L (04 00 00 00)
                         flags:
00001271                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001275                     STR: 't\x00\x00|\x00\x00\x83\x01\x00}\x05\x00t\x03\x00|\x00\x00|\x01\x00|\x02\x00\x83\x03\x00}\x03\x00|\x05\x00|\x03\x00\x17}\x04\x00|\x04\x00Sd\x00\x00S' (30 00 00 00 74 00 00 7C 00 00 83 01 00 7D 05 00 74 03 00 7C 00 00 7C 01 00 7C 02 00 83 03 00 7D 03 00 7C 05 00 7C 03 00 17 7D 04 00 7C 04 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'getMultiOnOnePenalty'
                             00000003     7C - LOAD_FAST           'attacker'
                             00000006     83 - CALL_FUNCTION       r0001
                             00000009     7D - STORE_FAST          'multiMod'
                             0000000C     74 - LOAD_GLOBAL         'getRangedVsMeleeAttackModifier'
                             0000000F     7C - LOAD_FAST           'attacker'
                             00000012     7C - LOAD_FAST           'defender'
                             00000015     7C - LOAD_FAST           'result'
                             00000018     83 - CALL_FUNCTION       r0003
                             0000001B     7D - STORE_FAST          'rangedMod'
                             0000001E     7C - LOAD_FAST           'multiMod'
                             00000021     7C - LOAD_FAST           'rangedMod'
                             00000024     17 - BINARY_ADD          
                             00000025     7D - STORE_FAST          'out_modifier'
                             00000028     7C - LOAD_FAST           'out_modifier'
                             0000002B     53 - RETURN_VALUE        
                             0000002C     64 - LOAD_CONST          None
                             0000002F     53 - RETURN_VALUE        
                         consts:
000012AA                     TUPLE: (
000012AF                         None (4E)
                             )
                         names:
000012B0                     TUPLE: (
000012B5                         STR: 'getMultiOnOnePenalty' (14 00 00 00 67 65 74 4D 75 6C 74 69 4F 6E 4F 6E 65 50 65 6E 61 6C 74 79),
000012CE                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
000012DB                         STR: 'multiMod' (08 00 00 00 6D 75 6C 74 69 4D 6F 64),
000012E8                         STR: 'getRangedVsMeleeAttackModifier' (1E 00 00 00 67 65 74 52 61 6E 67 65 64 56 73 4D 65 6C 65 65 41 74 74 61 63 6B 4D 6F 64 69 66 69 65 72),
0000130B                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
00001318                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00001323                         STR: 'rangedMod' (09 00 00 00 72 61 6E 67 65 64 4D 6F 64),
00001331                         STR: 'out_modifier' (0C 00 00 00 6F 75 74 5F 6D 6F 64 69 66 69 65 72)
                             )
                         varnames:
00001342                     TUPLE: (
00001347                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
00001354                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
00001361                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
0000136C                         STR: 'rangedMod' (09 00 00 00 72 61 6E 67 65 64 4D 6F 64),
0000137A                         STR: 'out_modifier' (0C 00 00 00 6F 75 74 5F 6D 6F 64 69 66 69 65 72),
0000138B                         STR: 'multiMod' (08 00 00 00 6D 75 6C 74 69 4D 6F 64)
                             )
                         freevars:
00001398                     TUPLE: ()
                         cellvars:
0000139D                     TUPLE: ()
                         filename:
000013A2                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_modifiers.py' (52 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 6D 6F 64 69 66 69 65 72 73 2E 70 79)
                         name:
000013F9                     STR: 'getAttackerMods' (0F 00 00 00 67 65 74 41 74 74 61 63 6B 65 72 4D 6F 64 73)
                         firslineno:
0000140D                     LONG: 127L (7F 00 00 00)
                         lnotab:
00001411                     STR: '\x00\x01\x0c\x01\x12\x02\n\x02' (08 00 00 00 00 01 0C 01 12 02 0A 02),
0000141E             CODE:
                         argcount:
0000141F                     LONG: 3L (03 00 00 00)
                         nlocals:
00001423                     LONG: 6L (06 00 00 00)
                         stacksize:
00001427                     LONG: 4L (04 00 00 00)
                         flags:
0000142B                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000142F                     STR: 't\x00\x00|\x01\x00\x83\x01\x00}\x05\x00t\x03\x00|\x00\x00|\x01\x00|\x02\x00\x83\x03\x00}\x03\x00|\x05\x00|\x03\x00\x17}\x04\x00|\x04\x00Sd\x00\x00S' (30 00 00 00 74 00 00 7C 01 00 83 01 00 7D 05 00 74 03 00 7C 00 00 7C 01 00 7C 02 00 83 03 00 7D 03 00 7C 05 00 7C 03 00 17 7D 04 00 7C 04 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'getMultiOnOnePenalty'
                             00000003     7C - LOAD_FAST           'defender'
                             00000006     83 - CALL_FUNCTION       r0001
                             00000009     7D - STORE_FAST          'multiMod'
                             0000000C     74 - LOAD_GLOBAL         'getRangedVsMeleeDefenseModifier'
                             0000000F     7C - LOAD_FAST           'attacker'
                             00000012     7C - LOAD_FAST           'defender'
                             00000015     7C - LOAD_FAST           'result'
                             00000018     83 - CALL_FUNCTION       r0003
                             0000001B     7D - STORE_FAST          'rangedMod'
                             0000001E     7C - LOAD_FAST           'multiMod'
                             00000021     7C - LOAD_FAST           'rangedMod'
                             00000024     17 - BINARY_ADD          
                             00000025     7D - STORE_FAST          'out_modifier'
                             00000028     7C - LOAD_FAST           'out_modifier'
                             0000002B     53 - RETURN_VALUE        
                             0000002C     64 - LOAD_CONST          None
                             0000002F     53 - RETURN_VALUE        
                         consts:
00001464                     TUPLE: (
00001469                         None (4E)
                             )
                         names:
0000146A                     TUPLE: (
0000146F                         STR: 'getMultiOnOnePenalty' (14 00 00 00 67 65 74 4D 75 6C 74 69 4F 6E 4F 6E 65 50 65 6E 61 6C 74 79),
00001488                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
00001495                         STR: 'multiMod' (08 00 00 00 6D 75 6C 74 69 4D 6F 64),
000014A2                         STR: 'getRangedVsMeleeDefenseModifier' (1F 00 00 00 67 65 74 52 61 6E 67 65 64 56 73 4D 65 6C 65 65 44 65 66 65 6E 73 65 4D 6F 64 69 66 69 65 72),
000014C6                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
000014D3                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
000014DE                         STR: 'rangedMod' (09 00 00 00 72 61 6E 67 65 64 4D 6F 64),
000014EC                         STR: 'out_modifier' (0C 00 00 00 6F 75 74 5F 6D 6F 64 69 66 69 65 72)
                             )
                         varnames:
000014FD                     TUPLE: (
00001502                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
0000150F                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
0000151C                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00001527                         STR: 'rangedMod' (09 00 00 00 72 61 6E 67 65 64 4D 6F 64),
00001535                         STR: 'out_modifier' (0C 00 00 00 6F 75 74 5F 6D 6F 64 69 66 69 65 72),
00001546                         STR: 'multiMod' (08 00 00 00 6D 75 6C 74 69 4D 6F 64)
                             )
                         freevars:
00001553                     TUPLE: ()
                         cellvars:
00001558                     TUPLE: ()
                         filename:
0000155D                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_modifiers.py' (52 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 6D 6F 64 69 66 69 65 72 73 2E 70 79)
                         name:
000015B4                     STR: 'getDefenderMods' (0F 00 00 00 67 65 74 44 65 66 65 6E 64 65 72 4D 6F 64 73)
                         firslineno:
000015C8                     LONG: 137L (89 00 00 00)
                         lnotab:
000015CC                     STR: '\x00\x01\x0c\x01\x12\x02\n\x02' (08 00 00 00 00 01 0C 01 12 02 0A 02)
                 )
             names:
000015D9         TUPLE: (
000015DE             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
000015E9             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
000015F7             STR: 'obj' (03 00 00 00 6F 62 6A),
000015FF             STR: 'combat_defines' (0E 00 00 00 63 6F 6D 62 61 74 5F 64 65 66 69 6E 65 73),
00001612             STR: 'CD' (02 00 00 00 43 44),
00001619             STR: 'math' (04 00 00 00 6D 61 74 68),
00001622             STR: 'combat_utility' (0E 00 00 00 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79),
00001635             STR: 'CU' (02 00 00 00 43 55),
0000163C             STR: '_COMBAT_PREFERRED_TACTICAL_BONUS' (20 00 00 00 5F 43 4F 4D 42 41 54 5F 50 52 45 46 45 52 52 45 44 5F 54 41 43 54 49 43 41 4C 5F 42 4F 4E 55 53),
00001661             STR: 'getTacticalMod' (0E 00 00 00 67 65 74 54 61 63 74 69 63 61 6C 4D 6F 64),
00001674             STR: 'getTacticSpecificArmorPiercingPercent' (25 00 00 00 67 65 74 54 61 63 74 69 63 53 70 65 63 69 66 69 63 41 72 6D 6F 72 50 69 65 72 63 69 6E 67 50 65 72 63 65 6E 74),
0000169E             STR: 'getBaseRangedValue' (12 00 00 00 67 65 74 42 61 73 65 52 61 6E 67 65 64 56 61 6C 75 65),
000016B5             STR: 'getRangedVsMeleeAttackModifier' (1E 00 00 00 67 65 74 52 61 6E 67 65 64 56 73 4D 65 6C 65 65 41 74 74 61 63 6B 4D 6F 64 69 66 69 65 72),
000016D8             STR: 'getRangedVsMeleeDefenseModifier' (1F 00 00 00 67 65 74 52 61 6E 67 65 64 56 73 4D 65 6C 65 65 44 65 66 65 6E 73 65 4D 6F 64 69 66 69 65 72),
000016FC             STR: 'getOpponentCountModifier' (18 00 00 00 67 65 74 4F 70 70 6F 6E 65 6E 74 43 6F 75 6E 74 4D 6F 64 69 66 69 65 72),
00001719             STR: 'getMultiOnOnePenalty' (14 00 00 00 67 65 74 4D 75 6C 74 69 4F 6E 4F 6E 65 50 65 6E 61 6C 74 79),
00001732             STR: 'getAttackerMods' (0F 00 00 00 67 65 74 41 74 74 61 63 6B 65 72 4D 6F 64 73),
00001746             STR: 'getDefenderMods' (0F 00 00 00 67 65 74 44 65 66 65 6E 64 65 72 4D 6F 64 73)
                 )
             varnames:
0000175A         TUPLE: (
0000175F             STR: 'getMultiOnOnePenalty' (14 00 00 00 67 65 74 4D 75 6C 74 69 4F 6E 4F 6E 65 50 65 6E 61 6C 74 79),
00001778             STR: 'getTacticSpecificArmorPiercingPercent' (25 00 00 00 67 65 74 54 61 63 74 69 63 53 70 65 63 69 66 69 63 41 72 6D 6F 72 50 69 65 72 63 69 6E 67 50 65 72 63 65 6E 74),
000017A2             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
000017B0             STR: 'obj' (03 00 00 00 6F 62 6A),
000017B8             STR: 'getDefenderMods' (0F 00 00 00 67 65 74 44 65 66 65 6E 64 65 72 4D 6F 64 73),
000017CC             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
000017D7             STR: 'getRangedVsMeleeAttackModifier' (1E 00 00 00 67 65 74 52 61 6E 67 65 64 56 73 4D 65 6C 65 65 41 74 74 61 63 6B 4D 6F 64 69 66 69 65 72),
000017FA             STR: 'CD' (02 00 00 00 43 44),
00001801             STR: 'getAttackerMods' (0F 00 00 00 67 65 74 41 74 74 61 63 6B 65 72 4D 6F 64 73),
00001815             STR: 'getOpponentCountModifier' (18 00 00 00 67 65 74 4F 70 70 6F 6E 65 6E 74 43 6F 75 6E 74 4D 6F 64 69 66 69 65 72),
00001832             STR: 'getRangedVsMeleeDefenseModifier' (1F 00 00 00 67 65 74 52 61 6E 67 65 64 56 73 4D 65 6C 65 65 44 65 66 65 6E 73 65 4D 6F 64 69 66 69 65 72),
00001856             STR: 'math' (04 00 00 00 6D 61 74 68),
0000185F             STR: 'getTacticalMod' (0E 00 00 00 67 65 74 54 61 63 74 69 63 61 6C 4D 6F 64),
00001872             STR: 'getBaseRangedValue' (12 00 00 00 67 65 74 42 61 73 65 52 61 6E 67 65 64 56 61 6C 75 65),
00001889             STR: 'CU' (02 00 00 00 43 55),
00001890             STR: '_COMBAT_PREFERRED_TACTICAL_BONUS' (20 00 00 00 5F 43 4F 4D 42 41 54 5F 50 52 45 46 45 52 52 45 44 5F 54 41 43 54 49 43 41 4C 5F 42 4F 4E 55 53)
                 )
             freevars:
000018B5         TUPLE: ()
             cellvars:
000018BA         TUPLE: ()
             filename:
000018BF         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_modifiers.py' (52 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 6D 6F 64 69 66 69 65 72 73 2E 70 79)
             name:
00001916         STR: '?' (01 00 00 00 3F)
             firslineno:
0000191C         LONG: 1L (01 00 00 00)
             lnotab:
00001920         STR: '\t\x01\t\x01\t\x01\t\x01\t\x01\t\x02\x06\x01\t\x07\t\t\t\x0f\t\x1f\t \t\x0b\t\r\t\n' (1E 00 00 00 09 01 09 01 09 01 09 01 09 01 09 02 06 01 09 07 09 09 09 0F 09 1F 09 20 09 0B 09 0D 09 0A)

