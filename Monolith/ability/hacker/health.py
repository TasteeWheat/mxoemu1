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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00Z\x02\x00d\x00\x00k\x03\x00Z\x04\x00d\x00\x00k\x05\x00Z\x06\x00d\x00\x00k\x07\x00Z\x08\x00d\x00\x00k\t\x00i\n\x00Z\x0b\x00d\x01\x00k\x0c\x00Td\x00\x00k\r\x00Z\x0e\x00d\x02\x00Z\x0f\x00d\x03\x00\x84\x00\x00Z\x10\x00d\x04\x00\x84\x00\x00Z\x11\x00d\x05\x00e\x11\x00_\x12\x00d\x06\x00\x84\x00\x00Z\x13\x00d\x07\x00\x84\x00\x00Z\x14\x00d\x08\x00\x84\x00\x00Z\x15\x00d\t\x00\x84\x00\x00Z\x16\x00d\n\x00k\x17\x00l\x18\x00Z\x18\x00\x01d\x0b\x00Ge\x18\x00\x83\x00\x00GHd\x00\x00S' (B4 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 5A 02 00 64 00 00 6B 03 00 5A 04 00 64 00 00 6B 05 00 5A 06 00 64 00 00 6B 07 00 5A 08 00 64 00 00 6B 09 00 69 0A 00 5A 0B 00 64 01 00 6B 0C 00 54 64 00 00 6B 0D 00 5A 0E 00 64 02 00 5A 0F 00 64 03 00 84 00 00 5A 10 00 64 04 00 84 00 00 5A 11 00 64 05 00 65 11 00 5F 12 00 64 06 00 84 00 00 5A 13 00 64 07 00 84 00 00 5A 14 00 64 08 00 84 00 00 5A 15 00 64 09 00 84 00 00 5A 16 00 64 0A 00 6B 17 00 6C 18 00 5A 18 00 01 64 0B 00 47 65 18 00 83 00 00 47 48 64 00 00 53)
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
                 0000001E     6B - IMPORT_NAME         'missionvalidate'
                 00000021     5A - STORE_NAME          'mv'
                 00000024     64 - LOAD_CONST          None
                 00000027     6B - IMPORT_NAME         'combatvalidate'
                 0000002A     5A - STORE_NAME          'cv'
                 0000002D     64 - LOAD_CONST          None
                 00000030     6B - IMPORT_NAME         'stringtable_client'
                 00000033     5A - STORE_NAME          'StringTable'
                 00000036     64 - LOAD_CONST          None
                 00000039     6B - IMPORT_NAME         'ability.utility'
                 0000003C     69 - LOAD_ATTR           'utility'
                 0000003F     5A - STORE_NAME          'Utility'
                 00000042     64 - LOAD_CONST          ('*')
                 00000045     6B - IMPORT_NAME         'ability.defines'
                 00000048     54 - IMPORT_STAR         
                 00000049     64 - LOAD_CONST          None
                 0000004C     6B - IMPORT_NAME         'ltfxmap'
                 0000004F     5A - STORE_NAME          'FX'
                 00000052     64 - LOAD_CONST          60
                 00000055     5A - STORE_NAME          'RequestTime'
                 00000058     64 - LOAD_CONST          CODE('RestoreRSI_DirectObject')
                 0000005B     84 - MAKE_FUNCTION       r0000
                 0000005E     5A - STORE_NAME          'RestoreRSI_DirectObject'
                 00000061     64 - LOAD_CONST          CODE('RestoreRSI_Test')
                 00000064     84 - MAKE_FUNCTION       r0000
                 00000067     5A - STORE_NAME          'RestoreRSI_Test'
                 0000006A     64 - LOAD_CONST          '\n'
                 0000006D     65 - LOAD_NAME           'RestoreRSI_Test'
                 00000070     5F - STORE_ATTR          'depAttr'
                 00000073     64 - LOAD_CONST          CODE('RevitalizeRSI_DirectObject')
                 00000076     84 - MAKE_FUNCTION       r0000
                 00000079     5A - STORE_NAME          'RevitalizeRSI_DirectObject'
                 0000007C     64 - LOAD_CONST          CODE('RejuvenateRSI_DirectObject')
                 0000007F     84 - MAKE_FUNCTION       r0000
                 00000082     5A - STORE_NAME          'RejuvenateRSI_DirectObject'
                 00000085     64 - LOAD_CONST          CODE('ReviveRSI_DirectObject')
                 00000088     84 - MAKE_FUNCTION       r0000
                 0000008B     5A - STORE_NAME          'ReviveRSI_DirectObject'
                 0000008E     64 - LOAD_CONST          CODE('RenewRSI_DirectObject')
                 00000091     84 - MAKE_FUNCTION       r0000
                 00000094     5A - STORE_NAME          'RenewRSI_DirectObject'
                 00000097     64 - LOAD_CONST          ('ctime')
                 0000009A     6B - IMPORT_NAME         'time'
                 0000009D     6C - IMPORT_FROM         'ctime'
                 000000A0     5A - STORE_NAME          'ctime'
                 000000A3     01 - POP_TOP             
                 000000A4     64 - LOAD_CONST          'Reloading Health '
                 000000A7     47 - PRINT_ITEM          
                 000000A8     65 - LOAD_NAME           'ctime'
                 000000AB     83 - CALL_FUNCTION       r0000
                 000000AE     47 - PRINT_ITEM          
                 000000AF     48 - PRINT_NEWLINE       
                 000000B0     64 - LOAD_CONST          None
                 000000B3     53 - RETURN_VALUE        
             consts:
000000D2         TUPLE: (
000000D7             None (4E),
000000D8             TUPLE: (
000000DD                 STR: '*' (01 00 00 00 2A)
                     ),
000000E3             INT: 60 (3C 00 00 00),
000000E8             CODE:
                         argcount:
000000E9                     LONG: 2L (02 00 00 00)
                         nlocals:
000000ED                     LONG: 3L (03 00 00 00)
                         stacksize:
000000F1                     LONG: 5L (05 00 00 00)
                         flags:
000000F5                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000000F9                     STR: 'd\x01\x00}\x02\x00|\x00\x00i\x02\x00i\x03\x00\x83\x00\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x00\x00i\x04\x00i\x06\x00d\x02\x00\x18\x83\x01\x00\x01d\x02\x00|\x00\x00i\x04\x00_\x07\x00t\x08\x00i\t\x00|\x00\x00i\n\x00|\x00\x00i\n\x00t\x0b\x00i\x0c\x00d\x03\x00\x83\x04\x00\x01|\x00\x00i\r\x00i\x0e\x00t\x0f\x00t\x10\x00t\x11\x00\x83\x03\x00\x01t\x12\x00i\x13\x00t\x14\x00i\x15\x00t\x11\x00|\x01\x00\x83\x03\x00\x01t\x12\x00i\x17\x00t\x14\x00i\x18\x00t\x11\x00|\x01\x00\x83\x03\x00\x01|\x00\x00i\x04\x00i\x19\x00\x83\x00\x00o\x17\x00\x01t\x08\x00i\x1a\x00|\x01\x00i\x1b\x00d\x04\x00\x83\x02\x00\x01n\x01\x00\x01d\x00\x00S' (C5 00 00 00 64 01 00 7D 02 00 7C 00 00 69 02 00 69 03 00 83 00 00 01 7C 00 00 69 04 00 69 05 00 7C 00 00 69 04 00 69 06 00 64 02 00 18 83 01 00 01 64 02 00 7C 00 00 69 04 00 5F 07 00 74 08 00 69 09 00 7C 00 00 69 0A 00 7C 00 00 69 0A 00 74 0B 00 69 0C 00 64 03 00 83 04 00 01 7C 00 00 69 0D 00 69 0E 00 74 0F 00 74 10 00 74 11 00 83 03 00 01 74 12 00 69 13 00 74 14 00 69 15 00 74 11 00 7C 01 00 83 03 00 01 74 12 00 69 17 00 74 14 00 69 18 00 74 11 00 7C 01 00 83 03 00 01 7C 00 00 69 04 00 69 19 00 83 00 00 6F 17 00 01 74 08 00 69 1A 00 7C 01 00 69 1B 00 64 04 00 83 02 00 01 6E 01 00 01 64 00 00 53)
                             00000000     64 - LOAD_CONST          120
                             00000003     7D - STORE_FAST          'duration'
                             00000006     7C - LOAD_FAST           'subject'
                             00000009     69 - LOAD_ATTR           'PlayerCharacter'
                             0000000C     69 - LOAD_ATTR           'resuscitate'
                             0000000F     83 - CALL_FUNCTION       r0000
                             00000012     01 - POP_TOP             
                             00000013     7C - LOAD_FAST           'subject'
                             00000016     69 - LOAD_ATTR           'AbilityInv'
                             00000019     69 - LOAD_ATTR           'takeInnerStrength'
                             0000001C     7C - LOAD_FAST           'subject'
                             0000001F     69 - LOAD_ATTR           'AbilityInv'
                             00000022     69 - LOAD_ATTR           'InnerStrengthMax'
                             00000025     64 - LOAD_CONST          1
                             00000028     18 - BINARY_SUBTRACT     
                             00000029     83 - CALL_FUNCTION       r0001
                             0000002C     01 - POP_TOP             
                             0000002D     64 - LOAD_CONST          1
                             00000030     7C - LOAD_FAST           'subject'
                             00000033     69 - LOAD_ATTR           'AbilityInv'
                             00000036     5F - STORE_ATTR          'Health'
                             00000039     74 - LOAD_GLOBAL         'discovery'
                             0000003C     69 - LOAD_ATTR           'playEffect'
                             0000003F     7C - LOAD_FAST           'subject'
                             00000042     69 - LOAD_ATTR           'locator'
                             00000045     7C - LOAD_FAST           'subject'
                             00000048     69 - LOAD_ATTR           'locator'
                             0000004B     74 - LOAD_GLOBAL         'FX'
                             0000004E     69 - LOAD_ATTR           'FX_CHARACTER_RESTORE_RSI'
                             00000051     64 - LOAD_CONST          0
                             00000054     83 - CALL_FUNCTION       r0004
                             00000057     01 - POP_TOP             
                             00000058     7C - LOAD_FAST           'subject'
                             0000005B     69 - LOAD_ATTR           'CharMvt'
                             0000005E     69 - LOAD_ATTR           'playScript'
                             00000061     74 - LOAD_GLOBAL         'Stance_Stand'
                             00000064     74 - LOAD_GLOBAL         'Action_Resurrect'
                             00000067     74 - LOAD_GLOBAL         'RestoreRSIAbility'
                             0000006A     83 - CALL_FUNCTION       r0003
                             0000006D     01 - POP_TOP             
                             0000006E     74 - LOAD_GLOBAL         'Utility'
                             00000071     69 - LOAD_ATTR           'SendAbilityOutputToTargetMsg'
                             00000074     74 - LOAD_GLOBAL         'StringTable'
                             00000077     69 - LOAD_ATTR           'ID_CLIENT_ABILITY_REZ_DIRECTOBJECT'
                             0000007A     74 - LOAD_GLOBAL         'RestoreRSIAbility'
                             0000007D     7C - LOAD_FAST           'msg'
                             00000080     83 - CALL_FUNCTION       r0003
                             00000083     01 - POP_TOP             
                             00000084     74 - LOAD_GLOBAL         'Utility'
                             00000087     69 - LOAD_ATTR           'SendAbilityOutputToCasterMsg'
                             0000008A     74 - LOAD_GLOBAL         'StringTable'
                             0000008D     69 - LOAD_ATTR           'ID_CLIENT_ABILITY_REZ_SUBJECT'
                             00000090     74 - LOAD_GLOBAL         'RestoreRSIAbility'
                             00000093     7C - LOAD_FAST           'msg'
                             00000096     83 - CALL_FUNCTION       r0003
                             00000099     01 - POP_TOP             
                             0000009A     7C - LOAD_FAST           'subject'
                             0000009D     69 - LOAD_ATTR           'AbilityInv'
                             000000A0     69 - LOAD_ATTR           'isPvP'
                             000000A3     83 - CALL_FUNCTION       r0000
                             000000A6     6F - JUMP_IF_FALSE       -> 000000C0
                             000000A9     01 - POP_TOP             
                             000000AA     74 - LOAD_GLOBAL         'discovery'
                             000000AD     69 - LOAD_ATTR           'sendApplyAbilityToSelf'
                             000000B0     7C - LOAD_FAST           'msg'
                             000000B3     69 - LOAD_ATTR           'subjectLocator'
                             000000B6     64 - LOAD_CONST          1208
                             000000B9     83 - CALL_FUNCTION       r0002
                             000000BC     01 - POP_TOP             
                             000000BD     6E - JUMP_FORWARD        -> 000000C1
                             000000C0     01 - POP_TOP             
                             000000C1     64 - LOAD_CONST          None
                             000000C4     53 - RETURN_VALUE        
                         consts:
000001C3                     TUPLE: (
000001C8                         None (4E),
000001C9                         INT: 120 (78 00 00 00),
000001CE                         INT: 1 (01 00 00 00),
000001D3                         INT: 0 (00 00 00 00),
000001D8                         INT: 1208 (B8 04 00 00)
                             )
                         names:
000001DD                     TUPLE: (
000001E2                         STR: 'duration' (08 00 00 00 64 75 72 61 74 69 6F 6E),
000001EF                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000001FB                         STR: 'PlayerCharacter' (0F 00 00 00 50 6C 61 79 65 72 43 68 61 72 61 63 74 65 72),
0000020F                         STR: 'resuscitate' (0B 00 00 00 72 65 73 75 73 63 69 74 61 74 65),
0000021F                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
0000022E                         STR: 'takeInnerStrength' (11 00 00 00 74 61 6B 65 49 6E 6E 65 72 53 74 72 65 6E 67 74 68),
00000244                         STR: 'InnerStrengthMax' (10 00 00 00 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 4D 61 78),
00000259                         STR: 'Health' (06 00 00 00 48 65 61 6C 74 68),
00000264                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
00000272                         STR: 'playEffect' (0A 00 00 00 70 6C 61 79 45 66 66 65 63 74),
00000281                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
0000028D                         STR: 'FX' (02 00 00 00 46 58),
00000294                         STR: 'FX_CHARACTER_RESTORE_RSI' (18 00 00 00 46 58 5F 43 48 41 52 41 43 54 45 52 5F 52 45 53 54 4F 52 45 5F 52 53 49),
000002B1                         STR: 'CharMvt' (07 00 00 00 43 68 61 72 4D 76 74),
000002BD                         STR: 'playScript' (0A 00 00 00 70 6C 61 79 53 63 72 69 70 74),
000002CC                         STR: 'Stance_Stand' (0C 00 00 00 53 74 61 6E 63 65 5F 53 74 61 6E 64),
000002DD                         STR: 'Action_Resurrect' (10 00 00 00 41 63 74 69 6F 6E 5F 52 65 73 75 72 72 65 63 74),
000002F2                         STR: 'RestoreRSIAbility' (11 00 00 00 52 65 73 74 6F 72 65 52 53 49 41 62 69 6C 69 74 79),
00000308                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000314                         STR: 'SendAbilityOutputToTargetMsg' (1C 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 54 61 72 67 65 74 4D 73 67),
00000335                         STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00000345                         STR: 'ID_CLIENT_ABILITY_REZ_DIRECTOBJECT' (22 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 41 42 49 4C 49 54 59 5F 52 45 5A 5F 44 49 52 45 43 54 4F 42 4A 45 43 54),
0000036C                         STR: 'msg' (03 00 00 00 6D 73 67),
00000374                         STR: 'SendAbilityOutputToCasterMsg' (1C 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 43 61 73 74 65 72 4D 73 67),
00000395                         STR: 'ID_CLIENT_ABILITY_REZ_SUBJECT' (1D 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 41 42 49 4C 49 54 59 5F 52 45 5A 5F 53 55 42 4A 45 43 54),
000003B7                         STR: 'isPvP' (05 00 00 00 69 73 50 76 50),
000003C1                         STR: 'sendApplyAbilityToSelf' (16 00 00 00 73 65 6E 64 41 70 70 6C 79 41 62 69 6C 69 74 79 54 6F 53 65 6C 66),
000003DC                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
000003EF                     TUPLE: (
000003F4                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000400                         STR: 'msg' (03 00 00 00 6D 73 67),
00000408                         STR: 'duration' (08 00 00 00 64 75 72 61 74 69 6F 6E)
                             )
                         freevars:
00000415                     TUPLE: ()
                         cellvars:
0000041A                     TUPLE: ()
                         filename:
0000041F                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\health.py' (4D 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 68 65 61 6C 74 68 2E 70 79)
                         name:
00000471                     STR: 'RestoreRSI_DirectObject' (17 00 00 00 52 65 73 74 6F 72 65 52 53 49 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
0000048D                     LONG: 31L (1F 00 00 00)
                         lnotab:
00000491                     STR: '\x00\x02\x06\x01\r\x01\x1a\x01\x0c\x03\x1f\x02\x16\x01\x16\x01\x16\x01\x10\x01' (14 00 00 00 00 02 06 01 0D 01 1A 01 0C 03 1F 02 16 01 16 01 16 01 10 01),
000004AA             CODE:
                         argcount:
000004AB                     LONG: 1L (01 00 00 00)
                         nlocals:
000004AF                     LONG: 1L (01 00 00 00)
                         stacksize:
000004B3                     LONG: 2L (02 00 00 00)
                         flags:
000004B7                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000004BB                     STR: 't\x00\x00|\x00\x00_\x02\x00d\x00\x00S' (0D 00 00 00 74 00 00 7C 00 00 5F 02 00 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'SUCCESS'
                             00000003     7C - LOAD_FAST           'sentence'
                             00000006     5F - STORE_ATTR          'result'
                             00000009     64 - LOAD_CONST          None
                             0000000C     53 - RETURN_VALUE        
                         consts:
000004CD                     TUPLE: (
000004D2                         None (4E)
                             )
                         names:
000004D3                     TUPLE: (
000004D8                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
000004E4                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65),
000004F1                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74)
                             )
                         varnames:
000004FC                     TUPLE: (
00000501                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65)
                             )
                         freevars:
0000050E                     TUPLE: ()
                         cellvars:
00000513                     TUPLE: ()
                         filename:
00000518                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\health.py' (4D 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 68 65 61 6C 74 68 2E 70 79)
                         name:
0000056A                     STR: 'RestoreRSI_Test' (0F 00 00 00 52 65 73 74 6F 72 65 52 53 49 5F 54 65 73 74)
                         firslineno:
0000057E                     LONG: 49L (31 00 00 00)
                         lnotab:
00000582                     STR: '\x00\x01' (02 00 00 00 00 01),
00000589             STR: '\n' (01 00 00 00 0A),
0000058F             CODE:
                         argcount:
00000590                     LONG: 2L (02 00 00 00)
                         nlocals:
00000594                     LONG: 2L (02 00 00 00)
                         stacksize:
00000598                     LONG: 5L (05 00 00 00)
                         flags:
0000059C                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000005A0                     STR: '|\x00\x00i\x01\x00i\x02\x00\x83\x00\x00\x01t\x03\x00i\x04\x00|\x00\x00i\x05\x00|\x00\x00i\x05\x00t\x06\x00i\x07\x00d\x01\x00\x83\x04\x00\x01|\x00\x00i\x08\x00i\t\x00t\n\x00t\x0b\x00t\x0c\x00\x83\x03\x00\x01|\x00\x00i\r\x00i\x0e\x00|\x00\x00i\r\x00_\x0f\x00|\x00\x00i\r\x00i\x10\x00|\x00\x00i\r\x00i\x11\x00\x0b\x83\x01\x00\x01t\x12\x00i\x13\x00t\x14\x00i\x15\x00t\x0c\x00|\x01\x00\x83\x03\x00\x01t\x12\x00i\x17\x00t\x14\x00i\x18\x00t\x0c\x00|\x01\x00\x83\x03\x00\x01|\x00\x00i\r\x00i\x19\x00\x83\x00\x00o\x17\x00\x01t\x03\x00i\x1a\x00|\x01\x00i\x1b\x00d\x02\x00\x83\x02\x00\x01n\x01\x00\x01d\x00\x00S' (C2 00 00 00 7C 00 00 69 01 00 69 02 00 83 00 00 01 74 03 00 69 04 00 7C 00 00 69 05 00 7C 00 00 69 05 00 74 06 00 69 07 00 64 01 00 83 04 00 01 7C 00 00 69 08 00 69 09 00 74 0A 00 74 0B 00 74 0C 00 83 03 00 01 7C 00 00 69 0D 00 69 0E 00 7C 00 00 69 0D 00 5F 0F 00 7C 00 00 69 0D 00 69 10 00 7C 00 00 69 0D 00 69 11 00 0B 83 01 00 01 74 12 00 69 13 00 74 14 00 69 15 00 74 0C 00 7C 01 00 83 03 00 01 74 12 00 69 17 00 74 14 00 69 18 00 74 0C 00 7C 01 00 83 03 00 01 7C 00 00 69 0D 00 69 19 00 83 00 00 6F 17 00 01 74 03 00 69 1A 00 7C 01 00 69 1B 00 64 02 00 83 02 00 01 6E 01 00 01 64 00 00 53)
                             00000000     7C - LOAD_FAST           'subject'
                             00000003     69 - LOAD_ATTR           'PlayerCharacter'
                             00000006     69 - LOAD_ATTR           'resuscitate'
                             00000009     83 - CALL_FUNCTION       r0000
                             0000000C     01 - POP_TOP             
                             0000000D     74 - LOAD_GLOBAL         'discovery'
                             00000010     69 - LOAD_ATTR           'playEffect'
                             00000013     7C - LOAD_FAST           'subject'
                             00000016     69 - LOAD_ATTR           'locator'
                             00000019     7C - LOAD_FAST           'subject'
                             0000001C     69 - LOAD_ATTR           'locator'
                             0000001F     74 - LOAD_GLOBAL         'FX'
                             00000022     69 - LOAD_ATTR           'FX_CHARACTER_RESTORE_RSI'
                             00000025     64 - LOAD_CONST          0
                             00000028     83 - CALL_FUNCTION       r0004
                             0000002B     01 - POP_TOP             
                             0000002C     7C - LOAD_FAST           'subject'
                             0000002F     69 - LOAD_ATTR           'CharMvt'
                             00000032     69 - LOAD_ATTR           'playScript'
                             00000035     74 - LOAD_GLOBAL         'Stance_Stand'
                             00000038     74 - LOAD_GLOBAL         'Action_Resurrect'
                             0000003B     74 - LOAD_GLOBAL         'RevitalizeRSIAbility'
                             0000003E     83 - CALL_FUNCTION       r0003
                             00000041     01 - POP_TOP             
                             00000042     7C - LOAD_FAST           'subject'
                             00000045     69 - LOAD_ATTR           'AbilityInv'
                             00000048     69 - LOAD_ATTR           'MaxHealth'
                             0000004B     7C - LOAD_FAST           'subject'
                             0000004E     69 - LOAD_ATTR           'AbilityInv'
                             00000051     5F - STORE_ATTR          'Health'
                             00000054     7C - LOAD_FAST           'subject'
                             00000057     69 - LOAD_ATTR           'AbilityInv'
                             0000005A     69 - LOAD_ATTR           'takeInnerStrength'
                             0000005D     7C - LOAD_FAST           'subject'
                             00000060     69 - LOAD_ATTR           'AbilityInv'
                             00000063     69 - LOAD_ATTR           'InnerStrengthMax'
                             00000066     0B - UNARY_NEGATIVE      
                             00000067     83 - CALL_FUNCTION       r0001
                             0000006A     01 - POP_TOP             
                             0000006B     74 - LOAD_GLOBAL         'Utility'
                             0000006E     69 - LOAD_ATTR           'SendAbilityOutputToTargetMsg'
                             00000071     74 - LOAD_GLOBAL         'StringTable'
                             00000074     69 - LOAD_ATTR           'ID_CLIENT_ABILITY_REZ_DIRECTOBJECT'
                             00000077     74 - LOAD_GLOBAL         'RevitalizeRSIAbility'
                             0000007A     7C - LOAD_FAST           'msg'
                             0000007D     83 - CALL_FUNCTION       r0003
                             00000080     01 - POP_TOP             
                             00000081     74 - LOAD_GLOBAL         'Utility'
                             00000084     69 - LOAD_ATTR           'SendAbilityOutputToCasterMsg'
                             00000087     74 - LOAD_GLOBAL         'StringTable'
                             0000008A     69 - LOAD_ATTR           'ID_CLIENT_ABILITY_REZ_SUBJECT'
                             0000008D     74 - LOAD_GLOBAL         'RevitalizeRSIAbility'
                             00000090     7C - LOAD_FAST           'msg'
                             00000093     83 - CALL_FUNCTION       r0003
                             00000096     01 - POP_TOP             
                             00000097     7C - LOAD_FAST           'subject'
                             0000009A     69 - LOAD_ATTR           'AbilityInv'
                             0000009D     69 - LOAD_ATTR           'isPvP'
                             000000A0     83 - CALL_FUNCTION       r0000
                             000000A3     6F - JUMP_IF_FALSE       -> 000000BD
                             000000A6     01 - POP_TOP             
                             000000A7     74 - LOAD_GLOBAL         'discovery'
                             000000AA     69 - LOAD_ATTR           'sendApplyAbilityToSelf'
                             000000AD     7C - LOAD_FAST           'msg'
                             000000B0     69 - LOAD_ATTR           'subjectLocator'
                             000000B3     64 - LOAD_CONST          1208
                             000000B6     83 - CALL_FUNCTION       r0002
                             000000B9     01 - POP_TOP             
                             000000BA     6E - JUMP_FORWARD        -> 000000BE
                             000000BD     01 - POP_TOP             
                             000000BE     64 - LOAD_CONST          None
                             000000C1     53 - RETURN_VALUE        
                         consts:
00000667                     TUPLE: (
0000066C                         None (4E),
0000066D                         INT: 0 (00 00 00 00),
00000672                         INT: 1208 (B8 04 00 00)
                             )
                         names:
00000677                     TUPLE: (
0000067C                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000688                         STR: 'PlayerCharacter' (0F 00 00 00 50 6C 61 79 65 72 43 68 61 72 61 63 74 65 72),
0000069C                         STR: 'resuscitate' (0B 00 00 00 72 65 73 75 73 63 69 74 61 74 65),
000006AC                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
000006BA                         STR: 'playEffect' (0A 00 00 00 70 6C 61 79 45 66 66 65 63 74),
000006C9                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
000006D5                         STR: 'FX' (02 00 00 00 46 58),
000006DC                         STR: 'FX_CHARACTER_RESTORE_RSI' (18 00 00 00 46 58 5F 43 48 41 52 41 43 54 45 52 5F 52 45 53 54 4F 52 45 5F 52 53 49),
000006F9                         STR: 'CharMvt' (07 00 00 00 43 68 61 72 4D 76 74),
00000705                         STR: 'playScript' (0A 00 00 00 70 6C 61 79 53 63 72 69 70 74),
00000714                         STR: 'Stance_Stand' (0C 00 00 00 53 74 61 6E 63 65 5F 53 74 61 6E 64),
00000725                         STR: 'Action_Resurrect' (10 00 00 00 41 63 74 69 6F 6E 5F 52 65 73 75 72 72 65 63 74),
0000073A                         STR: 'RevitalizeRSIAbility' (14 00 00 00 52 65 76 69 74 61 6C 69 7A 65 52 53 49 41 62 69 6C 69 74 79),
00000753                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
00000762                         STR: 'MaxHealth' (09 00 00 00 4D 61 78 48 65 61 6C 74 68),
00000770                         STR: 'Health' (06 00 00 00 48 65 61 6C 74 68),
0000077B                         STR: 'takeInnerStrength' (11 00 00 00 74 61 6B 65 49 6E 6E 65 72 53 74 72 65 6E 67 74 68),
00000791                         STR: 'InnerStrengthMax' (10 00 00 00 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 4D 61 78),
000007A6                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000007B2                         STR: 'SendAbilityOutputToTargetMsg' (1C 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 54 61 72 67 65 74 4D 73 67),
000007D3                         STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
000007E3                         STR: 'ID_CLIENT_ABILITY_REZ_DIRECTOBJECT' (22 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 41 42 49 4C 49 54 59 5F 52 45 5A 5F 44 49 52 45 43 54 4F 42 4A 45 43 54),
0000080A                         STR: 'msg' (03 00 00 00 6D 73 67),
00000812                         STR: 'SendAbilityOutputToCasterMsg' (1C 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 43 61 73 74 65 72 4D 73 67),
00000833                         STR: 'ID_CLIENT_ABILITY_REZ_SUBJECT' (1D 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 41 42 49 4C 49 54 59 5F 52 45 5A 5F 53 55 42 4A 45 43 54),
00000855                         STR: 'isPvP' (05 00 00 00 69 73 50 76 50),
0000085F                         STR: 'sendApplyAbilityToSelf' (16 00 00 00 73 65 6E 64 41 70 70 6C 79 41 62 69 6C 69 74 79 54 6F 53 65 6C 66),
0000087A                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
0000088D                     TUPLE: (
00000892                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000089E                         STR: 'msg' (03 00 00 00 6D 73 67)
                             )
                         freevars:
000008A6                     TUPLE: ()
                         cellvars:
000008AB                     TUPLE: ()
                         filename:
000008B0                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\health.py' (4D 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 68 65 61 6C 74 68 2E 70 79)
                         name:
00000902                     STR: 'RevitalizeRSI_DirectObject' (1A 00 00 00 52 65 76 69 74 61 6C 69 7A 65 52 53 49 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000921                     LONG: 69L (45 00 00 00)
                         lnotab:
00000925                     STR: '\x00\x01\r\x03\x1f\x01\x16\x01\x12\x01\x17\x01\x16\x01\x16\x01\x10\x01' (12 00 00 00 00 01 0D 03 1F 01 16 01 12 01 17 01 16 01 16 01 10 01),
0000093C             CODE:
                         argcount:
0000093D                     LONG: 2L (02 00 00 00)
                         nlocals:
00000941                     LONG: 2L (02 00 00 00)
                         stacksize:
00000945                     LONG: 5L (05 00 00 00)
                         flags:
00000949                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000094D                     STR: '|\x00\x00i\x01\x00i\x02\x00\x83\x00\x00\x01|\x00\x00i\x03\x00i\x04\x00|\x00\x00i\x03\x00_\x05\x00|\x00\x00i\x03\x00i\x06\x00|\x00\x00i\x03\x00i\x07\x00\x0b\x83\x01\x00\x01t\x08\x00i\t\x00|\x00\x00i\n\x00|\x00\x00i\n\x00t\x0b\x00i\x0c\x00d\x01\x00\x83\x04\x00\x01|\x00\x00i\r\x00i\x0e\x00t\x0f\x00t\x10\x00t\x11\x00\x83\x03\x00\x01t\x12\x00i\x13\x00t\x14\x00i\x15\x00t\x11\x00|\x01\x00\x83\x03\x00\x01t\x12\x00i\x17\x00t\x14\x00i\x18\x00t\x11\x00|\x01\x00\x83\x03\x00\x01|\x00\x00i\x03\x00i\x19\x00\x83\x00\x00o\x17\x00\x01t\x08\x00i\x1a\x00|\x01\x00i\x1b\x00d\x02\x00\x83\x02\x00\x01n\x01\x00\x01d\x00\x00S' (C2 00 00 00 7C 00 00 69 01 00 69 02 00 83 00 00 01 7C 00 00 69 03 00 69 04 00 7C 00 00 69 03 00 5F 05 00 7C 00 00 69 03 00 69 06 00 7C 00 00 69 03 00 69 07 00 0B 83 01 00 01 74 08 00 69 09 00 7C 00 00 69 0A 00 7C 00 00 69 0A 00 74 0B 00 69 0C 00 64 01 00 83 04 00 01 7C 00 00 69 0D 00 69 0E 00 74 0F 00 74 10 00 74 11 00 83 03 00 01 74 12 00 69 13 00 74 14 00 69 15 00 74 11 00 7C 01 00 83 03 00 01 74 12 00 69 17 00 74 14 00 69 18 00 74 11 00 7C 01 00 83 03 00 01 7C 00 00 69 03 00 69 19 00 83 00 00 6F 17 00 01 74 08 00 69 1A 00 7C 01 00 69 1B 00 64 02 00 83 02 00 01 6E 01 00 01 64 00 00 53)
                             00000000     7C - LOAD_FAST           'subject'
                             00000003     69 - LOAD_ATTR           'PlayerCharacter'
                             00000006     69 - LOAD_ATTR           'resuscitate'
                             00000009     83 - CALL_FUNCTION       r0000
                             0000000C     01 - POP_TOP             
                             0000000D     7C - LOAD_FAST           'subject'
                             00000010     69 - LOAD_ATTR           'AbilityInv'
                             00000013     69 - LOAD_ATTR           'MaxHealth'
                             00000016     7C - LOAD_FAST           'subject'
                             00000019     69 - LOAD_ATTR           'AbilityInv'
                             0000001C     5F - STORE_ATTR          'Health'
                             0000001F     7C - LOAD_FAST           'subject'
                             00000022     69 - LOAD_ATTR           'AbilityInv'
                             00000025     69 - LOAD_ATTR           'takeInnerStrength'
                             00000028     7C - LOAD_FAST           'subject'
                             0000002B     69 - LOAD_ATTR           'AbilityInv'
                             0000002E     69 - LOAD_ATTR           'InnerStrengthMax'
                             00000031     0B - UNARY_NEGATIVE      
                             00000032     83 - CALL_FUNCTION       r0001
                             00000035     01 - POP_TOP             
                             00000036     74 - LOAD_GLOBAL         'discovery'
                             00000039     69 - LOAD_ATTR           'playEffect'
                             0000003C     7C - LOAD_FAST           'subject'
                             0000003F     69 - LOAD_ATTR           'locator'
                             00000042     7C - LOAD_FAST           'subject'
                             00000045     69 - LOAD_ATTR           'locator'
                             00000048     74 - LOAD_GLOBAL         'FX'
                             0000004B     69 - LOAD_ATTR           'FX_CHARACTER_RESTORE_RSI'
                             0000004E     64 - LOAD_CONST          0
                             00000051     83 - CALL_FUNCTION       r0004
                             00000054     01 - POP_TOP             
                             00000055     7C - LOAD_FAST           'subject'
                             00000058     69 - LOAD_ATTR           'CharMvt'
                             0000005B     69 - LOAD_ATTR           'playScript'
                             0000005E     74 - LOAD_GLOBAL         'Stance_Stand'
                             00000061     74 - LOAD_GLOBAL         'Action_Resurrect'
                             00000064     74 - LOAD_GLOBAL         'RejuvenateRSIAbility'
                             00000067     83 - CALL_FUNCTION       r0003
                             0000006A     01 - POP_TOP             
                             0000006B     74 - LOAD_GLOBAL         'Utility'
                             0000006E     69 - LOAD_ATTR           'SendAbilityOutputToTargetMsg'
                             00000071     74 - LOAD_GLOBAL         'StringTable'
                             00000074     69 - LOAD_ATTR           'ID_CLIENT_ABILITY_REZ_DIRECTOBJECT'
                             00000077     74 - LOAD_GLOBAL         'RejuvenateRSIAbility'
                             0000007A     7C - LOAD_FAST           'msg'
                             0000007D     83 - CALL_FUNCTION       r0003
                             00000080     01 - POP_TOP             
                             00000081     74 - LOAD_GLOBAL         'Utility'
                             00000084     69 - LOAD_ATTR           'SendAbilityOutputToCasterMsg'
                             00000087     74 - LOAD_GLOBAL         'StringTable'
                             0000008A     69 - LOAD_ATTR           'ID_CLIENT_ABILITY_REZ_SUBJECT'
                             0000008D     74 - LOAD_GLOBAL         'RejuvenateRSIAbility'
                             00000090     7C - LOAD_FAST           'msg'
                             00000093     83 - CALL_FUNCTION       r0003
                             00000096     01 - POP_TOP             
                             00000097     7C - LOAD_FAST           'subject'
                             0000009A     69 - LOAD_ATTR           'AbilityInv'
                             0000009D     69 - LOAD_ATTR           'isPvP'
                             000000A0     83 - CALL_FUNCTION       r0000
                             000000A3     6F - JUMP_IF_FALSE       -> 000000BD
                             000000A6     01 - POP_TOP             
                             000000A7     74 - LOAD_GLOBAL         'discovery'
                             000000AA     69 - LOAD_ATTR           'sendApplyAbilityToSelf'
                             000000AD     7C - LOAD_FAST           'msg'
                             000000B0     69 - LOAD_ATTR           'subjectLocator'
                             000000B3     64 - LOAD_CONST          1208
                             000000B6     83 - CALL_FUNCTION       r0002
                             000000B9     01 - POP_TOP             
                             000000BA     6E - JUMP_FORWARD        -> 000000BE
                             000000BD     01 - POP_TOP             
                             000000BE     64 - LOAD_CONST          None
                             000000C1     53 - RETURN_VALUE        
                         consts:
00000A14                     TUPLE: (
00000A19                         None (4E),
00000A1A                         INT: 0 (00 00 00 00),
00000A1F                         INT: 1208 (B8 04 00 00)
                             )
                         names:
00000A24                     TUPLE: (
00000A29                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000A35                         STR: 'PlayerCharacter' (0F 00 00 00 50 6C 61 79 65 72 43 68 61 72 61 63 74 65 72),
00000A49                         STR: 'resuscitate' (0B 00 00 00 72 65 73 75 73 63 69 74 61 74 65),
00000A59                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
00000A68                         STR: 'MaxHealth' (09 00 00 00 4D 61 78 48 65 61 6C 74 68),
00000A76                         STR: 'Health' (06 00 00 00 48 65 61 6C 74 68),
00000A81                         STR: 'takeInnerStrength' (11 00 00 00 74 61 6B 65 49 6E 6E 65 72 53 74 72 65 6E 67 74 68),
00000A97                         STR: 'InnerStrengthMax' (10 00 00 00 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 4D 61 78),
00000AAC                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
00000ABA                         STR: 'playEffect' (0A 00 00 00 70 6C 61 79 45 66 66 65 63 74),
00000AC9                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
00000AD5                         STR: 'FX' (02 00 00 00 46 58),
00000ADC                         STR: 'FX_CHARACTER_RESTORE_RSI' (18 00 00 00 46 58 5F 43 48 41 52 41 43 54 45 52 5F 52 45 53 54 4F 52 45 5F 52 53 49),
00000AF9                         STR: 'CharMvt' (07 00 00 00 43 68 61 72 4D 76 74),
00000B05                         STR: 'playScript' (0A 00 00 00 70 6C 61 79 53 63 72 69 70 74),
00000B14                         STR: 'Stance_Stand' (0C 00 00 00 53 74 61 6E 63 65 5F 53 74 61 6E 64),
00000B25                         STR: 'Action_Resurrect' (10 00 00 00 41 63 74 69 6F 6E 5F 52 65 73 75 72 72 65 63 74),
00000B3A                         STR: 'RejuvenateRSIAbility' (14 00 00 00 52 65 6A 75 76 65 6E 61 74 65 52 53 49 41 62 69 6C 69 74 79),
00000B53                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000B5F                         STR: 'SendAbilityOutputToTargetMsg' (1C 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 54 61 72 67 65 74 4D 73 67),
00000B80                         STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00000B90                         STR: 'ID_CLIENT_ABILITY_REZ_DIRECTOBJECT' (22 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 41 42 49 4C 49 54 59 5F 52 45 5A 5F 44 49 52 45 43 54 4F 42 4A 45 43 54),
00000BB7                         STR: 'msg' (03 00 00 00 6D 73 67),
00000BBF                         STR: 'SendAbilityOutputToCasterMsg' (1C 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 43 61 73 74 65 72 4D 73 67),
00000BE0                         STR: 'ID_CLIENT_ABILITY_REZ_SUBJECT' (1D 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 41 42 49 4C 49 54 59 5F 52 45 5A 5F 53 55 42 4A 45 43 54),
00000C02                         STR: 'isPvP' (05 00 00 00 69 73 50 76 50),
00000C0C                         STR: 'sendApplyAbilityToSelf' (16 00 00 00 73 65 6E 64 41 70 70 6C 79 41 62 69 6C 69 74 79 54 6F 53 65 6C 66),
00000C27                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00000C3A                     TUPLE: (
00000C3F                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000C4B                         STR: 'msg' (03 00 00 00 6D 73 67)
                             )
                         freevars:
00000C53                     TUPLE: ()
                         cellvars:
00000C58                     TUPLE: ()
                         filename:
00000C5D                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\health.py' (4D 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 68 65 61 6C 74 68 2E 70 79)
                         name:
00000CAF                     STR: 'RejuvenateRSI_DirectObject' (1A 00 00 00 52 65 6A 75 76 65 6E 61 74 65 52 53 49 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000CCE                     LONG: 87L (57 00 00 00)
                         lnotab:
00000CD2                     STR: '\x00\x01\r\x01\x12\x01\x17\x02\x1f\x01\x16\x02\x16\x01\x16\x01\x10\x01' (12 00 00 00 00 01 0D 01 12 01 17 02 1F 01 16 02 16 01 16 01 10 01),
00000CE9             CODE:
                         argcount:
00000CEA                     LONG: 2L (02 00 00 00)
                         nlocals:
00000CEE                     LONG: 2L (02 00 00 00)
                         stacksize:
00000CF2                     LONG: 5L (05 00 00 00)
                         flags:
00000CF6                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000CFA                     STR: '|\x00\x00i\x01\x00i\x02\x00\x83\x00\x00\x01|\x00\x00i\x03\x00i\x04\x00|\x00\x00i\x03\x00_\x05\x00|\x00\x00i\x03\x00i\x06\x00|\x00\x00i\x03\x00i\x07\x00\x0b\x83\x01\x00\x01t\x08\x00i\t\x00|\x00\x00i\n\x00|\x00\x00i\n\x00t\x0b\x00i\x0c\x00d\x01\x00\x83\x04\x00\x01|\x00\x00i\r\x00i\x0e\x00t\x0f\x00t\x10\x00t\x11\x00\x83\x03\x00\x01t\x12\x00i\x13\x00t\x14\x00i\x15\x00t\x11\x00|\x01\x00\x83\x03\x00\x01t\x12\x00i\x17\x00t\x14\x00i\x18\x00t\x11\x00|\x01\x00\x83\x03\x00\x01|\x00\x00i\x03\x00i\x19\x00\x83\x00\x00o\x17\x00\x01t\x08\x00i\x1a\x00|\x01\x00i\x1b\x00d\x02\x00\x83\x02\x00\x01n\x01\x00\x01d\x00\x00S' (C2 00 00 00 7C 00 00 69 01 00 69 02 00 83 00 00 01 7C 00 00 69 03 00 69 04 00 7C 00 00 69 03 00 5F 05 00 7C 00 00 69 03 00 69 06 00 7C 00 00 69 03 00 69 07 00 0B 83 01 00 01 74 08 00 69 09 00 7C 00 00 69 0A 00 7C 00 00 69 0A 00 74 0B 00 69 0C 00 64 01 00 83 04 00 01 7C 00 00 69 0D 00 69 0E 00 74 0F 00 74 10 00 74 11 00 83 03 00 01 74 12 00 69 13 00 74 14 00 69 15 00 74 11 00 7C 01 00 83 03 00 01 74 12 00 69 17 00 74 14 00 69 18 00 74 11 00 7C 01 00 83 03 00 01 7C 00 00 69 03 00 69 19 00 83 00 00 6F 17 00 01 74 08 00 69 1A 00 7C 01 00 69 1B 00 64 02 00 83 02 00 01 6E 01 00 01 64 00 00 53)
                             00000000     7C - LOAD_FAST           'subject'
                             00000003     69 - LOAD_ATTR           'PlayerCharacter'
                             00000006     69 - LOAD_ATTR           'resuscitate'
                             00000009     83 - CALL_FUNCTION       r0000
                             0000000C     01 - POP_TOP             
                             0000000D     7C - LOAD_FAST           'subject'
                             00000010     69 - LOAD_ATTR           'AbilityInv'
                             00000013     69 - LOAD_ATTR           'MaxHealth'
                             00000016     7C - LOAD_FAST           'subject'
                             00000019     69 - LOAD_ATTR           'AbilityInv'
                             0000001C     5F - STORE_ATTR          'Health'
                             0000001F     7C - LOAD_FAST           'subject'
                             00000022     69 - LOAD_ATTR           'AbilityInv'
                             00000025     69 - LOAD_ATTR           'takeInnerStrength'
                             00000028     7C - LOAD_FAST           'subject'
                             0000002B     69 - LOAD_ATTR           'AbilityInv'
                             0000002E     69 - LOAD_ATTR           'InnerStrengthMax'
                             00000031     0B - UNARY_NEGATIVE      
                             00000032     83 - CALL_FUNCTION       r0001
                             00000035     01 - POP_TOP             
                             00000036     74 - LOAD_GLOBAL         'discovery'
                             00000039     69 - LOAD_ATTR           'playEffect'
                             0000003C     7C - LOAD_FAST           'subject'
                             0000003F     69 - LOAD_ATTR           'locator'
                             00000042     7C - LOAD_FAST           'subject'
                             00000045     69 - LOAD_ATTR           'locator'
                             00000048     74 - LOAD_GLOBAL         'FX'
                             0000004B     69 - LOAD_ATTR           'FX_CHARACTER_RESTORE_RSI'
                             0000004E     64 - LOAD_CONST          0
                             00000051     83 - CALL_FUNCTION       r0004
                             00000054     01 - POP_TOP             
                             00000055     7C - LOAD_FAST           'subject'
                             00000058     69 - LOAD_ATTR           'CharMvt'
                             0000005B     69 - LOAD_ATTR           'playScript'
                             0000005E     74 - LOAD_GLOBAL         'Stance_Stand'
                             00000061     74 - LOAD_GLOBAL         'Action_Resurrect'
                             00000064     74 - LOAD_GLOBAL         'ReviveRSIAbility'
                             00000067     83 - CALL_FUNCTION       r0003
                             0000006A     01 - POP_TOP             
                             0000006B     74 - LOAD_GLOBAL         'Utility'
                             0000006E     69 - LOAD_ATTR           'SendAbilityOutputToTargetMsg'
                             00000071     74 - LOAD_GLOBAL         'StringTable'
                             00000074     69 - LOAD_ATTR           'ID_CLIENT_ABILITY_REZ_DIRECTOBJECT'
                             00000077     74 - LOAD_GLOBAL         'ReviveRSIAbility'
                             0000007A     7C - LOAD_FAST           'msg'
                             0000007D     83 - CALL_FUNCTION       r0003
                             00000080     01 - POP_TOP             
                             00000081     74 - LOAD_GLOBAL         'Utility'
                             00000084     69 - LOAD_ATTR           'SendAbilityOutputToCasterMsg'
                             00000087     74 - LOAD_GLOBAL         'StringTable'
                             0000008A     69 - LOAD_ATTR           'ID_CLIENT_ABILITY_REZ_SUBJECT'
                             0000008D     74 - LOAD_GLOBAL         'ReviveRSIAbility'
                             00000090     7C - LOAD_FAST           'msg'
                             00000093     83 - CALL_FUNCTION       r0003
                             00000096     01 - POP_TOP             
                             00000097     7C - LOAD_FAST           'subject'
                             0000009A     69 - LOAD_ATTR           'AbilityInv'
                             0000009D     69 - LOAD_ATTR           'isPvP'
                             000000A0     83 - CALL_FUNCTION       r0000
                             000000A3     6F - JUMP_IF_FALSE       -> 000000BD
                             000000A6     01 - POP_TOP             
                             000000A7     74 - LOAD_GLOBAL         'discovery'
                             000000AA     69 - LOAD_ATTR           'sendApplyAbilityToSelf'
                             000000AD     7C - LOAD_FAST           'msg'
                             000000B0     69 - LOAD_ATTR           'subjectLocator'
                             000000B3     64 - LOAD_CONST          1208
                             000000B6     83 - CALL_FUNCTION       r0002
                             000000B9     01 - POP_TOP             
                             000000BA     6E - JUMP_FORWARD        -> 000000BE
                             000000BD     01 - POP_TOP             
                             000000BE     64 - LOAD_CONST          None
                             000000C1     53 - RETURN_VALUE        
                         consts:
00000DC1                     TUPLE: (
00000DC6                         None (4E),
00000DC7                         INT: 0 (00 00 00 00),
00000DCC                         INT: 1208 (B8 04 00 00)
                             )
                         names:
00000DD1                     TUPLE: (
00000DD6                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000DE2                         STR: 'PlayerCharacter' (0F 00 00 00 50 6C 61 79 65 72 43 68 61 72 61 63 74 65 72),
00000DF6                         STR: 'resuscitate' (0B 00 00 00 72 65 73 75 73 63 69 74 61 74 65),
00000E06                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
00000E15                         STR: 'MaxHealth' (09 00 00 00 4D 61 78 48 65 61 6C 74 68),
00000E23                         STR: 'Health' (06 00 00 00 48 65 61 6C 74 68),
00000E2E                         STR: 'takeInnerStrength' (11 00 00 00 74 61 6B 65 49 6E 6E 65 72 53 74 72 65 6E 67 74 68),
00000E44                         STR: 'InnerStrengthMax' (10 00 00 00 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 4D 61 78),
00000E59                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
00000E67                         STR: 'playEffect' (0A 00 00 00 70 6C 61 79 45 66 66 65 63 74),
00000E76                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
00000E82                         STR: 'FX' (02 00 00 00 46 58),
00000E89                         STR: 'FX_CHARACTER_RESTORE_RSI' (18 00 00 00 46 58 5F 43 48 41 52 41 43 54 45 52 5F 52 45 53 54 4F 52 45 5F 52 53 49),
00000EA6                         STR: 'CharMvt' (07 00 00 00 43 68 61 72 4D 76 74),
00000EB2                         STR: 'playScript' (0A 00 00 00 70 6C 61 79 53 63 72 69 70 74),
00000EC1                         STR: 'Stance_Stand' (0C 00 00 00 53 74 61 6E 63 65 5F 53 74 61 6E 64),
00000ED2                         STR: 'Action_Resurrect' (10 00 00 00 41 63 74 69 6F 6E 5F 52 65 73 75 72 72 65 63 74),
00000EE7                         STR: 'ReviveRSIAbility' (10 00 00 00 52 65 76 69 76 65 52 53 49 41 62 69 6C 69 74 79),
00000EFC                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000F08                         STR: 'SendAbilityOutputToTargetMsg' (1C 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 54 61 72 67 65 74 4D 73 67),
00000F29                         STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00000F39                         STR: 'ID_CLIENT_ABILITY_REZ_DIRECTOBJECT' (22 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 41 42 49 4C 49 54 59 5F 52 45 5A 5F 44 49 52 45 43 54 4F 42 4A 45 43 54),
00000F60                         STR: 'msg' (03 00 00 00 6D 73 67),
00000F68                         STR: 'SendAbilityOutputToCasterMsg' (1C 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 43 61 73 74 65 72 4D 73 67),
00000F89                         STR: 'ID_CLIENT_ABILITY_REZ_SUBJECT' (1D 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 41 42 49 4C 49 54 59 5F 52 45 5A 5F 53 55 42 4A 45 43 54),
00000FAB                         STR: 'isPvP' (05 00 00 00 69 73 50 76 50),
00000FB5                         STR: 'sendApplyAbilityToSelf' (16 00 00 00 73 65 6E 64 41 70 70 6C 79 41 62 69 6C 69 74 79 54 6F 53 65 6C 66),
00000FD0                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00000FE3                     TUPLE: (
00000FE8                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000FF4                         STR: 'msg' (03 00 00 00 6D 73 67)
                             )
                         freevars:
00000FFC                     TUPLE: ()
                         cellvars:
00001001                     TUPLE: ()
                         filename:
00001006                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\health.py' (4D 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 68 65 61 6C 74 68 2E 70 79)
                         name:
00001058                     STR: 'ReviveRSI_DirectObject' (16 00 00 00 52 65 76 69 76 65 52 53 49 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00001073                     LONG: 105L (69 00 00 00)
                         lnotab:
00001077                     STR: '\x00\x01\r\x01\x12\x01\x17\x02\x1f\x01\x16\x02\x16\x01\x16\x01\x10\x01' (12 00 00 00 00 01 0D 01 12 01 17 02 1F 01 16 02 16 01 16 01 10 01),
0000108E             CODE:
                         argcount:
0000108F                     LONG: 2L (02 00 00 00)
                         nlocals:
00001093                     LONG: 2L (02 00 00 00)
                         stacksize:
00001097                     LONG: 5L (05 00 00 00)
                         flags:
0000109B                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000109F                     STR: '|\x00\x00i\x01\x00i\x02\x00\x83\x00\x00\x01|\x00\x00i\x03\x00i\x04\x00|\x00\x00i\x03\x00_\x05\x00|\x00\x00i\x03\x00i\x06\x00|\x00\x00i\x03\x00i\x07\x00\x0b\x83\x01\x00\x01t\x08\x00i\t\x00|\x00\x00i\n\x00|\x00\x00i\n\x00t\x0b\x00i\x0c\x00d\x01\x00\x83\x04\x00\x01|\x00\x00i\r\x00i\x0e\x00t\x0f\x00t\x10\x00t\x11\x00\x83\x03\x00\x01t\x12\x00i\x13\x00t\x14\x00i\x15\x00t\x16\x00|\x01\x00\x83\x03\x00\x01t\x12\x00i\x18\x00t\x14\x00i\x19\x00t\x16\x00|\x01\x00\x83\x03\x00\x01|\x00\x00i\x03\x00i\x1a\x00\x83\x00\x00o\x17\x00\x01t\x08\x00i\x1b\x00|\x01\x00i\x1c\x00d\x02\x00\x83\x02\x00\x01n\x01\x00\x01d\x00\x00S' (C2 00 00 00 7C 00 00 69 01 00 69 02 00 83 00 00 01 7C 00 00 69 03 00 69 04 00 7C 00 00 69 03 00 5F 05 00 7C 00 00 69 03 00 69 06 00 7C 00 00 69 03 00 69 07 00 0B 83 01 00 01 74 08 00 69 09 00 7C 00 00 69 0A 00 7C 00 00 69 0A 00 74 0B 00 69 0C 00 64 01 00 83 04 00 01 7C 00 00 69 0D 00 69 0E 00 74 0F 00 74 10 00 74 11 00 83 03 00 01 74 12 00 69 13 00 74 14 00 69 15 00 74 16 00 7C 01 00 83 03 00 01 74 12 00 69 18 00 74 14 00 69 19 00 74 16 00 7C 01 00 83 03 00 01 7C 00 00 69 03 00 69 1A 00 83 00 00 6F 17 00 01 74 08 00 69 1B 00 7C 01 00 69 1C 00 64 02 00 83 02 00 01 6E 01 00 01 64 00 00 53)
                             00000000     7C - LOAD_FAST           'subject'
                             00000003     69 - LOAD_ATTR           'PlayerCharacter'
                             00000006     69 - LOAD_ATTR           'resuscitate'
                             00000009     83 - CALL_FUNCTION       r0000
                             0000000C     01 - POP_TOP             
                             0000000D     7C - LOAD_FAST           'subject'
                             00000010     69 - LOAD_ATTR           'AbilityInv'
                             00000013     69 - LOAD_ATTR           'MaxHealth'
                             00000016     7C - LOAD_FAST           'subject'
                             00000019     69 - LOAD_ATTR           'AbilityInv'
                             0000001C     5F - STORE_ATTR          'Health'
                             0000001F     7C - LOAD_FAST           'subject'
                             00000022     69 - LOAD_ATTR           'AbilityInv'
                             00000025     69 - LOAD_ATTR           'takeInnerStrength'
                             00000028     7C - LOAD_FAST           'subject'
                             0000002B     69 - LOAD_ATTR           'AbilityInv'
                             0000002E     69 - LOAD_ATTR           'InnerStrengthMax'
                             00000031     0B - UNARY_NEGATIVE      
                             00000032     83 - CALL_FUNCTION       r0001
                             00000035     01 - POP_TOP             
                             00000036     74 - LOAD_GLOBAL         'discovery'
                             00000039     69 - LOAD_ATTR           'playEffect'
                             0000003C     7C - LOAD_FAST           'subject'
                             0000003F     69 - LOAD_ATTR           'locator'
                             00000042     7C - LOAD_FAST           'subject'
                             00000045     69 - LOAD_ATTR           'locator'
                             00000048     74 - LOAD_GLOBAL         'FX'
                             0000004B     69 - LOAD_ATTR           'FX_CHARACTER_RESTORE_RSI'
                             0000004E     64 - LOAD_CONST          0
                             00000051     83 - CALL_FUNCTION       r0004
                             00000054     01 - POP_TOP             
                             00000055     7C - LOAD_FAST           'subject'
                             00000058     69 - LOAD_ATTR           'CharMvt'
                             0000005B     69 - LOAD_ATTR           'playScript'
                             0000005E     74 - LOAD_GLOBAL         'Stance_Stand'
                             00000061     74 - LOAD_GLOBAL         'Action_Resurrect'
                             00000064     74 - LOAD_GLOBAL         'ReviveRSIAbility'
                             00000067     83 - CALL_FUNCTION       r0003
                             0000006A     01 - POP_TOP             
                             0000006B     74 - LOAD_GLOBAL         'Utility'
                             0000006E     69 - LOAD_ATTR           'SendAbilityOutputToTargetMsg'
                             00000071     74 - LOAD_GLOBAL         'StringTable'
                             00000074     69 - LOAD_ATTR           'ID_CLIENT_ABILITY_REZ_DIRECTOBJECT'
                             00000077     74 - LOAD_GLOBAL         'RenewRSIAbility'
                             0000007A     7C - LOAD_FAST           'msg'
                             0000007D     83 - CALL_FUNCTION       r0003
                             00000080     01 - POP_TOP             
                             00000081     74 - LOAD_GLOBAL         'Utility'
                             00000084     69 - LOAD_ATTR           'SendAbilityOutputToCasterMsg'
                             00000087     74 - LOAD_GLOBAL         'StringTable'
                             0000008A     69 - LOAD_ATTR           'ID_CLIENT_ABILITY_REZ_SUBJECT'
                             0000008D     74 - LOAD_GLOBAL         'RenewRSIAbility'
                             00000090     7C - LOAD_FAST           'msg'
                             00000093     83 - CALL_FUNCTION       r0003
                             00000096     01 - POP_TOP             
                             00000097     7C - LOAD_FAST           'subject'
                             0000009A     69 - LOAD_ATTR           'AbilityInv'
                             0000009D     69 - LOAD_ATTR           'isPvP'
                             000000A0     83 - CALL_FUNCTION       r0000
                             000000A3     6F - JUMP_IF_FALSE       -> 000000BD
                             000000A6     01 - POP_TOP             
                             000000A7     74 - LOAD_GLOBAL         'discovery'
                             000000AA     69 - LOAD_ATTR           'sendApplyAbilityToSelf'
                             000000AD     7C - LOAD_FAST           'msg'
                             000000B0     69 - LOAD_ATTR           'subjectLocator'
                             000000B3     64 - LOAD_CONST          1208
                             000000B6     83 - CALL_FUNCTION       r0002
                             000000B9     01 - POP_TOP             
                             000000BA     6E - JUMP_FORWARD        -> 000000BE
                             000000BD     01 - POP_TOP             
                             000000BE     64 - LOAD_CONST          None
                             000000C1     53 - RETURN_VALUE        
                         consts:
00001166                     TUPLE: (
0000116B                         None (4E),
0000116C                         INT: 0 (00 00 00 00),
00001171                         INT: 1208 (B8 04 00 00)
                             )
                         names:
00001176                     TUPLE: (
0000117B                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00001187                         STR: 'PlayerCharacter' (0F 00 00 00 50 6C 61 79 65 72 43 68 61 72 61 63 74 65 72),
0000119B                         STR: 'resuscitate' (0B 00 00 00 72 65 73 75 73 63 69 74 61 74 65),
000011AB                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
000011BA                         STR: 'MaxHealth' (09 00 00 00 4D 61 78 48 65 61 6C 74 68),
000011C8                         STR: 'Health' (06 00 00 00 48 65 61 6C 74 68),
000011D3                         STR: 'takeInnerStrength' (11 00 00 00 74 61 6B 65 49 6E 6E 65 72 53 74 72 65 6E 67 74 68),
000011E9                         STR: 'InnerStrengthMax' (10 00 00 00 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 4D 61 78),
000011FE                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
0000120C                         STR: 'playEffect' (0A 00 00 00 70 6C 61 79 45 66 66 65 63 74),
0000121B                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
00001227                         STR: 'FX' (02 00 00 00 46 58),
0000122E                         STR: 'FX_CHARACTER_RESTORE_RSI' (18 00 00 00 46 58 5F 43 48 41 52 41 43 54 45 52 5F 52 45 53 54 4F 52 45 5F 52 53 49),
0000124B                         STR: 'CharMvt' (07 00 00 00 43 68 61 72 4D 76 74),
00001257                         STR: 'playScript' (0A 00 00 00 70 6C 61 79 53 63 72 69 70 74),
00001266                         STR: 'Stance_Stand' (0C 00 00 00 53 74 61 6E 63 65 5F 53 74 61 6E 64),
00001277                         STR: 'Action_Resurrect' (10 00 00 00 41 63 74 69 6F 6E 5F 52 65 73 75 72 72 65 63 74),
0000128C                         STR: 'ReviveRSIAbility' (10 00 00 00 52 65 76 69 76 65 52 53 49 41 62 69 6C 69 74 79),
000012A1                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000012AD                         STR: 'SendAbilityOutputToTargetMsg' (1C 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 54 61 72 67 65 74 4D 73 67),
000012CE                         STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
000012DE                         STR: 'ID_CLIENT_ABILITY_REZ_DIRECTOBJECT' (22 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 41 42 49 4C 49 54 59 5F 52 45 5A 5F 44 49 52 45 43 54 4F 42 4A 45 43 54),
00001305                         STR: 'RenewRSIAbility' (0F 00 00 00 52 65 6E 65 77 52 53 49 41 62 69 6C 69 74 79),
00001319                         STR: 'msg' (03 00 00 00 6D 73 67),
00001321                         STR: 'SendAbilityOutputToCasterMsg' (1C 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 43 61 73 74 65 72 4D 73 67),
00001342                         STR: 'ID_CLIENT_ABILITY_REZ_SUBJECT' (1D 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 41 42 49 4C 49 54 59 5F 52 45 5A 5F 53 55 42 4A 45 43 54),
00001364                         STR: 'isPvP' (05 00 00 00 69 73 50 76 50),
0000136E                         STR: 'sendApplyAbilityToSelf' (16 00 00 00 73 65 6E 64 41 70 70 6C 79 41 62 69 6C 69 74 79 54 6F 53 65 6C 66),
00001389                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
0000139C                     TUPLE: (
000013A1                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000013AD                         STR: 'msg' (03 00 00 00 6D 73 67)
                             )
                         freevars:
000013B5                     TUPLE: ()
                         cellvars:
000013BA                     TUPLE: ()
                         filename:
000013BF                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\health.py' (4D 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 68 65 61 6C 74 68 2E 70 79)
                         name:
00001411                     STR: 'RenewRSI_DirectObject' (15 00 00 00 52 65 6E 65 77 52 53 49 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
0000142B                     LONG: 123L (7B 00 00 00)
                         lnotab:
0000142F                     STR: '\x00\x01\r\x01\x12\x01\x17\x02\x1f\x01\x16\x02\x16\x01\x16\x01\x10\x01' (12 00 00 00 00 01 0D 01 12 01 17 02 1F 01 16 02 16 01 16 01 10 01),
00001446             TUPLE: (
0000144B                 STR: 'ctime' (05 00 00 00 63 74 69 6D 65)
                     ),
00001455             STR: 'Reloading Health ' (11 00 00 00 52 65 6C 6F 61 64 69 6E 67 20 48 65 61 6C 74 68 20)
                 )
             names:
0000146B         TUPLE: (
00001470             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
0000147B             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00001489             STR: 'obj' (03 00 00 00 6F 62 6A),
00001491             STR: 'missionvalidate' (0F 00 00 00 6D 69 73 73 69 6F 6E 76 61 6C 69 64 61 74 65),
000014A5             STR: 'mv' (02 00 00 00 6D 76),
000014AC             STR: 'combatvalidate' (0E 00 00 00 63 6F 6D 62 61 74 76 61 6C 69 64 61 74 65),
000014BF             STR: 'cv' (02 00 00 00 63 76),
000014C6             STR: 'stringtable_client' (12 00 00 00 73 74 72 69 6E 67 74 61 62 6C 65 5F 63 6C 69 65 6E 74),
000014DD             STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
000014ED             STR: 'ability.utility' (0F 00 00 00 61 62 69 6C 69 74 79 2E 75 74 69 6C 69 74 79),
00001501             STR: 'utility' (07 00 00 00 75 74 69 6C 69 74 79),
0000150D             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00001519             STR: 'ability.defines' (0F 00 00 00 61 62 69 6C 69 74 79 2E 64 65 66 69 6E 65 73),
0000152D             STR: 'ltfxmap' (07 00 00 00 6C 74 66 78 6D 61 70),
00001539             STR: 'FX' (02 00 00 00 46 58),
00001540             STR: 'RequestTime' (0B 00 00 00 52 65 71 75 65 73 74 54 69 6D 65),
00001550             STR: 'RestoreRSI_DirectObject' (17 00 00 00 52 65 73 74 6F 72 65 52 53 49 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
0000156C             STR: 'RestoreRSI_Test' (0F 00 00 00 52 65 73 74 6F 72 65 52 53 49 5F 54 65 73 74),
00001580             STR: 'depAttr' (07 00 00 00 64 65 70 41 74 74 72),
0000158C             STR: 'RevitalizeRSI_DirectObject' (1A 00 00 00 52 65 76 69 74 61 6C 69 7A 65 52 53 49 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
000015AB             STR: 'RejuvenateRSI_DirectObject' (1A 00 00 00 52 65 6A 75 76 65 6E 61 74 65 52 53 49 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
000015CA             STR: 'ReviveRSI_DirectObject' (16 00 00 00 52 65 76 69 76 65 52 53 49 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
000015E5             STR: 'RenewRSI_DirectObject' (15 00 00 00 52 65 6E 65 77 52 53 49 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
000015FF             STR: 'time' (04 00 00 00 74 69 6D 65),
00001608             STR: 'ctime' (05 00 00 00 63 74 69 6D 65)
                 )
             varnames:
00001612         TUPLE: (
00001617             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00001625             STR: 'obj' (03 00 00 00 6F 62 6A),
0000162D             STR: 'RenewRSI_DirectObject' (15 00 00 00 52 65 6E 65 77 52 53 49 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001647             STR: 'RestoreRSI_DirectObject' (17 00 00 00 52 65 73 74 6F 72 65 52 53 49 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001663             STR: 'FX' (02 00 00 00 46 58),
0000166A             STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
0000167A             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00001685             STR: 'ctime' (05 00 00 00 63 74 69 6D 65),
0000168F             STR: 'RestoreRSI_Test' (0F 00 00 00 52 65 73 74 6F 72 65 52 53 49 5F 54 65 73 74),
000016A3             STR: 'RevitalizeRSI_DirectObject' (1A 00 00 00 52 65 76 69 74 61 6C 69 7A 65 52 53 49 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
000016C2             STR: 'mv' (02 00 00 00 6D 76),
000016C9             STR: 'RejuvenateRSI_DirectObject' (1A 00 00 00 52 65 6A 75 76 65 6E 61 74 65 52 53 49 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
000016E8             STR: 'ReviveRSI_DirectObject' (16 00 00 00 52 65 76 69 76 65 52 53 49 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001703             STR: 'RequestTime' (0B 00 00 00 52 65 71 75 65 73 74 54 69 6D 65),
00001713             STR: 'cv' (02 00 00 00 63 76),
0000171A             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79)
                 )
             freevars:
00001726         TUPLE: ()
             cellvars:
0000172B         TUPLE: ()
             filename:
00001730         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\health.py' (4D 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 68 65 61 6C 74 68 2E 70 79)
             name:
00001782         STR: '?' (01 00 00 00 3F)
             firslineno:
00001788         LONG: 5L (05 00 00 00)
             lnotab:
0000178C         STR: '\t\x01\t\x01\t\x03\t\x01\t\x01\t\x01\x0c\x04\x07\x03\t\x08\x06\x03\t\x12\t\x0b\t\t\t\x12\t\x12\t\x12\t\x0e\r\x01' (24 00 00 00 09 01 09 01 09 03 09 01 09 01 09 01 0C 04 07 03 09 08 06 03 09 12 09 0B 09 09 09 12 09 12 09 12 09 0E 0D 01)

