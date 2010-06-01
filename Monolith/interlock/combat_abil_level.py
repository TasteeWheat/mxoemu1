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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00Z\x02\x00d\x00\x00k\x03\x00Z\x04\x00d\x00\x00k\x05\x00Z\x05\x00d\x00\x00k\x06\x00Z\x07\x00d\x00\x00k\x08\x00Z\t\x00d\x01\x00\x84\x00\x00Z\n\x00e\x0b\x00e\x0c\x00e\r\x00g\x03\x00Z\x0e\x00d\x02\x00\x84\x00\x00Z\x0f\x00d\x03\x00\x84\x00\x00Z\x10\x00d\x04\x00\x84\x00\x00Z\x11\x00d\x05\x00\x84\x00\x00Z\x12\x00d\x06\x00\x84\x00\x00Z\x13\x00d\x07\x00\x84\x00\x00Z\x14\x00d\x08\x00\x84\x00\x00Z\x15\x00d\t\x00Z\x16\x00d\n\x00Z\x17\x00d\x0b\x00\x84\x00\x00Z\x18\x00d\x0c\x00\x84\x00\x00Z\x19\x00d\r\x00\x84\x00\x00Z\x1a\x00d\x0e\x00\x84\x00\x00Z\x1b\x00d\x00\x00S' (CA 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 5A 02 00 64 00 00 6B 03 00 5A 04 00 64 00 00 6B 05 00 5A 05 00 64 00 00 6B 06 00 5A 07 00 64 00 00 6B 08 00 5A 09 00 64 01 00 84 00 00 5A 0A 00 65 0B 00 65 0C 00 65 0D 00 67 03 00 5A 0E 00 64 02 00 84 00 00 5A 0F 00 64 03 00 84 00 00 5A 10 00 64 04 00 84 00 00 5A 11 00 64 05 00 84 00 00 5A 12 00 64 06 00 84 00 00 5A 13 00 64 07 00 84 00 00 5A 14 00 64 08 00 84 00 00 5A 15 00 64 09 00 5A 16 00 64 0A 00 5A 17 00 64 0B 00 84 00 00 5A 18 00 64 0C 00 84 00 00 5A 19 00 64 0D 00 84 00 00 5A 1A 00 64 0E 00 84 00 00 5A 1B 00 64 00 00 53)
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
                 00000036     64 - LOAD_CONST          None
                 00000039     6B - IMPORT_NAME         'combat_innerstrength'
                 0000003C     5A - STORE_NAME          'CI'
                 0000003F     64 - LOAD_CONST          CODE('getTacticalInitiativeBonus')
                 00000042     84 - MAKE_FUNCTION       r0000
                 00000045     5A - STORE_NAME          'getTacticalInitiativeBonus'
                 00000048     65 - LOAD_NAME           'KarateAbility'
                 0000004B     65 - LOAD_NAME           'KungFuAbility'
                 0000004E     65 - LOAD_NAME           'AikidoAbility'
                 00000051     67 - BUILD_LIST          r0003
                 00000054     5A - STORE_NAME          '_MartialArtList'
                 00000057     64 - LOAD_CONST          CODE('abilityLevel')
                 0000005A     84 - MAKE_FUNCTION       r0000
                 0000005D     5A - STORE_NAME          'abilityLevel'
                 00000060     64 - LOAD_CONST          CODE('getBaseAbilityLevel')
                 00000063     84 - MAKE_FUNCTION       r0000
                 00000066     5A - STORE_NAME          'getBaseAbilityLevel'
                 00000069     64 - LOAD_CONST          CODE('GetMasteryLevel')
                 0000006C     84 - MAKE_FUNCTION       r0000
                 0000006F     5A - STORE_NAME          'GetMasteryLevel'
                 00000072     64 - LOAD_CONST          CODE('GetItemAbilityLevel')
                 00000075     84 - MAKE_FUNCTION       r0000
                 00000078     5A - STORE_NAME          'GetItemAbilityLevel'
                 0000007B     64 - LOAD_CONST          CODE('SelectItemAbilityLevel')
                 0000007E     84 - MAKE_FUNCTION       r0000
                 00000081     5A - STORE_NAME          'SelectItemAbilityLevel'
                 00000084     64 - LOAD_CONST          CODE('SelectCombatAbilityLevel')
                 00000087     84 - MAKE_FUNCTION       r0000
                 0000008A     5A - STORE_NAME          'SelectCombatAbilityLevel'
                 0000008D     64 - LOAD_CONST          CODE('isUsingWeapon')
                 00000090     84 - MAKE_FUNCTION       r0000
                 00000093     5A - STORE_NAME          'isUsingWeapon'
                 00000096     64 - LOAD_CONST          25
                 00000099     5A - STORE_NAME          '_PRIMARY_TACTICAL_SETTING_SYNERGY_MOD'
                 0000009C     64 - LOAD_CONST          15
                 0000009F     5A - STORE_NAME          '_SECONDARY_TACTICAL_SETTING_SYNERGY_MOD'
                 000000A2     64 - LOAD_CONST          CODE('getMartialArtAbilityMod')
                 000000A5     84 - MAKE_FUNCTION       r0000
                 000000A8     5A - STORE_NAME          'getMartialArtAbilityMod'
                 000000AB     64 - LOAD_CONST          CODE('getItemAbilityMod')
                 000000AE     84 - MAKE_FUNCTION       r0000
                 000000B1     5A - STORE_NAME          'getItemAbilityMod'
                 000000B4     64 - LOAD_CONST          CODE('SetCombatTargetSettings')
                 000000B7     84 - MAKE_FUNCTION       r0000
                 000000BA     5A - STORE_NAME          'SetCombatTargetSettings'
                 000000BD     64 - LOAD_CONST          CODE('GetFreeAttackAbility')
                 000000C0     84 - MAKE_FUNCTION       r0000
                 000000C3     5A - STORE_NAME          'GetFreeAttackAbility'
                 000000C6     64 - LOAD_CONST          None
                 000000C9     53 - RETURN_VALUE        
             consts:
000000E8         TUPLE: (
000000ED             None (4E),
000000EE             CODE:
                         argcount:
000000EF                     LONG: 1L (01 00 00 00)
                         nlocals:
000000F3                     LONG: 2L (02 00 00 00)
                         stacksize:
000000F7                     LONG: 3L (03 00 00 00)
                         flags:
000000FB                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000000FF                     STR: 'd\x01\x00d\x02\x00d\x03\x00g\x03\x00}\x01\x00|\x00\x00t\x02\x00i\x03\x00i\x04\x00j\x05\x00o\x10\x00\x01|\x00\x00t\x02\x00i\x03\x00i\x05\x00j\x01\x00o\x0c\x00\x01|\x01\x00|\x00\x00\x19Sn\x01\x00\x01d\x03\x00Sd\x00\x00S' (49 00 00 00 64 01 00 64 02 00 64 03 00 67 03 00 7D 01 00 7C 00 00 74 02 00 69 03 00 69 04 00 6A 05 00 6F 10 00 01 7C 00 00 74 02 00 69 03 00 69 05 00 6A 01 00 6F 0C 00 01 7C 01 00 7C 00 00 19 53 6E 01 00 01 64 03 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          20
                             00000003     64 - LOAD_CONST          10
                             00000006     64 - LOAD_CONST          0
                             00000009     67 - BUILD_LIST          r0003
                             0000000C     7D - STORE_FAST          'tactical_initiatives'
                             0000000F     7C - LOAD_FAST           'tacticalSetting'
                             00000012     74 - LOAD_GLOBAL         'constants'
                             00000015     69 - LOAD_ATTR           'combat'
                             00000018     69 - LOAD_ATTR           'DEFENSE'
                             0000001B     6A - COMPARE_OP          ">="
                             0000001E     6F - JUMP_IF_FALSE       -> 00000031
                             00000021     01 - POP_TOP             
                             00000022     7C - LOAD_FAST           'tacticalSetting'
                             00000025     74 - LOAD_GLOBAL         'constants'
                             00000028     69 - LOAD_ATTR           'combat'
                             0000002B     69 - LOAD_ATTR           'SPEED'
                             0000002E     6A - COMPARE_OP          "<="
                             00000031     6F - JUMP_IF_FALSE       -> 00000040
                             00000034     01 - POP_TOP             
                             00000035     7C - LOAD_FAST           'tactical_initiatives'
                             00000038     7C - LOAD_FAST           'tacticalSetting'
                             0000003B     19 - BINARY_SUBSCR       
                             0000003C     53 - RETURN_VALUE        
                             0000003D     6E - JUMP_FORWARD        -> 00000041
                             00000040     01 - POP_TOP             
                             00000041     64 - LOAD_CONST          0
                             00000044     53 - RETURN_VALUE        
                             00000045     64 - LOAD_CONST          None
                             00000048     53 - RETURN_VALUE        
                         consts:
0000014D                     TUPLE: (
00000152                         None (4E),
00000153                         INT: 20 (14 00 00 00),
00000158                         INT: 10 (0A 00 00 00),
0000015D                         INT: 0 (00 00 00 00)
                             )
                         names:
00000162                     TUPLE: (
00000167                         STR: 'tactical_initiatives' (14 00 00 00 74 61 63 74 69 63 61 6C 5F 69 6E 69 74 69 61 74 69 76 65 73),
00000180                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
00000194                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
000001A2                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
000001AD                         STR: 'DEFENSE' (07 00 00 00 44 45 46 45 4E 53 45),
000001B9                         STR: 'SPEED' (05 00 00 00 53 50 45 45 44)
                             )
                         varnames:
000001C3                     TUPLE: (
000001C8                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
000001DC                         STR: 'tactical_initiatives' (14 00 00 00 74 61 63 74 69 63 61 6C 5F 69 6E 69 74 69 61 74 69 76 65 73)
                             )
                         freevars:
000001F5                     TUPLE: ()
                         cellvars:
000001FA                     TUPLE: ()
                         filename:
000001FF                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_abil_level.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 61 62 69 6C 5F 6C 65 76 65 6C 2E 70 79)
                         name:
00000257                     STR: 'getTacticalInitiativeBonus' (1A 00 00 00 67 65 74 54 61 63 74 69 63 61 6C 49 6E 69 74 69 61 74 69 76 65 42 6F 6E 75 73)
                         firslineno:
00000276                     LONG: 9L (09 00 00 00)
                         lnotab:
0000027A                     STR: '\x00\x01\x0f\x04&\x01\x0c\x02' (08 00 00 00 00 01 0F 04 26 01 0C 02),
00000287             CODE:
                         argcount:
00000288                     LONG: 2L (02 00 00 00)
                         nlocals:
0000028C                     LONG: 2L (02 00 00 00)
                         stacksize:
00000290                     LONG: 3L (03 00 00 00)
                         flags:
00000294                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000298                     STR: '|\x00\x00i\x01\x00|\x01\x00\x19o\x18\x00\x01t\x03\x00i\x04\x00|\x00\x00i\x05\x00|\x01\x00\x19\x83\x01\x00Sn\x05\x00\x01d\x01\x00Sd\x00\x00S' (2E 00 00 00 7C 00 00 69 01 00 7C 01 00 19 6F 18 00 01 74 03 00 69 04 00 7C 00 00 69 05 00 7C 01 00 19 83 01 00 53 6E 05 00 01 64 01 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'player'
                             00000003     69 - LOAD_ATTR           'hasAbility'
                             00000006     7C - LOAD_FAST           'ability'
                             00000009     19 - BINARY_SUBSCR       
                             0000000A     6F - JUMP_IF_FALSE       -> 00000025
                             0000000D     01 - POP_TOP             
                             0000000E     74 - LOAD_GLOBAL         'CU'
                             00000011     69 - LOAD_ATTR           'safeAbVal'
                             00000014     7C - LOAD_FAST           'player'
                             00000017     69 - LOAD_ATTR           'abilities'
                             0000001A     7C - LOAD_FAST           'ability'
                             0000001D     19 - BINARY_SUBSCR       
                             0000001E     83 - CALL_FUNCTION       r0001
                             00000021     53 - RETURN_VALUE        
                             00000022     6E - JUMP_FORWARD        -> 0000002A
                             00000025     01 - POP_TOP             
                             00000026     64 - LOAD_CONST          -10000
                             00000029     53 - RETURN_VALUE        
                             0000002A     64 - LOAD_CONST          None
                             0000002D     53 - RETURN_VALUE        
                         consts:
000002CB                     TUPLE: (
000002D0                         None (4E),
000002D1                         INT: -10000 (F0 D8 FF FF)
                             )
                         names:
000002D6                     TUPLE: (
000002DB                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
000002E6                         STR: 'hasAbility' (0A 00 00 00 68 61 73 41 62 69 6C 69 74 79),
000002F5                         STR: 'ability' (07 00 00 00 61 62 69 6C 69 74 79),
00000301                         STR: 'CU' (02 00 00 00 43 55),
00000308                         STR: 'safeAbVal' (09 00 00 00 73 61 66 65 41 62 56 61 6C),
00000316                         STR: 'abilities' (09 00 00 00 61 62 69 6C 69 74 69 65 73)
                             )
                         varnames:
00000324                     TUPLE: (
00000329                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00000334                         STR: 'ability' (07 00 00 00 61 62 69 6C 69 74 79)
                             )
                         freevars:
00000340                     TUPLE: ()
                         cellvars:
00000345                     TUPLE: ()
                         filename:
0000034A                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_abil_level.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 61 62 69 6C 5F 6C 65 76 65 6C 2E 70 79)
                         name:
000003A2                     STR: 'abilityLevel' (0C 00 00 00 61 62 69 6C 69 74 79 4C 65 76 65 6C)
                         firslineno:
000003B3                     LONG: 21L (15 00 00 00)
                         lnotab:
000003B7                     STR: '\x00\x01\x0e\x01\x18\x02' (06 00 00 00 00 01 0E 01 18 02),
000003C2             CODE:
                         argcount:
000003C3                     LONG: 1L (01 00 00 00)
                         nlocals:
000003C7                     LONG: 1L (01 00 00 00)
                         stacksize:
000003CB                     LONG: 4L (04 00 00 00)
                         flags:
000003CF                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000003D3                     STR: '|\x00\x00i\x01\x00t\x02\x00\x19o\x17\x00\x01t\x02\x00t\x03\x00|\x00\x00t\x02\x00\x83\x02\x00f\x02\x00Sn\x01\x00\x01t\x02\x00d\x01\x00f\x02\x00Sd\x00\x00S' (33 00 00 00 7C 00 00 69 01 00 74 02 00 19 6F 17 00 01 74 02 00 74 03 00 7C 00 00 74 02 00 83 02 00 66 02 00 53 6E 01 00 01 74 02 00 64 01 00 66 02 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'player'
                             00000003     69 - LOAD_ATTR           'hasAbility'
                             00000006     74 - LOAD_GLOBAL         'AwakenedAbility'
                             00000009     19 - BINARY_SUBSCR       
                             0000000A     6F - JUMP_IF_FALSE       -> 00000024
                             0000000D     01 - POP_TOP             
                             0000000E     74 - LOAD_GLOBAL         'AwakenedAbility'
                             00000011     74 - LOAD_GLOBAL         'abilityLevel'
                             00000014     7C - LOAD_FAST           'player'
                             00000017     74 - LOAD_GLOBAL         'AwakenedAbility'
                             0000001A     83 - CALL_FUNCTION       r0002
                             0000001D     66 - BUILD_TUPLE         r0002
                             00000020     53 - RETURN_VALUE        
                             00000021     6E - JUMP_FORWARD        -> 00000025
                             00000024     01 - POP_TOP             
                             00000025     74 - LOAD_GLOBAL         'AwakenedAbility'
                             00000028     64 - LOAD_CONST          0
                             0000002B     66 - BUILD_TUPLE         r0002
                             0000002E     53 - RETURN_VALUE        
                             0000002F     64 - LOAD_CONST          None
                             00000032     53 - RETURN_VALUE        
                         consts:
0000040B                     TUPLE: (
00000410                         None (4E),
00000411                         INT: 0 (00 00 00 00)
                             )
                         names:
00000416                     TUPLE: (
0000041B                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00000426                         STR: 'hasAbility' (0A 00 00 00 68 61 73 41 62 69 6C 69 74 79),
00000435                         STR: 'AwakenedAbility' (0F 00 00 00 41 77 61 6B 65 6E 65 64 41 62 69 6C 69 74 79),
00000449                         STR: 'abilityLevel' (0C 00 00 00 61 62 69 6C 69 74 79 4C 65 76 65 6C)
                             )
                         varnames:
0000045A                     TUPLE: (
0000045F                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72)
                             )
                         freevars:
0000046A                     TUPLE: ()
                         cellvars:
0000046F                     TUPLE: ()
                         filename:
00000474                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_abil_level.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 61 62 69 6C 5F 6C 65 76 65 6C 2E 70 79)
                         name:
000004CC                     STR: 'getBaseAbilityLevel' (13 00 00 00 67 65 74 42 61 73 65 41 62 69 6C 69 74 79 4C 65 76 65 6C)
                         firslineno:
000004E4                     LONG: 27L (1B 00 00 00)
                         lnotab:
000004E8                     STR: '\x00\x02\x0e\x01\x17\x03' (06 00 00 00 00 02 0E 01 17 03),
000004F3             CODE:
                         argcount:
000004F4                     LONG: 2L (02 00 00 00)
                         nlocals:
000004F8                     LONG: 2L (02 00 00 00)
                         stacksize:
000004FC                     LONG: 2L (02 00 00 00)
                         flags:
00000500                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000504                     STR: '|\x01\x00t\x01\x00j\x02\x00o\x08\x00\x01d\x01\x00Sn\x01\x00\x01d\x01\x00Sd\x00\x00S' (1D 00 00 00 7C 01 00 74 01 00 6A 02 00 6F 08 00 01 64 01 00 53 6E 01 00 01 64 01 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'ability'
                             00000003     74 - LOAD_GLOBAL         'InvalidAbility'
                             00000006     6A - COMPARE_OP          "=="
                             00000009     6F - JUMP_IF_FALSE       -> 00000014
                             0000000C     01 - POP_TOP             
                             0000000D     64 - LOAD_CONST          0
                             00000010     53 - RETURN_VALUE        
                             00000011     6E - JUMP_FORWARD        -> 00000015
                             00000014     01 - POP_TOP             
                             00000015     64 - LOAD_CONST          0
                             00000018     53 - RETURN_VALUE        
                             00000019     64 - LOAD_CONST          None
                             0000001C     53 - RETURN_VALUE        
                         consts:
00000526                     TUPLE: (
0000052B                         None (4E),
0000052C                         INT: 0 (00 00 00 00)
                             )
                         names:
00000531                     TUPLE: (
00000536                         STR: 'ability' (07 00 00 00 61 62 69 6C 69 74 79),
00000542                         STR: 'InvalidAbility' (0E 00 00 00 49 6E 76 61 6C 69 64 41 62 69 6C 69 74 79)
                             )
                         varnames:
00000555                     TUPLE: (
0000055A                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00000565                         STR: 'ability' (07 00 00 00 61 62 69 6C 69 74 79)
                             )
                         freevars:
00000571                     TUPLE: ()
                         cellvars:
00000576                     TUPLE: ()
                         filename:
0000057B                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_abil_level.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 61 62 69 6C 5F 6C 65 76 65 6C 2E 70 79)
                         name:
000005D3                     STR: 'GetMasteryLevel' (0F 00 00 00 47 65 74 4D 61 73 74 65 72 79 4C 65 76 65 6C)
                         firslineno:
000005E7                     LONG: 36L (24 00 00 00)
                         lnotab:
000005EB                     STR: '\x00\x01\r\x01\x08\x1e' (06 00 00 00 00 01 0D 01 08 1E),
000005F6             CODE:
                         argcount:
000005F7                     LONG: 3L (03 00 00 00)
                         nlocals:
000005FB                     LONG: 5L (05 00 00 00)
                         stacksize:
000005FF                     LONG: 4L (04 00 00 00)
                         flags:
00000603                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000607                     STR: 't\x00\x00}\x03\x00d\x01\x00}\x04\x00|\x01\x00t\x04\x00i\x05\x00i\x06\x00j\x02\x00o\x1c\x00\x01|\x02\x00i\x08\x00t\t\x00\x19o\n\x00\x01t\t\x00}\x03\x00q\xdb\x00\x01n\xa1\x00\x01|\x01\x00t\x04\x00i\x05\x00i\n\x00j\x02\x00o\x1c\x00\x01|\x02\x00i\x08\x00t\t\x00\x19o\n\x00\x01t\t\x00}\x03\x00q\xdb\x00\x01nr\x00\x01|\x01\x00t\x04\x00i\x05\x00i\x0b\x00j\x02\x00p\x10\x00\x01|\x01\x00t\x04\x00i\x05\x00i\x0c\x00j\x02\x00o\x1c\x00\x01|\x02\x00i\x08\x00t\r\x00\x19o\n\x00\x01t\r\x00}\x03\x00q\xdb\x00\x01n0\x00\x01|\x01\x00t\x04\x00i\x05\x00i\x0e\x00j\x02\x00o\x1c\x00\x01|\x02\x00i\x08\x00t\x0f\x00\x19o\n\x00\x01t\x0f\x00}\x03\x00q\xdb\x00\x01n\x01\x00\x01|\x03\x00t\x00\x00j\x03\x00o\x11\x00\x01|\x02\x00i\x10\x00|\x03\x00\x19}\x04\x00n\x01\x00\x01|\x04\x00t\x11\x00|\x02\x00|\x03\x00\x83\x02\x007}\x04\x00|\x03\x00|\x04\x00f\x02\x00Sd\x00\x00S' (1A 01 00 00 74 00 00 7D 03 00 64 01 00 7D 04 00 7C 01 00 74 04 00 69 05 00 69 06 00 6A 02 00 6F 1C 00 01 7C 02 00 69 08 00 74 09 00 19 6F 0A 00 01 74 09 00 7D 03 00 71 DB 00 01 6E A1 00 01 7C 01 00 74 04 00 69 05 00 69 0A 00 6A 02 00 6F 1C 00 01 7C 02 00 69 08 00 74 09 00 19 6F 0A 00 01 74 09 00 7D 03 00 71 DB 00 01 6E 72 00 01 7C 01 00 74 04 00 69 05 00 69 0B 00 6A 02 00 70 10 00 01 7C 01 00 74 04 00 69 05 00 69 0C 00 6A 02 00 6F 1C 00 01 7C 02 00 69 08 00 74 0D 00 19 6F 0A 00 01 74 0D 00 7D 03 00 71 DB 00 01 6E 30 00 01 7C 01 00 74 04 00 69 05 00 69 0E 00 6A 02 00 6F 1C 00 01 7C 02 00 69 08 00 74 0F 00 19 6F 0A 00 01 74 0F 00 7D 03 00 71 DB 00 01 6E 01 00 01 7C 03 00 74 00 00 6A 03 00 6F 11 00 01 7C 02 00 69 10 00 7C 03 00 19 7D 04 00 6E 01 00 01 7C 04 00 74 11 00 7C 02 00 7C 03 00 83 02 00 37 7D 04 00 7C 03 00 7C 04 00 66 02 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'InvalidAbility'
                             00000003     7D - STORE_FAST          'use_ability'
                             00000006     64 - LOAD_CONST          0
                             00000009     7D - STORE_FAST          'use_ability_level'
                             0000000C     7C - LOAD_FAST           'equippedItem'
                             0000000F     74 - LOAD_GLOBAL         'constants'
                             00000012     69 - LOAD_ATTR           'combat'
                             00000015     69 - LOAD_ATTR           'RANGED_SINGLE_PISTOL'
                             00000018     6A - COMPARE_OP          "=="
                             0000001B     6F - JUMP_IF_FALSE       -> 0000003A
                             0000001E     01 - POP_TOP             
                             0000001F     7C - LOAD_FAST           'player'
                             00000022     69 - LOAD_ATTR           'hasAbility'
                             00000025     74 - LOAD_GLOBAL         'HandgunsAbility'
                             00000028     19 - BINARY_SUBSCR       
                             00000029     6F - JUMP_IF_FALSE       -> 00000036
                             0000002C     01 - POP_TOP             
                             0000002D     74 - LOAD_GLOBAL         'HandgunsAbility'
                             00000030     7D - STORE_FAST          'use_ability'
                             00000033     71 - JUMP_ABSOLUTE       -> 000000DB
                             00000036     01 - POP_TOP             
                             00000037     6E - JUMP_FORWARD        -> 000000DB
                             0000003A     01 - POP_TOP             
                             0000003B     7C - LOAD_FAST           'equippedItem'
                             0000003E     74 - LOAD_GLOBAL         'constants'
                             00000041     69 - LOAD_ATTR           'combat'
                             00000044     69 - LOAD_ATTR           'RANGED_DOUBLE_PISTOL'
                             00000047     6A - COMPARE_OP          "=="
                             0000004A     6F - JUMP_IF_FALSE       -> 00000069
                             0000004D     01 - POP_TOP             
                             0000004E     7C - LOAD_FAST           'player'
                             00000051     69 - LOAD_ATTR           'hasAbility'
                             00000054     74 - LOAD_GLOBAL         'HandgunsAbility'
                             00000057     19 - BINARY_SUBSCR       
                             00000058     6F - JUMP_IF_FALSE       -> 00000065
                             0000005B     01 - POP_TOP             
                             0000005C     74 - LOAD_GLOBAL         'HandgunsAbility'
                             0000005F     7D - STORE_FAST          'use_ability'
                             00000062     71 - JUMP_ABSOLUTE       -> 000000DB
                             00000065     01 - POP_TOP             
                             00000066     6E - JUMP_FORWARD        -> 000000DB
                             00000069     01 - POP_TOP             
                             0000006A     7C - LOAD_FAST           'equippedItem'
                             0000006D     74 - LOAD_GLOBAL         'constants'
                             00000070     69 - LOAD_ATTR           'combat'
                             00000073     69 - LOAD_ATTR           'RANGED_RIFLE'
                             00000076     6A - COMPARE_OP          "=="
                             00000079     70 - JUMP_IF_TRUE        -> 0000008C
                             0000007C     01 - POP_TOP             
                             0000007D     7C - LOAD_FAST           'equippedItem'
                             00000080     74 - LOAD_GLOBAL         'constants'
                             00000083     69 - LOAD_ATTR           'combat'
                             00000086     69 - LOAD_ATTR           'RANGED_SHOTGUN'
                             00000089     6A - COMPARE_OP          "=="
                             0000008C     6F - JUMP_IF_FALSE       -> 000000AB
                             0000008F     01 - POP_TOP             
                             00000090     7C - LOAD_FAST           'player'
                             00000093     69 - LOAD_ATTR           'hasAbility'
                             00000096     74 - LOAD_GLOBAL         'RiflesAbility'
                             00000099     19 - BINARY_SUBSCR       
                             0000009A     6F - JUMP_IF_FALSE       -> 000000A7
                             0000009D     01 - POP_TOP             
                             0000009E     74 - LOAD_GLOBAL         'RiflesAbility'
                             000000A1     7D - STORE_FAST          'use_ability'
                             000000A4     71 - JUMP_ABSOLUTE       -> 000000DB
                             000000A7     01 - POP_TOP             
                             000000A8     6E - JUMP_FORWARD        -> 000000DB
                             000000AB     01 - POP_TOP             
                             000000AC     7C - LOAD_FAST           'equippedItem'
                             000000AF     74 - LOAD_GLOBAL         'constants'
                             000000B2     69 - LOAD_ATTR           'combat'
                             000000B5     69 - LOAD_ATTR           'RANGED_MACHINE_GUN'
                             000000B8     6A - COMPARE_OP          "=="
                             000000BB     6F - JUMP_IF_FALSE       -> 000000DA
                             000000BE     01 - POP_TOP             
                             000000BF     7C - LOAD_FAST           'player'
                             000000C2     69 - LOAD_ATTR           'hasAbility'
                             000000C5     74 - LOAD_GLOBAL         'SubmachinegunsAbility'
                             000000C8     19 - BINARY_SUBSCR       
                             000000C9     6F - JUMP_IF_FALSE       -> 000000D6
                             000000CC     01 - POP_TOP             
                             000000CD     74 - LOAD_GLOBAL         'SubmachinegunsAbility'
                             000000D0     7D - STORE_FAST          'use_ability'
                             000000D3     71 - JUMP_ABSOLUTE       -> 000000DB
                             000000D6     01 - POP_TOP             
                             000000D7     6E - JUMP_FORWARD        -> 000000DB
                             000000DA     01 - POP_TOP             
                             000000DB     7C - LOAD_FAST           'use_ability'
                             000000DE     74 - LOAD_GLOBAL         'InvalidAbility'
                             000000E1     6A - COMPARE_OP          "!="
                             000000E4     6F - JUMP_IF_FALSE       -> 000000F8
                             000000E7     01 - POP_TOP             
                             000000E8     7C - LOAD_FAST           'player'
                             000000EB     69 - LOAD_ATTR           'abilities'
                             000000EE     7C - LOAD_FAST           'use_ability'
                             000000F1     19 - BINARY_SUBSCR       
                             000000F2     7D - STORE_FAST          'use_ability_level'
                             000000F5     6E - JUMP_FORWARD        -> 000000F9
                             000000F8     01 - POP_TOP             
                             000000F9     7C - LOAD_FAST           'use_ability_level'
                             000000FC     74 - LOAD_GLOBAL         'GetMasteryLevel'
                             000000FF     7C - LOAD_FAST           'player'
                             00000102     7C - LOAD_FAST           'use_ability'
                             00000105     83 - CALL_FUNCTION       r0002
                             00000108     37 - INPLACE_ADD         
                             00000109     7D - STORE_FAST          'use_ability_level'
                             0000010C     7C - LOAD_FAST           'use_ability'
                             0000010F     7C - LOAD_FAST           'use_ability_level'
                             00000112     66 - BUILD_TUPLE         r0002
                             00000115     53 - RETURN_VALUE        
                             00000116     64 - LOAD_CONST          None
                             00000119     53 - RETURN_VALUE        
                         consts:
00000726                     TUPLE: (
0000072B                         None (4E),
0000072C                         INT: 0 (00 00 00 00)
                             )
                         names:
00000731                     TUPLE: (
00000736                         STR: 'InvalidAbility' (0E 00 00 00 49 6E 76 61 6C 69 64 41 62 69 6C 69 74 79),
00000749                         STR: 'use_ability' (0B 00 00 00 75 73 65 5F 61 62 69 6C 69 74 79),
00000759                         STR: 'use_ability_level' (11 00 00 00 75 73 65 5F 61 62 69 6C 69 74 79 5F 6C 65 76 65 6C),
0000076F                         STR: 'equippedItem' (0C 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D),
00000780                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
0000078E                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
00000799                         STR: 'RANGED_SINGLE_PISTOL' (14 00 00 00 52 41 4E 47 45 44 5F 53 49 4E 47 4C 45 5F 50 49 53 54 4F 4C),
000007B2                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
000007BD                         STR: 'hasAbility' (0A 00 00 00 68 61 73 41 62 69 6C 69 74 79),
000007CC                         STR: 'HandgunsAbility' (0F 00 00 00 48 61 6E 64 67 75 6E 73 41 62 69 6C 69 74 79),
000007E0                         STR: 'RANGED_DOUBLE_PISTOL' (14 00 00 00 52 41 4E 47 45 44 5F 44 4F 55 42 4C 45 5F 50 49 53 54 4F 4C),
000007F9                         STR: 'RANGED_RIFLE' (0C 00 00 00 52 41 4E 47 45 44 5F 52 49 46 4C 45),
0000080A                         STR: 'RANGED_SHOTGUN' (0E 00 00 00 52 41 4E 47 45 44 5F 53 48 4F 54 47 55 4E),
0000081D                         STR: 'RiflesAbility' (0D 00 00 00 52 69 66 6C 65 73 41 62 69 6C 69 74 79),
0000082F                         STR: 'RANGED_MACHINE_GUN' (12 00 00 00 52 41 4E 47 45 44 5F 4D 41 43 48 49 4E 45 5F 47 55 4E),
00000846                         STR: 'SubmachinegunsAbility' (15 00 00 00 53 75 62 6D 61 63 68 69 6E 65 67 75 6E 73 41 62 69 6C 69 74 79),
00000860                         STR: 'abilities' (09 00 00 00 61 62 69 6C 69 74 69 65 73),
0000086E                         STR: 'GetMasteryLevel' (0F 00 00 00 47 65 74 4D 61 73 74 65 72 79 4C 65 76 65 6C)
                             )
                         varnames:
00000882                     TUPLE: (
00000887                         STR: 'equippedItemID' (0E 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D 49 44),
0000089A                         STR: 'equippedItem' (0C 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D),
000008AB                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
000008B6                         STR: 'use_ability' (0B 00 00 00 75 73 65 5F 61 62 69 6C 69 74 79),
000008C6                         STR: 'use_ability_level' (11 00 00 00 75 73 65 5F 61 62 69 6C 69 74 79 5F 6C 65 76 65 6C)
                             )
                         freevars:
000008DC                     TUPLE: ()
                         cellvars:
000008E1                     TUPLE: ()
                         filename:
000008E6                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_abil_level.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 61 62 69 6C 5F 6C 65 76 65 6C 2E 70 79)
                         name:
0000093E                     STR: 'GetItemAbilityLevel' (13 00 00 00 47 65 74 49 74 65 6D 41 62 69 6C 69 74 79 4C 65 76 65 6C)
                         firslineno:
00000956                     LONG: 71L (47 00 00 00)
                         lnotab:
0000095A                     STR: '\x00\x02\x06\x01\x06\x02\x13\x01\x0e\x01\x0e\x01\x13\x01\x0e\x01\x0e\x01&\x01\x0e\x01\x0e\x01\x13\x01\x0e\x01\x0e\x02\r\x01\x11\x03\x13\x02' (24 00 00 00 00 02 06 01 06 02 13 01 0E 01 0E 01 13 01 0E 01 0E 01 26 01 0E 01 0E 01 13 01 0E 01 0E 02 0D 01 11 03 13 02),
00000983             CODE:
                         argcount:
00000984                     LONG: 4L (04 00 00 00)
                         nlocals:
00000988                     LONG: 6L (06 00 00 00)
                         stacksize:
0000098C                     LONG: 4L (04 00 00 00)
                         flags:
00000990                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000994                     STR: 't\x00\x00|\x00\x00|\x01\x00|\x02\x00\x83\x03\x00\\\x02\x00}\x04\x00}\x05\x00|\x04\x00|\x03\x00_\x07\x00|\x05\x00|\x03\x00_\x08\x00|\x00\x00|\x03\x00_\t\x00|\x01\x00|\x03\x00_\n\x00d\x00\x00S' (40 00 00 00 74 00 00 7C 00 00 7C 01 00 7C 02 00 83 03 00 5C 02 00 7D 04 00 7D 05 00 7C 04 00 7C 03 00 5F 07 00 7C 05 00 7C 03 00 5F 08 00 7C 00 00 7C 03 00 5F 09 00 7C 01 00 7C 03 00 5F 0A 00 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'GetItemAbilityLevel'
                             00000003     7C - LOAD_FAST           'equippedItemID'
                             00000006     7C - LOAD_FAST           'equippedItem'
                             00000009     7C - LOAD_FAST           'player'
                             0000000C     83 - CALL_FUNCTION       r0003
                             0000000F     5C - UNPACK_SEQUENCE     r0002
                             00000012     7D - STORE_FAST          'use_ability'
                             00000015     7D - STORE_FAST          'use_ability_level'
                             00000018     7C - LOAD_FAST           'use_ability'
                             0000001B     7C - LOAD_FAST           'result'
                             0000001E     5F - STORE_ATTR          'itemAbility'
                             00000021     7C - LOAD_FAST           'use_ability_level'
                             00000024     7C - LOAD_FAST           'result'
                             00000027     5F - STORE_ATTR          'itemAbilityLevel'
                             0000002A     7C - LOAD_FAST           'equippedItemID'
                             0000002D     7C - LOAD_FAST           'result'
                             00000030     5F - STORE_ATTR          'itemID'
                             00000033     7C - LOAD_FAST           'equippedItem'
                             00000036     7C - LOAD_FAST           'result'
                             00000039     5F - STORE_ATTR          'itemType'
                             0000003C     64 - LOAD_CONST          None
                             0000003F     53 - RETURN_VALUE        
                         consts:
000009D9                     TUPLE: (
000009DE                         None (4E)
                             )
                         names:
000009DF                     TUPLE: (
000009E4                         STR: 'GetItemAbilityLevel' (13 00 00 00 47 65 74 49 74 65 6D 41 62 69 6C 69 74 79 4C 65 76 65 6C),
000009FC                         STR: 'equippedItemID' (0E 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D 49 44),
00000A0F                         STR: 'equippedItem' (0C 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D),
00000A20                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00000A2B                         STR: 'use_ability' (0B 00 00 00 75 73 65 5F 61 62 69 6C 69 74 79),
00000A3B                         STR: 'use_ability_level' (11 00 00 00 75 73 65 5F 61 62 69 6C 69 74 79 5F 6C 65 76 65 6C),
00000A51                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00000A5C                         STR: 'itemAbility' (0B 00 00 00 69 74 65 6D 41 62 69 6C 69 74 79),
00000A6C                         STR: 'itemAbilityLevel' (10 00 00 00 69 74 65 6D 41 62 69 6C 69 74 79 4C 65 76 65 6C),
00000A81                         STR: 'itemID' (06 00 00 00 69 74 65 6D 49 44),
00000A8C                         STR: 'itemType' (08 00 00 00 69 74 65 6D 54 79 70 65)
                             )
                         varnames:
00000A99                     TUPLE: (
00000A9E                         STR: 'equippedItemID' (0E 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D 49 44),
00000AB1                         STR: 'equippedItem' (0C 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D),
00000AC2                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00000ACD                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00000AD8                         STR: 'use_ability' (0B 00 00 00 75 73 65 5F 61 62 69 6C 69 74 79),
00000AE8                         STR: 'use_ability_level' (11 00 00 00 75 73 65 5F 61 62 69 6C 69 74 79 5F 6C 65 76 65 6C)
                             )
                         freevars:
00000AFE                     TUPLE: ()
                         cellvars:
00000B03                     TUPLE: ()
                         filename:
00000B08                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_abil_level.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 61 62 69 6C 5F 6C 65 76 65 6C 2E 70 79)
                         name:
00000B60                     STR: 'SelectItemAbilityLevel' (16 00 00 00 53 65 6C 65 63 74 49 74 65 6D 41 62 69 6C 69 74 79 4C 65 76 65 6C)
                         firslineno:
00000B7B                     LONG: 98L (62 00 00 00)
                         lnotab:
00000B7F                     STR: '\x00\x02\x18\x02\t\x01\t\x02\t\x01' (0A 00 00 00 00 02 18 02 09 01 09 02 09 01),
00000B8E             CODE:
                         argcount:
00000B8F                     LONG: 4L (04 00 00 00)
                         nlocals:
00000B93                     LONG: 4L (04 00 00 00)
                         stacksize:
00000B97                     LONG: 3L (03 00 00 00)
                         flags:
00000B9B                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000B9F                     STR: '|\x02\x00i\x01\x00t\x02\x00|\x00\x00\x83\x01\x00\x17|\x03\x00_\x05\x00d\x00\x00S' (1A 00 00 00 7C 02 00 69 01 00 74 02 00 7C 00 00 83 01 00 17 7C 03 00 5F 05 00 64 00 00 53)
                             00000000     7C - LOAD_FAST           'player'
                             00000003     69 - LOAD_ATTR           'Level'
                             00000006     74 - LOAD_GLOBAL         'getTacticalInitiativeBonus'
                             00000009     7C - LOAD_FAST           'tacticalSetting'
                             0000000C     83 - CALL_FUNCTION       r0001
                             0000000F     17 - BINARY_ADD          
                             00000010     7C - LOAD_FAST           'result'
                             00000013     5F - STORE_ATTR          'initiative'
                             00000016     64 - LOAD_CONST          None
                             00000019     53 - RETURN_VALUE        
                         consts:
00000BBE                     TUPLE: (
00000BC3                         None (4E)
                             )
                         names:
