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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00Z\x02\x00d\x00\x00k\x03\x00Z\x04\x00d\x00\x00k\x05\x00Z\x05\x00d\x00\x00k\x06\x00i\x07\x00Z\x08\x00d\x00\x00k\t\x00i\n\x00Z\x0b\x00d\x00\x00k\x0c\x00i\r\x00Z\x0e\x00d\x00\x00k\x0f\x00i\x10\x00Z\x11\x00d\x00\x00k\x12\x00i\x13\x00Z\x14\x00d\x00\x00k\x15\x00i\x16\x00Z\x17\x00d\x00\x00k\x18\x00Z\x18\x00d\x01\x00\x84\x00\x00Z\x19\x00d\x02\x00\x84\x00\x00Z\x1a\x00d\x03\x00\x84\x00\x00Z\x1b\x00d\x04\x00\x84\x00\x00Z\x1c\x00d\x05\x00\x84\x00\x00Z\x1d\x00d\x06\x00\x84\x00\x00Z\x1e\x00d\x07\x00\x84\x00\x00Z\x1f\x00d\x08\x00\x84\x00\x00Z \x00d\t\x00\x84\x00\x00Z!\x00d\n\x00\x84\x00\x00Z"\x00d\x00\x00S' (DC 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 5A 02 00 64 00 00 6B 03 00 5A 04 00 64 00 00 6B 05 00 5A 05 00 64 00 00 6B 06 00 69 07 00 5A 08 00 64 00 00 6B 09 00 69 0A 00 5A 0B 00 64 00 00 6B 0C 00 69 0D 00 5A 0E 00 64 00 00 6B 0F 00 69 10 00 5A 11 00 64 00 00 6B 12 00 69 13 00 5A 14 00 64 00 00 6B 15 00 69 16 00 5A 17 00 64 00 00 6B 18 00 5A 18 00 64 01 00 84 00 00 5A 19 00 64 02 00 84 00 00 5A 1A 00 64 03 00 84 00 00 5A 1B 00 64 04 00 84 00 00 5A 1C 00 64 05 00 84 00 00 5A 1D 00 64 06 00 84 00 00 5A 1E 00 64 07 00 84 00 00 5A 1F 00 64 08 00 84 00 00 5A 20 00 64 09 00 84 00 00 5A 21 00 64 0A 00 84 00 00 5A 22 00 64 00 00 53)
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
                 00000030     6B - IMPORT_NAME         'interlock.combat_abil_level'
                 00000033     69 - LOAD_ATTR           'combat_abil_level'
                 00000036     5A - STORE_NAME          'CombatAbilLevel'
                 00000039     64 - LOAD_CONST          None
                 0000003C     6B - IMPORT_NAME         'interlock.combat_modifiers'
                 0000003F     69 - LOAD_ATTR           'combat_modifiers'
                 00000042     5A - STORE_NAME          'CombatMods'
                 00000045     64 - LOAD_CONST          None
                 00000048     6B - IMPORT_NAME         'interlock.combat_innerstrength'
                 0000004B     69 - LOAD_ATTR           'combat_innerstrength'
                 0000004E     5A - STORE_NAME          'CombatIS'
                 00000051     64 - LOAD_CONST          None
                 00000054     6B - IMPORT_NAME         'interlock.combat_resolution'
                 00000057     69 - LOAD_ATTR           'combat_resolution'
                 0000005A     5A - STORE_NAME          'CombatRes'
                 0000005D     64 - LOAD_CONST          None
                 00000060     6B - IMPORT_NAME         'interlock.combat_utility'
                 00000063     69 - LOAD_ATTR           'combat_utility'
                 00000066     5A - STORE_NAME          'CU'
                 00000069     64 - LOAD_CONST          None
                 0000006C     6B - IMPORT_NAME         'interlock.combat_free_attacks'
                 0000006F     69 - LOAD_ATTR           'combat_free_attacks'
                 00000072     5A - STORE_NAME          'CombatFA'
                 00000075     64 - LOAD_CONST          None
                 00000078     6B - IMPORT_NAME         'combat_calculations'
                 0000007B     5A - STORE_NAME          'combat_calculations'
                 0000007E     64 - LOAD_CONST          CODE('SetCombatTargetSettings')
                 00000081     84 - MAKE_FUNCTION       r0000
                 00000084     5A - STORE_NAME          'SetCombatTargetSettings'
                 00000087     64 - LOAD_CONST          CODE('SetFreeAttackAbility')
                 0000008A     84 - MAKE_FUNCTION       r0000
                 0000008D     5A - STORE_NAME          'SetFreeAttackAbility'
                 00000090     64 - LOAD_CONST          CODE('IsATactic')
                 00000093     84 - MAKE_FUNCTION       r0000
                 00000096     5A - STORE_NAME          'IsATactic'
                 00000099     64 - LOAD_CONST          CODE('GetTacticalPointsGained')
                 0000009C     84 - MAKE_FUNCTION       r0000
                 0000009F     5A - STORE_NAME          'GetTacticalPointsGained'
                 000000A2     64 - LOAD_CONST          CODE('GetInnerStrengthUsed')
                 000000A5     84 - MAKE_FUNCTION       r0000
                 000000A8     5A - STORE_NAME          'GetInnerStrengthUsed'
                 000000AB     64 - LOAD_CONST          CODE('DoProneStatesMatch')
                 000000AE     84 - MAKE_FUNCTION       r0000
                 000000B1     5A - STORE_NAME          'DoProneStatesMatch'
                 000000B4     64 - LOAD_CONST          CODE('DetermineDominantProneType')
                 000000B7     84 - MAKE_FUNCTION       r0000
                 000000BA     5A - STORE_NAME          'DetermineDominantProneType'
                 000000BD     64 - LOAD_CONST          CODE('HasProneStateExpired')
                 000000C0     84 - MAKE_FUNCTION       r0000
                 000000C3     5A - STORE_NAME          'HasProneStateExpired'
                 000000C6     64 - LOAD_CONST          CODE('PerformFreeAttack')
                 000000C9     84 - MAKE_FUNCTION       r0000
                 000000CC     5A - STORE_NAME          'PerformFreeAttack'
                 000000CF     64 - LOAD_CONST          CODE('ResolveCombat')
                 000000D2     84 - MAKE_FUNCTION       r0000
                 000000D5     5A - STORE_NAME          'ResolveCombat'
                 000000D8     64 - LOAD_CONST          None
                 000000DB     53 - RETURN_VALUE        
             consts:
000000FA         TUPLE: (
000000FF             None (4E),
00000100             CODE:
                         argcount:
00000101                     LONG: 3L (03 00 00 00)
                         nlocals:
00000105                     LONG: 3L (03 00 00 00)
                         stacksize:
00000109                     LONG: 4L (04 00 00 00)
                         flags:
0000010D                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000111                     STR: 't\x00\x00i\x01\x00|\x00\x00|\x01\x00|\x02\x00\x83\x03\x00\x01d\x00\x00S' (17 00 00 00 74 00 00 69 01 00 7C 00 00 7C 01 00 7C 02 00 83 03 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CombatAbilLevel'
                             00000003     69 - LOAD_ATTR           'SetCombatTargetSettings'
                             00000006     7C - LOAD_FAST           'player'
                             00000009     7C - LOAD_FAST           'desiredSettings'
                             0000000C     7C - LOAD_FAST           'result'
                             0000000F     83 - CALL_FUNCTION       r0003
                             00000012     01 - POP_TOP             
                             00000013     64 - LOAD_CONST          None
                             00000016     53 - RETURN_VALUE        
                         consts:
0000012D                     TUPLE: (
00000132                         None (4E)
                             )
                         names:
00000133                     TUPLE: (
00000138                         STR: 'CombatAbilLevel' (0F 00 00 00 43 6F 6D 62 61 74 41 62 69 6C 4C 65 76 65 6C),
0000014C                         STR: 'SetCombatTargetSettings' (17 00 00 00 53 65 74 43 6F 6D 62 61 74 54 61 72 67 65 74 53 65 74 74 69 6E 67 73),
00000168                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00000173                         STR: 'desiredSettings' (0F 00 00 00 64 65 73 69 72 65 64 53 65 74 74 69 6E 67 73),
00000187                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74)
                             )
                         varnames:
00000192                     TUPLE: (
00000197                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
000001A2                         STR: 'desiredSettings' (0F 00 00 00 64 65 73 69 72 65 64 53 65 74 74 69 6E 67 73),
000001B6                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74)
                             )
                         freevars:
000001C1                     TUPLE: ()
                         cellvars:
000001C6                     TUPLE: ()
                         filename:
000001CB                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat.py' (3E 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 2E 70 79)
                         name:
0000020E                     STR: 'SetCombatTargetSettings' (17 00 00 00 53 65 74 43 6F 6D 62 61 74 54 61 72 67 65 74 53 65 74 74 69 6E 67 73)
                         firslineno:
0000022A                     LONG: 15L (0F 00 00 00)
                         lnotab:
0000022E                     STR: '\x00\x01' (02 00 00 00 00 01),
00000235             CODE:
                         argcount:
00000236                     LONG: 5L (05 00 00 00)
                         nlocals:
0000023A                     LONG: 5L (05 00 00 00)
                         stacksize:
0000023E                     LONG: 6L (06 00 00 00)
                         flags:
