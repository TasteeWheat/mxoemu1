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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00Z\x02\x00d\x00\x00k\x03\x00Z\x04\x00d\x00\x00k\x05\x00Z\x05\x00d\x00\x00k\x06\x00i\x07\x00Z\x08\x00d\x01\x00\x84\x00\x00Z\t\x00d\x02\x00\x84\x00\x00Z\n\x00d\x03\x00\x84\x00\x00Z\x0b\x00d\x04\x00\x84\x00\x00Z\x0c\x00d\x05\x00\x84\x00\x00Z\r\x00d\x06\x00\x84\x00\x00Z\x0e\x00d\x07\x00\x84\x00\x00Z\x0f\x00d\x08\x00d\t\x00\x84\x01\x00Z\x10\x00d\n\x00\x84\x00\x00Z\x11\x00d\x0b\x00\x84\x00\x00Z\x12\x00d\x0c\x00\x84\x00\x00Z\x13\x00d\r\x00\x84\x00\x00Z\x14\x00d\x0e\x00\x84\x00\x00Z\x15\x00d\x0f\x00\x84\x00\x00Z\x16\x00d\x10\x00\x84\x00\x00Z\x17\x00d\x11\x00\x84\x00\x00Z\x18\x00d\x00\x00S' (D0 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 5A 02 00 64 00 00 6B 03 00 5A 04 00 64 00 00 6B 05 00 5A 05 00 64 00 00 6B 06 00 69 07 00 5A 08 00 64 01 00 84 00 00 5A 09 00 64 02 00 84 00 00 5A 0A 00 64 03 00 84 00 00 5A 0B 00 64 04 00 84 00 00 5A 0C 00 64 05 00 84 00 00 5A 0D 00 64 06 00 84 00 00 5A 0E 00 64 07 00 84 00 00 5A 0F 00 64 08 00 64 09 00 84 01 00 5A 10 00 64 0A 00 84 00 00 5A 11 00 64 0B 00 84 00 00 5A 12 00 64 0C 00 84 00 00 5A 13 00 64 0D 00 84 00 00 5A 14 00 64 0E 00 84 00 00 5A 15 00 64 0F 00 84 00 00 5A 16 00 64 10 00 84 00 00 5A 17 00 64 11 00 84 00 00 5A 18 00 64 00 00 53)
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
                 00000030     6B - IMPORT_NAME         'interlock.combat_utility'
                 00000033     69 - LOAD_ATTR           'combat_utility'
                 00000036     5A - STORE_NAME          'CU'
                 00000039     64 - LOAD_CONST          CODE('calcDamageWithGun')
                 0000003C     84 - MAKE_FUNCTION       r0000
                 0000003F     5A - STORE_NAME          'calcDamageWithGun'
                 00000042     64 - LOAD_CONST          CODE('GetTacticCombatTacticsMod')
                 00000045     84 - MAKE_FUNCTION       r0000
                 00000048     5A - STORE_NAME          'GetTacticCombatTacticsMod'
                 0000004B     64 - LOAD_CONST          CODE('GetTacticDefenseTacticsMod')
                 0000004E     84 - MAKE_FUNCTION       r0000
                 00000051     5A - STORE_NAME          'GetTacticDefenseTacticsMod'
                 00000054     64 - LOAD_CONST          CODE('GetTacticDamageMod')
                 00000057     84 - MAKE_FUNCTION       r0000
                 0000005A     5A - STORE_NAME          'GetTacticDamageMod'
                 0000005D     64 - LOAD_CONST          CODE('GetTacticWithdrawTacticsMod')
                 00000060     84 - MAKE_FUNCTION       r0000
                 00000063     5A - STORE_NAME          'GetTacticWithdrawTacticsMod'
                 00000066     64 - LOAD_CONST          CODE('GetFreeAttackDamage')
                 00000069     84 - MAKE_FUNCTION       r0000
                 0000006C     5A - STORE_NAME          'GetFreeAttackDamage'
                 0000006F     64 - LOAD_CONST          CODE('GetFreeAttackDamageMelee')
                 00000072     84 - MAKE_FUNCTION       r0000
                 00000075     5A - STORE_NAME          'GetFreeAttackDamageMelee'
                 00000078     64 - LOAD_CONST          1
                 0000007B     64 - LOAD_CONST          CODE('GetCloseCombatDamage')
                 0000007E     84 - MAKE_FUNCTION       r0001
                 00000081     5A - STORE_NAME          'GetCloseCombatDamage'
                 00000084     64 - LOAD_CONST          CODE('GetCombatTacticRoll')
                 00000087     84 - MAKE_FUNCTION       r0000
                 0000008A     5A - STORE_NAME          'GetCombatTacticRoll'
                 0000008D     64 - LOAD_CONST          CODE('GetDefenseTacticRoll')
                 00000090     84 - MAKE_FUNCTION       r0000
                 00000093     5A - STORE_NAME          'GetDefenseTacticRoll'
                 00000096     64 - LOAD_CONST          CODE('GetDamageReductionValue')
                 00000099     84 - MAKE_FUNCTION       r0000
                 0000009C     5A - STORE_NAME          'GetDamageReductionValue'
                 0000009F     64 - LOAD_CONST          CODE('GetShieldDamageValue')
                 000000A2     84 - MAKE_FUNCTION       r0000
                 000000A5     5A - STORE_NAME          'GetShieldDamageValue'
                 000000A8     64 - LOAD_CONST          CODE('GetShieldResistanceISDrainValue')
                 000000AB     84 - MAKE_FUNCTION       r0000
                 000000AE     5A - STORE_NAME          'GetShieldResistanceISDrainValue'
                 000000B1     64 - LOAD_CONST          CODE('DamageInterruptsCasting')
                 000000B4     84 - MAKE_FUNCTION       r0000
                 000000B7     5A - STORE_NAME          'DamageInterruptsCasting'
                 000000BA     64 - LOAD_CONST          CODE('GetFullAbilityDamage')
                 000000BD     84 - MAKE_FUNCTION       r0000
                 000000C0     5A - STORE_NAME          'GetFullAbilityDamage'
                 000000C3     64 - LOAD_CONST          CODE('GetAbilityMitigationDuration')
                 000000C6     84 - MAKE_FUNCTION       r0000
                 000000C9     5A - STORE_NAME          'GetAbilityMitigationDuration'
                 000000CC     64 - LOAD_CONST          None
                 000000CF     53 - RETURN_VALUE        
             consts:
