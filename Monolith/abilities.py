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
00000019         STR: 'd\x00\x00\x84\x00\x00Z\x00\x00d\x01\x00\x84\x00\x00Z\x01\x00d\x02\x00S' (16 00 00 00 64 00 00 84 00 00 5A 00 00 64 01 00 84 00 00 5A 01 00 64 02 00 53)
                 00000000     64 - LOAD_CONST          CODE('GetImportObjects')
                 00000003     84 - MAKE_FUNCTION       r0000
                 00000006     5A - STORE_NAME          'GetImportObjects'
                 00000009     64 - LOAD_CONST          CODE('abilitiesSuccess')
                 0000000C     84 - MAKE_FUNCTION       r0000
                 0000000F     5A - STORE_NAME          'abilitiesSuccess'
                 00000012     64 - LOAD_CONST          None
                 00000015     53 - RETURN_VALUE        
             consts:
00000034         TUPLE: (
00000039             CODE:
                         argcount:
0000003A                     LONG: 0L (00 00 00 00)
                         nlocals:
0000003E                     LONG: 1L (01 00 00 00)
                         stacksize:
00000042                     LONG: 2L (02 00 00 00)
                         flags:
00000046                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000004A                     STR: 'g\x00\x00}\x00\x00|\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01|\x00\x00i\x01\x00d\x02\x00\x83\x01\x00\x01|\x00\x00i\x01\x00d\x03\x00\x83\x01\x00\x01|\x00\x00i\x01\x00d\x04\x00\x83\x01\x00\x01|\x00\x00i\x01\x00d\x05\x00\x83\x01\x00\x01|\x00\x00i\x01\x00d\x06\x00\x83\x01\x00\x01|\x00\x00i\x01\x00d\x07\x00\x83\x01\x00\x01|\x00\x00i\x01\x00d\x08\x00\x83\x01\x00\x01|\x00\x00i\x01\x00d\t\x00\x83\x01\x00\x01|\x00\x00i\x01\x00d\n\x00\x83\x01\x00\x01|\x00\x00i\x01\x00d\x0b\x00\x83\x01\x00\x01|\x00\x00i\x01\x00d\x0c\x00\x83\x01\x00\x01|\x00\x00Sd\x00\x00S' (AA 00 00 00 67 00 00 7D 00 00 7C 00 00 69 01 00 64 01 00 83 01 00 01 7C 00 00 69 01 00 64 02 00 83 01 00 01 7C 00 00 69 01 00 64 03 00 83 01 00 01 7C 00 00 69 01 00 64 04 00 83 01 00 01 7C 00 00 69 01 00 64 05 00 83 01 00 01 7C 00 00 69 01 00 64 06 00 83 01 00 01 7C 00 00 69 01 00 64 07 00 83 01 00 01 7C 00 00 69 01 00 64 08 00 83 01 00 01 7C 00 00 69 01 00 64 09 00 83 01 00 01 7C 00 00 69 01 00 64 0A 00 83 01 00 01 7C 00 00 69 01 00 64 0B 00 83 01 00 01 7C 00 00 69 01 00 64 0C 00 83 01 00 01 7C 00 00 53 64 00 00 53)
                             00000000     67 - BUILD_LIST          r0000
                             00000003     7D - STORE_FAST          'importList'
                             00000006     7C - LOAD_FAST           'importList'
                             00000009     69 - LOAD_ATTR           'append'
                             0000000C     64 - LOAD_CONST          'ability.general'
                             0000000F     83 - CALL_FUNCTION       r0001
                             00000012     01 - POP_TOP             
                             00000013     7C - LOAD_FAST           'importList'
                             00000016     69 - LOAD_ATTR           'append'
                             00000019     64 - LOAD_CONST          'ability.effects'
                             0000001C     83 - CALL_FUNCTION       r0001
                             0000001F     01 - POP_TOP             
                             00000020     7C - LOAD_FAST           'importList'
                             00000023     69 - LOAD_ATTR           'append'
                             00000026     64 - LOAD_CONST          'ability.spy.sneaks'
                             00000029     83 - CALL_FUNCTION       r0001
                             0000002C     01 - POP_TOP             
                             0000002D     7C - LOAD_FAST           'importList'
                             00000030     69 - LOAD_ATTR           'append'
                             00000033     64 - LOAD_CONST          'ability.spy.misc'
                             00000036     83 - CALL_FUNCTION       r0001
                             00000039     01 - POP_TOP             
                             0000003A     7C - LOAD_FAST           'importList'
                             0000003D     69 - LOAD_ATTR           'append'
                             00000040     64 - LOAD_CONST          'ability.hacker.virii'
                             00000043     83 - CALL_FUNCTION       r0001
                             00000046     01 - POP_TOP             
                             00000047     7C - LOAD_FAST           'importList'
                             0000004A     69 - LOAD_ATTR           'append'
                             0000004D     64 - LOAD_CONST          'ability.hacker.health'
                             00000050     83 - CALL_FUNCTION       r0001
                             00000053     01 - POP_TOP             
                             00000054     7C - LOAD_FAST           'importList'
                             00000057     69 - LOAD_ATTR           'append'
                             0000005A     64 - LOAD_CONST          'ability.hacker.misc'
                             0000005D     83 - CALL_FUNCTION       r0001
                             00000060     01 - POP_TOP             
                             00000061     7C - LOAD_FAST           'importList'
                             00000064     69 - LOAD_ATTR           'append'
                             00000067     64 - LOAD_CONST          'ability.hacker.simulacra'
                             0000006A     83 - CALL_FUNCTION       r0001
                             0000006D     01 - POP_TOP             
                             0000006E     7C - LOAD_FAST           'importList'
                             00000071     69 - LOAD_ATTR           'append'
                             00000074     64 - LOAD_CONST          'ability.hacker.crafting'
                             00000077     83 - CALL_FUNCTION       r0001
                             0000007A     01 - POP_TOP             
                             0000007B     7C - LOAD_FAST           'importList'
                             0000007E     69 - LOAD_ATTR           'append'
                             00000081     64 - LOAD_CONST          'ability.soldier.misc'
                             00000084     83 - CALL_FUNCTION       r0001
                             00000087     01 - POP_TOP             
                             00000088     7C - LOAD_FAST           'importList'
                             0000008B     69 - LOAD_ATTR           'append'
                             0000008E     64 - LOAD_CONST          'ability.npc.specialmoves'
                             00000091     83 - CALL_FUNCTION       r0001
                             00000094     01 - POP_TOP             
                             00000095     7C - LOAD_FAST           'importList'
                             00000098     69 - LOAD_ATTR           'append'
                             0000009B     64 - LOAD_CONST          'generic_free_attacks'
                             0000009E     83 - CALL_FUNCTION       r0001
                             000000A1     01 - POP_TOP             
                             000000A2     7C - LOAD_FAST           'importList'
                             000000A5     53 - RETURN_VALUE        
                             000000A6     64 - LOAD_CONST          None
                             000000A9     53 - RETURN_VALUE        
                         consts:
000000F9                     TUPLE: (
000000FE                         None (4E),
000000FF                         STR: 'ability.general' (0F 00 00 00 61 62 69 6C 69 74 79 2E 67 65 6E 65 72 61 6C),
00000113                         STR: 'ability.effects' (0F 00 00 00 61 62 69 6C 69 74 79 2E 65 66 66 65 63 74 73),
00000127                         STR: 'ability.spy.sneaks' (12 00 00 00 61 62 69 6C 69 74 79 2E 73 70 79 2E 73 6E 65 61 6B 73),
0000013E                         STR: 'ability.spy.misc' (10 00 00 00 61 62 69 6C 69 74 79 2E 73 70 79 2E 6D 69 73 63),
00000153                         STR: 'ability.hacker.virii' (14 00 00 00 61 62 69 6C 69 74 79 2E 68 61 63 6B 65 72 2E 76 69 72 69 69),
0000016C                         STR: 'ability.hacker.health' (15 00 00 00 61 62 69 6C 69 74 79 2E 68 61 63 6B 65 72 2E 68 65 61 6C 74 68),
00000186                         STR: 'ability.hacker.misc' (13 00 00 00 61 62 69 6C 69 74 79 2E 68 61 63 6B 65 72 2E 6D 69 73 63),
0000019E                         STR: 'ability.hacker.simulacra' (18 00 00 00 61 62 69 6C 69 74 79 2E 68 61 63 6B 65 72 2E 73 69 6D 75 6C 61 63 72 61),
000001BB                         STR: 'ability.hacker.crafting' (17 00 00 00 61 62 69 6C 69 74 79 2E 68 61 63 6B 65 72 2E 63 72 61 66 74 69 6E 67),
000001D7                         STR: 'ability.soldier.misc' (14 00 00 00 61 62 69 6C 69 74 79 2E 73 6F 6C 64 69 65 72 2E 6D 69 73 63),
000001F0                         STR: 'ability.npc.specialmoves' (18 00 00 00 61 62 69 6C 69 74 79 2E 6E 70 63 2E 73 70 65 63 69 61 6C 6D 6F 76 65 73),
0000020D                         STR: 'generic_free_attacks' (14 00 00 00 67 65 6E 65 72 69 63 5F 66 72 65 65 5F 61 74 74 61 63 6B 73)
                             )
                         names:
00000226                     TUPLE: (
0000022B                         STR: 'importList' (0A 00 00 00 69 6D 70 6F 72 74 4C 69 73 74),
0000023A                         STR: 'append' (06 00 00 00 61 70 70 65 6E 64)
                             )
                         varnames:
00000245                     TUPLE: (
0000024A                         STR: 'importList' (0A 00 00 00 69 6D 70 6F 72 74 4C 69 73 74)
                             )
                         freevars:
00000259                     TUPLE: ()
                         cellvars:
0000025E                     TUPLE: ()
                         filename:
00000263                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\abilities.py' (41 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 69 65 73 2E 70 79)
                         name:
000002A9                     STR: 'GetImportObjects' (10 00 00 00 47 65 74 49 6D 70 6F 72 74 4F 62 6A 65 63 74 73)
                         firslineno:
000002BE                     LONG: 10L (0A 00 00 00)
                         lnotab:
000002C2                     STR: '\x00\x01\x06\x03\r\x02\r\x03\r\x01\r\x03\r\x01\r\x01\r\x01\r\x01\r\x03\r\x03\r\x03\r\x02' (1C 00 00 00 00 01 06 03 0D 02 0D 03 0D 01 0D 03 0D 01 0D 01 0D 01 0D 01 0D 03 0D 03 0D 03 0D 02),
000002E3             CODE:
                         argcount:
000002E4                     LONG: 0L (00 00 00 00)
                         nlocals:
000002E8                     LONG: 0L (00 00 00 00)
                         stacksize:
000002EC                     LONG: 2L (02 00 00 00)
                         flags:
000002F0                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000002F4                     STR: 't\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01t\x00\x00i\x01\x00d\x02\x00\x83\x01\x00\x01t\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01t\x00\x00i\x02\x00d\x03\x00\x83\x01\x00\x01d\x00\x00S' (38 00 00 00 74 00 00 69 01 00 64 01 00 83 01 00 01 74 00 00 69 01 00 64 02 00 83 01 00 01 74 00 00 69 01 00 64 01 00 83 01 00 01 74 00 00 69 02 00 64 03 00 83 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'discovery'
                             00000003     69 - LOAD_ATTR           'outputDebugString'
                             00000006     64 - LOAD_CONST          '-------------------------------------------------\n'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     01 - POP_TOP             
                             0000000D     74 - LOAD_GLOBAL         'discovery'
                             00000010     69 - LOAD_ATTR           'outputDebugString'
                             00000013     64 - LOAD_CONST          'python- abilities system loaded.\n'
                             00000016     83 - CALL_FUNCTION       r0001
                             00000019     01 - POP_TOP             
                             0000001A     74 - LOAD_GLOBAL         'discovery'
                             0000001D     69 - LOAD_ATTR           'outputDebugString'
                             00000020     64 - LOAD_CONST          '-------------------------------------------------\n'
                             00000023     83 - CALL_FUNCTION       r0001
                             00000026     01 - POP_TOP             
                             00000027     74 - LOAD_GLOBAL         'discovery'
                             0000002A     69 - LOAD_ATTR           'serverPrint'
                             0000002D     64 - LOAD_CONST          'SP: Abilities System Functioning'
                             00000030     83 - CALL_FUNCTION       r0001
                             00000033     01 - POP_TOP             
                             00000034     64 - LOAD_CONST          None
                             00000037     53 - RETURN_VALUE        
                         consts:
00000331                     TUPLE: (
00000336                         None (4E),
00000337                         STR: '-------------------------------------------------\n' (32 00 00 00 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 0A),
0000036E                         STR: 'python- abilities system loaded.\n' (21 00 00 00 70 79 74 68 6F 6E 2D 20 61 62 69 6C 69 74 69 65 73 20 73 79 73 74 65 6D 20 6C 6F 61 64 65 64 2E 0A),
00000394                         STR: 'SP: Abilities System Functioning' (20 00 00 00 53 50 3A 20 41 62 69 6C 69 74 69 65 73 20 53 79 73 74 65 6D 20 46 75 6E 63 74 69 6F 6E 69 6E 67)
                             )
                         names:
000003B9                     TUPLE: (
000003BE                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
000003CC                         STR: 'outputDebugString' (11 00 00 00 6F 75 74 70 75 74 44 65 62 75 67 53 74 72 69 6E 67),
000003E2                         STR: 'serverPrint' (0B 00 00 00 73 65 72 76 65 72 50 72 69 6E 74)
                             )
                         varnames:
000003F2                     TUPLE: ()
                         freevars:
000003F7                     TUPLE: ()
                         cellvars:
000003FC                     TUPLE: ()
                         filename:
00000401                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\abilities.py' (41 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 69 65 73 2E 70 79)
                         name:
00000447                     STR: 'abilitiesSuccess' (10 00 00 00 61 62 69 6C 69 74 69 65 73 53 75 63 63 65 73 73)
                         firslineno:
0000045C                     LONG: 46L (2E 00 00 00)
                         lnotab:
00000460                     STR: '\x00\x01\r\x01\r\x01\r\x01' (08 00 00 00 00 01 0D 01 0D 01 0D 01),
0000046D             None (4E)
                 )
             names:
0000046E         TUPLE: (
00000473             STR: 'GetImportObjects' (10 00 00 00 47 65 74 49 6D 70 6F 72 74 4F 62 6A 65 63 74 73),
00000488             STR: 'abilitiesSuccess' (10 00 00 00 61 62 69 6C 69 74 69 65 73 53 75 63 63 65 73 73)
                 )
             varnames:
0000049D         TUPLE: (
000004A2             STR: 'abilitiesSuccess' (10 00 00 00 61 62 69 6C 69 74 69 65 73 53 75 63 63 65 73 73),
000004B7             STR: 'GetImportObjects' (10 00 00 00 47 65 74 49 6D 70 6F 72 74 4F 62 6A 65 63 74 73)
                 )
             freevars:
000004CC         TUPLE: ()
             cellvars:
000004D1         TUPLE: ()
             filename:
000004D6         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\abilities.py' (41 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 69 65 73 2E 70 79)
             name:
0000051C         STR: '?' (01 00 00 00 3F)
             firslineno:
00000522         LONG: 10L (0A 00 00 00)
             lnotab:
00000526         STR: '\t$' (02 00 00 00 09 24)