00000242                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000246                     STR: 't\x00\x00i\x01\x00|\x00\x00|\x01\x00|\x02\x00|\x03\x00|\x04\x00\x83\x05\x00\x01d\x00\x00S' (1D 00 00 00 74 00 00 69 01 00 7C 00 00 7C 01 00 7C 02 00 7C 03 00 7C 04 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CombatAbilLevel'
                             00000003     69 - LOAD_ATTR           'GetFreeAttackAbility'
                             00000006     7C - LOAD_FAST           'player'
                             00000009     7C - LOAD_FAST           'equippedItemID'
                             0000000C     7C - LOAD_FAST           'equippedItem'
                             0000000F     7C - LOAD_FAST           'itemAbility'
                             00000012     7C - LOAD_FAST           'itemAbilityLevel'
                             00000015     83 - CALL_FUNCTION       r0005
                             00000018     01 - POP_TOP             
                             00000019     64 - LOAD_CONST          None
                             0000001C     53 - RETURN_VALUE        
                         consts:
00000268                     TUPLE: (
0000026D                         None (4E)
                             )
                         names:
0000026E                     TUPLE: (
00000273                         STR: 'CombatAbilLevel' (0F 00 00 00 43 6F 6D 62 61 74 41 62 69 6C 4C 65 76 65 6C),
00000287                         STR: 'GetFreeAttackAbility' (14 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 41 62 69 6C 69 74 79),
000002A0                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
000002AB                         STR: 'equippedItemID' (0E 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D 49 44),
000002BE                         STR: 'equippedItem' (0C 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D),
000002CF                         STR: 'itemAbility' (0B 00 00 00 69 74 65 6D 41 62 69 6C 69 74 79),
000002DF                         STR: 'itemAbilityLevel' (10 00 00 00 69 74 65 6D 41 62 69 6C 69 74 79 4C 65 76 65 6C)
                             )
                         varnames:
000002F4                     TUPLE: (
000002F9                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00000304                         STR: 'equippedItemID' (0E 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D 49 44),
00000317                         STR: 'equippedItem' (0C 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D),
00000328                         STR: 'itemAbility' (0B 00 00 00 69 74 65 6D 41 62 69 6C 69 74 79),
00000338                         STR: 'itemAbilityLevel' (10 00 00 00 69 74 65 6D 41 62 69 6C 69 74 79 4C 65 76 65 6C)
                             )
                         freevars:
0000034D                     TUPLE: ()
                         cellvars:
00000352                     TUPLE: ()
                         filename:
00000357                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat.py' (3E 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 2E 70 79)
                         name:
0000039A                     STR: 'SetFreeAttackAbility' (14 00 00 00 53 65 74 46 72 65 65 41 74 74 61 63 6B 41 62 69 6C 69 74 79)
                         firslineno:
000003B3                     LONG: 18L (12 00 00 00)
                         lnotab:
000003B7                     STR: '\x00\x01' (02 00 00 00 00 01),
000003BE             CODE:
                         argcount:
000003BF                     LONG: 1L (01 00 00 00)
                         nlocals:
000003C3                     LONG: 1L (01 00 00 00)
                         stacksize:
000003C7                     LONG: 2L (02 00 00 00)
                         flags:
000003CB                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000003CF                     STR: '|\x00\x00i\x01\x00t\x02\x00i\x03\x00i\x04\x00j\x02\x00p\x13\x00\x01|\x00\x00i\x01\x00t\x02\x00i\x03\x00i\x05\x00j\x02\x00o\x08\x00\x01t\x06\x00Sn\x01\x00\x01t\x07\x00Sd\x00\x00S' (3C 00 00 00 7C 00 00 69 01 00 74 02 00 69 03 00 69 04 00 6A 02 00 70 13 00 01 7C 00 00 69 01 00 74 02 00 69 03 00 69 05 00 6A 02 00 6F 08 00 01 74 06 00 53 6E 01 00 01 74 07 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'tacticalSettings'
                             00000003     69 - LOAD_ATTR           'elementType'
                             00000006     74 - LOAD_GLOBAL         'constants'
                             00000009     69 - LOAD_ATTR           'combat'
                             0000000C     69 - LOAD_ATTR           'QT_NORMAL'
                             0000000F     6A - COMPARE_OP          "=="
                             00000012     70 - JUMP_IF_TRUE        -> 00000028
                             00000015     01 - POP_TOP             
                             00000016     7C - LOAD_FAST           'tacticalSettings'
                             00000019     69 - LOAD_ATTR           'elementType'
                             0000001C     74 - LOAD_GLOBAL         'constants'
                             0000001F     69 - LOAD_ATTR           'combat'
                             00000022     69 - LOAD_ATTR           'QT_SPECIAL_TACTIC'
                             00000025     6A - COMPARE_OP          "=="
                             00000028     6F - JUMP_IF_FALSE       -> 00000033
                             0000002B     01 - POP_TOP             
                             0000002C     74 - LOAD_GLOBAL         'True'
                             0000002F     53 - RETURN_VALUE        
                             00000030     6E - JUMP_FORWARD        -> 00000034
                             00000033     01 - POP_TOP             
                             00000034     74 - LOAD_GLOBAL         'False'
                             00000037     53 - RETURN_VALUE        
                             00000038     64 - LOAD_CONST          None
                             0000003B     53 - RETURN_VALUE        
                         consts:
00000410                     TUPLE: (
00000415                         None (4E)
                             )
                         names:
00000416                     TUPLE: (
0000041B                         STR: 'tacticalSettings' (10 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67 73),
00000430                         STR: 'elementType' (0B 00 00 00 65 6C 65 6D 65 6E 74 54 79 70 65),
00000440                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
0000044E                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
00000459                         STR: 'QT_NORMAL' (09 00 00 00 51 54 5F 4E 4F 52 4D 41 4C),
00000467                         STR: 'QT_SPECIAL_TACTIC' (11 00 00 00 51 54 5F 53 50 45 43 49 41 4C 5F 54 41 43 54 49 43),
0000047D                         STR: 'True' (04 00 00 00 54 72 75 65),
00000486                         STR: 'False' (05 00 00 00 46 61 6C 73 65)
                             )
                         varnames:
00000490                     TUPLE: (
00000495                         STR: 'tacticalSettings' (10 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67 73)
                             )
                         freevars:
000004AA                     TUPLE: ()
                         cellvars:
000004AF                     TUPLE: ()
                         filename:
000004B4                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat.py' (3E 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 2E 70 79)
                         name:
000004F7                     STR: 'IsATactic' (09 00 00 00 49 73 41 54 61 63 74 69 63)
                         firslineno:
00000505                     LONG: 21L (15 00 00 00)
                         lnotab:
00000509                     STR: '\x00\x01,\x01\x08\x02' (06 00 00 00 00 01 2C 01 08 02),
00000514             CODE:
                         argcount:
00000515                     LONG: 2L (02 00 00 00)
                         nlocals:
00000519                     LONG: 2L (02 00 00 00)
                         stacksize:
0000051D                     LONG: 2L (02 00 00 00)
                         flags:
00000521                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000525                     STR: 't\x00\x00|\x01\x00\x83\x01\x00\x0co\x08\x00\x01d\x01\x00Sn\x01\x00\x01|\x01\x00i\x02\x00t\x03\x00i\x04\x00i\x05\x00j\x02\x00o\x08\x00\x01d\x01\x00Sn\x01\x00\x01|\x01\x00i\x06\x00t\x03\x00i\x04\x00i\x07\x00j\x02\x00o\x08\x00\x01d\x02\x00Sn=\x00\x01|\x01\x00i\x06\x00t\x03\x00i\x04\x00i\x08\x00j\x02\x00o\x08\x00\x01d\x02\x00Sn\x1f\x00\x01|\x01\x00i\x06\x00t\x03\x00i\x04\x00i\t\x00j\x02\x00o\x08\x00\x01d\x03\x00Sn\x01\x00\x01d\x00\x00S' (92 00 00 00 74 00 00 7C 01 00 83 01 00 0C 6F 08 00 01 64 01 00 53 6E 01 00 01 7C 01 00 69 02 00 74 03 00 69 04 00 69 05 00 6A 02 00 6F 08 00 01 64 01 00 53 6E 01 00 01 7C 01 00 69 06 00 74 03 00 69 04 00 69 07 00 6A 02 00 6F 08 00 01 64 02 00 53 6E 3D 00 01 7C 01 00 69 06 00 74 03 00 69 04 00 69 08 00 6A 02 00 6F 08 00 01 64 02 00 53 6E 1F 00 01 7C 01 00 69 06 00 74 03 00 69 04 00 69 09 00 6A 02 00 6F 08 00 01 64 03 00 53 6E 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'IsATactic'
                             00000003     7C - LOAD_FAST           'tacticalSettings'
                             00000006     83 - CALL_FUNCTION       r0001
                             00000009     0C - UNARY_NOT           
                             0000000A     6F - JUMP_IF_FALSE       -> 00000015
                             0000000D     01 - POP_TOP             
                             0000000E     64 - LOAD_CONST          0
                             00000011     53 - RETURN_VALUE        
                             00000012     6E - JUMP_FORWARD        -> 00000016
                             00000015     01 - POP_TOP             
                             00000016     7C - LOAD_FAST           'tacticalSettings'
                             00000019     69 - LOAD_ATTR           'tacticalSetting'
                             0000001C     74 - LOAD_GLOBAL         'constants'
                             0000001F     69 - LOAD_ATTR           'combat'
                             00000022     69 - LOAD_ATTR           'BLOCK'
                             00000025     6A - COMPARE_OP          "=="
                             00000028     6F - JUMP_IF_FALSE       -> 00000033
                             0000002B     01 - POP_TOP             
                             0000002C     64 - LOAD_CONST          0
                             0000002F     53 - RETURN_VALUE        
                             00000030     6E - JUMP_FORWARD        -> 00000034
                             00000033     01 - POP_TOP             
                             00000034     7C - LOAD_FAST           'tacticalSettings'
                             00000037     69 - LOAD_ATTR           'tacticType'
                             0000003A     74 - LOAD_GLOBAL         'constants'
                             0000003D     69 - LOAD_ATTR           'combat'
                             00000040     69 - LOAD_ATTR           'TT_INVALID'
                             00000043     6A - COMPARE_OP          "=="
                             00000046     6F - JUMP_IF_FALSE       -> 00000051
                             00000049     01 - POP_TOP             
                             0000004A     64 - LOAD_CONST          1
                             0000004D     53 - RETURN_VALUE        
                             0000004E     6E - JUMP_FORWARD        -> 0000008E
                             00000051     01 - POP_TOP             
                             00000052     7C - LOAD_FAST           'tacticalSettings'
                             00000055     69 - LOAD_ATTR           'tacticType'
                             00000058     74 - LOAD_GLOBAL         'constants'
                             0000005B     69 - LOAD_ATTR           'combat'
                             0000005E     69 - LOAD_ATTR           'TT_PRECISE'
                             00000061     6A - COMPARE_OP          "=="
                             00000064     6F - JUMP_IF_FALSE       -> 0000006F
                             00000067     01 - POP_TOP             
                             00000068     64 - LOAD_CONST          1
                             0000006B     53 - RETURN_VALUE        
                             0000006C     6E - JUMP_FORWARD        -> 0000008E
                             0000006F     01 - POP_TOP             
                             00000070     7C - LOAD_FAST           'tacticalSettings'
                             00000073     69 - LOAD_ATTR           'tacticType'
                             00000076     74 - LOAD_GLOBAL         'constants'
                             00000079     69 - LOAD_ATTR           'combat'
                             0000007C     69 - LOAD_ATTR           'TT_ENERGIZED'
                             0000007F     6A - COMPARE_OP          "=="
                             00000082     6F - JUMP_IF_FALSE       -> 0000008D
                             00000085     01 - POP_TOP             
                             00000086     64 - LOAD_CONST          2
                             00000089     53 - RETURN_VALUE        
                             0000008A     6E - JUMP_FORWARD        -> 0000008E
                             0000008D     01 - POP_TOP             
                             0000008E     64 - LOAD_CONST          None
                             00000091     53 - RETURN_VALUE        
                         consts:
000005BC                     TUPLE: (
000005C1                         None (4E),
000005C2                         INT: 0 (00 00 00 00),
000005C7                         INT: 1 (01 00 00 00),
000005CC                         INT: 2 (02 00 00 00)
                             )
                         names:
000005D1                     TUPLE: (
000005D6                         STR: 'IsATactic' (09 00 00 00 49 73 41 54 61 63 74 69 63),
000005E4                         STR: 'tacticalSettings' (10 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67 73),
000005F9                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
0000060D                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
0000061B                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
00000626                         STR: 'BLOCK' (05 00 00 00 42 4C 4F 43 4B),
00000630                         STR: 'tacticType' (0A 00 00 00 74 61 63 74 69 63 54 79 70 65),
0000063F                         STR: 'TT_INVALID' (0A 00 00 00 54 54 5F 49 4E 56 41 4C 49 44),
0000064E                         STR: 'TT_PRECISE' (0A 00 00 00 54 54 5F 50 52 45 43 49 53 45),
0000065D                         STR: 'TT_ENERGIZED' (0C 00 00 00 54 54 5F 45 4E 45 52 47 49 5A 45 44)
                             )
                         varnames:
0000066E                     TUPLE: (
00000673                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
0000067E                         STR: 'tacticalSettings' (10 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67 73)
                             )
                         freevars:
00000693                     TUPLE: ()
                         cellvars:
00000698                     TUPLE: ()
                         filename:
0000069D                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat.py' (3E 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 2E 70 79)
                         name:
000006E0                     STR: 'GetTacticalPointsGained' (17 00 00 00 47 65 74 54 61 63 74 69 63 61 6C 50 6F 69 6E 74 73 47 61 69 6E 65 64)
                         firslineno:
000006FC                     LONG: 27L (1B 00 00 00)
                         lnotab:
00000700                     STR: '\x00\x01\x0e\x01\x08\x02\x16\x01\x08\x02\x16\x01\x08\x01\x16\x01\x08\x01\x16\x01' (14 00 00 00 00 01 0E 01 08 02 16 01 08 02 16 01 08 01 16 01 08 01 16 01),
00000719             CODE:
                         argcount:
0000071A                     LONG: 2L (02 00 00 00)
                         nlocals:
0000071E                     LONG: 3L (03 00 00 00)
                         stacksize:
00000722                     LONG: 2L (02 00 00 00)
                         flags:
00000726                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000072A                     STR: 'd\x01\x00}\x02\x00|\x01\x00t\x02\x00i\x03\x00i\x04\x00j\x02\x00o\x1e\x00\x01t\x05\x00i\x06\x00o\n\x00\x01d\x02\x00}\x02\x00q=\x00\x01d\x01\x00}\x02\x00n\x07\x00\x01d\x01\x00}\x02\x00|\x02\x00Sd\x00\x00S' (45 00 00 00 64 01 00 7D 02 00 7C 01 00 74 02 00 69 03 00 69 04 00 6A 02 00 6F 1E 00 01 74 05 00 69 06 00 6F 0A 00 01 64 02 00 7D 02 00 71 3D 00 01 64 01 00 7D 02 00 6E 07 00 01 64 01 00 7D 02 00 7C 02 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          0
                             00000003     7D - STORE_FAST          'inner_strength_used'
                             00000006     7C - LOAD_FAST           'tacticalSetting'
                             00000009     74 - LOAD_GLOBAL         'constants'
                             0000000C     69 - LOAD_ATTR           'combat'
                             0000000F     69 - LOAD_ATTR           'BLOCK'
                             00000012     6A - COMPARE_OP          "=="
                             00000015     6F - JUMP_IF_FALSE       -> 00000036
                             00000018     01 - POP_TOP             
                             00000019     74 - LOAD_GLOBAL         'consolevar'
                             0000001C     69 - LOAD_ATTR           'GainISFromBlocks'
                             0000001F     6F - JUMP_IF_FALSE       -> 0000002C
                             00000022     01 - POP_TOP             
                             00000023     64 - LOAD_CONST          -10
                             00000026     7D - STORE_FAST          'inner_strength_used'
                             00000029     71 - JUMP_ABSOLUTE       -> 0000003D
                             0000002C     01 - POP_TOP             
                             0000002D     64 - LOAD_CONST          0
                             00000030     7D - STORE_FAST          'inner_strength_used'
                             00000033     6E - JUMP_FORWARD        -> 0000003D
                             00000036     01 - POP_TOP             
                             00000037     64 - LOAD_CONST          0
                             0000003A     7D - STORE_FAST          'inner_strength_used'
                             0000003D     7C - LOAD_FAST           'inner_strength_used'
                             00000040     53 - RETURN_VALUE        
                             00000041     64 - LOAD_CONST          None
                             00000044     53 - RETURN_VALUE        
                         consts:
00000774                     TUPLE: (
00000779                         None (4E),
0000077A                         INT: 0 (00 00 00 00),
0000077F                         INT: -10 (F6 FF FF FF)
                             )
                         names:
00000784                     TUPLE: (
00000789                         STR: 'inner_strength_used' (13 00 00 00 69 6E 6E 65 72 5F 73 74 72 65 6E 67 74 68 5F 75 73 65 64),
000007A1                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
000007B5                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
000007C3                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
000007CE                         STR: 'BLOCK' (05 00 00 00 42 4C 4F 43 4B),
000007D8                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
000007E7                         STR: 'GainISFromBlocks' (10 00 00 00 47 61 69 6E 49 53 46 72 6F 6D 42 6C 6F 63 6B 73)
                             )
                         varnames:
000007FC                     TUPLE: (
00000801                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
0000080C                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
00000820                         STR: 'inner_strength_used' (13 00 00 00 69 6E 6E 65 72 5F 73 74 72 65 6E 67 74 68 5F 75 73 65 64)
                             )
                         freevars:
00000838                     TUPLE: ()
                         cellvars:
0000083D                     TUPLE: ()
                         filename:
00000842                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat.py' (3E 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 2E 70 79)
                         name:
00000885                     STR: 'GetInnerStrengthUsed' (14 00 00 00 47 65 74 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 55 73 65 64)
                         firslineno:
0000089E                     LONG: 41L (29 00 00 00)
                         lnotab:
000008A2                     STR: '\x00\x01\x06\x06\x13\x01\n\x01\n\x02\n\x02\x06\x02' (0E 00 00 00 00 01 06 06 13 01 0A 01 0A 02 0A 02 06 02),
000008B5             CODE:
                         argcount:
000008B6                     LONG: 2L (02 00 00 00)
                         nlocals:
000008BA                     LONG: 3L (03 00 00 00)
                         stacksize:
000008BE                     LONG: 2L (02 00 00 00)
                         flags:
000008C2                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000008C6                     STR: '|\x00\x00t\x01\x00i\x02\x00@}\x02\x00|\x02\x00d\x01\x00j\x02\x00o\n\x00\x01|\x01\x00d\x01\x00j\x02\x00o\x08\x00\x01t\x05\x00Sn\x01\x00\x01|\x02\x00|\x01\x00@d\x01\x00j\x04\x00o\x08\x00\x01t\x05\x00Sn\x01\x00\x01t\x06\x00Sd\x00\x00S' (50 00 00 00 7C 00 00 74 01 00 69 02 00 40 7D 02 00 7C 02 00 64 01 00 6A 02 00 6F 0A 00 01 7C 01 00 64 01 00 6A 02 00 6F 08 00 01 74 05 00 53 6E 01 00 01 7C 02 00 7C 01 00 40 64 01 00 6A 04 00 6F 08 00 01 74 05 00 53 6E 01 00 01 74 06 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'player_flags'
                             00000003     74 - LOAD_GLOBAL         'CD'
                             00000006     69 - LOAD_ATTR           'COMBAT_CONTROLLED_MASK'
                             00000009     40 - BINARY_AND          
                             0000000A     7D - STORE_FAST          'player_combat_flags'
                             0000000D     7C - LOAD_FAST           'player_combat_flags'
                             00000010     64 - LOAD_CONST          0
                             00000013     6A - COMPARE_OP          "=="
                             00000016     6F - JUMP_IF_FALSE       -> 00000023
                             00000019     01 - POP_TOP             
                             0000001A     7C - LOAD_FAST           'move_flags'
                             0000001D     64 - LOAD_CONST          0
                             00000020     6A - COMPARE_OP          "=="
                             00000023     6F - JUMP_IF_FALSE       -> 0000002E
                             00000026     01 - POP_TOP             
                             00000027     74 - LOAD_GLOBAL         'True'
                             0000002A     53 - RETURN_VALUE        
                             0000002B     6E - JUMP_FORWARD        -> 0000002F
                             0000002E     01 - POP_TOP             
                             0000002F     7C - LOAD_FAST           'player_combat_flags'
                             00000032     7C - LOAD_FAST           'move_flags'
                             00000035     40 - BINARY_AND          
                             00000036     64 - LOAD_CONST          0
                             00000039     6A - COMPARE_OP          ">"
                             0000003C     6F - JUMP_IF_FALSE       -> 00000047
                             0000003F     01 - POP_TOP             
                             00000040     74 - LOAD_GLOBAL         'True'
                             00000043     53 - RETURN_VALUE        
                             00000044     6E - JUMP_FORWARD        -> 00000048
                             00000047     01 - POP_TOP             
                             00000048     74 - LOAD_GLOBAL         'False'
                             0000004B     53 - RETURN_VALUE        
                             0000004C     64 - LOAD_CONST          None
                             0000004F     53 - RETURN_VALUE        
                         consts:
0000091B                     TUPLE: (
00000920                         None (4E),
00000921                         INT: 0 (00 00 00 00)
                             )
                         names:
00000926                     TUPLE: (
0000092B                         STR: 'player_flags' (0C 00 00 00 70 6C 61 79 65 72 5F 66 6C 61 67 73),
0000093C                         STR: 'CD' (02 00 00 00 43 44),
00000943                         STR: 'COMBAT_CONTROLLED_MASK' (16 00 00 00 43 4F 4D 42 41 54 5F 43 4F 4E 54 52 4F 4C 4C 45 44 5F 4D 41 53 4B),
0000095E                         STR: 'player_combat_flags' (13 00 00 00 70 6C 61 79 65 72 5F 63 6F 6D 62 61 74 5F 66 6C 61 67 73),
00000976                         STR: 'move_flags' (0A 00 00 00 6D 6F 76 65 5F 66 6C 61 67 73),
00000985                         STR: 'True' (04 00 00 00 54 72 75 65),
0000098E                         STR: 'False' (05 00 00 00 46 61 6C 73 65)
                             )
                         varnames:
00000998                     TUPLE: (
0000099D                         STR: 'player_flags' (0C 00 00 00 70 6C 61 79 65 72 5F 66 6C 61 67 73),
000009AE                         STR: 'move_flags' (0A 00 00 00 6D 6F 76 65 5F 66 6C 61 67 73),
000009BD                         STR: 'player_combat_flags' (13 00 00 00 70 6C 61 79 65 72 5F 63 6F 6D 62 61 74 5F 66 6C 61 67 73)
                             )
                         freevars:
000009D5                     TUPLE: ()
                         cellvars:
000009DA                     TUPLE: ()
                         filename:
000009DF                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat.py' (3E 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 2E 70 79)
                         name:
00000A22                     STR: 'DoProneStatesMatch' (12 00 00 00 44 6F 50 72 6F 6E 65 53 74 61 74 65 73 4D 61 74 63 68)
                         firslineno:
00000A39                     LONG: 68L (44 00 00 00)
                         lnotab:
00000A3D                     STR: '\x00\x02\r\x01\x1a\x01\x08\x03\x11\x01\x08\x02' (0C 00 00 00 00 02 0D 01 1A 01 08 03 11 01 08 02),
00000A4E             CODE:
                         argcount:
00000A4F                     LONG: 1L (01 00 00 00)
                         nlocals:
00000A53                     LONG: 1L (01 00 00 00)
                         stacksize:
00000A57                     LONG: 2L (02 00 00 00)
                         flags:
00000A5B                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000A5F                     STR: '|\x00\x00t\x01\x00i\x02\x00i\x03\x00@o\x0e\x00\x01t\x01\x00i\x02\x00i\x03\x00Sn\x18\x01\x01|\x00\x00t\x01\x00i\x02\x00i\x04\x00@o\x0e\x00\x01t\x01\x00i\x02\x00i\x04\x00Sn\xf9\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x05\x00@o\x0e\x00\x01t\x01\x00i\x02\x00i\x05\x00Sn\xda\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x06\x00@o\x0e\x00\x01t\x01\x00i\x02\x00i\x06\x00Sn\xbb\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x07\x00@o\x0e\x00\x01t\x01\x00i\x02\x00i\x07\x00Sn\x9c\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x08\x00@o\x0e\x00\x01t\x01\x00i\x02\x00i\x08\x00Sn}\x00\x01|\x00\x00t\x01\x00i\x02\x00i\t\x00@o\x0e\x00\x01t\x01\x00i\x02\x00i\t\x00Sn^\x00\x01|\x00\x00t\x01\x00i\x02\x00i\n\x00@o\x0e\x00\x01t\x01\x00i\x02\x00i\n\x00Sn?\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x0b\x00@o\x0e\x00\x01t\x01\x00i\x02\x00i\x0b\x00Sn \x00\x01|\x00\x00t\x01\x00i\x02\x00i\x0c\x00@o\x0e\x00\x01t\x01\x00i\x02\x00i\x0c\x00Sn\x01\x00\x01d\x01\x00Sd\x00\x00S' (3E 01 00 00 7C 00 00 74 01 00 69 02 00 69 03 00 40 6F 0E 00 01 74 01 00 69 02 00 69 03 00 53 6E 18 01 01 7C 00 00 74 01 00 69 02 00 69 04 00 40 6F 0E 00 01 74 01 00 69 02 00 69 04 00 53 6E F9 00 01 7C 00 00 74 01 00 69 02 00 69 05 00 40 6F 0E 00 01 74 01 00 69 02 00 69 05 00 53 6E DA 00 01 7C 00 00 74 01 00 69 02 00 69 06 00 40 6F 0E 00 01 74 01 00 69 02 00 69 06 00 53 6E BB 00 01 7C 00 00 74 01 00 69 02 00 69 07 00 40 6F 0E 00 01 74 01 00 69 02 00 69 07 00 53 6E 9C 00 01 7C 00 00 74 01 00 69 02 00 69 08 00 40 6F 0E 00 01 74 01 00 69 02 00 69 08 00 53 6E 7D 00 01 7C 00 00 74 01 00 69 02 00 69 09 00 40 6F 0E 00 01 74 01 00 69 02 00 69 09 00 53 6E 5E 00 01 7C 00 00 74 01 00 69 02 00 69 0A 00 40 6F 0E 00 01 74 01 00 69 02 00 69 0A 00 53 6E 3F 00 01 7C 00 00 74 01 00 69 02 00 69 0B 00 40 6F 0E 00 01 74 01 00 69 02 00 69 0B 00 53 6E 20 00 01 7C 00 00 74 01 00 69 02 00 69 0C 00 40 6F 0E 00 01 74 01 00 69 02 00 69 0C 00 53 6E 01 00 01 64 01 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'flags'
                             00000003     74 - LOAD_GLOBAL         'constants'
                             00000006     69 - LOAD_ATTR           'combat_prone'
                             00000009     69 - LOAD_ATTR           'LAYING_FACEDOWN'
                             0000000C     40 - BINARY_AND          
                             0000000D     6F - JUMP_IF_FALSE       -> 0000001E
                             00000010     01 - POP_TOP             
                             00000011     74 - LOAD_GLOBAL         'constants'
                             00000014     69 - LOAD_ATTR           'combat_prone'
                             00000017     69 - LOAD_ATTR           'LAYING_FACEDOWN'
                             0000001A     53 - RETURN_VALUE        
                             0000001B     6E - JUMP_FORWARD        -> 00000136
                             0000001E     01 - POP_TOP             
                             0000001F     7C - LOAD_FAST           'flags'
                             00000022     74 - LOAD_GLOBAL         'constants'
                             00000025     69 - LOAD_ATTR           'combat_prone'
                             00000028     69 - LOAD_ATTR           'LAYING_FACEUP'
                             0000002B     40 - BINARY_AND          
                             0000002C     6F - JUMP_IF_FALSE       -> 0000003D
                             0000002F     01 - POP_TOP             
                             00000030     74 - LOAD_GLOBAL         'constants'
                             00000033     69 - LOAD_ATTR           'combat_prone'
                             00000036     69 - LOAD_ATTR           'LAYING_FACEUP'
                             00000039     53 - RETURN_VALUE        
                             0000003A     6E - JUMP_FORWARD        -> 00000136
                             0000003D     01 - POP_TOP             
                             0000003E     7C - LOAD_FAST           'flags'
                             00000041     74 - LOAD_GLOBAL         'constants'
                             00000044     69 - LOAD_ATTR           'combat_prone'
                             00000047     69 - LOAD_ATTR           'VISUAL_FACEDOWN'
                             0000004A     40 - BINARY_AND          
                             0000004B     6F - JUMP_IF_FALSE       -> 0000005C
                             0000004E     01 - POP_TOP             
                             0000004F     74 - LOAD_GLOBAL         'constants'
                             00000052     69 - LOAD_ATTR           'combat_prone'
                             00000055     69 - LOAD_ATTR           'VISUAL_FACEDOWN'
                             00000058     53 - RETURN_VALUE        
                             00000059     6E - JUMP_FORWARD        -> 00000136
                             0000005C     01 - POP_TOP             
                             0000005D     7C - LOAD_FAST           'flags'
                             00000060     74 - LOAD_GLOBAL         'constants'
                             00000063     69 - LOAD_ATTR           'combat_prone'
                             00000066     69 - LOAD_ATTR           'VISUAL_FACEUP'
                             00000069     40 - BINARY_AND          
                             0000006A     6F - JUMP_IF_FALSE       -> 0000007B
                             0000006D     01 - POP_TOP             
                             0000006E     74 - LOAD_GLOBAL         'constants'
                             00000071     69 - LOAD_ATTR           'combat_prone'
                             00000074     69 - LOAD_ATTR           'VISUAL_FACEUP'
                             00000077     53 - RETURN_VALUE        
                             00000078     6E - JUMP_FORWARD        -> 00000136
                             0000007B     01 - POP_TOP             
                             0000007C     7C - LOAD_FAST           'flags'
                             0000007F     74 - LOAD_GLOBAL         'constants'
                             00000082     69 - LOAD_ATTR           'combat_prone'
                             00000085     69 - LOAD_ATTR           'I_LB_TRANSITION'
                             00000088     40 - BINARY_AND          
                             00000089     6F - JUMP_IF_FALSE       -> 0000009A
                             0000008C     01 - POP_TOP             
                             0000008D     74 - LOAD_GLOBAL         'constants'
                             00000090     69 - LOAD_ATTR           'combat_prone'
                             00000093     69 - LOAD_ATTR           'I_LB_TRANSITION'
                             00000096     53 - RETURN_VALUE        
                             00000097     6E - JUMP_FORWARD        -> 00000136
                             0000009A     01 - POP_TOP             
                             0000009B     7C - LOAD_FAST           'flags'
                             0000009E     74 - LOAD_GLOBAL         'constants'
                             000000A1     69 - LOAD_ATTR           'combat_prone'
                             000000A4     69 - LOAD_ATTR           'V_LB_TRANSITION'
                             000000A7     40 - BINARY_AND          
                             000000A8     6F - JUMP_IF_FALSE       -> 000000B9
                             000000AB     01 - POP_TOP             
                             000000AC     74 - LOAD_GLOBAL         'constants'
                             000000AF     69 - LOAD_ATTR           'combat_prone'
                             000000B2     69 - LOAD_ATTR           'V_LB_TRANSITION'
                             000000B5     53 - RETURN_VALUE        
                             000000B6     6E - JUMP_FORWARD        -> 00000136
                             000000B9     01 - POP_TOP             
                             000000BA     7C - LOAD_FAST           'flags'
                             000000BD     74 - LOAD_GLOBAL         'constants'
                             000000C0     69 - LOAD_ATTR           'combat_prone'
                             000000C3     69 - LOAD_ATTR           'BLIND'
                             000000C6     40 - BINARY_AND          
                             000000C7     6F - JUMP_IF_FALSE       -> 000000D8
                             000000CA     01 - POP_TOP             
                             000000CB     74 - LOAD_GLOBAL         'constants'
                             000000CE     69 - LOAD_ATTR           'combat_prone'
                             000000D1     69 - LOAD_ATTR           'BLIND'
                             000000D4     53 - RETURN_VALUE        
                             000000D5     6E - JUMP_FORWARD        -> 00000136
                             000000D8     01 - POP_TOP             
                             000000D9     7C - LOAD_FAST           'flags'
                             000000DC     74 - LOAD_GLOBAL         'constants'
                             000000DF     69 - LOAD_ATTR           'combat_prone'
                             000000E2     69 - LOAD_ATTR           'STUNNED'
                             000000E5     40 - BINARY_AND          
                             000000E6     6F - JUMP_IF_FALSE       -> 000000F7
                             000000E9     01 - POP_TOP             
                             000000EA     74 - LOAD_GLOBAL         'constants'
                             000000ED     69 - LOAD_ATTR           'combat_prone'
                             000000F0     69 - LOAD_ATTR           'STUNNED'
                             000000F3     53 - RETURN_VALUE        
                             000000F4     6E - JUMP_FORWARD        -> 00000136
                             000000F7     01 - POP_TOP             
                             000000F8     7C - LOAD_FAST           'flags'
                             000000FB     74 - LOAD_GLOBAL         'constants'
                             000000FE     69 - LOAD_ATTR           'combat_prone'
                             00000101     69 - LOAD_ATTR           'CONFUSED'
                             00000104     40 - BINARY_AND          
                             00000105     6F - JUMP_IF_FALSE       -> 00000116
                             00000108     01 - POP_TOP             
                             00000109     74 - LOAD_GLOBAL         'constants'
                             0000010C     69 - LOAD_ATTR           'combat_prone'
                             0000010F     69 - LOAD_ATTR           'CONFUSED'
                             00000112     53 - RETURN_VALUE        
                             00000113     6E - JUMP_FORWARD        -> 00000136
                             00000116     01 - POP_TOP             
                             00000117     7C - LOAD_FAST           'flags'
                             0000011A     74 - LOAD_GLOBAL         'constants'
                             0000011D     69 - LOAD_ATTR           'combat_prone'
                             00000120     69 - LOAD_ATTR           'ENRAGED'
                             00000123     40 - BINARY_AND          
                             00000124     6F - JUMP_IF_FALSE       -> 00000135
                             00000127     01 - POP_TOP             
                             00000128     74 - LOAD_GLOBAL         'constants'
                             0000012B     69 - LOAD_ATTR           'combat_prone'
                             0000012E     69 - LOAD_ATTR           'ENRAGED'
                             00000131     53 - RETURN_VALUE        
                             00000132     6E - JUMP_FORWARD        -> 00000136
                             00000135     01 - POP_TOP             
                             00000136     64 - LOAD_CONST          0
                             00000139     53 - RETURN_VALUE        
                             0000013A     64 - LOAD_CONST          None
                             0000013D     53 - RETURN_VALUE        
                         consts:
00000BA2                     TUPLE: (
00000BA7                         None (4E),
00000BA8                         INT: 0 (00 00 00 00)
                             )
                         names:
00000BAD                     TUPLE: (
00000BB2                         STR: 'flags' (05 00 00 00 66 6C 61 67 73),
00000BBC                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00000BCA                         STR: 'combat_prone' (0C 00 00 00 63 6F 6D 62 61 74 5F 70 72 6F 6E 65),
00000BDB                         STR: 'LAYING_FACEDOWN' (0F 00 00 00 4C 41 59 49 4E 47 5F 46 41 43 45 44 4F 57 4E),
00000BEF                         STR: 'LAYING_FACEUP' (0D 00 00 00 4C 41 59 49 4E 47 5F 46 41 43 45 55 50),
00000C01                         STR: 'VISUAL_FACEDOWN' (0F 00 00 00 56 49 53 55 41 4C 5F 46 41 43 45 44 4F 57 4E),
00000C15                         STR: 'VISUAL_FACEUP' (0D 00 00 00 56 49 53 55 41 4C 5F 46 41 43 45 55 50),
00000C27                         STR: 'I_LB_TRANSITION' (0F 00 00 00 49 5F 4C 42 5F 54 52 41 4E 53 49 54 49 4F 4E),
00000C3B                         STR: 'V_LB_TRANSITION' (0F 00 00 00 56 5F 4C 42 5F 54 52 41 4E 53 49 54 49 4F 4E),
00000C4F                         STR: 'BLIND' (05 00 00 00 42 4C 49 4E 44),
00000C59                         STR: 'STUNNED' (07 00 00 00 53 54 55 4E 4E 45 44),
00000C65                         STR: 'CONFUSED' (08 00 00 00 43 4F 4E 46 55 53 45 44),
00000C72                         STR: 'ENRAGED' (07 00 00 00 45 4E 52 41 47 45 44)
                             )
                         varnames:
00000C7E                     TUPLE: (
00000C83                         STR: 'flags' (05 00 00 00 66 6C 61 67 73)
                             )
                         freevars:
00000C8D                     TUPLE: ()
                         cellvars:
00000C92                     TUPLE: ()
                         filename:
00000C97                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat.py' (3E 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 2E 70 79)
                         name:
00000CDA                     STR: 'DetermineDominantProneType' (1A 00 00 00 44 65 74 65 72 6D 69 6E 65 44 6F 6D 69 6E 61 6E 74 50 72 6F 6E 65 54 79 70 65)
                         firslineno:
00000CF9                     LONG: 80L (50 00 00 00)
                         lnotab:
00000CFD                     STR: '\x00\x02\x11\x01\x0e\x01\x11\x01\x0e\x01\x11\x01\x0e\x01\x11\x01\x0e\x01\x11\x01\x0e\x01\x11\x01\x0e\x01\x11\x01\x0e\x01\x11\x01\x0e\x01\x11\x01\x0e\x01\x11\x01\x0e\x03' (2A 00 00 00 00 02 11 01 0E 01 11 01 0E 01 11 01 0E 01 11 01 0E 01 11 01 0E 01 11 01 0E 01 11 01 0E 01 11 01 0E 01 11 01 0E 01 11 01 0E 03),
00000D2C             CODE:
                         argcount:
00000D2D                     LONG: 3L (03 00 00 00)
                         nlocals:
00000D31                     LONG: 3L (03 00 00 00)
                         stacksize:
00000D35                     LONG: 5L (05 00 00 00)
                         flags:
00000D39                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000D3D                     STR: 't\x00\x00i\x01\x00d\x01\x00|\x00\x00|\x01\x00f\x02\x00\x16d\x02\x00\x83\x02\x00\x01t\x04\x00i\x05\x00d\x03\x00j\x02\x00o\x1f\x00\x01t\x00\x00i\x01\x00d\x04\x00t\x04\x00i\x05\x00\x16d\x02\x00\x83\x02\x00\x01t\x06\x00Sn\x01\x00\x01|\x00\x00t\x07\x00i\x08\x00i\t\x00j\x05\x00o.\x00\x01t\x00\x00i\x01\x00d\x05\x00|\x00\x00t\n\x00t\x07\x00i\x08\x00i\t\x00\x83\x01\x00f\x02\x00\x16d\x02\x00\x83\x02\x00\x01t\x06\x00Sn\x01\x00\x01|\x00\x00t\x0b\x00i\x0c\x00@o\x18\x00\x01t\x00\x00i\x01\x00d\x06\x00d\x02\x00\x83\x02\x00\x01t\x06\x00Sn\x01\x00\x01t\x00\x00i\x01\x00d\x07\x00|\x02\x00|\x01\x00f\x02\x00\x16d\x02\x00\x83\x02\x00\x01|\x02\x00|\x01\x00\x18d\x08\x00j\x04\x00o"\x00\x01t\x00\x00i\x01\x00d\t\x00|\x02\x00|\x01\x00f\x02\x00\x16d\x02\x00\x83\x02\x00\x01t\x06\x00Sn\x15\x00\x01t\x00\x00i\x01\x00d\n\x00d\x02\x00\x83\x02\x00\x01t\x0e\x00St\x00\x00i\x01\x00d\x0b\x00d\x02\x00\x83\x02\x00\x01t\x0e\x00Sd\x00\x00S' (29 01 00 00 74 00 00 69 01 00 64 01 00 7C 00 00 7C 01 00 66 02 00 16 64 02 00 83 02 00 01 74 04 00 69 05 00 64 03 00 6A 02 00 6F 1F 00 01 74 00 00 69 01 00 64 04 00 74 04 00 69 05 00 16 64 02 00 83 02 00 01 74 06 00 53 6E 01 00 01 7C 00 00 74 07 00 69 08 00 69 09 00 6A 05 00 6F 2E 00 01 74 00 00 69 01 00 64 05 00 7C 00 00 74 0A 00 74 07 00 69 08 00 69 09 00 83 01 00 66 02 00 16 64 02 00 83 02 00 01 74 06 00 53 6E 01 00 01 7C 00 00 74 0B 00 69 0C 00 40 6F 18 00 01 74 00 00 69 01 00 64 06 00 64 02 00 83 02 00 01 74 06 00 53 6E 01 00 01 74 00 00 69 01 00 64 07 00 7C 02 00 7C 01 00 66 02 00 16 64 02 00 83 02 00 01 7C 02 00 7C 01 00 18 64 08 00 6A 04 00 6F 22 00 01 74 00 00 69 01 00 64 09 00 7C 02 00 7C 01 00 66 02 00 16 64 02 00 83 02 00 01 74 06 00 53 6E 15 00 01 74 00 00 69 01 00 64 0A 00 64 02 00 83 02 00 01 74 0E 00 53 74 00 00 69 01 00 64 0B 00 64 02 00 83 02 00 01 74 0E 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CU'
                             00000003     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000006     64 - LOAD_CONST          'prone flags %d %d'
                             00000009     7C - LOAD_FAST           'flags'
                             0000000C     7C - LOAD_FAST           'roundStarted'
                             0000000F     66 - BUILD_TUPLE         r0002
                             00000012     16 - BINARY_MODULO       
                             00000013     64 - LOAD_CONST          2
                             00000016     83 - CALL_FUNCTION       r0002
                             00000019     01 - POP_TOP             
                             0000001A     74 - LOAD_GLOBAL         'consolevar'
                             0000001D     69 - LOAD_ATTR           'CombatEnableProneAttacks'
                             00000020     64 - LOAD_CONST          0
                             00000023     6A - COMPARE_OP          "=="
                             00000026     6F - JUMP_IF_FALSE       -> 00000048
                             00000029     01 - POP_TOP             
                             0000002A     74 - LOAD_GLOBAL         'CU'
                             0000002D     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000030     64 - LOAD_CONST          'prone attacks not enabled %d'
                             00000033     74 - LOAD_GLOBAL         'consolevar'
                             00000036     69 - LOAD_ATTR           'CombatEnableProneAttacks'
                             00000039     16 - BINARY_MODULO       
                             0000003A     64 - LOAD_CONST          2
                             0000003D     83 - CALL_FUNCTION       r0002
                             00000040     01 - POP_TOP             
                             00000041     74 - LOAD_GLOBAL         'True'
                             00000044     53 - RETURN_VALUE        
                             00000045     6E - JUMP_FORWARD        -> 00000049
                             00000048     01 - POP_TOP             
                             00000049     7C - LOAD_FAST           'flags'
                             0000004C     74 - LOAD_GLOBAL         'constants'
                             0000004F     69 - LOAD_ATTR           'combat_prone'
                             00000052     69 - LOAD_ATTR           'COMBAT_PRONE_MASK'
                             00000055     6A - COMPARE_OP          ">="
                             00000058     6F - JUMP_IF_FALSE       -> 00000089
                             0000005B     01 - POP_TOP             
                             0000005C     74 - LOAD_GLOBAL         'CU'
                             0000005F     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000062     64 - LOAD_CONST          'prone state flags outside of combat controlled %d >= %d'
                             00000065     7C - LOAD_FAST           'flags'
                             00000068     74 - LOAD_GLOBAL         'int'
                             0000006B     74 - LOAD_GLOBAL         'constants'
                             0000006E     69 - LOAD_ATTR           'combat_prone'
                             00000071     69 - LOAD_ATTR           'COMBAT_PRONE_MASK'
                             00000074     83 - CALL_FUNCTION       r0001
                             00000077     66 - BUILD_TUPLE         r0002
                             0000007A     16 - BINARY_MODULO       
                             0000007B     64 - LOAD_CONST          2
                             0000007E     83 - CALL_FUNCTION       r0002
                             00000081     01 - POP_TOP             
                             00000082     74 - LOAD_GLOBAL         'True'
                             00000085     53 - RETURN_VALUE        
                             00000086     6E - JUMP_FORWARD        -> 0000008A
                             00000089     01 - POP_TOP             
                             0000008A     7C - LOAD_FAST           'flags'
                             0000008D     74 - LOAD_GLOBAL         'CD'
                             00000090     69 - LOAD_ATTR           'PRONE_RECOVERY_INSTANT'
                             00000093     40 - BINARY_AND          
                             00000094     6F - JUMP_IF_FALSE       -> 000000AF
                             00000097     01 - POP_TOP             
                             00000098     74 - LOAD_GLOBAL         'CU'
                             0000009B     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000009E     64 - LOAD_CONST          'instant prone recovery called for'
                             000000A1     64 - LOAD_CONST          2
                             000000A4     83 - CALL_FUNCTION       r0002
                             000000A7     01 - POP_TOP             
                             000000A8     74 - LOAD_GLOBAL         'True'
                             000000AB     53 - RETURN_VALUE        
                             000000AC     6E - JUMP_FORWARD        -> 000000B0
                             000000AF     01 - POP_TOP             
                             000000B0     74 - LOAD_GLOBAL         'CU'
                             000000B3     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000B6     64 - LOAD_CONST          'round %d %d'
                             000000B9     7C - LOAD_FAST           'currentRound'
                             000000BC     7C - LOAD_FAST           'roundStarted'
                             000000BF     66 - BUILD_TUPLE         r0002
                             000000C2     16 - BINARY_MODULO       
                             000000C3     64 - LOAD_CONST          2
                             000000C6     83 - CALL_FUNCTION       r0002
                             000000C9     01 - POP_TOP             
                             000000CA     7C - LOAD_FAST           'currentRound'
                             000000CD     7C - LOAD_FAST           'roundStarted'
                             000000D0     18 - BINARY_SUBTRACT     
                             000000D1     64 - LOAD_CONST          1
                             000000D4     6A - COMPARE_OP          ">"
                             000000D7     6F - JUMP_IF_FALSE       -> 000000FC
                             000000DA     01 - POP_TOP             
                             000000DB     74 - LOAD_GLOBAL         'CU'
                             000000DE     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000E1     64 - LOAD_CONST          'prone state expired due to round %d %d'
                             000000E4     7C - LOAD_FAST           'currentRound'
                             000000E7     7C - LOAD_FAST           'roundStarted'
                             000000EA     66 - BUILD_TUPLE         r0002
                             000000ED     16 - BINARY_MODULO       
                             000000EE     64 - LOAD_CONST          2
                             000000F1     83 - CALL_FUNCTION       r0002
                             000000F4     01 - POP_TOP             
                             000000F5     74 - LOAD_GLOBAL         'True'
                             000000F8     53 - RETURN_VALUE        
                             000000F9     6E - JUMP_FORWARD        -> 00000111
                             000000FC     01 - POP_TOP             
                             000000FD     74 - LOAD_GLOBAL         'CU'
                             00000100     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000103     64 - LOAD_CONST          'it is not time for prone recovery'
                             00000106     64 - LOAD_CONST          2
                             00000109     83 - CALL_FUNCTION       r0002
                             0000010C     01 - POP_TOP             
                             0000010D     74 - LOAD_GLOBAL         'False'
                             00000110     53 - RETURN_VALUE        
                             00000111     74 - LOAD_GLOBAL         'CU'
                             00000114     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000117     64 - LOAD_CONST          'Ended prone recovery check ... should not be here'
                             0000011A     64 - LOAD_CONST          2
                             0000011D     83 - CALL_FUNCTION       r0002
                             00000120     01 - POP_TOP             
                             00000121     74 - LOAD_GLOBAL         'False'
                             00000124     53 - RETURN_VALUE        
                             00000125     64 - LOAD_CONST          None
                             00000128     53 - RETURN_VALUE        
                         consts:
00000E6B                     TUPLE: (
00000E70                         None (4E),
00000E71                         STR: 'prone flags %d %d' (11 00 00 00 70 72 6F 6E 65 20 66 6C 61 67 73 20 25 64 20 25 64),
00000E87                         INT: 2 (02 00 00 00),
00000E8C                         INT: 0 (00 00 00 00),
00000E91                         STR: 'prone attacks not enabled %d' (1C 00 00 00 70 72 6F 6E 65 20 61 74 74 61 63 6B 73 20 6E 6F 74 20 65 6E 61 62 6C 65 64 20 25 64),
00000EB2                         STR: 'prone state flags outside of combat controlled %d >= %d' (37 00 00 00 70 72 6F 6E 65 20 73 74 61 74 65 20 66 6C 61 67 73 20 6F 75 74 73 69 64 65 20 6F 66 20 63 6F 6D 62 61 74 20 63 6F 6E 74 72 6F 6C 6C 65 64 20 25 64 20 3E 3D 20 25 64),
00000EEE                         STR: 'instant prone recovery called for' (21 00 00 00 69 6E 73 74 61 6E 74 20 70 72 6F 6E 65 20 72 65 63 6F 76 65 72 79 20 63 61 6C 6C 65 64 20 66 6F 72),
00000F14                         STR: 'round %d %d' (0B 00 00 00 72 6F 75 6E 64 20 25 64 20 25 64),
00000F24                         INT: 1 (01 00 00 00),
00000F29                         STR: 'prone state expired due to round %d %d' (26 00 00 00 70 72 6F 6E 65 20 73 74 61 74 65 20 65 78 70 69 72 65 64 20 64 75 65 20 74 6F 20 72 6F 75 6E 64 20 25 64 20 25 64),
00000F54                         STR: 'it is not time for prone recovery' (21 00 00 00 69 74 20 69 73 20 6E 6F 74 20 74 69 6D 65 20 66 6F 72 20 70 72 6F 6E 65 20 72 65 63 6F 76 65 72 79),
00000F7A                         STR: 'Ended prone recovery check ... should not be here' (31 00 00 00 45 6E 64 65 64 20 70 72 6F 6E 65 20 72 65 63 6F 76 65 72 79 20 63 68 65 63 6B 20 2E 2E 2E 20 73 68 6F 75 6C 64 20 6E 6F 74 20 62 65 20 68 65 72 65)
                             )
                         names:
00000FB0                     TUPLE: (
00000FB5                         STR: 'CU' (02 00 00 00 43 55),
00000FBC                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
00000FD9                         STR: 'flags' (05 00 00 00 66 6C 61 67 73),
00000FE3                         STR: 'roundStarted' (0C 00 00 00 72 6F 75 6E 64 53 74 61 72 74 65 64),
00000FF4                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
00001003                         STR: 'CombatEnableProneAttacks' (18 00 00 00 43 6F 6D 62 61 74 45 6E 61 62 6C 65 50 72 6F 6E 65 41 74 74 61 63 6B 73),
00001020                         STR: 'True' (04 00 00 00 54 72 75 65),
00001029                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00001037                         STR: 'combat_prone' (0C 00 00 00 63 6F 6D 62 61 74 5F 70 72 6F 6E 65),
00001048                         STR: 'COMBAT_PRONE_MASK' (11 00 00 00 43 4F 4D 42 41 54 5F 50 52 4F 4E 45 5F 4D 41 53 4B),
0000105E                         STR: 'int' (03 00 00 00 69 6E 74),
00001066                         STR: 'CD' (02 00 00 00 43 44),
0000106D                         STR: 'PRONE_RECOVERY_INSTANT' (16 00 00 00 50 52 4F 4E 45 5F 52 45 43 4F 56 45 52 59 5F 49 4E 53 54 41 4E 54),
00001088                         STR: 'currentRound' (0C 00 00 00 63 75 72 72 65 6E 74 52 6F 75 6E 64),
00001099                         STR: 'False' (05 00 00 00 46 61 6C 73 65)
                             )
                         varnames:
000010A3                     TUPLE: (
000010A8                         STR: 'flags' (05 00 00 00 66 6C 61 67 73),
000010B2                         STR: 'roundStarted' (0C 00 00 00 72 6F 75 6E 64 53 74 61 72 74 65 64),
000010C3                         STR: 'currentRound' (0C 00 00 00 63 75 72 72 65 6E 74 52 6F 75 6E 64)
                             )
                         freevars:
000010D4                     TUPLE: ()
                         cellvars:
000010D9                     TUPLE: ()
                         filename:
000010DE                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat.py' (3E 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 2E 70 79)
                         name:
00001121                     STR: 'HasProneStateExpired' (14 00 00 00 48 61 73 50 72 6F 6E 65 53 74 61 74 65 45 78 70 69 72 65 64)
                         firslineno:
0000113A                     LONG: 106L (6A 00 00 00)
                         lnotab:
0000113E                     STR: '\x00\x01\x1a\x03\x10\x01\x17\x01\x08\x03\x13\x01&\x01\x08\x02\x0e\x01\x10\x01\x08\x02\x1a\x02\x11\x01\x1a\x01\x08\x02\x10\x01\x04\x02\x10\x01' (24 00 00 00 00 01 1A 03 10 01 17 01 08 03 13 01 26 01 08 02 0E 01 10 01 08 02 1A 02 11 01 1A 01 08 02 10 01 04 02 10 01),
00001167             CODE:
                         argcount:
00001168                     LONG: 3L (03 00 00 00)
                         nlocals:
0000116C                     LONG: 3L (03 00 00 00)
                         stacksize:
00001170                     LONG: 4L (04 00 00 00)
                         flags:
00001174                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001178                     STR: "|\x00\x00i\x01\x00t\x02\x00i\x03\x00i\x04\x00j\x03\x00o'\x00\x01t\x05\x00i\x06\x00d\x01\x00d\x02\x00\x83\x02\x00\x01t\x07\x00i\x08\x00|\x00\x00|\x01\x00|\x02\x00\x83\x03\x00Sn8\x00\x01t\x0b\x00i\x0c\x00d\x03\x00j\x03\x00o'\x00\x01t\x05\x00i\x06\x00d\x04\x00d\x02\x00\x83\x02\x00\x01t\x07\x00i\r\x00|\x00\x00|\x01\x00|\x02\x00\x83\x03\x00Sn\x01\x00\x01t\x0e\x00Sd\x00\x00S" (7C 00 00 00 7C 00 00 69 01 00 74 02 00 69 03 00 69 04 00 6A 03 00 6F 27 00 01 74 05 00 69 06 00 64 01 00 64 02 00 83 02 00 01 74 07 00 69 08 00 7C 00 00 7C 01 00 7C 02 00 83 03 00 53 6E 38 00 01 74 0B 00 69 0C 00 64 03 00 6A 03 00 6F 27 00 01 74 05 00 69 06 00 64 04 00 64 02 00 83 02 00 01 74 07 00 69 0D 00 7C 00 00 7C 01 00 7C 02 00 83 03 00 53 6E 01 00 01 74 0E 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'attacker'
                             00000003     69 - LOAD_ATTR           'itemType'
                             00000006     74 - LOAD_GLOBAL         'constants'
                             00000009     69 - LOAD_ATTR           'combat'
                             0000000C     69 - LOAD_ATTR           'INVALID_WEAPON'
                             0000000F     6A - COMPARE_OP          "!="
                             00000012     6F - JUMP_IF_FALSE       -> 0000003C
                             00000015     01 - POP_TOP             
                             00000016     74 - LOAD_GLOBAL         'CU'
                             00000019     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000001C     64 - LOAD_CONST          'weapon free attack'
                             0000001F     64 - LOAD_CONST          2
                             00000022     83 - CALL_FUNCTION       r0002
                             00000025     01 - POP_TOP             
                             00000026     74 - LOAD_GLOBAL         'CombatFA'
                             00000029     69 - LOAD_ATTR           'PerformWeaponFreeAttack'
                             0000002C     7C - LOAD_FAST           'attacker'
                             0000002F     7C - LOAD_FAST           'defender'
                             00000032     7C - LOAD_FAST           'result'
                             00000035     83 - CALL_FUNCTION       r0003
                             00000038     53 - RETURN_VALUE        
                             00000039     6E - JUMP_FORWARD        -> 00000074
                             0000003C     01 - POP_TOP             
                             0000003D     74 - LOAD_GLOBAL         'consolevar'
                             00000040     69 - LOAD_ATTR           'MeleeFreeFire'
                             00000043     64 - LOAD_CONST          0
                             00000046     6A - COMPARE_OP          "!="
                             00000049     6F - JUMP_IF_FALSE       -> 00000073
                             0000004C     01 - POP_TOP             
                             0000004D     74 - LOAD_GLOBAL         'CU'
                             00000050     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000053     64 - LOAD_CONST          'melee free attack'
                             00000056     64 - LOAD_CONST          2
                             00000059     83 - CALL_FUNCTION       r0002
                             0000005C     01 - POP_TOP             
                             0000005D     74 - LOAD_GLOBAL         'CombatFA'
                             00000060     69 - LOAD_ATTR           'PerformMeleeFreeAttack'
                             00000063     7C - LOAD_FAST           'attacker'
                             00000066     7C - LOAD_FAST           'defender'
                             00000069     7C - LOAD_FAST           'result'
                             0000006C     83 - CALL_FUNCTION       r0003
                             0000006F     53 - RETURN_VALUE        
                             00000070     6E - JUMP_FORWARD        -> 00000074
                             00000073     01 - POP_TOP             
                             00000074     74 - LOAD_GLOBAL         'False'
                             00000077     53 - RETURN_VALUE        
                             00000078     64 - LOAD_CONST          None
                             0000007B     53 - RETURN_VALUE        
                         consts:
000011F9                     TUPLE: (
000011FE                         None (4E),
000011FF                         STR: 'weapon free attack' (12 00 00 00 77 65 61 70 6F 6E 20 66 72 65 65 20 61 74 74 61 63 6B),
00001216                         INT: 2 (02 00 00 00),
0000121B                         INT: 0 (00 00 00 00),
00001220                         STR: 'melee free attack' (11 00 00 00 6D 65 6C 65 65 20 66 72 65 65 20 61 74 74 61 63 6B)
                             )
                         names:
00001236                     TUPLE: (
0000123B                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
00001248                         STR: 'itemType' (08 00 00 00 69 74 65 6D 54 79 70 65),
00001255                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00001263                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
0000126E                         STR: 'INVALID_WEAPON' (0E 00 00 00 49 4E 56 41 4C 49 44 5F 57 45 41 50 4F 4E),
00001281                         STR: 'CU' (02 00 00 00 43 55),
00001288                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
000012A5                         STR: 'CombatFA' (08 00 00 00 43 6F 6D 62 61 74 46 41),
000012B2                         STR: 'PerformWeaponFreeAttack' (17 00 00 00 50 65 72 66 6F 72 6D 57 65 61 70 6F 6E 46 72 65 65 41 74 74 61 63 6B),
000012CE                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
000012DB                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
000012E6                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
000012F5                         STR: 'MeleeFreeFire' (0D 00 00 00 4D 65 6C 65 65 46 72 65 65 46 69 72 65),
00001307                         STR: 'PerformMeleeFreeAttack' (16 00 00 00 50 65 72 66 6F 72 6D 4D 65 6C 65 65 46 72 65 65 41 74 74 61 63 6B),
00001322                         STR: 'False' (05 00 00 00 46 61 6C 73 65)
                             )
                         varnames:
0000132C                     TUPLE: (
00001331                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
0000133E                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
0000134B                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74)
                             )
                         freevars:
00001356                     TUPLE: ()
                         cellvars:
0000135B                     TUPLE: ()
                         filename:
00001360                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat.py' (3E 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 2E 70 79)
                         name:
000013A3                     STR: 'PerformFreeAttack' (11 00 00 00 50 65 72 66 6F 72 6D 46 72 65 65 41 74 74 61 63 6B)
                         firslineno:
000013B9                     LONG: 136L (88 00 00 00)
                         lnotab:
000013BD                     STR: '\x00\x06\x16\x02\x10\x01\x17\x02\x10\x01\x10\x01\x17\x05' (0E 00 00 00 00 06 16 02 10 01 17 02 10 01 10 01 17 05),
000013D0             CODE:
                         argcount:
000013D1                     LONG: 3L (03 00 00 00)
                         nlocals:
000013D5                     LONG: 7L (07 00 00 00)
                         stacksize:
000013D9                     LONG: 5L (05 00 00 00)
                         flags:
000013DD                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000013E1                     STR: 't\x00\x00i\x01\x00d\x01\x00d\x02\x00\x83\x02\x00\x01t\x02\x00i\x03\x00|\x00\x00|\x01\x00|\x02\x00i\x07\x00\x83\x03\x00}\x04\x00|\x04\x00|\x00\x00j\x08\x00o\n\x00\x01|\x01\x00}\x05\x00n\x07\x00\x01|\x00\x00}\x05\x00t\x00\x00i\x01\x00d\x03\x00|\x00\x00i\n\x00|\x01\x00i\n\x00f\x02\x00\x16d\x02\x00\x83\x02\x00\x01t\x02\x00i\x0b\x00|\x04\x00|\x05\x00|\x02\x00\x83\x03\x00\\\x02\x00}\x06\x00}\x03\x00|\x06\x00t\x0e\x00j\x02\x00o\n\x00\x01|\x03\x00t\x0f\x00j\x02\x00o\x18\x00\x01t\x00\x00i\x01\x00d\x04\x00d\x02\x00\x83\x02\x00\x01d\x00\x00Sn\x01\x00\x01t\x02\x00i\x10\x00|\x04\x00|\x05\x00|\x03\x00|\x02\x00\x83\x04\x00\x01t\x00\x00i\x01\x00d\x05\x00d\x02\x00\x83\x02\x00\x01d\x00\x00S' (DC 00 00 00 74 00 00 69 01 00 64 01 00 64 02 00 83 02 00 01 74 02 00 69 03 00 7C 00 00 7C 01 00 7C 02 00 69 07 00 83 03 00 7D 04 00 7C 04 00 7C 00 00 6A 08 00 6F 0A 00 01 7C 01 00 7D 05 00 6E 07 00 01 7C 00 00 7D 05 00 74 00 00 69 01 00 64 03 00 7C 00 00 69 0A 00 7C 01 00 69 0A 00 66 02 00 16 64 02 00 83 02 00 01 74 02 00 69 0B 00 7C 04 00 7C 05 00 7C 02 00 83 03 00 5C 02 00 7D 06 00 7D 03 00 7C 06 00 74 0E 00 6A 02 00 6F 0A 00 01 7C 03 00 74 0F 00 6A 02 00 6F 18 00 01 74 00 00 69 01 00 64 04 00 64 02 00 83 02 00 01 64 00 00 53 6E 01 00 01 74 02 00 69 10 00 7C 04 00 7C 05 00 7C 03 00 7C 02 00 83 04 00 01 74 00 00 69 01 00 64 05 00 64 02 00 83 02 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CU'
                             00000003     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000006     64 - LOAD_CONST          '\n\n\n--start new combat resolution--'
                             00000009     64 - LOAD_CONST          3
                             0000000C     83 - CALL_FUNCTION       r0002
                             0000000F     01 - POP_TOP             
                             00000010     74 - LOAD_GLOBAL         'CombatRes'
                             00000013     69 - LOAD_ATTR           'determineAttacker'
                             00000016     7C - LOAD_FAST           'player1'
                             00000019     7C - LOAD_FAST           'player2'
                             0000001C     7C - LOAD_FAST           'result'
                             0000001F     69 - LOAD_ATTR           'distance'
                             00000022     83 - CALL_FUNCTION       r0003
                             00000025     7D - STORE_FAST          'attacker'
                             00000028     7C - LOAD_FAST           'attacker'
                             0000002B     7C - LOAD_FAST           'player1'
                             0000002E     6A - COMPARE_OP          "is"
                             00000031     6F - JUMP_IF_FALSE       -> 0000003E
                             00000034     01 - POP_TOP             
                             00000035     7C - LOAD_FAST           'player2'
                             00000038     7D - STORE_FAST          'defender'
                             0000003B     6E - JUMP_FORWARD        -> 00000045
                             0000003E     01 - POP_TOP             
                             0000003F     7C - LOAD_FAST           'player1'
                             00000042     7D - STORE_FAST          'defender'
                             00000045     74 - LOAD_GLOBAL         'CU'
                             00000048     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000004B     64 - LOAD_CONST          'attacker: %d defender: %d'
                             0000004E     7C - LOAD_FAST           'player1'
                             00000051     69 - LOAD_ATTR           'slot'
                             00000054     7C - LOAD_FAST           'player2'
                             00000057     69 - LOAD_ATTR           'slot'
                             0000005A     66 - BUILD_TUPLE         r0002
                             0000005D     16 - BINARY_MODULO       
                             0000005E     64 - LOAD_CONST          3
                             00000061     83 - CALL_FUNCTION       r0002
                             00000064     01 - POP_TOP             
                             00000065     74 - LOAD_GLOBAL         'CombatRes'
                             00000068     69 - LOAD_ATTR           'determineResultOfWithdrawalRequest'
                             0000006B     7C - LOAD_FAST           'attacker'
                             0000006E     7C - LOAD_FAST           'defender'
                             00000071     7C - LOAD_FAST           'result'
                             00000074     83 - CALL_FUNCTION       r0003
                             00000077     5C - UNPACK_SEQUENCE     r0002
                             0000007A     7D - STORE_FAST          'withdraw_processed'
                             0000007D     7D - STORE_FAST          'failed_to_withdraw'
                             00000080     7C - LOAD_FAST           'withdraw_processed'
                             00000083     74 - LOAD_GLOBAL         'True'
                             00000086     6A - COMPARE_OP          "=="
                             00000089     6F - JUMP_IF_FALSE       -> 00000096
                             0000008C     01 - POP_TOP             
                             0000008D     7C - LOAD_FAST           'failed_to_withdraw'
                             00000090     74 - LOAD_GLOBAL         'False'
                             00000093     6A - COMPARE_OP          "=="
                             00000096     6F - JUMP_IF_FALSE       -> 000000B1
                             00000099     01 - POP_TOP             
                             0000009A     74 - LOAD_GLOBAL         'CU'
                             0000009D     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000A0     64 - LOAD_CONST          'successfully withdrew ---\n\n'
                             000000A3     64 - LOAD_CONST          3
                             000000A6     83 - CALL_FUNCTION       r0002
                             000000A9     01 - POP_TOP             
                             000000AA     64 - LOAD_CONST          None
                             000000AD     53 - RETURN_VALUE        
                             000000AE     6E - JUMP_FORWARD        -> 000000B2
                             000000B1     01 - POP_TOP             
                             000000B2     74 - LOAD_GLOBAL         'CombatRes'
                             000000B5     69 - LOAD_ATTR           'determineResultForStandardCombat'
                             000000B8     7C - LOAD_FAST           'attacker'
                             000000BB     7C - LOAD_FAST           'defender'
                             000000BE     7C - LOAD_FAST           'failed_to_withdraw'
                             000000C1     7C - LOAD_FAST           'result'
                             000000C4     83 - CALL_FUNCTION       r0004
                             000000C7     01 - POP_TOP             
                             000000C8     74 - LOAD_GLOBAL         'CU'
                             000000CB     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000CE     64 - LOAD_CONST          'end new combat resolution ---'
                             000000D1     64 - LOAD_CONST          3
                             000000D4     83 - CALL_FUNCTION       r0002
                             000000D7     01 - POP_TOP             
                             000000D8     64 - LOAD_CONST          None
                             000000DB     53 - RETURN_VALUE        
                         consts:
000014C2                     TUPLE: (
000014C7                         None (4E),
000014C8                         STR: '\n\n\n--start new combat resolution--' (22 00 00 00 0A 0A 0A 2D 2D 73 74 61 72 74 20 6E 65 77 20 63 6F 6D 62 61 74 20 72 65 73 6F 6C 75 74 69 6F 6E 2D 2D),
000014EF                         INT: 3 (03 00 00 00),
000014F4                         STR: 'attacker: %d defender: %d' (19 00 00 00 61 74 74 61 63 6B 65 72 3A 20 25 64 20 64 65 66 65 6E 64 65 72 3A 20 25 64),
00001512                         STR: 'successfully withdrew ---\n\n' (1B 00 00 00 73 75 63 63 65 73 73 66 75 6C 6C 79 20 77 69 74 68 64 72 65 77 20 2D 2D 2D 0A 0A),
00001532                         STR: 'end new combat resolution ---' (1D 00 00 00 65 6E 64 20 6E 65 77 20 63 6F 6D 62 61 74 20 72 65 73 6F 6C 75 74 69 6F 6E 20 2D 2D 2D)
                             )
                         names:
00001554                     TUPLE: (
00001559                         STR: 'CU' (02 00 00 00 43 55),
00001560                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
0000157D                         STR: 'CombatRes' (09 00 00 00 43 6F 6D 62 61 74 52 65 73),
0000158B                         STR: 'determineAttacker' (11 00 00 00 64 65 74 65 72 6D 69 6E 65 41 74 74 61 63 6B 65 72),
000015A1                         STR: 'player1' (07 00 00 00 70 6C 61 79 65 72 31),
000015AD                         STR: 'player2' (07 00 00 00 70 6C 61 79 65 72 32),
000015B9                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
000015C4                         STR: 'distance' (08 00 00 00 64 69 73 74 61 6E 63 65),
000015D1                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
000015DE                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
000015EB                         STR: 'slot' (04 00 00 00 73 6C 6F 74),
000015F4                         STR: 'determineResultOfWithdrawalRequest' (22 00 00 00 64 65 74 65 72 6D 69 6E 65 52 65 73 75 6C 74 4F 66 57 69 74 68 64 72 61 77 61 6C 52 65 71 75 65 73 74),
0000161B                         STR: 'withdraw_processed' (12 00 00 00 77 69 74 68 64 72 61 77 5F 70 72 6F 63 65 73 73 65 64),
00001632                         STR: 'failed_to_withdraw' (12 00 00 00 66 61 69 6C 65 64 5F 74 6F 5F 77 69 74 68 64 72 61 77),
00001649                         STR: 'True' (04 00 00 00 54 72 75 65),
00001652                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
0000165C                         STR: 'determineResultForStandardCombat' (20 00 00 00 64 65 74 65 72 6D 69 6E 65 52 65 73 75 6C 74 46 6F 72 53 74 61 6E 64 61 72 64 43 6F 6D 62 61 74)
                             )
                         varnames:
00001681                     TUPLE: (
00001686                         STR: 'player1' (07 00 00 00 70 6C 61 79 65 72 31),
00001692                         STR: 'player2' (07 00 00 00 70 6C 61 79 65 72 32),
0000169E                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
000016A9                         STR: 'failed_to_withdraw' (12 00 00 00 66 61 69 6C 65 64 5F 74 6F 5F 77 69 74 68 64 72 61 77),
000016C0                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
000016CD                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
000016DA                         STR: 'withdraw_processed' (12 00 00 00 77 69 74 68 64 72 61 77 5F 70 72 6F 63 65 73 73 65 64)
                             )
                         freevars:
000016F1                     TUPLE: ()
                         cellvars:
000016F6                     TUPLE: ()
                         filename:
000016FB                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat.py' (3E 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 2E 70 79)
                         name:
0000173E                     STR: 'ResolveCombat' (0D 00 00 00 52 65 73 6F 6C 76 65 43 6F 6D 62 61 74)
                         firslineno:
00001750                     LONG: 165L (A5 00 00 00)
                         lnotab:
00001754                     STR: '\x00\x01\x10\x03\x18\x02\r\x01\n\x02\x06\x02 \x03\x1b\x01\x1a\x02\x10\x01\x08\x03\x16\x01' (18 00 00 00 00 01 10 03 18 02 0D 01 0A 02 06 02 20 03 1B 01 1A 02 10 01 08 03 16 01)
                 )
             names:
00001771         TUPLE: (
00001776             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00001781             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
0000178F             STR: 'obj' (03 00 00 00 6F 62 6A),
00001797             STR: 'combat_defines' (0E 00 00 00 63 6F 6D 62 61 74 5F 64 65 66 69 6E 65 73),
000017AA             STR: 'CD' (02 00 00 00 43 44),
000017B1             STR: 'math' (04 00 00 00 6D 61 74 68),
000017BA             STR: 'interlock.combat_abil_level' (1B 00 00 00 69 6E 74 65 72 6C 6F 63 6B 2E 63 6F 6D 62 61 74 5F 61 62 69 6C 5F 6C 65 76 65 6C),
000017DA             STR: 'combat_abil_level' (11 00 00 00 63 6F 6D 62 61 74 5F 61 62 69 6C 5F 6C 65 76 65 6C),
000017F0             STR: 'CombatAbilLevel' (0F 00 00 00 43 6F 6D 62 61 74 41 62 69 6C 4C 65 76 65 6C),
00001804             STR: 'interlock.combat_modifiers' (1A 00 00 00 69 6E 74 65 72 6C 6F 63 6B 2E 63 6F 6D 62 61 74 5F 6D 6F 64 69 66 69 65 72 73),
00001823             STR: 'combat_modifiers' (10 00 00 00 63 6F 6D 62 61 74 5F 6D 6F 64 69 66 69 65 72 73),
00001838             STR: 'CombatMods' (0A 00 00 00 43 6F 6D 62 61 74 4D 6F 64 73),
00001847             STR: 'interlock.combat_innerstrength' (1E 00 00 00 69 6E 74 65 72 6C 6F 63 6B 2E 63 6F 6D 62 61 74 5F 69 6E 6E 65 72 73 74 72 65 6E 67 74 68),
0000186A             STR: 'combat_innerstrength' (14 00 00 00 63 6F 6D 62 61 74 5F 69 6E 6E 65 72 73 74 72 65 6E 67 74 68),
00001883             STR: 'CombatIS' (08 00 00 00 43 6F 6D 62 61 74 49 53),
00001890             STR: 'interlock.combat_resolution' (1B 00 00 00 69 6E 74 65 72 6C 6F 63 6B 2E 63 6F 6D 62 61 74 5F 72 65 73 6F 6C 75 74 69 6F 6E),
000018B0             STR: 'combat_resolution' (11 00 00 00 63 6F 6D 62 61 74 5F 72 65 73 6F 6C 75 74 69 6F 6E),
000018C6             STR: 'CombatRes' (09 00 00 00 43 6F 6D 62 61 74 52 65 73),
000018D4             STR: 'interlock.combat_utility' (18 00 00 00 69 6E 74 65 72 6C 6F 63 6B 2E 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79),
000018F1             STR: 'combat_utility' (0E 00 00 00 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79),
00001904             STR: 'CU' (02 00 00 00 43 55),
0000190B             STR: 'interlock.combat_free_attacks' (1D 00 00 00 69 6E 74 65 72 6C 6F 63 6B 2E 63 6F 6D 62 61 74 5F 66 72 65 65 5F 61 74 74 61 63 6B 73),
0000192D             STR: 'combat_free_attacks' (13 00 00 00 63 6F 6D 62 61 74 5F 66 72 65 65 5F 61 74 74 61 63 6B 73),
00001945             STR: 'CombatFA' (08 00 00 00 43 6F 6D 62 61 74 46 41),
00001952             STR: 'combat_calculations' (13 00 00 00 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73),
0000196A             STR: 'SetCombatTargetSettings' (17 00 00 00 53 65 74 43 6F 6D 62 61 74 54 61 72 67 65 74 53 65 74 74 69 6E 67 73),
00001986             STR: 'SetFreeAttackAbility' (14 00 00 00 53 65 74 46 72 65 65 41 74 74 61 63 6B 41 62 69 6C 69 74 79),
0000199F             STR: 'IsATactic' (09 00 00 00 49 73 41 54 61 63 74 69 63),
000019AD             STR: 'GetTacticalPointsGained' (17 00 00 00 47 65 74 54 61 63 74 69 63 61 6C 50 6F 69 6E 74 73 47 61 69 6E 65 64),
000019C9             STR: 'GetInnerStrengthUsed' (14 00 00 00 47 65 74 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 55 73 65 64),
000019E2             STR: 'DoProneStatesMatch' (12 00 00 00 44 6F 50 72 6F 6E 65 53 74 61 74 65 73 4D 61 74 63 68),
000019F9             STR: 'DetermineDominantProneType' (1A 00 00 00 44 65 74 65 72 6D 69 6E 65 44 6F 6D 69 6E 61 6E 74 50 72 6F 6E 65 54 79 70 65),
00001A18             STR: 'HasProneStateExpired' (14 00 00 00 48 61 73 50 72 6F 6E 65 53 74 61 74 65 45 78 70 69 72 65 64),
00001A31             STR: 'PerformFreeAttack' (11 00 00 00 50 65 72 66 6F 72 6D 46 72 65 65 41 74 74 61 63 6B),
00001A47             STR: 'ResolveCombat' (0D 00 00 00 52 65 73 6F 6C 76 65 43 6F 6D 62 61 74)
                 )
             varnames:
00001A59         TUPLE: (
00001A5E             STR: 'CombatAbilLevel' (0F 00 00 00 43 6F 6D 62 61 74 41 62 69 6C 4C 65 76 65 6C),
00001A72             STR: 'SetFreeAttackAbility' (14 00 00 00 53 65 74 46 72 65 65 41 74 74 61 63 6B 41 62 69 6C 69 74 79),
00001A8B             STR: 'PerformFreeAttack' (11 00 00 00 50 65 72 66 6F 72 6D 46 72 65 65 41 74 74 61 63 6B),
00001AA1             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00001AAC             STR: 'DetermineDominantProneType' (1A 00 00 00 44 65 74 65 72 6D 69 6E 65 44 6F 6D 69 6E 61 6E 74 50 72 6F 6E 65 54 79 70 65),
00001ACB             STR: 'DoProneStatesMatch' (12 00 00 00 44 6F 50 72 6F 6E 65 53 74 61 74 65 73 4D 61 74 63 68),
00001AE2             STR: 'CombatMods' (0A 00 00 00 43 6F 6D 62 61 74 4D 6F 64 73),
00001AF1             STR: 'combat_calculations' (13 00 00 00 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73),
00001B09             STR: 'HasProneStateExpired' (14 00 00 00 48 61 73 50 72 6F 6E 65 53 74 61 74 65 45 78 70 69 72 65 64),
00001B22             STR: 'CombatFA' (08 00 00 00 43 6F 6D 62 61 74 46 41),
00001B2F             STR: 'math' (04 00 00 00 6D 61 74 68),
00001B38             STR: 'GetTacticalPointsGained' (17 00 00 00 47 65 74 54 61 63 74 69 63 61 6C 50 6F 69 6E 74 73 47 61 69 6E 65 64),
00001B54             STR: 'SetCombatTargetSettings' (17 00 00 00 53 65 74 43 6F 6D 62 61 74 54 61 72 67 65 74 53 65 74 74 69 6E 67 73),
00001B70             STR: 'CD' (02 00 00 00 43 44),
00001B77             STR: 'IsATactic' (09 00 00 00 49 73 41 54 61 63 74 69 63),
00001B85             STR: 'CU' (02 00 00 00 43 55),
00001B8C             STR: 'CombatIS' (08 00 00 00 43 6F 6D 62 61 74 49 53),
00001B99             STR: 'ResolveCombat' (0D 00 00 00 52 65 73 6F 6C 76 65 43 6F 6D 62 61 74),
00001BAB             STR: 'CombatRes' (09 00 00 00 43 6F 6D 62 61 74 52 65 73),
00001BB9             STR: 'obj' (03 00 00 00 6F 62 6A),
00001BC1             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00001BCF             STR: 'GetInnerStrengthUsed' (14 00 00 00 47 65 74 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 55 73 65 64)
                 )
             freevars:
00001BE8         TUPLE: ()
             cellvars:
00001BED         TUPLE: ()
             filename:
00001BF2         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat.py' (3E 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 2E 70 79)
             name:
00001C35         STR: '?' (01 00 00 00 3F)
             firslineno:
00001C3B         LONG: 1L (01 00 00 00)
             lnotab:
00001C3F         STR: '\t\x01\t\x01\t\x01\t\x01\t\x01\x0c\x01\x0c\x01\x0c\x01\x0c\x01\x0c\x01\x0c\x01\t\x03\t\x03\t\x03\t\x06\t\x0e\t\x1b\t\x0c\t\x1a\t\x1e\t\x1d' (2A 00 00 00 09 01 09 01 09 01 09 01 09 01 0C 01 0C 01 0C 01 0C 01 0C 01 0C 01 09 03 09 03 09 03 09 06 09 0E 09 1B 09 0C 09 1A 09 1E 09 1D)