000000EE         TUPLE: (
000000F3             None (4E),
000000F4             CODE:
                         argcount:
000000F5                     LONG: 3L (03 00 00 00)
                         nlocals:
000000F9                     LONG: 5L (05 00 00 00)
                         stacksize:
000000FD                     LONG: 4L (04 00 00 00)
                         flags:
00000101                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000105                     STR: 't\x00\x00i\x01\x00d\x01\x00d\x02\x00|\x01\x00f\x02\x00\x16d\x03\x00\x83\x02\x00\x01d\x02\x00}\x03\x00|\x01\x00d\x02\x00j\x04\x00o\x1e\x00\x01t\x04\x00i\x05\x00d\x02\x00|\x01\x00d\x03\x00\x14\x83\x02\x00|\x01\x00\x18}\x03\x00n\x01\x00\x01d\x02\x00}\x04\x00|\x00\x00|\x03\x00\x17|\x04\x00\x17Sd\x00\x00S' (61 00 00 00 74 00 00 69 01 00 64 01 00 64 02 00 7C 01 00 66 02 00 16 64 03 00 83 02 00 01 64 02 00 7D 03 00 7C 01 00 64 02 00 6A 04 00 6F 1E 00 01 74 04 00 69 05 00 64 02 00 7C 01 00 64 03 00 14 83 02 00 7C 01 00 18 7D 03 00 6E 01 00 01 64 02 00 7D 04 00 7C 00 00 7C 03 00 17 7C 04 00 17 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CU'
                             00000003     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000006     64 - LOAD_CONST          'range calc: %d %d'
                             00000009     64 - LOAD_CONST          0
                             0000000C     7C - LOAD_FAST           'itemDeltaDamage'
                             0000000F     66 - BUILD_TUPLE         r0002
                             00000012     16 - BINARY_MODULO       
                             00000013     64 - LOAD_CONST          2
                             00000016     83 - CALL_FUNCTION       r0002
                             00000019     01 - POP_TOP             
                             0000001A     64 - LOAD_CONST          0
                             0000001D     7D - STORE_FAST          'calcDeltaDamage'
                             00000020     7C - LOAD_FAST           'itemDeltaDamage'
                             00000023     64 - LOAD_CONST          0
                             00000026     6A - COMPARE_OP          ">"
                             00000029     6F - JUMP_IF_FALSE       -> 0000004A
                             0000002C     01 - POP_TOP             
                             0000002D     74 - LOAD_GLOBAL         'random'
                             00000030     69 - LOAD_ATTR           'randrange'
                             00000033     64 - LOAD_CONST          0
                             00000036     7C - LOAD_FAST           'itemDeltaDamage'
                             00000039     64 - LOAD_CONST          2
                             0000003C     14 - BINARY_MULTIPLY     
                             0000003D     83 - CALL_FUNCTION       r0002
                             00000040     7C - LOAD_FAST           'itemDeltaDamage'
                             00000043     18 - BINARY_SUBTRACT     
                             00000044     7D - STORE_FAST          'calcDeltaDamage'
                             00000047     6E - JUMP_FORWARD        -> 0000004B
                             0000004A     01 - POP_TOP             
                             0000004B     64 - LOAD_CONST          0
                             0000004E     7D - STORE_FAST          'tacticalBonus'
                             00000051     7C - LOAD_FAST           'itemBaseDamage'
                             00000054     7C - LOAD_FAST           'calcDeltaDamage'
                             00000057     17 - BINARY_ADD          
                             00000058     7C - LOAD_FAST           'tacticalBonus'
                             0000005B     17 - BINARY_ADD          
                             0000005C     53 - RETURN_VALUE        
                             0000005D     64 - LOAD_CONST          None
                             00000060     53 - RETURN_VALUE        
                         consts:
0000016B                     TUPLE: (
00000170                         None (4E),
00000171                         STR: 'range calc: %d %d' (11 00 00 00 72 61 6E 67 65 20 63 61 6C 63 3A 20 25 64 20 25 64),
00000187                         INT: 0 (00 00 00 00),
0000018C                         INT: 2 (02 00 00 00)
                             )
                         names:
00000191                     TUPLE: (
00000196                         STR: 'CU' (02 00 00 00 43 55),
0000019D                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
000001BA                         STR: 'itemDeltaDamage' (0F 00 00 00 69 74 65 6D 44 65 6C 74 61 44 61 6D 61 67 65),
000001CE                         STR: 'calcDeltaDamage' (0F 00 00 00 63 61 6C 63 44 65 6C 74 61 44 61 6D 61 67 65),
000001E2                         STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
000001ED                         STR: 'randrange' (09 00 00 00 72 61 6E 64 72 61 6E 67 65),
000001FB                         STR: 'tacticalBonus' (0D 00 00 00 74 61 63 74 69 63 61 6C 42 6F 6E 75 73),
0000020D                         STR: 'itemBaseDamage' (0E 00 00 00 69 74 65 6D 42 61 73 65 44 61 6D 61 67 65)
                             )
                         varnames:
00000220                     TUPLE: (
00000225                         STR: 'itemBaseDamage' (0E 00 00 00 69 74 65 6D 42 61 73 65 44 61 6D 61 67 65),
00000238                         STR: 'itemDeltaDamage' (0F 00 00 00 69 74 65 6D 44 65 6C 74 61 44 61 6D 61 67 65),
0000024C                         STR: 'tactical_setting' (10 00 00 00 74 61 63 74 69 63 61 6C 5F 73 65 74 74 69 6E 67),
00000261                         STR: 'calcDeltaDamage' (0F 00 00 00 63 61 6C 63 44 65 6C 74 61 44 61 6D 61 67 65),
00000275                         STR: 'tacticalBonus' (0D 00 00 00 74 61 63 74 69 63 61 6C 42 6F 6E 75 73)
                             )
                         freevars:
00000287                     TUPLE: ()
                         cellvars:
0000028C                     TUPLE: ()
                         filename:
00000291                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat_calculations.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73 2E 70 79)
                         name:
000002E1                     STR: 'calcDamageWithGun' (11 00 00 00 63 61 6C 63 44 61 6D 61 67 65 57 69 74 68 47 75 6E)
                         firslineno:
000002F7                     LONG: 8L (08 00 00 00)
                         lnotab:
000002FB                     STR: '\x00\x01\x1a\x03\x06\x01\r\x01\x1e\x03\x06\x02' (0C 00 00 00 00 01 1A 03 06 01 0D 01 1E 03 06 02),
0000030C             CODE:
                         argcount:
0000030D                     LONG: 1L (01 00 00 00)
                         nlocals:
00000311                     LONG: 2L (02 00 00 00)
                         stacksize:
00000315                     LONG: 2L (02 00 00 00)
                         flags:
00000319                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000031D                     STR: 'd\x01\x00}\x01\x00|\x00\x00t\x02\x00i\x03\x00i\x04\x00j\x02\x00o\n\x00\x01d\x02\x00}\x01\x00nX\x00\x01|\x00\x00t\x02\x00i\x03\x00i\x05\x00j\x02\x00o\n\x00\x01d\x03\x00}\x01\x00n;\x00\x01|\x00\x00t\x02\x00i\x03\x00i\x06\x00j\x02\x00o\n\x00\x01d\x04\x00}\x01\x00n\x1e\x00\x01|\x00\x00t\x02\x00i\x03\x00i\x07\x00j\x02\x00o\n\x00\x01d\x05\x00}\x01\x00n\x01\x00\x01|\x01\x00Sd\x00\x00S' (82 00 00 00 64 01 00 7D 01 00 7C 00 00 74 02 00 69 03 00 69 04 00 6A 02 00 6F 0A 00 01 64 02 00 7D 01 00 6E 58 00 01 7C 00 00 74 02 00 69 03 00 69 05 00 6A 02 00 6F 0A 00 01 64 03 00 7D 01 00 6E 3B 00 01 7C 00 00 74 02 00 69 03 00 69 06 00 6A 02 00 6F 0A 00 01 64 04 00 7D 01 00 6E 1E 00 01 7C 00 00 74 02 00 69 03 00 69 07 00 6A 02 00 6F 0A 00 01 64 05 00 7D 01 00 6E 01 00 01 7C 01 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          1.0
                             00000003     7D - STORE_FAST          'tacticBonus'
                             00000006     7C - LOAD_FAST           'tacticalSetting'
                             00000009     74 - LOAD_GLOBAL         'constants'
                             0000000C     69 - LOAD_ATTR           'combat'
                             0000000F     69 - LOAD_ATTR           'BLOCK'
                             00000012     6A - COMPARE_OP          "=="
                             00000015     6F - JUMP_IF_FALSE       -> 00000022
                             00000018     01 - POP_TOP             
                             00000019     64 - LOAD_CONST          0.0
                             0000001C     7D - STORE_FAST          'tacticBonus'
                             0000001F     6E - JUMP_FORWARD        -> 0000007A
                             00000022     01 - POP_TOP             
                             00000023     7C - LOAD_FAST           'tacticalSetting'
                             00000026     74 - LOAD_GLOBAL         'constants'
                             00000029     69 - LOAD_ATTR           'combat'
                             0000002C     69 - LOAD_ATTR           'SPEED'
                             0000002F     6A - COMPARE_OP          "=="
                             00000032     6F - JUMP_IF_FALSE       -> 0000003F
                             00000035     01 - POP_TOP             
                             00000036     64 - LOAD_CONST          1.1499999999999999
                             00000039     7D - STORE_FAST          'tacticBonus'
                             0000003C     6E - JUMP_FORWARD        -> 0000007A
                             0000003F     01 - POP_TOP             
                             00000040     7C - LOAD_FAST           'tacticalSetting'
                             00000043     74 - LOAD_GLOBAL         'constants'
                             00000046     69 - LOAD_ATTR           'combat'
                             00000049     69 - LOAD_ATTR           'POWER'
                             0000004C     6A - COMPARE_OP          "=="
                             0000004F     6F - JUMP_IF_FALSE       -> 0000005C
                             00000052     01 - POP_TOP             
                             00000053     64 - LOAD_CONST          0.90000000000000002
                             00000056     7D - STORE_FAST          'tacticBonus'
                             00000059     6E - JUMP_FORWARD        -> 0000007A
                             0000005C     01 - POP_TOP             
                             0000005D     7C - LOAD_FAST           'tacticalSetting'
                             00000060     74 - LOAD_GLOBAL         'constants'
                             00000063     69 - LOAD_ATTR           'combat'
                             00000066     69 - LOAD_ATTR           'DEFENSE'
                             00000069     6A - COMPARE_OP          "=="
                             0000006C     6F - JUMP_IF_FALSE       -> 00000079
                             0000006F     01 - POP_TOP             
                             00000070     64 - LOAD_CONST          1.05
                             00000073     7D - STORE_FAST          'tacticBonus'
                             00000076     6E - JUMP_FORWARD        -> 0000007A
                             00000079     01 - POP_TOP             
                             0000007A     7C - LOAD_FAST           'tacticBonus'
                             0000007D     53 - RETURN_VALUE        
                             0000007E     64 - LOAD_CONST          None
                             00000081     53 - RETURN_VALUE        
                         consts:
000003A4                     TUPLE: (
000003A9                         None (4E),
000003AA                         FLOAT: 1.0 (03 31 2E 30),
000003AF                         FLOAT: 0.0 (03 30 2E 30),
000003B4                         FLOAT: 1.1499999999999999 (12 31 2E 31 34 39 39 39 39 39 39 39 39 39 39 39 39 39 39),
000003C8                         FLOAT: 0.90000000000000002 (13 30 2E 39 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 32),
000003DD                         FLOAT: 1.05 (04 31 2E 30 35)
                             )
                         names:
000003E3                     TUPLE: (
000003E8                         STR: 'tacticBonus' (0B 00 00 00 74 61 63 74 69 63 42 6F 6E 75 73),
000003F8                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
0000040C                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
0000041A                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
00000425                         STR: 'BLOCK' (05 00 00 00 42 4C 4F 43 4B),
0000042F                         STR: 'SPEED' (05 00 00 00 53 50 45 45 44),
00000439                         STR: 'POWER' (05 00 00 00 50 4F 57 45 52),
00000443                         STR: 'DEFENSE' (07 00 00 00 44 45 46 45 4E 53 45)
                             )
                         varnames:
0000044F                     TUPLE: (
00000454                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
00000468                         STR: 'tacticBonus' (0B 00 00 00 74 61 63 74 69 63 42 6F 6E 75 73)
                             )
                         freevars:
00000478                     TUPLE: ()
                         cellvars:
0000047D                     TUPLE: ()
                         filename:
00000482                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat_calculations.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73 2E 70 79)
                         name:
000004D2                     STR: 'GetTacticCombatTacticsMod' (19 00 00 00 47 65 74 54 61 63 74 69 63 43 6F 6D 62 61 74 54 61 63 74 69 63 73 4D 6F 64)
                         firslineno:
000004F0                     LONG: 21L (15 00 00 00)
                         lnotab:
000004F4                     STR: '\x00\x02\x06\x01\x13\x01\n\x01\x13\x01\n\x01\x13\x01\n\x01\x13\x01\n\x02' (14 00 00 00 00 02 06 01 13 01 0A 01 13 01 0A 01 13 01 0A 01 13 01 0A 02),
0000050D             CODE:
                         argcount:
0000050E                     LONG: 1L (01 00 00 00)
                         nlocals:
00000512                     LONG: 2L (02 00 00 00)
                         stacksize:
00000516                     LONG: 2L (02 00 00 00)
                         flags:
0000051A                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000051E                     STR: 'd\x01\x00}\x01\x00|\x00\x00t\x02\x00i\x03\x00i\x04\x00j\x02\x00o\n\x00\x01d\x02\x00}\x01\x00nX\x00\x01|\x00\x00t\x02\x00i\x03\x00i\x05\x00j\x02\x00o\n\x00\x01d\x03\x00}\x01\x00n;\x00\x01|\x00\x00t\x02\x00i\x03\x00i\x06\x00j\x02\x00o\n\x00\x01d\x01\x00}\x01\x00n\x1e\x00\x01|\x00\x00t\x02\x00i\x03\x00i\x07\x00j\x02\x00o\n\x00\x01d\x04\x00}\x01\x00n\x01\x00\x01|\x01\x00Sd\x00\x00S' (82 00 00 00 64 01 00 7D 01 00 7C 00 00 74 02 00 69 03 00 69 04 00 6A 02 00 6F 0A 00 01 64 02 00 7D 01 00 6E 58 00 01 7C 00 00 74 02 00 69 03 00 69 05 00 6A 02 00 6F 0A 00 01 64 03 00 7D 01 00 6E 3B 00 01 7C 00 00 74 02 00 69 03 00 69 06 00 6A 02 00 6F 0A 00 01 64 01 00 7D 01 00 6E 1E 00 01 7C 00 00 74 02 00 69 03 00 69 07 00 6A 02 00 6F 0A 00 01 64 04 00 7D 01 00 6E 01 00 01 7C 01 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          1.0
                             00000003     7D - STORE_FAST          'tacticBonus'
                             00000006     7C - LOAD_FAST           'tacticalSetting'
                             00000009     74 - LOAD_GLOBAL         'constants'
                             0000000C     69 - LOAD_ATTR           'combat'
                             0000000F     69 - LOAD_ATTR           'BLOCK'
                             00000012     6A - COMPARE_OP          "=="
                             00000015     6F - JUMP_IF_FALSE       -> 00000022
                             00000018     01 - POP_TOP             
                             00000019     64 - LOAD_CONST          1.5
                             0000001C     7D - STORE_FAST          'tacticBonus'
                             0000001F     6E - JUMP_FORWARD        -> 0000007A
                             00000022     01 - POP_TOP             
                             00000023     7C - LOAD_FAST           'tacticalSetting'
                             00000026     74 - LOAD_GLOBAL         'constants'
                             00000029     69 - LOAD_ATTR           'combat'
                             0000002C     69 - LOAD_ATTR           'SPEED'
                             0000002F     6A - COMPARE_OP          "=="
                             00000032     6F - JUMP_IF_FALSE       -> 0000003F
                             00000035     01 - POP_TOP             
                             00000036     64 - LOAD_CONST          0.90000000000000002
                             00000039     7D - STORE_FAST          'tacticBonus'
                             0000003C     6E - JUMP_FORWARD        -> 0000007A
                             0000003F     01 - POP_TOP             
                             00000040     7C - LOAD_FAST           'tacticalSetting'
                             00000043     74 - LOAD_GLOBAL         'constants'
                             00000046     69 - LOAD_ATTR           'combat'
                             00000049     69 - LOAD_ATTR           'POWER'
                             0000004C     6A - COMPARE_OP          "=="
                             0000004F     6F - JUMP_IF_FALSE       -> 0000005C
                             00000052     01 - POP_TOP             
                             00000053     64 - LOAD_CONST          1.0
                             00000056     7D - STORE_FAST          'tacticBonus'
                             00000059     6E - JUMP_FORWARD        -> 0000007A
                             0000005C     01 - POP_TOP             
                             0000005D     7C - LOAD_FAST           'tacticalSetting'
                             00000060     74 - LOAD_GLOBAL         'constants'
                             00000063     69 - LOAD_ATTR           'combat'
                             00000066     69 - LOAD_ATTR           'DEFENSE'
                             00000069     6A - COMPARE_OP          "=="
                             0000006C     6F - JUMP_IF_FALSE       -> 00000079
                             0000006F     01 - POP_TOP             
                             00000070     64 - LOAD_CONST          1.3
                             00000073     7D - STORE_FAST          'tacticBonus'
                             00000076     6E - JUMP_FORWARD        -> 0000007A
                             00000079     01 - POP_TOP             
                             0000007A     7C - LOAD_FAST           'tacticBonus'
                             0000007D     53 - RETURN_VALUE        
                             0000007E     64 - LOAD_CONST          None
                             00000081     53 - RETURN_VALUE        
                         consts:
000005A5                     TUPLE: (
000005AA                         None (4E),
000005AB                         FLOAT: 1.0 (03 31 2E 30),
000005B0                         FLOAT: 1.5 (03 31 2E 35),
000005B5                         FLOAT: 0.90000000000000002 (13 30 2E 39 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 32),
000005CA                         FLOAT: 1.3 (03 31 2E 33)
                             )
                         names:
000005CF                     TUPLE: (
000005D4                         STR: 'tacticBonus' (0B 00 00 00 74 61 63 74 69 63 42 6F 6E 75 73),
000005E4                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
000005F8                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00000606                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
00000611                         STR: 'BLOCK' (05 00 00 00 42 4C 4F 43 4B),
0000061B                         STR: 'SPEED' (05 00 00 00 53 50 45 45 44),
00000625                         STR: 'POWER' (05 00 00 00 50 4F 57 45 52),
0000062F                         STR: 'DEFENSE' (07 00 00 00 44 45 46 45 4E 53 45)
                             )
                         varnames:
0000063B                     TUPLE: (
00000640                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
00000654                         STR: 'tacticBonus' (0B 00 00 00 74 61 63 74 69 63 42 6F 6E 75 73)
                             )
                         freevars:
00000664                     TUPLE: ()
                         cellvars:
00000669                     TUPLE: ()
                         filename:
0000066E                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat_calculations.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73 2E 70 79)
                         name:
000006BE                     STR: 'GetTacticDefenseTacticsMod' (1A 00 00 00 47 65 74 54 61 63 74 69 63 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 4D 6F 64)
                         firslineno:
000006DD                     LONG: 36L (24 00 00 00)
                         lnotab:
000006E1                     STR: '\x00\x02\x06\x01\x13\x01\n\x01\x13\x01\n\x01\x13\x01\n\x01\x13\x01\n\x02' (14 00 00 00 00 02 06 01 13 01 0A 01 13 01 0A 01 13 01 0A 01 13 01 0A 02),
000006FA             CODE:
                         argcount:
000006FB                     LONG: 1L (01 00 00 00)
                         nlocals:
000006FF                     LONG: 2L (02 00 00 00)
                         stacksize:
00000703                     LONG: 2L (02 00 00 00)
                         flags:
00000707                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000070B                     STR: 'd\x01\x00}\x01\x00|\x00\x00t\x02\x00i\x03\x00i\x04\x00j\x02\x00o\n\x00\x01d\x02\x00}\x01\x00nX\x00\x01|\x00\x00t\x02\x00i\x03\x00i\x05\x00j\x02\x00o\n\x00\x01d\x01\x00}\x01\x00n;\x00\x01|\x00\x00t\x02\x00i\x03\x00i\x06\x00j\x02\x00o\n\x00\x01d\x03\x00}\x01\x00n\x1e\x00\x01|\x00\x00t\x02\x00i\x03\x00i\x07\x00j\x02\x00o\n\x00\x01d\x04\x00}\x01\x00n\x01\x00\x01|\x01\x00Sd\x00\x00S' (82 00 00 00 64 01 00 7D 01 00 7C 00 00 74 02 00 69 03 00 69 04 00 6A 02 00 6F 0A 00 01 64 02 00 7D 01 00 6E 58 00 01 7C 00 00 74 02 00 69 03 00 69 05 00 6A 02 00 6F 0A 00 01 64 01 00 7D 01 00 6E 3B 00 01 7C 00 00 74 02 00 69 03 00 69 06 00 6A 02 00 6F 0A 00 01 64 03 00 7D 01 00 6E 1E 00 01 7C 00 00 74 02 00 69 03 00 69 07 00 6A 02 00 6F 0A 00 01 64 04 00 7D 01 00 6E 01 00 01 7C 01 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          1.0
                             00000003     7D - STORE_FAST          'dmgBonus'
                             00000006     7C - LOAD_FAST           'tacticalSetting'
                             00000009     74 - LOAD_GLOBAL         'constants'
                             0000000C     69 - LOAD_ATTR           'combat'
                             0000000F     69 - LOAD_ATTR           'BLOCK'
                             00000012     6A - COMPARE_OP          "=="
                             00000015     6F - JUMP_IF_FALSE       -> 00000022
                             00000018     01 - POP_TOP             
                             00000019     64 - LOAD_CONST          0
                             0000001C     7D - STORE_FAST          'dmgBonus'
                             0000001F     6E - JUMP_FORWARD        -> 0000007A
                             00000022     01 - POP_TOP             
                             00000023     7C - LOAD_FAST           'tacticalSetting'
                             00000026     74 - LOAD_GLOBAL         'constants'
                             00000029     69 - LOAD_ATTR           'combat'
                             0000002C     69 - LOAD_ATTR           'SPEED'
                             0000002F     6A - COMPARE_OP          "=="
                             00000032     6F - JUMP_IF_FALSE       -> 0000003F
                             00000035     01 - POP_TOP             
                             00000036     64 - LOAD_CONST          1.0
                             00000039     7D - STORE_FAST          'dmgBonus'
                             0000003C     6E - JUMP_FORWARD        -> 0000007A
                             0000003F     01 - POP_TOP             
                             00000040     7C - LOAD_FAST           'tacticalSetting'
                             00000043     74 - LOAD_GLOBAL         'constants'
                             00000046     69 - LOAD_ATTR           'combat'
                             00000049     69 - LOAD_ATTR           'POWER'
                             0000004C     6A - COMPARE_OP          "=="
                             0000004F     6F - JUMP_IF_FALSE       -> 0000005C
                             00000052     01 - POP_TOP             
                             00000053     64 - LOAD_CONST          1.2
                             00000056     7D - STORE_FAST          'dmgBonus'
                             00000059     6E - JUMP_FORWARD        -> 0000007A
                             0000005C     01 - POP_TOP             
                             0000005D     7C - LOAD_FAST           'tacticalSetting'
                             00000060     74 - LOAD_GLOBAL         'constants'
                             00000063     69 - LOAD_ATTR           'combat'
                             00000066     69 - LOAD_ATTR           'DEFENSE'
                             00000069     6A - COMPARE_OP          "=="
                             0000006C     6F - JUMP_IF_FALSE       -> 00000079
                             0000006F     01 - POP_TOP             
                             00000070     64 - LOAD_CONST          0.84999999999999998
                             00000073     7D - STORE_FAST          'dmgBonus'
                             00000076     6E - JUMP_FORWARD        -> 0000007A
                             00000079     01 - POP_TOP             
                             0000007A     7C - LOAD_FAST           'dmgBonus'
                             0000007D     53 - RETURN_VALUE        
                             0000007E     64 - LOAD_CONST          None
                             00000081     53 - RETURN_VALUE        
                         consts:
00000792                     TUPLE: (
00000797                         None (4E),
00000798                         FLOAT: 1.0 (03 31 2E 30),
0000079D                         INT: 0 (00 00 00 00),
000007A2                         FLOAT: 1.2 (03 31 2E 32),
000007A7                         FLOAT: 0.84999999999999998 (13 30 2E 38 34 39 39 39 39 39 39 39 39 39 39 39 39 39 39 38)
                             )
                         names:
000007BC                     TUPLE: (
000007C1                         STR: 'dmgBonus' (08 00 00 00 64 6D 67 42 6F 6E 75 73),
000007CE                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
000007E2                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
000007F0                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
000007FB                         STR: 'BLOCK' (05 00 00 00 42 4C 4F 43 4B),
00000805                         STR: 'SPEED' (05 00 00 00 53 50 45 45 44),
0000080F                         STR: 'POWER' (05 00 00 00 50 4F 57 45 52),
00000819                         STR: 'DEFENSE' (07 00 00 00 44 45 46 45 4E 53 45)
                             )
                         varnames:
00000825                     TUPLE: (
0000082A                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
0000083E                         STR: 'dmgBonus' (08 00 00 00 64 6D 67 42 6F 6E 75 73)
                             )
                         freevars:
0000084B                     TUPLE: ()
                         cellvars:
00000850                     TUPLE: ()
                         filename:
00000855                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat_calculations.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73 2E 70 79)
                         name:
000008A5                     STR: 'GetTacticDamageMod' (12 00 00 00 47 65 74 54 61 63 74 69 63 44 61 6D 61 67 65 4D 6F 64)
                         firslineno:
000008BC                     LONG: 50L (32 00 00 00)
                         lnotab:
000008C0                     STR: '\x00\x02\x06\x01\x13\x01\n\x01\x13\x01\n\x01\x13\x01\n\x01\x13\x01\n\x02' (14 00 00 00 00 02 06 01 13 01 0A 01 13 01 0A 01 13 01 0A 01 13 01 0A 02),
000008D9             CODE:
                         argcount:
000008DA                     LONG: 1L (01 00 00 00)
                         nlocals:
000008DE                     LONG: 2L (02 00 00 00)
                         stacksize:
000008E2                     LONG: 2L (02 00 00 00)
                         flags:
000008E6                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000008EA                     STR: 'd\x01\x00}\x01\x00|\x00\x00t\x02\x00i\x03\x00i\x04\x00j\x02\x00o\n\x00\x01d\x01\x00}\x01\x00nX\x00\x01|\x00\x00t\x02\x00i\x03\x00i\x05\x00j\x02\x00o\n\x00\x01d\x01\x00}\x01\x00n;\x00\x01|\x00\x00t\x02\x00i\x03\x00i\x06\x00j\x02\x00o\n\x00\x01d\x02\x00}\x01\x00n\x1e\x00\x01|\x00\x00t\x02\x00i\x03\x00i\x07\x00j\x02\x00o\n\x00\x01d\x03\x00}\x01\x00n\x01\x00\x01|\x01\x00Sd\x00\x00S' (82 00 00 00 64 01 00 7D 01 00 7C 00 00 74 02 00 69 03 00 69 04 00 6A 02 00 6F 0A 00 01 64 01 00 7D 01 00 6E 58 00 01 7C 00 00 74 02 00 69 03 00 69 05 00 6A 02 00 6F 0A 00 01 64 01 00 7D 01 00 6E 3B 00 01 7C 00 00 74 02 00 69 03 00 69 06 00 6A 02 00 6F 0A 00 01 64 02 00 7D 01 00 6E 1E 00 01 7C 00 00 74 02 00 69 03 00 69 07 00 6A 02 00 6F 0A 00 01 64 03 00 7D 01 00 6E 01 00 01 7C 01 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          1.0
                             00000003     7D - STORE_FAST          'dmgBonus'
                             00000006     7C - LOAD_FAST           'tacticalSetting'
                             00000009     74 - LOAD_GLOBAL         'constants'
                             0000000C     69 - LOAD_ATTR           'combat'
                             0000000F     69 - LOAD_ATTR           'BLOCK'
                             00000012     6A - COMPARE_OP          "=="
                             00000015     6F - JUMP_IF_FALSE       -> 00000022
                             00000018     01 - POP_TOP             
                             00000019     64 - LOAD_CONST          1.0
                             0000001C     7D - STORE_FAST          'dmgBonus'
                             0000001F     6E - JUMP_FORWARD        -> 0000007A
                             00000022     01 - POP_TOP             
                             00000023     7C - LOAD_FAST           'tacticalSetting'
                             00000026     74 - LOAD_GLOBAL         'constants'
                             00000029     69 - LOAD_ATTR           'combat'
                             0000002C     69 - LOAD_ATTR           'SPEED'
                             0000002F     6A - COMPARE_OP          "=="
                             00000032     6F - JUMP_IF_FALSE       -> 0000003F
                             00000035     01 - POP_TOP             
                             00000036     64 - LOAD_CONST          1.0
                             00000039     7D - STORE_FAST          'dmgBonus'
                             0000003C     6E - JUMP_FORWARD        -> 0000007A
                             0000003F     01 - POP_TOP             
                             00000040     7C - LOAD_FAST           'tacticalSetting'
                             00000043     74 - LOAD_GLOBAL         'constants'
                             00000046     69 - LOAD_ATTR           'combat'
                             00000049     69 - LOAD_ATTR           'POWER'
                             0000004C     6A - COMPARE_OP          "=="
                             0000004F     6F - JUMP_IF_FALSE       -> 0000005C
                             00000052     01 - POP_TOP             
                             00000053     64 - LOAD_CONST          1.2
                             00000056     7D - STORE_FAST          'dmgBonus'
                             00000059     6E - JUMP_FORWARD        -> 0000007A
                             0000005C     01 - POP_TOP             
                             0000005D     7C - LOAD_FAST           'tacticalSetting'
                             00000060     74 - LOAD_GLOBAL         'constants'
                             00000063     69 - LOAD_ATTR           'combat'
                             00000066     69 - LOAD_ATTR           'DEFENSE'
                             00000069     6A - COMPARE_OP          "=="
                             0000006C     6F - JUMP_IF_FALSE       -> 00000079
                             0000006F     01 - POP_TOP             
                             00000070     64 - LOAD_CONST          0.90000000000000002
                             00000073     7D - STORE_FAST          'dmgBonus'
                             00000076     6E - JUMP_FORWARD        -> 0000007A
                             00000079     01 - POP_TOP             
                             0000007A     7C - LOAD_FAST           'dmgBonus'
                             0000007D     53 - RETURN_VALUE        
                             0000007E     64 - LOAD_CONST          None
                             00000081     53 - RETURN_VALUE        
                         consts:
00000971                     TUPLE: (
00000976                         None (4E),
00000977                         FLOAT: 1.0 (03 31 2E 30),
0000097C                         FLOAT: 1.2 (03 31 2E 32),
00000981                         FLOAT: 0.90000000000000002 (13 30 2E 39 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 32)
                             )
                         names:
00000996                     TUPLE: (
0000099B                         STR: 'dmgBonus' (08 00 00 00 64 6D 67 42 6F 6E 75 73),
000009A8                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
000009BC                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
000009CA                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
000009D5                         STR: 'BLOCK' (05 00 00 00 42 4C 4F 43 4B),
000009DF                         STR: 'SPEED' (05 00 00 00 53 50 45 45 44),
000009E9                         STR: 'POWER' (05 00 00 00 50 4F 57 45 52),
000009F3                         STR: 'DEFENSE' (07 00 00 00 44 45 46 45 4E 53 45)
                             )
                         varnames:
000009FF                     TUPLE: (
00000A04                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
00000A18                         STR: 'dmgBonus' (08 00 00 00 64 6D 67 42 6F 6E 75 73)
                             )
                         freevars:
00000A25                     TUPLE: ()
                         cellvars:
00000A2A                     TUPLE: ()
                         filename:
00000A2F                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat_calculations.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73 2E 70 79)
                         name:
00000A7F                     STR: 'GetTacticWithdrawTacticsMod' (1B 00 00 00 47 65 74 54 61 63 74 69 63 57 69 74 68 64 72 61 77 54 61 63 74 69 63 73 4D 6F 64)
                         firslineno:
00000A9F                     LONG: 65L (41 00 00 00)
                         lnotab:
00000AA3                     STR: '\x00\x02\x06\x01\x13\x01\n\x01\x13\x01\n\x01\x13\x01\n\x01\x13\x01\n\x02' (14 00 00 00 00 02 06 01 13 01 0A 01 13 01 0A 01 13 01 0A 01 13 01 0A 02),
00000ABC             CODE:
                         argcount:
00000ABD                     LONG: 9L (09 00 00 00)
                         nlocals:
00000AC1                     LONG: 12L (0C 00 00 00)
                         stacksize:
00000AC5                     LONG: 6L (06 00 00 00)
                         flags:
00000AC9                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000ACD                     STR: 'd\x01\x00}\x0b\x00t\x01\x00|\x02\x00|\x03\x00|\x07\x00\x83\x03\x00}\x0b\x00t\x05\x00i\x06\x00d\x02\x00|\x0b\x00\x16d\x03\x00\x83\x02\x00\x01|\x02\x00d\x01\x00j\x03\x00o;\x00\x01|\x0b\x00t\x07\x00t\x08\x00|\x0b\x00\x83\x01\x00|\x01\x00\x14\x83\x01\x007}\x0b\x00t\x05\x00i\x06\x00d\x04\x00|\x02\x00|\x01\x00|\x0b\x00f\x03\x00\x16d\x03\x00\x83\x02\x00\x01n\x01\x00\x01|\x08\x00o@\x00\x01t\x0b\x00i\x0c\x00|\x0b\x00|\x0b\x00d\x03\x00\x15|\x0b\x00d\x05\x00\x15d\x06\x00|\x0b\x00\x14d\x05\x00\x15\x83\x04\x00}\x0b\x00t\x05\x00i\x06\x00d\x07\x00|\x0b\x00\x16d\x03\x00\x83\x02\x00\x01n\x01\x00\x01|\x00\x00|\x0b\x00\x17}\n\x00t\x05\x00i\x0f\x00d\x08\x00|\x0b\x00|\x00\x00|\n\x00f\x03\x00\x16d\x03\x00\x83\x02\x00\x01|\n\x00t\x10\x00i\x11\x009}\n\x00t\x05\x00i\x0f\x00d\t\x00|\n\x00\x16d\x03\x00\x83\x02\x00\x01t\x12\x00|\x07\x00\x83\x01\x00}\t\x00t\x07\x00|\n\x00|\t\x00\x14\x83\x01\x00}\n\x00t\x05\x00i\x06\x00d\n\x00|\t\x00|\n\x00f\x02\x00\x16d\x03\x00\x83\x02\x00\x01|\x05\x00o(\x00\x01t\x07\x00|\n\x00d\x0b\x00\x14\x83\x01\x00}\n\x00t\x05\x00i\x06\x00d\x0c\x00|\n\x00\x16d\x03\x00\x83\x02\x00\x01n\x01\x00\x01|\x06\x00o(\x00\x01t\x07\x00|\n\x00d\r\x00\x14\x83\x01\x00}\n\x00t\x05\x00i\x06\x00d\x0e\x00|\n\x00\x16d\x03\x00\x83\x02\x00\x01n\x01\x00\x01t\x07\x00t\x08\x00|\n\x00\x83\x01\x00|\x04\x00\x14\x83\x01\x00}\n\x00t\x05\x00i\x06\x00d\x0f\x00|\x04\x00|\n\x00f\x02\x00\x16d\x03\x00\x83\x02\x00\x01t\x07\x00|\n\x00\x83\x01\x00Sd\x00\x00S' (D5 01 00 00 64 01 00 7D 0B 00 74 01 00 7C 02 00 7C 03 00 7C 07 00 83 03 00 7D 0B 00 74 05 00 69 06 00 64 02 00 7C 0B 00 16 64 03 00 83 02 00 01 7C 02 00 64 01 00 6A 03 00 6F 3B 00 01 7C 0B 00 74 07 00 74 08 00 7C 0B 00 83 01 00 7C 01 00 14 83 01 00 37 7D 0B 00 74 05 00 69 06 00 64 04 00 7C 02 00 7C 01 00 7C 0B 00 66 03 00 16 64 03 00 83 02 00 01 6E 01 00 01 7C 08 00 6F 40 00 01 74 0B 00 69 0C 00 7C 0B 00 7C 0B 00 64 03 00 15 7C 0B 00 64 05 00 15 64 06 00 7C 0B 00 14 64 05 00 15 83 04 00 7D 0B 00 74 05 00 69 06 00 64 07 00 7C 0B 00 16 64 03 00 83 02 00 01 6E 01 00 01 7C 00 00 7C 0B 00 17 7D 0A 00 74 05 00 69 0F 00 64 08 00 7C 0B 00 7C 00 00 7C 0A 00 66 03 00 16 64 03 00 83 02 00 01 7C 0A 00 74 10 00 69 11 00 39 7D 0A 00 74 05 00 69 0F 00 64 09 00 7C 0A 00 16 64 03 00 83 02 00 01 74 12 00 7C 07 00 83 01 00 7D 09 00 74 07 00 7C 0A 00 7C 09 00 14 83 01 00 7D 0A 00 74 05 00 69 06 00 64 0A 00 7C 09 00 7C 0A 00 66 02 00 16 64 03 00 83 02 00 01 7C 05 00 6F 28 00 01 74 07 00 7C 0A 00 64 0B 00 14 83 01 00 7D 0A 00 74 05 00 69 06 00 64 0C 00 7C 0A 00 16 64 03 00 83 02 00 01 6E 01 00 01 7C 06 00 6F 28 00 01 74 07 00 7C 0A 00 64 0D 00 14 83 01 00 7D 0A 00 74 05 00 69 06 00 64 0E 00 7C 0A 00 16 64 03 00 83 02 00 01 6E 01 00 01 74 07 00 74 08 00 7C 0A 00 83 01 00 7C 04 00 14 83 01 00 7D 0A 00 74 05 00 69 06 00 64 0F 00 7C 04 00 7C 0A 00 66 02 00 16 64 03 00 83 02 00 01 74 07 00 7C 0A 00 83 01 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          0
                             00000003     7D - STORE_FAST          'baseDamage'
                             00000006     74 - LOAD_GLOBAL         'calcDamageWithGun'
                             00000009     7C - LOAD_FAST           'iWeaponBaseDamage'
                             0000000C     7C - LOAD_FAST           'iWeaponDamageRange'
                             0000000F     7C - LOAD_FAST           'eTacticType'
                             00000012     83 - CALL_FUNCTION       r0003
                             00000015     7D - STORE_FAST          'baseDamage'
                             00000018     74 - LOAD_GLOBAL         'CU'
                             0000001B     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             0000001E     64 - LOAD_CONST          'GetFreeAttackDamage: damage with gun: %d'
                             00000021     7C - LOAD_FAST           'baseDamage'
                             00000024     16 - BINARY_MODULO       
                             00000025     64 - LOAD_CONST          10
                             00000028     83 - CALL_FUNCTION       r0002
                             0000002B     01 - POP_TOP             
                             0000002C     7C - LOAD_FAST           'iWeaponBaseDamage'
                             0000002F     64 - LOAD_CONST          0
                             00000032     6A - COMPARE_OP          "!="
                             00000035     6F - JUMP_IF_FALSE       -> 00000073
                             00000038     01 - POP_TOP             
                             00000039     7C - LOAD_FAST           'baseDamage'
                             0000003C     74 - LOAD_GLOBAL         'int'
                             0000003F     74 - LOAD_GLOBAL         'float'
                             00000042     7C - LOAD_FAST           'baseDamage'
                             00000045     83 - CALL_FUNCTION       r0001
                             00000048     7C - LOAD_FAST           'damageTypeInfluence'
                             0000004B     14 - BINARY_MULTIPLY     
                             0000004C     83 - CALL_FUNCTION       r0001
                             0000004F     37 - INPLACE_ADD         
                             00000050     7D - STORE_FAST          'baseDamage'
                             00000053     74 - LOAD_GLOBAL         'CU'
                             00000056     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000059     64 - LOAD_CONST          'Damage with weapon bonus (weapDmg(%d)*DamageInflu(%g)) = %d'
                             0000005C     7C - LOAD_FAST           'iWeaponBaseDamage'
                             0000005F     7C - LOAD_FAST           'damageTypeInfluence'
                             00000062     7C - LOAD_FAST           'baseDamage'
                             00000065     66 - BUILD_TUPLE         r0003
                             00000068     16 - BINARY_MODULO       
                             00000069     64 - LOAD_CONST          10
                             0000006C     83 - CALL_FUNCTION       r0002
                             0000006F     01 - POP_TOP             
                             00000070     6E - JUMP_FORWARD        -> 00000074
                             00000073     01 - POP_TOP             
                             00000074     7C - LOAD_FAST           'bAddRandGaussian'
                             00000077     6F - JUMP_IF_FALSE       -> 000000BA
                             0000007A     01 - POP_TOP             
                             0000007B     74 - LOAD_GLOBAL         'discovery'
                             0000007E     69 - LOAD_ATTR           'getGaussianRandomClamped'
                             00000081     7C - LOAD_FAST           'baseDamage'
                             00000084     7C - LOAD_FAST           'baseDamage'
                             00000087     64 - LOAD_CONST          10
                             0000008A     15 - BINARY_DIVIDE       
                             0000008B     7C - LOAD_FAST           'baseDamage'
                             0000008E     64 - LOAD_CONST          3
                             00000091     15 - BINARY_DIVIDE       
                             00000092     64 - LOAD_CONST          4
                             00000095     7C - LOAD_FAST           'baseDamage'
                             00000098     14 - BINARY_MULTIPLY     
                             00000099     64 - LOAD_CONST          3
                             0000009C     15 - BINARY_DIVIDE       
                             0000009D     83 - CALL_FUNCTION       r0004
                             000000A0     7D - STORE_FAST          'baseDamage'
                             000000A3     74 - LOAD_GLOBAL         'CU'
                             000000A6     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             000000A9     64 - LOAD_CONST          'GetFreeAttackDamage: new damage with rand: %d'
                             000000AC     7C - LOAD_FAST           'baseDamage'
                             000000AF     16 - BINARY_MODULO       
                             000000B0     64 - LOAD_CONST          10
                             000000B3     83 - CALL_FUNCTION       r0002
                             000000B6     01 - POP_TOP             
                             000000B7     6E - JUMP_FORWARD        -> 000000BB
                             000000BA     01 - POP_TOP             
                             000000BB     7C - LOAD_FAST           'iBonuses'
                             000000BE     7C - LOAD_FAST           'baseDamage'
                             000000C1     17 - BINARY_ADD          
                             000000C2     7D - STORE_FAST          'damage_total'
                             000000C5     74 - LOAD_GLOBAL         'CU'
                             000000C8     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000CB     64 - LOAD_CONST          'GetFreeAttackDamage: attacker damage: (%dDmg + %dDmgBonus) = %dTotalDmg'
                             000000CE     7C - LOAD_FAST           'baseDamage'
                             000000D1     7C - LOAD_FAST           'iBonuses'
                             000000D4     7C - LOAD_FAST           'damage_total'
                             000000D7     66 - BUILD_TUPLE         r0003
                             000000DA     16 - BINARY_MODULO       
                             000000DB     64 - LOAD_CONST          10
                             000000DE     83 - CALL_FUNCTION       r0002
                             000000E1     01 - POP_TOP             
                             000000E2     7C - LOAD_FAST           'damage_total'
                             000000E5     74 - LOAD_GLOBAL         'consolevar'
                             000000E8     69 - LOAD_ATTR           'FreeFireScalar'
                             000000EB     39 - INPLACE_MULTIPLY    
                             000000EC     7D - STORE_FAST          'damage_total'
                             000000EF     74 - LOAD_GLOBAL         'CU'
                             000000F2     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000F5     64 - LOAD_CONST          'GetFreeAttackDamage: attacker damage after scalar: %dTotalDmg'
                             000000F8     7C - LOAD_FAST           'damage_total'
                             000000FB     16 - BINARY_MODULO       
                             000000FC     64 - LOAD_CONST          10
                             000000FF     83 - CALL_FUNCTION       r0002
                             00000102     01 - POP_TOP             
                             00000103     74 - LOAD_GLOBAL         'GetTacticDamageMod'
                             00000106     7C - LOAD_FAST           'eTacticType'
                             00000109     83 - CALL_FUNCTION       r0001
                             0000010C     7D - STORE_FAST          'tacticDamagePercentMod'
                             0000010F     74 - LOAD_GLOBAL         'int'
                             00000112     7C - LOAD_FAST           'damage_total'
                             00000115     7C - LOAD_FAST           'tacticDamagePercentMod'
                             00000118     14 - BINARY_MULTIPLY     
                             00000119     83 - CALL_FUNCTION       r0001
                             0000011C     7D - STORE_FAST          'damage_total'
                             0000011F     74 - LOAD_GLOBAL         'CU'
                             00000122     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000125     64 - LOAD_CONST          'GetFreeAttackDamage: damage (after %g tacticMod): %d'
                             00000128     7C - LOAD_FAST           'tacticDamagePercentMod'
                             0000012B     7C - LOAD_FAST           'damage_total'
                             0000012E     66 - BUILD_TUPLE         r0002
                             00000131     16 - BINARY_MODULO       
                             00000132     64 - LOAD_CONST          10
                             00000135     83 - CALL_FUNCTION       r0002
                             00000138     01 - POP_TOP             
                             00000139     7C - LOAD_FAST           'isEnergizedTactic'
                             0000013C     6F - JUMP_IF_FALSE       -> 00000167
                             0000013F     01 - POP_TOP             
                             00000140     74 - LOAD_GLOBAL         'int'
                             00000143     7C - LOAD_FAST           'damage_total'
                             00000146     64 - LOAD_CONST          1.1499999999999999
                             00000149     14 - BINARY_MULTIPLY     
                             0000014A     83 - CALL_FUNCTION       r0001
                             0000014D     7D - STORE_FAST          'damage_total'
                             00000150     74 - LOAD_GLOBAL         'CU'
                             00000153     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000156     64 - LOAD_CONST          'GetFreeAttackDamage: Engerzied boost: %d'
                             00000159     7C - LOAD_FAST           'damage_total'
                             0000015C     16 - BINARY_MODULO       
                             0000015D     64 - LOAD_CONST          10
                             00000160     83 - CALL_FUNCTION       r0002
                             00000163     01 - POP_TOP             
                             00000164     6E - JUMP_FORWARD        -> 00000168
                             00000167     01 - POP_TOP             
                             00000168     7C - LOAD_FAST           'isPreciseBlows'
                             0000016B     6F - JUMP_IF_FALSE       -> 00000196
                             0000016E     01 - POP_TOP             
                             0000016F     74 - LOAD_GLOBAL         'int'
                             00000172     7C - LOAD_FAST           'damage_total'
                             00000175     64 - LOAD_CONST          0.84999999999999998
                             00000178     14 - BINARY_MULTIPLY     
                             00000179     83 - CALL_FUNCTION       r0001
                             0000017C     7D - STORE_FAST          'damage_total'
                             0000017F     74 - LOAD_GLOBAL         'CU'
                             00000182     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000185     64 - LOAD_CONST          'GetFreeAttackDamage: Percise blows deboost: %d'
                             00000188     7C - LOAD_FAST           'damage_total'
                             0000018B     16 - BINARY_MODULO       
                             0000018C     64 - LOAD_CONST          10
                             0000018F     83 - CALL_FUNCTION       r0002
                             00000192     01 - POP_TOP             
                             00000193     6E - JUMP_FORWARD        -> 00000197
                             00000196     01 - POP_TOP             
                             00000197     74 - LOAD_GLOBAL         'int'
                             0000019A     74 - LOAD_GLOBAL         'float'
                             0000019D     7C - LOAD_FAST           'damage_total'
                             000001A0     83 - CALL_FUNCTION       r0001
                             000001A3     7C - LOAD_FAST           'fWeaponSpeed'
                             000001A6     14 - BINARY_MULTIPLY     
                             000001A7     83 - CALL_FUNCTION       r0001
                             000001AA     7D - STORE_FAST          'damage_total'
                             000001AD     74 - LOAD_GLOBAL         'CU'
                             000001B0     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             000001B3     64 - LOAD_CONST          'GetFreeAttackDamage: damage (after %g weapon speed): %d'
                             000001B6     7C - LOAD_FAST           'fWeaponSpeed'
                             000001B9     7C - LOAD_FAST           'damage_total'
                             000001BC     66 - BUILD_TUPLE         r0002
                             000001BF     16 - BINARY_MODULO       
                             000001C0     64 - LOAD_CONST          10
                             000001C3     83 - CALL_FUNCTION       r0002
                             000001C6     01 - POP_TOP             
                             000001C7     74 - LOAD_GLOBAL         'int'
                             000001CA     7C - LOAD_FAST           'damage_total'
                             000001CD     83 - CALL_FUNCTION       r0001
                             000001D0     53 - RETURN_VALUE        
                             000001D1     64 - LOAD_CONST          None
                             000001D4     53 - RETURN_VALUE        
                         consts:
00000CA7                     TUPLE: (
00000CAC                         None (4E),
00000CAD                         INT: 0 (00 00 00 00),
00000CB2                         STR: 'GetFreeAttackDamage: damage with gun: %d' (28 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65 3A 20 64 61 6D 61 67 65 20 77 69 74 68 20 67 75 6E 3A 20 25 64),
00000CDF                         INT: 10 (0A 00 00 00),
00000CE4                         STR: 'Damage with weapon bonus (weapDmg(%d)*DamageInflu(%g)) = %d' (3B 00 00 00 44 61 6D 61 67 65 20 77 69 74 68 20 77 65 61 70 6F 6E 20 62 6F 6E 75 73 20 28 77 65 61 70 44 6D 67 28 25 64 29 2A 44 61 6D 61 67 65 49 6E 66 6C 75 28 25 67 29 29 20 3D 20 25 64),
00000D24                         INT: 3 (03 00 00 00),
00000D29                         INT: 4 (04 00 00 00),
00000D2E                         STR: 'GetFreeAttackDamage: new damage with rand: %d' (2D 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65 3A 20 6E 65 77 20 64 61 6D 61 67 65 20 77 69 74 68 20 72 61 6E 64 3A 20 25 64),
00000D60                         STR: 'GetFreeAttackDamage: attacker damage: (%dDmg + %dDmgBonus) = %dTotalDmg' (47 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65 3A 20 61 74 74 61 63 6B 65 72 20 64 61 6D 61 67 65 3A 20 28 25 64 44 6D 67 20 2B 20 25 64 44 6D 67 42 6F 6E 75 73 29 20 3D 20 25 64 54 6F 74 61 6C 44 6D 67),
00000DAC                         STR: 'GetFreeAttackDamage: attacker damage after scalar: %dTotalDmg' (3D 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65 3A 20 61 74 74 61 63 6B 65 72 20 64 61 6D 61 67 65 20 61 66 74 65 72 20 73 63 61 6C 61 72 3A 20 25 64 54 6F 74 61 6C 44 6D 67),
00000DEE                         STR: 'GetFreeAttackDamage: damage (after %g tacticMod): %d' (34 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65 3A 20 64 61 6D 61 67 65 20 28 61 66 74 65 72 20 25 67 20 74 61 63 74 69 63 4D 6F 64 29 3A 20 25 64),
00000E27                         FLOAT: 1.1499999999999999 (12 31 2E 31 34 39 39 39 39 39 39 39 39 39 39 39 39 39 39),
00000E3B                         STR: 'GetFreeAttackDamage: Engerzied boost: %d' (28 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65 3A 20 45 6E 67 65 72 7A 69 65 64 20 62 6F 6F 73 74 3A 20 25 64),
00000E68                         FLOAT: 0.84999999999999998 (13 30 2E 38 34 39 39 39 39 39 39 39 39 39 39 39 39 39 39 38),
00000E7D                         STR: 'GetFreeAttackDamage: Percise blows deboost: %d' (2E 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65 3A 20 50 65 72 63 69 73 65 20 62 6C 6F 77 73 20 64 65 62 6F 6F 73 74 3A 20 25 64),
00000EB0                         STR: 'GetFreeAttackDamage: damage (after %g weapon speed): %d' (37 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65 3A 20 64 61 6D 61 67 65 20 28 61 66 74 65 72 20 25 67 20 77 65 61 70 6F 6E 20 73 70 65 65 64 29 3A 20 25 64)
                             )
                         names:
00000EEC                     TUPLE: (
00000EF1                         STR: 'baseDamage' (0A 00 00 00 62 61 73 65 44 61 6D 61 67 65),
00000F00                         STR: 'calcDamageWithGun' (11 00 00 00 63 61 6C 63 44 61 6D 61 67 65 57 69 74 68 47 75 6E),
00000F16                         STR: 'iWeaponBaseDamage' (11 00 00 00 69 57 65 61 70 6F 6E 42 61 73 65 44 61 6D 61 67 65),
00000F2C                         STR: 'iWeaponDamageRange' (12 00 00 00 69 57 65 61 70 6F 6E 44 61 6D 61 67 65 52 61 6E 67 65),
00000F43                         STR: 'eTacticType' (0B 00 00 00 65 54 61 63 74 69 63 54 79 70 65),
00000F53                         STR: 'CU' (02 00 00 00 43 55),
00000F5A                         STR: 'outputCombatDebugMessageOnMatch' (1F 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 4F 6E 4D 61 74 63 68),
00000F7E                         STR: 'int' (03 00 00 00 69 6E 74),
00000F86                         STR: 'float' (05 00 00 00 66 6C 6F 61 74),
00000F90                         STR: 'damageTypeInfluence' (13 00 00 00 64 61 6D 61 67 65 54 79 70 65 49 6E 66 6C 75 65 6E 63 65),
00000FA8                         STR: 'bAddRandGaussian' (10 00 00 00 62 41 64 64 52 61 6E 64 47 61 75 73 73 69 61 6E),
00000FBD                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
00000FCB                         STR: 'getGaussianRandomClamped' (18 00 00 00 67 65 74 47 61 75 73 73 69 61 6E 52 61 6E 64 6F 6D 43 6C 61 6D 70 65 64),
00000FE8                         STR: 'iBonuses' (08 00 00 00 69 42 6F 6E 75 73 65 73),
00000FF5                         STR: 'damage_total' (0C 00 00 00 64 61 6D 61 67 65 5F 74 6F 74 61 6C),
00001006                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
00001023                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
00001032                         STR: 'FreeFireScalar' (0E 00 00 00 46 72 65 65 46 69 72 65 53 63 61 6C 61 72),
00001045                         STR: 'GetTacticDamageMod' (12 00 00 00 47 65 74 54 61 63 74 69 63 44 61 6D 61 67 65 4D 6F 64),
0000105C                         STR: 'tacticDamagePercentMod' (16 00 00 00 74 61 63 74 69 63 44 61 6D 61 67 65 50 65 72 63 65 6E 74 4D 6F 64),
00001077                         STR: 'isEnergizedTactic' (11 00 00 00 69 73 45 6E 65 72 67 69 7A 65 64 54 61 63 74 69 63),
0000108D                         STR: 'isPreciseBlows' (0E 00 00 00 69 73 50 72 65 63 69 73 65 42 6C 6F 77 73),
000010A0                         STR: 'fWeaponSpeed' (0C 00 00 00 66 57 65 61 70 6F 6E 53 70 65 65 64)
                             )
                         varnames:
000010B1                     TUPLE: (
000010B6                         STR: 'iBonuses' (08 00 00 00 69 42 6F 6E 75 73 65 73),
000010C3                         STR: 'damageTypeInfluence' (13 00 00 00 64 61 6D 61 67 65 54 79 70 65 49 6E 66 6C 75 65 6E 63 65),
000010DB                         STR: 'iWeaponBaseDamage' (11 00 00 00 69 57 65 61 70 6F 6E 42 61 73 65 44 61 6D 61 67 65),
000010F1                         STR: 'iWeaponDamageRange' (12 00 00 00 69 57 65 61 70 6F 6E 44 61 6D 61 67 65 52 61 6E 67 65),
00001108                         STR: 'fWeaponSpeed' (0C 00 00 00 66 57 65 61 70 6F 6E 53 70 65 65 64),
00001119                         STR: 'isEnergizedTactic' (11 00 00 00 69 73 45 6E 65 72 67 69 7A 65 64 54 61 63 74 69 63),
0000112F                         STR: 'isPreciseBlows' (0E 00 00 00 69 73 50 72 65 63 69 73 65 42 6C 6F 77 73),
00001142                         STR: 'eTacticType' (0B 00 00 00 65 54 61 63 74 69 63 54 79 70 65),
00001152                         STR: 'bAddRandGaussian' (10 00 00 00 62 41 64 64 52 61 6E 64 47 61 75 73 73 69 61 6E),
00001167                         STR: 'tacticDamagePercentMod' (16 00 00 00 74 61 63 74 69 63 44 61 6D 61 67 65 50 65 72 63 65 6E 74 4D 6F 64),
00001182                         STR: 'damage_total' (0C 00 00 00 64 61 6D 61 67 65 5F 74 6F 74 61 6C),
00001193                         STR: 'baseDamage' (0A 00 00 00 62 61 73 65 44 61 6D 61 67 65)
                             )
                         freevars:
000011A2                     TUPLE: ()
                         cellvars:
000011A7                     TUPLE: ()
                         filename:
000011AC                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat_calculations.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73 2E 70 79)
                         name:
000011FC                     STR: 'GetFreeAttackDamage' (13 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65)
                         firslineno:
00001214                     LONG: 87L (57 00 00 00)
                         lnotab:
00001218                     STR: '\x00\x02\x06\x02\x12\x01\x14\x04\r\x01\x1a\x01!\x04\x07\x01(\x01\x18\x02\n\x01\x1d\x02\r\x01\x14\x03\x0c\x01\x10\x01\x1a\x03\x07\x01\x10\x01\x18\x04\x07\x01\x10\x01\x18\x02\x16\x01\x1a\x02' (32 00 00 00 00 02 06 02 12 01 14 04 0D 01 1A 01 21 04 07 01 28 01 18 02 0A 01 1D 02 0D 01 14 03 0C 01 10 01 1A 03 07 01 10 01 18 04 07 01 10 01 18 02 16 01 1A 02),
0000124F             CODE:
                         argcount:
00001250                     LONG: 6L (06 00 00 00)
                         nlocals:
00001254                     LONG: 9L (09 00 00 00)
                         stacksize:
00001258                     LONG: 6L (06 00 00 00)
                         flags:
0000125C                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001260                     STR: '|\x00\x00}\x08\x00|\x05\x00o@\x00\x01t\x03\x00i\x04\x00|\x08\x00|\x08\x00d\x01\x00\x15|\x08\x00d\x02\x00\x15d\x03\x00|\x08\x00\x14d\x02\x00\x15\x83\x04\x00}\x08\x00t\x05\x00i\x06\x00d\x04\x00|\x08\x00\x16d\x01\x00\x83\x02\x00\x01n\x01\x00\x01|\x08\x00}\x07\x00t\x05\x00i\x08\x00d\x05\x00|\x00\x00|\x07\x00f\x02\x00\x16d\x01\x00\x83\x02\x00\x01|\x07\x00t\t\x00i\n\x009}\x07\x00t\x05\x00i\x08\x00d\x06\x00|\x07\x00\x16d\x01\x00\x83\x02\x00\x01t\x0b\x00|\x04\x00\x83\x01\x00}\x06\x00t\x0e\x00|\x07\x00|\x06\x00\x14\x83\x01\x00}\x07\x00t\x05\x00i\x06\x00d\x07\x00|\x06\x00|\x07\x00f\x02\x00\x16d\x01\x00\x83\x02\x00\x01|\x02\x00o(\x00\x01t\x0e\x00|\x07\x00d\x08\x00\x14\x83\x01\x00}\x07\x00t\x05\x00i\x06\x00d\t\x00|\x07\x00\x16d\x01\x00\x83\x02\x00\x01n\x01\x00\x01|\x03\x00o(\x00\x01t\x0e\x00|\x07\x00d\n\x00\x14\x83\x01\x00}\x07\x00t\x05\x00i\x06\x00d\x0b\x00|\x07\x00\x16d\x01\x00\x83\x02\x00\x01n\x01\x00\x01t\x0e\x00t\x11\x00|\x07\x00\x83\x01\x00|\x01\x00\x14\x83\x01\x00}\x07\x00t\x05\x00i\x06\x00d\x0c\x00|\x01\x00|\x07\x00f\x02\x00\x16d\x01\x00\x83\x02\x00\x01t\x0e\x00|\x07\x00\x83\x01\x00Sd\x00\x00S' (60 01 00 00 7C 00 00 7D 08 00 7C 05 00 6F 40 00 01 74 03 00 69 04 00 7C 08 00 7C 08 00 64 01 00 15 7C 08 00 64 02 00 15 64 03 00 7C 08 00 14 64 02 00 15 83 04 00 7D 08 00 74 05 00 69 06 00 64 04 00 7C 08 00 16 64 01 00 83 02 00 01 6E 01 00 01 7C 08 00 7D 07 00 74 05 00 69 08 00 64 05 00 7C 00 00 7C 07 00 66 02 00 16 64 01 00 83 02 00 01 7C 07 00 74 09 00 69 0A 00 39 7D 07 00 74 05 00 69 08 00 64 06 00 7C 07 00 16 64 01 00 83 02 00 01 74 0B 00 7C 04 00 83 01 00 7D 06 00 74 0E 00 7C 07 00 7C 06 00 14 83 01 00 7D 07 00 74 05 00 69 06 00 64 07 00 7C 06 00 7C 07 00 66 02 00 16 64 01 00 83 02 00 01 7C 02 00 6F 28 00 01 74 0E 00 7C 07 00 64 08 00 14 83 01 00 7D 07 00 74 05 00 69 06 00 64 09 00 7C 07 00 16 64 01 00 83 02 00 01 6E 01 00 01 7C 03 00 6F 28 00 01 74 0E 00 7C 07 00 64 0A 00 14 83 01 00 7D 07 00 74 05 00 69 06 00 64 0B 00 7C 07 00 16 64 01 00 83 02 00 01 6E 01 00 01 74 0E 00 74 11 00 7C 07 00 83 01 00 7C 01 00 14 83 01 00 7D 07 00 74 05 00 69 06 00 64 0C 00 7C 01 00 7C 07 00 66 02 00 16 64 01 00 83 02 00 01 74 0E 00 7C 07 00 83 01 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'iBonuses'
                             00000003     7D - STORE_FAST          'baseDamage'
                             00000006     7C - LOAD_FAST           'bAddRandGaussian'
                             00000009     6F - JUMP_IF_FALSE       -> 0000004C
                             0000000C     01 - POP_TOP             
                             0000000D     74 - LOAD_GLOBAL         'discovery'
                             00000010     69 - LOAD_ATTR           'getGaussianRandomClamped'
                             00000013     7C - LOAD_FAST           'baseDamage'
                             00000016     7C - LOAD_FAST           'baseDamage'
                             00000019     64 - LOAD_CONST          10
                             0000001C     15 - BINARY_DIVIDE       
                             0000001D     7C - LOAD_FAST           'baseDamage'
                             00000020     64 - LOAD_CONST          3
                             00000023     15 - BINARY_DIVIDE       
                             00000024     64 - LOAD_CONST          4
                             00000027     7C - LOAD_FAST           'baseDamage'
                             0000002A     14 - BINARY_MULTIPLY     
                             0000002B     64 - LOAD_CONST          3
                             0000002E     15 - BINARY_DIVIDE       
                             0000002F     83 - CALL_FUNCTION       r0004
                             00000032     7D - STORE_FAST          'baseDamage'
                             00000035     74 - LOAD_GLOBAL         'CU'
                             00000038     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             0000003B     64 - LOAD_CONST          'GetFreeAttackDamageMelee: new damage with rand: %d'
                             0000003E     7C - LOAD_FAST           'baseDamage'
                             00000041     16 - BINARY_MODULO       
                             00000042     64 - LOAD_CONST          10
                             00000045     83 - CALL_FUNCTION       r0002
                             00000048     01 - POP_TOP             
                             00000049     6E - JUMP_FORWARD        -> 0000004D
                             0000004C     01 - POP_TOP             
                             0000004D     7C - LOAD_FAST           'baseDamage'
                             00000050     7D - STORE_FAST          'damage_total'
                             00000053     74 - LOAD_GLOBAL         'CU'
                             00000056     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000059     64 - LOAD_CONST          'GetFreeAttackDamageMelee: attacker damage: (%dDmgBonus) = %dTotalDmg'
                             0000005C     7C - LOAD_FAST           'iBonuses'
                             0000005F     7C - LOAD_FAST           'damage_total'
                             00000062     66 - BUILD_TUPLE         r0002
                             00000065     16 - BINARY_MODULO       
                             00000066     64 - LOAD_CONST          10
                             00000069     83 - CALL_FUNCTION       r0002
                             0000006C     01 - POP_TOP             
                             0000006D     7C - LOAD_FAST           'damage_total'
                             00000070     74 - LOAD_GLOBAL         'consolevar'
                             00000073     69 - LOAD_ATTR           'MeleeFreeFireScalar'
                             00000076     39 - INPLACE_MULTIPLY    
                             00000077     7D - STORE_FAST          'damage_total'
                             0000007A     74 - LOAD_GLOBAL         'CU'
                             0000007D     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000080     64 - LOAD_CONST          'GetFreeAttackDamageMelee: attacker damage after scalar: %dTotalDmg'
                             00000083     7C - LOAD_FAST           'damage_total'
                             00000086     16 - BINARY_MODULO       
                             00000087     64 - LOAD_CONST          10
                             0000008A     83 - CALL_FUNCTION       r0002
                             0000008D     01 - POP_TOP             
                             0000008E     74 - LOAD_GLOBAL         'GetTacticDamageMod'
                             00000091     7C - LOAD_FAST           'eTacticType'
                             00000094     83 - CALL_FUNCTION       r0001
                             00000097     7D - STORE_FAST          'tacticDamagePercentMod'
                             0000009A     74 - LOAD_GLOBAL         'int'
                             0000009D     7C - LOAD_FAST           'damage_total'
                             000000A0     7C - LOAD_FAST           'tacticDamagePercentMod'
                             000000A3     14 - BINARY_MULTIPLY     
                             000000A4     83 - CALL_FUNCTION       r0001
                             000000A7     7D - STORE_FAST          'damage_total'
                             000000AA     74 - LOAD_GLOBAL         'CU'
                             000000AD     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             000000B0     64 - LOAD_CONST          'GetFreeAttackDamageMelee: damage (after %g tacticMod): %d'
                             000000B3     7C - LOAD_FAST           'tacticDamagePercentMod'
                             000000B6     7C - LOAD_FAST           'damage_total'
                             000000B9     66 - BUILD_TUPLE         r0002
                             000000BC     16 - BINARY_MODULO       
                             000000BD     64 - LOAD_CONST          10
                             000000C0     83 - CALL_FUNCTION       r0002
                             000000C3     01 - POP_TOP             
                             000000C4     7C - LOAD_FAST           'isEnergizedTactic'
                             000000C7     6F - JUMP_IF_FALSE       -> 000000F2
                             000000CA     01 - POP_TOP             
                             000000CB     74 - LOAD_GLOBAL         'int'
                             000000CE     7C - LOAD_FAST           'damage_total'
                             000000D1     64 - LOAD_CONST          1.1499999999999999
                             000000D4     14 - BINARY_MULTIPLY     
                             000000D5     83 - CALL_FUNCTION       r0001
                             000000D8     7D - STORE_FAST          'damage_total'
                             000000DB     74 - LOAD_GLOBAL         'CU'
                             000000DE     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             000000E1     64 - LOAD_CONST          'GetFreeAttackDamageMelee: Engerzied boost = %d'
                             000000E4     7C - LOAD_FAST           'damage_total'
                             000000E7     16 - BINARY_MODULO       
                             000000E8     64 - LOAD_CONST          10
                             000000EB     83 - CALL_FUNCTION       r0002
                             000000EE     01 - POP_TOP             
                             000000EF     6E - JUMP_FORWARD        -> 000000F3
                             000000F2     01 - POP_TOP             
                             000000F3     7C - LOAD_FAST           'isPreciseBlows'
                             000000F6     6F - JUMP_IF_FALSE       -> 00000121
                             000000F9     01 - POP_TOP             
                             000000FA     74 - LOAD_GLOBAL         'int'
                             000000FD     7C - LOAD_FAST           'damage_total'
                             00000100     64 - LOAD_CONST          0.84999999999999998
                             00000103     14 - BINARY_MULTIPLY     
                             00000104     83 - CALL_FUNCTION       r0001
                             00000107     7D - STORE_FAST          'damage_total'
                             0000010A     74 - LOAD_GLOBAL         'CU'
                             0000010D     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000110     64 - LOAD_CONST          'GetFreeAttackDamageMelee: Percise blows deboost = %d'
                             00000113     7C - LOAD_FAST           'damage_total'
                             00000116     16 - BINARY_MODULO       
                             00000117     64 - LOAD_CONST          10
                             0000011A     83 - CALL_FUNCTION       r0002
                             0000011D     01 - POP_TOP             
                             0000011E     6E - JUMP_FORWARD        -> 00000122
                             00000121     01 - POP_TOP             
                             00000122     74 - LOAD_GLOBAL         'int'
                             00000125     74 - LOAD_GLOBAL         'float'
                             00000128     7C - LOAD_FAST           'damage_total'
                             0000012B     83 - CALL_FUNCTION       r0001
                             0000012E     7C - LOAD_FAST           'fWeaponSpeed'
                             00000131     14 - BINARY_MULTIPLY     
                             00000132     83 - CALL_FUNCTION       r0001
                             00000135     7D - STORE_FAST          'damage_total'
                             00000138     74 - LOAD_GLOBAL         'CU'
                             0000013B     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             0000013E     64 - LOAD_CONST          'GetFreeAttackDamageMelee: damage (after %g weapon speed): %d'
                             00000141     7C - LOAD_FAST           'fWeaponSpeed'
                             00000144     7C - LOAD_FAST           'damage_total'
                             00000147     66 - BUILD_TUPLE         r0002
                             0000014A     16 - BINARY_MODULO       
                             0000014B     64 - LOAD_CONST          10
                             0000014E     83 - CALL_FUNCTION       r0002
                             00000151     01 - POP_TOP             
                             00000152     74 - LOAD_GLOBAL         'int'
                             00000155     7C - LOAD_FAST           'damage_total'
                             00000158     83 - CALL_FUNCTION       r0001
                             0000015B     53 - RETURN_VALUE        
                             0000015C     64 - LOAD_CONST          None
                             0000015F     53 - RETURN_VALUE        
                         consts:
000013C5                     TUPLE: (
000013CA                         None (4E),
000013CB                         INT: 10 (0A 00 00 00),
000013D0                         INT: 3 (03 00 00 00),
000013D5                         INT: 4 (04 00 00 00),
000013DA                         STR: 'GetFreeAttackDamageMelee: new damage with rand: %d' (32 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65 4D 65 6C 65 65 3A 20 6E 65 77 20 64 61 6D 61 67 65 20 77 69 74 68 20 72 61 6E 64 3A 20 25 64),
00001411                         STR: 'GetFreeAttackDamageMelee: attacker damage: (%dDmgBonus) = %dTotalDmg' (44 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65 4D 65 6C 65 65 3A 20 61 74 74 61 63 6B 65 72 20 64 61 6D 61 67 65 3A 20 28 25 64 44 6D 67 42 6F 6E 75 73 29 20 3D 20 25 64 54 6F 74 61 6C 44 6D 67),
0000145A                         STR: 'GetFreeAttackDamageMelee: attacker damage after scalar: %dTotalDmg' (42 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65 4D 65 6C 65 65 3A 20 61 74 74 61 63 6B 65 72 20 64 61 6D 61 67 65 20 61 66 74 65 72 20 73 63 61 6C 61 72 3A 20 25 64 54 6F 74 61 6C 44 6D 67),
000014A1                         STR: 'GetFreeAttackDamageMelee: damage (after %g tacticMod): %d' (39 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65 4D 65 6C 65 65 3A 20 64 61 6D 61 67 65 20 28 61 66 74 65 72 20 25 67 20 74 61 63 74 69 63 4D 6F 64 29 3A 20 25 64),
000014DF                         FLOAT: 1.1499999999999999 (12 31 2E 31 34 39 39 39 39 39 39 39 39 39 39 39 39 39 39),
000014F3                         STR: 'GetFreeAttackDamageMelee: Engerzied boost = %d' (2E 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65 4D 65 6C 65 65 3A 20 45 6E 67 65 72 7A 69 65 64 20 62 6F 6F 73 74 20 3D 20 25 64),
00001526                         FLOAT: 0.84999999999999998 (13 30 2E 38 34 39 39 39 39 39 39 39 39 39 39 39 39 39 39 38),
0000153B                         STR: 'GetFreeAttackDamageMelee: Percise blows deboost = %d' (34 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65 4D 65 6C 65 65 3A 20 50 65 72 63 69 73 65 20 62 6C 6F 77 73 20 64 65 62 6F 6F 73 74 20 3D 20 25 64),
00001574                         STR: 'GetFreeAttackDamageMelee: damage (after %g weapon speed): %d' (3C 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65 4D 65 6C 65 65 3A 20 64 61 6D 61 67 65 20 28 61 66 74 65 72 20 25 67 20 77 65 61 70 6F 6E 20 73 70 65 65 64 29 3A 20 25 64)
                             )
                         names:
000015B5                     TUPLE: (
000015BA                         STR: 'iBonuses' (08 00 00 00 69 42 6F 6E 75 73 65 73),
000015C7                         STR: 'baseDamage' (0A 00 00 00 62 61 73 65 44 61 6D 61 67 65),
000015D6                         STR: 'bAddRandGaussian' (10 00 00 00 62 41 64 64 52 61 6E 64 47 61 75 73 73 69 61 6E),
000015EB                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
000015F9                         STR: 'getGaussianRandomClamped' (18 00 00 00 67 65 74 47 61 75 73 73 69 61 6E 52 61 6E 64 6F 6D 43 6C 61 6D 70 65 64),
00001616                         STR: 'CU' (02 00 00 00 43 55),
0000161D                         STR: 'outputCombatDebugMessageOnMatch' (1F 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 4F 6E 4D 61 74 63 68),
00001641                         STR: 'damage_total' (0C 00 00 00 64 61 6D 61 67 65 5F 74 6F 74 61 6C),
00001652                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
0000166F                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
0000167E                         STR: 'MeleeFreeFireScalar' (13 00 00 00 4D 65 6C 65 65 46 72 65 65 46 69 72 65 53 63 61 6C 61 72),
00001696                         STR: 'GetTacticDamageMod' (12 00 00 00 47 65 74 54 61 63 74 69 63 44 61 6D 61 67 65 4D 6F 64),
000016AD                         STR: 'eTacticType' (0B 00 00 00 65 54 61 63 74 69 63 54 79 70 65),
000016BD                         STR: 'tacticDamagePercentMod' (16 00 00 00 74 61 63 74 69 63 44 61 6D 61 67 65 50 65 72 63 65 6E 74 4D 6F 64),
000016D8                         STR: 'int' (03 00 00 00 69 6E 74),
000016E0                         STR: 'isEnergizedTactic' (11 00 00 00 69 73 45 6E 65 72 67 69 7A 65 64 54 61 63 74 69 63),
000016F6                         STR: 'isPreciseBlows' (0E 00 00 00 69 73 50 72 65 63 69 73 65 42 6C 6F 77 73),
00001709                         STR: 'float' (05 00 00 00 66 6C 6F 61 74),
00001713                         STR: 'fWeaponSpeed' (0C 00 00 00 66 57 65 61 70 6F 6E 53 70 65 65 64)
                             )
                         varnames:
00001724                     TUPLE: (
00001729                         STR: 'iBonuses' (08 00 00 00 69 42 6F 6E 75 73 65 73),
00001736                         STR: 'fWeaponSpeed' (0C 00 00 00 66 57 65 61 70 6F 6E 53 70 65 65 64),
00001747                         STR: 'isEnergizedTactic' (11 00 00 00 69 73 45 6E 65 72 67 69 7A 65 64 54 61 63 74 69 63),
0000175D                         STR: 'isPreciseBlows' (0E 00 00 00 69 73 50 72 65 63 69 73 65 42 6C 6F 77 73),
00001770                         STR: 'eTacticType' (0B 00 00 00 65 54 61 63 74 69 63 54 79 70 65),
00001780                         STR: 'bAddRandGaussian' (10 00 00 00 62 41 64 64 52 61 6E 64 47 61 75 73 73 69 61 6E),
00001795                         STR: 'tacticDamagePercentMod' (16 00 00 00 74 61 63 74 69 63 44 61 6D 61 67 65 50 65 72 63 65 6E 74 4D 6F 64),
000017B0                         STR: 'damage_total' (0C 00 00 00 64 61 6D 61 67 65 5F 74 6F 74 61 6C),
000017C1                         STR: 'baseDamage' (0A 00 00 00 62 61 73 65 44 61 6D 61 67 65)
                             )
                         freevars:
000017D0                     TUPLE: ()
                         cellvars:
000017D5                     TUPLE: ()
                         filename:
000017DA                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat_calculations.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73 2E 70 79)
                         name:
0000182A                     STR: 'GetFreeAttackDamageMelee' (18 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65 4D 65 6C 65 65)
                         firslineno:
00001847                     LONG: 142L (8E 00 00 00)
                         lnotab:
0000184B                     STR: '\x00\x02\x06\x03\x07\x01(\x01\x18\x02\x06\x01\x1a\x03\r\x01\x14\x03\x0c\x01\x10\x01\x1a\x03\x07\x01\x10\x01\x18\x03\x07\x01\x10\x01\x18\x02\x16\x01\x1a\x02' (28 00 00 00 00 02 06 03 07 01 28 01 18 02 06 01 1A 03 0D 01 14 03 0C 01 10 01 1A 03 07 01 10 01 18 03 07 01 10 01 18 02 16 01 1A 02),
00001878             INT: 1 (01 00 00 00),
0000187D             CODE:
                         argcount:
0000187E                     LONG: 11L (0B 00 00 00)
                         nlocals:
00001882                     LONG: 20L (14 00 00 00)
                         stacksize:
00001886                     LONG: 6L (06 00 00 00)
                         flags:
0000188A                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000188E                     STR: 'd\x01\x00}\x11\x00t\x01\x00i\x02\x00d\x02\x00d\x03\x00\x83\x02\x00\x01t\x01\x00i\x03\x00d\x04\x00|\x11\x00\x16d\x03\x00\x83\x02\x00\x01t\x01\x00i\x04\x00|\x02\x00\x83\x01\x00oj\x00\x01t\x06\x00|\x03\x00|\x04\x00|\x05\x00\x83\x03\x00}\x11\x00t\x01\x00i\x02\x00d\x05\x00|\x03\x00|\x04\x00|\x11\x00f\x03\x00\x16d\x03\x00\x83\x02\x00\x01|\x11\x00t\n\x00t\x0b\x00|\x11\x00\x83\x01\x00|\x01\x00\x14\x83\x01\x007}\x11\x00t\x01\x00i\x03\x00d\x06\x00|\x03\x00|\x01\x00|\x11\x00f\x03\x00\x16d\x03\x00\x83\x02\x00\x01n\x01\x00\x01t\x01\x00i\x03\x00d\x07\x00|\x11\x00\x16d\x03\x00\x83\x02\x00\x01|\x07\x00}\x0e\x00|\x00\x00}\r\x00d\x01\x00}\x10\x00|\t\x00o\x1e\x00\x01t\x01\x00i\x03\x00d\x08\x00d\x03\x00\x83\x02\x00\x01|\x0e\x00d\t\x007}\x0e\x00n\x01\x00\x01|\x08\x00o\x1e\x00\x01t\x01\x00i\x03\x00d\n\x00d\x03\x00\x83\x02\x00\x01|\x0e\x00d\t\x008}\x0e\x00n\x01\x00\x01|\x11\x00}\x10\x00|\x11\x00|\r\x007}\x11\x00t\n\x00t\x0b\x00|\x11\x00\x83\x01\x00|\x0e\x00\x14\x83\x01\x00}\x11\x00t\x01\x00i\x03\x00d\x0b\x00|\x10\x00|\r\x00|\x0e\x00|\x11\x00f\x04\x00\x16d\x03\x00\x83\x02\x00\x01|\x06\x00oX\x00\x01|\x11\x00d\x03\x00\x15}\x13\x00|\x11\x00d\x0c\x00\x15}\x0f\x00d\r\x00|\x11\x00\x14d\x0c\x00\x15}\x0b\x00|\x11\x00}\x0c\x00t\x19\x00i\x1a\x00|\x0c\x00|\x13\x00|\x0f\x00|\x0b\x00\x83\x04\x00}\x11\x00t\x01\x00i\x03\x00d\x0e\x00|\x11\x00\x16d\x03\x00\x83\x02\x00\x01n\x01\x00\x01t\x1b\x00|\x05\x00\x83\x01\x00}\x12\x00t\n\x00|\x11\x00|\x12\x00\x14\x83\x01\x00}\x11\x00t\x01\x00i\x03\x00d\x0f\x00|\x12\x00|\x11\x00f\x02\x00\x16d\x03\x00\x83\x02\x00\x01t\n\x00t\x0b\x00|\x11\x00\x83\x01\x00d\x10\x00\x14\x83\x01\x00}\x11\x00t\x01\x00i\x03\x00d\x11\x00d\x10\x00|\x11\x00f\x02\x00\x16d\x03\x00\x83\x02\x00\x01|\x11\x00Sd\x00\x00S' (27 02 00 00 64 01 00 7D 11 00 74 01 00 69 02 00 64 02 00 64 03 00 83 02 00 01 74 01 00 69 03 00 64 04 00 7C 11 00 16 64 03 00 83 02 00 01 74 01 00 69 04 00 7C 02 00 83 01 00 6F 6A 00 01 74 06 00 7C 03 00 7C 04 00 7C 05 00 83 03 00 7D 11 00 74 01 00 69 02 00 64 05 00 7C 03 00 7C 04 00 7C 11 00 66 03 00 16 64 03 00 83 02 00 01 7C 11 00 74 0A 00 74 0B 00 7C 11 00 83 01 00 7C 01 00 14 83 01 00 37 7D 11 00 74 01 00 69 03 00 64 06 00 7C 03 00 7C 01 00 7C 11 00 66 03 00 16 64 03 00 83 02 00 01 6E 01 00 01 74 01 00 69 03 00 64 07 00 7C 11 00 16 64 03 00 83 02 00 01 7C 07 00 7D 0E 00 7C 00 00 7D 0D 00 64 01 00 7D 10 00 7C 09 00 6F 1E 00 01 74 01 00 69 03 00 64 08 00 64 03 00 83 02 00 01 7C 0E 00 64 09 00 37 7D 0E 00 6E 01 00 01 7C 08 00 6F 1E 00 01 74 01 00 69 03 00 64 0A 00 64 03 00 83 02 00 01 7C 0E 00 64 09 00 38 7D 0E 00 6E 01 00 01 7C 11 00 7D 10 00 7C 11 00 7C 0D 00 37 7D 11 00 74 0A 00 74 0B 00 7C 11 00 83 01 00 7C 0E 00 14 83 01 00 7D 11 00 74 01 00 69 03 00 64 0B 00 7C 10 00 7C 0D 00 7C 0E 00 7C 11 00 66 04 00 16 64 03 00 83 02 00 01 7C 06 00 6F 58 00 01 7C 11 00 64 03 00 15 7D 13 00 7C 11 00 64 0C 00 15 7D 0F 00 64 0D 00 7C 11 00 14 64 0C 00 15 7D 0B 00 7C 11 00 7D 0C 00 74 19 00 69 1A 00 7C 0C 00 7C 13 00 7C 0F 00 7C 0B 00 83 04 00 7D 11 00 74 01 00 69 03 00 64 0E 00 7C 11 00 16 64 03 00 83 02 00 01 6E 01 00 01 74 1B 00 7C 05 00 83 01 00 7D 12 00 74 0A 00 7C 11 00 7C 12 00 14 83 01 00 7D 11 00 74 01 00 69 03 00 64 0F 00 7C 12 00 7C 11 00 66 02 00 16 64 03 00 83 02 00 01 74 0A 00 74 0B 00 7C 11 00 83 01 00 64 10 00 14 83 01 00 7D 11 00 74 01 00 69 03 00 64 11 00 64 10 00 7C 11 00 66 02 00 16 64 03 00 83 02 00 01 7C 11 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          0
                             00000003     7D - STORE_FAST          'damage_amount'
                             00000006     74 - LOAD_GLOBAL         'CU'
                             00000009     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000000C     64 - LOAD_CONST          '---- begin damage calc -----'
                             0000000F     64 - LOAD_CONST          10
                             00000012     83 - CALL_FUNCTION       r0002
                             00000015     01 - POP_TOP             
                             00000016     74 - LOAD_GLOBAL         'CU'
                             00000019     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             0000001C     64 - LOAD_CONST          'base damage:%d'
                             0000001F     7C - LOAD_FAST           'damage_amount'
                             00000022     16 - BINARY_MODULO       
                             00000023     64 - LOAD_CONST          10
                             00000026     83 - CALL_FUNCTION       r0002
                             00000029     01 - POP_TOP             
                             0000002A     74 - LOAD_GLOBAL         'CU'
                             0000002D     69 - LOAD_ATTR           'isUsingWeapon'
                             00000030     7C - LOAD_FAST           'iWeaponType'
                             00000033     83 - CALL_FUNCTION       r0001
                             00000036     6F - JUMP_IF_FALSE       -> 000000A3
                             00000039     01 - POP_TOP             
                             0000003A     74 - LOAD_GLOBAL         'calcDamageWithGun'
                             0000003D     7C - LOAD_FAST           'iWeaponBaseDamage'
                             00000040     7C - LOAD_FAST           'iWeaponDamageRange'
                             00000043     7C - LOAD_FAST           'eTacticType'
                             00000046     83 - CALL_FUNCTION       r0003
                             00000049     7D - STORE_FAST          'damage_amount'
                             0000004C     74 - LOAD_GLOBAL         'CU'
                             0000004F     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000052     64 - LOAD_CONST          'weapon damage weaponBaseDamage: %d weaponDelta: %d, weaponDamageRoll: %d'
                             00000055     7C - LOAD_FAST           'iWeaponBaseDamage'
                             00000058     7C - LOAD_FAST           'iWeaponDamageRange'
                             0000005B     7C - LOAD_FAST           'damage_amount'
                             0000005E     66 - BUILD_TUPLE         r0003
                             00000061     16 - BINARY_MODULO       
                             00000062     64 - LOAD_CONST          10
                             00000065     83 - CALL_FUNCTION       r0002
                             00000068     01 - POP_TOP             
                             00000069     7C - LOAD_FAST           'damage_amount'
                             0000006C     74 - LOAD_GLOBAL         'int'
                             0000006F     74 - LOAD_GLOBAL         'float'
                             00000072     7C - LOAD_FAST           'damage_amount'
                             00000075     83 - CALL_FUNCTION       r0001
                             00000078     7C - LOAD_FAST           'damageTypeInfluence'
                             0000007B     14 - BINARY_MULTIPLY     
                             0000007C     83 - CALL_FUNCTION       r0001
                             0000007F     37 - INPLACE_ADD         
                             00000080     7D - STORE_FAST          'damage_amount'
                             00000083     74 - LOAD_GLOBAL         'CU'
                             00000086     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000089     64 - LOAD_CONST          'Damage with weapon bonus (weapDmg(%d)*DamageInflu(%g)) = %d'
                             0000008C     7C - LOAD_FAST           'iWeaponBaseDamage'
                             0000008F     7C - LOAD_FAST           'damageTypeInfluence'
                             00000092     7C - LOAD_FAST           'damage_amount'
                             00000095     66 - BUILD_TUPLE         r0003
                             00000098     16 - BINARY_MODULO       
                             00000099     64 - LOAD_CONST          10
                             0000009C     83 - CALL_FUNCTION       r0002
                             0000009F     01 - POP_TOP             
                             000000A0     6E - JUMP_FORWARD        -> 000000A4
                             000000A3     01 - POP_TOP             
                             000000A4     74 - LOAD_GLOBAL         'CU'
                             000000A7     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             000000AA     64 - LOAD_CONST          'damage with gun/martialArt: %d'
                             000000AD     7C - LOAD_FAST           'damage_amount'
                             000000B0     16 - BINARY_MODULO       
                             000000B1     64 - LOAD_CONST          10
                             000000B4     83 - CALL_FUNCTION       r0002
                             000000B7     01 - POP_TOP             
                             000000B8     7C - LOAD_FAST           'defaultMultiplier'
                             000000BB     7D - STORE_FAST          'damage_multiplier'
                             000000BE     7C - LOAD_FAST           'iBonuses'
                             000000C1     7D - STORE_FAST          'damage_adder'
                             000000C4     64 - LOAD_CONST          0
                             000000C7     7D - STORE_FAST          'damage_base'
                             000000CA     7C - LOAD_FAST           'isUsingEnergizedTactic'
                             000000CD     6F - JUMP_IF_FALSE       -> 000000EE
                             000000D0     01 - POP_TOP             
                             000000D1     74 - LOAD_GLOBAL         'CU'
                             000000D4     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             000000D7     64 - LOAD_CONST          'giving energized damage bonus'
                             000000DA     64 - LOAD_CONST          10
                             000000DD     83 - CALL_FUNCTION       r0002
                             000000E0     01 - POP_TOP             
                             000000E1     7C - LOAD_FAST           'damage_multiplier'
                             000000E4     64 - LOAD_CONST          0.14999999999999999
                             000000E7     37 - INPLACE_ADD         
                             000000E8     7D - STORE_FAST          'damage_multiplier'
                             000000EB     6E - JUMP_FORWARD        -> 000000EF
                             000000EE     01 - POP_TOP             
                             000000EF     7C - LOAD_FAST           'isUsingPreciseBlows'
                             000000F2     6F - JUMP_IF_FALSE       -> 00000113
                             000000F5     01 - POP_TOP             
                             000000F6     74 - LOAD_GLOBAL         'CU'
                             000000F9     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             000000FC     64 - LOAD_CONST          'giving precise blows damage penalty'
                             000000FF     64 - LOAD_CONST          10
                             00000102     83 - CALL_FUNCTION       r0002
                             00000105     01 - POP_TOP             
                             00000106     7C - LOAD_FAST           'damage_multiplier'
                             00000109     64 - LOAD_CONST          0.14999999999999999
                             0000010C     38 - INPLACE_SUBTRACT    
                             0000010D     7D - STORE_FAST          'damage_multiplier'
                             00000110     6E - JUMP_FORWARD        -> 00000114
                             00000113     01 - POP_TOP             
                             00000114     7C - LOAD_FAST           'damage_amount'
                             00000117     7D - STORE_FAST          'damage_base'
                             0000011A     7C - LOAD_FAST           'damage_amount'
                             0000011D     7C - LOAD_FAST           'damage_adder'
                             00000120     37 - INPLACE_ADD         
                             00000121     7D - STORE_FAST          'damage_amount'
                             00000124     74 - LOAD_GLOBAL         'int'
                             00000127     74 - LOAD_GLOBAL         'float'
                             0000012A     7C - LOAD_FAST           'damage_amount'
                             0000012D     83 - CALL_FUNCTION       r0001
                             00000130     7C - LOAD_FAST           'damage_multiplier'
                             00000133     14 - BINARY_MULTIPLY     
                             00000134     83 - CALL_FUNCTION       r0001
                             00000137     7D - STORE_FAST          'damage_amount'
                             0000013A     74 - LOAD_GLOBAL         'CU'
                             0000013D     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000140     64 - LOAD_CONST          'damage: (bd:%d + da:%d) * dm:%g = dt%d'
                             00000143     7C - LOAD_FAST           'damage_base'
                             00000146     7C - LOAD_FAST           'damage_adder'
                             00000149     7C - LOAD_FAST           'damage_multiplier'
                             0000014C     7C - LOAD_FAST           'damage_amount'
                             0000014F     66 - BUILD_TUPLE         r0004
                             00000152     16 - BINARY_MODULO       
                             00000153     64 - LOAD_CONST          10
                             00000156     83 - CALL_FUNCTION       r0002
                             00000159     01 - POP_TOP             
                             0000015A     7C - LOAD_FAST           'bAddRandGaussian'
                             0000015D     6F - JUMP_IF_FALSE       -> 000001B8
                             00000160     01 - POP_TOP             
                             00000161     7C - LOAD_FAST           'damage_amount'
                             00000164     64 - LOAD_CONST          10
                             00000167     15 - BINARY_DIVIDE       
                             00000168     7D - STORE_FAST          'stddev'
                             0000016B     7C - LOAD_FAST           'damage_amount'
                             0000016E     64 - LOAD_CONST          3
                             00000171     15 - BINARY_DIVIDE       
                             00000172     7D - STORE_FAST          'absoluteMin'
                             00000175     64 - LOAD_CONST          4
                             00000178     7C - LOAD_FAST           'damage_amount'
                             0000017B     14 - BINARY_MULTIPLY     
                             0000017C     64 - LOAD_CONST          3
                             0000017F     15 - BINARY_DIVIDE       
                             00000180     7D - STORE_FAST          'absoluteMax'
                             00000183     7C - LOAD_FAST           'damage_amount'
                             00000186     7D - STORE_FAST          'avg'
                             00000189     74 - LOAD_GLOBAL         'discovery'
                             0000018C     69 - LOAD_ATTR           'getGaussianRandomClamped'
                             0000018F     7C - LOAD_FAST           'avg'
                             00000192     7C - LOAD_FAST           'stddev'
                             00000195     7C - LOAD_FAST           'absoluteMin'
                             00000198     7C - LOAD_FAST           'absoluteMax'
                             0000019B     83 - CALL_FUNCTION       r0004
                             0000019E     7D - STORE_FAST          'damage_amount'
                             000001A1     74 - LOAD_GLOBAL         'CU'
                             000001A4     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             000001A7     64 - LOAD_CONST          'damage with rand: %d'
                             000001AA     7C - LOAD_FAST           'damage_amount'
                             000001AD     16 - BINARY_MODULO       
                             000001AE     64 - LOAD_CONST          10
                             000001B1     83 - CALL_FUNCTION       r0002
                             000001B4     01 - POP_TOP             
                             000001B5     6E - JUMP_FORWARD        -> 000001B9
                             000001B8     01 - POP_TOP             
                             000001B9     74 - LOAD_GLOBAL         'GetTacticDamageMod'
                             000001BC     7C - LOAD_FAST           'eTacticType'
                             000001BF     83 - CALL_FUNCTION       r0001
                             000001C2     7D - STORE_FAST          'tacticDamagePercentMod'
                             000001C5     74 - LOAD_GLOBAL         'int'
                             000001C8     7C - LOAD_FAST           'damage_amount'
                             000001CB     7C - LOAD_FAST           'tacticDamagePercentMod'
                             000001CE     14 - BINARY_MULTIPLY     
                             000001CF     83 - CALL_FUNCTION       r0001
                             000001D2     7D - STORE_FAST          'damage_amount'
                             000001D5     74 - LOAD_GLOBAL         'CU'
                             000001D8     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             000001DB     64 - LOAD_CONST          'damage (after %g tacticMod): %d'
                             000001DE     7C - LOAD_FAST           'tacticDamagePercentMod'
                             000001E1     7C - LOAD_FAST           'damage_amount'
                             000001E4     66 - BUILD_TUPLE         r0002
                             000001E7     16 - BINARY_MODULO       
                             000001E8     64 - LOAD_CONST          10
                             000001EB     83 - CALL_FUNCTION       r0002
                             000001EE     01 - POP_TOP             
                             000001EF     74 - LOAD_GLOBAL         'int'
                             000001F2     74 - LOAD_GLOBAL         'float'
                             000001F5     7C - LOAD_FAST           'damage_amount'
                             000001F8     83 - CALL_FUNCTION       r0001
                             000001FB     64 - LOAD_CONST          4.0
                             000001FE     14 - BINARY_MULTIPLY     
                             000001FF     83 - CALL_FUNCTION       r0001
                             00000202     7D - STORE_FAST          'damage_amount'
                             00000205     74 - LOAD_GLOBAL         'CU'
                             00000208     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             0000020B     64 - LOAD_CONST          'damage (after %g weapon speed): %d'
                             0000020E     64 - LOAD_CONST          4.0
                             00000211     7C - LOAD_FAST           'damage_amount'
                             00000214     66 - BUILD_TUPLE         r0002
                             00000217     16 - BINARY_MODULO       
                             00000218     64 - LOAD_CONST          10
                             0000021B     83 - CALL_FUNCTION       r0002
                             0000021E     01 - POP_TOP             
                             0000021F     7C - LOAD_FAST           'damage_amount'
                             00000222     53 - RETURN_VALUE        
                             00000223     64 - LOAD_CONST          None
                             00000226     53 - RETURN_VALUE        
                         consts:
00001ABA                     TUPLE: (
00001ABF                         None (4E),
00001AC0                         INT: 0 (00 00 00 00),
00001AC5                         STR: '---- begin damage calc -----' (1C 00 00 00 2D 2D 2D 2D 20 62 65 67 69 6E 20 64 61 6D 61 67 65 20 63 61 6C 63 20 2D 2D 2D 2D 2D),
00001AE6                         INT: 10 (0A 00 00 00),
00001AEB                         STR: 'base damage:%d' (0E 00 00 00 62 61 73 65 20 64 61 6D 61 67 65 3A 25 64),
00001AFE                         STR: 'weapon damage weaponBaseDamage: %d weaponDelta: %d, weaponDamageRoll: %d' (48 00 00 00 77 65 61 70 6F 6E 20 64 61 6D 61 67 65 20 77 65 61 70 6F 6E 42 61 73 65 44 61 6D 61 67 65 3A 20 25 64 20 77 65 61 70 6F 6E 44 65 6C 74 61 3A 20 25 64 2C 20 77 65 61 70 6F 6E 44 61 6D 61 67 65 52 6F 6C 6C 3A 20 25 64),
00001B4B                         STR: 'Damage with weapon bonus (weapDmg(%d)*DamageInflu(%g)) = %d' (3B 00 00 00 44 61 6D 61 67 65 20 77 69 74 68 20 77 65 61 70 6F 6E 20 62 6F 6E 75 73 20 28 77 65 61 70 44 6D 67 28 25 64 29 2A 44 61 6D 61 67 65 49 6E 66 6C 75 28 25 67 29 29 20 3D 20 25 64),
00001B8B                         STR: 'damage with gun/martialArt: %d' (1E 00 00 00 64 61 6D 61 67 65 20 77 69 74 68 20 67 75 6E 2F 6D 61 72 74 69 61 6C 41 72 74 3A 20 25 64),
00001BAE                         STR: 'giving energized damage bonus' (1D 00 00 00 67 69 76 69 6E 67 20 65 6E 65 72 67 69 7A 65 64 20 64 61 6D 61 67 65 20 62 6F 6E 75 73),
00001BD0                         FLOAT: 0.14999999999999999 (13 30 2E 31 34 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39),
00001BE5                         STR: 'giving precise blows damage penalty' (23 00 00 00 67 69 76 69 6E 67 20 70 72 65 63 69 73 65 20 62 6C 6F 77 73 20 64 61 6D 61 67 65 20 70 65 6E 61 6C 74 79),
00001C0D                         STR: 'damage: (bd:%d + da:%d) * dm:%g = dt%d' (26 00 00 00 64 61 6D 61 67 65 3A 20 28 62 64 3A 25 64 20 2B 20 64 61 3A 25 64 29 20 2A 20 64 6D 3A 25 67 20 3D 20 64 74 25 64),
00001C38                         INT: 3 (03 00 00 00),
00001C3D                         INT: 4 (04 00 00 00),
00001C42                         STR: 'damage with rand: %d' (14 00 00 00 64 61 6D 61 67 65 20 77 69 74 68 20 72 61 6E 64 3A 20 25 64),
00001C5B                         STR: 'damage (after %g tacticMod): %d' (1F 00 00 00 64 61 6D 61 67 65 20 28 61 66 74 65 72 20 25 67 20 74 61 63 74 69 63 4D 6F 64 29 3A 20 25 64),
00001C7F                         FLOAT: 4.0 (03 34 2E 30),
00001C84                         STR: 'damage (after %g weapon speed): %d' (22 00 00 00 64 61 6D 61 67 65 20 28 61 66 74 65 72 20 25 67 20 77 65 61 70 6F 6E 20 73 70 65 65 64 29 3A 20 25 64)
                             )
                         names:
00001CAB                     TUPLE: (
00001CB0                         STR: 'damage_amount' (0D 00 00 00 64 61 6D 61 67 65 5F 61 6D 6F 75 6E 74),
00001CC2                         STR: 'CU' (02 00 00 00 43 55),
00001CC9                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
00001CE6                         STR: 'outputCombatDebugMessageOnMatch' (1F 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 4F 6E 4D 61 74 63 68),
00001D0A                         STR: 'isUsingWeapon' (0D 00 00 00 69 73 55 73 69 6E 67 57 65 61 70 6F 6E),
00001D1C                         STR: 'iWeaponType' (0B 00 00 00 69 57 65 61 70 6F 6E 54 79 70 65),
00001D2C                         STR: 'calcDamageWithGun' (11 00 00 00 63 61 6C 63 44 61 6D 61 67 65 57 69 74 68 47 75 6E),
00001D42                         STR: 'iWeaponBaseDamage' (11 00 00 00 69 57 65 61 70 6F 6E 42 61 73 65 44 61 6D 61 67 65),
00001D58                         STR: 'iWeaponDamageRange' (12 00 00 00 69 57 65 61 70 6F 6E 44 61 6D 61 67 65 52 61 6E 67 65),
00001D6F                         STR: 'eTacticType' (0B 00 00 00 65 54 61 63 74 69 63 54 79 70 65),
00001D7F                         STR: 'int' (03 00 00 00 69 6E 74),
00001D87                         STR: 'float' (05 00 00 00 66 6C 6F 61 74),
00001D91                         STR: 'damageTypeInfluence' (13 00 00 00 64 61 6D 61 67 65 54 79 70 65 49 6E 66 6C 75 65 6E 63 65),
00001DA9                         STR: 'defaultMultiplier' (11 00 00 00 64 65 66 61 75 6C 74 4D 75 6C 74 69 70 6C 69 65 72),
00001DBF                         STR: 'damage_multiplier' (11 00 00 00 64 61 6D 61 67 65 5F 6D 75 6C 74 69 70 6C 69 65 72),
00001DD5                         STR: 'iBonuses' (08 00 00 00 69 42 6F 6E 75 73 65 73),
00001DE2                         STR: 'damage_adder' (0C 00 00 00 64 61 6D 61 67 65 5F 61 64 64 65 72),
00001DF3                         STR: 'damage_base' (0B 00 00 00 64 61 6D 61 67 65 5F 62 61 73 65),
00001E03                         STR: 'isUsingEnergizedTactic' (16 00 00 00 69 73 55 73 69 6E 67 45 6E 65 72 67 69 7A 65 64 54 61 63 74 69 63),
00001E1E                         STR: 'isUsingPreciseBlows' (13 00 00 00 69 73 55 73 69 6E 67 50 72 65 63 69 73 65 42 6C 6F 77 73),
00001E36                         STR: 'bAddRandGaussian' (10 00 00 00 62 41 64 64 52 61 6E 64 47 61 75 73 73 69 61 6E),
00001E4B                         STR: 'stddev' (06 00 00 00 73 74 64 64 65 76),
00001E56                         STR: 'absoluteMin' (0B 00 00 00 61 62 73 6F 6C 75 74 65 4D 69 6E),
00001E66                         STR: 'absoluteMax' (0B 00 00 00 61 62 73 6F 6C 75 74 65 4D 61 78),
00001E76                         STR: 'avg' (03 00 00 00 61 76 67),
00001E7E                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
00001E8C                         STR: 'getGaussianRandomClamped' (18 00 00 00 67 65 74 47 61 75 73 73 69 61 6E 52 61 6E 64 6F 6D 43 6C 61 6D 70 65 64),
00001EA9                         STR: 'GetTacticDamageMod' (12 00 00 00 47 65 74 54 61 63 74 69 63 44 61 6D 61 67 65 4D 6F 64),
00001EC0                         STR: 'tacticDamagePercentMod' (16 00 00 00 74 61 63 74 69 63 44 61 6D 61 67 65 50 65 72 63 65 6E 74 4D 6F 64)
                             )
                         varnames:
00001EDB                     TUPLE: (
00001EE0                         STR: 'iBonuses' (08 00 00 00 69 42 6F 6E 75 73 65 73),
00001EED                         STR: 'damageTypeInfluence' (13 00 00 00 64 61 6D 61 67 65 54 79 70 65 49 6E 66 6C 75 65 6E 63 65),
00001F05                         STR: 'iWeaponType' (0B 00 00 00 69 57 65 61 70 6F 6E 54 79 70 65),
00001F15                         STR: 'iWeaponBaseDamage' (11 00 00 00 69 57 65 61 70 6F 6E 42 61 73 65 44 61 6D 61 67 65),
00001F2B                         STR: 'iWeaponDamageRange' (12 00 00 00 69 57 65 61 70 6F 6E 44 61 6D 61 67 65 52 61 6E 67 65),
00001F42                         STR: 'eTacticType' (0B 00 00 00 65 54 61 63 74 69 63 54 79 70 65),
00001F52                         STR: 'bAddRandGaussian' (10 00 00 00 62 41 64 64 52 61 6E 64 47 61 75 73 73 69 61 6E),
00001F67                         STR: 'defaultMultiplier' (11 00 00 00 64 65 66 61 75 6C 74 4D 75 6C 74 69 70 6C 69 65 72),
00001F7D                         STR: 'isUsingPreciseBlows' (13 00 00 00 69 73 55 73 69 6E 67 50 72 65 63 69 73 65 42 6C 6F 77 73),
00001F95                         STR: 'isUsingEnergizedTactic' (16 00 00 00 69 73 55 73 69 6E 67 45 6E 65 72 67 69 7A 65 64 54 61 63 74 69 63),
00001FB0                         STR: 'winnerOpponentCount' (13 00 00 00 77 69 6E 6E 65 72 4F 70 70 6F 6E 65 6E 74 43 6F 75 6E 74),
00001FC8                         STR: 'absoluteMax' (0B 00 00 00 61 62 73 6F 6C 75 74 65 4D 61 78),
00001FD8                         STR: 'avg' (03 00 00 00 61 76 67),
00001FE0                         STR: 'damage_adder' (0C 00 00 00 64 61 6D 61 67 65 5F 61 64 64 65 72),
00001FF1                         STR: 'damage_multiplier' (11 00 00 00 64 61 6D 61 67 65 5F 6D 75 6C 74 69 70 6C 69 65 72),
00002007                         STR: 'absoluteMin' (0B 00 00 00 61 62 73 6F 6C 75 74 65 4D 69 6E),
00002017                         STR: 'damage_base' (0B 00 00 00 64 61 6D 61 67 65 5F 62 61 73 65),
00002027                         STR: 'damage_amount' (0D 00 00 00 64 61 6D 61 67 65 5F 61 6D 6F 75 6E 74),
00002039                         STR: 'tacticDamagePercentMod' (16 00 00 00 74 61 63 74 69 63 44 61 6D 61 67 65 50 65 72 63 65 6E 74 4D 6F 64),
00002054                         STR: 'stddev' (06 00 00 00 73 74 64 64 65 76)
                             )
                         freevars:
0000205F                     TUPLE: ()
                         cellvars:
00002064                     TUPLE: ()
                         filename:
00002069                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat_calculations.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73 2E 70 79)
                         name:
000020B9                     STR: 'GetCloseCombatDamage' (14 00 00 00 47 65 74 43 6C 6F 73 65 43 6F 6D 62 61 74 44 61 6D 61 67 65)
                         firslineno:
000020D2                     LONG: 188L (BC 00 00 00)
                         lnotab:
000020D6                     STR: '\x00\x02\x06\x02\x10\x03\x14\x03\x10\x01\x12\x01\x1d\x01\x1a\x01!\x03\x14\x03\x06\x01\x06\x01\x06\x03\x07\x01\x10\x01\x0e\x03\x07\x01\x10\x01\x0e\x02\x06\x01\n\x01\x16\x02 \x03\x07\x01\n\x01\n\x01\x0e\x01\x06\x02\x18\x01\x18\x03\x0c\x01\x10\x01\x1a\x02\x16\x01\x1a\x02' (46 00 00 00 00 02 06 02 10 03 14 03 10 01 12 01 1D 01 1A 01 21 03 14 03 06 01 06 01 06 03 07 01 10 01 0E 03 07 01 10 01 0E 02 06 01 0A 01 16 02 20 03 07 01 0A 01 0A 01 0E 01 06 02 18 01 18 03 0C 01 10 01 1A 02 16 01 1A 02),
00002121             CODE:
                         argcount:
00002122                     LONG: 7L (07 00 00 00)
                         nlocals:
00002126                     LONG: 11L (0B 00 00 00)
                         stacksize:
0000212A                     LONG: 5L (05 00 00 00)
                         flags:
0000212E                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00002132                     STR: 't\x00\x00|\x03\x00\x83\x01\x00}\x07\x00t\x03\x00|\x01\x00|\x07\x00\x14\x83\x01\x00}\t\x00t\x06\x00i\x07\x00d\x01\x00|\x01\x00|\x07\x00|\t\x00f\x03\x00\x16d\x02\x00\x83\x02\x00\x01|\x04\x00\x0co\n\x00\x01d\x03\x00}\x00\x00n\x01\x00\x01d\x04\x00}\x08\x00|\x06\x00o\x1e\x00\x01t\x06\x00i\x07\x00d\x05\x00d\x02\x00\x83\x02\x00\x01|\x08\x00d\x06\x008}\x08\x00n\x01\x00\x01|\x05\x00o\x1e\x00\x01t\x06\x00i\x07\x00d\x07\x00d\x02\x00\x83\x02\x00\x01|\x08\x00d\x06\x007}\x08\x00n\x01\x00\x01t\x03\x00t\r\x00|\t\x00\x83\x01\x00|\x08\x00\x14\x83\x01\x00}\t\x00t\x0e\x00i\x0f\x00|\t\x00|\x00\x00d\x03\x00\x83\x03\x00}\n\x00t\x06\x00i\x07\x00d\x08\x00|\x00\x00|\n\x00f\x02\x00\x16d\x02\x00\x83\x02\x00\x01|\n\x00Sd\x00\x00S' (E8 00 00 00 74 00 00 7C 03 00 83 01 00 7D 07 00 74 03 00 7C 01 00 7C 07 00 14 83 01 00 7D 09 00 74 06 00 69 07 00 64 01 00 7C 01 00 7C 07 00 7C 09 00 66 03 00 16 64 02 00 83 02 00 01 7C 04 00 0C 6F 0A 00 01 64 03 00 7D 00 00 6E 01 00 01 64 04 00 7D 08 00 7C 06 00 6F 1E 00 01 74 06 00 69 07 00 64 05 00 64 02 00 83 02 00 01 7C 08 00 64 06 00 38 7D 08 00 6E 01 00 01 7C 05 00 6F 1E 00 01 74 06 00 69 07 00 64 07 00 64 02 00 83 02 00 01 7C 08 00 64 06 00 37 7D 08 00 6E 01 00 01 74 03 00 74 0D 00 7C 09 00 83 01 00 7C 08 00 14 83 01 00 7D 09 00 74 0E 00 69 0F 00 7C 09 00 7C 00 00 64 03 00 83 03 00 7D 0A 00 74 06 00 69 07 00 64 08 00 7C 00 00 7C 0A 00 66 02 00 16 64 02 00 83 02 00 01 7C 0A 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'GetTacticCombatTacticsMod'
                             00000003     7C - LOAD_FAST           'eTacticType'
                             00000006     83 - CALL_FUNCTION       r0001
                             00000009     7D - STORE_FAST          'tactic_Multiplier'
                             0000000C     74 - LOAD_GLOBAL         'int'
                             0000000F     7C - LOAD_FAST           'iCombatTacticBonuses'
                             00000012     7C - LOAD_FAST           'tactic_Multiplier'
                             00000015     14 - BINARY_MULTIPLY     
                             00000016     83 - CALL_FUNCTION       r0001
                             00000019     7D - STORE_FAST          'totalTacticBase'
                             0000001C     74 - LOAD_GLOBAL         'CU'
                             0000001F     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000022     64 - LOAD_CONST          'combat tactics %d (after %g tacticMod): %d'
                             00000025     7C - LOAD_FAST           'iCombatTacticBonuses'
                             00000028     7C - LOAD_FAST           'tactic_Multiplier'
                             0000002B     7C - LOAD_FAST           'totalTacticBase'
                             0000002E     66 - BUILD_TUPLE         r0003
                             00000031     16 - BINARY_MODULO       
                             00000032     64 - LOAD_CONST          12
                             00000035     83 - CALL_FUNCTION       r0002
                             00000038     01 - POP_TOP             
                             00000039     7C - LOAD_FAST           'bAddRandGaussian'
                             0000003C     0C - UNARY_NOT           
                             0000003D     6F - JUMP_IF_FALSE       -> 0000004A
                             00000040     01 - POP_TOP             
                             00000041     64 - LOAD_CONST          100
                             00000044     7D - STORE_FAST          'iConsistancyValue'
                             00000047     6E - JUMP_FORWARD        -> 0000004B
                             0000004A     01 - POP_TOP             
                             0000004B     64 - LOAD_CONST          1.0
                             0000004E     7D - STORE_FAST          'damage_multiplier'
                             00000051     7C - LOAD_FAST           'isUsingEnergizedTactic'
                             00000054     6F - JUMP_IF_FALSE       -> 00000075
                             00000057     01 - POP_TOP             
                             00000058     74 - LOAD_GLOBAL         'CU'
                             0000005B     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             0000005E     64 - LOAD_CONST          'giving energized tactic penalty'
                             00000061     64 - LOAD_CONST          12
                             00000064     83 - CALL_FUNCTION       r0002
                             00000067     01 - POP_TOP             
                             00000068     7C - LOAD_FAST           'damage_multiplier'
                             0000006B     64 - LOAD_CONST          0.14999999999999999
                             0000006E     38 - INPLACE_SUBTRACT    
                             0000006F     7D - STORE_FAST          'damage_multiplier'
                             00000072     6E - JUMP_FORWARD        -> 00000076
                             00000075     01 - POP_TOP             
                             00000076     7C - LOAD_FAST           'isUsingPreciseBlows'
                             00000079     6F - JUMP_IF_FALSE       -> 0000009A
                             0000007C     01 - POP_TOP             
                             0000007D     74 - LOAD_GLOBAL         'CU'
                             00000080     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000083     64 - LOAD_CONST          'giving precise blows tactics bonus'
                             00000086     64 - LOAD_CONST          12
                             00000089     83 - CALL_FUNCTION       r0002
                             0000008C     01 - POP_TOP             
                             0000008D     7C - LOAD_FAST           'damage_multiplier'
                             00000090     64 - LOAD_CONST          0.14999999999999999
                             00000093     37 - INPLACE_ADD         
                             00000094     7D - STORE_FAST          'damage_multiplier'
                             00000097     6E - JUMP_FORWARD        -> 0000009B
                             0000009A     01 - POP_TOP             
                             0000009B     74 - LOAD_GLOBAL         'int'
                             0000009E     74 - LOAD_GLOBAL         'float'
                             000000A1     7C - LOAD_FAST           'totalTacticBase'
                             000000A4     83 - CALL_FUNCTION       r0001
                             000000A7     7C - LOAD_FAST           'damage_multiplier'
                             000000AA     14 - BINARY_MULTIPLY     
                             000000AB     83 - CALL_FUNCTION       r0001
                             000000AE     7D - STORE_FAST          'totalTacticBase'
                             000000B1     74 - LOAD_GLOBAL         'combatlib'
                             000000B4     69 - LOAD_ATTR           'getTacticRoll'
                             000000B7     7C - LOAD_FAST           'totalTacticBase'
                             000000BA     7C - LOAD_FAST           'iConsistancyValue'
                             000000BD     64 - LOAD_CONST          100
                             000000C0     83 - CALL_FUNCTION       r0003
                             000000C3     7D - STORE_FAST          'finalTactics'
                             000000C6     74 - LOAD_GLOBAL         'CU'
                             000000C9     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             000000CC     64 - LOAD_CONST          'combat tactics after gaussian(consistancy %d): %d'
                             000000CF     7C - LOAD_FAST           'iConsistancyValue'
                             000000D2     7C - LOAD_FAST           'finalTactics'
                             000000D5     66 - BUILD_TUPLE         r0002
                             000000D8     16 - BINARY_MODULO       
                             000000D9     64 - LOAD_CONST          12
                             000000DC     83 - CALL_FUNCTION       r0002
                             000000DF     01 - POP_TOP             
                             000000E0     7C - LOAD_FAST           'finalTactics'
                             000000E3     53 - RETURN_VALUE        
                             000000E4     64 - LOAD_CONST          None
                             000000E7     53 - RETURN_VALUE        
                         consts:
0000221F                     TUPLE: (
00002224                         None (4E),
00002225                         STR: 'combat tactics %d (after %g tacticMod): %d' (2A 00 00 00 63 6F 6D 62 61 74 20 74 61 63 74 69 63 73 20 25 64 20 28 61 66 74 65 72 20 25 67 20 74 61 63 74 69 63 4D 6F 64 29 3A 20 25 64),
00002254                         INT: 12 (0C 00 00 00),
00002259                         INT: 100 (64 00 00 00),
0000225E                         FLOAT: 1.0 (03 31 2E 30),
00002263                         STR: 'giving energized tactic penalty' (1F 00 00 00 67 69 76 69 6E 67 20 65 6E 65 72 67 69 7A 65 64 20 74 61 63 74 69 63 20 70 65 6E 61 6C 74 79),
00002287                         FLOAT: 0.14999999999999999 (13 30 2E 31 34 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39),
0000229C                         STR: 'giving precise blows tactics bonus' (22 00 00 00 67 69 76 69 6E 67 20 70 72 65 63 69 73 65 20 62 6C 6F 77 73 20 74 61 63 74 69 63 73 20 62 6F 6E 75 73),
000022C3                         STR: 'combat tactics after gaussian(consistancy %d): %d' (31 00 00 00 63 6F 6D 62 61 74 20 74 61 63 74 69 63 73 20 61 66 74 65 72 20 67 61 75 73 73 69 61 6E 28 63 6F 6E 73 69 73 74 61 6E 63 79 20 25 64 29 3A 20 25 64)
                             )
                         names:
000022F9                     TUPLE: (
000022FE                         STR: 'GetTacticCombatTacticsMod' (19 00 00 00 47 65 74 54 61 63 74 69 63 43 6F 6D 62 61 74 54 61 63 74 69 63 73 4D 6F 64),
0000231C                         STR: 'eTacticType' (0B 00 00 00 65 54 61 63 74 69 63 54 79 70 65),
0000232C                         STR: 'tactic_Multiplier' (11 00 00 00 74 61 63 74 69 63 5F 4D 75 6C 74 69 70 6C 69 65 72),
00002342                         STR: 'int' (03 00 00 00 69 6E 74),
0000234A                         STR: 'iCombatTacticBonuses' (14 00 00 00 69 43 6F 6D 62 61 74 54 61 63 74 69 63 42 6F 6E 75 73 65 73),
00002363                         STR: 'totalTacticBase' (0F 00 00 00 74 6F 74 61 6C 54 61 63 74 69 63 42 61 73 65),
00002377                         STR: 'CU' (02 00 00 00 43 55),
0000237E                         STR: 'outputCombatDebugMessageOnMatch' (1F 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 4F 6E 4D 61 74 63 68),
000023A2                         STR: 'bAddRandGaussian' (10 00 00 00 62 41 64 64 52 61 6E 64 47 61 75 73 73 69 61 6E),
000023B7                         STR: 'iConsistancyValue' (11 00 00 00 69 43 6F 6E 73 69 73 74 61 6E 63 79 56 61 6C 75 65),
000023CD                         STR: 'damage_multiplier' (11 00 00 00 64 61 6D 61 67 65 5F 6D 75 6C 74 69 70 6C 69 65 72),
000023E3                         STR: 'isUsingEnergizedTactic' (16 00 00 00 69 73 55 73 69 6E 67 45 6E 65 72 67 69 7A 65 64 54 61 63 74 69 63),
000023FE                         STR: 'isUsingPreciseBlows' (13 00 00 00 69 73 55 73 69 6E 67 50 72 65 63 69 73 65 42 6C 6F 77 73),
00002416                         STR: 'float' (05 00 00 00 66 6C 6F 61 74),
00002420                         STR: 'combatlib' (09 00 00 00 63 6F 6D 62 61 74 6C 69 62),
0000242E                         STR: 'getTacticRoll' (0D 00 00 00 67 65 74 54 61 63 74 69 63 52 6F 6C 6C),
00002440                         STR: 'finalTactics' (0C 00 00 00 66 69 6E 61 6C 54 61 63 74 69 63 73)
                             )
                         varnames:
00002451                     TUPLE: (
00002456                         STR: 'iConsistancyValue' (11 00 00 00 69 43 6F 6E 73 69 73 74 61 6E 63 79 56 61 6C 75 65),
0000246C                         STR: 'iCombatTacticBonuses' (14 00 00 00 69 43 6F 6D 62 61 74 54 61 63 74 69 63 42 6F 6E 75 73 65 73),
00002485                         STR: 'iWeaponType' (0B 00 00 00 69 57 65 61 70 6F 6E 54 79 70 65),
00002495                         STR: 'eTacticType' (0B 00 00 00 65 54 61 63 74 69 63 54 79 70 65),
000024A5                         STR: 'bAddRandGaussian' (10 00 00 00 62 41 64 64 52 61 6E 64 47 61 75 73 73 69 61 6E),
000024BA                         STR: 'isUsingPreciseBlows' (13 00 00 00 69 73 55 73 69 6E 67 50 72 65 63 69 73 65 42 6C 6F 77 73),
000024D2                         STR: 'isUsingEnergizedTactic' (16 00 00 00 69 73 55 73 69 6E 67 45 6E 65 72 67 69 7A 65 64 54 61 63 74 69 63),
000024ED                         STR: 'tactic_Multiplier' (11 00 00 00 74 61 63 74 69 63 5F 4D 75 6C 74 69 70 6C 69 65 72),
00002503                         STR: 'damage_multiplier' (11 00 00 00 64 61 6D 61 67 65 5F 6D 75 6C 74 69 70 6C 69 65 72),
00002519                         STR: 'totalTacticBase' (0F 00 00 00 74 6F 74 61 6C 54 61 63 74 69 63 42 61 73 65),
0000252D                         STR: 'finalTactics' (0C 00 00 00 66 69 6E 61 6C 54 61 63 74 69 63 73)
                             )
                         freevars:
0000253E                     TUPLE: ()
                         cellvars:
00002543                     TUPLE: ()
                         filename:
00002548                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat_calculations.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73 2E 70 79)
                         name:
00002598                     STR: 'GetCombatTacticRoll' (13 00 00 00 47 65 74 43 6F 6D 62 61 74 54 61 63 74 69 63 52 6F 6C 6C)
                         firslineno:
000025B0                     LONG: 258L (02 01 00 00)
                         lnotab:
000025B4                     STR: '\x00\x03\x0c\x01\x10\x01\x1d\x03\x08\x01\n\x02\x06\x02\x07\x01\x10\x01\x0e\x03\x07\x01\x10\x01\x0e\x02\x16\x03\x15\x01\x1a\x02' (20 00 00 00 00 03 0C 01 10 01 1D 03 08 01 0A 02 06 02 07 01 10 01 0E 03 07 01 10 01 0E 02 16 03 15 01 1A 02),
000025D9             CODE:
                         argcount:
000025DA                     LONG: 7L (07 00 00 00)
                         nlocals:
000025DE                     LONG: 10L (0A 00 00 00)
                         stacksize:
000025E2                     LONG: 5L (05 00 00 00)
                         flags:
000025E6                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000025EA                     STR: 't\x00\x00|\x03\x00\x83\x01\x00}\x07\x00t\x03\x00|\x01\x00|\x07\x00\x14\x83\x01\x00}\x08\x00t\x06\x00i\x07\x00d\x01\x00|\x01\x00|\x07\x00|\x08\x00f\x03\x00\x16d\x02\x00\x83\x02\x00\x01|\x04\x00\x0co\n\x00\x01d\x03\x00}\x00\x00n\x01\x00\x01t\n\x00i\x0b\x00|\x08\x00|\x00\x00d\x04\x00\x83\x03\x00}\t\x00t\x06\x00i\x07\x00d\x05\x00|\x00\x00|\t\x00f\x02\x00\x16d\x02\x00\x83\x02\x00\x01|\t\x00Sd\x00\x00S' (82 00 00 00 74 00 00 7C 03 00 83 01 00 7D 07 00 74 03 00 7C 01 00 7C 07 00 14 83 01 00 7D 08 00 74 06 00 69 07 00 64 01 00 7C 01 00 7C 07 00 7C 08 00 66 03 00 16 64 02 00 83 02 00 01 7C 04 00 0C 6F 0A 00 01 64 03 00 7D 00 00 6E 01 00 01 74 0A 00 69 0B 00 7C 08 00 7C 00 00 64 04 00 83 03 00 7D 09 00 74 06 00 69 07 00 64 05 00 7C 00 00 7C 09 00 66 02 00 16 64 02 00 83 02 00 01 7C 09 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'GetTacticDefenseTacticsMod'
                             00000003     7C - LOAD_FAST           'eTacticType'
                             00000006     83 - CALL_FUNCTION       r0001
                             00000009     7D - STORE_FAST          'tactic_Multiplier'
                             0000000C     74 - LOAD_GLOBAL         'int'
                             0000000F     7C - LOAD_FAST           'iDefenseTacticsBonus'
                             00000012     7C - LOAD_FAST           'tactic_Multiplier'
                             00000015     14 - BINARY_MULTIPLY     
                             00000016     83 - CALL_FUNCTION       r0001
                             00000019     7D - STORE_FAST          'totalTacticBase'
                             0000001C     74 - LOAD_GLOBAL         'CU'
                             0000001F     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000022     64 - LOAD_CONST          'defense tactics %d (after %g tacticMod): %d'
                             00000025     7C - LOAD_FAST           'iDefenseTacticsBonus'
                             00000028     7C - LOAD_FAST           'tactic_Multiplier'
                             0000002B     7C - LOAD_FAST           'totalTacticBase'
                             0000002E     66 - BUILD_TUPLE         r0003
                             00000031     16 - BINARY_MODULO       
                             00000032     64 - LOAD_CONST          12
                             00000035     83 - CALL_FUNCTION       r0002
                             00000038     01 - POP_TOP             
                             00000039     7C - LOAD_FAST           'bAddRandGaussian'
                             0000003C     0C - UNARY_NOT           
                             0000003D     6F - JUMP_IF_FALSE       -> 0000004A
                             00000040     01 - POP_TOP             
                             00000041     64 - LOAD_CONST          100
                             00000044     7D - STORE_FAST          'iConsistancyValue'
                             00000047     6E - JUMP_FORWARD        -> 0000004B
                             0000004A     01 - POP_TOP             
                             0000004B     74 - LOAD_GLOBAL         'combatlib'
                             0000004E     69 - LOAD_ATTR           'getTacticRoll'
                             00000051     7C - LOAD_FAST           'totalTacticBase'
                             00000054     7C - LOAD_FAST           'iConsistancyValue'
                             00000057     64 - LOAD_CONST          69
                             0000005A     83 - CALL_FUNCTION       r0003
                             0000005D     7D - STORE_FAST          'finalTactics'
                             00000060     74 - LOAD_GLOBAL         'CU'
                             00000063     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000066     64 - LOAD_CONST          'defense tactics after gaussian(consistancy %d): %d'
                             00000069     7C - LOAD_FAST           'iConsistancyValue'
                             0000006C     7C - LOAD_FAST           'finalTactics'
                             0000006F     66 - BUILD_TUPLE         r0002
                             00000072     16 - BINARY_MODULO       
                             00000073     64 - LOAD_CONST          12
                             00000076     83 - CALL_FUNCTION       r0002
                             00000079     01 - POP_TOP             
                             0000007A     7C - LOAD_FAST           'finalTactics'
                             0000007D     53 - RETURN_VALUE        
                             0000007E     64 - LOAD_CONST          None
                             00000081     53 - RETURN_VALUE        
                         consts:
00002671                     TUPLE: (
00002676                         None (4E),
00002677                         STR: 'defense tactics %d (after %g tacticMod): %d' (2B 00 00 00 64 65 66 65 6E 73 65 20 74 61 63 74 69 63 73 20 25 64 20 28 61 66 74 65 72 20 25 67 20 74 61 63 74 69 63 4D 6F 64 29 3A 20 25 64),
000026A7                         INT: 12 (0C 00 00 00),
000026AC                         INT: 100 (64 00 00 00),
000026B1                         INT: 69 (45 00 00 00),
000026B6                         STR: 'defense tactics after gaussian(consistancy %d): %d' (32 00 00 00 64 65 66 65 6E 73 65 20 74 61 63 74 69 63 73 20 61 66 74 65 72 20 67 61 75 73 73 69 61 6E 28 63 6F 6E 73 69 73 74 61 6E 63 79 20 25 64 29 3A 20 25 64)
                             )
                         names:
000026ED                     TUPLE: (
000026F2                         STR: 'GetTacticDefenseTacticsMod' (1A 00 00 00 47 65 74 54 61 63 74 69 63 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 4D 6F 64),
00002711                         STR: 'eTacticType' (0B 00 00 00 65 54 61 63 74 69 63 54 79 70 65),
00002721                         STR: 'tactic_Multiplier' (11 00 00 00 74 61 63 74 69 63 5F 4D 75 6C 74 69 70 6C 69 65 72),
00002737                         STR: 'int' (03 00 00 00 69 6E 74),
0000273F                         STR: 'iDefenseTacticsBonus' (14 00 00 00 69 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 42 6F 6E 75 73),
00002758                         STR: 'totalTacticBase' (0F 00 00 00 74 6F 74 61 6C 54 61 63 74 69 63 42 61 73 65),
0000276C                         STR: 'CU' (02 00 00 00 43 55),
00002773                         STR: 'outputCombatDebugMessageOnMatch' (1F 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 4F 6E 4D 61 74 63 68),
00002797                         STR: 'bAddRandGaussian' (10 00 00 00 62 41 64 64 52 61 6E 64 47 61 75 73 73 69 61 6E),
000027AC                         STR: 'iConsistancyValue' (11 00 00 00 69 43 6F 6E 73 69 73 74 61 6E 63 79 56 61 6C 75 65),
000027C2                         STR: 'combatlib' (09 00 00 00 63 6F 6D 62 61 74 6C 69 62),
000027D0                         STR: 'getTacticRoll' (0D 00 00 00 67 65 74 54 61 63 74 69 63 52 6F 6C 6C),
000027E2                         STR: 'finalTactics' (0C 00 00 00 66 69 6E 61 6C 54 61 63 74 69 63 73)
                             )
                         varnames:
000027F3                     TUPLE: (
000027F8                         STR: 'iConsistancyValue' (11 00 00 00 69 43 6F 6E 73 69 73 74 61 6E 63 79 56 61 6C 75 65),
0000280E                         STR: 'iDefenseTacticsBonus' (14 00 00 00 69 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 42 6F 6E 75 73),
00002827                         STR: 'iWeaponType' (0B 00 00 00 69 57 65 61 70 6F 6E 54 79 70 65),
00002837                         STR: 'eTacticType' (0B 00 00 00 65 54 61 63 74 69 63 54 79 70 65),
00002847                         STR: 'bAddRandGaussian' (10 00 00 00 62 41 64 64 52 61 6E 64 47 61 75 73 73 69 61 6E),
0000285C                         STR: 'isUsingPowerShot' (10 00 00 00 69 73 55 73 69 6E 67 50 6F 77 65 72 53 68 6F 74),
00002871                         STR: 'isUsingEnergizedTactic' (16 00 00 00 69 73 55 73 69 6E 67 45 6E 65 72 67 69 7A 65 64 54 61 63 74 69 63),
0000288C                         STR: 'tactic_Multiplier' (11 00 00 00 74 61 63 74 69 63 5F 4D 75 6C 74 69 70 6C 69 65 72),
000028A2                         STR: 'totalTacticBase' (0F 00 00 00 74 6F 74 61 6C 54 61 63 74 69 63 42 61 73 65),
000028B6                         STR: 'finalTactics' (0C 00 00 00 66 69 6E 61 6C 54 61 63 74 69 63 73)
                             )
                         freevars:
000028C7                     TUPLE: ()
                         cellvars:
000028CC                     TUPLE: ()
                         filename:
000028D1                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat_calculations.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73 2E 70 79)
                         name:
00002921                     STR: 'GetDefenseTacticRoll' (14 00 00 00 47 65 74 44 65 66 65 6E 73 65 54 61 63 74 69 63 52 6F 6C 6C)
                         firslineno:
0000293A                     LONG: 297L (29 01 00 00)
                         lnotab:
0000293E                     STR: '\x00\x03\x0c\x01\x10\x01\x1d\x03\x08\x01\n\x02\x15\x01\x1a\x02' (10 00 00 00 00 03 0C 01 10 01 1D 03 08 01 0A 02 15 01 1A 02),
00002953             CODE:
                         argcount:
00002954                     LONG: 4L (04 00 00 00)
                         nlocals:
00002958                     LONG: 18L (12 00 00 00)
                         stacksize:
0000295C                     LONG: 6L (06 00 00 00)
                         flags:
00002960                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00002964                     STR: 't\x00\x00i\x01\x00d\x01\x00|\x00\x00|\x01\x00|\x02\x00|\x03\x00f\x04\x00\x16d\x02\x00\x83\x02\x00\x01d\x03\x00}\x04\x00d\x03\x00}\x10\x00d\x03\x00}\t\x00d\x04\x00}\x0b\x00d\x05\x00}\n\x00d\x06\x00}\x05\x00d\x07\x00}\x06\x00|\x06\x00|\x05\x00\x18}\x11\x00d\x08\x00}\x0f\x00d\t\x00}\r\x00d\n\x00}\x07\x00t\x11\x00|\x01\x00\x83\x01\x00t\x11\x00|\x00\x00\x83\x01\x00\x18}\x08\x00|\x08\x00|\n\x00\x14}\x10\x00t\x00\x00i\x01\x00d\x0b\x00|\x08\x00|\x10\x00f\x02\x00\x16d\x02\x00\x83\x02\x00\x01t\x11\x00|\x01\x00\x83\x01\x00|\x0b\x00\x14|\x07\x00\x18}\x0c\x00|\x11\x00|\x0c\x00\x15}\x0e\x00|\x0e\x00t\x11\x00|\x02\x00\x83\x01\x00|\x07\x00\x18\x14|\x05\x00\x17}\t\x00t\x00\x00i\x01\x00d\x0c\x00|\x02\x00|\t\x00f\x02\x00\x16d\x02\x00\x83\x02\x00\x01|\t\x00|\x06\x00j\x04\x00o\x1e\x00\x01|\x06\x00}\t\x00t\x00\x00i\x01\x00d\r\x00|\x06\x00\x16d\x02\x00\x83\x02\x00\x01n\x01\x00\x01|\x10\x00|\t\x00\x17}\x04\x00t\x00\x00i\x01\x00d\x0e\x00|\x10\x00|\t\x00|\x04\x00f\x03\x00\x16d\x02\x00\x83\x02\x00\x01|\x04\x00|\r\x00j\x04\x00o\x1e\x00\x01|\r\x00}\x04\x00t\x00\x00i\x01\x00d\x0f\x00|\r\x00\x16d\x02\x00\x83\x02\x00\x01n,\x00\x01|\x04\x00|\x0f\x00j\x00\x00o\x1e\x00\x01|\x0f\x00}\x04\x00t\x00\x00i\x01\x00d\x0f\x00|\x0f\x00\x16d\x02\x00\x83\x02\x00\x01n\x01\x00\x01|\x04\x00Sd\x00\x00S' (A0 01 00 00 74 00 00 69 01 00 64 01 00 7C 00 00 7C 01 00 7C 02 00 7C 03 00 66 04 00 16 64 02 00 83 02 00 01 64 03 00 7D 04 00 64 03 00 7D 10 00 64 03 00 7D 09 00 64 04 00 7D 0B 00 64 05 00 7D 0A 00 64 06 00 7D 05 00 64 07 00 7D 06 00 7C 06 00 7C 05 00 18 7D 11 00 64 08 00 7D 0F 00 64 09 00 7D 0D 00 64 0A 00 7D 07 00 74 11 00 7C 01 00 83 01 00 74 11 00 7C 00 00 83 01 00 18 7D 08 00 7C 08 00 7C 0A 00 14 7D 10 00 74 00 00 69 01 00 64 0B 00 7C 08 00 7C 10 00 66 02 00 16 64 02 00 83 02 00 01 74 11 00 7C 01 00 83 01 00 7C 0B 00 14 7C 07 00 18 7D 0C 00 7C 11 00 7C 0C 00 15 7D 0E 00 7C 0E 00 74 11 00 7C 02 00 83 01 00 7C 07 00 18 14 7C 05 00 17 7D 09 00 74 00 00 69 01 00 64 0C 00 7C 02 00 7C 09 00 66 02 00 16 64 02 00 83 02 00 01 7C 09 00 7C 06 00 6A 04 00 6F 1E 00 01 7C 06 00 7D 09 00 74 00 00 69 01 00 64 0D 00 7C 06 00 16 64 02 00 83 02 00 01 6E 01 00 01 7C 10 00 7C 09 00 17 7D 04 00 74 00 00 69 01 00 64 0E 00 7C 10 00 7C 09 00 7C 04 00 66 03 00 16 64 02 00 83 02 00 01 7C 04 00 7C 0D 00 6A 04 00 6F 1E 00 01 7C 0D 00 7D 04 00 74 00 00 69 01 00 64 0F 00 7C 0D 00 16 64 02 00 83 02 00 01 6E 2C 00 01 7C 04 00 7C 0F 00 6A 00 00 6F 1E 00 01 7C 0F 00 7D 04 00 74 00 00 69 01 00 64 0F 00 7C 0F 00 16 64 02 00 83 02 00 01 6E 01 00 01 7C 04 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CU'
                             00000003     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000006     64 - LOAD_CONST          'GetDamageReductionValue Input: atkLvl(%d) defLvl(%d) defDmgReduc(%d), dmgAmnt(%d)'
                             00000009     7C - LOAD_FAST           'attackerLvl'
                             0000000C     7C - LOAD_FAST           'defenderLvl'
                             0000000F     7C - LOAD_FAST           'curDamageReduction'
                             00000012     7C - LOAD_FAST           'damageAmount'
                             00000015     66 - BUILD_TUPLE         r0004
                             00000018     16 - BINARY_MODULO       
                             00000019     64 - LOAD_CONST          21
                             0000001C     83 - CALL_FUNCTION       r0002
                             0000001F     01 - POP_TOP             
                             00000020     64 - LOAD_CONST          0.0
                             00000023     7D - STORE_FAST          'fOverallDamageReduction'
                             00000026     64 - LOAD_CONST          0.0
                             00000029     7D - STORE_FAST          'fLevelDifDamageReduction'
                             0000002C     64 - LOAD_CONST          0.0
                             0000002F     7D - STORE_FAST          'fArmorDamageReduction'
                             00000032     64 - LOAD_CONST          4.0
                             00000035     7D - STORE_FAST          'fLevelScale'
                             00000038     64 - LOAD_CONST          0.20000000000000001
                             0000003B     7D - STORE_FAST          'fScalePerLevelDef'
                             0000003E     64 - LOAD_CONST          -0.33000000000000002
                             00000041     7D - STORE_FAST          'fMinArmorReduction'
                             00000044     64 - LOAD_CONST          0.33000000000000002
                             00000047     7D - STORE_FAST          'fMaxArmorReduction'
                             0000004A     7C - LOAD_FAST           'fMaxArmorReduction'
                             0000004D     7C - LOAD_FAST           'fMinArmorReduction'
                             00000050     18 - BINARY_SUBTRACT     
                             00000051     7D - STORE_FAST          'fArmorReductionRange'
                             00000054     64 - LOAD_CONST          -0.90000000000000002
                             00000057     7D - STORE_FAST          'fMinReduction'
                             0000005A     64 - LOAD_CONST          0.90000000000000002
                             0000005D     7D - STORE_FAST          'fMaxReduction'
                             00000060     64 - LOAD_CONST          -20.0
                             00000063     7D - STORE_FAST          'fArmorStartPos'
                             00000066     74 - LOAD_GLOBAL         'float'
                             00000069     7C - LOAD_FAST           'defenderLvl'
                             0000006C     83 - CALL_FUNCTION       r0001
                             0000006F     74 - LOAD_GLOBAL         'float'
                             00000072     7C - LOAD_FAST           'attackerLvl'
                             00000075     83 - CALL_FUNCTION       r0001
                             00000078     18 - BINARY_SUBTRACT     
                             00000079     7D - STORE_FAST          'levelDiff'
                             0000007C     7C - LOAD_FAST           'levelDiff'
                             0000007F     7C - LOAD_FAST           'fScalePerLevelDef'
                             00000082     14 - BINARY_MULTIPLY     
                             00000083     7D - STORE_FAST          'fLevelDifDamageReduction'
                             00000086     74 - LOAD_GLOBAL         'CU'
                             00000089     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             0000008C     64 - LOAD_CONST          'GetDamageReductionValue: LevelDif(%f), LevelReduc(%f)'
                             0000008F     7C - LOAD_FAST           'levelDiff'
                             00000092     7C - LOAD_FAST           'fLevelDifDamageReduction'
                             00000095     66 - BUILD_TUPLE         r0002
                             00000098     16 - BINARY_MODULO       
                             00000099     64 - LOAD_CONST          21
                             0000009C     83 - CALL_FUNCTION       r0002
                             0000009F     01 - POP_TOP             
                             000000A0     74 - LOAD_GLOBAL         'float'
                             000000A3     7C - LOAD_FAST           'defenderLvl'
                             000000A6     83 - CALL_FUNCTION       r0001
                             000000A9     7C - LOAD_FAST           'fLevelScale'
                             000000AC     14 - BINARY_MULTIPLY     
                             000000AD     7C - LOAD_FAST           'fArmorStartPos'
                             000000B0     18 - BINARY_SUBTRACT     
                             000000B1     7D - STORE_FAST          'fTotalRange'
                             000000B4     7C - LOAD_FAST           'fArmorReductionRange'
                             000000B7     7C - LOAD_FAST           'fTotalRange'
                             000000BA     15 - BINARY_DIVIDE       
                             000000BB     7D - STORE_FAST          'fTickSize'
                             000000BE     7C - LOAD_FAST           'fTickSize'
                             000000C1     74 - LOAD_GLOBAL         'float'
                             000000C4     7C - LOAD_FAST           'curDamageReduction'
                             000000C7     83 - CALL_FUNCTION       r0001
                             000000CA     7C - LOAD_FAST           'fArmorStartPos'
                             000000CD     18 - BINARY_SUBTRACT     
                             000000CE     14 - BINARY_MULTIPLY     
                             000000CF     7C - LOAD_FAST           'fMinArmorReduction'
                             000000D2     17 - BINARY_ADD          
                             000000D3     7D - STORE_FAST          'fArmorDamageReduction'
                             000000D6     74 - LOAD_GLOBAL         'CU'
                             000000D9     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             000000DC     64 - LOAD_CONST          'GetDamageReductionValue: defDmgReduc(%d), fArmorDamageReduction(%f)'
                             000000DF     7C - LOAD_FAST           'curDamageReduction'
                             000000E2     7C - LOAD_FAST           'fArmorDamageReduction'
                             000000E5     66 - BUILD_TUPLE         r0002
                             000000E8     16 - BINARY_MODULO       
                             000000E9     64 - LOAD_CONST          21
                             000000EC     83 - CALL_FUNCTION       r0002
                             000000EF     01 - POP_TOP             
                             000000F0     7C - LOAD_FAST           'fArmorDamageReduction'
                             000000F3     7C - LOAD_FAST           'fMaxArmorReduction'
                             000000F6     6A - COMPARE_OP          ">"
                             000000F9     6F - JUMP_IF_FALSE       -> 0000011A
                             000000FC     01 - POP_TOP             
                             000000FD     7C - LOAD_FAST           'fMaxArmorReduction'
                             00000100     7D - STORE_FAST          'fArmorDamageReduction'
                             00000103     74 - LOAD_GLOBAL         'CU'
                             00000106     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000109     64 - LOAD_CONST          'GetDamageReductionValue: Armor capped at %f'
                             0000010C     7C - LOAD_FAST           'fMaxArmorReduction'
                             0000010F     16 - BINARY_MODULO       
                             00000110     64 - LOAD_CONST          21
                             00000113     83 - CALL_FUNCTION       r0002
                             00000116     01 - POP_TOP             
                             00000117     6E - JUMP_FORWARD        -> 0000011B
                             0000011A     01 - POP_TOP             
                             0000011B     7C - LOAD_FAST           'fLevelDifDamageReduction'
                             0000011E     7C - LOAD_FAST           'fArmorDamageReduction'
                             00000121     17 - BINARY_ADD          
                             00000122     7D - STORE_FAST          'fOverallDamageReduction'
                             00000125     74 - LOAD_GLOBAL         'CU'
                             00000128     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             0000012B     64 - LOAD_CONST          'GetDamageReductionValue: levelDmgReduc(%f) + armorDmgReduc(%f) = totalDmgReduc(%f)'
                             0000012E     7C - LOAD_FAST           'fLevelDifDamageReduction'
                             00000131     7C - LOAD_FAST           'fArmorDamageReduction'
                             00000134     7C - LOAD_FAST           'fOverallDamageReduction'
                             00000137     66 - BUILD_TUPLE         r0003
                             0000013A     16 - BINARY_MODULO       
                             0000013B     64 - LOAD_CONST          21
                             0000013E     83 - CALL_FUNCTION       r0002
                             00000141     01 - POP_TOP             
                             00000142     7C - LOAD_FAST           'fOverallDamageReduction'
                             00000145     7C - LOAD_FAST           'fMaxReduction'
                             00000148     6A - COMPARE_OP          ">"
                             0000014B     6F - JUMP_IF_FALSE       -> 0000016C
                             0000014E     01 - POP_TOP             
                             0000014F     7C - LOAD_FAST           'fMaxReduction'
                             00000152     7D - STORE_FAST          'fOverallDamageReduction'
                             00000155     74 - LOAD_GLOBAL         'CU'
                             00000158     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             0000015B     64 - LOAD_CONST          'GetDamageReductionValue: Capped at %f'
                             0000015E     7C - LOAD_FAST           'fMaxReduction'
                             00000161     16 - BINARY_MODULO       
                             00000162     64 - LOAD_CONST          21
                             00000165     83 - CALL_FUNCTION       r0002
                             00000168     01 - POP_TOP             
                             00000169     6E - JUMP_FORWARD        -> 00000198
                             0000016C     01 - POP_TOP             
                             0000016D     7C - LOAD_FAST           'fOverallDamageReduction'
                             00000170     7C - LOAD_FAST           'fMinReduction'
                             00000173     6A - COMPARE_OP          "<"
                             00000176     6F - JUMP_IF_FALSE       -> 00000197
                             00000179     01 - POP_TOP             
                             0000017A     7C - LOAD_FAST           'fMinReduction'
                             0000017D     7D - STORE_FAST          'fOverallDamageReduction'
                             00000180     74 - LOAD_GLOBAL         'CU'
                             00000183     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000186     64 - LOAD_CONST          'GetDamageReductionValue: Capped at %f'
                             00000189     7C - LOAD_FAST           'fMinReduction'
                             0000018C     16 - BINARY_MODULO       
                             0000018D     64 - LOAD_CONST          21
                             00000190     83 - CALL_FUNCTION       r0002
                             00000193     01 - POP_TOP             
                             00000194     6E - JUMP_FORWARD        -> 00000198
                             00000197     01 - POP_TOP             
                             00000198     7C - LOAD_FAST           'fOverallDamageReduction'
                             0000019B     53 - RETURN_VALUE        
                             0000019C     64 - LOAD_CONST          None
                             0000019F     53 - RETURN_VALUE        
                         consts:
00002B09                     TUPLE: (
00002B0E                         None (4E),
00002B0F                         STR: 'GetDamageReductionValue Input: atkLvl(%d) defLvl(%d) defDmgReduc(%d), dmgAmnt(%d)' (51 00 00 00 47 65 74 44 61 6D 61 67 65 52 65 64 75 63 74 69 6F 6E 56 61 6C 75 65 20 49 6E 70 75 74 3A 20 61 74 6B 4C 76 6C 28 25 64 29 20 64 65 66 4C 76 6C 28 25 64 29 20 64 65 66 44 6D 67 52 65 64 75 63 28 25 64 29 2C 20 64 6D 67 41 6D 6E 74 28 25 64 29),
00002B65                         INT: 21 (15 00 00 00),
00002B6A                         FLOAT: 0.0 (03 30 2E 30),
00002B6F                         FLOAT: 4.0 (03 34 2E 30),
00002B74                         FLOAT: 0.20000000000000001 (13 30 2E 32 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 31),
00002B89                         FLOAT: -0.33000000000000002 (14 2D 30 2E 33 33 30 30 30 30 30 30 30 30 30 30 30 30 30 30 32),
00002B9F                         FLOAT: 0.33000000000000002 (13 30 2E 33 33 30 30 30 30 30 30 30 30 30 30 30 30 30 30 32),
00002BB4                         FLOAT: -0.90000000000000002 (14 2D 30 2E 39 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 32),
00002BCA                         FLOAT: 0.90000000000000002 (13 30 2E 39 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 32),
00002BDF                         FLOAT: -20.0 (05 2D 32 30 2E 30),
00002BE6                         STR: 'GetDamageReductionValue: LevelDif(%f), LevelReduc(%f)' (35 00 00 00 47 65 74 44 61 6D 61 67 65 52 65 64 75 63 74 69 6F 6E 56 61 6C 75 65 3A 20 4C 65 76 65 6C 44 69 66 28 25 66 29 2C 20 4C 65 76 65 6C 52 65 64 75 63 28 25 66 29),
00002C20                         STR: 'GetDamageReductionValue: defDmgReduc(%d), fArmorDamageReduction(%f)' (43 00 00 00 47 65 74 44 61 6D 61 67 65 52 65 64 75 63 74 69 6F 6E 56 61 6C 75 65 3A 20 64 65 66 44 6D 67 52 65 64 75 63 28 25 64 29 2C 20 66 41 72 6D 6F 72 44 61 6D 61 67 65 52 65 64 75 63 74 69 6F 6E 28 25 66 29),
00002C68                         STR: 'GetDamageReductionValue: Armor capped at %f' (2B 00 00 00 47 65 74 44 61 6D 61 67 65 52 65 64 75 63 74 69 6F 6E 56 61 6C 75 65 3A 20 41 72 6D 6F 72 20 63 61 70 70 65 64 20 61 74 20 25 66),
00002C98                         STR: 'GetDamageReductionValue: levelDmgReduc(%f) + armorDmgReduc(%f) = totalDmgReduc(%f)' (52 00 00 00 47 65 74 44 61 6D 61 67 65 52 65 64 75 63 74 69 6F 6E 56 61 6C 75 65 3A 20 6C 65 76 65 6C 44 6D 67 52 65 64 75 63 28 25 66 29 20 2B 20 61 72 6D 6F 72 44 6D 67 52 65 64 75 63 28 25 66 29 20 3D 20 74 6F 74 61 6C 44 6D 67 52 65 64 75 63 28 25 66 29),
00002CEF                         STR: 'GetDamageReductionValue: Capped at %f' (25 00 00 00 47 65 74 44 61 6D 61 67 65 52 65 64 75 63 74 69 6F 6E 56 61 6C 75 65 3A 20 43 61 70 70 65 64 20 61 74 20 25 66)
                             )
                         names:
00002D19                     TUPLE: (
00002D1E                         STR: 'CU' (02 00 00 00 43 55),
00002D25                         STR: 'outputCombatDebugMessageOnMatch' (1F 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 4F 6E 4D 61 74 63 68),
00002D49                         STR: 'attackerLvl' (0B 00 00 00 61 74 74 61 63 6B 65 72 4C 76 6C),
00002D59                         STR: 'defenderLvl' (0B 00 00 00 64 65 66 65 6E 64 65 72 4C 76 6C),
00002D69                         STR: 'curDamageReduction' (12 00 00 00 63 75 72 44 61 6D 61 67 65 52 65 64 75 63 74 69 6F 6E),
00002D80                         STR: 'damageAmount' (0C 00 00 00 64 61 6D 61 67 65 41 6D 6F 75 6E 74),
00002D91                         STR: 'fOverallDamageReduction' (17 00 00 00 66 4F 76 65 72 61 6C 6C 44 61 6D 61 67 65 52 65 64 75 63 74 69 6F 6E),
00002DAD                         STR: 'fLevelDifDamageReduction' (18 00 00 00 66 4C 65 76 65 6C 44 69 66 44 61 6D 61 67 65 52 65 64 75 63 74 69 6F 6E),
00002DCA                         STR: 'fArmorDamageReduction' (15 00 00 00 66 41 72 6D 6F 72 44 61 6D 61 67 65 52 65 64 75 63 74 69 6F 6E),
00002DE4                         STR: 'fLevelScale' (0B 00 00 00 66 4C 65 76 65 6C 53 63 61 6C 65),
00002DF4                         STR: 'fScalePerLevelDef' (11 00 00 00 66 53 63 61 6C 65 50 65 72 4C 65 76 65 6C 44 65 66),
00002E0A                         STR: 'fMinArmorReduction' (12 00 00 00 66 4D 69 6E 41 72 6D 6F 72 52 65 64 75 63 74 69 6F 6E),
00002E21                         STR: 'fMaxArmorReduction' (12 00 00 00 66 4D 61 78 41 72 6D 6F 72 52 65 64 75 63 74 69 6F 6E),
00002E38                         STR: 'fArmorReductionRange' (14 00 00 00 66 41 72 6D 6F 72 52 65 64 75 63 74 69 6F 6E 52 61 6E 67 65),
00002E51                         STR: 'fMinReduction' (0D 00 00 00 66 4D 69 6E 52 65 64 75 63 74 69 6F 6E),
00002E63                         STR: 'fMaxReduction' (0D 00 00 00 66 4D 61 78 52 65 64 75 63 74 69 6F 6E),
00002E75                         STR: 'fArmorStartPos' (0E 00 00 00 66 41 72 6D 6F 72 53 74 61 72 74 50 6F 73),
00002E88                         STR: 'float' (05 00 00 00 66 6C 6F 61 74),
00002E92                         STR: 'levelDiff' (09 00 00 00 6C 65 76 65 6C 44 69 66 66),
00002EA0                         STR: 'fTotalRange' (0B 00 00 00 66 54 6F 74 61 6C 52 61 6E 67 65),
00002EB0                         STR: 'fTickSize' (09 00 00 00 66 54 69 63 6B 53 69 7A 65)
                             )
                         varnames:
00002EBE                     TUPLE: (
00002EC3                         STR: 'attackerLvl' (0B 00 00 00 61 74 74 61 63 6B 65 72 4C 76 6C),
00002ED3                         STR: 'defenderLvl' (0B 00 00 00 64 65 66 65 6E 64 65 72 4C 76 6C),
00002EE3                         STR: 'curDamageReduction' (12 00 00 00 63 75 72 44 61 6D 61 67 65 52 65 64 75 63 74 69 6F 6E),
00002EFA                         STR: 'damageAmount' (0C 00 00 00 64 61 6D 61 67 65 41 6D 6F 75 6E 74),
00002F0B                         STR: 'fOverallDamageReduction' (17 00 00 00 66 4F 76 65 72 61 6C 6C 44 61 6D 61 67 65 52 65 64 75 63 74 69 6F 6E),
00002F27                         STR: 'fMinArmorReduction' (12 00 00 00 66 4D 69 6E 41 72 6D 6F 72 52 65 64 75 63 74 69 6F 6E),
00002F3E                         STR: 'fMaxArmorReduction' (12 00 00 00 66 4D 61 78 41 72 6D 6F 72 52 65 64 75 63 74 69 6F 6E),
00002F55                         STR: 'fArmorStartPos' (0E 00 00 00 66 41 72 6D 6F 72 53 74 61 72 74 50 6F 73),
00002F68                         STR: 'levelDiff' (09 00 00 00 6C 65 76 65 6C 44 69 66 66),
00002F76                         STR: 'fArmorDamageReduction' (15 00 00 00 66 41 72 6D 6F 72 44 61 6D 61 67 65 52 65 64 75 63 74 69 6F 6E),
00002F90                         STR: 'fScalePerLevelDef' (11 00 00 00 66 53 63 61 6C 65 50 65 72 4C 65 76 65 6C 44 65 66),
00002FA6                         STR: 'fLevelScale' (0B 00 00 00 66 4C 65 76 65 6C 53 63 61 6C 65),
00002FB6                         STR: 'fTotalRange' (0B 00 00 00 66 54 6F 74 61 6C 52 61 6E 67 65),
00002FC6                         STR: 'fMaxReduction' (0D 00 00 00 66 4D 61 78 52 65 64 75 63 74 69 6F 6E),
00002FD8                         STR: 'fTickSize' (09 00 00 00 66 54 69 63 6B 53 69 7A 65),
00002FE6                         STR: 'fMinReduction' (0D 00 00 00 66 4D 69 6E 52 65 64 75 63 74 69 6F 6E),
00002FF8                         STR: 'fLevelDifDamageReduction' (18 00 00 00 66 4C 65 76 65 6C 44 69 66 44 61 6D 61 67 65 52 65 64 75 63 74 69 6F 6E),
00003015                         STR: 'fArmorReductionRange' (14 00 00 00 66 41 72 6D 6F 72 52 65 64 75 63 74 69 6F 6E 52 61 6E 67 65)
                             )
                         freevars:
0000302E                     TUPLE: ()
                         cellvars:
00003033                     TUPLE: ()
                         filename:
00003038                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat_calculations.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73 2E 70 79)
                         name:
00003088                     STR: 'GetDamageReductionValue' (17 00 00 00 47 65 74 44 61 6D 61 67 65 52 65 64 75 63 74 69 6F 6E 56 61 6C 75 65)
                         firslineno:
000030A4                     LONG: 324L (44 01 00 00)
                         lnotab:
000030A8                     STR: '\x00\x02 \x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\n\x01\x06\x01\x06\x01\x06\x04\x16\x01\n\x01\x1a\x04\x14\x01\n\x01\x18\x01\x1a\x03\r\x01\x06\x01\x18\n\n\x01\x1d\x04\r\x01\x06\x01\x18\x01\r\x01\x06\x01\x18\x02' (3E 00 00 00 00 02 20 01 06 01 06 01 06 01 06 01 06 01 06 01 06 01 0A 01 06 01 06 01 06 04 16 01 0A 01 1A 04 14 01 0A 01 18 01 1A 03 0D 01 06 01 18 0A 0A 01 1D 04 0D 01 06 01 18 01 0D 01 06 01 18 02),
000030EB             CODE:
                         argcount:
000030EC                     LONG: 3L (03 00 00 00)
                         nlocals:
000030F0                     LONG: 7L (07 00 00 00)
                         stacksize:
000030F4                     LONG: 5L (05 00 00 00)
                         flags:
000030F8                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000030FC                     STR: 't\x00\x00i\x01\x00d\x01\x00|\x00\x00|\x01\x00|\x02\x00f\x03\x00\x16d\x02\x00\x83\x02\x00\x01|\x00\x00|\x01\x00j\x05\x00o\x1a\x00\x01d\x03\x00|\x01\x00|\x00\x00\x18\x18d\x04\x00\x14d\x05\x00\x17}\x06\x00n\x17\x00\x01|\x01\x00|\x00\x00\x18d\x06\x00\x18d\x07\x00\x14d\x08\x00\x17}\x06\x00t\x06\x00|\x02\x00\x83\x01\x00d\t\x00\x15}\x04\x00t\x08\x00|\x06\x00|\x04\x00\x14\x83\x01\x00}\x05\x00|\x06\x00|\x05\x00\x17}\x03\x00t\x00\x00i\x01\x00d\n\x00|\x06\x00|\x05\x00|\x03\x00f\x03\x00\x16d\x02\x00\x83\x02\x00\x01|\x03\x00d\x0b\x00j\x04\x00o\x1a\x00\x01d\x0b\x00}\x03\x00t\x00\x00i\x01\x00d\x0c\x00d\x02\x00\x83\x02\x00\x01n(\x00\x01|\x03\x00d\r\x00j\x00\x00o\x1a\x00\x01d\r\x00}\x03\x00t\x00\x00i\x01\x00d\x0e\x00d\x02\x00\x83\x02\x00\x01n\x01\x00\x01t\x08\x00|\x03\x00\x83\x01\x00Sd\x00\x00S' (FD 00 00 00 74 00 00 69 01 00 64 01 00 7C 00 00 7C 01 00 7C 02 00 66 03 00 16 64 02 00 83 02 00 01 7C 00 00 7C 01 00 6A 05 00 6F 1A 00 01 64 03 00 7C 01 00 7C 00 00 18 18 64 04 00 14 64 05 00 17 7D 06 00 6E 17 00 01 7C 01 00 7C 00 00 18 64 06 00 18 64 07 00 14 64 08 00 17 7D 06 00 74 06 00 7C 02 00 83 01 00 64 09 00 15 7D 04 00 74 08 00 7C 06 00 7C 04 00 14 83 01 00 7D 05 00 7C 06 00 7C 05 00 17 7D 03 00 74 00 00 69 01 00 64 0A 00 7C 06 00 7C 05 00 7C 03 00 66 03 00 16 64 02 00 83 02 00 01 7C 03 00 64 0B 00 6A 04 00 6F 1A 00 01 64 0B 00 7D 03 00 74 00 00 69 01 00 64 0C 00 64 02 00 83 02 00 01 6E 28 00 01 7C 03 00 64 0D 00 6A 00 00 6F 1A 00 01 64 0D 00 7D 03 00 74 00 00 69 01 00 64 0E 00 64 02 00 83 02 00 01 6E 01 00 01 74 08 00 7C 03 00 83 01 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CU'
                             00000003     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000006     64 - LOAD_CONST          'GetShieldDamageValue Input: atkLvl(%d) defLvl(%d) forceCombatBonus(%d)'
                             00000009     7C - LOAD_FAST           'attackerLvl'
                             0000000C     7C - LOAD_FAST           'defenderLvl'
                             0000000F     7C - LOAD_FAST           'forceCombatBonus'
                             00000012     66 - BUILD_TUPLE         r0003
                             00000015     16 - BINARY_MODULO       
                             00000016     64 - LOAD_CONST          21
                             00000019     83 - CALL_FUNCTION       r0002
                             0000001C     01 - POP_TOP             
                             0000001D     7C - LOAD_FAST           'attackerLvl'
                             00000020     7C - LOAD_FAST           'defenderLvl'
                             00000023     6A - COMPARE_OP          ">="
                             00000026     6F - JUMP_IF_FALSE       -> 00000043
                             00000029     01 - POP_TOP             
                             0000002A     64 - LOAD_CONST          4
                             0000002D     7C - LOAD_FAST           'defenderLvl'
                             00000030     7C - LOAD_FAST           'attackerLvl'
                             00000033     18 - BINARY_SUBTRACT     
                             00000034     18 - BINARY_SUBTRACT     
                             00000035     64 - LOAD_CONST          7.2999999999999998
                             00000038     14 - BINARY_MULTIPLY     
                             00000039     64 - LOAD_CONST          6
                             0000003C     17 - BINARY_ADD          
                             0000003D     7D - STORE_FAST          'baseDamage'
                             00000040     6E - JUMP_FORWARD        -> 0000005A
                             00000043     01 - POP_TOP             
                             00000044     7C - LOAD_FAST           'defenderLvl'
                             00000047     7C - LOAD_FAST           'attackerLvl'
                             0000004A     18 - BINARY_SUBTRACT     
                             0000004B     64 - LOAD_CONST          9
                             0000004E     18 - BINARY_SUBTRACT     
                             0000004F     64 - LOAD_CONST          -2
                             00000052     14 - BINARY_MULTIPLY     
                             00000053     64 - LOAD_CONST          22
                             00000056     17 - BINARY_ADD          
                             00000057     7D - STORE_FAST          'baseDamage'
                             0000005A     74 - LOAD_GLOBAL         'float'
                             0000005D     7C - LOAD_FAST           'forceCombatBonus'
                             00000060     83 - CALL_FUNCTION       r0001
                             00000063     64 - LOAD_CONST          100.0
                             00000066     15 - BINARY_DIVIDE       
                             00000067     7D - STORE_FAST          'bonusPercent'
                             0000006A     74 - LOAD_GLOBAL         'int'
                             0000006D     7C - LOAD_FAST           'baseDamage'
                             00000070     7C - LOAD_FAST           'bonusPercent'
                             00000073     14 - BINARY_MULTIPLY     
                             00000074     83 - CALL_FUNCTION       r0001
                             00000077     7D - STORE_FAST          'bonusDamage'
                             0000007A     7C - LOAD_FAST           'baseDamage'
                             0000007D     7C - LOAD_FAST           'bonusDamage'
                             00000080     17 - BINARY_ADD          
                             00000081     7D - STORE_FAST          'totalDamage'
                             00000084     74 - LOAD_GLOBAL         'CU'
                             00000087     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             0000008A     64 - LOAD_CONST          'GetShieldDamageValue Total: base(%d) bonus(%d) total(%d)'
                             0000008D     7C - LOAD_FAST           'baseDamage'
                             00000090     7C - LOAD_FAST           'bonusDamage'
                             00000093     7C - LOAD_FAST           'totalDamage'
                             00000096     66 - BUILD_TUPLE         r0003
                             00000099     16 - BINARY_MODULO       
                             0000009A     64 - LOAD_CONST          21
                             0000009D     83 - CALL_FUNCTION       r0002
                             000000A0     01 - POP_TOP             
                             000000A1     7C - LOAD_FAST           'totalDamage'
                             000000A4     64 - LOAD_CONST          500
                             000000A7     6A - COMPARE_OP          ">"
                             000000AA     6F - JUMP_IF_FALSE       -> 000000C7
                             000000AD     01 - POP_TOP             
                             000000AE     64 - LOAD_CONST          500
                             000000B1     7D - STORE_FAST          'totalDamage'
                             000000B4     74 - LOAD_GLOBAL         'CU'
                             000000B7     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             000000BA     64 - LOAD_CONST          'GetShieldDamageValue: Capped at 500'
                             000000BD     64 - LOAD_CONST          21
                             000000C0     83 - CALL_FUNCTION       r0002
                             000000C3     01 - POP_TOP             
                             000000C4     6E - JUMP_FORWARD        -> 000000EF
                             000000C7     01 - POP_TOP             
                             000000C8     7C - LOAD_FAST           'totalDamage'
                             000000CB     64 - LOAD_CONST          10
                             000000CE     6A - COMPARE_OP          "<"
                             000000D1     6F - JUMP_IF_FALSE       -> 000000EE
                             000000D4     01 - POP_TOP             
                             000000D5     64 - LOAD_CONST          10
                             000000D8     7D - STORE_FAST          'totalDamage'
                             000000DB     74 - LOAD_GLOBAL         'CU'
                             000000DE     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             000000E1     64 - LOAD_CONST          'GetShieldDamageValue: Capped at 10'
                             000000E4     64 - LOAD_CONST          21
                             000000E7     83 - CALL_FUNCTION       r0002
                             000000EA     01 - POP_TOP             
                             000000EB     6E - JUMP_FORWARD        -> 000000EF
                             000000EE     01 - POP_TOP             
                             000000EF     74 - LOAD_GLOBAL         'int'
                             000000F2     7C - LOAD_FAST           'totalDamage'
                             000000F5     83 - CALL_FUNCTION       r0001
                             000000F8     53 - RETURN_VALUE        
                             000000F9     64 - LOAD_CONST          None
                             000000FC     53 - RETURN_VALUE        
                         consts:
000031FE                     TUPLE: (
00003203                         None (4E),
00003204                         STR: 'GetShieldDamageValue Input: atkLvl(%d) defLvl(%d) forceCombatBonus(%d)' (46 00 00 00 47 65 74 53 68 69 65 6C 64 44 61 6D 61 67 65 56 61 6C 75 65 20 49 6E 70 75 74 3A 20 61 74 6B 4C 76 6C 28 25 64 29 20 64 65 66 4C 76 6C 28 25 64 29 20 66 6F 72 63 65 43 6F 6D 62 61 74 42 6F 6E 75 73 28 25 64 29),
0000324F                         INT: 21 (15 00 00 00),
00003254                         INT: 4 (04 00 00 00),
00003259                         FLOAT: 7.2999999999999998 (12 37 2E 32 39 39 39 39 39 39 39 39 39 39 39 39 39 39 38),
0000326D                         INT: 6 (06 00 00 00),
00003272                         INT: 9 (09 00 00 00),
00003277                         INT: -2 (FE FF FF FF),
0000327C                         INT: 22 (16 00 00 00),
00003281                         FLOAT: 100.0 (05 31 30 30 2E 30),
00003288                         STR: 'GetShieldDamageValue Total: base(%d) bonus(%d) total(%d)' (38 00 00 00 47 65 74 53 68 69 65 6C 64 44 61 6D 61 67 65 56 61 6C 75 65 20 54 6F 74 61 6C 3A 20 62 61 73 65 28 25 64 29 20 62 6F 6E 75 73 28 25 64 29 20 74 6F 74 61 6C 28 25 64 29),
000032C5                         INT: 500 (F4 01 00 00),
000032CA                         STR: 'GetShieldDamageValue: Capped at 500' (23 00 00 00 47 65 74 53 68 69 65 6C 64 44 61 6D 61 67 65 56 61 6C 75 65 3A 20 43 61 70 70 65 64 20 61 74 20 35 30 30),
000032F2                         INT: 10 (0A 00 00 00),
000032F7                         STR: 'GetShieldDamageValue: Capped at 10' (22 00 00 00 47 65 74 53 68 69 65 6C 64 44 61 6D 61 67 65 56 61 6C 75 65 3A 20 43 61 70 70 65 64 20 61 74 20 31 30)
                             )
                         names:
0000331E                     TUPLE: (
00003323                         STR: 'CU' (02 00 00 00 43 55),
0000332A                         STR: 'outputCombatDebugMessageOnMatch' (1F 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 4F 6E 4D 61 74 63 68),
0000334E                         STR: 'attackerLvl' (0B 00 00 00 61 74 74 61 63 6B 65 72 4C 76 6C),
0000335E                         STR: 'defenderLvl' (0B 00 00 00 64 65 66 65 6E 64 65 72 4C 76 6C),
0000336E                         STR: 'forceCombatBonus' (10 00 00 00 66 6F 72 63 65 43 6F 6D 62 61 74 42 6F 6E 75 73),
00003383                         STR: 'baseDamage' (0A 00 00 00 62 61 73 65 44 61 6D 61 67 65),
00003392                         STR: 'float' (05 00 00 00 66 6C 6F 61 74),
0000339C                         STR: 'bonusPercent' (0C 00 00 00 62 6F 6E 75 73 50 65 72 63 65 6E 74),
000033AD                         STR: 'int' (03 00 00 00 69 6E 74),
000033B5                         STR: 'bonusDamage' (0B 00 00 00 62 6F 6E 75 73 44 61 6D 61 67 65),
000033C5                         STR: 'totalDamage' (0B 00 00 00 74 6F 74 61 6C 44 61 6D 61 67 65)
                             )
                         varnames:
000033D5                     TUPLE: (
000033DA                         STR: 'attackerLvl' (0B 00 00 00 61 74 74 61 63 6B 65 72 4C 76 6C),
000033EA                         STR: 'defenderLvl' (0B 00 00 00 64 65 66 65 6E 64 65 72 4C 76 6C),
000033FA                         STR: 'forceCombatBonus' (10 00 00 00 66 6F 72 63 65 43 6F 6D 62 61 74 42 6F 6E 75 73),
0000340F                         STR: 'totalDamage' (0B 00 00 00 74 6F 74 61 6C 44 61 6D 61 67 65),
0000341F                         STR: 'bonusPercent' (0C 00 00 00 62 6F 6E 75 73 50 65 72 63 65 6E 74),
00003430                         STR: 'bonusDamage' (0B 00 00 00 62 6F 6E 75 73 44 61 6D 61 67 65),
00003440                         STR: 'baseDamage' (0A 00 00 00 62 61 73 65 44 61 6D 61 67 65)
                             )
                         freevars:
0000344F                     TUPLE: ()
                         cellvars:
00003454                     TUPLE: ()
                         filename:
00003459                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat_calculations.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73 2E 70 79)
                         name:
000034A9                     STR: 'GetShieldDamageValue' (14 00 00 00 47 65 74 53 68 69 65 6C 64 44 61 6D 61 67 65 56 61 6C 75 65)
                         firslineno:
000034C2                     LONG: 390L (86 01 00 00)
                         lnotab:
000034C6                     STR: '\x00\x02\x1d\x03\r\x01\x1a\x02\x16\x02\x10\x01\x10\x01\n\x03\x1d\x02\r\x01\x06\x01\x14\x01\r\x01\x06\x01\x14\x02' (1E 00 00 00 00 02 1D 03 0D 01 1A 02 16 02 10 01 10 01 0A 03 1D 02 0D 01 06 01 14 01 0D 01 06 01 14 02),
000034E9             CODE:
                         argcount:
000034EA                     LONG: 2L (02 00 00 00)
                         nlocals:
000034EE                     LONG: 6L (06 00 00 00)
                         stacksize:
000034F2                     LONG: 4L (04 00 00 00)
                         flags:
000034F6                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000034FA                     STR: 't\x00\x00i\x01\x00d\x01\x00|\x00\x00|\x01\x00f\x02\x00\x16d\x02\x00\x83\x02\x00\x01d\x03\x00}\x02\x00|\x01\x00|\x00\x00\x18}\x03\x00|\x03\x00d\x04\x00j\x01\x00o"\x00\x01t\x00\x00i\x01\x00d\x05\x00|\x03\x00|\x02\x00f\x02\x00\x16d\x02\x00\x83\x02\x00\x01|\x02\x00Sn\x01\x00\x01t\x06\x00|\x03\x00d\x06\x00\x18d\x04\x00\x83\x02\x00}\x05\x00d\x07\x00}\x04\x00|\x02\x00|\x05\x00|\x04\x00\x148}\x02\x00t\x00\x00i\x01\x00d\x05\x00|\x03\x00|\x02\x00f\x02\x00\x16d\x02\x00\x83\x02\x00\x01|\x02\x00d\x08\x00j\x00\x00o\x1a\x00\x01d\x08\x00}\x02\x00t\x00\x00i\x01\x00d\t\x00d\x02\x00\x83\x02\x00\x01n(\x00\x01|\x02\x00d\x03\x00j\x04\x00o\x1a\x00\x01d\x03\x00}\x02\x00t\x00\x00i\x01\x00d\n\x00d\x02\x00\x83\x02\x00\x01n\x01\x00\x01|\x02\x00Sd\x00\x00S' (F0 00 00 00 74 00 00 69 01 00 64 01 00 7C 00 00 7C 01 00 66 02 00 16 64 02 00 83 02 00 01 64 03 00 7D 02 00 7C 01 00 7C 00 00 18 7D 03 00 7C 03 00 64 04 00 6A 01 00 6F 22 00 01 74 00 00 69 01 00 64 05 00 7C 03 00 7C 02 00 66 02 00 16 64 02 00 83 02 00 01 7C 02 00 53 6E 01 00 01 74 06 00 7C 03 00 64 06 00 18 64 04 00 83 02 00 7D 05 00 64 07 00 7D 04 00 7C 02 00 7C 05 00 7C 04 00 14 38 7D 02 00 74 00 00 69 01 00 64 05 00 7C 03 00 7C 02 00 66 02 00 16 64 02 00 83 02 00 01 7C 02 00 64 08 00 6A 00 00 6F 1A 00 01 64 08 00 7D 02 00 74 00 00 69 01 00 64 09 00 64 02 00 83 02 00 01 6E 28 00 01 7C 02 00 64 03 00 6A 04 00 6F 1A 00 01 64 03 00 7D 02 00 74 00 00 69 01 00 64 0A 00 64 02 00 83 02 00 01 6E 01 00 01 7C 02 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CU'
                             00000003     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000006     64 - LOAD_CONST          'GetShieldResistanceISDrainValue Input: atkLvl(%d) defLvl(%d)'
                             00000009     7C - LOAD_FAST           'attackerLvl'
                             0000000C     7C - LOAD_FAST           'defenderLvl'
                             0000000F     66 - BUILD_TUPLE         r0002
                             00000012     16 - BINARY_MODULO       
                             00000013     64 - LOAD_CONST          21
                             00000016     83 - CALL_FUNCTION       r0002
                             00000019     01 - POP_TOP             
                             0000001A     64 - LOAD_CONST          10
                             0000001D     7D - STORE_FAST          'ISCost'
                             00000020     7C - LOAD_FAST           'defenderLvl'
                             00000023     7C - LOAD_FAST           'attackerLvl'
                             00000026     18 - BINARY_SUBTRACT     
                             00000027     7D - STORE_FAST          'levelDiff'
                             0000002A     7C - LOAD_FAST           'levelDiff'
                             0000002D     64 - LOAD_CONST          0
                             00000030     6A - COMPARE_OP          "<="
                             00000033     6F - JUMP_IF_FALSE       -> 00000058
                             00000036     01 - POP_TOP             
                             00000037     74 - LOAD_GLOBAL         'CU'
                             0000003A     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             0000003D     64 - LOAD_CONST          'GetShieldResistanceISDrainValue Total: lvldiff(%d) ISCost(%d)'
                             00000040     7C - LOAD_FAST           'levelDiff'
                             00000043     7C - LOAD_FAST           'ISCost'
                             00000046     66 - BUILD_TUPLE         r0002
                             00000049     16 - BINARY_MODULO       
                             0000004A     64 - LOAD_CONST          21
                             0000004D     83 - CALL_FUNCTION       r0002
                             00000050     01 - POP_TOP             
                             00000051     7C - LOAD_FAST           'ISCost'
                             00000054     53 - RETURN_VALUE        
                             00000055     6E - JUMP_FORWARD        -> 00000059
                             00000058     01 - POP_TOP             
                             00000059     74 - LOAD_GLOBAL         'max'
                             0000005C     7C - LOAD_FAST           'levelDiff'
                             0000005F     64 - LOAD_CONST          5
                             00000062     18 - BINARY_SUBTRACT     
                             00000063     64 - LOAD_CONST          0
                             00000066     83 - CALL_FUNCTION       r0002
                             00000069     7D - STORE_FAST          'LevelDiffAfterScale'
                             0000006C     64 - LOAD_CONST          1
                             0000006F     7D - STORE_FAST          'ISPerLevelCost'
                             00000072     7C - LOAD_FAST           'ISCost'
                             00000075     7C - LOAD_FAST           'LevelDiffAfterScale'
                             00000078     7C - LOAD_FAST           'ISPerLevelCost'
                             0000007B     14 - BINARY_MULTIPLY     
                             0000007C     38 - INPLACE_SUBTRACT    
                             0000007D     7D - STORE_FAST          'ISCost'
                             00000080     74 - LOAD_GLOBAL         'CU'
                             00000083     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000086     64 - LOAD_CONST          'GetShieldResistanceISDrainValue Total: lvldiff(%d) ISCost(%d)'
                             00000089     7C - LOAD_FAST           'levelDiff'
                             0000008C     7C - LOAD_FAST           'ISCost'
                             0000008F     66 - BUILD_TUPLE         r0002
                             00000092     16 - BINARY_MODULO       
                             00000093     64 - LOAD_CONST          21
                             00000096     83 - CALL_FUNCTION       r0002
                             00000099     01 - POP_TOP             
                             0000009A     7C - LOAD_FAST           'ISCost'
                             0000009D     64 - LOAD_CONST          2
                             000000A0     6A - COMPARE_OP          "<"
                             000000A3     6F - JUMP_IF_FALSE       -> 000000C0
                             000000A6     01 - POP_TOP             
                             000000A7     64 - LOAD_CONST          2
                             000000AA     7D - STORE_FAST          'ISCost'
                             000000AD     74 - LOAD_GLOBAL         'CU'
                             000000B0     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             000000B3     64 - LOAD_CONST          'GetShieldResistanceISDrainValue: Capped at -2'
                             000000B6     64 - LOAD_CONST          21
                             000000B9     83 - CALL_FUNCTION       r0002
                             000000BC     01 - POP_TOP             
                             000000BD     6E - JUMP_FORWARD        -> 000000E8
                             000000C0     01 - POP_TOP             
                             000000C1     7C - LOAD_FAST           'ISCost'
                             000000C4     64 - LOAD_CONST          10
                             000000C7     6A - COMPARE_OP          ">"
                             000000CA     6F - JUMP_IF_FALSE       -> 000000E7
                             000000CD     01 - POP_TOP             
                             000000CE     64 - LOAD_CONST          10
                             000000D1     7D - STORE_FAST          'ISCost'
                             000000D4     74 - LOAD_GLOBAL         'CU'
                             000000D7     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             000000DA     64 - LOAD_CONST          'GetShieldResistanceISDrainValue: Capped at -10'
                             000000DD     64 - LOAD_CONST          21
                             000000E0     83 - CALL_FUNCTION       r0002
                             000000E3     01 - POP_TOP             
                             000000E4     6E - JUMP_FORWARD        -> 000000E8
                             000000E7     01 - POP_TOP             
                             000000E8     7C - LOAD_FAST           'ISCost'
                             000000EB     53 - RETURN_VALUE        
                             000000EC     64 - LOAD_CONST          None
                             000000EF     53 - RETURN_VALUE        
                         consts:
000035EF                     TUPLE: (
000035F4                         None (4E),
000035F5                         STR: 'GetShieldResistanceISDrainValue Input: atkLvl(%d) defLvl(%d)' (3C 00 00 00 47 65 74 53 68 69 65 6C 64 52 65 73 69 73 74 61 6E 63 65 49 53 44 72 61 69 6E 56 61 6C 75 65 20 49 6E 70 75 74 3A 20 61 74 6B 4C 76 6C 28 25 64 29 20 64 65 66 4C 76 6C 28 25 64 29),
00003636                         INT: 21 (15 00 00 00),
0000363B                         INT: 10 (0A 00 00 00),
00003640                         INT: 0 (00 00 00 00),
00003645                         STR: 'GetShieldResistanceISDrainValue Total: lvldiff(%d) ISCost(%d)' (3D 00 00 00 47 65 74 53 68 69 65 6C 64 52 65 73 69 73 74 61 6E 63 65 49 53 44 72 61 69 6E 56 61 6C 75 65 20 54 6F 74 61 6C 3A 20 6C 76 6C 64 69 66 66 28 25 64 29 20 49 53 43 6F 73 74 28 25 64 29),
00003687                         INT: 5 (05 00 00 00),
0000368C                         INT: 1 (01 00 00 00),
00003691                         INT: 2 (02 00 00 00),
00003696                         STR: 'GetShieldResistanceISDrainValue: Capped at -2' (2D 00 00 00 47 65 74 53 68 69 65 6C 64 52 65 73 69 73 74 61 6E 63 65 49 53 44 72 61 69 6E 56 61 6C 75 65 3A 20 43 61 70 70 65 64 20 61 74 20 2D 32),
000036C8                         STR: 'GetShieldResistanceISDrainValue: Capped at -10' (2E 00 00 00 47 65 74 53 68 69 65 6C 64 52 65 73 69 73 74 61 6E 63 65 49 53 44 72 61 69 6E 56 61 6C 75 65 3A 20 43 61 70 70 65 64 20 61 74 20 2D 31 30)
                             )
                         names:
000036FB                     TUPLE: (
00003700                         STR: 'CU' (02 00 00 00 43 55),
00003707                         STR: 'outputCombatDebugMessageOnMatch' (1F 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 4F 6E 4D 61 74 63 68),
0000372B                         STR: 'attackerLvl' (0B 00 00 00 61 74 74 61 63 6B 65 72 4C 76 6C),
0000373B                         STR: 'defenderLvl' (0B 00 00 00 64 65 66 65 6E 64 65 72 4C 76 6C),
0000374B                         STR: 'ISCost' (06 00 00 00 49 53 43 6F 73 74),
00003756                         STR: 'levelDiff' (09 00 00 00 6C 65 76 65 6C 44 69 66 66),
00003764                         STR: 'max' (03 00 00 00 6D 61 78),
0000376C                         STR: 'LevelDiffAfterScale' (13 00 00 00 4C 65 76 65 6C 44 69 66 66 41 66 74 65 72 53 63 61 6C 65),
00003784                         STR: 'ISPerLevelCost' (0E 00 00 00 49 53 50 65 72 4C 65 76 65 6C 43 6F 73 74)
                             )
                         varnames:
00003797                     TUPLE: (
0000379C                         STR: 'attackerLvl' (0B 00 00 00 61 74 74 61 63 6B 65 72 4C 76 6C),
000037AC                         STR: 'defenderLvl' (0B 00 00 00 64 65 66 65 6E 64 65 72 4C 76 6C),
000037BC                         STR: 'ISCost' (06 00 00 00 49 53 43 6F 73 74),
000037C7                         STR: 'levelDiff' (09 00 00 00 6C 65 76 65 6C 44 69 66 66),
000037D5                         STR: 'ISPerLevelCost' (0E 00 00 00 49 53 50 65 72 4C 65 76 65 6C 43 6F 73 74),
000037E8                         STR: 'LevelDiffAfterScale' (13 00 00 00 4C 65 76 65 6C 44 69 66 66 41 66 74 65 72 53 63 61 6C 65)
                             )
                         freevars:
00003800                     TUPLE: ()
                         cellvars:
00003805                     TUPLE: ()
                         filename:
0000380A                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat_calculations.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73 2E 70 79)
                         name:
0000385A                     STR: 'GetShieldResistanceISDrainValue' (1F 00 00 00 47 65 74 53 68 69 65 6C 64 52 65 73 69 73 74 61 6E 63 65 49 53 44 72 61 69 6E 56 61 6C 75 65)
                         firslineno:
0000387E                     LONG: 426L (AA 01 00 00)
                         lnotab:
00003882                     STR: '\x00\x02\x1a\x02\x06\x01\n\x03\r\x01\x1a\x01\x08\x02\x13\x01\x06\x01\x0e\x03\x1a\x02\r\x01\x06\x01\x14\x01\r\x01\x06\x01\x14\x02' (22 00 00 00 00 02 1A 02 06 01 0A 03 0D 01 1A 01 08 02 13 01 06 01 0E 03 1A 02 0D 01 06 01 14 01 0D 01 06 01 14 02),
000038A9             CODE:
                         argcount:
000038AA                     LONG: 5L (05 00 00 00)
                         nlocals:
000038AE                     LONG: 17L (11 00 00 00)
                         stacksize:
000038B2                     LONG: 5L (05 00 00 00)
                         flags:
000038B6                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000038BA                     STR: 't\x00\x00}\x06\x00t\x02\x00|\x00\x00|\x01\x00\x15\x83\x01\x00}\x07\x00d\x01\x00}\x0f\x00d\x01\x00}\x05\x00t\x02\x00|\x04\x00\x83\x01\x00d\x02\x00\x14}\r\x00d\x03\x00}\x0b\x00|\x05\x00|\r\x00\x17|\x0b\x00\x17}\n\x00|\x07\x00|\x0f\x00\x14}\t\x00|\n\x00|\t\x00\x18}\x10\x00t\x0e\x00i\x0f\x00d\x04\x00|\n\x00|\t\x00|\x10\x00f\x03\x00\x16d\x05\x00\x83\x02\x00\x01d\x06\x00}\x08\x00d\x07\x00}\x0e\x00|\x10\x00|\x08\x00j\x00\x00o\n\x00\x01|\x08\x00}\x10\x00n\x18\x00\x01|\x10\x00|\x0e\x00j\x04\x00o\n\x00\x01|\x0e\x00}\x10\x00n\x01\x00\x01t\x12\x00i\x13\x00d\x08\x00d\t\x00\x83\x02\x00}\x0c\x00|\x0c\x00t\x15\x00|\x10\x00d\n\x00\x14\x83\x01\x00j\x01\x00}\x06\x00|\x06\x00o\x14\x00\x01t\x0e\x00i\x0f\x00d\x0b\x00d\x05\x00\x83\x02\x00\x01n\x11\x00\x01t\x0e\x00i\x0f\x00d\x0c\x00d\x05\x00\x83\x02\x00\x01|\x06\x00Sd\x00\x00S' (0C 01 00 00 74 00 00 7D 06 00 74 02 00 7C 00 00 7C 01 00 15 83 01 00 7D 07 00 64 01 00 7D 0F 00 64 01 00 7D 05 00 74 02 00 7C 04 00 83 01 00 64 02 00 14 7D 0D 00 64 03 00 7D 0B 00 7C 05 00 7C 0D 00 17 7C 0B 00 17 7D 0A 00 7C 07 00 7C 0F 00 14 7D 09 00 7C 0A 00 7C 09 00 18 7D 10 00 74 0E 00 69 0F 00 64 04 00 7C 0A 00 7C 09 00 7C 10 00 66 03 00 16 64 05 00 83 02 00 01 64 06 00 7D 08 00 64 07 00 7D 0E 00 7C 10 00 7C 08 00 6A 00 00 6F 0A 00 01 7C 08 00 7D 10 00 6E 18 00 01 7C 10 00 7C 0E 00 6A 04 00 6F 0A 00 01 7C 0E 00 7D 10 00 6E 01 00 01 74 12 00 69 13 00 64 08 00 64 09 00 83 02 00 7D 0C 00 7C 0C 00 74 15 00 7C 10 00 64 0A 00 14 83 01 00 6A 01 00 7D 06 00 7C 06 00 6F 14 00 01 74 0E 00 69 0F 00 64 0B 00 64 05 00 83 02 00 01 6E 11 00 01 74 0E 00 69 0F 00 64 0C 00 64 05 00 83 02 00 01 7C 06 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'False'
                             00000003     7D - STORE_FAST          'bResisted'
                             00000006     74 - LOAD_GLOBAL         'float'
                             00000009     7C - LOAD_FAST           'damageAmount'
                             0000000C     7C - LOAD_FAST           'maxHealth'
                             0000000F     15 - BINARY_DIVIDE       
                             00000010     83 - CALL_FUNCTION       r0001
                             00000013     7D - STORE_FAST          'percentOfLeftTaken'
                             00000016     64 - LOAD_CONST          0.75
                             00000019     7D - STORE_FAST          'attackerMod'
                             0000001C     64 - LOAD_CONST          0.75
                             0000001F     7D - STORE_FAST          'basicChance'
                             00000022     74 - LOAD_GLOBAL         'float'
                             00000025     7C - LOAD_FAST           'concentrationValue'
                             00000028     83 - CALL_FUNCTION       r0001
                             0000002B     64 - LOAD_CONST          0.0050000000000000001
                             0000002E     14 - BINARY_MULTIPLY     
                             0000002F     7D - STORE_FAST          'concentrationChance'
                             00000032     64 - LOAD_CONST          0
                             00000035     7D - STORE_FAST          'lvlChance'
                             00000038     7C - LOAD_FAST           'basicChance'
                             0000003B     7C - LOAD_FAST           'concentrationChance'
                             0000003E     17 - BINARY_ADD          
                             0000003F     7C - LOAD_FAST           'lvlChance'
                             00000042     17 - BINARY_ADD          
                             00000043     7D - STORE_FAST          'fDefenderChance'
                             00000046     7C - LOAD_FAST           'percentOfLeftTaken'
                             00000049     7C - LOAD_FAST           'attackerMod'
                             0000004C     14 - BINARY_MULTIPLY     
                             0000004D     7D - STORE_FAST          'fAttackerChance'
                             00000050     7C - LOAD_FAST           'fDefenderChance'
                             00000053     7C - LOAD_FAST           'fAttackerChance'
                             00000056     18 - BINARY_SUBTRACT     
                             00000057     7D - STORE_FAST          'fFinal'
                             0000005A     74 - LOAD_GLOBAL         'CU'
                             0000005D     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000060     64 - LOAD_CONST          'CastThrough Def(%g) - Atk(%g) = chance(%g)'
                             00000063     7C - LOAD_FAST           'fDefenderChance'
                             00000066     7C - LOAD_FAST           'fAttackerChance'
                             00000069     7C - LOAD_FAST           'fFinal'
                             0000006C     66 - BUILD_TUPLE         r0003
                             0000006F     16 - BINARY_MODULO       
                             00000070     64 - LOAD_CONST          21
                             00000073     83 - CALL_FUNCTION       r0002
                             00000076     01 - POP_TOP             
                             00000077     64 - LOAD_CONST          0.33000000000000002
                             0000007A     7D - STORE_FAST          'min'
                             0000007D     64 - LOAD_CONST          0.90000000000000002
                             00000080     7D - STORE_FAST          'max'
                             00000083     7C - LOAD_FAST           'fFinal'
                             00000086     7C - LOAD_FAST           'min'
                             00000089     6A - COMPARE_OP          "<"
                             0000008C     6F - JUMP_IF_FALSE       -> 00000099
                             0000008F     01 - POP_TOP             
                             00000090     7C - LOAD_FAST           'min'
                             00000093     7D - STORE_FAST          'fFinal'
                             00000096     6E - JUMP_FORWARD        -> 000000B1
                             00000099     01 - POP_TOP             
                             0000009A     7C - LOAD_FAST           'fFinal'
                             0000009D     7C - LOAD_FAST           'max'
                             000000A0     6A - COMPARE_OP          ">"
                             000000A3     6F - JUMP_IF_FALSE       -> 000000B0
                             000000A6     01 - POP_TOP             
                             000000A7     7C - LOAD_FAST           'max'
                             000000AA     7D - STORE_FAST          'fFinal'
                             000000AD     6E - JUMP_FORWARD        -> 000000B1
                             000000B0     01 - POP_TOP             
                             000000B1     74 - LOAD_GLOBAL         'random'
                             000000B4     69 - LOAD_ATTR           'randrange'
                             000000B7     64 - LOAD_CONST          1
                             000000BA     64 - LOAD_CONST          100
                             000000BD     83 - CALL_FUNCTION       r0002
                             000000C0     7D - STORE_FAST          'roll'
                             000000C3     7C - LOAD_FAST           'roll'
                             000000C6     74 - LOAD_GLOBAL         'int'
                             000000C9     7C - LOAD_FAST           'fFinal'
                             000000CC     64 - LOAD_CONST          100.0
                             000000CF     14 - BINARY_MULTIPLY     
                             000000D0     83 - CALL_FUNCTION       r0001
                             000000D3     6A - COMPARE_OP          "<="
                             000000D6     7D - STORE_FAST          'bResisted'
                             000000D9     7C - LOAD_FAST           'bResisted'
                             000000DC     6F - JUMP_IF_FALSE       -> 000000F3
                             000000DF     01 - POP_TOP             
                             000000E0     74 - LOAD_GLOBAL         'CU'
                             000000E3     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             000000E6     64 - LOAD_CONST          'Cast Through: SUCCESS'
                             000000E9     64 - LOAD_CONST          21
                             000000EC     83 - CALL_FUNCTION       r0002
                             000000EF     01 - POP_TOP             
                             000000F0     6E - JUMP_FORWARD        -> 00000104
                             000000F3     01 - POP_TOP             
                             000000F4     74 - LOAD_GLOBAL         'CU'
                             000000F7     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             000000FA     64 - LOAD_CONST          'Cast Through: FAILED'
                             000000FD     64 - LOAD_CONST          21
                             00000100     83 - CALL_FUNCTION       r0002
                             00000103     01 - POP_TOP             
                             00000104     7C - LOAD_FAST           'bResisted'
                             00000107     53 - RETURN_VALUE        
                             00000108     64 - LOAD_CONST          None
                             0000010B     53 - RETURN_VALUE        
                         consts:
000039CB                     TUPLE: (
000039D0                         None (4E),
000039D1                         FLOAT: 0.75 (04 30 2E 37 35),
000039D7                         FLOAT: 0.0050000000000000001 (15 30 2E 30 30 35 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 31),
000039EE                         INT: 0 (00 00 00 00),
000039F3                         STR: 'CastThrough Def(%g) - Atk(%g) = chance(%g)' (2A 00 00 00 43 61 73 74 54 68 72 6F 75 67 68 20 44 65 66 28 25 67 29 20 2D 20 41 74 6B 28 25 67 29 20 3D 20 63 68 61 6E 63 65 28 25 67 29),
00003A22                         INT: 21 (15 00 00 00),
00003A27                         FLOAT: 0.33000000000000002 (13 30 2E 33 33 30 30 30 30 30 30 30 30 30 30 30 30 30 30 32),
00003A3C                         FLOAT: 0.90000000000000002 (13 30 2E 39 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 32),
00003A51                         INT: 1 (01 00 00 00),
00003A56                         INT: 100 (64 00 00 00),
00003A5B                         FLOAT: 100.0 (05 31 30 30 2E 30),
00003A62                         STR: 'Cast Through: SUCCESS' (15 00 00 00 43 61 73 74 20 54 68 72 6F 75 67 68 3A 20 53 55 43 43 45 53 53),
00003A7C                         STR: 'Cast Through: FAILED' (14 00 00 00 43 61 73 74 20 54 68 72 6F 75 67 68 3A 20 46 41 49 4C 45 44)
                             )
                         names:
00003A95                     TUPLE: (
00003A9A                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
00003AA4                         STR: 'bResisted' (09 00 00 00 62 52 65 73 69 73 74 65 64),
00003AB2                         STR: 'float' (05 00 00 00 66 6C 6F 61 74),
00003ABC                         STR: 'damageAmount' (0C 00 00 00 64 61 6D 61 67 65 41 6D 6F 75 6E 74),
00003ACD                         STR: 'maxHealth' (09 00 00 00 6D 61 78 48 65 61 6C 74 68),
00003ADB                         STR: 'percentOfLeftTaken' (12 00 00 00 70 65 72 63 65 6E 74 4F 66 4C 65 66 74 54 61 6B 65 6E),
00003AF2                         STR: 'attackerMod' (0B 00 00 00 61 74 74 61 63 6B 65 72 4D 6F 64),
00003B02                         STR: 'basicChance' (0B 00 00 00 62 61 73 69 63 43 68 61 6E 63 65),
00003B12                         STR: 'concentrationValue' (12 00 00 00 63 6F 6E 63 65 6E 74 72 61 74 69 6F 6E 56 61 6C 75 65),
00003B29                         STR: 'concentrationChance' (13 00 00 00 63 6F 6E 63 65 6E 74 72 61 74 69 6F 6E 43 68 61 6E 63 65),
00003B41                         STR: 'lvlChance' (09 00 00 00 6C 76 6C 43 68 61 6E 63 65),
00003B4F                         STR: 'fDefenderChance' (0F 00 00 00 66 44 65 66 65 6E 64 65 72 43 68 61 6E 63 65),
00003B63                         STR: 'fAttackerChance' (0F 00 00 00 66 41 74 74 61 63 6B 65 72 43 68 61 6E 63 65),
00003B77                         STR: 'fFinal' (06 00 00 00 66 46 69 6E 61 6C),
00003B82                         STR: 'CU' (02 00 00 00 43 55),
00003B89                         STR: 'outputCombatDebugMessageOnMatch' (1F 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 4F 6E 4D 61 74 63 68),
00003BAD                         STR: 'min' (03 00 00 00 6D 69 6E),
00003BB5                         STR: 'max' (03 00 00 00 6D 61 78),
00003BBD                         STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00003BC8                         STR: 'randrange' (09 00 00 00 72 61 6E 64 72 61 6E 67 65),
00003BD6                         STR: 'roll' (04 00 00 00 72 6F 6C 6C),
00003BDF                         STR: 'int' (03 00 00 00 69 6E 74)
                             )
                         varnames:
00003BE7                     TUPLE: (
00003BEC                         STR: 'damageAmount' (0C 00 00 00 64 61 6D 61 67 65 41 6D 6F 75 6E 74),
00003BFD                         STR: 'maxHealth' (09 00 00 00 6D 61 78 48 65 61 6C 74 68),
00003C0B                         STR: 'maxHealthBuffValue' (12 00 00 00 6D 61 78 48 65 61 6C 74 68 42 75 66 66 56 61 6C 75 65),
00003C22                         STR: 'charLvl' (07 00 00 00 63 68 61 72 4C 76 6C),
00003C2E                         STR: 'concentrationValue' (12 00 00 00 63 6F 6E 63 65 6E 74 72 61 74 69 6F 6E 56 61 6C 75 65),
00003C45                         STR: 'basicChance' (0B 00 00 00 62 61 73 69 63 43 68 61 6E 63 65),
00003C55                         STR: 'bResisted' (09 00 00 00 62 52 65 73 69 73 74 65 64),
00003C63                         STR: 'percentOfLeftTaken' (12 00 00 00 70 65 72 63 65 6E 74 4F 66 4C 65 66 74 54 61 6B 65 6E),
00003C7A                         STR: 'min' (03 00 00 00 6D 69 6E),
00003C82                         STR: 'fAttackerChance' (0F 00 00 00 66 41 74 74 61 63 6B 65 72 43 68 61 6E 63 65),
00003C96                         STR: 'fDefenderChance' (0F 00 00 00 66 44 65 66 65 6E 64 65 72 43 68 61 6E 63 65),
00003CAA                         STR: 'lvlChance' (09 00 00 00 6C 76 6C 43 68 61 6E 63 65),
00003CB8                         STR: 'roll' (04 00 00 00 72 6F 6C 6C),
00003CC1                         STR: 'concentrationChance' (13 00 00 00 63 6F 6E 63 65 6E 74 72 61 74 69 6F 6E 43 68 61 6E 63 65),
00003CD9                         STR: 'max' (03 00 00 00 6D 61 78),
00003CE1                         STR: 'attackerMod' (0B 00 00 00 61 74 74 61 63 6B 65 72 4D 6F 64),
00003CF1                         STR: 'fFinal' (06 00 00 00 66 46 69 6E 61 6C)
                             )
                         freevars:
00003CFC                     TUPLE: ()
                         cellvars:
00003D01                     TUPLE: ()
                         filename:
00003D06                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat_calculations.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73 2E 70 79)
                         name:
00003D56                     STR: 'DamageInterruptsCasting' (17 00 00 00 44 61 6D 61 67 65 49 6E 74 65 72 72 75 70 74 73 43 61 73 74 69 6E 67)
                         firslineno:
00003D72                     LONG: 463L (CF 01 00 00)
                         lnotab:
00003D76                     STR: '\x00\x02\x06\x01\x10\x01\x06\x01\x06\x01\x10\x01\x06\x02\x0e\x01\n\x01\n\x01\x1d\x03\x06\x01\x06\x02\r\x01\n\x01\r\x01\n\x03\x12\x01\x16\x02\x07\x01\x14\x02\x10\x02' (2C 00 00 00 00 02 06 01 10 01 06 01 06 01 10 01 06 02 0E 01 0A 01 0A 01 1D 03 06 01 06 02 0D 01 0A 01 0D 01 0A 03 12 01 16 02 07 01 14 02 10 02),
00003DA7             CODE:
                         argcount:
00003DA8                     LONG: 5L (05 00 00 00)
                         nlocals:
00003DAC                     LONG: 8L (08 00 00 00)
                         stacksize:
00003DB0                     LONG: 5L (05 00 00 00)
                         flags:
00003DB4                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00003DB8                     STR: '|\x00\x00}\x05\x00d\x01\x00|\x01\x00d\x02\x00\x15\x17}\x07\x00|\x05\x00|\x02\x007}\x05\x00t\x05\x00i\x06\x00d\x03\x00|\x02\x00|\x05\x00f\x02\x00\x16d\x04\x00\x83\x02\x00\x01|\x03\x00d\x05\x00j\x03\x00o;\x00\x01|\x05\x00t\x08\x00t\t\x00|\x03\x00\x83\x01\x00|\x07\x00\x14\x83\x01\x007}\x05\x00t\x05\x00i\x06\x00d\x06\x00|\x03\x00|\x07\x00|\x05\x00f\x03\x00\x16d\x04\x00\x83\x02\x00\x01n\x01\x00\x01t\n\x00|\x04\x00\x83\x01\x00}\x06\x00t\x08\x00t\t\x00|\x05\x00\x83\x01\x00|\x06\x00\x14\x83\x01\x00}\x05\x00t\x05\x00i\x06\x00d\x07\x00|\x06\x00|\x05\x00f\x02\x00\x16d\x04\x00\x83\x02\x00\x01t\x08\x00|\x05\x00\x83\x01\x00Sd\x00\x00S' (CA 00 00 00 7C 00 00 7D 05 00 64 01 00 7C 01 00 64 02 00 15 17 7D 07 00 7C 05 00 7C 02 00 37 7D 05 00 74 05 00 69 06 00 64 03 00 7C 02 00 7C 05 00 66 02 00 16 64 04 00 83 02 00 01 7C 03 00 64 05 00 6A 03 00 6F 3B 00 01 7C 05 00 74 08 00 74 09 00 7C 03 00 83 01 00 7C 07 00 14 83 01 00 37 7D 05 00 74 05 00 69 06 00 64 06 00 7C 03 00 7C 07 00 7C 05 00 66 03 00 16 64 04 00 83 02 00 01 6E 01 00 01 74 0A 00 7C 04 00 83 01 00 7D 06 00 74 08 00 74 09 00 7C 05 00 83 01 00 7C 06 00 14 83 01 00 7D 05 00 74 05 00 69 06 00 64 07 00 7C 06 00 7C 05 00 66 02 00 16 64 04 00 83 02 00 01 74 08 00 7C 05 00 83 01 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'curDamageValue'
                             00000003     7D - STORE_FAST          'damageTotal'
                             00000006     64 - LOAD_CONST          1.0
                             00000009     7C - LOAD_FAST           'damageTypeInfluence'
                             0000000C     64 - LOAD_CONST          100.0
                             0000000F     15 - BINARY_DIVIDE       
                             00000010     17 - BINARY_ADD          
                             00000011     7D - STORE_FAST          'damageTypeInfluencePercent'
                             00000014     7C - LOAD_FAST           'damageTotal'
                             00000017     7C - LOAD_FAST           'damageBonus'
                             0000001A     37 - INPLACE_ADD         
                             0000001B     7D - STORE_FAST          'damageTotal'
                             0000001E     74 - LOAD_GLOBAL         'CU'
                             00000021     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000024     64 - LOAD_CONST          'Ability Damage with %d damageBonus = %d'
                             00000027     7C - LOAD_FAST           'damageBonus'
                             0000002A     7C - LOAD_FAST           'damageTotal'
                             0000002D     66 - BUILD_TUPLE         r0002
                             00000030     16 - BINARY_MODULO       
                             00000031     64 - LOAD_CONST          20
                             00000034     83 - CALL_FUNCTION       r0002
                             00000037     01 - POP_TOP             
                             00000038     7C - LOAD_FAST           'weaponDamage'
                             0000003B     64 - LOAD_CONST          0
                             0000003E     6A - COMPARE_OP          "!="
                             00000041     6F - JUMP_IF_FALSE       -> 0000007F
                             00000044     01 - POP_TOP             
                             00000045     7C - LOAD_FAST           'damageTotal'
                             00000048     74 - LOAD_GLOBAL         'int'
                             0000004B     74 - LOAD_GLOBAL         'float'
                             0000004E     7C - LOAD_FAST           'weaponDamage'
                             00000051     83 - CALL_FUNCTION       r0001
                             00000054     7C - LOAD_FAST           'damageTypeInfluencePercent'
                             00000057     14 - BINARY_MULTIPLY     
                             00000058     83 - CALL_FUNCTION       r0001
                             0000005B     37 - INPLACE_ADD         
                             0000005C     7D - STORE_FAST          'damageTotal'
                             0000005F     74 - LOAD_GLOBAL         'CU'
                             00000062     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000065     64 - LOAD_CONST          'Ability Damage with weapon bonus (weapDmg(%d)*DamageInflu(%f))+curDamage = %d'
                             00000068     7C - LOAD_FAST           'weaponDamage'
                             0000006B     7C - LOAD_FAST           'damageTypeInfluencePercent'
                             0000006E     7C - LOAD_FAST           'damageTotal'
                             00000071     66 - BUILD_TUPLE         r0003
                             00000074     16 - BINARY_MODULO       
                             00000075     64 - LOAD_CONST          20
                             00000078     83 - CALL_FUNCTION       r0002
                             0000007B     01 - POP_TOP             
                             0000007C     6E - JUMP_FORWARD        -> 00000080
                             0000007F     01 - POP_TOP             
                             00000080     74 - LOAD_GLOBAL         'GetTacticDamageMod'
                             00000083     7C - LOAD_FAST           'eTacticTypeUsed'
                             00000086     83 - CALL_FUNCTION       r0001
                             00000089     7D - STORE_FAST          'tacticDamagePercentMod'
                             0000008C     74 - LOAD_GLOBAL         'int'
                             0000008F     74 - LOAD_GLOBAL         'float'
                             00000092     7C - LOAD_FAST           'damageTotal'
                             00000095     83 - CALL_FUNCTION       r0001
                             00000098     7C - LOAD_FAST           'tacticDamagePercentMod'
                             0000009B     14 - BINARY_MULTIPLY     
                             0000009C     83 - CALL_FUNCTION       r0001
                             0000009F     7D - STORE_FAST          'damageTotal'
                             000000A2     74 - LOAD_GLOBAL         'CU'
                             000000A5     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             000000A8     64 - LOAD_CONST          'Ability Damage with %g tacticBonus = %d'
                             000000AB     7C - LOAD_FAST           'tacticDamagePercentMod'
                             000000AE     7C - LOAD_FAST           'damageTotal'
                             000000B1     66 - BUILD_TUPLE         r0002
                             000000B4     16 - BINARY_MODULO       
                             000000B5     64 - LOAD_CONST          20
                             000000B8     83 - CALL_FUNCTION       r0002
                             000000BB     01 - POP_TOP             
                             000000BC     74 - LOAD_GLOBAL         'int'
                             000000BF     7C - LOAD_FAST           'damageTotal'
                             000000C2     83 - CALL_FUNCTION       r0001
                             000000C5     53 - RETURN_VALUE        
                             000000C6     64 - LOAD_CONST          None
                             000000C9     53 - RETURN_VALUE        
                         consts:
00003E87                     TUPLE: (
00003E8C                         None (4E),
00003E8D                         FLOAT: 1.0 (03 31 2E 30),
00003E92                         FLOAT: 100.0 (05 31 30 30 2E 30),
00003E99                         STR: 'Ability Damage with %d damageBonus = %d' (27 00 00 00 41 62 69 6C 69 74 79 20 44 61 6D 61 67 65 20 77 69 74 68 20 25 64 20 64 61 6D 61 67 65 42 6F 6E 75 73 20 3D 20 25 64),
00003EC5                         INT: 20 (14 00 00 00),
00003ECA                         INT: 0 (00 00 00 00),
00003ECF                         STR: 'Ability Damage with weapon bonus (weapDmg(%d)*DamageInflu(%f))+curDamage = %d' (4D 00 00 00 41 62 69 6C 69 74 79 20 44 61 6D 61 67 65 20 77 69 74 68 20 77 65 61 70 6F 6E 20 62 6F 6E 75 73 20 28 77 65 61 70 44 6D 67 28 25 64 29 2A 44 61 6D 61 67 65 49 6E 66 6C 75 28 25 66 29 29 2B 63 75 72 44 61 6D 61 67 65 20 3D 20 25 64),
00003F21                         STR: 'Ability Damage with %g tacticBonus = %d' (27 00 00 00 41 62 69 6C 69 74 79 20 44 61 6D 61 67 65 20 77 69 74 68 20 25 67 20 74 61 63 74 69 63 42 6F 6E 75 73 20 3D 20 25 64)
                             )
                         names:
00003F4D                     TUPLE: (
00003F52                         STR: 'curDamageValue' (0E 00 00 00 63 75 72 44 61 6D 61 67 65 56 61 6C 75 65),
00003F65                         STR: 'damageTotal' (0B 00 00 00 64 61 6D 61 67 65 54 6F 74 61 6C),
00003F75                         STR: 'damageTypeInfluence' (13 00 00 00 64 61 6D 61 67 65 54 79 70 65 49 6E 66 6C 75 65 6E 63 65),
00003F8D                         STR: 'damageTypeInfluencePercent' (1A 00 00 00 64 61 6D 61 67 65 54 79 70 65 49 6E 66 6C 75 65 6E 63 65 50 65 72 63 65 6E 74),
00003FAC                         STR: 'damageBonus' (0B 00 00 00 64 61 6D 61 67 65 42 6F 6E 75 73),
00003FBC                         STR: 'CU' (02 00 00 00 43 55),
00003FC3                         STR: 'outputCombatDebugMessageOnMatch' (1F 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 4F 6E 4D 61 74 63 68),
00003FE7                         STR: 'weaponDamage' (0C 00 00 00 77 65 61 70 6F 6E 44 61 6D 61 67 65),
00003FF8                         STR: 'int' (03 00 00 00 69 6E 74),
00004000                         STR: 'float' (05 00 00 00 66 6C 6F 61 74),
0000400A                         STR: 'GetTacticDamageMod' (12 00 00 00 47 65 74 54 61 63 74 69 63 44 61 6D 61 67 65 4D 6F 64),
00004021                         STR: 'eTacticTypeUsed' (0F 00 00 00 65 54 61 63 74 69 63 54 79 70 65 55 73 65 64),
00004035                         STR: 'tacticDamagePercentMod' (16 00 00 00 74 61 63 74 69 63 44 61 6D 61 67 65 50 65 72 63 65 6E 74 4D 6F 64)
                             )
                         varnames:
00004050                     TUPLE: (
00004055                         STR: 'curDamageValue' (0E 00 00 00 63 75 72 44 61 6D 61 67 65 56 61 6C 75 65),
00004068                         STR: 'damageTypeInfluence' (13 00 00 00 64 61 6D 61 67 65 54 79 70 65 49 6E 66 6C 75 65 6E 63 65),
00004080                         STR: 'damageBonus' (0B 00 00 00 64 61 6D 61 67 65 42 6F 6E 75 73),
00004090                         STR: 'weaponDamage' (0C 00 00 00 77 65 61 70 6F 6E 44 61 6D 61 67 65),
000040A1                         STR: 'eTacticTypeUsed' (0F 00 00 00 65 54 61 63 74 69 63 54 79 70 65 55 73 65 64),
000040B5                         STR: 'damageTotal' (0B 00 00 00 64 61 6D 61 67 65 54 6F 74 61 6C),
000040C5                         STR: 'tacticDamagePercentMod' (16 00 00 00 74 61 63 74 69 63 44 61 6D 61 67 65 50 65 72 63 65 6E 74 4D 6F 64),
000040E0                         STR: 'damageTypeInfluencePercent' (1A 00 00 00 64 61 6D 61 67 65 54 79 70 65 49 6E 66 6C 75 65 6E 63 65 50 65 72 63 65 6E 74)
                             )
                         freevars:
000040FF                     TUPLE: ()
                         cellvars:
00004104                     TUPLE: ()
                         filename:
00004109                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat_calculations.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73 2E 70 79)
                         name:
00004159                     STR: 'GetFullAbilityDamage' (14 00 00 00 47 65 74 46 75 6C 6C 41 62 69 6C 69 74 79 44 61 6D 61 67 65)
                         firslineno:
00004172                     LONG: 505L (F9 01 00 00)
                         lnotab:
00004176                     STR: '\x00\x02\x06\x01\x0e\t\n\x01\x1a\x03\r\x01\x1a\x01!\x03\x0c\x01\x16\x01\x1a\x02' (16 00 00 00 00 02 06 01 0E 09 0A 01 1A 03 0D 01 1A 01 21 03 0C 01 16 01 1A 02),
00004191             CODE:
                         argcount:
00004192                     LONG: 3L (03 00 00 00)
                         nlocals:
00004196                     LONG: 11L (0B 00 00 00)
                         stacksize:
0000419A                     LONG: 7L (07 00 00 00)
                         flags:
0000419E                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000041A2                     STR: 'd\x01\x00}\x08\x00d\x02\x00}\x04\x00t\x02\x00|\x02\x00\x83\x01\x00|\x04\x00\x15}\x03\x00|\x03\x00t\x02\x00|\x01\x00\x83\x01\x00\x18}\x05\x00d\x03\x00}\x07\x00d\x04\x00}\x06\x00d\x05\x00}\t\x00t\n\x00i\x0b\x00d\x06\x00|\x00\x00|\x01\x00|\x02\x00|\x03\x00|\x05\x00f\x05\x00\x16d\x07\x00\x83\x02\x00\x01|\x05\x00d\x08\x00j\x01\x00o\x1c\x00\x01t\n\x00i\x0b\x00d\t\x00|\x00\x00\x16d\x07\x00\x83\x02\x00\x01|\x00\x00Sn\x01\x00\x01d\x05\x00|\x05\x00|\x07\x00\x14\x18}\n\x00|\n\x00d\x04\x00j\x00\x00o\n\x00\x01d\x04\x00}\n\x00n\x18\x00\x01|\n\x00d\x05\x00j\x04\x00o\n\x00\x01d\x05\x00}\n\x00n\x01\x00\x01|\x00\x00|\n\x00\x14}\x08\x00t\n\x00i\x0b\x00d\n\x00|\x08\x00|\n\x00f\x02\x00\x16d\x07\x00\x83\x02\x00\x01|\x08\x00Sd\x00\x00S' (F2 00 00 00 64 01 00 7D 08 00 64 02 00 7D 04 00 74 02 00 7C 02 00 83 01 00 7C 04 00 15 7D 03 00 7C 03 00 74 02 00 7C 01 00 83 01 00 18 7D 05 00 64 03 00 7D 07 00 64 04 00 7D 06 00 64 05 00 7D 09 00 74 0A 00 69 0B 00 64 06 00 7C 00 00 7C 01 00 7C 02 00 7C 03 00 7C 05 00 66 05 00 16 64 07 00 83 02 00 01 7C 05 00 64 08 00 6A 01 00 6F 1C 00 01 74 0A 00 69 0B 00 64 09 00 7C 00 00 16 64 07 00 83 02 00 01 7C 00 00 53 6E 01 00 01 64 05 00 7C 05 00 7C 07 00 14 18 7D 0A 00 7C 0A 00 64 04 00 6A 00 00 6F 0A 00 01 64 04 00 7D 0A 00 6E 18 00 01 7C 0A 00 64 05 00 6A 04 00 6F 0A 00 01 64 05 00 7D 0A 00 6E 01 00 01 7C 00 00 7C 0A 00 14 7D 08 00 74 0A 00 69 0B 00 64 0A 00 7C 08 00 7C 0A 00 66 02 00 16 64 07 00 83 02 00 01 7C 08 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          0.0
                             00000003     7D - STORE_FAST          'fNewDuration'
                             00000006     64 - LOAD_CONST          5.0
                             00000009     7D - STORE_FAST          'fDerminationPerLevel'
                             0000000C     74 - LOAD_GLOBAL         'float'
                             0000000F     7C - LOAD_FAST           'determinationLvl'
                             00000012     83 - CALL_FUNCTION       r0001
                             00000015     7C - LOAD_FAST           'fDerminationPerLevel'
                             00000018     15 - BINARY_DIVIDE       
                             00000019     7D - STORE_FAST          'targetLevel'
                             0000001C     7C - LOAD_FAST           'targetLevel'
                             0000001F     74 - LOAD_GLOBAL         'float'
                             00000022     7C - LOAD_FAST           'casterLvl'
                             00000025     83 - CALL_FUNCTION       r0001
                             00000028     18 - BINARY_SUBTRACT     
                             00000029     7D - STORE_FAST          'levelDef'
                             0000002C     64 - LOAD_CONST          0.066000000000000003
                             0000002F     7D - STORE_FAST          'Nob'
                             00000032     64 - LOAD_CONST          0.33000000000000002
                             00000035     7D - STORE_FAST          'clampLow'
                             00000038     64 - LOAD_CONST          1.0
                             0000003B     7D - STORE_FAST          'clampHigh'
                             0000003E     74 - LOAD_GLOBAL         'CU'
                             00000041     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000044     64 - LOAD_CONST          'Mit. Dur. Input: duration(%g), caster(%d), target(%d -> %g), lvlDef(%g)'
                             00000047     7C - LOAD_FAST           'fCurDuration'
                             0000004A     7C - LOAD_FAST           'casterLvl'
                             0000004D     7C - LOAD_FAST           'determinationLvl'
                             00000050     7C - LOAD_FAST           'targetLevel'
                             00000053     7C - LOAD_FAST           'levelDef'
                             00000056     66 - BUILD_TUPLE         r0005
                             00000059     16 - BINARY_MODULO       
                             0000005A     64 - LOAD_CONST          22
                             0000005D     83 - CALL_FUNCTION       r0002
                             00000060     01 - POP_TOP             
                             00000061     7C - LOAD_FAST           'levelDef'
                             00000064     64 - LOAD_CONST          0
                             00000067     6A - COMPARE_OP          "<="
                             0000006A     6F - JUMP_IF_FALSE       -> 00000089
                             0000006D     01 - POP_TOP             
                             0000006E     74 - LOAD_GLOBAL         'CU'
                             00000071     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000074     64 - LOAD_CONST          'Mit. Dur. Output: duration(%g)'
                             00000077     7C - LOAD_FAST           'fCurDuration'
                             0000007A     16 - BINARY_MODULO       
                             0000007B     64 - LOAD_CONST          22
                             0000007E     83 - CALL_FUNCTION       r0002
                             00000081     01 - POP_TOP             
                             00000082     7C - LOAD_FAST           'fCurDuration'
                             00000085     53 - RETURN_VALUE        
                             00000086     6E - JUMP_FORWARD        -> 0000008A
                             00000089     01 - POP_TOP             
                             0000008A     64 - LOAD_CONST          1.0
                             0000008D     7C - LOAD_FAST           'levelDef'
                             00000090     7C - LOAD_FAST           'Nob'
                             00000093     14 - BINARY_MULTIPLY     
                             00000094     18 - BINARY_SUBTRACT     
                             00000095     7D - STORE_FAST          'durationScale'
                             00000098     7C - LOAD_FAST           'durationScale'
                             0000009B     64 - LOAD_CONST          0.33000000000000002
                             0000009E     6A - COMPARE_OP          "<"
                             000000A1     6F - JUMP_IF_FALSE       -> 000000AE
                             000000A4     01 - POP_TOP             
                             000000A5     64 - LOAD_CONST          0.33000000000000002
                             000000A8     7D - STORE_FAST          'durationScale'
                             000000AB     6E - JUMP_FORWARD        -> 000000C6
                             000000AE     01 - POP_TOP             
                             000000AF     7C - LOAD_FAST           'durationScale'
                             000000B2     64 - LOAD_CONST          1.0
                             000000B5     6A - COMPARE_OP          ">"
                             000000B8     6F - JUMP_IF_FALSE       -> 000000C5
                             000000BB     01 - POP_TOP             
                             000000BC     64 - LOAD_CONST          1.0
                             000000BF     7D - STORE_FAST          'durationScale'
                             000000C2     6E - JUMP_FORWARD        -> 000000C6
                             000000C5     01 - POP_TOP             
                             000000C6     7C - LOAD_FAST           'fCurDuration'
                             000000C9     7C - LOAD_FAST           'durationScale'
                             000000CC     14 - BINARY_MULTIPLY     
                             000000CD     7D - STORE_FAST          'fNewDuration'
                             000000D0     74 - LOAD_GLOBAL         'CU'
                             000000D3     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             000000D6     64 - LOAD_CONST          'Mit. Dur. Output: duration(%g) mod(%g)'
                             000000D9     7C - LOAD_FAST           'fNewDuration'
                             000000DC     7C - LOAD_FAST           'durationScale'
                             000000DF     66 - BUILD_TUPLE         r0002
                             000000E2     16 - BINARY_MODULO       
                             000000E3     64 - LOAD_CONST          22
                             000000E6     83 - CALL_FUNCTION       r0002
                             000000E9     01 - POP_TOP             
                             000000EA     7C - LOAD_FAST           'fNewDuration'
                             000000ED     53 - RETURN_VALUE        
                             000000EE     64 - LOAD_CONST          None
                             000000F1     53 - RETURN_VALUE        
                         consts:
00004299                     TUPLE: (
0000429E                         None (4E),
0000429F                         FLOAT: 0.0 (03 30 2E 30),
000042A4                         FLOAT: 5.0 (03 35 2E 30),
000042A9                         FLOAT: 0.066000000000000003 (14 30 2E 30 36 36 30 30 30 30 30 30 30 30 30 30 30 30 30 30 33),
000042BF                         FLOAT: 0.33000000000000002 (13 30 2E 33 33 30 30 30 30 30 30 30 30 30 30 30 30 30 30 32),
000042D4                         FLOAT: 1.0 (03 31 2E 30),
000042D9                         STR: 'Mit. Dur. Input: duration(%g), caster(%d), target(%d -> %g), lvlDef(%g)' (47 00 00 00 4D 69 74 2E 20 44 75 72 2E 20 49 6E 70 75 74 3A 20 64 75 72 61 74 69 6F 6E 28 25 67 29 2C 20 63 61 73 74 65 72 28 25 64 29 2C 20 74 61 72 67 65 74 28 25 64 20 2D 3E 20 25 67 29 2C 20 6C 76 6C 44 65 66 28 25 67 29),
00004325                         INT: 22 (16 00 00 00),
0000432A                         INT: 0 (00 00 00 00),
0000432F                         STR: 'Mit. Dur. Output: duration(%g)' (1E 00 00 00 4D 69 74 2E 20 44 75 72 2E 20 4F 75 74 70 75 74 3A 20 64 75 72 61 74 69 6F 6E 28 25 67 29),
00004352                         STR: 'Mit. Dur. Output: duration(%g) mod(%g)' (26 00 00 00 4D 69 74 2E 20 44 75 72 2E 20 4F 75 74 70 75 74 3A 20 64 75 72 61 74 69 6F 6E 28 25 67 29 20 6D 6F 64 28 25 67 29)
                             )
                         names:
0000437D                     TUPLE: (
00004382                         STR: 'fNewDuration' (0C 00 00 00 66 4E 65 77 44 75 72 61 74 69 6F 6E),
00004393                         STR: 'fDerminationPerLevel' (14 00 00 00 66 44 65 72 6D 69 6E 61 74 69 6F 6E 50 65 72 4C 65 76 65 6C),
000043AC                         STR: 'float' (05 00 00 00 66 6C 6F 61 74),
000043B6                         STR: 'determinationLvl' (10 00 00 00 64 65 74 65 72 6D 69 6E 61 74 69 6F 6E 4C 76 6C),
000043CB                         STR: 'targetLevel' (0B 00 00 00 74 61 72 67 65 74 4C 65 76 65 6C),
000043DB                         STR: 'casterLvl' (09 00 00 00 63 61 73 74 65 72 4C 76 6C),
000043E9                         STR: 'levelDef' (08 00 00 00 6C 65 76 65 6C 44 65 66),
000043F6                         STR: 'Nob' (03 00 00 00 4E 6F 62),
000043FE                         STR: 'clampLow' (08 00 00 00 63 6C 61 6D 70 4C 6F 77),
0000440B                         STR: 'clampHigh' (09 00 00 00 63 6C 61 6D 70 48 69 67 68),
00004419                         STR: 'CU' (02 00 00 00 43 55),
00004420                         STR: 'outputCombatDebugMessageOnMatch' (1F 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 4F 6E 4D 61 74 63 68),
00004444                         STR: 'fCurDuration' (0C 00 00 00 66 43 75 72 44 75 72 61 74 69 6F 6E),
00004455                         STR: 'durationScale' (0D 00 00 00 64 75 72 61 74 69 6F 6E 53 63 61 6C 65)
                             )
                         varnames:
00004467                     TUPLE: (
0000446C                         STR: 'fCurDuration' (0C 00 00 00 66 43 75 72 44 75 72 61 74 69 6F 6E),
0000447D                         STR: 'casterLvl' (09 00 00 00 63 61 73 74 65 72 4C 76 6C),
0000448B                         STR: 'determinationLvl' (10 00 00 00 64 65 74 65 72 6D 69 6E 61 74 69 6F 6E 4C 76 6C),
000044A0                         STR: 'targetLevel' (0B 00 00 00 74 61 72 67 65 74 4C 65 76 65 6C),
000044B0                         STR: 'fDerminationPerLevel' (14 00 00 00 66 44 65 72 6D 69 6E 61 74 69 6F 6E 50 65 72 4C 65 76 65 6C),
000044C9                         STR: 'levelDef' (08 00 00 00 6C 65 76 65 6C 44 65 66),
000044D6                         STR: 'clampLow' (08 00 00 00 63 6C 61 6D 70 4C 6F 77),
000044E3                         STR: 'Nob' (03 00 00 00 4E 6F 62),
000044EB                         STR: 'fNewDuration' (0C 00 00 00 66 4E 65 77 44 75 72 61 74 69 6F 6E),
000044FC                         STR: 'clampHigh' (09 00 00 00 63 6C 61 6D 70 48 69 67 68),
0000450A                         STR: 'durationScale' (0D 00 00 00 64 75 72 61 74 69 6F 6E 53 63 61 6C 65)
                             )
                         freevars:
0000451C                     TUPLE: ()
                         cellvars:
00004521                     TUPLE: ()
                         filename:
00004526                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat_calculations.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73 2E 70 79)
                         name:
00004576                     STR: 'GetAbilityMitigationDuration' (1C 00 00 00 47 65 74 41 62 69 6C 69 74 79 4D 69 74 69 67 61 74 69 6F 6E 44 75 72 61 74 69 6F 6E)
                         firslineno:
00004597                     LONG: 540L (1C 02 00 00)
                         lnotab:
0000459B                     STR: '\x00\x02\x06\x01\x06\x01\x10\x01\x10\x01\x06\x01\x06\x01\x06\x01#\x03\r\x01\x14\x01\x08\x03\x0e\x03\r\x01\n\x03\r\x01\n\x02\n\x01\x1a\x02' (26 00 00 00 00 02 06 01 06 01 10 01 10 01 06 01 06 01 06 01 23 03 0D 01 14 01 08 03 0E 03 0D 01 0A 03 0D 01 0A 02 0A 01 1A 02)
                 )
             names:
000045C6         TUPLE: (
000045CB             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
000045D6             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
000045E4             STR: 'obj' (03 00 00 00 6F 62 6A),
000045EC             STR: 'combat_defines' (0E 00 00 00 63 6F 6D 62 61 74 5F 64 65 66 69 6E 65 73),
000045FF             STR: 'CD' (02 00 00 00 43 44),
00004606             STR: 'math' (04 00 00 00 6D 61 74 68),
0000460F             STR: 'interlock.combat_utility' (18 00 00 00 69 6E 74 65 72 6C 6F 63 6B 2E 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79),
0000462C             STR: 'combat_utility' (0E 00 00 00 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79),
0000463F             STR: 'CU' (02 00 00 00 43 55),
00004646             STR: 'calcDamageWithGun' (11 00 00 00 63 61 6C 63 44 61 6D 61 67 65 57 69 74 68 47 75 6E),
0000465C             STR: 'GetTacticCombatTacticsMod' (19 00 00 00 47 65 74 54 61 63 74 69 63 43 6F 6D 62 61 74 54 61 63 74 69 63 73 4D 6F 64),
0000467A             STR: 'GetTacticDefenseTacticsMod' (1A 00 00 00 47 65 74 54 61 63 74 69 63 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 4D 6F 64),
00004699             STR: 'GetTacticDamageMod' (12 00 00 00 47 65 74 54 61 63 74 69 63 44 61 6D 61 67 65 4D 6F 64),
000046B0             STR: 'GetTacticWithdrawTacticsMod' (1B 00 00 00 47 65 74 54 61 63 74 69 63 57 69 74 68 64 72 61 77 54 61 63 74 69 63 73 4D 6F 64),
000046D0             STR: 'GetFreeAttackDamage' (13 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65),
000046E8             STR: 'GetFreeAttackDamageMelee' (18 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65 4D 65 6C 65 65),
00004705             STR: 'GetCloseCombatDamage' (14 00 00 00 47 65 74 43 6C 6F 73 65 43 6F 6D 62 61 74 44 61 6D 61 67 65),
0000471E             STR: 'GetCombatTacticRoll' (13 00 00 00 47 65 74 43 6F 6D 62 61 74 54 61 63 74 69 63 52 6F 6C 6C),
00004736             STR: 'GetDefenseTacticRoll' (14 00 00 00 47 65 74 44 65 66 65 6E 73 65 54 61 63 74 69 63 52 6F 6C 6C),
0000474F             STR: 'GetDamageReductionValue' (17 00 00 00 47 65 74 44 61 6D 61 67 65 52 65 64 75 63 74 69 6F 6E 56 61 6C 75 65),
0000476B             STR: 'GetShieldDamageValue' (14 00 00 00 47 65 74 53 68 69 65 6C 64 44 61 6D 61 67 65 56 61 6C 75 65),
00004784             STR: 'GetShieldResistanceISDrainValue' (1F 00 00 00 47 65 74 53 68 69 65 6C 64 52 65 73 69 73 74 61 6E 63 65 49 53 44 72 61 69 6E 56 61 6C 75 65),
000047A8             STR: 'DamageInterruptsCasting' (17 00 00 00 44 61 6D 61 67 65 49 6E 74 65 72 72 75 70 74 73 43 61 73 74 69 6E 67),
000047C4             STR: 'GetFullAbilityDamage' (14 00 00 00 47 65 74 46 75 6C 6C 41 62 69 6C 69 74 79 44 61 6D 61 67 65),
000047DD             STR: 'GetAbilityMitigationDuration' (1C 00 00 00 47 65 74 41 62 69 6C 69 74 79 4D 69 74 69 67 61 74 69 6F 6E 44 75 72 61 74 69 6F 6E)
                 )
             varnames:
000047FE         TUPLE: (
00004803             STR: 'GetTacticCombatTacticsMod' (19 00 00 00 47 65 74 54 61 63 74 69 63 43 6F 6D 62 61 74 54 61 63 74 69 63 73 4D 6F 64),
00004821             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
0000482C             STR: 'GetFullAbilityDamage' (14 00 00 00 47 65 74 46 75 6C 6C 41 62 69 6C 69 74 79 44 61 6D 61 67 65),
00004845             STR: 'calcDamageWithGun' (11 00 00 00 63 61 6C 63 44 61 6D 61 67 65 57 69 74 68 47 75 6E),
0000485B             STR: 'GetShieldResistanceISDrainValue' (1F 00 00 00 47 65 74 53 68 69 65 6C 64 52 65 73 69 73 74 61 6E 63 65 49 53 44 72 61 69 6E 56 61 6C 75 65),
0000487F             STR: 'GetAbilityMitigationDuration' (1C 00 00 00 47 65 74 41 62 69 6C 69 74 79 4D 69 74 69 67 61 74 69 6F 6E 44 75 72 61 74 69 6F 6E),
000048A0             STR: 'DamageInterruptsCasting' (17 00 00 00 44 61 6D 61 67 65 49 6E 74 65 72 72 75 70 74 73 43 61 73 74 69 6E 67),
000048BC             STR: 'GetShieldDamageValue' (14 00 00 00 47 65 74 53 68 69 65 6C 64 44 61 6D 61 67 65 56 61 6C 75 65),
000048D5             STR: 'math' (04 00 00 00 6D 61 74 68),
000048DE             STR: 'GetDamageReductionValue' (17 00 00 00 47 65 74 44 61 6D 61 67 65 52 65 64 75 63 74 69 6F 6E 56 61 6C 75 65),
000048FA             STR: 'GetFreeAttackDamageMelee' (18 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65 4D 65 6C 65 65),
00004917             STR: 'CD' (02 00 00 00 43 44),
0000491E             STR: 'GetFreeAttackDamage' (13 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65),
00004936             STR: 'CU' (02 00 00 00 43 55),
0000493D             STR: 'GetCloseCombatDamage' (14 00 00 00 47 65 74 43 6C 6F 73 65 43 6F 6D 62 61 74 44 61 6D 61 67 65),
00004956             STR: 'obj' (03 00 00 00 6F 62 6A),
0000495E             STR: 'GetTacticDefenseTacticsMod' (1A 00 00 00 47 65 74 54 61 63 74 69 63 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 4D 6F 64),
0000497D             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
0000498B             STR: 'GetCombatTacticRoll' (13 00 00 00 47 65 74 43 6F 6D 62 61 74 54 61 63 74 69 63 52 6F 6C 6C),
000049A3             STR: 'GetTacticWithdrawTacticsMod' (1B 00 00 00 47 65 74 54 61 63 74 69 63 57 69 74 68 64 72 61 77 54 61 63 74 69 63 73 4D 6F 64),
000049C3             STR: 'GetTacticDamageMod' (12 00 00 00 47 65 74 54 61 63 74 69 63 44 61 6D 61 67 65 4D 6F 64),
000049DA             STR: 'GetDefenseTacticRoll' (14 00 00 00 47 65 74 44 65 66 65 6E 73 65 54 61 63 74 69 63 52 6F 6C 6C)
                 )
             freevars:
000049F3         TUPLE: ()
             cellvars:
000049F8         TUPLE: ()
             filename:
000049FD         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat_calculations.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73 2E 70 79)
             name:
00004A4D         STR: '?' (01 00 00 00 3F)
             firslineno:
00004A53         LONG: 1L (01 00 00 00)
             lnotab:
00004A57         STR: "\t\x01\t\x01\t\x01\t\x01\t\x01\x0c\x02\t\r\t\x0f\t\x0e\t\x0f\t\x16\t7\t.\x0cF\t'\t\x1b\tB\t$\t%\t*\t#" (2A 00 00 00 09 01 09 01 09 01 09 01 09 01 0C 02 09 0D 09 0F 09 0E 09 0F 09 16 09 37 09 2E 0C 46 09 27 09 1B 09 42 09 24 09 25 09 2A 09 23)

