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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00Z\x02\x00d\x00\x00k\x03\x00Z\x04\x00d\x00\x00k\x05\x00Z\x06\x00d\x00\x00k\x07\x00Z\x08\x00d\x00\x00k\t\x00i\n\x00Z\x0b\x00d\x00\x00k\x0c\x00Z\r\x00d\x01\x00k\x0e\x00Td\x02\x00Z\x0f\x00d\x03\x00Z\x10\x00e\r\x00i\x11\x00Z\x12\x00d\x04\x00\x84\x00\x00Z\x13\x00d\x05\x00\x84\x00\x00Z\x14\x00d\x00\x00S' (7D 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 5A 02 00 64 00 00 6B 03 00 5A 04 00 64 00 00 6B 05 00 5A 06 00 64 00 00 6B 07 00 5A 08 00 64 00 00 6B 09 00 69 0A 00 5A 0B 00 64 00 00 6B 0C 00 5A 0D 00 64 01 00 6B 0E 00 54 64 02 00 5A 0F 00 64 03 00 5A 10 00 65 0D 00 69 11 00 5A 12 00 64 04 00 84 00 00 5A 13 00 64 05 00 84 00 00 5A 14 00 64 00 00 53)
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
                 00000042     64 - LOAD_CONST          None
                 00000045     6B - IMPORT_NAME         'ltfxmap'
                 00000048     5A - STORE_NAME          'FX'
                 0000004B     64 - LOAD_CONST          ('*')
                 0000004E     6B - IMPORT_NAME         'ability.defines'
                 00000051     54 - IMPORT_STAR         
                 00000052     64 - LOAD_CONST          12
                 00000055     5A - STORE_NAME          'SYNAPTIC_SWEEP_KICK_DAMAGE_MIN'
                 00000058     64 - LOAD_CONST          48
                 0000005B     5A - STORE_NAME          'SYNAPTIC_SWEEP_KICK_DAMAGE_MAX'
                 0000005E     65 - LOAD_NAME           'FX'
                 00000061     69 - LOAD_ATTR           'FX_CHARACTER_SYNAPTIC_SWEEP_KICK'
                 00000064     5A - STORE_NAME          'SYNAPTIC_SWEEP_KICK_FX'
                 00000067     64 - LOAD_CONST          CODE('SynapticSweepKick_DirectObject')
                 0000006A     84 - MAKE_FUNCTION       r0000
                 0000006D     5A - STORE_NAME          'SynapticSweepKick_DirectObject'
                 00000070     64 - LOAD_CONST          CODE('SynapticSweepKick_Subject')
                 00000073     84 - MAKE_FUNCTION       r0000
                 00000076     5A - STORE_NAME          'SynapticSweepKick_Subject'
                 00000079     64 - LOAD_CONST          None
                 0000007C     53 - RETURN_VALUE        
             consts:
0000009B         TUPLE: (
000000A0             None (4E),
000000A1             TUPLE: (
000000A6                 STR: '*' (01 00 00 00 2A)
                     ),
000000AC             INT: 12 (0C 00 00 00),
000000B1             INT: 48 (30 00 00 00),
000000B6             CODE:
                         argcount:
000000B7                     LONG: 2L (02 00 00 00)
                         nlocals:
000000BB                     LONG: 3L (03 00 00 00)
                         stacksize:
000000BF                     LONG: 6L (06 00 00 00)
                         flags:
000000C3                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000000C7                     STR: 't\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01|\x00\x00i\x03\x00i\x04\x00|\x01\x00i\x06\x00\x83\x01\x00\x0co\x08\x00\x01d\x00\x00Sn\x01\x00\x01t\x07\x00i\x08\x00t\t\x00t\n\x00\x83\x02\x00}\x02\x00t\x00\x00i\x01\x00d\x02\x00|\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x0c\x00i\r\x00|\x01\x00i\x06\x00|\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\x0e\x00t\x0f\x00t\x10\x00|\x01\x00i\x06\x00|\x01\x00i\x11\x00|\x02\x00\x83\x05\x00\x01t\x12\x00i\x13\x00|\x00\x00i\x14\x00|\x00\x00i\x14\x00t\x15\x00d\x03\x00\x83\x04\x00\x01d\x00\x00S' (A6 00 00 00 74 00 00 69 01 00 64 01 00 83 01 00 01 7C 00 00 69 03 00 69 04 00 7C 01 00 69 06 00 83 01 00 0C 6F 08 00 01 64 00 00 53 6E 01 00 01 74 07 00 69 08 00 74 09 00 74 0A 00 83 02 00 7D 02 00 74 00 00 69 01 00 64 02 00 7C 02 00 16 83 01 00 01 7C 00 00 69 0C 00 69 0D 00 7C 01 00 69 06 00 7C 02 00 83 02 00 7D 02 00 74 00 00 69 0E 00 74 0F 00 74 10 00 7C 01 00 69 06 00 7C 01 00 69 11 00 7C 02 00 83 05 00 01 74 12 00 69 13 00 7C 00 00 69 14 00 7C 00 00 69 14 00 74 15 00 64 03 00 83 04 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'SynapticSweepKick_DirectObject:'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     01 - POP_TOP             
                             0000000D     7C - LOAD_FAST           'subject'
                             00000010     69 - LOAD_ATTR           'CharMvt'
                             00000013     69 - LOAD_ATTR           'isEnemy'
                             00000016     7C - LOAD_FAST           'msg'
                             00000019     69 - LOAD_ATTR           'subjectLocator'
                             0000001C     83 - CALL_FUNCTION       r0001
                             0000001F     0C - UNARY_NOT           
                             00000020     6F - JUMP_IF_FALSE       -> 0000002B
                             00000023     01 - POP_TOP             
                             00000024     64 - LOAD_CONST          None
                             00000027     53 - RETURN_VALUE        
                             00000028     6E - JUMP_FORWARD        -> 0000002C
                             0000002B     01 - POP_TOP             
                             0000002C     74 - LOAD_GLOBAL         'random'
                             0000002F     69 - LOAD_ATTR           'randrange'
                             00000032     74 - LOAD_GLOBAL         'SYNAPTIC_SWEEP_KICK_DAMAGE_MIN'
                             00000035     74 - LOAD_GLOBAL         'SYNAPTIC_SWEEP_KICK_DAMAGE_MAX'
                             00000038     83 - CALL_FUNCTION       r0002
                             0000003B     7D - STORE_FAST          'damage'
                             0000003E     74 - LOAD_GLOBAL         'Utility'
                             00000041     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000044     64 - LOAD_CONST          'SynapticSweepKick_DirectObject: %d damage dealt'
                             00000047     7C - LOAD_FAST           'damage'
                             0000004A     16 - BINARY_MODULO       
                             0000004B     83 - CALL_FUNCTION       r0001
                             0000004E     01 - POP_TOP             
                             0000004F     7C - LOAD_FAST           'subject'
                             00000052     69 - LOAD_ATTR           'Interlock'
                             00000055     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             00000058     7C - LOAD_FAST           'msg'
                             0000005B     69 - LOAD_ATTR           'subjectLocator'
                             0000005E     7C - LOAD_FAST           'damage'
                             00000061     83 - CALL_FUNCTION       r0002
                             00000064     7D - STORE_FAST          'damage'
                             00000067     74 - LOAD_GLOBAL         'Utility'
                             0000006A     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000006D     74 - LOAD_GLOBAL         'SUCCESS'
                             00000070     74 - LOAD_GLOBAL         'SynapticSweepKickAbility'
                             00000073     7C - LOAD_FAST           'msg'
                             00000076     69 - LOAD_ATTR           'subjectLocator'
                             00000079     7C - LOAD_FAST           'msg'
                             0000007C     69 - LOAD_ATTR           'directObjectLocator'
                             0000007F     7C - LOAD_FAST           'damage'
                             00000082     83 - CALL_FUNCTION       r0005
                             00000085     01 - POP_TOP             
                             00000086     74 - LOAD_GLOBAL         'discovery'
                             00000089     69 - LOAD_ATTR           'playEffect'
                             0000008C     7C - LOAD_FAST           'subject'
                             0000008F     69 - LOAD_ATTR           'locator'
                             00000092     7C - LOAD_FAST           'subject'
                             00000095     69 - LOAD_ATTR           'locator'
                             00000098     74 - LOAD_GLOBAL         'SYNAPTIC_SWEEP_KICK_FX'
                             0000009B     64 - LOAD_CONST          0
                             0000009E     83 - CALL_FUNCTION       r0004
                             000000A1     01 - POP_TOP             
                             000000A2     64 - LOAD_CONST          None
                             000000A5     53 - RETURN_VALUE        
                         consts:
00000172                     TUPLE: (
00000177                         None (4E),
00000178                         STR: 'SynapticSweepKick_DirectObject:' (1F 00 00 00 53 79 6E 61 70 74 69 63 53 77 65 65 70 4B 69 63 6B 5F 44 69 72 65 63 74 4F 62 6A 65 63 74 3A),
0000019C                         STR: 'SynapticSweepKick_DirectObject: %d damage dealt' (2F 00 00 00 53 79 6E 61 70 74 69 63 53 77 65 65 70 4B 69 63 6B 5F 44 69 72 65 63 74 4F 62 6A 65 63 74 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74),
000001D0                         INT: 0 (00 00 00 00)
                             )
                         names:
000001D5                     TUPLE: (
000001DA                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000001E6                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
000001FD                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000209                         STR: 'CharMvt' (07 00 00 00 43 68 61 72 4D 76 74),
00000215                         STR: 'isEnemy' (07 00 00 00 69 73 45 6E 65 6D 79),
00000221                         STR: 'msg' (03 00 00 00 6D 73 67),
00000229                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
0000023C                         STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00000247                         STR: 'randrange' (09 00 00 00 72 61 6E 64 72 61 6E 67 65),
00000255                         STR: 'SYNAPTIC_SWEEP_KICK_DAMAGE_MIN' (1E 00 00 00 53 59 4E 41 50 54 49 43 5F 53 57 45 45 50 5F 4B 49 43 4B 5F 44 41 4D 41 47 45 5F 4D 49 4E),
00000278                         STR: 'SYNAPTIC_SWEEP_KICK_DAMAGE_MAX' (1E 00 00 00 53 59 4E 41 50 54 49 43 5F 53 57 45 45 50 5F 4B 49 43 4B 5F 44 41 4D 41 47 45 5F 4D 41 58),
0000029B                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
000002A6                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
000002B4                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
000002D2                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
000002F0                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
000002FC                         STR: 'SynapticSweepKickAbility' (18 00 00 00 53 79 6E 61 70 74 69 63 53 77 65 65 70 4B 69 63 6B 41 62 69 6C 69 74 79),
00000319                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00000331                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
0000033F                         STR: 'playEffect' (0A 00 00 00 70 6C 61 79 45 66 66 65 63 74),
0000034E                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
0000035A                         STR: 'SYNAPTIC_SWEEP_KICK_FX' (16 00 00 00 53 59 4E 41 50 54 49 43 5F 53 57 45 45 50 5F 4B 49 43 4B 5F 46 58)
                             )
                         varnames:
00000375                     TUPLE: (
0000037A                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000386                         STR: 'msg' (03 00 00 00 6D 73 67),
0000038E                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00000399                     TUPLE: ()
                         cellvars:
0000039E                     TUPLE: ()
                         filename:
000003A3                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\misc.py' (4C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6D 69 73 63 2E 70 79)
                         name:
000003F4                     STR: 'SynapticSweepKick_DirectObject' (1E 00 00 00 53 79 6E 61 70 74 69 63 53 77 65 65 70 4B 69 63 6B 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000417                     LONG: 31L (1F 00 00 00)
                         lnotab:
0000041B                     STR: '\x00\x02\r\x02\x17\x01\x08\x02\x12\x01\x11\x03\x18\x01\x1f\x02' (10 00 00 00 00 02 0D 02 17 01 08 02 12 01 11 03 18 01 1F 02),
00000430             CODE:
                         argcount:
00000431                     LONG: 2L (02 00 00 00)
                         nlocals:
00000435                     LONG: 3L (03 00 00 00)
                         stacksize:
00000439                     LONG: 7L (07 00 00 00)
                         flags:
0000043D                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000441                     STR: 't\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01|\x00\x00i\x03\x00i\x04\x00}\x02\x00|\x00\x00i\x06\x00i\x07\x00t\x08\x00t\t\x00|\x02\x00i\n\x00|\x02\x00i\x0b\x00|\x02\x00i\x0c\x00d\x02\x00\x83\x06\x00\x01|\x00\x00i\r\x00\x0co\x1a\x00\x01|\x00\x00i\x03\x00i\x0e\x00t\x0f\x00t\x10\x00t\x08\x00\x83\x03\x00\x01n\x01\x00\x01d\x00\x00S' (6A 00 00 00 74 00 00 69 01 00 64 01 00 83 01 00 01 7C 00 00 69 03 00 69 04 00 7D 02 00 7C 00 00 69 06 00 69 07 00 74 08 00 74 09 00 7C 02 00 69 0A 00 7C 02 00 69 0B 00 7C 02 00 69 0C 00 64 02 00 83 06 00 01 7C 00 00 69 0D 00 0C 6F 1A 00 01 7C 00 00 69 03 00 69 0E 00 74 0F 00 74 10 00 74 08 00 83 03 00 01 6E 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'SynapticSweepKick_Subject  : '
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     01 - POP_TOP             
                             0000000D     7C - LOAD_FAST           'subject'
                             00000010     69 - LOAD_ATTR           'CharMvt'
                             00000013     69 - LOAD_ATTR           'Position'
                             00000016     7D - STORE_FAST          'loc'
                             00000019     7C - LOAD_FAST           'subject'
                             0000001C     69 - LOAD_ATTR           'AbilityInv'
                             0000001F     69 - LOAD_ATTR           'applyAbilityToArea'
                             00000022     74 - LOAD_GLOBAL         'SynapticSweepKickAbility'
                             00000025     74 - LOAD_GLOBAL         'SUCCESS'
                             00000028     7C - LOAD_FAST           'loc'
                             0000002B     69 - LOAD_ATTR           'x'
                             0000002E     7C - LOAD_FAST           'loc'
                             00000031     69 - LOAD_ATTR           'y'
                             00000034     7C - LOAD_FAST           'loc'
                             00000037     69 - LOAD_ATTR           'z'
                             0000003A     64 - LOAD_CONST          400
                             0000003D     83 - CALL_FUNCTION       r0006
                             00000040     01 - POP_TOP             
                             00000041     7C - LOAD_FAST           'subject'
                             00000044     69 - LOAD_ATTR           'isInCombat'
                             00000047     0C - UNARY_NOT           
                             00000048     6F - JUMP_IF_FALSE       -> 00000065
                             0000004B     01 - POP_TOP             
                             0000004C     7C - LOAD_FAST           'subject'
                             0000004F     69 - LOAD_ATTR           'CharMvt'
                             00000052     69 - LOAD_ATTR           'playScript'
                             00000055     74 - LOAD_GLOBAL         'Stance_Stand'
                             00000058     74 - LOAD_GLOBAL         'Action_SweepKick'
                             0000005B     74 - LOAD_GLOBAL         'SynapticSweepKickAbility'
                             0000005E     83 - CALL_FUNCTION       r0003
                             00000061     01 - POP_TOP             
                             00000062     6E - JUMP_FORWARD        -> 00000066
                             00000065     01 - POP_TOP             
                             00000066     64 - LOAD_CONST          None
                             00000069     53 - RETURN_VALUE        
                         consts:
000004B0                     TUPLE: (
000004B5                         None (4E),
000004B6                         STR: 'SynapticSweepKick_Subject  : ' (1D 00 00 00 53 79 6E 61 70 74 69 63 53 77 65 65 70 4B 69 63 6B 5F 53 75 62 6A 65 63 74 20 20 3A 20),
000004D8                         INT: 400 (90 01 00 00)
                             )
                         names:
000004DD                     TUPLE: (
000004E2                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000004EE                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000505                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000511                         STR: 'CharMvt' (07 00 00 00 43 68 61 72 4D 76 74),
0000051D                         STR: 'Position' (08 00 00 00 50 6F 73 69 74 69 6F 6E),
0000052A                         STR: 'loc' (03 00 00 00 6C 6F 63),
00000532                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
00000541                         STR: 'applyAbilityToArea' (12 00 00 00 61 70 70 6C 79 41 62 69 6C 69 74 79 54 6F 41 72 65 61),
00000558                         STR: 'SynapticSweepKickAbility' (18 00 00 00 53 79 6E 61 70 74 69 63 53 77 65 65 70 4B 69 63 6B 41 62 69 6C 69 74 79),
00000575                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00000581                         STR: 'x' (01 00 00 00 78),
00000587                         STR: 'y' (01 00 00 00 79),
0000058D                         STR: 'z' (01 00 00 00 7A),
00000593                         STR: 'isInCombat' (0A 00 00 00 69 73 49 6E 43 6F 6D 62 61 74),
000005A2                         STR: 'playScript' (0A 00 00 00 70 6C 61 79 53 63 72 69 70 74),
000005B1                         STR: 'Stance_Stand' (0C 00 00 00 53 74 61 6E 63 65 5F 53 74 61 6E 64),
000005C2                         STR: 'Action_SweepKick' (10 00 00 00 41 63 74 69 6F 6E 5F 53 77 65 65 70 4B 69 63 6B)
                             )
                         varnames:
000005D7                     TUPLE: (
000005DC                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000005E8                         STR: 'msg' (03 00 00 00 6D 73 67),
000005F0                         STR: 'loc' (03 00 00 00 6C 6F 63)
                             )
                         freevars:
000005F8                     TUPLE: ()
                         cellvars:
000005FD                     TUPLE: ()
                         filename:
00000602                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\misc.py' (4C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6D 69 73 63 2E 70 79)
                         name:
00000653                     STR: 'SynapticSweepKick_Subject' (19 00 00 00 53 79 6E 61 70 74 69 63 53 77 65 65 70 4B 69 63 6B 5F 53 75 62 6A 65 63 74)
                         firslineno:
00000671                     LONG: 48L (30 00 00 00)
                         lnotab:
00000675                     STR: '\x00\x01\r\x02\x0c\x01(\x03\x0b\x01' (0A 00 00 00 00 01 0D 02 0C 01 28 03 0B 01)
                 )
             names:
00000684         TUPLE: (
00000689             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00000694             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
000006A2             STR: 'obj' (03 00 00 00 6F 62 6A),
000006AA             STR: 'missionvalidate' (0F 00 00 00 6D 69 73 73 69 6F 6E 76 61 6C 69 64 61 74 65),
000006BE             STR: 'mv' (02 00 00 00 6D 76),
000006C5             STR: 'combatvalidate' (0E 00 00 00 63 6F 6D 62 61 74 76 61 6C 69 64 61 74 65),
000006D8             STR: 'cv' (02 00 00 00 63 76),
000006DF             STR: 'stringtable_client' (12 00 00 00 73 74 72 69 6E 67 74 61 62 6C 65 5F 63 6C 69 65 6E 74),
000006F6             STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00000706             STR: 'ability.utility' (0F 00 00 00 61 62 69 6C 69 74 79 2E 75 74 69 6C 69 74 79),
0000071A             STR: 'utility' (07 00 00 00 75 74 69 6C 69 74 79),
00000726             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000732             STR: 'ltfxmap' (07 00 00 00 6C 74 66 78 6D 61 70),
0000073E             STR: 'FX' (02 00 00 00 46 58),
00000745             STR: 'ability.defines' (0F 00 00 00 61 62 69 6C 69 74 79 2E 64 65 66 69 6E 65 73),
00000759             STR: 'SYNAPTIC_SWEEP_KICK_DAMAGE_MIN' (1E 00 00 00 53 59 4E 41 50 54 49 43 5F 53 57 45 45 50 5F 4B 49 43 4B 5F 44 41 4D 41 47 45 5F 4D 49 4E),
0000077C             STR: 'SYNAPTIC_SWEEP_KICK_DAMAGE_MAX' (1E 00 00 00 53 59 4E 41 50 54 49 43 5F 53 57 45 45 50 5F 4B 49 43 4B 5F 44 41 4D 41 47 45 5F 4D 41 58),
0000079F             STR: 'FX_CHARACTER_SYNAPTIC_SWEEP_KICK' (20 00 00 00 46 58 5F 43 48 41 52 41 43 54 45 52 5F 53 59 4E 41 50 54 49 43 5F 53 57 45 45 50 5F 4B 49 43 4B),
000007C4             STR: 'SYNAPTIC_SWEEP_KICK_FX' (16 00 00 00 53 59 4E 41 50 54 49 43 5F 53 57 45 45 50 5F 4B 49 43 4B 5F 46 58),
000007DF             STR: 'SynapticSweepKick_DirectObject' (1E 00 00 00 53 79 6E 61 70 74 69 63 53 77 65 65 70 4B 69 63 6B 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00000802             STR: 'SynapticSweepKick_Subject' (19 00 00 00 53 79 6E 61 70 74 69 63 53 77 65 65 70 4B 69 63 6B 5F 53 75 62 6A 65 63 74)
                 )
             varnames:
00000820         TUPLE: (
00000825             STR: 'SynapticSweepKick_Subject' (19 00 00 00 53 79 6E 61 70 74 69 63 53 77 65 65 70 4B 69 63 6B 5F 53 75 62 6A 65 63 74),
00000843             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00000851             STR: 'obj' (03 00 00 00 6F 62 6A),
00000859             STR: 'SYNAPTIC_SWEEP_KICK_DAMAGE_MIN' (1E 00 00 00 53 59 4E 41 50 54 49 43 5F 53 57 45 45 50 5F 4B 49 43 4B 5F 44 41 4D 41 47 45 5F 4D 49 4E),
0000087C             STR: 'FX' (02 00 00 00 46 58),
00000883             STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00000893             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
0000089E             STR: 'SYNAPTIC_SWEEP_KICK_FX' (16 00 00 00 53 59 4E 41 50 54 49 43 5F 53 57 45 45 50 5F 4B 49 43 4B 5F 46 58),
000008B9             STR: 'SYNAPTIC_SWEEP_KICK_DAMAGE_MAX' (1E 00 00 00 53 59 4E 41 50 54 49 43 5F 53 57 45 45 50 5F 4B 49 43 4B 5F 44 41 4D 41 47 45 5F 4D 41 58),
000008DC             STR: 'mv' (02 00 00 00 6D 76),
000008E3             STR: 'SynapticSweepKick_DirectObject' (1E 00 00 00 53 79 6E 61 70 74 69 63 53 77 65 65 70 4B 69 63 6B 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00000906             STR: 'cv' (02 00 00 00 63 76),
0000090D             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79)
                 )
             freevars:
00000919         TUPLE: ()
             cellvars:
0000091E         TUPLE: ()
             filename:
00000923         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\misc.py' (4C 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6D 69 73 63 2E 70 79)
             name:
00000974         STR: '?' (01 00 00 00 3F)
             firslineno:
0000097A         LONG: 1L (01 00 00 00)
             lnotab:
0000097E         STR: '\t\x01\t\x01\t\x03\t\x01\t\x01\t\x01\x0c\x01\t\x03\x07\x06\x06\x01\x06\x05\t\x06\t\x11' (1A 00 00 00 09 01 09 01 09 03 09 01 09 01 09 01 0C 01 09 03 07 06 06 01 06 05 09 06 09 11)

