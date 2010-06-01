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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00Z\x02\x00d\x00\x00k\x03\x00Z\x04\x00d\x01\x00\x84\x00\x00Z\x05\x00d\x02\x00e\x05\x00_\x06\x00d\x03\x00\x84\x00\x00Z\x07\x00d\x04\x00e\x07\x00_\x06\x00d\x00\x00S' (4C 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 5A 02 00 64 00 00 6B 03 00 5A 04 00 64 01 00 84 00 00 5A 05 00 64 02 00 65 05 00 5F 06 00 64 03 00 84 00 00 5A 07 00 64 04 00 65 07 00 5F 06 00 64 00 00 53)
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
                 00000024     64 - LOAD_CONST          CODE('CanFollow')
                 00000027     84 - MAKE_FUNCTION       r0000
                 0000002A     5A - STORE_NAME          'CanFollow'
                 0000002D     64 - LOAD_CONST          '\ndirectObject.MissionKey\n'
                 00000030     65 - LOAD_NAME           'CanFollow'
                 00000033     5F - STORE_ATTR          'depAttr'
                 00000036     64 - LOAD_CONST          CODE('CanStopFollow')
                 00000039     84 - MAKE_FUNCTION       r0000
                 0000003C     5A - STORE_NAME          'CanStopFollow'
                 0000003F     64 - LOAD_CONST          '\ndirectObject.MasterCharacterID\n'
                 00000042     65 - LOAD_NAME           'CanStopFollow'
                 00000045     5F - STORE_ATTR          'depAttr'
                 00000048     64 - LOAD_CONST          None
                 0000004B     53 - RETURN_VALUE        
             consts:
0000006A         TUPLE: (
0000006F             None (4E),
00000070             CODE:
                         argcount:
00000071                     LONG: 2L (02 00 00 00)
                         nlocals:
00000075                     LONG: 2L (02 00 00 00)
                         stacksize:
00000079                     LONG: 3L (03 00 00 00)
                         flags:
0000007D                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000081                     STR: 't\x00\x00i\x01\x00|\x00\x00i\x03\x00i\x04\x00|\x01\x00i\x04\x00\x83\x02\x00o\x08\x00\x01t\x06\x00Sn\x01\x00\x01t\x07\x00Sd\x00\x00S' (2C 00 00 00 74 00 00 69 01 00 7C 00 00 69 03 00 69 04 00 7C 01 00 69 04 00 83 02 00 6F 08 00 01 74 06 00 53 6E 01 00 01 74 07 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'mv'
                             00000003     69 - LOAD_ATTR           'ValidMissionKeyBaseMatch'
                             00000006     7C - LOAD_FAST           'subject'
                             00000009     69 - LOAD_ATTR           'MissionTeam'
                             0000000C     69 - LOAD_ATTR           'MissionKey'
                             0000000F     7C - LOAD_FAST           'directObject'
                             00000012     69 - LOAD_ATTR           'MissionKey'
                             00000015     83 - CALL_FUNCTION       r0002
                             00000018     6F - JUMP_IF_FALSE       -> 00000023
                             0000001B     01 - POP_TOP             
                             0000001C     74 - LOAD_GLOBAL         'True'
                             0000001F     53 - RETURN_VALUE        
                             00000020     6E - JUMP_FORWARD        -> 00000024
                             00000023     01 - POP_TOP             
                             00000024     74 - LOAD_GLOBAL         'False'
                             00000027     53 - RETURN_VALUE        
                             00000028     64 - LOAD_CONST          None
                             0000002B     53 - RETURN_VALUE        
                         consts:
000000B2                     TUPLE: (
000000B7                         None (4E)
                             )
                         names:
000000B8                     TUPLE: (
000000BD                         STR: 'mv' (02 00 00 00 6D 76),
000000C4                         STR: 'ValidMissionKeyBaseMatch' (18 00 00 00 56 61 6C 69 64 4D 69 73 73 69 6F 6E 4B 65 79 42 61 73 65 4D 61 74 63 68),
000000E1                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000000ED                         STR: 'MissionTeam' (0B 00 00 00 4D 69 73 73 69 6F 6E 54 65 61 6D),
000000FD                         STR: 'MissionKey' (0A 00 00 00 4D 69 73 73 69 6F 6E 4B 65 79),
0000010C                         STR: 'directObject' (0C 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74),
0000011D                         STR: 'True' (04 00 00 00 54 72 75 65),
00000126                         STR: 'False' (05 00 00 00 46 61 6C 73 65)
                             )
                         varnames:
00000130                     TUPLE: (
00000135                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000141                         STR: 'directObject' (0C 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74)
                             )
                         freevars:
00000152                     TUPLE: ()
                         cellvars:
00000157                     TUPLE: ()
                         filename:
0000015C                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\followvalidate.py' (46 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 66 6F 6C 6C 6F 77 76 61 6C 69 64 61 74 65 2E 70 79)
                         name:
000001A7                     STR: 'CanFollow' (09 00 00 00 43 61 6E 46 6F 6C 6C 6F 77)
                         firslineno:
000001B5                     LONG: 9L (09 00 00 00)
                         lnotab:
000001B9                     STR: '\x00\x02\x1c\x01\x08\x01' (06 00 00 00 00 02 1C 01 08 01),
000001C4             STR: '\ndirectObject.MissionKey\n' (19 00 00 00 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 4D 69 73 73 69 6F 6E 4B 65 79 0A),
000001E2             CODE:
                         argcount:
000001E3                     LONG: 2L (02 00 00 00)
                         nlocals:
000001E7                     LONG: 2L (02 00 00 00)
                         stacksize:
000001EB                     LONG: 2L (02 00 00 00)
                         flags:
000001EF                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000001F3                     STR: '|\x00\x00i\x01\x00i\x02\x00|\x01\x00i\x04\x00j\x02\x00o\x08\x00\x01t\x05\x00Sn\x01\x00\x01t\x06\x00Sd\x00\x00S' (26 00 00 00 7C 00 00 69 01 00 69 02 00 7C 01 00 69 04 00 6A 02 00 6F 08 00 01 74 05 00 53 6E 01 00 01 74 06 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'subject'
                             00000003     69 - LOAD_ATTR           'PlayerCharacter'
                             00000006     69 - LOAD_ATTR           'CharacterID'
                             00000009     7C - LOAD_FAST           'directObject'
                             0000000C     69 - LOAD_ATTR           'MasterCharacterID'
                             0000000F     6A - COMPARE_OP          "=="
                             00000012     6F - JUMP_IF_FALSE       -> 0000001D
                             00000015     01 - POP_TOP             
                             00000016     74 - LOAD_GLOBAL         'True'
                             00000019     53 - RETURN_VALUE        
                             0000001A     6E - JUMP_FORWARD        -> 0000001E
                             0000001D     01 - POP_TOP             
                             0000001E     74 - LOAD_GLOBAL         'False'
                             00000021     53 - RETURN_VALUE        
                             00000022     64 - LOAD_CONST          None
                             00000025     53 - RETURN_VALUE        
                         consts:
0000021E                     TUPLE: (
00000223                         None (4E)
                             )
                         names:
00000224                     TUPLE: (
00000229                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000235                         STR: 'PlayerCharacter' (0F 00 00 00 50 6C 61 79 65 72 43 68 61 72 61 63 74 65 72),
00000249                         STR: 'CharacterID' (0B 00 00 00 43 68 61 72 61 63 74 65 72 49 44),
00000259                         STR: 'directObject' (0C 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74),
0000026A                         STR: 'MasterCharacterID' (11 00 00 00 4D 61 73 74 65 72 43 68 61 72 61 63 74 65 72 49 44),
00000280                         STR: 'True' (04 00 00 00 54 72 75 65),
00000289                         STR: 'False' (05 00 00 00 46 61 6C 73 65)
                             )
                         varnames:
00000293                     TUPLE: (
00000298                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000002A4                         STR: 'directObject' (0C 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74)
                             )
                         freevars:
000002B5                     TUPLE: ()
                         cellvars:
000002BA                     TUPLE: ()
                         filename:
000002BF                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\followvalidate.py' (46 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 66 6F 6C 6C 6F 77 76 61 6C 69 64 61 74 65 2E 70 79)
                         name:
0000030A                     STR: 'CanStopFollow' (0D 00 00 00 43 61 6E 53 74 6F 70 46 6F 6C 6C 6F 77)
                         firslineno:
0000031C                     LONG: 19L (13 00 00 00)
                         lnotab:
00000320                     STR: '\x00\x02\x16\x01\x08\x01' (06 00 00 00 00 02 16 01 08 01),
0000032B             STR: '\ndirectObject.MasterCharacterID\n' (20 00 00 00 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 4D 61 73 74 65 72 43 68 61 72 61 63 74 65 72 49 44 0A)
                 )
             names:
00000350         TUPLE: (
00000355             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00000360             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
0000036E             STR: 'obj' (03 00 00 00 6F 62 6A),
00000376             STR: 'missionvalidate' (0F 00 00 00 6D 69 73 73 69 6F 6E 76 61 6C 69 64 61 74 65),
0000038A             STR: 'mv' (02 00 00 00 6D 76),
00000391             STR: 'CanFollow' (09 00 00 00 43 61 6E 46 6F 6C 6C 6F 77),
0000039F             STR: 'depAttr' (07 00 00 00 64 65 70 41 74 74 72),
000003AB             STR: 'CanStopFollow' (0D 00 00 00 43 61 6E 53 74 6F 70 46 6F 6C 6C 6F 77)
                 )
             varnames:
000003BD         TUPLE: (
000003C2             STR: 'CanStopFollow' (0D 00 00 00 43 61 6E 53 74 6F 70 46 6F 6C 6C 6F 77),
000003D4             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
000003E2             STR: 'obj' (03 00 00 00 6F 62 6A),
000003EA             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
000003F5             STR: 'CanFollow' (09 00 00 00 43 61 6E 46 6F 6C 6C 6F 77),
00000403             STR: 'mv' (02 00 00 00 6D 76)
                 )
             freevars:
0000040A         TUPLE: ()
             cellvars:
0000040F         TUPLE: ()
             filename:
00000414         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\followvalidate.py' (46 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 66 6F 6C 6C 6F 77 76 61 6C 69 64 61 74 65 2E 70 79)
             name:
0000045F         STR: '?' (01 00 00 00 3F)
             firslineno:
00000465         LONG: 2L (02 00 00 00)
             lnotab:
00000469         STR: '\t\x01\t\x02\t\x02\t\x02\t\x06\t\x04\t\x07' (0E 00 00 00 09 01 09 02 09 02 09 02 09 06 09 04 09 07)