00000BC4                     TUPLE: (
00000BC9                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00000BD4                         STR: 'Level' (05 00 00 00 4C 65 76 65 6C),
00000BDE                         STR: 'getTacticalInitiativeBonus' (1A 00 00 00 67 65 74 54 61 63 74 69 63 61 6C 49 6E 69 74 69 61 74 69 76 65 42 6F 6E 75 73),
00000BFD                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
00000C11                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00000C1C                         STR: 'initiative' (0A 00 00 00 69 6E 69 74 69 61 74 69 76 65)
                             )
                         varnames:
00000C2B                     TUPLE: (
00000C30                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
00000C44                         STR: 'requestedMartialArt' (13 00 00 00 72 65 71 75 65 73 74 65 64 4D 61 72 74 69 61 6C 41 72 74),
00000C5C                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00000C67                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74)
                             )
                         freevars:
00000C72                     TUPLE: ()
                         cellvars:
00000C77                     TUPLE: ()
                         filename:
00000C7C                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_abil_level.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 61 62 69 6C 5F 6C 65 76 65 6C 2E 70 79)
                         name:
00000CD4                     STR: 'SelectCombatAbilityLevel' (18 00 00 00 53 65 6C 65 63 74 43 6F 6D 62 61 74 41 62 69 6C 69 74 79 4C 65 76 65 6C)
                         firslineno:
00000CF1                     LONG: 109L (6D 00 00 00)
                         lnotab:
00000CF5                     STR: '\x00\x03' (02 00 00 00 00 03),
00000CFC             CODE:
                         argcount:
00000CFD                     LONG: 1L (01 00 00 00)
                         nlocals:
00000D01                     LONG: 1L (01 00 00 00)
                         stacksize:
00000D05                     LONG: 3L (03 00 00 00)
                         flags:
00000D09                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000D0D                     STR: '|\x00\x00t\x01\x00i\x02\x00i\x03\x00j\x02\x00o\x1c\x00\x01t\x04\x00i\x05\x00d\x01\x00|\x00\x00\x16d\x02\x00\x83\x02\x00\x01t\x06\x00Sn\xec\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x07\x00j\x02\x00o\x1c\x00\x01t\x04\x00i\x05\x00d\x03\x00|\x00\x00\x16d\x02\x00\x83\x02\x00\x01t\x06\x00Sn\xbd\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x08\x00j\x02\x00o\x1c\x00\x01t\x04\x00i\x05\x00d\x04\x00|\x00\x00\x16d\x02\x00\x83\x02\x00\x01t\x06\x00Sn\x8e\x00\x01|\x00\x00t\x01\x00i\x02\x00i\t\x00j\x02\x00o\x1c\x00\x01t\x04\x00i\x05\x00d\x05\x00|\x00\x00\x16d\x02\x00\x83\x02\x00\x01t\x06\x00Sn_\x00\x01|\x00\x00t\x01\x00i\x02\x00i\n\x00j\x02\x00o\x1c\x00\x01t\x04\x00i\x05\x00d\x06\x00|\x00\x00\x16d\x02\x00\x83\x02\x00\x01t\x06\x00Sn0\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x0b\x00j\x02\x00o\x1c\x00\x01t\x04\x00i\x05\x00d\x07\x00|\x00\x00\x16d\x02\x00\x83\x02\x00\x01t\x06\x00Sn\x01\x00\x01|\x00\x00d\x08\x00j\x02\x00o\x18\x00\x01t\x04\x00i\x05\x00d\t\x00|\x00\x00\x16d\x02\x00\x83\x02\x00\x01n\x15\x00\x01t\x04\x00i\x05\x00d\n\x00|\x00\x00\x16d\x02\x00\x83\x02\x00\x01t\x0c\x00Sd\x00\x00S' (5B 01 00 00 7C 00 00 74 01 00 69 02 00 69 03 00 6A 02 00 6F 1C 00 01 74 04 00 69 05 00 64 01 00 7C 00 00 16 64 02 00 83 02 00 01 74 06 00 53 6E EC 00 01 7C 00 00 74 01 00 69 02 00 69 07 00 6A 02 00 6F 1C 00 01 74 04 00 69 05 00 64 03 00 7C 00 00 16 64 02 00 83 02 00 01 74 06 00 53 6E BD 00 01 7C 00 00 74 01 00 69 02 00 69 08 00 6A 02 00 6F 1C 00 01 74 04 00 69 05 00 64 04 00 7C 00 00 16 64 02 00 83 02 00 01 74 06 00 53 6E 8E 00 01 7C 00 00 74 01 00 69 02 00 69 09 00 6A 02 00 6F 1C 00 01 74 04 00 69 05 00 64 05 00 7C 00 00 16 64 02 00 83 02 00 01 74 06 00 53 6E 5F 00 01 7C 00 00 74 01 00 69 02 00 69 0A 00 6A 02 00 6F 1C 00 01 74 04 00 69 05 00 64 06 00 7C 00 00 16 64 02 00 83 02 00 01 74 06 00 53 6E 30 00 01 7C 00 00 74 01 00 69 02 00 69 0B 00 6A 02 00 6F 1C 00 01 74 04 00 69 05 00 64 07 00 7C 00 00 16 64 02 00 83 02 00 01 74 06 00 53 6E 01 00 01 7C 00 00 64 08 00 6A 02 00 6F 18 00 01 74 04 00 69 05 00 64 09 00 7C 00 00 16 64 02 00 83 02 00 01 6E 15 00 01 74 04 00 69 05 00 64 0A 00 7C 00 00 16 64 02 00 83 02 00 01 74 0C 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'equippedItem'
                             00000003     74 - LOAD_GLOBAL         'constants'
                             00000006     69 - LOAD_ATTR           'combat'
                             00000009     69 - LOAD_ATTR           'RANGED_DOUBLE_PISTOL'
                             0000000C     6A - COMPARE_OP          "=="
                             0000000F     6F - JUMP_IF_FALSE       -> 0000002E
                             00000012     01 - POP_TOP             
                             00000013     74 - LOAD_GLOBAL         'CU'
                             00000016     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000019     64 - LOAD_CONST          'weapon is dual pistol: %d '
                             0000001C     7C - LOAD_FAST           'equippedItem'
                             0000001F     16 - BINARY_MODULO       
                             00000020     64 - LOAD_CONST          10
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     01 - POP_TOP             
                             00000027     74 - LOAD_GLOBAL         'True'
                             0000002A     53 - RETURN_VALUE        
                             0000002B     6E - JUMP_FORWARD        -> 0000011A
                             0000002E     01 - POP_TOP             
                             0000002F     7C - LOAD_FAST           'equippedItem'
                             00000032     74 - LOAD_GLOBAL         'constants'
                             00000035     69 - LOAD_ATTR           'combat'
                             00000038     69 - LOAD_ATTR           'RANGED_SINGLE_PISTOL'
                             0000003B     6A - COMPARE_OP          "=="
                             0000003E     6F - JUMP_IF_FALSE       -> 0000005D
                             00000041     01 - POP_TOP             
                             00000042     74 - LOAD_GLOBAL         'CU'
                             00000045     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000048     64 - LOAD_CONST          'weapon is pistol: %d '
                             0000004B     7C - LOAD_FAST           'equippedItem'
                             0000004E     16 - BINARY_MODULO       
                             0000004F     64 - LOAD_CONST          10
                             00000052     83 - CALL_FUNCTION       r0002
                             00000055     01 - POP_TOP             
                             00000056     74 - LOAD_GLOBAL         'True'
                             00000059     53 - RETURN_VALUE        
                             0000005A     6E - JUMP_FORWARD        -> 0000011A
                             0000005D     01 - POP_TOP             
                             0000005E     7C - LOAD_FAST           'equippedItem'
                             00000061     74 - LOAD_GLOBAL         'constants'
                             00000064     69 - LOAD_ATTR           'combat'
                             00000067     69 - LOAD_ATTR           'RANGED_SHOTGUN'
                             0000006A     6A - COMPARE_OP          "=="
                             0000006D     6F - JUMP_IF_FALSE       -> 0000008C
                             00000070     01 - POP_TOP             
                             00000071     74 - LOAD_GLOBAL         'CU'
                             00000074     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000077     64 - LOAD_CONST          'weapon is shotgun: %d '
                             0000007A     7C - LOAD_FAST           'equippedItem'
                             0000007D     16 - BINARY_MODULO       
                             0000007E     64 - LOAD_CONST          10
                             00000081     83 - CALL_FUNCTION       r0002
                             00000084     01 - POP_TOP             
                             00000085     74 - LOAD_GLOBAL         'True'
                             00000088     53 - RETURN_VALUE        
                             00000089     6E - JUMP_FORWARD        -> 0000011A
                             0000008C     01 - POP_TOP             
                             0000008D     7C - LOAD_FAST           'equippedItem'
                             00000090     74 - LOAD_GLOBAL         'constants'
                             00000093     69 - LOAD_ATTR           'combat'
                             00000096     69 - LOAD_ATTR           'RANGED_MACHINE_GUN'
                             00000099     6A - COMPARE_OP          "=="
                             0000009C     6F - JUMP_IF_FALSE       -> 000000BB
                             0000009F     01 - POP_TOP             
                             000000A0     74 - LOAD_GLOBAL         'CU'
                             000000A3     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000A6     64 - LOAD_CONST          'weapon is machine gun: %d '
                             000000A9     7C - LOAD_FAST           'equippedItem'
                             000000AC     16 - BINARY_MODULO       
                             000000AD     64 - LOAD_CONST          10
                             000000B0     83 - CALL_FUNCTION       r0002
                             000000B3     01 - POP_TOP             
                             000000B4     74 - LOAD_GLOBAL         'True'
                             000000B7     53 - RETURN_VALUE        
                             000000B8     6E - JUMP_FORWARD        -> 0000011A
                             000000BB     01 - POP_TOP             
                             000000BC     7C - LOAD_FAST           'equippedItem'
                             000000BF     74 - LOAD_GLOBAL         'constants'
                             000000C2     69 - LOAD_ATTR           'combat'
                             000000C5     69 - LOAD_ATTR           'RANGED_RIFLE'
                             000000C8     6A - COMPARE_OP          "=="
                             000000CB     6F - JUMP_IF_FALSE       -> 000000EA
                             000000CE     01 - POP_TOP             
                             000000CF     74 - LOAD_GLOBAL         'CU'
                             000000D2     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000D5     64 - LOAD_CONST          'weapon is rifle: %d '
                             000000D8     7C - LOAD_FAST           'equippedItem'
                             000000DB     16 - BINARY_MODULO       
                             000000DC     64 - LOAD_CONST          10
                             000000DF     83 - CALL_FUNCTION       r0002
                             000000E2     01 - POP_TOP             
                             000000E3     74 - LOAD_GLOBAL         'True'
                             000000E6     53 - RETURN_VALUE        
                             000000E7     6E - JUMP_FORWARD        -> 0000011A
                             000000EA     01 - POP_TOP             
                             000000EB     7C - LOAD_FAST           'equippedItem'
                             000000EE     74 - LOAD_GLOBAL         'constants'
                             000000F1     69 - LOAD_ATTR           'combat'
                             000000F4     69 - LOAD_ATTR           'RANGED_DBL_MACHINE_GUN'
                             000000F7     6A - COMPARE_OP          "=="
                             000000FA     6F - JUMP_IF_FALSE       -> 00000119
                             000000FD     01 - POP_TOP             
                             000000FE     74 - LOAD_GLOBAL         'CU'
                             00000101     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000104     64 - LOAD_CONST          'weapon is dual submahine gun: %d '
                             00000107     7C - LOAD_FAST           'equippedItem'
                             0000010A     16 - BINARY_MODULO       
                             0000010B     64 - LOAD_CONST          10
                             0000010E     83 - CALL_FUNCTION       r0002
                             00000111     01 - POP_TOP             
                             00000112     74 - LOAD_GLOBAL         'True'
                             00000115     53 - RETURN_VALUE        
                             00000116     6E - JUMP_FORWARD        -> 0000011A
                             00000119     01 - POP_TOP             
                             0000011A     7C - LOAD_FAST           'equippedItem'
                             0000011D     64 - LOAD_CONST          0
                             00000120     6A - COMPARE_OP          "=="
                             00000123     6F - JUMP_IF_FALSE       -> 0000013E
                             00000126     01 - POP_TOP             
                             00000127     74 - LOAD_GLOBAL         'CU'
                             0000012A     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000012D     64 - LOAD_CONST          'weapon type invalid: %d '
                             00000130     7C - LOAD_FAST           'equippedItem'
                             00000133     16 - BINARY_MODULO       
                             00000134     64 - LOAD_CONST          10
                             00000137     83 - CALL_FUNCTION       r0002
                             0000013A     01 - POP_TOP             
                             0000013B     6E - JUMP_FORWARD        -> 00000153
                             0000013E     01 - POP_TOP             
                             0000013F     74 - LOAD_GLOBAL         'CU'
                             00000142     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000145     64 - LOAD_CONST          'weapon type not found: %d '
                             00000148     7C - LOAD_FAST           'equippedItem'
                             0000014B     16 - BINARY_MODULO       
                             0000014C     64 - LOAD_CONST          10
                             0000014F     83 - CALL_FUNCTION       r0002
                             00000152     01 - POP_TOP             
                             00000153     74 - LOAD_GLOBAL         'False'
                             00000156     53 - RETURN_VALUE        
                             00000157     64 - LOAD_CONST          None
                             0000015A     53 - RETURN_VALUE        
                         consts:
00000E6D                     TUPLE: (
00000E72                         None (4E),
00000E73                         STR: 'weapon is dual pistol: %d ' (1A 00 00 00 77 65 61 70 6F 6E 20 69 73 20 64 75 61 6C 20 70 69 73 74 6F 6C 3A 20 25 64 20),
00000E92                         INT: 10 (0A 00 00 00),
00000E97                         STR: 'weapon is pistol: %d ' (15 00 00 00 77 65 61 70 6F 6E 20 69 73 20 70 69 73 74 6F 6C 3A 20 25 64 20),
00000EB1                         STR: 'weapon is shotgun: %d ' (16 00 00 00 77 65 61 70 6F 6E 20 69 73 20 73 68 6F 74 67 75 6E 3A 20 25 64 20),
00000ECC                         STR: 'weapon is machine gun: %d ' (1A 00 00 00 77 65 61 70 6F 6E 20 69 73 20 6D 61 63 68 69 6E 65 20 67 75 6E 3A 20 25 64 20),
00000EEB                         STR: 'weapon is rifle: %d ' (14 00 00 00 77 65 61 70 6F 6E 20 69 73 20 72 69 66 6C 65 3A 20 25 64 20),
00000F04                         STR: 'weapon is dual submahine gun: %d ' (21 00 00 00 77 65 61 70 6F 6E 20 69 73 20 64 75 61 6C 20 73 75 62 6D 61 68 69 6E 65 20 67 75 6E 3A 20 25 64 20),
00000F2A                         INT: 0 (00 00 00 00),
00000F2F                         STR: 'weapon type invalid: %d ' (18 00 00 00 77 65 61 70 6F 6E 20 74 79 70 65 20 69 6E 76 61 6C 69 64 3A 20 25 64 20),
00000F4C                         STR: 'weapon type not found: %d ' (1A 00 00 00 77 65 61 70 6F 6E 20 74 79 70 65 20 6E 6F 74 20 66 6F 75 6E 64 3A 20 25 64 20)
                             )
                         names:
00000F6B                     TUPLE: (
00000F70                         STR: 'equippedItem' (0C 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D),
00000F81                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00000F8F                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
00000F9A                         STR: 'RANGED_DOUBLE_PISTOL' (14 00 00 00 52 41 4E 47 45 44 5F 44 4F 55 42 4C 45 5F 50 49 53 54 4F 4C),
00000FB3                         STR: 'CU' (02 00 00 00 43 55),
00000FBA                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
00000FD7                         STR: 'True' (04 00 00 00 54 72 75 65),
00000FE0                         STR: 'RANGED_SINGLE_PISTOL' (14 00 00 00 52 41 4E 47 45 44 5F 53 49 4E 47 4C 45 5F 50 49 53 54 4F 4C),
00000FF9                         STR: 'RANGED_SHOTGUN' (0E 00 00 00 52 41 4E 47 45 44 5F 53 48 4F 54 47 55 4E),
0000100C                         STR: 'RANGED_MACHINE_GUN' (12 00 00 00 52 41 4E 47 45 44 5F 4D 41 43 48 49 4E 45 5F 47 55 4E),
00001023                         STR: 'RANGED_RIFLE' (0C 00 00 00 52 41 4E 47 45 44 5F 52 49 46 4C 45),
00001034                         STR: 'RANGED_DBL_MACHINE_GUN' (16 00 00 00 52 41 4E 47 45 44 5F 44 42 4C 5F 4D 41 43 48 49 4E 45 5F 47 55 4E),
0000104F                         STR: 'False' (05 00 00 00 46 61 6C 73 65)
                             )
                         varnames:
00001059                     TUPLE: (
0000105E                         STR: 'equippedItem' (0C 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D)
                             )
                         freevars:
0000106F                     TUPLE: ()
                         cellvars:
00001074                     TUPLE: ()
                         filename:
00001079                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_abil_level.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 61 62 69 6C 5F 6C 65 76 65 6C 2E 70 79)
                         name:
000010D1                     STR: 'isUsingWeapon' (0D 00 00 00 69 73 55 73 69 6E 67 57 65 61 70 6F 6E)
                         firslineno:
000010E3                     LONG: 115L (73 00 00 00)
                         lnotab:
000010E7                     STR: '\x00\x02\x13\x01\x14\x01\x08\x01\x13\x01\x14\x01\x08\x01\x13\x01\x14\x01\x08\x01\x13\x01\x14\x01\x08\x01\x13\x01\x14\x01\x08\x01\x13\x01\x14\x01\x08\x02\r\x01\x18\x02\x14\x01' (2C 00 00 00 00 02 13 01 14 01 08 01 13 01 14 01 08 01 13 01 14 01 08 01 13 01 14 01 08 01 13 01 14 01 08 01 13 01 14 01 08 02 0D 01 18 02 14 01),
00001118             INT: 25 (19 00 00 00),
0000111D             INT: 15 (0F 00 00 00),
00001122             CODE:
                         argcount:
00001123                     LONG: 2L (02 00 00 00)
                         nlocals:
00001127                     LONG: 2L (02 00 00 00)
                         stacksize:
0000112B                     LONG: 1L (01 00 00 00)
                         flags:
0000112F                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001133                     STR: 'd\x01\x00Sd\x00\x00S' (08 00 00 00 64 01 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          0
                             00000003     53 - RETURN_VALUE        
                             00000004     64 - LOAD_CONST          None
                             00000007     53 - RETURN_VALUE        
                         consts:
00001140                     TUPLE: (
00001145                         None (4E),
00001146                         INT: 0 (00 00 00 00)
                             )
                         names:
0000114B                     TUPLE: ()
                         varnames:
00001150                     TUPLE: (
00001155                         STR: 'ability' (07 00 00 00 61 62 69 6C 69 74 79),
00001161                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67)
                             )
                         freevars:
00001175                     TUPLE: ()
                         cellvars:
0000117A                     TUPLE: ()
                         filename:
0000117F                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_abil_level.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 61 62 69 6C 5F 6C 65 76 65 6C 2E 70 79)
                         name:
000011D7                     STR: 'getMartialArtAbilityMod' (17 00 00 00 67 65 74 4D 61 72 74 69 61 6C 41 72 74 41 62 69 6C 69 74 79 4D 6F 64)
                         firslineno:
000011F3                     LONG: 145L (91 00 00 00)
                         lnotab:
000011F7                     STR: '\x00\x0c' (02 00 00 00 00 0C),
000011FE             CODE:
                         argcount:
000011FF                     LONG: 2L (02 00 00 00)
                         nlocals:
00001203                     LONG: 2L (02 00 00 00)
                         stacksize:
00001207                     LONG: 1L (01 00 00 00)
                         flags:
0000120B                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000120F                     STR: 'd\x01\x00Sd\x00\x00S' (08 00 00 00 64 01 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          0
                             00000003     53 - RETURN_VALUE        
                             00000004     64 - LOAD_CONST          None
                             00000007     53 - RETURN_VALUE        
                         consts:
0000121C                     TUPLE: (
00001221                         None (4E),
00001222                         INT: 0 (00 00 00 00)
                             )
                         names:
00001227                     TUPLE: ()
                         varnames:
0000122C                     TUPLE: (
00001231                         STR: 'itemAbility' (0B 00 00 00 69 74 65 6D 41 62 69 6C 69 74 79),
00001241                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67)
                             )
                         freevars:
00001255                     TUPLE: ()
                         cellvars:
0000125A                     TUPLE: ()
                         filename:
0000125F                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_abil_level.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 61 62 69 6C 5F 6C 65 76 65 6C 2E 70 79)
                         name:
000012B7                     STR: 'getItemAbilityMod' (11 00 00 00 67 65 74 49 74 65 6D 41 62 69 6C 69 74 79 4D 6F 64)
                         firslineno:
000012CD                     LONG: 160L (A0 00 00 00)
                         lnotab:
000012D1                     STR: '\x00\x0c' (02 00 00 00 00 0C),
000012D8             CODE:
                         argcount:
000012D9                     LONG: 3L (03 00 00 00)
                         nlocals:
000012DD                     LONG: 3L (03 00 00 00)
                         stacksize:
000012E1                     LONG: 5L (05 00 00 00)
                         flags:
000012E5                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000012E9                     STR: 't\x00\x00|\x01\x00i\x02\x00|\x01\x00i\x03\x00|\x00\x00|\x02\x00\x83\x04\x00\x01t\x06\x00|\x01\x00i\x07\x00|\x01\x00i\x08\x00|\x00\x00|\x02\x00\x83\x04\x00\x01|\x01\x00i\t\x00t\n\x00j\x03\x00o8\x00\x01|\x00\x00i\x0b\x00|\x01\x00i\t\x00\x19o#\x00\x01|\x01\x00i\t\x00|\x02\x00_\t\x00|\x00\x00i\x0c\x00|\x01\x00i\t\x00\x19|\x02\x00_\r\x00qz\x00\x01n\x01\x00\x01|\x01\x00i\x02\x00|\x02\x00_\x02\x00d\x00\x00S' (8A 00 00 00 74 00 00 7C 01 00 69 02 00 7C 01 00 69 03 00 7C 00 00 7C 02 00 83 04 00 01 74 06 00 7C 01 00 69 07 00 7C 01 00 69 08 00 7C 00 00 7C 02 00 83 04 00 01 7C 01 00 69 09 00 74 0A 00 6A 03 00 6F 38 00 01 7C 00 00 69 0B 00 7C 01 00 69 09 00 19 6F 23 00 01 7C 01 00 69 09 00 7C 02 00 5F 09 00 7C 00 00 69 0C 00 7C 01 00 69 09 00 19 7C 02 00 5F 0D 00 71 7A 00 01 6E 01 00 01 7C 01 00 69 02 00 7C 02 00 5F 02 00 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'SelectCombatAbilityLevel'
                             00000003     7C - LOAD_FAST           'desiredSettings'
                             00000006     69 - LOAD_ATTR           'tacticalSetting'
                             00000009     7C - LOAD_FAST           'desiredSettings'
                             0000000C     69 - LOAD_ATTR           'martialArt'
                             0000000F     7C - LOAD_FAST           'player'
                             00000012     7C - LOAD_FAST           'result'
                             00000015     83 - CALL_FUNCTION       r0004
                             00000018     01 - POP_TOP             
                             00000019     74 - LOAD_GLOBAL         'SelectItemAbilityLevel'
                             0000001C     7C - LOAD_FAST           'desiredSettings'
                             0000001F     69 - LOAD_ATTR           'equippedItemID'
                             00000022     7C - LOAD_FAST           'desiredSettings'
                             00000025     69 - LOAD_ATTR           'equippedItem'
                             00000028     7C - LOAD_FAST           'player'
                             0000002B     7C - LOAD_FAST           'result'
                             0000002E     83 - CALL_FUNCTION       r0004
                             00000031     01 - POP_TOP             
                             00000032     7C - LOAD_FAST           'desiredSettings'
                             00000035     69 - LOAD_ATTR           'specialMove'
                             00000038     74 - LOAD_GLOBAL         'InvalidAbility'
                             0000003B     6A - COMPARE_OP          "!="
                             0000003E     6F - JUMP_IF_FALSE       -> 00000079
                             00000041     01 - POP_TOP             
                             00000042     7C - LOAD_FAST           'player'
                             00000045     69 - LOAD_ATTR           'hasAbility'
                             00000048     7C - LOAD_FAST           'desiredSettings'
                             0000004B     69 - LOAD_ATTR           'specialMove'
                             0000004E     19 - BINARY_SUBSCR       
                             0000004F     6F - JUMP_IF_FALSE       -> 00000075
                             00000052     01 - POP_TOP             
                             00000053     7C - LOAD_FAST           'desiredSettings'
                             00000056     69 - LOAD_ATTR           'specialMove'
                             00000059     7C - LOAD_FAST           'result'
                             0000005C     5F - STORE_ATTR          'specialMove'
                             0000005F     7C - LOAD_FAST           'player'
                             00000062     69 - LOAD_ATTR           'abilities'
                             00000065     7C - LOAD_FAST           'desiredSettings'
                             00000068     69 - LOAD_ATTR           'specialMove'
                             0000006B     19 - BINARY_SUBSCR       
                             0000006C     7C - LOAD_FAST           'result'
                             0000006F     5F - STORE_ATTR          'specialMoveLevel'
                             00000072     71 - JUMP_ABSOLUTE       -> 0000007A
                             00000075     01 - POP_TOP             
                             00000076     6E - JUMP_FORWARD        -> 0000007A
                             00000079     01 - POP_TOP             
                             0000007A     7C - LOAD_FAST           'desiredSettings'
                             0000007D     69 - LOAD_ATTR           'tacticalSetting'
                             00000080     7C - LOAD_FAST           'result'
                             00000083     5F - STORE_ATTR          'tacticalSetting'
                             00000086     64 - LOAD_CONST          None
                             00000089     53 - RETURN_VALUE        
                         consts:
00001378                     TUPLE: (
0000137D                         None (4E)
                             )
                         names:
0000137E                     TUPLE: (
00001383                         STR: 'SelectCombatAbilityLevel' (18 00 00 00 53 65 6C 65 63 74 43 6F 6D 62 61 74 41 62 69 6C 69 74 79 4C 65 76 65 6C),
000013A0                         STR: 'desiredSettings' (0F 00 00 00 64 65 73 69 72 65 64 53 65 74 74 69 6E 67 73),
000013B4                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
000013C8                         STR: 'martialArt' (0A 00 00 00 6D 61 72 74 69 61 6C 41 72 74),
000013D7                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
000013E2                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
000013ED                         STR: 'SelectItemAbilityLevel' (16 00 00 00 53 65 6C 65 63 74 49 74 65 6D 41 62 69 6C 69 74 79 4C 65 76 65 6C),
00001408                         STR: 'equippedItemID' (0E 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D 49 44),
0000141B                         STR: 'equippedItem' (0C 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D),
0000142C                         STR: 'specialMove' (0B 00 00 00 73 70 65 63 69 61 6C 4D 6F 76 65),
0000143C                         STR: 'InvalidAbility' (0E 00 00 00 49 6E 76 61 6C 69 64 41 62 69 6C 69 74 79),
0000144F                         STR: 'hasAbility' (0A 00 00 00 68 61 73 41 62 69 6C 69 74 79),
0000145E                         STR: 'abilities' (09 00 00 00 61 62 69 6C 69 74 69 65 73),
0000146C                         STR: 'specialMoveLevel' (10 00 00 00 73 70 65 63 69 61 6C 4D 6F 76 65 4C 65 76 65 6C)
                             )
                         varnames:
00001481                     TUPLE: (
00001486                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00001491                         STR: 'desiredSettings' (0F 00 00 00 64 65 73 69 72 65 64 53 65 74 74 69 6E 67 73),
000014A5                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74)
                             )
                         freevars:
000014B0                     TUPLE: ()
                         cellvars:
000014B5                     TUPLE: ()
                         filename:
000014BA                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_abil_level.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 61 62 69 6C 5F 6C 65 76 65 6C 2E 70 79)
                         name:
00001512                     STR: 'SetCombatTargetSettings' (17 00 00 00 53 65 74 43 6F 6D 62 61 74 54 61 72 67 65 74 53 65 74 74 69 6E 67 73)
                         firslineno:
0000152E                     LONG: 175L (AF 00 00 00)
                         lnotab:
00001532                     STR: '\x00\x02\x19\x01\x19\x02\x10\x01\x11\x01\x0c\x01\x1b\x02' (0E 00 00 00 00 02 19 01 19 02 10 01 11 01 0C 01 1B 02),
00001545             CODE:
                         argcount:
00001546                     LONG: 5L (05 00 00 00)
                         nlocals:
0000154A                     LONG: 5L (05 00 00 00)
                         stacksize:
0000154E                     LONG: 4L (04 00 00 00)
                         flags:
00001552                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001556                     STR: 't\x00\x00|\x00\x00|\x01\x00|\x02\x00\x83\x03\x00\\\x02\x00}\x03\x00}\x04\x00d\x00\x00S' (1C 00 00 00 74 00 00 7C 00 00 7C 01 00 7C 02 00 83 03 00 5C 02 00 7D 03 00 7D 04 00 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'GetItemAbilityLevel'
                             00000003     7C - LOAD_FAST           'player'
                             00000006     7C - LOAD_FAST           'equippedItemID'
                             00000009     7C - LOAD_FAST           'equippedItem'
                             0000000C     83 - CALL_FUNCTION       r0003
                             0000000F     5C - UNPACK_SEQUENCE     r0002
                             00000012     7D - STORE_FAST          'itemAbility'
                             00000015     7D - STORE_FAST          'itemAbilityLevel'
                             00000018     64 - LOAD_CONST          None
                             0000001B     53 - RETURN_VALUE        
                         consts:
00001577                     TUPLE: (
0000157C                         None (4E)
                             )
                         names:
0000157D                     TUPLE: (
00001582                         STR: 'GetItemAbilityLevel' (13 00 00 00 47 65 74 49 74 65 6D 41 62 69 6C 69 74 79 4C 65 76 65 6C),
0000159A                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
000015A5                         STR: 'equippedItemID' (0E 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D 49 44),
000015B8                         STR: 'equippedItem' (0C 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D),
000015C9                         STR: 'itemAbility' (0B 00 00 00 69 74 65 6D 41 62 69 6C 69 74 79),
000015D9                         STR: 'itemAbilityLevel' (10 00 00 00 69 74 65 6D 41 62 69 6C 69 74 79 4C 65 76 65 6C)
                             )
                         varnames:
000015EE                     TUPLE: (
000015F3                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
000015FE                         STR: 'equippedItemID' (0E 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D 49 44),
00001611                         STR: 'equippedItem' (0C 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D),
00001622                         STR: 'itemAbility' (0B 00 00 00 69 74 65 6D 41 62 69 6C 69 74 79),
00001632                         STR: 'itemAbilityLevel' (10 00 00 00 69 74 65 6D 41 62 69 6C 69 74 79 4C 65 76 65 6C)
                             )
                         freevars:
00001647                     TUPLE: ()
                         cellvars:
0000164C                     TUPLE: ()
                         filename:
00001651                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_abil_level.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 61 62 69 6C 5F 6C 65 76 65 6C 2E 70 79)
                         name:
000016A9                     STR: 'GetFreeAttackAbility' (14 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 41 62 69 6C 69 74 79)
                         firslineno:
000016C2                     LONG: 188L (BC 00 00 00)
                         lnotab:
000016C6                     STR: '\x00\x01' (02 00 00 00 00 01)
                 )
             names:
000016CD         TUPLE: (
000016D2             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
000016DD             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
000016EB             STR: 'obj' (03 00 00 00 6F 62 6A),
000016F3             STR: 'combat_defines' (0E 00 00 00 63 6F 6D 62 61 74 5F 64 65 66 69 6E 65 73),
00001706             STR: 'CD' (02 00 00 00 43 44),
0000170D             STR: 'math' (04 00 00 00 6D 61 74 68),
00001716             STR: 'combat_utility' (0E 00 00 00 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79),
00001729             STR: 'CU' (02 00 00 00 43 55),
00001730             STR: 'combat_innerstrength' (14 00 00 00 63 6F 6D 62 61 74 5F 69 6E 6E 65 72 73 74 72 65 6E 67 74 68),
00001749             STR: 'CI' (02 00 00 00 43 49),
00001750             STR: 'getTacticalInitiativeBonus' (1A 00 00 00 67 65 74 54 61 63 74 69 63 61 6C 49 6E 69 74 69 61 74 69 76 65 42 6F 6E 75 73),
0000176F             STR: 'KarateAbility' (0D 00 00 00 4B 61 72 61 74 65 41 62 69 6C 69 74 79),
00001781             STR: 'KungFuAbility' (0D 00 00 00 4B 75 6E 67 46 75 41 62 69 6C 69 74 79),
00001793             STR: 'AikidoAbility' (0D 00 00 00 41 69 6B 69 64 6F 41 62 69 6C 69 74 79),
000017A5             STR: '_MartialArtList' (0F 00 00 00 5F 4D 61 72 74 69 61 6C 41 72 74 4C 69 73 74),
000017B9             STR: 'abilityLevel' (0C 00 00 00 61 62 69 6C 69 74 79 4C 65 76 65 6C),
000017CA             STR: 'getBaseAbilityLevel' (13 00 00 00 67 65 74 42 61 73 65 41 62 69 6C 69 74 79 4C 65 76 65 6C),
000017E2             STR: 'GetMasteryLevel' (0F 00 00 00 47 65 74 4D 61 73 74 65 72 79 4C 65 76 65 6C),
000017F6             STR: 'GetItemAbilityLevel' (13 00 00 00 47 65 74 49 74 65 6D 41 62 69 6C 69 74 79 4C 65 76 65 6C),
0000180E             STR: 'SelectItemAbilityLevel' (16 00 00 00 53 65 6C 65 63 74 49 74 65 6D 41 62 69 6C 69 74 79 4C 65 76 65 6C),
00001829             STR: 'SelectCombatAbilityLevel' (18 00 00 00 53 65 6C 65 63 74 43 6F 6D 62 61 74 41 62 69 6C 69 74 79 4C 65 76 65 6C),
00001846             STR: 'isUsingWeapon' (0D 00 00 00 69 73 55 73 69 6E 67 57 65 61 70 6F 6E),
00001858             STR: '_PRIMARY_TACTICAL_SETTING_SYNERGY_MOD' (25 00 00 00 5F 50 52 49 4D 41 52 59 5F 54 41 43 54 49 43 41 4C 5F 53 45 54 54 49 4E 47 5F 53 59 4E 45 52 47 59 5F 4D 4F 44),
00001882             STR: '_SECONDARY_TACTICAL_SETTING_SYNERGY_MOD' (27 00 00 00 5F 53 45 43 4F 4E 44 41 52 59 5F 54 41 43 54 49 43 41 4C 5F 53 45 54 54 49 4E 47 5F 53 59 4E 45 52 47 59 5F 4D 4F 44),
000018AE             STR: 'getMartialArtAbilityMod' (17 00 00 00 67 65 74 4D 61 72 74 69 61 6C 41 72 74 41 62 69 6C 69 74 79 4D 6F 64),
000018CA             STR: 'getItemAbilityMod' (11 00 00 00 67 65 74 49 74 65 6D 41 62 69 6C 69 74 79 4D 6F 64),
000018E0             STR: 'SetCombatTargetSettings' (17 00 00 00 53 65 74 43 6F 6D 62 61 74 54 61 72 67 65 74 53 65 74 74 69 6E 67 73),
000018FC             STR: 'GetFreeAttackAbility' (14 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 41 62 69 6C 69 74 79)
                 )
             varnames:
00001915         TUPLE: (
0000191A             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00001925             STR: 'SelectCombatAbilityLevel' (18 00 00 00 53 65 6C 65 63 74 43 6F 6D 62 61 74 41 62 69 6C 69 74 79 4C 65 76 65 6C),
00001942             STR: '_PRIMARY_TACTICAL_SETTING_SYNERGY_MOD' (25 00 00 00 5F 50 52 49 4D 41 52 59 5F 54 41 43 54 49 43 41 4C 5F 53 45 54 54 49 4E 47 5F 53 59 4E 45 52 47 59 5F 4D 4F 44),
0000196C             STR: 'getMartialArtAbilityMod' (17 00 00 00 67 65 74 4D 61 72 74 69 61 6C 41 72 74 41 62 69 6C 69 74 79 4D 6F 64),
00001988             STR: '_MartialArtList' (0F 00 00 00 5F 4D 61 72 74 69 61 6C 41 72 74 4C 69 73 74),
0000199C             STR: 'isUsingWeapon' (0D 00 00 00 69 73 55 73 69 6E 67 57 65 61 70 6F 6E),
000019AE             STR: 'abilityLevel' (0C 00 00 00 61 62 69 6C 69 74 79 4C 65 76 65 6C),
000019BF             STR: 'GetMasteryLevel' (0F 00 00 00 47 65 74 4D 61 73 74 65 72 79 4C 65 76 65 6C),
000019D3             STR: 'getItemAbilityMod' (11 00 00 00 67 65 74 49 74 65 6D 41 62 69 6C 69 74 79 4D 6F 64),
000019E9             STR: '_SECONDARY_TACTICAL_SETTING_SYNERGY_MOD' (27 00 00 00 5F 53 45 43 4F 4E 44 41 52 59 5F 54 41 43 54 49 43 41 4C 5F 53 45 54 54 49 4E 47 5F 53 59 4E 45 52 47 59 5F 4D 4F 44),
00001A15             STR: 'math' (04 00 00 00 6D 61 74 68),
00001A1E             STR: 'SelectItemAbilityLevel' (16 00 00 00 53 65 6C 65 63 74 49 74 65 6D 41 62 69 6C 69 74 79 4C 65 76 65 6C),
00001A39             STR: 'CI' (02 00 00 00 43 49),
00001A40             STR: 'SetCombatTargetSettings' (17 00 00 00 53 65 74 43 6F 6D 62 61 74 54 61 72 67 65 74 53 65 74 74 69 6E 67 73),
00001A5C             STR: 'CD' (02 00 00 00 43 44),
00001A63             STR: 'GetFreeAttackAbility' (14 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 41 62 69 6C 69 74 79),
00001A7C             STR: 'getBaseAbilityLevel' (13 00 00 00 67 65 74 42 61 73 65 41 62 69 6C 69 74 79 4C 65 76 65 6C),
00001A94             STR: 'getTacticalInitiativeBonus' (1A 00 00 00 67 65 74 54 61 63 74 69 63 61 6C 49 6E 69 74 69 61 74 69 76 65 42 6F 6E 75 73),
00001AB3             STR: 'CU' (02 00 00 00 43 55),
00001ABA             STR: 'obj' (03 00 00 00 6F 62 6A),
00001AC2             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00001AD0             STR: 'GetItemAbilityLevel' (13 00 00 00 47 65 74 49 74 65 6D 41 62 69 6C 69 74 79 4C 65 76 65 6C)
                 )
             freevars:
00001AE8         TUPLE: ()
             cellvars:
00001AED         TUPLE: ()
             filename:
00001AF2         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_abil_level.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 61 62 69 6C 5F 6C 65 76 65 6C 2E 70 79)
             name:
00001B4A         STR: '?' (01 00 00 00 3F)
             firslineno:
00001B50         LONG: 1L (01 00 00 00)
             lnotab:
00001B54         STR: '\t\x01\t\x01\t\x01\t\x01\t\x01\t\x01\t\x02\t\n\x0f\x02\t\x06\t\t\t#\t\x1b\t\x0b\t\x06\t\x1c\x06\x01\x06\x01\t\x0f\t\x0f\t\r' (2A 00 00 00 09 01 09 01 09 01 09 01 09 01 09 01 09 02 09 0A 0F 02 09 06 09 09 09 23 09 1B 09 0B 09 06 09 1C 06 01 06 01 09 0F 09 0F 09 0D)

