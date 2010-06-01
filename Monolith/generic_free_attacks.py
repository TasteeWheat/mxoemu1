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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00i\x03\x00Z\x04\x00d\x00\x00k\x05\x00i\x06\x00i\x07\x00Z\x08\x00d\x00\x00k\t\x00i\n\x00Z\x0b\x00d\x00\x00k\x0c\x00Z\r\x00d\x00\x00k\x0e\x00Z\x0f\x00d\x00\x00k\x10\x00Z\x11\x00d\x01\x00\x84\x00\x00Z\x12\x00d\x02\x00\x84\x00\x00Z\x13\x00d\x03\x00\x84\x00\x00Z\x14\x00d\x04\x00\x84\x00\x00Z\x15\x00d\x05\x00e\x15\x00_\x16\x00d\x06\x00\x84\x00\x00Z\x17\x00d\x07\x00e\x17\x00_\x16\x00d\x08\x00\x84\x00\x00Z\x18\x00d\t\x00e\x18\x00_\x16\x00d\n\x00\x84\x00\x00Z\x19\x00d\x0b\x00e\x19\x00_\x16\x00d\x0c\x00\x84\x00\x00Z\x1a\x00d\r\x00e\x1a\x00_\x16\x00d\x00\x00S' (CD 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 69 03 00 5A 04 00 64 00 00 6B 05 00 69 06 00 69 07 00 5A 08 00 64 00 00 6B 09 00 69 0A 00 5A 0B 00 64 00 00 6B 0C 00 5A 0D 00 64 00 00 6B 0E 00 5A 0F 00 64 00 00 6B 10 00 5A 11 00 64 01 00 84 00 00 5A 12 00 64 02 00 84 00 00 5A 13 00 64 03 00 84 00 00 5A 14 00 64 04 00 84 00 00 5A 15 00 64 05 00 65 15 00 5F 16 00 64 06 00 84 00 00 5A 17 00 64 07 00 65 17 00 5F 16 00 64 08 00 84 00 00 5A 18 00 64 09 00 65 18 00 5F 16 00 64 0A 00 84 00 00 5A 19 00 64 0B 00 65 19 00 5F 16 00 64 0C 00 84 00 00 5A 1A 00 64 0D 00 65 1A 00 5F 16 00 64 00 00 53)
                 00000000     64 - LOAD_CONST          None
                 00000003     6B - IMPORT_NAME         'random'
                 00000006     5A - STORE_NAME          'random'
                 00000009     64 - LOAD_CONST          None
                 0000000C     6B - IMPORT_NAME         'traceback'
                 0000000F     5A - STORE_NAME          'traceback'
                 00000012     64 - LOAD_CONST          None
                 00000015     6B - IMPORT_NAME         'interlock.combat_utility'
                 00000018     69 - LOAD_ATTR           'combat_utility'
                 0000001B     5A - STORE_NAME          'CU'
                 0000001E     64 - LOAD_CONST          None
                 00000021     6B - IMPORT_NAME         'ability.hacker.virii_defines'
                 00000024     69 - LOAD_ATTR           'hacker'
                 00000027     69 - LOAD_ATTR           'virii_defines'
                 0000002A     5A - STORE_NAME          'VIRII'
                 0000002D     64 - LOAD_CONST          None
                 00000030     6B - IMPORT_NAME         'ability.utility'
                 00000033     69 - LOAD_ATTR           'utility'
                 00000036     5A - STORE_NAME          'Utility'
                 00000039     64 - LOAD_CONST          None
                 0000003C     6B - IMPORT_NAME         'stringtable_client'
                 0000003F     5A - STORE_NAME          'StringTable'
                 00000042     64 - LOAD_CONST          None
                 00000045     6B - IMPORT_NAME         'ltfxmap'
                 00000048     5A - STORE_NAME          'FX'
                 0000004B     64 - LOAD_CONST          None
                 0000004E     6B - IMPORT_NAME         'combat_calculations'
                 00000051     5A - STORE_NAME          'CC'
                 00000054     64 - LOAD_CONST          CODE('GenericFreeAttackTest')
                 00000057     84 - MAKE_FUNCTION       r0000
                 0000005A     5A - STORE_NAME          'GenericFreeAttackTest'
                 0000005D     64 - LOAD_CONST          CODE('ComputeAttackerTotal')
                 00000060     84 - MAKE_FUNCTION       r0000
                 00000063     5A - STORE_NAME          'ComputeAttackerTotal'
                 00000066     64 - LOAD_CONST          CODE('ComputeDefenderTotal')
                 00000069     84 - MAKE_FUNCTION       r0000
                 0000006C     5A - STORE_NAME          'ComputeDefenderTotal'
                 0000006F     64 - LOAD_CONST          CODE('AbilityThrowFreeAttack')
                 00000072     84 - MAKE_FUNCTION       r0000
                 00000075     5A - STORE_NAME          'AbilityThrowFreeAttack'
                 00000078     64 - LOAD_CONST          '\ndirectObject.hasAbility[CurrentTacticAbility]\ndirectObject.hasAbility[ThrowDefenseTacticsAbility]\ndirectObject.abilities[ThrowDefenseTacticsAbility]\ndirectObject.abilities[ConsistencyAbility]\ndirectObject.abilities[CurrentTacticAbility]\ndirectObject.locator\n'
                 0000007B     65 - LOAD_NAME           'AbilityThrowFreeAttack'
                 0000007E     5F - STORE_ATTR          'depAttr'
                 00000081     64 - LOAD_CONST          CODE('AbilityMeleeFreeAttack')
                 00000084     84 - MAKE_FUNCTION       r0000
                 00000087     5A - STORE_NAME          'AbilityMeleeFreeAttack'
                 0000008A     64 - LOAD_CONST          '\ndirectObject.hasAbility[CurrentTacticAbility]\ndirectObject.hasAbility[MeleeDefenseTacticsAbility]\ndirectObject.abilities[MeleeDefenseTacticsAbility]\ndirectObject.abilities[ConsistencyAbility]\ndirectObject.abilities[CurrentTacticAbility]\ndirectObject.locator\n'
                 0000008D     65 - LOAD_NAME           'AbilityMeleeFreeAttack'
                 00000090     5F - STORE_ATTR          'depAttr'
                 00000093     64 - LOAD_CONST          CODE('AbilityRangeFreeAttack')
                 00000096     84 - MAKE_FUNCTION       r0000
                 00000099     5A - STORE_NAME          'AbilityRangeFreeAttack'
                 0000009C     64 - LOAD_CONST          '\ndirectObject.hasAbility[CurrentTacticAbility]\ndirectObject.hasAbility[RangedDefenseTacticsAbility]\ndirectObject.abilities[RangedDefenseTacticsAbility]\ndirectObject.abilities[ConsistencyAbility]\ndirectObject.abilities[CurrentTacticAbility]\ndirectObject.locator\n'
                 0000009F     65 - LOAD_NAME           'AbilityRangeFreeAttack'
                 000000A2     5F - STORE_ATTR          'depAttr'
                 000000A5     64 - LOAD_CONST          CODE('AbilityViralFreeAttack')
                 000000A8     84 - MAKE_FUNCTION       r0000
                 000000AB     5A - STORE_NAME          'AbilityViralFreeAttack'
                 000000AE     64 - LOAD_CONST          '\ndirectObject.hasAbility[CurrentTacticAbility]\ndirectObject.hasAbility[ViralDeflectionAbility]\ndirectObject.abilities[ViralDeflectionAbility]\ndirectObject.abilities[ConsistencyAbility]\ndirectObject.abilities[CurrentTacticAbility]\ndirectObject.locator\n'
                 000000B1     65 - LOAD_NAME           'AbilityViralFreeAttack'
                 000000B4     5F - STORE_ATTR          'depAttr'
                 000000B7     64 - LOAD_CONST          CODE('AbilityOutOfCombat')
                 000000BA     84 - MAKE_FUNCTION       r0000
                 000000BD     5A - STORE_NAME          'AbilityOutOfCombat'
                 000000C0     64 - LOAD_CONST          '\ndirectObject.locator\n'
                 000000C3     65 - LOAD_NAME           'AbilityOutOfCombat'
                 000000C6     5F - STORE_ATTR          'depAttr'
                 000000C9     64 - LOAD_CONST          None
                 000000CC     53 - RETURN_VALUE        
             consts:
000000EB         TUPLE: (
000000F0             None (4E),
000000F1             CODE:
                         argcount:
000000F2                     LONG: 4L (04 00 00 00)
                         nlocals:
000000F6                     LONG: 4L (04 00 00 00)
                         stacksize:
000000FA                     LONG: 6L (06 00 00 00)
                         flags:
000000FE                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000102                     STR: 't\x00\x00i\x01\x00d\x01\x00|\x01\x00|\x00\x00|\x03\x00|\x02\x00f\x04\x00\x16d\x02\x00\x83\x02\x00\x01|\x01\x00|\x03\x00j\x04\x00o\x08\x00\x01d\x03\x00Sn\x01\x00\x01d\x04\x00Sd\x00\x00S' (3D 00 00 00 74 00 00 69 01 00 64 01 00 7C 01 00 7C 00 00 7C 03 00 7C 02 00 66 04 00 16 64 02 00 83 02 00 01 7C 01 00 7C 03 00 6A 04 00 6F 08 00 01 64 03 00 53 6E 01 00 01 64 04 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CU'
                             00000003     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000006     64 - LOAD_CONST          'GenericFreeAttackTest: %d(%d) > %d(%d)?'
                             00000009     7C - LOAD_FAST           'atrTotal'
                             0000000C     7C - LOAD_FAST           'attackerBonus'
                             0000000F     7C - LOAD_FAST           'defTotal'
                             00000012     7C - LOAD_FAST           'defenderBonus'
                             00000015     66 - BUILD_TUPLE         r0004
                             00000018     16 - BINARY_MODULO       
                             00000019     64 - LOAD_CONST          2
                             0000001C     83 - CALL_FUNCTION       r0002
                             0000001F     01 - POP_TOP             
                             00000020     7C - LOAD_FAST           'atrTotal'
                             00000023     7C - LOAD_FAST           'defTotal'
                             00000026     6A - COMPARE_OP          ">"
                             00000029     6F - JUMP_IF_FALSE       -> 00000034
                             0000002C     01 - POP_TOP             
                             0000002D     64 - LOAD_CONST          1
                             00000030     53 - RETURN_VALUE        
                             00000031     6E - JUMP_FORWARD        -> 00000035
                             00000034     01 - POP_TOP             
                             00000035     64 - LOAD_CONST          0
                             00000038     53 - RETURN_VALUE        
                             00000039     64 - LOAD_CONST          None
                             0000003C     53 - RETURN_VALUE        
                         consts:
00000144                     TUPLE: (
00000149                         None (4E),
0000014A                         STR: 'GenericFreeAttackTest: %d(%d) > %d(%d)?' (27 00 00 00 47 65 6E 65 72 69 63 46 72 65 65 41 74 74 61 63 6B 54 65 73 74 3A 20 25 64 28 25 64 29 20 3E 20 25 64 28 25 64 29 3F),
00000176                         INT: 2 (02 00 00 00),
0000017B                         INT: 1 (01 00 00 00),
00000180                         INT: 0 (00 00 00 00)
                             )
                         names:
00000185                     TUPLE: (
0000018A                         STR: 'CU' (02 00 00 00 43 55),
00000191                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
000001AE                         STR: 'atrTotal' (08 00 00 00 61 74 72 54 6F 74 61 6C),
000001BB                         STR: 'attackerBonus' (0D 00 00 00 61 74 74 61 63 6B 65 72 42 6F 6E 75 73),
000001CD                         STR: 'defTotal' (08 00 00 00 64 65 66 54 6F 74 61 6C),
000001DA                         STR: 'defenderBonus' (0D 00 00 00 64 65 66 65 6E 64 65 72 42 6F 6E 75 73)
                             )
                         varnames:
000001EC                     TUPLE: (
000001F1                         STR: 'attackerBonus' (0D 00 00 00 61 74 74 61 63 6B 65 72 42 6F 6E 75 73),
00000203                         STR: 'atrTotal' (08 00 00 00 61 74 72 54 6F 74 61 6C),
00000210                         STR: 'defenderBonus' (0D 00 00 00 64 65 66 65 6E 64 65 72 42 6F 6E 75 73),
00000222                         STR: 'defTotal' (08 00 00 00 64 65 66 54 6F 74 61 6C)
                             )
                         freevars:
0000022F                     TUPLE: ()
                         cellvars:
00000234                     TUPLE: ()
                         filename:
00000239                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\generic_free_attacks.py' (4C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 67 65 6E 65 72 69 63 5F 66 72 65 65 5F 61 74 74 61 63 6B 73 2E 70 79)
                         name:
0000028A                     STR: 'GenericFreeAttackTest' (15 00 00 00 47 65 6E 65 72 69 63 46 72 65 65 41 74 74 61 63 6B 54 65 73 74)
                         firslineno:
000002A4                     LONG: 10L (0A 00 00 00)
                         lnotab:
000002A8                     STR: '\x00\x02 \x02\r\x01\x08\x01' (08 00 00 00 00 02 20 02 0D 01 08 01),
000002B5             CODE:
                         argcount:
000002B6                     LONG: 2L (02 00 00 00)
                         nlocals:
000002BA                     LONG: 4L (04 00 00 00)
                         stacksize:
000002BE                     LONG: 4L (04 00 00 00)
                         flags:
000002C2                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000002C6                     STR: 't\x00\x00i\x01\x00\x0co\x19\x00\x01t\x02\x00i\x03\x00|\x00\x00|\x01\x00d\x01\x00\x83\x03\x00}\x02\x00n\x1d\x00\x01t\x07\x00i\x08\x00d\x02\x00d\x01\x00\x83\x02\x00}\x03\x00|\x03\x00|\x00\x00\x17}\x02\x00|\x02\x00Sd\x00\x00S' (48 00 00 00 74 00 00 69 01 00 0C 6F 19 00 01 74 02 00 69 03 00 7C 00 00 7C 01 00 64 01 00 83 03 00 7D 02 00 6E 1D 00 01 74 07 00 69 08 00 64 02 00 64 01 00 83 02 00 7D 03 00 7C 03 00 7C 00 00 17 7D 02 00 7C 02 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consolevar'
                             00000003     69 - LOAD_ATTR           'OldTacticRolls'
                             00000006     0C - UNARY_NOT           
                             00000007     6F - JUMP_IF_FALSE       -> 00000023
                             0000000A     01 - POP_TOP             
                             0000000B     74 - LOAD_GLOBAL         'combatlib'
                             0000000E     69 - LOAD_ATTR           'getTacticRoll'
                             00000011     7C - LOAD_FAST           'attackerBonus'
                             00000014     7C - LOAD_FAST           'consistancy'
                             00000017     64 - LOAD_CONST          100
                             0000001A     83 - CALL_FUNCTION       r0003
                             0000001D     7D - STORE_FAST          'attackerTotal'
                             00000020     6E - JUMP_FORWARD        -> 00000040
                             00000023     01 - POP_TOP             
                             00000024     74 - LOAD_GLOBAL         'random'
                             00000027     69 - LOAD_ATTR           'randrange'
                             0000002A     64 - LOAD_CONST          1
                             0000002D     64 - LOAD_CONST          100
                             00000030     83 - CALL_FUNCTION       r0002
                             00000033     7D - STORE_FAST          'atrRoll'
                             00000036     7C - LOAD_FAST           'atrRoll'
                             00000039     7C - LOAD_FAST           'attackerBonus'
                             0000003C     17 - BINARY_ADD          
                             0000003D     7D - STORE_FAST          'attackerTotal'
                             00000040     7C - LOAD_FAST           'attackerTotal'
                             00000043     53 - RETURN_VALUE        
                             00000044     64 - LOAD_CONST          None
                             00000047     53 - RETURN_VALUE        
                         consts:
00000313                     TUPLE: (
00000318                         None (4E),
00000319                         INT: 100 (64 00 00 00),
0000031E                         INT: 1 (01 00 00 00)
                             )
                         names:
00000323                     TUPLE: (
00000328                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
00000337                         STR: 'OldTacticRolls' (0E 00 00 00 4F 6C 64 54 61 63 74 69 63 52 6F 6C 6C 73),
0000034A                         STR: 'combatlib' (09 00 00 00 63 6F 6D 62 61 74 6C 69 62),
00000358                         STR: 'getTacticRoll' (0D 00 00 00 67 65 74 54 61 63 74 69 63 52 6F 6C 6C),
0000036A                         STR: 'attackerBonus' (0D 00 00 00 61 74 74 61 63 6B 65 72 42 6F 6E 75 73),
0000037C                         STR: 'consistancy' (0B 00 00 00 63 6F 6E 73 69 73 74 61 6E 63 79),
0000038C                         STR: 'attackerTotal' (0D 00 00 00 61 74 74 61 63 6B 65 72 54 6F 74 61 6C),
0000039E                         STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
000003A9                         STR: 'randrange' (09 00 00 00 72 61 6E 64 72 61 6E 67 65),
000003B7                         STR: 'atrRoll' (07 00 00 00 61 74 72 52 6F 6C 6C)
                             )
                         varnames:
000003C3                     TUPLE: (
000003C8                         STR: 'attackerBonus' (0D 00 00 00 61 74 74 61 63 6B 65 72 42 6F 6E 75 73),
000003DA                         STR: 'consistancy' (0B 00 00 00 63 6F 6E 73 69 73 74 61 6E 63 79),
000003EA                         STR: 'attackerTotal' (0D 00 00 00 61 74 74 61 63 6B 65 72 54 6F 74 61 6C),
000003FC                         STR: 'atrRoll' (07 00 00 00 61 74 72 52 6F 6C 6C)
                             )
                         freevars:
00000408                     TUPLE: ()
                         cellvars:
0000040D                     TUPLE: ()
                         filename:
00000412                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\generic_free_attacks.py' (4C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 67 65 6E 65 72 69 63 5F 66 72 65 65 5F 61 74 74 61 63 6B 73 2E 70 79)
                         name:
00000463                     STR: 'ComputeAttackerTotal' (14 00 00 00 43 6F 6D 70 75 74 65 41 74 74 61 63 6B 65 72 54 6F 74 61 6C)
                         firslineno:
0000047C                     LONG: 18L (12 00 00 00)
                         lnotab:
00000480                     STR: '\x00\x02\x0b\x01\x19\x02\x12\x01\n\x02' (0A 00 00 00 00 02 0B 01 19 02 12 01 0A 02),
0000048F             CODE:
                         argcount:
00000490                     LONG: 2L (02 00 00 00)
                         nlocals:
00000494                     LONG: 4L (04 00 00 00)
                         stacksize:
00000498                     LONG: 4L (04 00 00 00)
                         flags:
0000049C                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000004A0                     STR: 't\x00\x00i\x01\x00\x0co\x19\x00\x01t\x02\x00i\x03\x00|\x00\x00|\x01\x00d\x01\x00\x83\x03\x00}\x02\x00n\x1d\x00\x01t\x07\x00i\x08\x00d\x02\x00d\x03\x00\x83\x02\x00}\x03\x00|\x03\x00|\x00\x00\x17}\x02\x00|\x02\x00Sd\x00\x00S' (48 00 00 00 74 00 00 69 01 00 0C 6F 19 00 01 74 02 00 69 03 00 7C 00 00 7C 01 00 64 01 00 83 03 00 7D 02 00 6E 1D 00 01 74 07 00 69 08 00 64 02 00 64 03 00 83 02 00 7D 03 00 7C 03 00 7C 00 00 17 7D 02 00 7C 02 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consolevar'
                             00000003     69 - LOAD_ATTR           'OldTacticRolls'
                             00000006     0C - UNARY_NOT           
                             00000007     6F - JUMP_IF_FALSE       -> 00000023
                             0000000A     01 - POP_TOP             
                             0000000B     74 - LOAD_GLOBAL         'combatlib'
                             0000000E     69 - LOAD_ATTR           'getTacticRoll'
                             00000011     7C - LOAD_FAST           'defenderBonus'
                             00000014     7C - LOAD_FAST           'consistancy'
                             00000017     64 - LOAD_CONST          69
                             0000001A     83 - CALL_FUNCTION       r0003
                             0000001D     7D - STORE_FAST          'defenderTotal'
                             00000020     6E - JUMP_FORWARD        -> 00000040
                             00000023     01 - POP_TOP             
                             00000024     74 - LOAD_GLOBAL         'random'
                             00000027     69 - LOAD_ATTR           'randrange'
                             0000002A     64 - LOAD_CONST          1
                             0000002D     64 - LOAD_CONST          100
                             00000030     83 - CALL_FUNCTION       r0002
                             00000033     7D - STORE_FAST          'defRoll'
                             00000036     7C - LOAD_FAST           'defRoll'
                             00000039     7C - LOAD_FAST           'defenderBonus'
                             0000003C     17 - BINARY_ADD          
                             0000003D     7D - STORE_FAST          'defenderTotal'
                             00000040     7C - LOAD_FAST           'defenderTotal'
                             00000043     53 - RETURN_VALUE        
                             00000044     64 - LOAD_CONST          None
                             00000047     53 - RETURN_VALUE        
                         consts:
000004ED                     TUPLE: (
000004F2                         None (4E),
000004F3                         INT: 69 (45 00 00 00),
000004F8                         INT: 1 (01 00 00 00),
000004FD                         INT: 100 (64 00 00 00)
                             )
                         names:
00000502                     TUPLE: (
00000507                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
00000516                         STR: 'OldTacticRolls' (0E 00 00 00 4F 6C 64 54 61 63 74 69 63 52 6F 6C 6C 73),
00000529                         STR: 'combatlib' (09 00 00 00 63 6F 6D 62 61 74 6C 69 62),
00000537                         STR: 'getTacticRoll' (0D 00 00 00 67 65 74 54 61 63 74 69 63 52 6F 6C 6C),
00000549                         STR: 'defenderBonus' (0D 00 00 00 64 65 66 65 6E 64 65 72 42 6F 6E 75 73),
0000055B                         STR: 'consistancy' (0B 00 00 00 63 6F 6E 73 69 73 74 61 6E 63 79),
0000056B                         STR: 'defenderTotal' (0D 00 00 00 64 65 66 65 6E 64 65 72 54 6F 74 61 6C),
0000057D                         STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00000588                         STR: 'randrange' (09 00 00 00 72 61 6E 64 72 61 6E 67 65),
00000596                         STR: 'defRoll' (07 00 00 00 64 65 66 52 6F 6C 6C)
                             )
                         varnames:
000005A2                     TUPLE: (
000005A7                         STR: 'defenderBonus' (0D 00 00 00 64 65 66 65 6E 64 65 72 42 6F 6E 75 73),
000005B9                         STR: 'consistancy' (0B 00 00 00 63 6F 6E 73 69 73 74 61 6E 63 79),
000005C9                         STR: 'defenderTotal' (0D 00 00 00 64 65 66 65 6E 64 65 72 54 6F 74 61 6C),
000005DB                         STR: 'defRoll' (07 00 00 00 64 65 66 52 6F 6C 6C)
                             )
                         freevars:
000005E7                     TUPLE: ()
                         cellvars:
000005EC                     TUPLE: ()
                         filename:
000005F1                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\generic_free_attacks.py' (4C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 67 65 6E 65 72 69 63 5F 66 72 65 65 5F 61 74 74 61 63 6B 73 2E 70 79)
                         name:
00000642                     STR: 'ComputeDefenderTotal' (14 00 00 00 43 6F 6D 70 75 74 65 44 65 66 65 6E 64 65 72 54 6F 74 61 6C)
                         firslineno:
0000065B                     LONG: 28L (1C 00 00 00)
                         lnotab:
0000065F                     STR: '\x00\x02\x0b\x01\x19\x02\x12\x01\n\x02' (0A 00 00 00 00 02 0B 01 19 02 12 01 0A 02),
0000066E             CODE:
                         argcount:
0000066F                     LONG: 1L (01 00 00 00)
                         nlocals:
00000673                     LONG: 12L (0C 00 00 00)
                         stacksize:
00000677                     LONG: 9L (09 00 00 00)
                         flags:
0000067B                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000067F                     STR: "|\x00\x00i\x01\x00i\x02\x00i\x03\x00o,\x00\x01|\x00\x00i\x01\x00i\x02\x00i\x04\x00|\x00\x00i\x05\x00i\x06\x00\x83\x01\x00o\x10\x00\x01t\x07\x00i\x08\x00|\x00\x00i\t\x00\x83\x01\x00o\x11\x00\x01t\n\x00|\x00\x00_\x0b\x00d\x00\x00Sn\x01\x00\x01d\x01\x00}\t\x00d\x01\x00}\x08\x00|\x00\x00i\x01\x00i\x0e\x00t\x0f\x00\x19}\x07\x00|\x00\x00i\x05\x00i\x0e\x00t\x11\x00\x19}\x0b\x00|\x00\x00i\x01\x00i\x13\x00t\x14\x00\x19}\x06\x00|\x00\x00i\x05\x00i\x13\x00t\x14\x00\x19}\x01\x00|\x07\x00o\x18\x00\x01|\x08\x00|\x00\x00i\x01\x00i\x13\x00t\x0f\x00\x197}\x08\x00n\x01\x00\x01|\x0b\x00o\x18\x00\x01|\t\x00|\x00\x00i\x05\x00i\x13\x00t\x11\x00\x197}\t\x00n\x01\x00\x01|\x00\x00i\x01\x00i\x13\x00t\x17\x00\x19}\x03\x00|\x00\x00i\x05\x00i\x13\x00t\x17\x00\x19}\n\x00t\x1a\x00t\x1b\x00|\x08\x00\x83\x01\x00t\x1c\x00i\x1d\x00|\x03\x00\x83\x01\x00\x14\x83\x01\x00}\x08\x00t\x1a\x00t\x1b\x00|\t\x00\x83\x01\x00t\x1c\x00i\x1e\x00|\n\x00\x83\x01\x00\x14\x83\x01\x00}\t\x00t\x1f\x00|\x08\x00|\x06\x00\x83\x02\x00}\x05\x00t!\x00|\t\x00|\x01\x00\x83\x02\x00}\x02\x00t#\x00i$\x00\x0co\x10\x00\x01d\x01\x00}\t\x00d\x01\x00}\x08\x00n\x01\x00\x01t%\x00|\x08\x00|\x05\x00|\t\x00|\x02\x00\x83\x04\x00}\x04\x00t\n\x00|\x00\x00_\x0b\x00|\x04\x00d\x02\x00j\x02\x00ov\x00\x01t'\x00i(\x00t)\x00i*\x00|\x00\x00i\t\x00|\x00\x00i\x01\x00i\x06\x00|\x00\x00i\x05\x00i\x06\x00|\x05\x00|\x08\x00|\x02\x00|\t\x00f\x04\x00\x83\x05\x00\x01t'\x00i+\x00t)\x00i,\x00|\x00\x00i\t\x00|\x00\x00i\x01\x00i\x06\x00|\x00\x00i\x05\x00i\x06\x00|\x05\x00|\x08\x00|\x02\x00|\t\x00f\x04\x00\x83\x05\x00\x01d\x00\x00Sn\x01\x00\x01t'\x00i(\x00t)\x00i-\x00|\x00\x00i\t\x00|\x00\x00i\x01\x00i\x06\x00|\x00\x00i\x05\x00i\x06\x00|\x05\x00|\x08\x00|\x02\x00|\t\x00f\x04\x00\x83\x05\x00\x01t'\x00i+\x00t)\x00i.\x00|\x00\x00i\t\x00|\x00\x00i\x01\x00i\x06\x00|\x00\x00i\x05\x00i\x06\x00|\x05\x00|\x08\x00|\x02\x00|\t\x00f\x04\x00\x83\x05\x00\x01t/\x00|\x00\x00_\x0b\x00d\x00\x00S" (8D 02 00 00 7C 00 00 69 01 00 69 02 00 69 03 00 6F 2C 00 01 7C 00 00 69 01 00 69 02 00 69 04 00 7C 00 00 69 05 00 69 06 00 83 01 00 6F 10 00 01 74 07 00 69 08 00 7C 00 00 69 09 00 83 01 00 6F 11 00 01 74 0A 00 7C 00 00 5F 0B 00 64 00 00 53 6E 01 00 01 64 01 00 7D 09 00 64 01 00 7D 08 00 7C 00 00 69 01 00 69 0E 00 74 0F 00 19 7D 07 00 7C 00 00 69 05 00 69 0E 00 74 11 00 19 7D 0B 00 7C 00 00 69 01 00 69 13 00 74 14 00 19 7D 06 00 7C 00 00 69 05 00 69 13 00 74 14 00 19 7D 01 00 7C 07 00 6F 18 00 01 7C 08 00 7C 00 00 69 01 00 69 13 00 74 0F 00 19 37 7D 08 00 6E 01 00 01 7C 0B 00 6F 18 00 01 7C 09 00 7C 00 00 69 05 00 69 13 00 74 11 00 19 37 7D 09 00 6E 01 00 01 7C 00 00 69 01 00 69 13 00 74 17 00 19 7D 03 00 7C 00 00 69 05 00 69 13 00 74 17 00 19 7D 0A 00 74 1A 00 74 1B 00 7C 08 00 83 01 00 74 1C 00 69 1D 00 7C 03 00 83 01 00 14 83 01 00 7D 08 00 74 1A 00 74 1B 00 7C 09 00 83 01 00 74 1C 00 69 1E 00 7C 0A 00 83 01 00 14 83 01 00 7D 09 00 74 1F 00 7C 08 00 7C 06 00 83 02 00 7D 05 00 74 21 00 7C 09 00 7C 01 00 83 02 00 7D 02 00 74 23 00 69 24 00 0C 6F 10 00 01 64 01 00 7D 09 00 64 01 00 7D 08 00 6E 01 00 01 74 25 00 7C 08 00 7C 05 00 7C 09 00 7C 02 00 83 04 00 7D 04 00 74 0A 00 7C 00 00 5F 0B 00 7C 04 00 64 02 00 6A 02 00 6F 76 00 01 74 27 00 69 28 00 74 29 00 69 2A 00 7C 00 00 69 09 00 7C 00 00 69 01 00 69 06 00 7C 00 00 69 05 00 69 06 00 7C 05 00 7C 08 00 7C 02 00 7C 09 00 66 04 00 83 05 00 01 74 27 00 69 2B 00 74 29 00 69 2C 00 7C 00 00 69 09 00 7C 00 00 69 01 00 69 06 00 7C 00 00 69 05 00 69 06 00 7C 05 00 7C 08 00 7C 02 00 7C 09 00 66 04 00 83 05 00 01 64 00 00 53 6E 01 00 01 74 27 00 69 28 00 74 29 00 69 2D 00 7C 00 00 69 09 00 7C 00 00 69 01 00 69 06 00 7C 00 00 69 05 00 69 06 00 7C 05 00 7C 08 00 7C 02 00 7C 09 00 66 04 00 83 05 00 01 74 27 00 69 2B 00 74 29 00 69 2E 00 7C 00 00 69 09 00 7C 00 00 69 01 00 69 06 00 7C 00 00 69 05 00 69 06 00 7C 05 00 7C 08 00 7C 02 00 7C 09 00 66 04 00 83 05 00 01 74 2F 00 7C 00 00 5F 0B 00 64 00 00 53)
                             00000000     7C - LOAD_FAST           'sentence'
                             00000003     69 - LOAD_ATTR           'subject'
                             00000006     69 - LOAD_ATTR           'Interlock'
                             00000009     69 - LOAD_ATTR           'isInCombat'
                             0000000C     6F - JUMP_IF_FALSE       -> 0000003B
                             0000000F     01 - POP_TOP             
                             00000010     7C - LOAD_FAST           'sentence'
                             00000013     69 - LOAD_ATTR           'subject'
                             00000016     69 - LOAD_ATTR           'Interlock'
                             00000019     69 - LOAD_ATTR           'isCombatTarget'
                             0000001C     7C - LOAD_FAST           'sentence'
                             0000001F     69 - LOAD_ATTR           'directObject'
                             00000022     69 - LOAD_ATTR           'locator'
                             00000025     83 - CALL_FUNCTION       r0001
                             00000028     6F - JUMP_IF_FALSE       -> 0000003B
                             0000002B     01 - POP_TOP             
                             0000002C     74 - LOAD_GLOBAL         'abilitylib'
                             0000002F     69 - LOAD_ATTR           'createsAnExchange'
                             00000032     7C - LOAD_FAST           'sentence'
                             00000035     69 - LOAD_ATTR           'verbID'
                             00000038     83 - CALL_FUNCTION       r0001
                             0000003B     6F - JUMP_IF_FALSE       -> 0000004F
                             0000003E     01 - POP_TOP             
                             0000003F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000042     7C - LOAD_FAST           'sentence'
                             00000045     5F - STORE_ATTR          'result'
                             00000048     64 - LOAD_CONST          None
                             0000004B     53 - RETURN_VALUE        
                             0000004C     6E - JUMP_FORWARD        -> 00000050
                             0000004F     01 - POP_TOP             
                             00000050     64 - LOAD_CONST          0
                             00000053     7D - STORE_FAST          'defBonusTotal'
                             00000056     64 - LOAD_CONST          0
                             00000059     7D - STORE_FAST          'atrBonusTotal'
                             0000005C     7C - LOAD_FAST           'sentence'
                             0000005F     69 - LOAD_ATTR           'subject'
                             00000062     69 - LOAD_ATTR           'hasAbility'
                             00000065     74 - LOAD_GLOBAL         'ThrowAccuracyAbility'
                             00000068     19 - BINARY_SUBSCR       
                             00000069     7D - STORE_FAST          'atrHasThrowBonus'
                             0000006C     7C - LOAD_FAST           'sentence'
                             0000006F     69 - LOAD_ATTR           'directObject'
                             00000072     69 - LOAD_ATTR           'hasAbility'
                             00000075     74 - LOAD_GLOBAL         'ThrowDefenseTacticsAbility'
                             00000078     19 - BINARY_SUBSCR       
                             00000079     7D - STORE_FAST          'defHasThrowDefenseTacticsBonus'
                             0000007C     7C - LOAD_FAST           'sentence'
                             0000007F     69 - LOAD_ATTR           'subject'
                             00000082     69 - LOAD_ATTR           'abilities'
                             00000085     74 - LOAD_GLOBAL         'ConsistencyAbility'
                             00000088     19 - BINARY_SUBSCR       
                             00000089     7D - STORE_FAST          'atrConsistancy'
                             0000008C     7C - LOAD_FAST           'sentence'
                             0000008F     69 - LOAD_ATTR           'directObject'
                             00000092     69 - LOAD_ATTR           'abilities'
                             00000095     74 - LOAD_GLOBAL         'ConsistencyAbility'
                             00000098     19 - BINARY_SUBSCR       
                             00000099     7D - STORE_FAST          'defConsistancy'
                             0000009C     7C - LOAD_FAST           'atrHasThrowBonus'
                             0000009F     6F - JUMP_IF_FALSE       -> 000000BA
                             000000A2     01 - POP_TOP             
                             000000A3     7C - LOAD_FAST           'atrBonusTotal'
                             000000A6     7C - LOAD_FAST           'sentence'
                             000000A9     69 - LOAD_ATTR           'subject'
                             000000AC     69 - LOAD_ATTR           'abilities'
                             000000AF     74 - LOAD_GLOBAL         'ThrowAccuracyAbility'
                             000000B2     19 - BINARY_SUBSCR       
                             000000B3     37 - INPLACE_ADD         
                             000000B4     7D - STORE_FAST          'atrBonusTotal'
                             000000B7     6E - JUMP_FORWARD        -> 000000BB
                             000000BA     01 - POP_TOP             
                             000000BB     7C - LOAD_FAST           'defHasThrowDefenseTacticsBonus'
                             000000BE     6F - JUMP_IF_FALSE       -> 000000D9
                             000000C1     01 - POP_TOP             
                             000000C2     7C - LOAD_FAST           'defBonusTotal'
                             000000C5     7C - LOAD_FAST           'sentence'
                             000000C8     69 - LOAD_ATTR           'directObject'
                             000000CB     69 - LOAD_ATTR           'abilities'
                             000000CE     74 - LOAD_GLOBAL         'ThrowDefenseTacticsAbility'
                             000000D1     19 - BINARY_SUBSCR       
                             000000D2     37 - INPLACE_ADD         
                             000000D3     7D - STORE_FAST          'defBonusTotal'
                             000000D6     6E - JUMP_FORWARD        -> 000000DA
                             000000D9     01 - POP_TOP             
                             000000DA     7C - LOAD_FAST           'sentence'
                             000000DD     69 - LOAD_ATTR           'subject'
                             000000E0     69 - LOAD_ATTR           'abilities'
                             000000E3     74 - LOAD_GLOBAL         'CurrentTacticAbility'
                             000000E6     19 - BINARY_SUBSCR       
                             000000E7     7D - STORE_FAST          'atrTactic'
                             000000EA     7C - LOAD_FAST           'sentence'
                             000000ED     69 - LOAD_ATTR           'directObject'
                             000000F0     69 - LOAD_ATTR           'abilities'
                             000000F3     74 - LOAD_GLOBAL         'CurrentTacticAbility'
                             000000F6     19 - BINARY_SUBSCR       
                             000000F7     7D - STORE_FAST          'defTactic'
                             000000FA     74 - LOAD_GLOBAL         'int'
                             000000FD     74 - LOAD_GLOBAL         'float'
                             00000100     7C - LOAD_FAST           'atrBonusTotal'
                             00000103     83 - CALL_FUNCTION       r0001
                             00000106     74 - LOAD_GLOBAL         'CC'
                             00000109     69 - LOAD_ATTR           'GetTacticCombatTacticsMod'
                             0000010C     7C - LOAD_FAST           'atrTactic'
                             0000010F     83 - CALL_FUNCTION       r0001
                             00000112     14 - BINARY_MULTIPLY     
                             00000113     83 - CALL_FUNCTION       r0001
                             00000116     7D - STORE_FAST          'atrBonusTotal'
                             00000119     74 - LOAD_GLOBAL         'int'
                             0000011C     74 - LOAD_GLOBAL         'float'
                             0000011F     7C - LOAD_FAST           'defBonusTotal'
                             00000122     83 - CALL_FUNCTION       r0001
                             00000125     74 - LOAD_GLOBAL         'CC'
                             00000128     69 - LOAD_ATTR           'GetTacticDefenseTacticsMod'
                             0000012B     7C - LOAD_FAST           'defTactic'
                             0000012E     83 - CALL_FUNCTION       r0001
                             00000131     14 - BINARY_MULTIPLY     
                             00000132     83 - CALL_FUNCTION       r0001
                             00000135     7D - STORE_FAST          'defBonusTotal'
                             00000138     74 - LOAD_GLOBAL         'ComputeAttackerTotal'
                             0000013B     7C - LOAD_FAST           'atrBonusTotal'
                             0000013E     7C - LOAD_FAST           'atrConsistancy'
                             00000141     83 - CALL_FUNCTION       r0002
                             00000144     7D - STORE_FAST          'attackerTotal'
                             00000147     74 - LOAD_GLOBAL         'ComputeDefenderTotal'
                             0000014A     7C - LOAD_FAST           'defBonusTotal'
                             0000014D     7C - LOAD_FAST           'defConsistancy'
                             00000150     83 - CALL_FUNCTION       r0002
                             00000153     7D - STORE_FAST          'defenderTotal'
                             00000156     74 - LOAD_GLOBAL         'consolevar'
                             00000159     69 - LOAD_ATTR           'OldTacticRolls'
                             0000015C     0C - UNARY_NOT           
                             0000015D     6F - JUMP_IF_FALSE       -> 00000170
                             00000160     01 - POP_TOP             
                             00000161     64 - LOAD_CONST          0
                             00000164     7D - STORE_FAST          'defBonusTotal'
                             00000167     64 - LOAD_CONST          0
                             0000016A     7D - STORE_FAST          'atrBonusTotal'
                             0000016D     6E - JUMP_FORWARD        -> 00000171
                             00000170     01 - POP_TOP             
                             00000171     74 - LOAD_GLOBAL         'GenericFreeAttackTest'
                             00000174     7C - LOAD_FAST           'atrBonusTotal'
                             00000177     7C - LOAD_FAST           'attackerTotal'
                             0000017A     7C - LOAD_FAST           'defBonusTotal'
                             0000017D     7C - LOAD_FAST           'defenderTotal'
                             00000180     83 - CALL_FUNCTION       r0004
                             00000183     7D - STORE_FAST          'atrWon'
                             00000186     74 - LOAD_GLOBAL         'SUCCESS'
                             00000189     7C - LOAD_FAST           'sentence'
                             0000018C     5F - STORE_ATTR          'result'
                             0000018F     7C - LOAD_FAST           'atrWon'
                             00000192     64 - LOAD_CONST          1
                             00000195     6A - COMPARE_OP          "=="
                             00000198     6F - JUMP_IF_FALSE       -> 00000211
                             0000019B     01 - POP_TOP             
                             0000019C     74 - LOAD_GLOBAL         'Utility'
                             0000019F     69 - LOAD_ATTR           'SendAbilityOutputToCaster'
                             000001A2     74 - LOAD_GLOBAL         'StringTable'
                             000001A5     69 - LOAD_ATTR           'ID_ABILITY_RANGED_FREE_ATTACK_SUCCESS_CASTER'
                             000001A8     7C - LOAD_FAST           'sentence'
                             000001AB     69 - LOAD_ATTR           'verbID'
                             000001AE     7C - LOAD_FAST           'sentence'
                             000001B1     69 - LOAD_ATTR           'subject'
                             000001B4     69 - LOAD_ATTR           'locator'
                             000001B7     7C - LOAD_FAST           'sentence'
                             000001BA     69 - LOAD_ATTR           'directObject'
                             000001BD     69 - LOAD_ATTR           'locator'
                             000001C0     7C - LOAD_FAST           'attackerTotal'
                             000001C3     7C - LOAD_FAST           'atrBonusTotal'
                             000001C6     7C - LOAD_FAST           'defenderTotal'
                             000001C9     7C - LOAD_FAST           'defBonusTotal'
                             000001CC     66 - BUILD_TUPLE         r0004
                             000001CF     83 - CALL_FUNCTION       r0005
                             000001D2     01 - POP_TOP             
                             000001D3     74 - LOAD_GLOBAL         'Utility'
                             000001D6     69 - LOAD_ATTR           'SendAbilityOutputToTarget'
                             000001D9     74 - LOAD_GLOBAL         'StringTable'
                             000001DC     69 - LOAD_ATTR           'ID_ABILITY_RANGED_FREE_ATTACK_SUCCESS_TARGET'
                             000001DF     7C - LOAD_FAST           'sentence'
                             000001E2     69 - LOAD_ATTR           'verbID'
                             000001E5     7C - LOAD_FAST           'sentence'
                             000001E8     69 - LOAD_ATTR           'subject'
                             000001EB     69 - LOAD_ATTR           'locator'
                             000001EE     7C - LOAD_FAST           'sentence'
                             000001F1     69 - LOAD_ATTR           'directObject'
                             000001F4     69 - LOAD_ATTR           'locator'
                             000001F7     7C - LOAD_FAST           'attackerTotal'
                             000001FA     7C - LOAD_FAST           'atrBonusTotal'
                             000001FD     7C - LOAD_FAST           'defenderTotal'
                             00000200     7C - LOAD_FAST           'defBonusTotal'
                             00000203     66 - BUILD_TUPLE         r0004
                             00000206     83 - CALL_FUNCTION       r0005
                             00000209     01 - POP_TOP             
                             0000020A     64 - LOAD_CONST          None
                             0000020D     53 - RETURN_VALUE        
                             0000020E     6E - JUMP_FORWARD        -> 00000212
                             00000211     01 - POP_TOP             
                             00000212     74 - LOAD_GLOBAL         'Utility'
                             00000215     69 - LOAD_ATTR           'SendAbilityOutputToCaster'
                             00000218     74 - LOAD_GLOBAL         'StringTable'
                             0000021B     69 - LOAD_ATTR           'ID_ABILITY_RANGED_FREE_ATTACK_FAILURE_CASTER'
                             0000021E     7C - LOAD_FAST           'sentence'
                             00000221     69 - LOAD_ATTR           'verbID'
                             00000224     7C - LOAD_FAST           'sentence'
                             00000227     69 - LOAD_ATTR           'subject'
                             0000022A     69 - LOAD_ATTR           'locator'
                             0000022D     7C - LOAD_FAST           'sentence'
                             00000230     69 - LOAD_ATTR           'directObject'
                             00000233     69 - LOAD_ATTR           'locator'
                             00000236     7C - LOAD_FAST           'attackerTotal'
                             00000239     7C - LOAD_FAST           'atrBonusTotal'
                             0000023C     7C - LOAD_FAST           'defenderTotal'
                             0000023F     7C - LOAD_FAST           'defBonusTotal'
                             00000242     66 - BUILD_TUPLE         r0004
                             00000245     83 - CALL_FUNCTION       r0005
                             00000248     01 - POP_TOP             
                             00000249     74 - LOAD_GLOBAL         'Utility'
                             0000024C     69 - LOAD_ATTR           'SendAbilityOutputToTarget'
                             0000024F     74 - LOAD_GLOBAL         'StringTable'
                             00000252     69 - LOAD_ATTR           'ID_ABILITY_RANGED_FREE_ATTACK_FAILURE_TARGET'
                             00000255     7C - LOAD_FAST           'sentence'
                             00000258     69 - LOAD_ATTR           'verbID'
                             0000025B     7C - LOAD_FAST           'sentence'
                             0000025E     69 - LOAD_ATTR           'subject'
                             00000261     69 - LOAD_ATTR           'locator'
                             00000264     7C - LOAD_FAST           'sentence'
                             00000267     69 - LOAD_ATTR           'directObject'
                             0000026A     69 - LOAD_ATTR           'locator'
                             0000026D     7C - LOAD_FAST           'attackerTotal'
                             00000270     7C - LOAD_FAST           'atrBonusTotal'
                             00000273     7C - LOAD_FAST           'defenderTotal'
                             00000276     7C - LOAD_FAST           'defBonusTotal'
                             00000279     66 - BUILD_TUPLE         r0004
                             0000027C     83 - CALL_FUNCTION       r0005
                             0000027F     01 - POP_TOP             
                             00000280     74 - LOAD_GLOBAL         'DEFLECTED'
                             00000283     7C - LOAD_FAST           'sentence'
                             00000286     5F - STORE_ATTR          'result'
                             00000289     64 - LOAD_CONST          None
                             0000028C     53 - RETURN_VALUE        
                         consts:
00000911                     TUPLE: (
00000916                         None (4E),
00000917                         INT: 0 (00 00 00 00),
0000091C                         INT: 1 (01 00 00 00)
                             )
                         names:
00000921                     TUPLE: (
00000926                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65),
00000933                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000093F                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
0000094D                         STR: 'isInCombat' (0A 00 00 00 69 73 49 6E 43 6F 6D 62 61 74),
0000095C                         STR: 'isCombatTarget' (0E 00 00 00 69 73 43 6F 6D 62 61 74 54 61 72 67 65 74),
0000096F                         STR: 'directObject' (0C 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74),
00000980                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
0000098C                         STR: 'abilitylib' (0A 00 00 00 61 62 69 6C 69 74 79 6C 69 62),
0000099B                         STR: 'createsAnExchange' (11 00 00 00 63 72 65 61 74 65 73 41 6E 45 78 63 68 61 6E 67 65),
000009B1                         STR: 'verbID' (06 00 00 00 76 65 72 62 49 44),
000009BC                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
000009C8                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
000009D3                         STR: 'defBonusTotal' (0D 00 00 00 64 65 66 42 6F 6E 75 73 54 6F 74 61 6C),
000009E5                         STR: 'atrBonusTotal' (0D 00 00 00 61 74 72 42 6F 6E 75 73 54 6F 74 61 6C),
000009F7                         STR: 'hasAbility' (0A 00 00 00 68 61 73 41 62 69 6C 69 74 79),
00000A06                         STR: 'ThrowAccuracyAbility' (14 00 00 00 54 68 72 6F 77 41 63 63 75 72 61 63 79 41 62 69 6C 69 74 79),
00000A1F                         STR: 'atrHasThrowBonus' (10 00 00 00 61 74 72 48 61 73 54 68 72 6F 77 42 6F 6E 75 73),
00000A34                         STR: 'ThrowDefenseTacticsAbility' (1A 00 00 00 54 68 72 6F 77 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 41 62 69 6C 69 74 79),
00000A53                         STR: 'defHasThrowDefenseTacticsBonus' (1E 00 00 00 64 65 66 48 61 73 54 68 72 6F 77 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 42 6F 6E 75 73),
00000A76                         STR: 'abilities' (09 00 00 00 61 62 69 6C 69 74 69 65 73),
00000A84                         STR: 'ConsistencyAbility' (12 00 00 00 43 6F 6E 73 69 73 74 65 6E 63 79 41 62 69 6C 69 74 79),
00000A9B                         STR: 'atrConsistancy' (0E 00 00 00 61 74 72 43 6F 6E 73 69 73 74 61 6E 63 79),
00000AAE                         STR: 'defConsistancy' (0E 00 00 00 64 65 66 43 6F 6E 73 69 73 74 61 6E 63 79),
00000AC1                         STR: 'CurrentTacticAbility' (14 00 00 00 43 75 72 72 65 6E 74 54 61 63 74 69 63 41 62 69 6C 69 74 79),
00000ADA                         STR: 'atrTactic' (09 00 00 00 61 74 72 54 61 63 74 69 63),
00000AE8                         STR: 'defTactic' (09 00 00 00 64 65 66 54 61 63 74 69 63),
00000AF6                         STR: 'int' (03 00 00 00 69 6E 74),
00000AFE                         STR: 'float' (05 00 00 00 66 6C 6F 61 74),
00000B08                         STR: 'CC' (02 00 00 00 43 43),
00000B0F                         STR: 'GetTacticCombatTacticsMod' (19 00 00 00 47 65 74 54 61 63 74 69 63 43 6F 6D 62 61 74 54 61 63 74 69 63 73 4D 6F 64),
00000B2D                         STR: 'GetTacticDefenseTacticsMod' (1A 00 00 00 47 65 74 54 61 63 74 69 63 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 4D 6F 64),
00000B4C                         STR: 'ComputeAttackerTotal' (14 00 00 00 43 6F 6D 70 75 74 65 41 74 74 61 63 6B 65 72 54 6F 74 61 6C),
00000B65                         STR: 'attackerTotal' (0D 00 00 00 61 74 74 61 63 6B 65 72 54 6F 74 61 6C),
00000B77                         STR: 'ComputeDefenderTotal' (14 00 00 00 43 6F 6D 70 75 74 65 44 65 66 65 6E 64 65 72 54 6F 74 61 6C),
00000B90                         STR: 'defenderTotal' (0D 00 00 00 64 65 66 65 6E 64 65 72 54 6F 74 61 6C),
00000BA2                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
00000BB1                         STR: 'OldTacticRolls' (0E 00 00 00 4F 6C 64 54 61 63 74 69 63 52 6F 6C 6C 73),
00000BC4                         STR: 'GenericFreeAttackTest' (15 00 00 00 47 65 6E 65 72 69 63 46 72 65 65 41 74 74 61 63 6B 54 65 73 74),
00000BDE                         STR: 'atrWon' (06 00 00 00 61 74 72 57 6F 6E),
00000BE9                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000BF5                         STR: 'SendAbilityOutputToCaster' (19 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 43 61 73 74 65 72),
00000C13                         STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00000C23                         STR: 'ID_ABILITY_RANGED_FREE_ATTACK_SUCCESS_CASTER' (2C 00 00 00 49 44 5F 41 42 49 4C 49 54 59 5F 52 41 4E 47 45 44 5F 46 52 45 45 5F 41 54 54 41 43 4B 5F 53 55 43 43 45 53 53 5F 43 41 53 54 45 52),
00000C54                         STR: 'SendAbilityOutputToTarget' (19 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 54 61 72 67 65 74),
00000C72                         STR: 'ID_ABILITY_RANGED_FREE_ATTACK_SUCCESS_TARGET' (2C 00 00 00 49 44 5F 41 42 49 4C 49 54 59 5F 52 41 4E 47 45 44 5F 46 52 45 45 5F 41 54 54 41 43 4B 5F 53 55 43 43 45 53 53 5F 54 41 52 47 45 54),
00000CA3                         STR: 'ID_ABILITY_RANGED_FREE_ATTACK_FAILURE_CASTER' (2C 00 00 00 49 44 5F 41 42 49 4C 49 54 59 5F 52 41 4E 47 45 44 5F 46 52 45 45 5F 41 54 54 41 43 4B 5F 46 41 49 4C 55 52 45 5F 43 41 53 54 45 52),
00000CD4                         STR: 'ID_ABILITY_RANGED_FREE_ATTACK_FAILURE_TARGET' (2C 00 00 00 49 44 5F 41 42 49 4C 49 54 59 5F 52 41 4E 47 45 44 5F 46 52 45 45 5F 41 54 54 41 43 4B 5F 46 41 49 4C 55 52 45 5F 54 41 52 47 45 54),
00000D05                         STR: 'DEFLECTED' (09 00 00 00 44 45 46 4C 45 43 54 45 44)
                             )
                         varnames:
00000D13                     TUPLE: (
00000D18                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65),
00000D25                         STR: 'defConsistancy' (0E 00 00 00 64 65 66 43 6F 6E 73 69 73 74 61 6E 63 79),
00000D38                         STR: 'defenderTotal' (0D 00 00 00 64 65 66 65 6E 64 65 72 54 6F 74 61 6C),
00000D4A                         STR: 'atrTactic' (09 00 00 00 61 74 72 54 61 63 74 69 63),
00000D58                         STR: 'atrWon' (06 00 00 00 61 74 72 57 6F 6E),
00000D63                         STR: 'attackerTotal' (0D 00 00 00 61 74 74 61 63 6B 65 72 54 6F 74 61 6C),
00000D75                         STR: 'atrConsistancy' (0E 00 00 00 61 74 72 43 6F 6E 73 69 73 74 61 6E 63 79),
00000D88                         STR: 'atrHasThrowBonus' (10 00 00 00 61 74 72 48 61 73 54 68 72 6F 77 42 6F 6E 75 73),
00000D9D                         STR: 'atrBonusTotal' (0D 00 00 00 61 74 72 42 6F 6E 75 73 54 6F 74 61 6C),
00000DAF                         STR: 'defBonusTotal' (0D 00 00 00 64 65 66 42 6F 6E 75 73 54 6F 74 61 6C),
00000DC1                         STR: 'defTactic' (09 00 00 00 64 65 66 54 61 63 74 69 63),
00000DCF                         STR: 'defHasThrowDefenseTacticsBonus' (1E 00 00 00 64 65 66 48 61 73 54 68 72 6F 77 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 42 6F 6E 75 73)
                             )
                         freevars:
00000DF2                     TUPLE: ()
                         cellvars:
00000DF7                     TUPLE: ()
                         filename:
00000DFC                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\generic_free_attacks.py' (4C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 67 65 6E 65 72 69 63 5F 66 72 65 65 5F 61 74 74 61 63 6B 73 2E 70 79)
                         name:
00000E4D                     STR: 'AbilityThrowFreeAttack' (16 00 00 00 41 62 69 6C 69 74 79 54 68 72 6F 77 46 72 65 65 41 74 74 61 63 6B)
                         firslineno:
00000E68                     LONG: 43L (2B 00 00 00)
                         lnotab:
00000E6C                     STR: '\x00\x04?\x01\t\x01\x08\x02\x06\x01\x06\x02\x10\x01\x10\x02\x10\x01\x10\x03\x07\x01\x18\x03\x07\x01\x18\x03\x10\x01\x10\x01\x1f\x01\x1f\x03\x0f\x01\x0f\x02\x0b\x01\x06\x01\n\x03\x15\x01\t\x01\r\x017\x017\x01\x08\x027\x017\x01' (3E 00 00 00 00 04 3F 01 09 01 08 02 06 01 06 02 10 01 10 02 10 01 10 03 07 01 18 03 07 01 18 03 10 01 10 01 1F 01 1F 03 0F 01 0F 02 0B 01 06 01 0A 03 15 01 09 01 0D 01 37 01 37 01 08 02 37 01 37 01),
00000EAF             STR: '\ndirectObject.hasAbility[CurrentTacticAbility]\ndirectObject.hasAbility[ThrowDefenseTacticsAbility]\ndirectObject.abilities[ThrowDefenseTacticsAbility]\ndirectObject.abilities[ConsistencyAbility]\ndirectObject.abilities[CurrentTacticAbility]\ndirectObject.locator\n' (03 01 00 00 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 68 61 73 41 62 69 6C 69 74 79 5B 43 75 72 72 65 6E 74 54 61 63 74 69 63 41 62 69 6C 69 74 79 5D 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 68 61 73 41 62 69 6C 69 74 79 5B 54 68 72 6F 77 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 41 62 69 6C 69 74 79 5D 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 61 62 69 6C 69 74 69 65 73 5B 54 68 72 6F 77 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 41 62 69 6C 69 74 79 5D 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 61 62 69 6C 69 74 69 65 73 5B 43 6F 6E 73 69 73 74 65 6E 63 79 41 62 69 6C 69 74 79 5D 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 61 62 69 6C 69 74 69 65 73 5B 43 75 72 72 65 6E 74 54 61 63 74 69 63 41 62 69 6C 69 74 79 5D 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 6C 6F 63 61 74 6F 72 0A),
00000FB7             CODE:
                         argcount:
00000FB8                     LONG: 1L (01 00 00 00)
                         nlocals:
00000FBC                     LONG: 12L (0C 00 00 00)
                         stacksize:
00000FC0                     LONG: 9L (09 00 00 00)
                         flags:
00000FC4                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000FC8                     STR: "|\x00\x00i\x01\x00i\x02\x00i\x03\x00o,\x00\x01|\x00\x00i\x01\x00i\x02\x00i\x04\x00|\x00\x00i\x05\x00i\x06\x00\x83\x01\x00o\x10\x00\x01t\x07\x00i\x08\x00|\x00\x00i\t\x00\x83\x01\x00o\x11\x00\x01t\n\x00|\x00\x00_\x0b\x00d\x00\x00Sn\x01\x00\x01d\x01\x00}\t\x00d\x01\x00}\x08\x00|\x00\x00i\x01\x00i\x0e\x00t\x0f\x00\x19}\x0b\x00|\x00\x00i\x05\x00i\x0e\x00t\x11\x00\x19}\x05\x00|\x00\x00i\x01\x00i\x13\x00t\x14\x00\x19}\x07\x00|\x00\x00i\x05\x00i\x13\x00t\x14\x00\x19}\x01\x00|\x0b\x00o\x18\x00\x01|\x08\x00|\x00\x00i\x01\x00i\x13\x00t\x0f\x00\x197}\x08\x00n\x01\x00\x01|\x05\x00o\x18\x00\x01|\t\x00|\x00\x00i\x05\x00i\x13\x00t\x11\x00\x197}\t\x00n\x01\x00\x01|\x00\x00i\x01\x00i\x13\x00t\x17\x00\x19}\x03\x00|\x00\x00i\x05\x00i\x13\x00t\x17\x00\x19}\n\x00t\x1a\x00t\x1b\x00|\x08\x00\x83\x01\x00t\x1c\x00i\x1d\x00|\x03\x00\x83\x01\x00\x14\x83\x01\x00}\x08\x00t\x1a\x00t\x1b\x00|\t\x00\x83\x01\x00t\x1c\x00i\x1e\x00|\n\x00\x83\x01\x00\x14\x83\x01\x00}\t\x00t\x1f\x00|\x08\x00|\x07\x00\x83\x02\x00}\x06\x00t!\x00|\t\x00|\x01\x00\x83\x02\x00}\x02\x00t#\x00i$\x00\x0co\x10\x00\x01d\x01\x00}\t\x00d\x01\x00}\x08\x00n\x01\x00\x01t%\x00|\x08\x00|\x06\x00|\t\x00|\x02\x00\x83\x04\x00}\x04\x00t\n\x00|\x00\x00_\x0b\x00|\x04\x00d\x02\x00j\x02\x00ov\x00\x01t'\x00i(\x00t)\x00i*\x00|\x00\x00i\t\x00|\x00\x00i\x01\x00i\x06\x00|\x00\x00i\x05\x00i\x06\x00|\x06\x00|\x08\x00|\x02\x00|\t\x00f\x04\x00\x83\x05\x00\x01t'\x00i+\x00t)\x00i,\x00|\x00\x00i\t\x00|\x00\x00i\x01\x00i\x06\x00|\x00\x00i\x05\x00i\x06\x00|\x06\x00|\x08\x00|\x02\x00|\t\x00f\x04\x00\x83\x05\x00\x01d\x00\x00Sn\x01\x00\x01t'\x00i(\x00t)\x00i-\x00|\x00\x00i\t\x00|\x00\x00i\x01\x00i\x06\x00|\x00\x00i\x05\x00i\x06\x00|\x06\x00|\x08\x00|\x02\x00|\t\x00f\x04\x00\x83\x05\x00\x01t'\x00i+\x00t)\x00i.\x00|\x00\x00i\t\x00|\x00\x00i\x01\x00i\x06\x00|\x00\x00i\x05\x00i\x06\x00|\x06\x00|\x08\x00|\x02\x00|\t\x00f\x04\x00\x83\x05\x00\x01t/\x00|\x00\x00_\x0b\x00d\x00\x00S" (8D 02 00 00 7C 00 00 69 01 00 69 02 00 69 03 00 6F 2C 00 01 7C 00 00 69 01 00 69 02 00 69 04 00 7C 00 00 69 05 00 69 06 00 83 01 00 6F 10 00 01 74 07 00 69 08 00 7C 00 00 69 09 00 83 01 00 6F 11 00 01 74 0A 00 7C 00 00 5F 0B 00 64 00 00 53 6E 01 00 01 64 01 00 7D 09 00 64 01 00 7D 08 00 7C 00 00 69 01 00 69 0E 00 74 0F 00 19 7D 0B 00 7C 00 00 69 05 00 69 0E 00 74 11 00 19 7D 05 00 7C 00 00 69 01 00 69 13 00 74 14 00 19 7D 07 00 7C 00 00 69 05 00 69 13 00 74 14 00 19 7D 01 00 7C 0B 00 6F 18 00 01 7C 08 00 7C 00 00 69 01 00 69 13 00 74 0F 00 19 37 7D 08 00 6E 01 00 01 7C 05 00 6F 18 00 01 7C 09 00 7C 00 00 69 05 00 69 13 00 74 11 00 19 37 7D 09 00 6E 01 00 01 7C 00 00 69 01 00 69 13 00 74 17 00 19 7D 03 00 7C 00 00 69 05 00 69 13 00 74 17 00 19 7D 0A 00 74 1A 00 74 1B 00 7C 08 00 83 01 00 74 1C 00 69 1D 00 7C 03 00 83 01 00 14 83 01 00 7D 08 00 74 1A 00 74 1B 00 7C 09 00 83 01 00 74 1C 00 69 1E 00 7C 0A 00 83 01 00 14 83 01 00 7D 09 00 74 1F 00 7C 08 00 7C 07 00 83 02 00 7D 06 00 74 21 00 7C 09 00 7C 01 00 83 02 00 7D 02 00 74 23 00 69 24 00 0C 6F 10 00 01 64 01 00 7D 09 00 64 01 00 7D 08 00 6E 01 00 01 74 25 00 7C 08 00 7C 06 00 7C 09 00 7C 02 00 83 04 00 7D 04 00 74 0A 00 7C 00 00 5F 0B 00 7C 04 00 64 02 00 6A 02 00 6F 76 00 01 74 27 00 69 28 00 74 29 00 69 2A 00 7C 00 00 69 09 00 7C 00 00 69 01 00 69 06 00 7C 00 00 69 05 00 69 06 00 7C 06 00 7C 08 00 7C 02 00 7C 09 00 66 04 00 83 05 00 01 74 27 00 69 2B 00 74 29 00 69 2C 00 7C 00 00 69 09 00 7C 00 00 69 01 00 69 06 00 7C 00 00 69 05 00 69 06 00 7C 06 00 7C 08 00 7C 02 00 7C 09 00 66 04 00 83 05 00 01 64 00 00 53 6E 01 00 01 74 27 00 69 28 00 74 29 00 69 2D 00 7C 00 00 69 09 00 7C 00 00 69 01 00 69 06 00 7C 00 00 69 05 00 69 06 00 7C 06 00 7C 08 00 7C 02 00 7C 09 00 66 04 00 83 05 00 01 74 27 00 69 2B 00 74 29 00 69 2E 00 7C 00 00 69 09 00 7C 00 00 69 01 00 69 06 00 7C 00 00 69 05 00 69 06 00 7C 06 00 7C 08 00 7C 02 00 7C 09 00 66 04 00 83 05 00 01 74 2F 00 7C 00 00 5F 0B 00 64 00 00 53)
                             00000000     7C - LOAD_FAST           'sentence'
                             00000003     69 - LOAD_ATTR           'subject'
                             00000006     69 - LOAD_ATTR           'Interlock'
                             00000009     69 - LOAD_ATTR           'isInCombat'
                             0000000C     6F - JUMP_IF_FALSE       -> 0000003B
                             0000000F     01 - POP_TOP             
                             00000010     7C - LOAD_FAST           'sentence'
                             00000013     69 - LOAD_ATTR           'subject'
                             00000016     69 - LOAD_ATTR           'Interlock'
                             00000019     69 - LOAD_ATTR           'isCombatTarget'
                             0000001C     7C - LOAD_FAST           'sentence'
                             0000001F     69 - LOAD_ATTR           'directObject'
                             00000022     69 - LOAD_ATTR           'locator'
                             00000025     83 - CALL_FUNCTION       r0001
                             00000028     6F - JUMP_IF_FALSE       -> 0000003B
                             0000002B     01 - POP_TOP             
                             0000002C     74 - LOAD_GLOBAL         'abilitylib'
                             0000002F     69 - LOAD_ATTR           'createsAnExchange'
                             00000032     7C - LOAD_FAST           'sentence'
                             00000035     69 - LOAD_ATTR           'verbID'
                             00000038     83 - CALL_FUNCTION       r0001
                             0000003B     6F - JUMP_IF_FALSE       -> 0000004F
                             0000003E     01 - POP_TOP             
                             0000003F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000042     7C - LOAD_FAST           'sentence'
                             00000045     5F - STORE_ATTR          'result'
                             00000048     64 - LOAD_CONST          None
                             0000004B     53 - RETURN_VALUE        
                             0000004C     6E - JUMP_FORWARD        -> 00000050
                             0000004F     01 - POP_TOP             
                             00000050     64 - LOAD_CONST          0
                             00000053     7D - STORE_FAST          'defBonusTotal'
                             00000056     64 - LOAD_CONST          0
                             00000059     7D - STORE_FAST          'atrBonusTotal'
                             0000005C     7C - LOAD_FAST           'sentence'
                             0000005F     69 - LOAD_ATTR           'subject'
                             00000062     69 - LOAD_ATTR           'hasAbility'
                             00000065     74 - LOAD_GLOBAL         'MeleeCombatTacticsAbility'
                             00000068     19 - BINARY_SUBSCR       
                             00000069     7D - STORE_FAST          'atrHasMeleeBonus'
                             0000006C     7C - LOAD_FAST           'sentence'
                             0000006F     69 - LOAD_ATTR           'directObject'
                             00000072     69 - LOAD_ATTR           'hasAbility'
                             00000075     74 - LOAD_GLOBAL         'MeleeDefenseTacticsAbility'
                             00000078     19 - BINARY_SUBSCR       
                             00000079     7D - STORE_FAST          'defHasMeleeDefBonus'
                             0000007C     7C - LOAD_FAST           'sentence'
                             0000007F     69 - LOAD_ATTR           'subject'
                             00000082     69 - LOAD_ATTR           'abilities'
                             00000085     74 - LOAD_GLOBAL         'ConsistencyAbility'
                             00000088     19 - BINARY_SUBSCR       
                             00000089     7D - STORE_FAST          'atrConsistancy'
                             0000008C     7C - LOAD_FAST           'sentence'
                             0000008F     69 - LOAD_ATTR           'directObject'
                             00000092     69 - LOAD_ATTR           'abilities'
                             00000095     74 - LOAD_GLOBAL         'ConsistencyAbility'
                             00000098     19 - BINARY_SUBSCR       
                             00000099     7D - STORE_FAST          'defConsistancy'
                             0000009C     7C - LOAD_FAST           'atrHasMeleeBonus'
                             0000009F     6F - JUMP_IF_FALSE       -> 000000BA
                             000000A2     01 - POP_TOP             
                             000000A3     7C - LOAD_FAST           'atrBonusTotal'
                             000000A6     7C - LOAD_FAST           'sentence'
                             000000A9     69 - LOAD_ATTR           'subject'
                             000000AC     69 - LOAD_ATTR           'abilities'
                             000000AF     74 - LOAD_GLOBAL         'MeleeCombatTacticsAbility'
                             000000B2     19 - BINARY_SUBSCR       
                             000000B3     37 - INPLACE_ADD         
                             000000B4     7D - STORE_FAST          'atrBonusTotal'
                             000000B7     6E - JUMP_FORWARD        -> 000000BB
                             000000BA     01 - POP_TOP             
                             000000BB     7C - LOAD_FAST           'defHasMeleeDefBonus'
                             000000BE     6F - JUMP_IF_FALSE       -> 000000D9
                             000000C1     01 - POP_TOP             
                             000000C2     7C - LOAD_FAST           'defBonusTotal'
                             000000C5     7C - LOAD_FAST           'sentence'
                             000000C8     69 - LOAD_ATTR           'directObject'
                             000000CB     69 - LOAD_ATTR           'abilities'
                             000000CE     74 - LOAD_GLOBAL         'MeleeDefenseTacticsAbility'
                             000000D1     19 - BINARY_SUBSCR       
                             000000D2     37 - INPLACE_ADD         
                             000000D3     7D - STORE_FAST          'defBonusTotal'
                             000000D6     6E - JUMP_FORWARD        -> 000000DA
                             000000D9     01 - POP_TOP             
                             000000DA     7C - LOAD_FAST           'sentence'
                             000000DD     69 - LOAD_ATTR           'subject'
                             000000E0     69 - LOAD_ATTR           'abilities'
                             000000E3     74 - LOAD_GLOBAL         'CurrentTacticAbility'
                             000000E6     19 - BINARY_SUBSCR       
                             000000E7     7D - STORE_FAST          'atrTactic'
                             000000EA     7C - LOAD_FAST           'sentence'
                             000000ED     69 - LOAD_ATTR           'directObject'
                             000000F0     69 - LOAD_ATTR           'abilities'
                             000000F3     74 - LOAD_GLOBAL         'CurrentTacticAbility'
                             000000F6     19 - BINARY_SUBSCR       
                             000000F7     7D - STORE_FAST          'defTactic'
                             000000FA     74 - LOAD_GLOBAL         'int'
                             000000FD     74 - LOAD_GLOBAL         'float'
                             00000100     7C - LOAD_FAST           'atrBonusTotal'
                             00000103     83 - CALL_FUNCTION       r0001
                             00000106     74 - LOAD_GLOBAL         'CC'
                             00000109     69 - LOAD_ATTR           'GetTacticCombatTacticsMod'
                             0000010C     7C - LOAD_FAST           'atrTactic'
                             0000010F     83 - CALL_FUNCTION       r0001
                             00000112     14 - BINARY_MULTIPLY     
                             00000113     83 - CALL_FUNCTION       r0001
                             00000116     7D - STORE_FAST          'atrBonusTotal'
                             00000119     74 - LOAD_GLOBAL         'int'
                             0000011C     74 - LOAD_GLOBAL         'float'
                             0000011F     7C - LOAD_FAST           'defBonusTotal'
                             00000122     83 - CALL_FUNCTION       r0001
                             00000125     74 - LOAD_GLOBAL         'CC'
                             00000128     69 - LOAD_ATTR           'GetTacticDefenseTacticsMod'
                             0000012B     7C - LOAD_FAST           'defTactic'
                             0000012E     83 - CALL_FUNCTION       r0001
                             00000131     14 - BINARY_MULTIPLY     
                             00000132     83 - CALL_FUNCTION       r0001
                             00000135     7D - STORE_FAST          'defBonusTotal'
                             00000138     74 - LOAD_GLOBAL         'ComputeAttackerTotal'
                             0000013B     7C - LOAD_FAST           'atrBonusTotal'
                             0000013E     7C - LOAD_FAST           'atrConsistancy'
                             00000141     83 - CALL_FUNCTION       r0002
                             00000144     7D - STORE_FAST          'attackerTotal'
                             00000147     74 - LOAD_GLOBAL         'ComputeDefenderTotal'
                             0000014A     7C - LOAD_FAST           'defBonusTotal'
                             0000014D     7C - LOAD_FAST           'defConsistancy'
                             00000150     83 - CALL_FUNCTION       r0002
                             00000153     7D - STORE_FAST          'defenderTotal'
                             00000156     74 - LOAD_GLOBAL         'consolevar'
                             00000159     69 - LOAD_ATTR           'OldTacticRolls'
                             0000015C     0C - UNARY_NOT           
                             0000015D     6F - JUMP_IF_FALSE       -> 00000170
                             00000160     01 - POP_TOP             
                             00000161     64 - LOAD_CONST          0
                             00000164     7D - STORE_FAST          'defBonusTotal'
                             00000167     64 - LOAD_CONST          0
                             0000016A     7D - STORE_FAST          'atrBonusTotal'
                             0000016D     6E - JUMP_FORWARD        -> 00000171
                             00000170     01 - POP_TOP             
                             00000171     74 - LOAD_GLOBAL         'GenericFreeAttackTest'
                             00000174     7C - LOAD_FAST           'atrBonusTotal'
                             00000177     7C - LOAD_FAST           'attackerTotal'
                             0000017A     7C - LOAD_FAST           'defBonusTotal'
                             0000017D     7C - LOAD_FAST           'defenderTotal'
                             00000180     83 - CALL_FUNCTION       r0004
                             00000183     7D - STORE_FAST          'atrWon'
                             00000186     74 - LOAD_GLOBAL         'SUCCESS'
                             00000189     7C - LOAD_FAST           'sentence'
                             0000018C     5F - STORE_ATTR          'result'
                             0000018F     7C - LOAD_FAST           'atrWon'
                             00000192     64 - LOAD_CONST          1
                             00000195     6A - COMPARE_OP          "=="
                             00000198     6F - JUMP_IF_FALSE       -> 00000211
                             0000019B     01 - POP_TOP             
                             0000019C     74 - LOAD_GLOBAL         'Utility'
                             0000019F     69 - LOAD_ATTR           'SendAbilityOutputToCaster'
                             000001A2     74 - LOAD_GLOBAL         'StringTable'
                             000001A5     69 - LOAD_ATTR           'ID_ABILITY_RANGED_FREE_ATTACK_SUCCESS_CASTER'
                             000001A8     7C - LOAD_FAST           'sentence'
                             000001AB     69 - LOAD_ATTR           'verbID'
                             000001AE     7C - LOAD_FAST           'sentence'
                             000001B1     69 - LOAD_ATTR           'subject'
                             000001B4     69 - LOAD_ATTR           'locator'
                             000001B7     7C - LOAD_FAST           'sentence'
                             000001BA     69 - LOAD_ATTR           'directObject'
                             000001BD     69 - LOAD_ATTR           'locator'
                             000001C0     7C - LOAD_FAST           'attackerTotal'
                             000001C3     7C - LOAD_FAST           'atrBonusTotal'
                             000001C6     7C - LOAD_FAST           'defenderTotal'
                             000001C9     7C - LOAD_FAST           'defBonusTotal'
                             000001CC     66 - BUILD_TUPLE         r0004
                             000001CF     83 - CALL_FUNCTION       r0005
                             000001D2     01 - POP_TOP             
                             000001D3     74 - LOAD_GLOBAL         'Utility'
                             000001D6     69 - LOAD_ATTR           'SendAbilityOutputToTarget'
                             000001D9     74 - LOAD_GLOBAL         'StringTable'
                             000001DC     69 - LOAD_ATTR           'ID_ABILITY_RANGED_FREE_ATTACK_SUCCESS_TARGET'
                             000001DF     7C - LOAD_FAST           'sentence'
                             000001E2     69 - LOAD_ATTR           'verbID'
                             000001E5     7C - LOAD_FAST           'sentence'
                             000001E8     69 - LOAD_ATTR           'subject'
                             000001EB     69 - LOAD_ATTR           'locator'
                             000001EE     7C - LOAD_FAST           'sentence'
                             000001F1     69 - LOAD_ATTR           'directObject'
                             000001F4     69 - LOAD_ATTR           'locator'
                             000001F7     7C - LOAD_FAST           'attackerTotal'
                             000001FA     7C - LOAD_FAST           'atrBonusTotal'
                             000001FD     7C - LOAD_FAST           'defenderTotal'
                             00000200     7C - LOAD_FAST           'defBonusTotal'
                             00000203     66 - BUILD_TUPLE         r0004
                             00000206     83 - CALL_FUNCTION       r0005
                             00000209     01 - POP_TOP             
                             0000020A     64 - LOAD_CONST          None
                             0000020D     53 - RETURN_VALUE        
                             0000020E     6E - JUMP_FORWARD        -> 00000212
                             00000211     01 - POP_TOP             
                             00000212     74 - LOAD_GLOBAL         'Utility'
                             00000215     69 - LOAD_ATTR           'SendAbilityOutputToCaster'
                             00000218     74 - LOAD_GLOBAL         'StringTable'
                             0000021B     69 - LOAD_ATTR           'ID_ABILITY_RANGED_FREE_ATTACK_FAILURE_CASTER'
                             0000021E     7C - LOAD_FAST           'sentence'
                             00000221     69 - LOAD_ATTR           'verbID'
                             00000224     7C - LOAD_FAST           'sentence'
                             00000227     69 - LOAD_ATTR           'subject'
                             0000022A     69 - LOAD_ATTR           'locator'
                             0000022D     7C - LOAD_FAST           'sentence'
                             00000230     69 - LOAD_ATTR           'directObject'
                             00000233     69 - LOAD_ATTR           'locator'
                             00000236     7C - LOAD_FAST           'attackerTotal'
                             00000239     7C - LOAD_FAST           'atrBonusTotal'
                             0000023C     7C - LOAD_FAST           'defenderTotal'
                             0000023F     7C - LOAD_FAST           'defBonusTotal'
                             00000242     66 - BUILD_TUPLE         r0004
                             00000245     83 - CALL_FUNCTION       r0005
                             00000248     01 - POP_TOP             
                             00000249     74 - LOAD_GLOBAL         'Utility'
                             0000024C     69 - LOAD_ATTR           'SendAbilityOutputToTarget'
                             0000024F     74 - LOAD_GLOBAL         'StringTable'
                             00000252     69 - LOAD_ATTR           'ID_ABILITY_RANGED_FREE_ATTACK_FAILURE_TARGET'
                             00000255     7C - LOAD_FAST           'sentence'
                             00000258     69 - LOAD_ATTR           'verbID'
                             0000025B     7C - LOAD_FAST           'sentence'
                             0000025E     69 - LOAD_ATTR           'subject'
                             00000261     69 - LOAD_ATTR           'locator'
                             00000264     7C - LOAD_FAST           'sentence'
                             00000267     69 - LOAD_ATTR           'directObject'
                             0000026A     69 - LOAD_ATTR           'locator'
                             0000026D     7C - LOAD_FAST           'attackerTotal'
                             00000270     7C - LOAD_FAST           'atrBonusTotal'
                             00000273     7C - LOAD_FAST           'defenderTotal'
                             00000276     7C - LOAD_FAST           'defBonusTotal'
                             00000279     66 - BUILD_TUPLE         r0004
                             0000027C     83 - CALL_FUNCTION       r0005
                             0000027F     01 - POP_TOP             
                             00000280     74 - LOAD_GLOBAL         'DEFLECTED'
                             00000283     7C - LOAD_FAST           'sentence'
                             00000286     5F - STORE_ATTR          'result'
                             00000289     64 - LOAD_CONST          None
                             0000028C     53 - RETURN_VALUE        
                         consts:
0000125A                     TUPLE: (
0000125F                         None (4E),
00001260                         INT: 0 (00 00 00 00),
00001265                         INT: 1 (01 00 00 00)
                             )
                         names:
0000126A                     TUPLE: (
0000126F                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65),
0000127C                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00001288                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00001296                         STR: 'isInCombat' (0A 00 00 00 69 73 49 6E 43 6F 6D 62 61 74),
000012A5                         STR: 'isCombatTarget' (0E 00 00 00 69 73 43 6F 6D 62 61 74 54 61 72 67 65 74),
000012B8                         STR: 'directObject' (0C 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74),
000012C9                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
000012D5                         STR: 'abilitylib' (0A 00 00 00 61 62 69 6C 69 74 79 6C 69 62),
000012E4                         STR: 'createsAnExchange' (11 00 00 00 63 72 65 61 74 65 73 41 6E 45 78 63 68 61 6E 67 65),
000012FA                         STR: 'verbID' (06 00 00 00 76 65 72 62 49 44),
00001305                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00001311                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
0000131C                         STR: 'defBonusTotal' (0D 00 00 00 64 65 66 42 6F 6E 75 73 54 6F 74 61 6C),
0000132E                         STR: 'atrBonusTotal' (0D 00 00 00 61 74 72 42 6F 6E 75 73 54 6F 74 61 6C),
00001340                         STR: 'hasAbility' (0A 00 00 00 68 61 73 41 62 69 6C 69 74 79),
0000134F                         STR: 'MeleeCombatTacticsAbility' (19 00 00 00 4D 65 6C 65 65 43 6F 6D 62 61 74 54 61 63 74 69 63 73 41 62 69 6C 69 74 79),
0000136D                         STR: 'atrHasMeleeBonus' (10 00 00 00 61 74 72 48 61 73 4D 65 6C 65 65 42 6F 6E 75 73),
00001382                         STR: 'MeleeDefenseTacticsAbility' (1A 00 00 00 4D 65 6C 65 65 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 41 62 69 6C 69 74 79),
000013A1                         STR: 'defHasMeleeDefBonus' (13 00 00 00 64 65 66 48 61 73 4D 65 6C 65 65 44 65 66 42 6F 6E 75 73),
000013B9                         STR: 'abilities' (09 00 00 00 61 62 69 6C 69 74 69 65 73),
000013C7                         STR: 'ConsistencyAbility' (12 00 00 00 43 6F 6E 73 69 73 74 65 6E 63 79 41 62 69 6C 69 74 79),
000013DE                         STR: 'atrConsistancy' (0E 00 00 00 61 74 72 43 6F 6E 73 69 73 74 61 6E 63 79),
000013F1                         STR: 'defConsistancy' (0E 00 00 00 64 65 66 43 6F 6E 73 69 73 74 61 6E 63 79),
00001404                         STR: 'CurrentTacticAbility' (14 00 00 00 43 75 72 72 65 6E 74 54 61 63 74 69 63 41 62 69 6C 69 74 79),
0000141D                         STR: 'atrTactic' (09 00 00 00 61 74 72 54 61 63 74 69 63),
0000142B                         STR: 'defTactic' (09 00 00 00 64 65 66 54 61 63 74 69 63),
00001439                         STR: 'int' (03 00 00 00 69 6E 74),
00001441                         STR: 'float' (05 00 00 00 66 6C 6F 61 74),
0000144B                         STR: 'CC' (02 00 00 00 43 43),
00001452                         STR: 'GetTacticCombatTacticsMod' (19 00 00 00 47 65 74 54 61 63 74 69 63 43 6F 6D 62 61 74 54 61 63 74 69 63 73 4D 6F 64),
00001470                         STR: 'GetTacticDefenseTacticsMod' (1A 00 00 00 47 65 74 54 61 63 74 69 63 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 4D 6F 64),
0000148F                         STR: 'ComputeAttackerTotal' (14 00 00 00 43 6F 6D 70 75 74 65 41 74 74 61 63 6B 65 72 54 6F 74 61 6C),
000014A8                         STR: 'attackerTotal' (0D 00 00 00 61 74 74 61 63 6B 65 72 54 6F 74 61 6C),
000014BA                         STR: 'ComputeDefenderTotal' (14 00 00 00 43 6F 6D 70 75 74 65 44 65 66 65 6E 64 65 72 54 6F 74 61 6C),
000014D3                         STR: 'defenderTotal' (0D 00 00 00 64 65 66 65 6E 64 65 72 54 6F 74 61 6C),
000014E5                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
000014F4                         STR: 'OldTacticRolls' (0E 00 00 00 4F 6C 64 54 61 63 74 69 63 52 6F 6C 6C 73),
00001507                         STR: 'GenericFreeAttackTest' (15 00 00 00 47 65 6E 65 72 69 63 46 72 65 65 41 74 74 61 63 6B 54 65 73 74),
00001521                         STR: 'atrWon' (06 00 00 00 61 74 72 57 6F 6E),
0000152C                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00001538                         STR: 'SendAbilityOutputToCaster' (19 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 43 61 73 74 65 72),
00001556                         STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00001566                         STR: 'ID_ABILITY_RANGED_FREE_ATTACK_SUCCESS_CASTER' (2C 00 00 00 49 44 5F 41 42 49 4C 49 54 59 5F 52 41 4E 47 45 44 5F 46 52 45 45 5F 41 54 54 41 43 4B 5F 53 55 43 43 45 53 53 5F 43 41 53 54 45 52),
00001597                         STR: 'SendAbilityOutputToTarget' (19 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 54 61 72 67 65 74),
000015B5                         STR: 'ID_ABILITY_RANGED_FREE_ATTACK_SUCCESS_TARGET' (2C 00 00 00 49 44 5F 41 42 49 4C 49 54 59 5F 52 41 4E 47 45 44 5F 46 52 45 45 5F 41 54 54 41 43 4B 5F 53 55 43 43 45 53 53 5F 54 41 52 47 45 54),
000015E6                         STR: 'ID_ABILITY_RANGED_FREE_ATTACK_FAILURE_CASTER' (2C 00 00 00 49 44 5F 41 42 49 4C 49 54 59 5F 52 41 4E 47 45 44 5F 46 52 45 45 5F 41 54 54 41 43 4B 5F 46 41 49 4C 55 52 45 5F 43 41 53 54 45 52),
00001617                         STR: 'ID_ABILITY_RANGED_FREE_ATTACK_FAILURE_TARGET' (2C 00 00 00 49 44 5F 41 42 49 4C 49 54 59 5F 52 41 4E 47 45 44 5F 46 52 45 45 5F 41 54 54 41 43 4B 5F 46 41 49 4C 55 52 45 5F 54 41 52 47 45 54),
00001648                         STR: 'DEFLECTED' (09 00 00 00 44 45 46 4C 45 43 54 45 44)
                             )
                         varnames:
00001656                     TUPLE: (
0000165B                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65),
00001668                         STR: 'defConsistancy' (0E 00 00 00 64 65 66 43 6F 6E 73 69 73 74 61 6E 63 79),
0000167B                         STR: 'defenderTotal' (0D 00 00 00 64 65 66 65 6E 64 65 72 54 6F 74 61 6C),
0000168D                         STR: 'atrTactic' (09 00 00 00 61 74 72 54 61 63 74 69 63),
0000169B                         STR: 'atrWon' (06 00 00 00 61 74 72 57 6F 6E),
000016A6                         STR: 'defHasMeleeDefBonus' (13 00 00 00 64 65 66 48 61 73 4D 65 6C 65 65 44 65 66 42 6F 6E 75 73),
000016BE                         STR: 'attackerTotal' (0D 00 00 00 61 74 74 61 63 6B 65 72 54 6F 74 61 6C),
000016D0                         STR: 'atrConsistancy' (0E 00 00 00 61 74 72 43 6F 6E 73 69 73 74 61 6E 63 79),
000016E3                         STR: 'atrBonusTotal' (0D 00 00 00 61 74 72 42 6F 6E 75 73 54 6F 74 61 6C),
000016F5                         STR: 'defBonusTotal' (0D 00 00 00 64 65 66 42 6F 6E 75 73 54 6F 74 61 6C),
00001707                         STR: 'defTactic' (09 00 00 00 64 65 66 54 61 63 74 69 63),
00001715                         STR: 'atrHasMeleeBonus' (10 00 00 00 61 74 72 48 61 73 4D 65 6C 65 65 42 6F 6E 75 73)
                             )
                         freevars:
0000172A                     TUPLE: ()
                         cellvars:
0000172F                     TUPLE: ()
                         filename:
00001734                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\generic_free_attacks.py' (4C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 67 65 6E 65 72 69 63 5F 66 72 65 65 5F 61 74 74 61 63 6B 73 2E 70 79)
                         name:
00001785                     STR: 'AbilityMeleeFreeAttack' (16 00 00 00 41 62 69 6C 69 74 79 4D 65 6C 65 65 46 72 65 65 41 74 74 61 63 6B)
                         firslineno:
000017A0                     LONG: 109L (6D 00 00 00)
                         lnotab:
000017A4                     STR: '\x00\x03?\x01\t\x01\x08\x02\x06\x01\x06\x02\x10\x01\x10\x02\x10\x01\x10\x03\x07\x01\x18\x03\x07\x01\x18\x03\x10\x01\x10\x01\x1f\x01\x1f\x03\x0f\x01\x0f\x02\x0b\x01\x06\x01\n\x03\x15\x01\t\x01\r\x017\x017\x01\x08\x027\x017\x01' (3E 00 00 00 00 03 3F 01 09 01 08 02 06 01 06 02 10 01 10 02 10 01 10 03 07 01 18 03 07 01 18 03 10 01 10 01 1F 01 1F 03 0F 01 0F 02 0B 01 06 01 0A 03 15 01 09 01 0D 01 37 01 37 01 08 02 37 01 37 01),
000017E7             STR: '\ndirectObject.hasAbility[CurrentTacticAbility]\ndirectObject.hasAbility[MeleeDefenseTacticsAbility]\ndirectObject.abilities[MeleeDefenseTacticsAbility]\ndirectObject.abilities[ConsistencyAbility]\ndirectObject.abilities[CurrentTacticAbility]\ndirectObject.locator\n' (03 01 00 00 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 68 61 73 41 62 69 6C 69 74 79 5B 43 75 72 72 65 6E 74 54 61 63 74 69 63 41 62 69 6C 69 74 79 5D 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 68 61 73 41 62 69 6C 69 74 79 5B 4D 65 6C 65 65 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 41 62 69 6C 69 74 79 5D 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 61 62 69 6C 69 74 69 65 73 5B 4D 65 6C 65 65 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 41 62 69 6C 69 74 79 5D 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 61 62 69 6C 69 74 69 65 73 5B 43 6F 6E 73 69 73 74 65 6E 63 79 41 62 69 6C 69 74 79 5D 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 61 62 69 6C 69 74 69 65 73 5B 43 75 72 72 65 6E 74 54 61 63 74 69 63 41 62 69 6C 69 74 79 5D 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 6C 6F 63 61 74 6F 72 0A),
000018EF             CODE:
                         argcount:
000018F0                     LONG: 1L (01 00 00 00)
                         nlocals:
000018F4                     LONG: 12L (0C 00 00 00)
                         stacksize:
000018F8                     LONG: 9L (09 00 00 00)
                         flags:
000018FC                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001900                     STR: "|\x00\x00i\x01\x00i\x02\x00i\x03\x00o,\x00\x01|\x00\x00i\x01\x00i\x02\x00i\x04\x00|\x00\x00i\x05\x00i\x06\x00\x83\x01\x00o\x10\x00\x01t\x07\x00i\x08\x00|\x00\x00i\t\x00\x83\x01\x00o\x11\x00\x01t\n\x00|\x00\x00_\x0b\x00d\x00\x00Sn\x01\x00\x01d\x01\x00}\x08\x00d\x01\x00}\x07\x00|\x00\x00i\x01\x00i\x0e\x00t\x0f\x00\x19}\x04\x00|\x00\x00i\x05\x00i\x0e\x00t\x11\x00\x19}\x0b\x00|\x00\x00i\x01\x00i\x13\x00t\x14\x00\x19}\x06\x00|\x00\x00i\x05\x00i\x13\x00t\x14\x00\x19}\x01\x00|\x04\x00o\x18\x00\x01|\x07\x00|\x00\x00i\x01\x00i\x13\x00t\x0f\x00\x197}\x07\x00n\x01\x00\x01|\x0b\x00o\x18\x00\x01|\x08\x00|\x00\x00i\x05\x00i\x13\x00t\x11\x00\x197}\x08\x00n\x01\x00\x01|\x00\x00i\x01\x00i\x13\x00t\x17\x00\x19}\x03\x00|\x00\x00i\x05\x00i\x13\x00t\x17\x00\x19}\t\x00t\x1a\x00i\x1b\x00d\x02\x00|\x03\x00|\t\x00f\x02\x00\x16d\x03\x00\x83\x02\x00\x01t\x1c\x00t\x1d\x00|\x07\x00\x83\x01\x00t\x1e\x00i\x1f\x00|\x03\x00\x83\x01\x00\x14\x83\x01\x00}\x07\x00t\x1c\x00t\x1d\x00|\x08\x00\x83\x01\x00t\x1e\x00i \x00|\t\x00\x83\x01\x00\x14\x83\x01\x00}\x08\x00t!\x00|\x07\x00|\x06\x00\x83\x02\x00}\x05\x00t#\x00|\x08\x00|\x01\x00\x83\x02\x00}\x02\x00t%\x00i&\x00\x0co\x10\x00\x01d\x01\x00}\x08\x00d\x01\x00}\x07\x00n\x01\x00\x01t'\x00|\x07\x00|\x05\x00|\x08\x00|\x02\x00\x83\x04\x00}\n\x00t\n\x00|\x00\x00_\x0b\x00|\n\x00d\x04\x00j\x02\x00ov\x00\x01t)\x00i*\x00t+\x00i,\x00|\x00\x00i\t\x00|\x00\x00i\x01\x00i\x06\x00|\x00\x00i\x05\x00i\x06\x00|\x05\x00|\x07\x00|\x02\x00|\x08\x00f\x04\x00\x83\x05\x00\x01t)\x00i-\x00t+\x00i.\x00|\x00\x00i\t\x00|\x00\x00i\x01\x00i\x06\x00|\x00\x00i\x05\x00i\x06\x00|\x05\x00|\x07\x00|\x02\x00|\x08\x00f\x04\x00\x83\x05\x00\x01d\x00\x00Sn\x01\x00\x01t)\x00i*\x00t+\x00i/\x00|\x00\x00i\t\x00|\x00\x00i\x01\x00i\x06\x00|\x00\x00i\x05\x00i\x06\x00|\x05\x00|\x07\x00|\x02\x00|\x08\x00f\x04\x00\x83\x05\x00\x01t)\x00i-\x00t+\x00i0\x00|\x00\x00i\t\x00|\x00\x00i\x01\x00i\x06\x00|\x00\x00i\x05\x00i\x06\x00|\x05\x00|\x07\x00|\x02\x00|\x08\x00f\x04\x00\x83\x05\x00\x01t1\x00|\x00\x00_\x0b\x00d\x00\x00S" (A7 02 00 00 7C 00 00 69 01 00 69 02 00 69 03 00 6F 2C 00 01 7C 00 00 69 01 00 69 02 00 69 04 00 7C 00 00 69 05 00 69 06 00 83 01 00 6F 10 00 01 74 07 00 69 08 00 7C 00 00 69 09 00 83 01 00 6F 11 00 01 74 0A 00 7C 00 00 5F 0B 00 64 00 00 53 6E 01 00 01 64 01 00 7D 08 00 64 01 00 7D 07 00 7C 00 00 69 01 00 69 0E 00 74 0F 00 19 7D 04 00 7C 00 00 69 05 00 69 0E 00 74 11 00 19 7D 0B 00 7C 00 00 69 01 00 69 13 00 74 14 00 19 7D 06 00 7C 00 00 69 05 00 69 13 00 74 14 00 19 7D 01 00 7C 04 00 6F 18 00 01 7C 07 00 7C 00 00 69 01 00 69 13 00 74 0F 00 19 37 7D 07 00 6E 01 00 01 7C 0B 00 6F 18 00 01 7C 08 00 7C 00 00 69 05 00 69 13 00 74 11 00 19 37 7D 08 00 6E 01 00 01 7C 00 00 69 01 00 69 13 00 74 17 00 19 7D 03 00 7C 00 00 69 05 00 69 13 00 74 17 00 19 7D 09 00 74 1A 00 69 1B 00 64 02 00 7C 03 00 7C 09 00 66 02 00 16 64 03 00 83 02 00 01 74 1C 00 74 1D 00 7C 07 00 83 01 00 74 1E 00 69 1F 00 7C 03 00 83 01 00 14 83 01 00 7D 07 00 74 1C 00 74 1D 00 7C 08 00 83 01 00 74 1E 00 69 20 00 7C 09 00 83 01 00 14 83 01 00 7D 08 00 74 21 00 7C 07 00 7C 06 00 83 02 00 7D 05 00 74 23 00 7C 08 00 7C 01 00 83 02 00 7D 02 00 74 25 00 69 26 00 0C 6F 10 00 01 64 01 00 7D 08 00 64 01 00 7D 07 00 6E 01 00 01 74 27 00 7C 07 00 7C 05 00 7C 08 00 7C 02 00 83 04 00 7D 0A 00 74 0A 00 7C 00 00 5F 0B 00 7C 0A 00 64 04 00 6A 02 00 6F 76 00 01 74 29 00 69 2A 00 74 2B 00 69 2C 00 7C 00 00 69 09 00 7C 00 00 69 01 00 69 06 00 7C 00 00 69 05 00 69 06 00 7C 05 00 7C 07 00 7C 02 00 7C 08 00 66 04 00 83 05 00 01 74 29 00 69 2D 00 74 2B 00 69 2E 00 7C 00 00 69 09 00 7C 00 00 69 01 00 69 06 00 7C 00 00 69 05 00 69 06 00 7C 05 00 7C 07 00 7C 02 00 7C 08 00 66 04 00 83 05 00 01 64 00 00 53 6E 01 00 01 74 29 00 69 2A 00 74 2B 00 69 2F 00 7C 00 00 69 09 00 7C 00 00 69 01 00 69 06 00 7C 00 00 69 05 00 69 06 00 7C 05 00 7C 07 00 7C 02 00 7C 08 00 66 04 00 83 05 00 01 74 29 00 69 2D 00 74 2B 00 69 30 00 7C 00 00 69 09 00 7C 00 00 69 01 00 69 06 00 7C 00 00 69 05 00 69 06 00 7C 05 00 7C 07 00 7C 02 00 7C 08 00 66 04 00 83 05 00 01 74 31 00 7C 00 00 5F 0B 00 64 00 00 53)
                             00000000     7C - LOAD_FAST           'sentence'
                             00000003     69 - LOAD_ATTR           'subject'
                             00000006     69 - LOAD_ATTR           'Interlock'
                             00000009     69 - LOAD_ATTR           'isInCombat'
                             0000000C     6F - JUMP_IF_FALSE       -> 0000003B
                             0000000F     01 - POP_TOP             
                             00000010     7C - LOAD_FAST           'sentence'
                             00000013     69 - LOAD_ATTR           'subject'
                             00000016     69 - LOAD_ATTR           'Interlock'
                             00000019     69 - LOAD_ATTR           'isCombatTarget'
                             0000001C     7C - LOAD_FAST           'sentence'
                             0000001F     69 - LOAD_ATTR           'directObject'
                             00000022     69 - LOAD_ATTR           'locator'
                             00000025     83 - CALL_FUNCTION       r0001
                             00000028     6F - JUMP_IF_FALSE       -> 0000003B
                             0000002B     01 - POP_TOP             
                             0000002C     74 - LOAD_GLOBAL         'abilitylib'
                             0000002F     69 - LOAD_ATTR           'createsAnExchange'
                             00000032     7C - LOAD_FAST           'sentence'
                             00000035     69 - LOAD_ATTR           'verbID'
                             00000038     83 - CALL_FUNCTION       r0001
                             0000003B     6F - JUMP_IF_FALSE       -> 0000004F
                             0000003E     01 - POP_TOP             
                             0000003F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000042     7C - LOAD_FAST           'sentence'
                             00000045     5F - STORE_ATTR          'result'
                             00000048     64 - LOAD_CONST          None
                             0000004B     53 - RETURN_VALUE        
                             0000004C     6E - JUMP_FORWARD        -> 00000050
                             0000004F     01 - POP_TOP             
                             00000050     64 - LOAD_CONST          0
                             00000053     7D - STORE_FAST          'defBonusTotal'
                             00000056     64 - LOAD_CONST          0
                             00000059     7D - STORE_FAST          'atrBonusTotal'
                             0000005C     7C - LOAD_FAST           'sentence'
                             0000005F     69 - LOAD_ATTR           'subject'
                             00000062     69 - LOAD_ATTR           'hasAbility'
                             00000065     74 - LOAD_GLOBAL         'RangeCombatTacticsAbility'
                             00000068     19 - BINARY_SUBSCR       
                             00000069     7D - STORE_FAST          'atrHasRangedBonus'
                             0000006C     7C - LOAD_FAST           'sentence'
                             0000006F     69 - LOAD_ATTR           'directObject'
                             00000072     69 - LOAD_ATTR           'hasAbility'
                             00000075     74 - LOAD_GLOBAL         'RangedDefenseTacticsAbility'
                             00000078     19 - BINARY_SUBSCR       
                             00000079     7D - STORE_FAST          'defHasRangedDefBonus'
                             0000007C     7C - LOAD_FAST           'sentence'
                             0000007F     69 - LOAD_ATTR           'subject'
                             00000082     69 - LOAD_ATTR           'abilities'
                             00000085     74 - LOAD_GLOBAL         'ConsistencyAbility'
                             00000088     19 - BINARY_SUBSCR       
                             00000089     7D - STORE_FAST          'atrConsistancy'
                             0000008C     7C - LOAD_FAST           'sentence'
                             0000008F     69 - LOAD_ATTR           'directObject'
                             00000092     69 - LOAD_ATTR           'abilities'
                             00000095     74 - LOAD_GLOBAL         'ConsistencyAbility'
                             00000098     19 - BINARY_SUBSCR       
                             00000099     7D - STORE_FAST          'defConsistancy'
                             0000009C     7C - LOAD_FAST           'atrHasRangedBonus'
                             0000009F     6F - JUMP_IF_FALSE       -> 000000BA
                             000000A2     01 - POP_TOP             
                             000000A3     7C - LOAD_FAST           'atrBonusTotal'
                             000000A6     7C - LOAD_FAST           'sentence'
                             000000A9     69 - LOAD_ATTR           'subject'
                             000000AC     69 - LOAD_ATTR           'abilities'
                             000000AF     74 - LOAD_GLOBAL         'RangeCombatTacticsAbility'
                             000000B2     19 - BINARY_SUBSCR       
                             000000B3     37 - INPLACE_ADD         
                             000000B4     7D - STORE_FAST          'atrBonusTotal'
                             000000B7     6E - JUMP_FORWARD        -> 000000BB
                             000000BA     01 - POP_TOP             
                             000000BB     7C - LOAD_FAST           'defHasRangedDefBonus'
                             000000BE     6F - JUMP_IF_FALSE       -> 000000D9
                             000000C1     01 - POP_TOP             
                             000000C2     7C - LOAD_FAST           'defBonusTotal'
                             000000C5     7C - LOAD_FAST           'sentence'
                             000000C8     69 - LOAD_ATTR           'directObject'
                             000000CB     69 - LOAD_ATTR           'abilities'
                             000000CE     74 - LOAD_GLOBAL         'RangedDefenseTacticsAbility'
                             000000D1     19 - BINARY_SUBSCR       
                             000000D2     37 - INPLACE_ADD         
                             000000D3     7D - STORE_FAST          'defBonusTotal'
                             000000D6     6E - JUMP_FORWARD        -> 000000DA
                             000000D9     01 - POP_TOP             
                             000000DA     7C - LOAD_FAST           'sentence'
                             000000DD     69 - LOAD_ATTR           'subject'
                             000000E0     69 - LOAD_ATTR           'abilities'
                             000000E3     74 - LOAD_GLOBAL         'CurrentTacticAbility'
                             000000E6     19 - BINARY_SUBSCR       
                             000000E7     7D - STORE_FAST          'atrTactic'
                             000000EA     7C - LOAD_FAST           'sentence'
                             000000ED     69 - LOAD_ATTR           'directObject'
                             000000F0     69 - LOAD_ATTR           'abilities'
                             000000F3     74 - LOAD_GLOBAL         'CurrentTacticAbility'
                             000000F6     19 - BINARY_SUBSCR       
                             000000F7     7D - STORE_FAST          'defTactic'
                             000000FA     74 - LOAD_GLOBAL         'CU'
                             000000FD     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000100     64 - LOAD_CONST          'RangedAB Tactic A(%d) D(%d)'
                             00000103     7C - LOAD_FAST           'atrTactic'
                             00000106     7C - LOAD_FAST           'defTactic'
                             00000109     66 - BUILD_TUPLE         r0002
                             0000010C     16 - BINARY_MODULO       
                             0000010D     64 - LOAD_CONST          2
                             00000110     83 - CALL_FUNCTION       r0002
                             00000113     01 - POP_TOP             
                             00000114     74 - LOAD_GLOBAL         'int'
                             00000117     74 - LOAD_GLOBAL         'float'
                             0000011A     7C - LOAD_FAST           'atrBonusTotal'
                             0000011D     83 - CALL_FUNCTION       r0001
                             00000120     74 - LOAD_GLOBAL         'CC'
                             00000123     69 - LOAD_ATTR           'GetTacticCombatTacticsMod'
                             00000126     7C - LOAD_FAST           'atrTactic'
                             00000129     83 - CALL_FUNCTION       r0001
                             0000012C     14 - BINARY_MULTIPLY     
                             0000012D     83 - CALL_FUNCTION       r0001
                             00000130     7D - STORE_FAST          'atrBonusTotal'
                             00000133     74 - LOAD_GLOBAL         'int'
                             00000136     74 - LOAD_GLOBAL         'float'
                             00000139     7C - LOAD_FAST           'defBonusTotal'
                             0000013C     83 - CALL_FUNCTION       r0001
                             0000013F     74 - LOAD_GLOBAL         'CC'
                             00000142     69 - LOAD_ATTR           'GetTacticDefenseTacticsMod'
                             00000145     7C - LOAD_FAST           'defTactic'
                             00000148     83 - CALL_FUNCTION       r0001
                             0000014B     14 - BINARY_MULTIPLY     
                             0000014C     83 - CALL_FUNCTION       r0001
                             0000014F     7D - STORE_FAST          'defBonusTotal'
                             00000152     74 - LOAD_GLOBAL         'ComputeAttackerTotal'
                             00000155     7C - LOAD_FAST           'atrBonusTotal'
                             00000158     7C - LOAD_FAST           'atrConsistancy'
                             0000015B     83 - CALL_FUNCTION       r0002
                             0000015E     7D - STORE_FAST          'attackerTotal'
                             00000161     74 - LOAD_GLOBAL         'ComputeDefenderTotal'
                             00000164     7C - LOAD_FAST           'defBonusTotal'
                             00000167     7C - LOAD_FAST           'defConsistancy'
                             0000016A     83 - CALL_FUNCTION       r0002
                             0000016D     7D - STORE_FAST          'defenderTotal'
                             00000170     74 - LOAD_GLOBAL         'consolevar'
                             00000173     69 - LOAD_ATTR           'OldTacticRolls'
                             00000176     0C - UNARY_NOT           
                             00000177     6F - JUMP_IF_FALSE       -> 0000018A
                             0000017A     01 - POP_TOP             
                             0000017B     64 - LOAD_CONST          0
                             0000017E     7D - STORE_FAST          'defBonusTotal'
                             00000181     64 - LOAD_CONST          0
                             00000184     7D - STORE_FAST          'atrBonusTotal'
                             00000187     6E - JUMP_FORWARD        -> 0000018B
                             0000018A     01 - POP_TOP             
                             0000018B     74 - LOAD_GLOBAL         'GenericFreeAttackTest'
                             0000018E     7C - LOAD_FAST           'atrBonusTotal'
                             00000191     7C - LOAD_FAST           'attackerTotal'
                             00000194     7C - LOAD_FAST           'defBonusTotal'
                             00000197     7C - LOAD_FAST           'defenderTotal'
                             0000019A     83 - CALL_FUNCTION       r0004
                             0000019D     7D - STORE_FAST          'atrWon'
                             000001A0     74 - LOAD_GLOBAL         'SUCCESS'
                             000001A3     7C - LOAD_FAST           'sentence'
                             000001A6     5F - STORE_ATTR          'result'
                             000001A9     7C - LOAD_FAST           'atrWon'
                             000001AC     64 - LOAD_CONST          1
                             000001AF     6A - COMPARE_OP          "=="
                             000001B2     6F - JUMP_IF_FALSE       -> 0000022B
                             000001B5     01 - POP_TOP             
                             000001B6     74 - LOAD_GLOBAL         'Utility'
                             000001B9     69 - LOAD_ATTR           'SendAbilityOutputToCaster'
                             000001BC     74 - LOAD_GLOBAL         'StringTable'
                             000001BF     69 - LOAD_ATTR           'ID_ABILITY_RANGED_FREE_ATTACK_SUCCESS_CASTER'
                             000001C2     7C - LOAD_FAST           'sentence'
                             000001C5     69 - LOAD_ATTR           'verbID'
                             000001C8     7C - LOAD_FAST           'sentence'
                             000001CB     69 - LOAD_ATTR           'subject'
                             000001CE     69 - LOAD_ATTR           'locator'
                             000001D1     7C - LOAD_FAST           'sentence'
                             000001D4     69 - LOAD_ATTR           'directObject'
                             000001D7     69 - LOAD_ATTR           'locator'
                             000001DA     7C - LOAD_FAST           'attackerTotal'
                             000001DD     7C - LOAD_FAST           'atrBonusTotal'
                             000001E0     7C - LOAD_FAST           'defenderTotal'
                             000001E3     7C - LOAD_FAST           'defBonusTotal'
                             000001E6     66 - BUILD_TUPLE         r0004
                             000001E9     83 - CALL_FUNCTION       r0005
                             000001EC     01 - POP_TOP             
                             000001ED     74 - LOAD_GLOBAL         'Utility'
                             000001F0     69 - LOAD_ATTR           'SendAbilityOutputToTarget'
                             000001F3     74 - LOAD_GLOBAL         'StringTable'
                             000001F6     69 - LOAD_ATTR           'ID_ABILITY_RANGED_FREE_ATTACK_SUCCESS_TARGET'
                             000001F9     7C - LOAD_FAST           'sentence'
                             000001FC     69 - LOAD_ATTR           'verbID'
                             000001FF     7C - LOAD_FAST           'sentence'
                             00000202     69 - LOAD_ATTR           'subject'
                             00000205     69 - LOAD_ATTR           'locator'
                             00000208     7C - LOAD_FAST           'sentence'
                             0000020B     69 - LOAD_ATTR           'directObject'
                             0000020E     69 - LOAD_ATTR           'locator'
                             00000211     7C - LOAD_FAST           'attackerTotal'
                             00000214     7C - LOAD_FAST           'atrBonusTotal'
                             00000217     7C - LOAD_FAST           'defenderTotal'
                             0000021A     7C - LOAD_FAST           'defBonusTotal'
                             0000021D     66 - BUILD_TUPLE         r0004
                             00000220     83 - CALL_FUNCTION       r0005
                             00000223     01 - POP_TOP             
                             00000224     64 - LOAD_CONST          None
                             00000227     53 - RETURN_VALUE        
                             00000228     6E - JUMP_FORWARD        -> 0000022C
                             0000022B     01 - POP_TOP             
                             0000022C     74 - LOAD_GLOBAL         'Utility'
                             0000022F     69 - LOAD_ATTR           'SendAbilityOutputToCaster'
                             00000232     74 - LOAD_GLOBAL         'StringTable'
                             00000235     69 - LOAD_ATTR           'ID_ABILITY_RANGED_FREE_ATTACK_FAILURE_CASTER'
                             00000238     7C - LOAD_FAST           'sentence'
                             0000023B     69 - LOAD_ATTR           'verbID'
                             0000023E     7C - LOAD_FAST           'sentence'
                             00000241     69 - LOAD_ATTR           'subject'
                             00000244     69 - LOAD_ATTR           'locator'
                             00000247     7C - LOAD_FAST           'sentence'
                             0000024A     69 - LOAD_ATTR           'directObject'
                             0000024D     69 - LOAD_ATTR           'locator'
                             00000250     7C - LOAD_FAST           'attackerTotal'
                             00000253     7C - LOAD_FAST           'atrBonusTotal'
                             00000256     7C - LOAD_FAST           'defenderTotal'
                             00000259     7C - LOAD_FAST           'defBonusTotal'
                             0000025C     66 - BUILD_TUPLE         r0004
                             0000025F     83 - CALL_FUNCTION       r0005
                             00000262     01 - POP_TOP             
                             00000263     74 - LOAD_GLOBAL         'Utility'
                             00000266     69 - LOAD_ATTR           'SendAbilityOutputToTarget'
                             00000269     74 - LOAD_GLOBAL         'StringTable'
                             0000026C     69 - LOAD_ATTR           'ID_ABILITY_RANGED_FREE_ATTACK_FAILURE_TARGET'
                             0000026F     7C - LOAD_FAST           'sentence'
                             00000272     69 - LOAD_ATTR           'verbID'
                             00000275     7C - LOAD_FAST           'sentence'
                             00000278     69 - LOAD_ATTR           'subject'
                             0000027B     69 - LOAD_ATTR           'locator'
                             0000027E     7C - LOAD_FAST           'sentence'
                             00000281     69 - LOAD_ATTR           'directObject'
                             00000284     69 - LOAD_ATTR           'locator'
                             00000287     7C - LOAD_FAST           'attackerTotal'
                             0000028A     7C - LOAD_FAST           'atrBonusTotal'
                             0000028D     7C - LOAD_FAST           'defenderTotal'
                             00000290     7C - LOAD_FAST           'defBonusTotal'
                             00000293     66 - BUILD_TUPLE         r0004
                             00000296     83 - CALL_FUNCTION       r0005
                             00000299     01 - POP_TOP             
                             0000029A     74 - LOAD_GLOBAL         'DEFLECTED'
                             0000029D     7C - LOAD_FAST           'sentence'
                             000002A0     5F - STORE_ATTR          'result'
                             000002A3     64 - LOAD_CONST          None
                             000002A6     53 - RETURN_VALUE        
                         consts:
00001BAC                     TUPLE: (
00001BB1                         None (4E),
00001BB2                         INT: 0 (00 00 00 00),
00001BB7                         STR: 'RangedAB Tactic A(%d) D(%d)' (1B 00 00 00 52 61 6E 67 65 64 41 42 20 54 61 63 74 69 63 20 41 28 25 64 29 20 44 28 25 64 29),
00001BD7                         INT: 2 (02 00 00 00),
00001BDC                         INT: 1 (01 00 00 00)
                             )
                         names:
00001BE1                     TUPLE: (
00001BE6                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65),
00001BF3                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00001BFF                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00001C0D                         STR: 'isInCombat' (0A 00 00 00 69 73 49 6E 43 6F 6D 62 61 74),
00001C1C                         STR: 'isCombatTarget' (0E 00 00 00 69 73 43 6F 6D 62 61 74 54 61 72 67 65 74),
00001C2F                         STR: 'directObject' (0C 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74),
00001C40                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
00001C4C                         STR: 'abilitylib' (0A 00 00 00 61 62 69 6C 69 74 79 6C 69 62),
00001C5B                         STR: 'createsAnExchange' (11 00 00 00 63 72 65 61 74 65 73 41 6E 45 78 63 68 61 6E 67 65),
00001C71                         STR: 'verbID' (06 00 00 00 76 65 72 62 49 44),
00001C7C                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00001C88                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00001C93                         STR: 'defBonusTotal' (0D 00 00 00 64 65 66 42 6F 6E 75 73 54 6F 74 61 6C),
00001CA5                         STR: 'atrBonusTotal' (0D 00 00 00 61 74 72 42 6F 6E 75 73 54 6F 74 61 6C),
00001CB7                         STR: 'hasAbility' (0A 00 00 00 68 61 73 41 62 69 6C 69 74 79),
00001CC6                         STR: 'RangeCombatTacticsAbility' (19 00 00 00 52 61 6E 67 65 43 6F 6D 62 61 74 54 61 63 74 69 63 73 41 62 69 6C 69 74 79),
00001CE4                         STR: 'atrHasRangedBonus' (11 00 00 00 61 74 72 48 61 73 52 61 6E 67 65 64 42 6F 6E 75 73),
00001CFA                         STR: 'RangedDefenseTacticsAbility' (1B 00 00 00 52 61 6E 67 65 64 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 41 62 69 6C 69 74 79),
00001D1A                         STR: 'defHasRangedDefBonus' (14 00 00 00 64 65 66 48 61 73 52 61 6E 67 65 64 44 65 66 42 6F 6E 75 73),
00001D33                         STR: 'abilities' (09 00 00 00 61 62 69 6C 69 74 69 65 73),
00001D41                         STR: 'ConsistencyAbility' (12 00 00 00 43 6F 6E 73 69 73 74 65 6E 63 79 41 62 69 6C 69 74 79),
00001D58                         STR: 'atrConsistancy' (0E 00 00 00 61 74 72 43 6F 6E 73 69 73 74 61 6E 63 79),
00001D6B                         STR: 'defConsistancy' (0E 00 00 00 64 65 66 43 6F 6E 73 69 73 74 61 6E 63 79),
00001D7E                         STR: 'CurrentTacticAbility' (14 00 00 00 43 75 72 72 65 6E 74 54 61 63 74 69 63 41 62 69 6C 69 74 79),
00001D97                         STR: 'atrTactic' (09 00 00 00 61 74 72 54 61 63 74 69 63),
00001DA5                         STR: 'defTactic' (09 00 00 00 64 65 66 54 61 63 74 69 63),
00001DB3                         STR: 'CU' (02 00 00 00 43 55),
00001DBA                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
00001DD7                         STR: 'int' (03 00 00 00 69 6E 74),
00001DDF                         STR: 'float' (05 00 00 00 66 6C 6F 61 74),
00001DE9                         STR: 'CC' (02 00 00 00 43 43),
00001DF0                         STR: 'GetTacticCombatTacticsMod' (19 00 00 00 47 65 74 54 61 63 74 69 63 43 6F 6D 62 61 74 54 61 63 74 69 63 73 4D 6F 64),
00001E0E                         STR: 'GetTacticDefenseTacticsMod' (1A 00 00 00 47 65 74 54 61 63 74 69 63 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 4D 6F 64),
00001E2D                         STR: 'ComputeAttackerTotal' (14 00 00 00 43 6F 6D 70 75 74 65 41 74 74 61 63 6B 65 72 54 6F 74 61 6C),
00001E46                         STR: 'attackerTotal' (0D 00 00 00 61 74 74 61 63 6B 65 72 54 6F 74 61 6C),
00001E58                         STR: 'ComputeDefenderTotal' (14 00 00 00 43 6F 6D 70 75 74 65 44 65 66 65 6E 64 65 72 54 6F 74 61 6C),
00001E71                         STR: 'defenderTotal' (0D 00 00 00 64 65 66 65 6E 64 65 72 54 6F 74 61 6C),
00001E83                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
00001E92                         STR: 'OldTacticRolls' (0E 00 00 00 4F 6C 64 54 61 63 74 69 63 52 6F 6C 6C 73),
00001EA5                         STR: 'GenericFreeAttackTest' (15 00 00 00 47 65 6E 65 72 69 63 46 72 65 65 41 74 74 61 63 6B 54 65 73 74),
00001EBF                         STR: 'atrWon' (06 00 00 00 61 74 72 57 6F 6E),
00001ECA                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00001ED6                         STR: 'SendAbilityOutputToCaster' (19 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 43 61 73 74 65 72),
00001EF4                         STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00001F04                         STR: 'ID_ABILITY_RANGED_FREE_ATTACK_SUCCESS_CASTER' (2C 00 00 00 49 44 5F 41 42 49 4C 49 54 59 5F 52 41 4E 47 45 44 5F 46 52 45 45 5F 41 54 54 41 43 4B 5F 53 55 43 43 45 53 53 5F 43 41 53 54 45 52),
00001F35                         STR: 'SendAbilityOutputToTarget' (19 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 54 61 72 67 65 74),
00001F53                         STR: 'ID_ABILITY_RANGED_FREE_ATTACK_SUCCESS_TARGET' (2C 00 00 00 49 44 5F 41 42 49 4C 49 54 59 5F 52 41 4E 47 45 44 5F 46 52 45 45 5F 41 54 54 41 43 4B 5F 53 55 43 43 45 53 53 5F 54 41 52 47 45 54),
00001F84                         STR: 'ID_ABILITY_RANGED_FREE_ATTACK_FAILURE_CASTER' (2C 00 00 00 49 44 5F 41 42 49 4C 49 54 59 5F 52 41 4E 47 45 44 5F 46 52 45 45 5F 41 54 54 41 43 4B 5F 46 41 49 4C 55 52 45 5F 43 41 53 54 45 52),
00001FB5                         STR: 'ID_ABILITY_RANGED_FREE_ATTACK_FAILURE_TARGET' (2C 00 00 00 49 44 5F 41 42 49 4C 49 54 59 5F 52 41 4E 47 45 44 5F 46 52 45 45 5F 41 54 54 41 43 4B 5F 46 41 49 4C 55 52 45 5F 54 41 52 47 45 54),
00001FE6                         STR: 'DEFLECTED' (09 00 00 00 44 45 46 4C 45 43 54 45 44)
                             )
                         varnames:
00001FF4                     TUPLE: (
00001FF9                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65),
00002006                         STR: 'defConsistancy' (0E 00 00 00 64 65 66 43 6F 6E 73 69 73 74 61 6E 63 79),
00002019                         STR: 'defenderTotal' (0D 00 00 00 64 65 66 65 6E 64 65 72 54 6F 74 61 6C),
0000202B                         STR: 'atrTactic' (09 00 00 00 61 74 72 54 61 63 74 69 63),
00002039                         STR: 'atrHasRangedBonus' (11 00 00 00 61 74 72 48 61 73 52 61 6E 67 65 64 42 6F 6E 75 73),
0000204F                         STR: 'attackerTotal' (0D 00 00 00 61 74 74 61 63 6B 65 72 54 6F 74 61 6C),
00002061                         STR: 'atrConsistancy' (0E 00 00 00 61 74 72 43 6F 6E 73 69 73 74 61 6E 63 79),
00002074                         STR: 'atrBonusTotal' (0D 00 00 00 61 74 72 42 6F 6E 75 73 54 6F 74 61 6C),
00002086                         STR: 'defBonusTotal' (0D 00 00 00 64 65 66 42 6F 6E 75 73 54 6F 74 61 6C),
00002098                         STR: 'defTactic' (09 00 00 00 64 65 66 54 61 63 74 69 63),
000020A6                         STR: 'atrWon' (06 00 00 00 61 74 72 57 6F 6E),
000020B1                         STR: 'defHasRangedDefBonus' (14 00 00 00 64 65 66 48 61 73 52 61 6E 67 65 64 44 65 66 42 6F 6E 75 73)
                             )
                         freevars:
000020CA                     TUPLE: ()
                         cellvars:
000020CF                     TUPLE: ()
                         filename:
000020D4                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\generic_free_attacks.py' (4C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 67 65 6E 65 72 69 63 5F 66 72 65 65 5F 61 74 74 61 63 6B 73 2E 70 79)
                         name:
00002125                     STR: 'AbilityRangeFreeAttack' (16 00 00 00 41 62 69 6C 69 74 79 52 61 6E 67 65 46 72 65 65 41 74 74 61 63 6B)
                         firslineno:
00002140                     LONG: 175L (AF 00 00 00)
                         lnotab:
00002144                     STR: '\x00\x03?\x01\t\x01\x08\x02\x06\x01\x06\x02\x10\x01\x10\x02\x10\x01\x10\x03\x07\x01\x18\x03\x07\x01\x18\x03\x10\x01\x10\x01\x1a\x01\x1f\x01\x1f\x03\x0f\x01\x0f\x02\x0b\x01\x06\x01\n\x03\x15\x01\t\x01\r\x017\x017\x01\x08\x027\x017\x01' (40 00 00 00 00 03 3F 01 09 01 08 02 06 01 06 02 10 01 10 02 10 01 10 03 07 01 18 03 07 01 18 03 10 01 10 01 1A 01 1F 01 1F 03 0F 01 0F 02 0B 01 06 01 0A 03 15 01 09 01 0D 01 37 01 37 01 08 02 37 01 37 01),
00002189             STR: '\ndirectObject.hasAbility[CurrentTacticAbility]\ndirectObject.hasAbility[RangedDefenseTacticsAbility]\ndirectObject.abilities[RangedDefenseTacticsAbility]\ndirectObject.abilities[ConsistencyAbility]\ndirectObject.abilities[CurrentTacticAbility]\ndirectObject.locator\n' (05 01 00 00 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 68 61 73 41 62 69 6C 69 74 79 5B 43 75 72 72 65 6E 74 54 61 63 74 69 63 41 62 69 6C 69 74 79 5D 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 68 61 73 41 62 69 6C 69 74 79 5B 52 61 6E 67 65 64 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 41 62 69 6C 69 74 79 5D 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 61 62 69 6C 69 74 69 65 73 5B 52 61 6E 67 65 64 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 41 62 69 6C 69 74 79 5D 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 61 62 69 6C 69 74 69 65 73 5B 43 6F 6E 73 69 73 74 65 6E 63 79 41 62 69 6C 69 74 79 5D 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 61 62 69 6C 69 74 69 65 73 5B 43 75 72 72 65 6E 74 54 61 63 74 69 63 41 62 69 6C 69 74 79 5D 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 6C 6F 63 61 74 6F 72 0A),
00002293             CODE:
                         argcount:
00002294                     LONG: 1L (01 00 00 00)
                         nlocals:
00002298                     LONG: 14L (0E 00 00 00)
                         stacksize:
0000229C                     LONG: 10L (0A 00 00 00)
                         flags:
000022A0                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000022A4                     STR: "|\x00\x00i\x01\x00i\x02\x00i\x03\x00o,\x00\x01|\x00\x00i\x01\x00i\x02\x00i\x04\x00|\x00\x00i\x05\x00i\x06\x00\x83\x01\x00o\x10\x00\x01t\x07\x00i\x08\x00|\x00\x00i\t\x00\x83\x01\x00o3\x00\x01t\n\x00|\x00\x00_\x0b\x00t\x0c\x00i\r\x00|\x00\x00i\x0b\x00|\x00\x00i\t\x00|\x00\x00i\x01\x00|\x00\x00i\x05\x00\x83\x04\x00\x01d\x00\x00Sn\x01\x00\x01d\x01\x00}\n\x00d\x01\x00}\t\x00|\x00\x00i\x01\x00i\x10\x00t\x11\x00\x19}\x0c\x00|\x00\x00i\x05\x00i\x10\x00t\x13\x00\x19}\r\x00|\x00\x00i\x01\x00i\x15\x00t\x16\x00\x19}\x07\x00|\x00\x00i\x05\x00i\x15\x00t\x16\x00\x19}\x01\x00|\x0c\x00o\x18\x00\x01|\t\x00|\x00\x00i\x01\x00i\x15\x00t\x11\x00\x197}\t\x00n\x01\x00\x01|\r\x00o\x18\x00\x01|\n\x00|\x00\x00i\x05\x00i\x15\x00t\x13\x00\x197}\n\x00n\x01\x00\x01|\x00\x00i\x01\x00i\x15\x00t\x19\x00\x19}\x03\x00|\x00\x00i\x05\x00i\x15\x00t\x19\x00\x19}\x0b\x00t\x1c\x00i\x1d\x00d\x02\x00|\x03\x00|\x0b\x00f\x02\x00\x16d\x03\x00\x83\x02\x00\x01t\x1c\x00i\x1d\x00d\x04\x00|\t\x00|\n\x00f\x02\x00\x16d\x03\x00\x83\x02\x00\x01t\x1e\x00i\x1f\x00|\x03\x00\x83\x01\x00}\x05\x00t\x1e\x00i!\x00|\x0b\x00\x83\x01\x00}\x02\x00t#\x00t$\x00|\t\x00\x83\x01\x00|\x05\x00\x14\x83\x01\x00}\t\x00t#\x00t$\x00|\n\x00\x83\x01\x00|\x02\x00\x14\x83\x01\x00}\n\x00t\x1c\x00i\x1d\x00d\x05\x00|\t\x00|\x05\x00|\n\x00|\x02\x00f\x04\x00\x16d\x03\x00\x83\x02\x00\x01t%\x00|\t\x00|\x07\x00\x83\x02\x00}\x06\x00t'\x00|\n\x00|\x01\x00\x83\x02\x00}\x08\x00t)\x00i*\x00\x0co\x10\x00\x01d\x01\x00}\n\x00d\x01\x00}\t\x00n\x01\x00\x01t+\x00|\t\x00|\x06\x00|\n\x00|\x08\x00\x83\x04\x00}\x04\x00|\x04\x00d\x06\x00j\x02\x00o\r\x00\x01t\n\x00|\x00\x00_\x0b\x00n?\x00\x01t\x1c\x00i\x1d\x00d\x07\x00d\x03\x00\x83\x02\x00\x01t-\x00|\x00\x00_\x0b\x00t.\x00i/\x00|\x00\x00i\x05\x00i\x06\x00|\x00\x00i\x05\x00i\x06\x00t0\x00i1\x00d\x01\x00\x83\x04\x00\x01t\x0c\x00i\r\x00|\x00\x00i\x0b\x00|\x00\x00i\t\x00|\x00\x00i\x01\x00i\x06\x00|\x00\x00i\x05\x00i\x06\x00t2\x00|\x06\x00|\t\x00|\x08\x00|\n\x00f\x04\x00\x83\x06\x00\x01d\x00\x00S" (9E 02 00 00 7C 00 00 69 01 00 69 02 00 69 03 00 6F 2C 00 01 7C 00 00 69 01 00 69 02 00 69 04 00 7C 00 00 69 05 00 69 06 00 83 01 00 6F 10 00 01 74 07 00 69 08 00 7C 00 00 69 09 00 83 01 00 6F 33 00 01 74 0A 00 7C 00 00 5F 0B 00 74 0C 00 69 0D 00 7C 00 00 69 0B 00 7C 00 00 69 09 00 7C 00 00 69 01 00 7C 00 00 69 05 00 83 04 00 01 64 00 00 53 6E 01 00 01 64 01 00 7D 0A 00 64 01 00 7D 09 00 7C 00 00 69 01 00 69 10 00 74 11 00 19 7D 0C 00 7C 00 00 69 05 00 69 10 00 74 13 00 19 7D 0D 00 7C 00 00 69 01 00 69 15 00 74 16 00 19 7D 07 00 7C 00 00 69 05 00 69 15 00 74 16 00 19 7D 01 00 7C 0C 00 6F 18 00 01 7C 09 00 7C 00 00 69 01 00 69 15 00 74 11 00 19 37 7D 09 00 6E 01 00 01 7C 0D 00 6F 18 00 01 7C 0A 00 7C 00 00 69 05 00 69 15 00 74 13 00 19 37 7D 0A 00 6E 01 00 01 7C 00 00 69 01 00 69 15 00 74 19 00 19 7D 03 00 7C 00 00 69 05 00 69 15 00 74 19 00 19 7D 0B 00 74 1C 00 69 1D 00 64 02 00 7C 03 00 7C 0B 00 66 02 00 16 64 03 00 83 02 00 01 74 1C 00 69 1D 00 64 04 00 7C 09 00 7C 0A 00 66 02 00 16 64 03 00 83 02 00 01 74 1E 00 69 1F 00 7C 03 00 83 01 00 7D 05 00 74 1E 00 69 21 00 7C 0B 00 83 01 00 7D 02 00 74 23 00 74 24 00 7C 09 00 83 01 00 7C 05 00 14 83 01 00 7D 09 00 74 23 00 74 24 00 7C 0A 00 83 01 00 7C 02 00 14 83 01 00 7D 0A 00 74 1C 00 69 1D 00 64 05 00 7C 09 00 7C 05 00 7C 0A 00 7C 02 00 66 04 00 16 64 03 00 83 02 00 01 74 25 00 7C 09 00 7C 07 00 83 02 00 7D 06 00 74 27 00 7C 0A 00 7C 01 00 83 02 00 7D 08 00 74 29 00 69 2A 00 0C 6F 10 00 01 64 01 00 7D 0A 00 64 01 00 7D 09 00 6E 01 00 01 74 2B 00 7C 09 00 7C 06 00 7C 0A 00 7C 08 00 83 04 00 7D 04 00 7C 04 00 64 06 00 6A 02 00 6F 0D 00 01 74 0A 00 7C 00 00 5F 0B 00 6E 3F 00 01 74 1C 00 69 1D 00 64 07 00 64 03 00 83 02 00 01 74 2D 00 7C 00 00 5F 0B 00 74 2E 00 69 2F 00 7C 00 00 69 05 00 69 06 00 7C 00 00 69 05 00 69 06 00 74 30 00 69 31 00 64 01 00 83 04 00 01 74 0C 00 69 0D 00 7C 00 00 69 0B 00 7C 00 00 69 09 00 7C 00 00 69 01 00 69 06 00 7C 00 00 69 05 00 69 06 00 74 32 00 7C 06 00 7C 09 00 7C 08 00 7C 0A 00 66 04 00 83 06 00 01 64 00 00 53)
                             00000000     7C - LOAD_FAST           'sentence'
                             00000003     69 - LOAD_ATTR           'subject'
                             00000006     69 - LOAD_ATTR           'Interlock'
                             00000009     69 - LOAD_ATTR           'isInCombat'
                             0000000C     6F - JUMP_IF_FALSE       -> 0000003B
                             0000000F     01 - POP_TOP             
                             00000010     7C - LOAD_FAST           'sentence'
                             00000013     69 - LOAD_ATTR           'subject'
                             00000016     69 - LOAD_ATTR           'Interlock'
                             00000019     69 - LOAD_ATTR           'isCombatTarget'
                             0000001C     7C - LOAD_FAST           'sentence'
                             0000001F     69 - LOAD_ATTR           'directObject'
                             00000022     69 - LOAD_ATTR           'locator'
                             00000025     83 - CALL_FUNCTION       r0001
                             00000028     6F - JUMP_IF_FALSE       -> 0000003B
                             0000002B     01 - POP_TOP             
                             0000002C     74 - LOAD_GLOBAL         'abilitylib'
                             0000002F     69 - LOAD_ATTR           'createsAnExchange'
                             00000032     7C - LOAD_FAST           'sentence'
                             00000035     69 - LOAD_ATTR           'verbID'
                             00000038     83 - CALL_FUNCTION       r0001
                             0000003B     6F - JUMP_IF_FALSE       -> 00000071
                             0000003E     01 - POP_TOP             
                             0000003F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000042     7C - LOAD_FAST           'sentence'
                             00000045     5F - STORE_ATTR          'result'
                             00000048     74 - LOAD_GLOBAL         'VIRII'
                             0000004B     69 - LOAD_ATTR           'SendVirusResultToAll'
                             0000004E     7C - LOAD_FAST           'sentence'
                             00000051     69 - LOAD_ATTR           'result'
                             00000054     7C - LOAD_FAST           'sentence'
                             00000057     69 - LOAD_ATTR           'verbID'
                             0000005A     7C - LOAD_FAST           'sentence'
                             0000005D     69 - LOAD_ATTR           'subject'
                             00000060     7C - LOAD_FAST           'sentence'
                             00000063     69 - LOAD_ATTR           'directObject'
                             00000066     83 - CALL_FUNCTION       r0004
                             00000069     01 - POP_TOP             
                             0000006A     64 - LOAD_CONST          None
                             0000006D     53 - RETURN_VALUE        
                             0000006E     6E - JUMP_FORWARD        -> 00000072
                             00000071     01 - POP_TOP             
                             00000072     64 - LOAD_CONST          0
                             00000075     7D - STORE_FAST          'defBonusTotal'
                             00000078     64 - LOAD_CONST          0
                             0000007B     7D - STORE_FAST          'atrBonusTotal'
                             0000007E     7C - LOAD_FAST           'sentence'
                             00000081     69 - LOAD_ATTR           'subject'
                             00000084     69 - LOAD_ATTR           'hasAbility'
                             00000087     74 - LOAD_GLOBAL         'ViralTransmissionAbility'
                             0000008A     19 - BINARY_SUBSCR       
                             0000008B     7D - STORE_FAST          'atrHasTransmitBonus'
                             0000008E     7C - LOAD_FAST           'sentence'
                             00000091     69 - LOAD_ATTR           'directObject'
                             00000094     69 - LOAD_ATTR           'hasAbility'
                             00000097     74 - LOAD_GLOBAL         'ViralDeflectionAbility'
                             0000009A     19 - BINARY_SUBSCR       
                             0000009B     7D - STORE_FAST          'defHasViralDeflectionBonus'
                             0000009E     7C - LOAD_FAST           'sentence'
                             000000A1     69 - LOAD_ATTR           'subject'
                             000000A4     69 - LOAD_ATTR           'abilities'
                             000000A7     74 - LOAD_GLOBAL         'ConsistencyAbility'
                             000000AA     19 - BINARY_SUBSCR       
                             000000AB     7D - STORE_FAST          'atrConsistancy'
                             000000AE     7C - LOAD_FAST           'sentence'
                             000000B1     69 - LOAD_ATTR           'directObject'
                             000000B4     69 - LOAD_ATTR           'abilities'
                             000000B7     74 - LOAD_GLOBAL         'ConsistencyAbility'
                             000000BA     19 - BINARY_SUBSCR       
                             000000BB     7D - STORE_FAST          'defConsistancy'
                             000000BE     7C - LOAD_FAST           'atrHasTransmitBonus'
                             000000C1     6F - JUMP_IF_FALSE       -> 000000DC
                             000000C4     01 - POP_TOP             
                             000000C5     7C - LOAD_FAST           'atrBonusTotal'
                             000000C8     7C - LOAD_FAST           'sentence'
                             000000CB     69 - LOAD_ATTR           'subject'
                             000000CE     69 - LOAD_ATTR           'abilities'
                             000000D1     74 - LOAD_GLOBAL         'ViralTransmissionAbility'
                             000000D4     19 - BINARY_SUBSCR       
                             000000D5     37 - INPLACE_ADD         
                             000000D6     7D - STORE_FAST          'atrBonusTotal'
                             000000D9     6E - JUMP_FORWARD        -> 000000DD
                             000000DC     01 - POP_TOP             
                             000000DD     7C - LOAD_FAST           'defHasViralDeflectionBonus'
                             000000E0     6F - JUMP_IF_FALSE       -> 000000FB
                             000000E3     01 - POP_TOP             
                             000000E4     7C - LOAD_FAST           'defBonusTotal'
                             000000E7     7C - LOAD_FAST           'sentence'
                             000000EA     69 - LOAD_ATTR           'directObject'
                             000000ED     69 - LOAD_ATTR           'abilities'
                             000000F0     74 - LOAD_GLOBAL         'ViralDeflectionAbility'
                             000000F3     19 - BINARY_SUBSCR       
                             000000F4     37 - INPLACE_ADD         
                             000000F5     7D - STORE_FAST          'defBonusTotal'
                             000000F8     6E - JUMP_FORWARD        -> 000000FC
                             000000FB     01 - POP_TOP             
                             000000FC     7C - LOAD_FAST           'sentence'
                             000000FF     69 - LOAD_ATTR           'subject'
                             00000102     69 - LOAD_ATTR           'abilities'
                             00000105     74 - LOAD_GLOBAL         'CurrentTacticAbility'
                             00000108     19 - BINARY_SUBSCR       
                             00000109     7D - STORE_FAST          'atrTactic'
                             0000010C     7C - LOAD_FAST           'sentence'
                             0000010F     69 - LOAD_ATTR           'directObject'
                             00000112     69 - LOAD_ATTR           'abilities'
                             00000115     74 - LOAD_GLOBAL         'CurrentTacticAbility'
                             00000118     19 - BINARY_SUBSCR       
                             00000119     7D - STORE_FAST          'defTactic'
                             0000011C     74 - LOAD_GLOBAL         'CU'
                             0000011F     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000122     64 - LOAD_CONST          'Viral Tactic A(%d) D(%d)'
                             00000125     7C - LOAD_FAST           'atrTactic'
                             00000128     7C - LOAD_FAST           'defTactic'
                             0000012B     66 - BUILD_TUPLE         r0002
                             0000012E     16 - BINARY_MODULO       
                             0000012F     64 - LOAD_CONST          2
                             00000132     83 - CALL_FUNCTION       r0002
                             00000135     01 - POP_TOP             
                             00000136     74 - LOAD_GLOBAL         'CU'
                             00000139     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000013C     64 - LOAD_CONST          'Viral Tactic before: %dvs%d'
                             0000013F     7C - LOAD_FAST           'atrBonusTotal'
                             00000142     7C - LOAD_FAST           'defBonusTotal'
                             00000145     66 - BUILD_TUPLE         r0002
                             00000148     16 - BINARY_MODULO       
                             00000149     64 - LOAD_CONST          2
                             0000014C     83 - CALL_FUNCTION       r0002
                             0000014F     01 - POP_TOP             
                             00000150     74 - LOAD_GLOBAL         'CC'
                             00000153     69 - LOAD_ATTR           'GetTacticCombatTacticsMod'
                             00000156     7C - LOAD_FAST           'atrTactic'
                             00000159     83 - CALL_FUNCTION       r0001
                             0000015C     7D - STORE_FAST          'atrTacticBonus'
                             0000015F     74 - LOAD_GLOBAL         'CC'
                             00000162     69 - LOAD_ATTR           'GetTacticDefenseTacticsMod'
                             00000165     7C - LOAD_FAST           'defTactic'
                             00000168     83 - CALL_FUNCTION       r0001
                             0000016B     7D - STORE_FAST          'defTacticBonus'
                             0000016E     74 - LOAD_GLOBAL         'int'
                             00000171     74 - LOAD_GLOBAL         'float'
                             00000174     7C - LOAD_FAST           'atrBonusTotal'
                             00000177     83 - CALL_FUNCTION       r0001
                             0000017A     7C - LOAD_FAST           'atrTacticBonus'
                             0000017D     14 - BINARY_MULTIPLY     
                             0000017E     83 - CALL_FUNCTION       r0001
                             00000181     7D - STORE_FAST          'atrBonusTotal'
                             00000184     74 - LOAD_GLOBAL         'int'
                             00000187     74 - LOAD_GLOBAL         'float'
                             0000018A     7C - LOAD_FAST           'defBonusTotal'
                             0000018D     83 - CALL_FUNCTION       r0001
                             00000190     7C - LOAD_FAST           'defTacticBonus'
                             00000193     14 - BINARY_MULTIPLY     
                             00000194     83 - CALL_FUNCTION       r0001
                             00000197     7D - STORE_FAST          'defBonusTotal'
                             0000019A     74 - LOAD_GLOBAL         'CU'
                             0000019D     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000001A0     64 - LOAD_CONST          'Viral Tactic after: %d(%gmod)vs%d(w%gmod)'
                             000001A3     7C - LOAD_FAST           'atrBonusTotal'
                             000001A6     7C - LOAD_FAST           'atrTacticBonus'
                             000001A9     7C - LOAD_FAST           'defBonusTotal'
                             000001AC     7C - LOAD_FAST           'defTacticBonus'
                             000001AF     66 - BUILD_TUPLE         r0004
                             000001B2     16 - BINARY_MODULO       
                             000001B3     64 - LOAD_CONST          2
                             000001B6     83 - CALL_FUNCTION       r0002
                             000001B9     01 - POP_TOP             
                             000001BA     74 - LOAD_GLOBAL         'ComputeAttackerTotal'
                             000001BD     7C - LOAD_FAST           'atrBonusTotal'
                             000001C0     7C - LOAD_FAST           'atrConsistancy'
                             000001C3     83 - CALL_FUNCTION       r0002
                             000001C6     7D - STORE_FAST          'attackerTotal'
                             000001C9     74 - LOAD_GLOBAL         'ComputeDefenderTotal'
                             000001CC     7C - LOAD_FAST           'defBonusTotal'
                             000001CF     7C - LOAD_FAST           'defConsistancy'
                             000001D2     83 - CALL_FUNCTION       r0002
                             000001D5     7D - STORE_FAST          'defenderTotal'
                             000001D8     74 - LOAD_GLOBAL         'consolevar'
                             000001DB     69 - LOAD_ATTR           'OldTacticRolls'
                             000001DE     0C - UNARY_NOT           
                             000001DF     6F - JUMP_IF_FALSE       -> 000001F2
                             000001E2     01 - POP_TOP             
                             000001E3     64 - LOAD_CONST          0
                             000001E6     7D - STORE_FAST          'defBonusTotal'
                             000001E9     64 - LOAD_CONST          0
                             000001EC     7D - STORE_FAST          'atrBonusTotal'
                             000001EF     6E - JUMP_FORWARD        -> 000001F3
                             000001F2     01 - POP_TOP             
                             000001F3     74 - LOAD_GLOBAL         'GenericFreeAttackTest'
                             000001F6     7C - LOAD_FAST           'atrBonusTotal'
                             000001F9     7C - LOAD_FAST           'attackerTotal'
                             000001FC     7C - LOAD_FAST           'defBonusTotal'
                             000001FF     7C - LOAD_FAST           'defenderTotal'
                             00000202     83 - CALL_FUNCTION       r0004
                             00000205     7D - STORE_FAST          'atrWon'
                             00000208     7C - LOAD_FAST           'atrWon'
                             0000020B     64 - LOAD_CONST          1
                             0000020E     6A - COMPARE_OP          "=="
                             00000211     6F - JUMP_IF_FALSE       -> 00000221
                             00000214     01 - POP_TOP             
                             00000215     74 - LOAD_GLOBAL         'SUCCESS'
                             00000218     7C - LOAD_FAST           'sentence'
                             0000021B     5F - STORE_ATTR          'result'
                             0000021E     6E - JUMP_FORWARD        -> 00000260
                             00000221     01 - POP_TOP             
                             00000222     74 - LOAD_GLOBAL         'CU'
                             00000225     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000228     64 - LOAD_CONST          'AbilityViralFreeAttack: FAILED'
                             0000022B     64 - LOAD_CONST          2
                             0000022E     83 - CALL_FUNCTION       r0002
                             00000231     01 - POP_TOP             
                             00000232     74 - LOAD_GLOBAL         'DEFLECTED'
                             00000235     7C - LOAD_FAST           'sentence'
                             00000238     5F - STORE_ATTR          'result'
                             0000023B     74 - LOAD_GLOBAL         'discovery'
                             0000023E     69 - LOAD_ATTR           'playEffect'
                             00000241     7C - LOAD_FAST           'sentence'
                             00000244     69 - LOAD_ATTR           'directObject'
                             00000247     69 - LOAD_ATTR           'locator'
                             0000024A     7C - LOAD_FAST           'sentence'
                             0000024D     69 - LOAD_ATTR           'directObject'
                             00000250     69 - LOAD_ATTR           'locator'
                             00000253     74 - LOAD_GLOBAL         'FX'
                             00000256     69 - LOAD_ATTR           'FX_CHARACTER_DEFLECTION'
                             00000259     64 - LOAD_CONST          0
                             0000025C     83 - CALL_FUNCTION       r0004
                             0000025F     01 - POP_TOP             
                             00000260     74 - LOAD_GLOBAL         'VIRII'
                             00000263     69 - LOAD_ATTR           'SendVirusResultToAll'
                             00000266     7C - LOAD_FAST           'sentence'
                             00000269     69 - LOAD_ATTR           'result'
                             0000026C     7C - LOAD_FAST           'sentence'
                             0000026F     69 - LOAD_ATTR           'verbID'
                             00000272     7C - LOAD_FAST           'sentence'
                             00000275     69 - LOAD_ATTR           'subject'
                             00000278     69 - LOAD_ATTR           'locator'
                             0000027B     7C - LOAD_FAST           'sentence'
                             0000027E     69 - LOAD_ATTR           'directObject'
                             00000281     69 - LOAD_ATTR           'locator'
                             00000284     74 - LOAD_GLOBAL         'True'
                             00000287     7C - LOAD_FAST           'attackerTotal'
                             0000028A     7C - LOAD_FAST           'atrBonusTotal'
                             0000028D     7C - LOAD_FAST           'defenderTotal'
                             00000290     7C - LOAD_FAST           'defBonusTotal'
                             00000293     66 - BUILD_TUPLE         r0004
                             00000296     83 - CALL_FUNCTION       r0006
                             00000299     01 - POP_TOP             
                             0000029A     64 - LOAD_CONST          None
                             0000029D     53 - RETURN_VALUE        
                         consts:
00002547                     TUPLE: (
0000254C                         None (4E),
0000254D                         INT: 0 (00 00 00 00),
00002552                         STR: 'Viral Tactic A(%d) D(%d)' (18 00 00 00 56 69 72 61 6C 20 54 61 63 74 69 63 20 41 28 25 64 29 20 44 28 25 64 29),
0000256F                         INT: 2 (02 00 00 00),
00002574                         STR: 'Viral Tactic before: %dvs%d' (1B 00 00 00 56 69 72 61 6C 20 54 61 63 74 69 63 20 62 65 66 6F 72 65 3A 20 25 64 76 73 25 64),
00002594                         STR: 'Viral Tactic after: %d(%gmod)vs%d(w%gmod)' (29 00 00 00 56 69 72 61 6C 20 54 61 63 74 69 63 20 61 66 74 65 72 3A 20 25 64 28 25 67 6D 6F 64 29 76 73 25 64 28 77 25 67 6D 6F 64 29),
000025C2                         INT: 1 (01 00 00 00),
000025C7                         STR: 'AbilityViralFreeAttack: FAILED' (1E 00 00 00 41 62 69 6C 69 74 79 56 69 72 61 6C 46 72 65 65 41 74 74 61 63 6B 3A 20 46 41 49 4C 45 44)
                             )
                         names:
000025EA                     TUPLE: (
000025EF                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65),
000025FC                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00002608                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00002616                         STR: 'isInCombat' (0A 00 00 00 69 73 49 6E 43 6F 6D 62 61 74),
00002625                         STR: 'isCombatTarget' (0E 00 00 00 69 73 43 6F 6D 62 61 74 54 61 72 67 65 74),
00002638                         STR: 'directObject' (0C 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74),
00002649                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
00002655                         STR: 'abilitylib' (0A 00 00 00 61 62 69 6C 69 74 79 6C 69 62),
00002664                         STR: 'createsAnExchange' (11 00 00 00 63 72 65 61 74 65 73 41 6E 45 78 63 68 61 6E 67 65),
0000267A                         STR: 'verbID' (06 00 00 00 76 65 72 62 49 44),
00002685                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00002691                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
0000269C                         STR: 'VIRII' (05 00 00 00 56 49 52 49 49),
000026A6                         STR: 'SendVirusResultToAll' (14 00 00 00 53 65 6E 64 56 69 72 75 73 52 65 73 75 6C 74 54 6F 41 6C 6C),
000026BF                         STR: 'defBonusTotal' (0D 00 00 00 64 65 66 42 6F 6E 75 73 54 6F 74 61 6C),
000026D1                         STR: 'atrBonusTotal' (0D 00 00 00 61 74 72 42 6F 6E 75 73 54 6F 74 61 6C),
000026E3                         STR: 'hasAbility' (0A 00 00 00 68 61 73 41 62 69 6C 69 74 79),
000026F2                         STR: 'ViralTransmissionAbility' (18 00 00 00 56 69 72 61 6C 54 72 61 6E 73 6D 69 73 73 69 6F 6E 41 62 69 6C 69 74 79),
0000270F                         STR: 'atrHasTransmitBonus' (13 00 00 00 61 74 72 48 61 73 54 72 61 6E 73 6D 69 74 42 6F 6E 75 73),
00002727                         STR: 'ViralDeflectionAbility' (16 00 00 00 56 69 72 61 6C 44 65 66 6C 65 63 74 69 6F 6E 41 62 69 6C 69 74 79),
00002742                         STR: 'defHasViralDeflectionBonus' (1A 00 00 00 64 65 66 48 61 73 56 69 72 61 6C 44 65 66 6C 65 63 74 69 6F 6E 42 6F 6E 75 73),
00002761                         STR: 'abilities' (09 00 00 00 61 62 69 6C 69 74 69 65 73),
0000276F                         STR: 'ConsistencyAbility' (12 00 00 00 43 6F 6E 73 69 73 74 65 6E 63 79 41 62 69 6C 69 74 79),
00002786                         STR: 'atrConsistancy' (0E 00 00 00 61 74 72 43 6F 6E 73 69 73 74 61 6E 63 79),
00002799                         STR: 'defConsistancy' (0E 00 00 00 64 65 66 43 6F 6E 73 69 73 74 61 6E 63 79),
000027AC                         STR: 'CurrentTacticAbility' (14 00 00 00 43 75 72 72 65 6E 74 54 61 63 74 69 63 41 62 69 6C 69 74 79),
000027C5                         STR: 'atrTactic' (09 00 00 00 61 74 72 54 61 63 74 69 63),
000027D3                         STR: 'defTactic' (09 00 00 00 64 65 66 54 61 63 74 69 63),
000027E1                         STR: 'CU' (02 00 00 00 43 55),
000027E8                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
00002805                         STR: 'CC' (02 00 00 00 43 43),
0000280C                         STR: 'GetTacticCombatTacticsMod' (19 00 00 00 47 65 74 54 61 63 74 69 63 43 6F 6D 62 61 74 54 61 63 74 69 63 73 4D 6F 64),
0000282A                         STR: 'atrTacticBonus' (0E 00 00 00 61 74 72 54 61 63 74 69 63 42 6F 6E 75 73),
0000283D                         STR: 'GetTacticDefenseTacticsMod' (1A 00 00 00 47 65 74 54 61 63 74 69 63 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 4D 6F 64),
0000285C                         STR: 'defTacticBonus' (0E 00 00 00 64 65 66 54 61 63 74 69 63 42 6F 6E 75 73),
0000286F                         STR: 'int' (03 00 00 00 69 6E 74),
00002877                         STR: 'float' (05 00 00 00 66 6C 6F 61 74),
00002881                         STR: 'ComputeAttackerTotal' (14 00 00 00 43 6F 6D 70 75 74 65 41 74 74 61 63 6B 65 72 54 6F 74 61 6C),
0000289A                         STR: 'attackerTotal' (0D 00 00 00 61 74 74 61 63 6B 65 72 54 6F 74 61 6C),
000028AC                         STR: 'ComputeDefenderTotal' (14 00 00 00 43 6F 6D 70 75 74 65 44 65 66 65 6E 64 65 72 54 6F 74 61 6C),
000028C5                         STR: 'defenderTotal' (0D 00 00 00 64 65 66 65 6E 64 65 72 54 6F 74 61 6C),
000028D7                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
000028E6                         STR: 'OldTacticRolls' (0E 00 00 00 4F 6C 64 54 61 63 74 69 63 52 6F 6C 6C 73),
000028F9                         STR: 'GenericFreeAttackTest' (15 00 00 00 47 65 6E 65 72 69 63 46 72 65 65 41 74 74 61 63 6B 54 65 73 74),
00002913                         STR: 'atrWon' (06 00 00 00 61 74 72 57 6F 6E),
0000291E                         STR: 'DEFLECTED' (09 00 00 00 44 45 46 4C 45 43 54 45 44),
0000292C                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
0000293A                         STR: 'playEffect' (0A 00 00 00 70 6C 61 79 45 66 66 65 63 74),
00002949                         STR: 'FX' (02 00 00 00 46 58),
00002950                         STR: 'FX_CHARACTER_DEFLECTION' (17 00 00 00 46 58 5F 43 48 41 52 41 43 54 45 52 5F 44 45 46 4C 45 43 54 49 4F 4E),
0000296C                         STR: 'True' (04 00 00 00 54 72 75 65)
                             )
                         varnames:
00002975                     TUPLE: (
0000297A                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65),
00002987                         STR: 'defConsistancy' (0E 00 00 00 64 65 66 43 6F 6E 73 69 73 74 61 6E 63 79),
0000299A                         STR: 'defTacticBonus' (0E 00 00 00 64 65 66 54 61 63 74 69 63 42 6F 6E 75 73),
000029AD                         STR: 'atrTactic' (09 00 00 00 61 74 72 54 61 63 74 69 63),
000029BB                         STR: 'atrWon' (06 00 00 00 61 74 72 57 6F 6E),
000029C6                         STR: 'atrTacticBonus' (0E 00 00 00 61 74 72 54 61 63 74 69 63 42 6F 6E 75 73),
000029D9                         STR: 'attackerTotal' (0D 00 00 00 61 74 74 61 63 6B 65 72 54 6F 74 61 6C),
000029EB                         STR: 'atrConsistancy' (0E 00 00 00 61 74 72 43 6F 6E 73 69 73 74 61 6E 63 79),
000029FE                         STR: 'defenderTotal' (0D 00 00 00 64 65 66 65 6E 64 65 72 54 6F 74 61 6C),
00002A10                         STR: 'atrBonusTotal' (0D 00 00 00 61 74 72 42 6F 6E 75 73 54 6F 74 61 6C),
00002A22                         STR: 'defBonusTotal' (0D 00 00 00 64 65 66 42 6F 6E 75 73 54 6F 74 61 6C),
00002A34                         STR: 'defTactic' (09 00 00 00 64 65 66 54 61 63 74 69 63),
00002A42                         STR: 'atrHasTransmitBonus' (13 00 00 00 61 74 72 48 61 73 54 72 61 6E 73 6D 69 74 42 6F 6E 75 73),
00002A5A                         STR: 'defHasViralDeflectionBonus' (1A 00 00 00 64 65 66 48 61 73 56 69 72 61 6C 44 65 66 6C 65 63 74 69 6F 6E 42 6F 6E 75 73)
                             )
                         freevars:
00002A79                     TUPLE: ()
                         cellvars:
00002A7E                     TUPLE: ()
                         filename:
00002A83                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\generic_free_attacks.py' (4C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 67 65 6E 65 72 69 63 5F 66 72 65 65 5F 61 74 74 61 63 6B 73 2E 70 79)
                         name:
00002AD4                     STR: 'AbilityViralFreeAttack' (16 00 00 00 41 62 69 6C 69 74 79 56 69 72 61 6C 46 72 65 65 41 74 74 61 63 6B)
                         firslineno:
00002AEF                     LONG: 241L (F1 00 00 00)
                         lnotab:
00002AF3                     STR: '\x00\x05?\x01\t\x01"\x01\x08\x02\x06\x01\x06\x02\x10\x01\x10\x03\x10\x01\x10\x03\x07\x01\x18\x03\x07\x01\x18\x03\x10\x01\x10\x01\x1a\x01\x1a\x01\x0f\x01\x0f\x01\x16\x01\x16\x01 \x03\x0f\x01\x0f\x02\x0b\x01\x06\x01\n\x03\x15\x02\r\x01\r\x02\x10\x01\t\x02%\x03' (46 00 00 00 00 05 3F 01 09 01 22 01 08 02 06 01 06 02 10 01 10 03 10 01 10 03 07 01 18 03 07 01 18 03 10 01 10 01 1A 01 1A 01 0F 01 0F 01 16 01 16 01 20 03 0F 01 0F 02 0B 01 06 01 0A 03 15 02 0D 01 0D 02 10 01 09 02 25 03),
00002B3E             STR: '\ndirectObject.hasAbility[CurrentTacticAbility]\ndirectObject.hasAbility[ViralDeflectionAbility]\ndirectObject.abilities[ViralDeflectionAbility]\ndirectObject.abilities[ConsistencyAbility]\ndirectObject.abilities[CurrentTacticAbility]\ndirectObject.locator\n' (FB 00 00 00 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 68 61 73 41 62 69 6C 69 74 79 5B 43 75 72 72 65 6E 74 54 61 63 74 69 63 41 62 69 6C 69 74 79 5D 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 68 61 73 41 62 69 6C 69 74 79 5B 56 69 72 61 6C 44 65 66 6C 65 63 74 69 6F 6E 41 62 69 6C 69 74 79 5D 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 61 62 69 6C 69 74 69 65 73 5B 56 69 72 61 6C 44 65 66 6C 65 63 74 69 6F 6E 41 62 69 6C 69 74 79 5D 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 61 62 69 6C 69 74 69 65 73 5B 43 6F 6E 73 69 73 74 65 6E 63 79 41 62 69 6C 69 74 79 5D 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 61 62 69 6C 69 74 69 65 73 5B 43 75 72 72 65 6E 74 54 61 63 74 69 63 41 62 69 6C 69 74 79 5D 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 6C 6F 63 61 74 6F 72 0A),
00002C3E             CODE:
                         argcount:
00002C3F                     LONG: 1L (01 00 00 00)
                         nlocals:
00002C43                     LONG: 1L (01 00 00 00)
                         stacksize:
00002C47                     LONG: 9L (09 00 00 00)
                         flags:
00002C4B                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00002C4F                     STR: '|\x00\x00i\x01\x00i\x02\x00i\x03\x00t\x04\x00i\x05\x00i\x06\x00@oD\x00\x01t\x07\x00|\x00\x00_\x08\x00t\t\x00i\n\x00t\x0b\x00i\x0c\x00|\x00\x00i\r\x00|\x00\x00i\x01\x00i\x0e\x00|\x00\x00i\x0f\x00i\x0e\x00d\x01\x00d\x01\x00d\x01\x00d\x01\x00f\x04\x00\x83\x05\x00\x01n\n\x00\x01t\x10\x00|\x00\x00_\x08\x00d\x00\x00S' (6B 00 00 00 7C 00 00 69 01 00 69 02 00 69 03 00 74 04 00 69 05 00 69 06 00 40 6F 44 00 01 74 07 00 7C 00 00 5F 08 00 74 09 00 69 0A 00 74 0B 00 69 0C 00 7C 00 00 69 0D 00 7C 00 00 69 01 00 69 0E 00 7C 00 00 69 0F 00 69 0E 00 64 01 00 64 01 00 64 01 00 64 01 00 66 04 00 83 05 00 01 6E 0A 00 01 74 10 00 7C 00 00 5F 08 00 64 00 00 53)
                             00000000     7C - LOAD_FAST           'sentence'
                             00000003     69 - LOAD_ATTR           'subject'
                             00000006     69 - LOAD_ATTR           'AbilityInv'
                             00000009     69 - LOAD_ATTR           'ConditionStateFlags'
                             0000000C     74 - LOAD_GLOBAL         'constants'
                             0000000F     69 - LOAD_ATTR           'combat'
                             00000012     69 - LOAD_ATTR           'ST_COMBAT_EFFECT'
                             00000015     40 - BINARY_AND          
                             00000016     6F - JUMP_IF_FALSE       -> 0000005D
                             00000019     01 - POP_TOP             
                             0000001A     74 - LOAD_GLOBAL         'DEFLECTED'
                             0000001D     7C - LOAD_FAST           'sentence'
                             00000020     5F - STORE_ATTR          'result'
                             00000023     74 - LOAD_GLOBAL         'Utility'
                             00000026     69 - LOAD_ATTR           'SendAbilityOutputToCaster'
                             00000029     74 - LOAD_GLOBAL         'StringTable'
                             0000002C     69 - LOAD_ATTR           'ID_ABILITY_NONCOMBAT_ABILITY'
                             0000002F     7C - LOAD_FAST           'sentence'
                             00000032     69 - LOAD_ATTR           'verbID'
                             00000035     7C - LOAD_FAST           'sentence'
                             00000038     69 - LOAD_ATTR           'subject'
                             0000003B     69 - LOAD_ATTR           'locator'
                             0000003E     7C - LOAD_FAST           'sentence'
                             00000041     69 - LOAD_ATTR           'directObject'
                             00000044     69 - LOAD_ATTR           'locator'
                             00000047     64 - LOAD_CONST          0
                             0000004A     64 - LOAD_CONST          0
                             0000004D     64 - LOAD_CONST          0
                             00000050     64 - LOAD_CONST          0
                             00000053     66 - BUILD_TUPLE         r0004
                             00000056     83 - CALL_FUNCTION       r0005
                             00000059     01 - POP_TOP             
                             0000005A     6E - JUMP_FORWARD        -> 00000067
                             0000005D     01 - POP_TOP             
                             0000005E     74 - LOAD_GLOBAL         'SUCCESS'
                             00000061     7C - LOAD_FAST           'sentence'
                             00000064     5F - STORE_ATTR          'result'
                             00000067     64 - LOAD_CONST          None
                             0000006A     53 - RETURN_VALUE        
                         consts:
00002CBF                     TUPLE: (
00002CC4                         None (4E),
00002CC5                         INT: 0 (00 00 00 00)
                             )
                         names:
00002CCA                     TUPLE: (
00002CCF                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65),
00002CDC                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00002CE8                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
00002CF7                         STR: 'ConditionStateFlags' (13 00 00 00 43 6F 6E 64 69 74 69 6F 6E 53 74 61 74 65 46 6C 61 67 73),
00002D0F                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00002D1D                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
00002D28                         STR: 'ST_COMBAT_EFFECT' (10 00 00 00 53 54 5F 43 4F 4D 42 41 54 5F 45 46 46 45 43 54),
00002D3D                         STR: 'DEFLECTED' (09 00 00 00 44 45 46 4C 45 43 54 45 44),
00002D4B                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00002D56                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00002D62                         STR: 'SendAbilityOutputToCaster' (19 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 43 61 73 74 65 72),
00002D80                         STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00002D90                         STR: 'ID_ABILITY_NONCOMBAT_ABILITY' (1C 00 00 00 49 44 5F 41 42 49 4C 49 54 59 5F 4E 4F 4E 43 4F 4D 42 41 54 5F 41 42 49 4C 49 54 59),
00002DB1                         STR: 'verbID' (06 00 00 00 76 65 72 62 49 44),
00002DBC                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
00002DC8                         STR: 'directObject' (0C 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74),
00002DD9                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53)
                             )
                         varnames:
00002DE5                     TUPLE: (
00002DEA                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65)
                             )
                         freevars:
00002DF7                     TUPLE: ()
                         cellvars:
00002DFC                     TUPLE: ()
                         filename:
00002E01                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\generic_free_attacks.py' (4C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 67 65 6E 65 72 69 63 5F 66 72 65 65 5F 61 74 74 61 63 6B 73 2E 70 79)
                         name:
00002E52                     STR: 'AbilityOutOfCombat' (12 00 00 00 41 62 69 6C 69 74 79 4F 75 74 4F 66 43 6F 6D 62 61 74)
                         firslineno:
00002E69                     LONG: 317L (3D 01 00 00)
                         lnotab:
00002E6D                     STR: '\x00\x02\x1a\x01\t\x01;\x02' (08 00 00 00 00 02 1A 01 09 01 3B 02),
00002E7A             STR: '\ndirectObject.locator\n' (16 00 00 00 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 6C 6F 63 61 74 6F 72 0A)
                 )
             names:
00002E95         TUPLE: (
00002E9A             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00002EA5             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00002EB3             STR: 'interlock.combat_utility' (18 00 00 00 69 6E 74 65 72 6C 6F 63 6B 2E 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79),
00002ED0             STR: 'combat_utility' (0E 00 00 00 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79),
00002EE3             STR: 'CU' (02 00 00 00 43 55),
00002EEA             STR: 'ability.hacker.virii_defines' (1C 00 00 00 61 62 69 6C 69 74 79 2E 68 61 63 6B 65 72 2E 76 69 72 69 69 5F 64 65 66 69 6E 65 73),
00002F0B             STR: 'hacker' (06 00 00 00 68 61 63 6B 65 72),
00002F16             STR: 'virii_defines' (0D 00 00 00 76 69 72 69 69 5F 64 65 66 69 6E 65 73),
00002F28             STR: 'VIRII' (05 00 00 00 56 49 52 49 49),
00002F32             STR: 'ability.utility' (0F 00 00 00 61 62 69 6C 69 74 79 2E 75 74 69 6C 69 74 79),
00002F46             STR: 'utility' (07 00 00 00 75 74 69 6C 69 74 79),
00002F52             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00002F5E             STR: 'stringtable_client' (12 00 00 00 73 74 72 69 6E 67 74 61 62 6C 65 5F 63 6C 69 65 6E 74),
00002F75             STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00002F85             STR: 'ltfxmap' (07 00 00 00 6C 74 66 78 6D 61 70),
00002F91             STR: 'FX' (02 00 00 00 46 58),
00002F98             STR: 'combat_calculations' (13 00 00 00 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73),
00002FB0             STR: 'CC' (02 00 00 00 43 43),
00002FB7             STR: 'GenericFreeAttackTest' (15 00 00 00 47 65 6E 65 72 69 63 46 72 65 65 41 74 74 61 63 6B 54 65 73 74),
00002FD1             STR: 'ComputeAttackerTotal' (14 00 00 00 43 6F 6D 70 75 74 65 41 74 74 61 63 6B 65 72 54 6F 74 61 6C),
00002FEA             STR: 'ComputeDefenderTotal' (14 00 00 00 43 6F 6D 70 75 74 65 44 65 66 65 6E 64 65 72 54 6F 74 61 6C),
00003003             STR: 'AbilityThrowFreeAttack' (16 00 00 00 41 62 69 6C 69 74 79 54 68 72 6F 77 46 72 65 65 41 74 74 61 63 6B),
0000301E             STR: 'depAttr' (07 00 00 00 64 65 70 41 74 74 72),
0000302A             STR: 'AbilityMeleeFreeAttack' (16 00 00 00 41 62 69 6C 69 74 79 4D 65 6C 65 65 46 72 65 65 41 74 74 61 63 6B),
00003045             STR: 'AbilityRangeFreeAttack' (16 00 00 00 41 62 69 6C 69 74 79 52 61 6E 67 65 46 72 65 65 41 74 74 61 63 6B),
00003060             STR: 'AbilityViralFreeAttack' (16 00 00 00 41 62 69 6C 69 74 79 56 69 72 61 6C 46 72 65 65 41 74 74 61 63 6B),
0000307B             STR: 'AbilityOutOfCombat' (12 00 00 00 41 62 69 6C 69 74 79 4F 75 74 4F 66 43 6F 6D 62 61 74)
                 )
             varnames:
00003092         TUPLE: (
00003097             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
000030A5             STR: 'AbilityViralFreeAttack' (16 00 00 00 41 62 69 6C 69 74 79 56 69 72 61 6C 46 72 65 65 41 74 74 61 63 6B),
000030C0             STR: 'AbilityThrowFreeAttack' (16 00 00 00 41 62 69 6C 69 74 79 54 68 72 6F 77 46 72 65 65 41 74 74 61 63 6B),
000030DB             STR: 'AbilityOutOfCombat' (12 00 00 00 41 62 69 6C 69 74 79 4F 75 74 4F 66 43 6F 6D 62 61 74),
000030F2             STR: 'FX' (02 00 00 00 46 58),
000030F9             STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00003109             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00003114             STR: 'ComputeDefenderTotal' (14 00 00 00 43 6F 6D 70 75 74 65 44 65 66 65 6E 64 65 72 54 6F 74 61 6C),
0000312D             STR: 'AbilityMeleeFreeAttack' (16 00 00 00 41 62 69 6C 69 74 79 4D 65 6C 65 65 46 72 65 65 41 74 74 61 63 6B),
00003148             STR: 'GenericFreeAttackTest' (15 00 00 00 47 65 6E 65 72 69 63 46 72 65 65 41 74 74 61 63 6B 54 65 73 74),
00003162             STR: 'CC' (02 00 00 00 43 43),
00003169             STR: 'ComputeAttackerTotal' (14 00 00 00 43 6F 6D 70 75 74 65 41 74 74 61 63 6B 65 72 54 6F 74 61 6C),
00003182             STR: 'VIRII' (05 00 00 00 56 49 52 49 49),
0000318C             STR: 'AbilityRangeFreeAttack' (16 00 00 00 41 62 69 6C 69 74 79 52 61 6E 67 65 46 72 65 65 41 74 74 61 63 6B),
000031A7             STR: 'CU' (02 00 00 00 43 55),
000031AE             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79)
                 )
             freevars:
000031BA         TUPLE: ()
             cellvars:
000031BF         TUPLE: ()
             filename:
000031C4         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\generic_free_attacks.py' (4C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 67 65 6E 65 72 69 63 5F 66 72 65 65 5F 61 74 74 61 63 6B 73 2E 70 79)
             name:
00003215         STR: '?' (01 00 00 00 3F)
             firslineno:
0000321B         LONG: 1L (01 00 00 00)
             lnotab:
0000321F         STR: '\t\x01\t\x01\x0c\x01\x0f\x01\x0c\x01\t\x01\t\x01\t\x02\t\x08\t\n\t\x0f\t4\t\x0e\t3\t\x0f\t4\t\x0e\t>\t\x0e\t\x08' (28 00 00 00 09 01 09 01 0C 01 0F 01 0C 01 09 01 09 01 09 02 09 08 09 0A 09 0F 09 34 09 0E 09 33 09 0F 09 34 09 0E 09 3E 09 0E 09 08)

