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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00Z\x02\x00d\x00\x00k\x03\x00Z\x04\x00d\x01\x00\x84\x00\x00Z\x05\x00d\x02\x00d\x03\x00\x84\x01\x00Z\x06\x00d\x04\x00\x84\x00\x00Z\x07\x00d\x05\x00e\x07\x00_\x08\x00d\x00\x00S' (4F 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 5A 02 00 64 00 00 6B 03 00 5A 04 00 64 01 00 84 00 00 5A 05 00 64 02 00 64 03 00 84 01 00 5A 06 00 64 04 00 84 00 00 5A 07 00 64 05 00 65 07 00 5F 08 00 64 00 00 53)
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
                 00000024     64 - LOAD_CONST          CODE('DistanceWithin')
                 00000027     84 - MAKE_FUNCTION       r0000
                 0000002A     5A - STORE_NAME          'DistanceWithin'
                 0000002D     64 - LOAD_CONST          700
                 00000030     64 - LOAD_CONST          CODE('CombatPhysicsOkay')
                 00000033     84 - MAKE_FUNCTION       r0001
                 00000036     5A - STORE_NAME          'CombatPhysicsOkay'
                 00000039     64 - LOAD_CONST          CODE('CanFight')
                 0000003C     84 - MAKE_FUNCTION       r0000
                 0000003F     5A - STORE_NAME          'CanFight'
                 00000042     64 - LOAD_CONST          '\ndirectObject.IsDead\ndirectObject.Position\ndirectObject.locator\n'
                 00000045     65 - LOAD_NAME           'CanFight'
                 00000048     5F - STORE_ATTR          'depAttr'
                 0000004B     64 - LOAD_CONST          None
                 0000004E     53 - RETURN_VALUE        
             consts:
0000006D         TUPLE: (
00000072             None (4E),
00000073             CODE:
                         argcount:
00000074                     LONG: 3L (03 00 00 00)
                         nlocals:
00000078                     LONG: 6L (06 00 00 00)
                         stacksize:
0000007C                     LONG: 3L (03 00 00 00)
                         flags:
00000080                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000084                     STR: '|\x00\x00i\x01\x00|\x01\x00i\x01\x00\x18}\x04\x00|\x00\x00i\x04\x00|\x01\x00i\x04\x00\x18}\x05\x00|\x00\x00i\x06\x00|\x01\x00i\x06\x00\x18}\x03\x00|\x04\x00|\x04\x00\x14|\x05\x00|\x05\x00\x14\x17|\x03\x00|\x03\x00\x14\x17|\x02\x00|\x02\x00\x14j\x00\x00Sd\x01\x00S' (56 00 00 00 7C 00 00 69 01 00 7C 01 00 69 01 00 18 7D 04 00 7C 00 00 69 04 00 7C 01 00 69 04 00 18 7D 05 00 7C 00 00 69 06 00 7C 01 00 69 06 00 18 7D 03 00 7C 04 00 7C 04 00 14 7C 05 00 7C 05 00 14 17 7C 03 00 7C 03 00 14 17 7C 02 00 7C 02 00 14 6A 00 00 53 64 01 00 53)
                             00000000     7C - LOAD_FAST           'pos1'
                             00000003     69 - LOAD_ATTR           'x'
                             00000006     7C - LOAD_FAST           'pos2'
                             00000009     69 - LOAD_ATTR           'x'
                             0000000C     18 - BINARY_SUBTRACT     
                             0000000D     7D - STORE_FAST          'x_diff'
                             00000010     7C - LOAD_FAST           'pos1'
                             00000013     69 - LOAD_ATTR           'y'
                             00000016     7C - LOAD_FAST           'pos2'
                             00000019     69 - LOAD_ATTR           'y'
                             0000001C     18 - BINARY_SUBTRACT     
                             0000001D     7D - STORE_FAST          'y_diff'
                             00000020     7C - LOAD_FAST           'pos1'
                             00000023     69 - LOAD_ATTR           'z'
                             00000026     7C - LOAD_FAST           'pos2'
                             00000029     69 - LOAD_ATTR           'z'
                             0000002C     18 - BINARY_SUBTRACT     
                             0000002D     7D - STORE_FAST          'z_diff'
                             00000030     7C - LOAD_FAST           'x_diff'
                             00000033     7C - LOAD_FAST           'x_diff'
                             00000036     14 - BINARY_MULTIPLY     
                             00000037     7C - LOAD_FAST           'y_diff'
                             0000003A     7C - LOAD_FAST           'y_diff'
                             0000003D     14 - BINARY_MULTIPLY     
                             0000003E     17 - BINARY_ADD          
                             0000003F     7C - LOAD_FAST           'z_diff'
                             00000042     7C - LOAD_FAST           'z_diff'
                             00000045     14 - BINARY_MULTIPLY     
                             00000046     17 - BINARY_ADD          
                             00000047     7C - LOAD_FAST           'dist'
                             0000004A     7C - LOAD_FAST           'dist'
                             0000004D     14 - BINARY_MULTIPLY     
                             0000004E     6A - COMPARE_OP          "<"
                             00000051     53 - RETURN_VALUE        
                             00000052     64 - LOAD_CONST          None
                             00000055     53 - RETURN_VALUE        
                         consts:
000000DF                     TUPLE: (
000000E4                         STR: ' Returns true if the vectors pos1 and pos2 have a distance of less than dist. ' (4E 00 00 00 20 52 65 74 75 72 6E 73 20 74 72 75 65 20 69 66 20 74 68 65 20 76 65 63 74 6F 72 73 20 70 6F 73 31 20 61 6E 64 20 70 6F 73 32 20 68 61 76 65 20 61 20 64 69 73 74 61 6E 63 65 20 6F 66 20 6C 65 73 73 20 74 68 61 6E 20 64 69 73 74 2E 20),
00000137                         None (4E)
                             )
                         names:
00000138                     TUPLE: (
0000013D                         STR: 'pos1' (04 00 00 00 70 6F 73 31),
00000146                         STR: 'x' (01 00 00 00 78),
0000014C                         STR: 'pos2' (04 00 00 00 70 6F 73 32),
00000155                         STR: 'x_diff' (06 00 00 00 78 5F 64 69 66 66),
00000160                         STR: 'y' (01 00 00 00 79),
00000166                         STR: 'y_diff' (06 00 00 00 79 5F 64 69 66 66),
00000171                         STR: 'z' (01 00 00 00 7A),
00000177                         STR: 'z_diff' (06 00 00 00 7A 5F 64 69 66 66),
00000182                         STR: 'dist' (04 00 00 00 64 69 73 74)
                             )
                         varnames:
0000018B                     TUPLE: (
00000190                         STR: 'pos1' (04 00 00 00 70 6F 73 31),
00000199                         STR: 'pos2' (04 00 00 00 70 6F 73 32),
000001A2                         STR: 'dist' (04 00 00 00 64 69 73 74),
000001AB                         STR: 'z_diff' (06 00 00 00 7A 5F 64 69 66 66),
000001B6                         STR: 'x_diff' (06 00 00 00 78 5F 64 69 66 66),
000001C1                         STR: 'y_diff' (06 00 00 00 79 5F 64 69 66 66)
                             )
                         freevars:
000001CC                     TUPLE: ()
                         cellvars:
000001D1                     TUPLE: ()
                         filename:
000001D6                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combatvalidate.py' (46 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 76 61 6C 69 64 61 74 65 2E 70 79)
                         name:
00000221                     STR: 'DistanceWithin' (0E 00 00 00 44 69 73 74 61 6E 63 65 57 69 74 68 69 6E)
                         firslineno:
00000234                     LONG: 9L (09 00 00 00)
                         lnotab:
00000238                     STR: '\x00\x01\x00\x02\x10\x01\x10\x01\x10\x02' (0A 00 00 00 00 01 00 02 10 01 10 01 10 02),
00000247             INT: 700 (BC 02 00 00),
0000024C             CODE:
                         argcount:
0000024D                     LONG: 3L (03 00 00 00)
                         nlocals:
00000251                     LONG: 5L (05 00 00 00)
                         stacksize:
00000255                     LONG: 4L (04 00 00 00)
                         flags:
00000259                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000025D                     STR: '|\x00\x00i\x01\x00}\x04\x00|\x01\x00i\x01\x00}\x03\x00t\x05\x00|\x04\x00|\x03\x00|\x02\x00\x83\x03\x00\x0co\x08\x00\x01t\x07\x00Sn\x01\x00\x01t\x08\x00i\t\x00|\x04\x00|\x03\x00\x83\x02\x00\x0co\x08\x00\x01t\x07\x00Sn\x01\x00\x01t\n\x00Sd\x00\x00S' (52 00 00 00 7C 00 00 69 01 00 7D 04 00 7C 01 00 69 01 00 7D 03 00 74 05 00 7C 04 00 7C 03 00 7C 02 00 83 03 00 0C 6F 08 00 01 74 07 00 53 6E 01 00 01 74 08 00 69 09 00 7C 04 00 7C 03 00 83 02 00 0C 6F 08 00 01 74 07 00 53 6E 01 00 01 74 0A 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'subject'
                             00000003     69 - LOAD_ATTR           'Position'
                             00000006     7D - STORE_FAST          'pos1'
                             00000009     7C - LOAD_FAST           'directObject'
                             0000000C     69 - LOAD_ATTR           'Position'
                             0000000F     7D - STORE_FAST          'pos2'
                             00000012     74 - LOAD_GLOBAL         'DistanceWithin'
                             00000015     7C - LOAD_FAST           'pos1'
                             00000018     7C - LOAD_FAST           'pos2'
                             0000001B     7C - LOAD_FAST           'rangeValue'
                             0000001E     83 - CALL_FUNCTION       r0003
                             00000021     0C - UNARY_NOT           
                             00000022     6F - JUMP_IF_FALSE       -> 0000002D
                             00000025     01 - POP_TOP             
                             00000026     74 - LOAD_GLOBAL         'False'
                             00000029     53 - RETURN_VALUE        
                             0000002A     6E - JUMP_FORWARD        -> 0000002E
                             0000002D     01 - POP_TOP             
                             0000002E     74 - LOAD_GLOBAL         'physics'
                             00000031     69 - LOAD_ATTR           'clearLine'
                             00000034     7C - LOAD_FAST           'pos1'
                             00000037     7C - LOAD_FAST           'pos2'
                             0000003A     83 - CALL_FUNCTION       r0002
                             0000003D     0C - UNARY_NOT           
                             0000003E     6F - JUMP_IF_FALSE       -> 00000049
                             00000041     01 - POP_TOP             
                             00000042     74 - LOAD_GLOBAL         'False'
                             00000045     53 - RETURN_VALUE        
                             00000046     6E - JUMP_FORWARD        -> 0000004A
                             00000049     01 - POP_TOP             
                             0000004A     74 - LOAD_GLOBAL         'True'
                             0000004D     53 - RETURN_VALUE        
                             0000004E     64 - LOAD_CONST          None
                             00000051     53 - RETURN_VALUE        
                         consts:
000002B4                     TUPLE: (
000002B9                         None (4E)
                             )
                         names:
000002BA                     TUPLE: (
000002BF                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000002CB                         STR: 'Position' (08 00 00 00 50 6F 73 69 74 69 6F 6E),
000002D8                         STR: 'pos1' (04 00 00 00 70 6F 73 31),
000002E1                         STR: 'directObject' (0C 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74),
000002F2                         STR: 'pos2' (04 00 00 00 70 6F 73 32),
000002FB                         STR: 'DistanceWithin' (0E 00 00 00 44 69 73 74 61 6E 63 65 57 69 74 68 69 6E),
0000030E                         STR: 'rangeValue' (0A 00 00 00 72 61 6E 67 65 56 61 6C 75 65),
0000031D                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
00000327                         STR: 'physics' (07 00 00 00 70 68 79 73 69 63 73),
00000333                         STR: 'clearLine' (09 00 00 00 63 6C 65 61 72 4C 69 6E 65),
00000341                         STR: 'True' (04 00 00 00 54 72 75 65)
                             )
                         varnames:
0000034A                     TUPLE: (
0000034F                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000035B                         STR: 'directObject' (0C 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74),
0000036C                         STR: 'rangeValue' (0A 00 00 00 72 61 6E 67 65 56 61 6C 75 65),
0000037B                         STR: 'pos2' (04 00 00 00 70 6F 73 32),
00000384                         STR: 'pos1' (04 00 00 00 70 6F 73 31)
                             )
                         freevars:
0000038D                     TUPLE: ()
                         cellvars:
00000392                     TUPLE: ()
                         filename:
00000397                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combatvalidate.py' (46 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 76 61 6C 69 64 61 74 65 2E 70 79)
                         name:
000003E2                     STR: 'CombatPhysicsOkay' (11 00 00 00 43 6F 6D 62 61 74 50 68 79 73 69 63 73 4F 6B 61 79)
                         firslineno:
000003F8                     LONG: 18L (12 00 00 00)
                         lnotab:
000003FC                     STR: '\x00\x02\t\x01\t\x02\x14\x01\x08\x02\x14\x01\x08\x02' (0E 00 00 00 00 02 09 01 09 02 14 01 08 02 14 01 08 02),
0000040F             CODE:
                         argcount:
00000410                     LONG: 2L (02 00 00 00)
                         nlocals:
00000414                     LONG: 2L (02 00 00 00)
                         stacksize:
00000418                     LONG: 3L (03 00 00 00)
                         flags:
0000041C                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000420                     STR: '|\x01\x00i\x01\x00p\x07\x00\x01|\x00\x00i\x01\x00o\x08\x00\x01t\x03\x00Sn\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x06\x00\x83\x01\x00\x0co\x08\x00\x01t\x03\x00Sn\x01\x00\x01t\x07\x00|\x00\x00|\x01\x00\x83\x02\x00\x0co\x08\x00\x01t\x03\x00Sn\x01\x00\x01t\x08\x00Sd\x01\x00S' (5C 00 00 00 7C 01 00 69 01 00 70 07 00 01 7C 00 00 69 01 00 6F 08 00 01 74 03 00 53 6E 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 06 00 83 01 00 0C 6F 08 00 01 74 03 00 53 6E 01 00 01 74 07 00 7C 00 00 7C 01 00 83 02 00 0C 6F 08 00 01 74 03 00 53 6E 01 00 01 74 08 00 53 64 01 00 53)
                             00000000     7C - LOAD_FAST           'directObject'
                             00000003     69 - LOAD_ATTR           'IsDead'
                             00000006     70 - JUMP_IF_TRUE        -> 00000010
                             00000009     01 - POP_TOP             
                             0000000A     7C - LOAD_FAST           'subject'
                             0000000D     69 - LOAD_ATTR           'IsDead'
                             00000010     6F - JUMP_IF_FALSE       -> 0000001B
                             00000013     01 - POP_TOP             
                             00000014     74 - LOAD_GLOBAL         'False'
                             00000017     53 - RETURN_VALUE        
                             00000018     6E - JUMP_FORWARD        -> 0000001C
                             0000001B     01 - POP_TOP             
                             0000001C     7C - LOAD_FAST           'subject'
                             0000001F     69 - LOAD_ATTR           'CharMvt'
                             00000022     69 - LOAD_ATTR           'isEnemy'
                             00000025     7C - LOAD_FAST           'directObject'
                             00000028     69 - LOAD_ATTR           'locator'
                             0000002B     83 - CALL_FUNCTION       r0001
                             0000002E     0C - UNARY_NOT           
                             0000002F     6F - JUMP_IF_FALSE       -> 0000003A
                             00000032     01 - POP_TOP             
                             00000033     74 - LOAD_GLOBAL         'False'
                             00000036     53 - RETURN_VALUE        
                             00000037     6E - JUMP_FORWARD        -> 0000003B
                             0000003A     01 - POP_TOP             
                             0000003B     74 - LOAD_GLOBAL         'CombatPhysicsOkay'
                             0000003E     7C - LOAD_FAST           'subject'
                             00000041     7C - LOAD_FAST           'directObject'
                             00000044     83 - CALL_FUNCTION       r0002
                             00000047     0C - UNARY_NOT           
                             00000048     6F - JUMP_IF_FALSE       -> 00000053
                             0000004B     01 - POP_TOP             
                             0000004C     74 - LOAD_GLOBAL         'False'
                             0000004F     53 - RETURN_VALUE        
                             00000050     6E - JUMP_FORWARD        -> 00000054
                             00000053     01 - POP_TOP             
                             00000054     74 - LOAD_GLOBAL         'True'
                             00000057     53 - RETURN_VALUE        
                             00000058     64 - LOAD_CONST          None
                             0000005B     53 - RETURN_VALUE        
                         consts:
00000481                     TUPLE: (
00000486                         STR: '\n    This rule should become quite complex as it tries to figure\n\tout if anyone can fight anything.\n\t\n\tNope, all the complexity is buried in CharMvt.isEnemy.\n    ' (A2 00 00 00 0A 20 20 20 20 54 68 69 73 20 72 75 6C 65 20 73 68 6F 75 6C 64 20 62 65 63 6F 6D 65 20 71 75 69 74 65 20 63 6F 6D 70 6C 65 78 20 61 73 20 69 74 20 74 72 69 65 73 20 74 6F 20 66 69 67 75 72 65 0A 09 6F 75 74 20 69 66 20 61 6E 79 6F 6E 65 20 63 61 6E 20 66 69 67 68 74 20 61 6E 79 74 68 69 6E 67 2E 0A 09 0A 09 4E 6F 70 65 2C 20 61 6C 6C 20 74 68 65 20 63 6F 6D 70 6C 65 78 69 74 79 20 69 73 20 62 75 72 69 65 64 20 69 6E 20 43 68 61 72 4D 76 74 2E 69 73 45 6E 65 6D 79 2E 0A 20 20 20 20),
0000052D                         None (4E)
                             )
                         names:
0000052E                     TUPLE: (
00000533                         STR: 'directObject' (0C 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74),
00000544                         STR: 'IsDead' (06 00 00 00 49 73 44 65 61 64),
0000054F                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000055B                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
00000565                         STR: 'CharMvt' (07 00 00 00 43 68 61 72 4D 76 74),
00000571                         STR: 'isEnemy' (07 00 00 00 69 73 45 6E 65 6D 79),
0000057D                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
00000589                         STR: 'CombatPhysicsOkay' (11 00 00 00 43 6F 6D 62 61 74 50 68 79 73 69 63 73 4F 6B 61 79),
0000059F                         STR: 'True' (04 00 00 00 54 72 75 65)
                             )
                         varnames:
000005A8                     TUPLE: (
000005AD                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000005B9                         STR: 'directObject' (0C 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74)
                             )
                         freevars:
000005CA                     TUPLE: ()
                         cellvars:
000005CF                     TUPLE: ()
                         filename:
000005D4                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combatvalidate.py' (46 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 76 61 6C 69 64 61 74 65 2E 70 79)
                         name:
0000061F                     STR: 'CanFight' (08 00 00 00 43 61 6E 46 69 67 68 74)
                         firslineno:
0000062C                     LONG: 31L (1F 00 00 00)
                         lnotab:
00000630                     STR: '\x00\x06\x00\x04\x14\x01\x08\x02\x17\x02\x08\x03\x11\x01\x08\x02' (10 00 00 00 00 06 00 04 14 01 08 02 17 02 08 03 11 01 08 02),
00000645             STR: '\ndirectObject.IsDead\ndirectObject.Position\ndirectObject.locator\n' (40 00 00 00 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 49 73 44 65 61 64 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 50 6F 73 69 74 69 6F 6E 0A 64 69 72 65 63 74 4F 62 6A 65 63 74 2E 6C 6F 63 61 74 6F 72 0A)
                 )
             names:
0000068A         TUPLE: (
0000068F             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
0000069A             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
000006A8             STR: 'obj' (03 00 00 00 6F 62 6A),
000006B0             STR: 'missionvalidate' (0F 00 00 00 6D 69 73 73 69 6F 6E 76 61 6C 69 64 61 74 65),
000006C4             STR: 'mv' (02 00 00 00 6D 76),
000006CB             STR: 'DistanceWithin' (0E 00 00 00 44 69 73 74 61 6E 63 65 57 69 74 68 69 6E),
000006DE             STR: 'CombatPhysicsOkay' (11 00 00 00 43 6F 6D 62 61 74 50 68 79 73 69 63 73 4F 6B 61 79),
000006F4             STR: 'CanFight' (08 00 00 00 43 61 6E 46 69 67 68 74),
00000701             STR: 'depAttr' (07 00 00 00 64 65 70 41 74 74 72)
                 )
             varnames:
0000070D         TUPLE: (
00000712             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00000720             STR: 'obj' (03 00 00 00 6F 62 6A),
00000728             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00000733             STR: 'CanFight' (08 00 00 00 43 61 6E 46 69 67 68 74),
00000740             STR: 'DistanceWithin' (0E 00 00 00 44 69 73 74 61 6E 63 65 57 69 74 68 69 6E),
00000753             STR: 'mv' (02 00 00 00 6D 76),
0000075A             STR: 'CombatPhysicsOkay' (11 00 00 00 43 6F 6D 62 61 74 50 68 79 73 69 63 73 4F 6B 61 79)
                 )
             freevars:
00000770         TUPLE: ()
             cellvars:
00000775         TUPLE: ()
             filename:
0000077A         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combatvalidate.py' (46 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 76 61 6C 69 64 61 74 65 2E 70 79)
             name:
000007C5         STR: '?' (01 00 00 00 3F)
             firslineno:
000007CB         LONG: 2L (02 00 00 00)
             lnotab:
000007CF         STR: '\t\x01\t\x02\t\x02\t\x02\t\t\x0c\r\t\x18' (0E 00 00 00 09 01 09 02 09 02 09 02 09 09 0C 0D 09 18)

