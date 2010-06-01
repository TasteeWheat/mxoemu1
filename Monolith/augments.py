--== Disasm ==--
00000008 CODE:
             argcount:
00000009         LONG: 0L (00 00 00 00)
             nlocals:
0000000D         LONG: 0L (00 00 00 00)
             stacksize:
00000011         LONG: 11L (0B 00 00 00)
             flags:
00000015         LONG: 64L (40 00 00 00)
                 (NOFREE)
             code:
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00g\x00\x00Z\x02\x00g\x00\x00Z\x03\x00g\x00\x00Z\x04\x00g\x00\x00Z\x05\x00g\x00\x00Z\x06\x00g\x00\x00Z\x07\x00g\x00\x00Z\x08\x00g\x00\x00Z\t\x00g\x00\x00Z\n\x00g\x00\x00e\x02\x00e\x03\x00e\x04\x00e\x05\x00e\x06\x00e\x07\x00g\x00\x00e\x08\x00e\t\x00e\n\x00g\x0b\x00Z\x0b\x00d\x01\x00\x84\x00\x00Z\x0c\x00d\x00\x00S' (7C 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 67 00 00 5A 02 00 67 00 00 5A 03 00 67 00 00 5A 04 00 67 00 00 5A 05 00 67 00 00 5A 06 00 67 00 00 5A 07 00 67 00 00 5A 08 00 67 00 00 5A 09 00 67 00 00 5A 0A 00 67 00 00 65 02 00 65 03 00 65 04 00 65 05 00 65 06 00 65 07 00 67 00 00 65 08 00 65 09 00 65 0A 00 67 0B 00 5A 0B 00 64 01 00 84 00 00 5A 0C 00 64 00 00 53)
                 00000000     64 - LOAD_CONST          None
                 00000003     6B - IMPORT_NAME         'traceback'
                 00000006     5A - STORE_NAME          'traceback'
                 00000009     64 - LOAD_CONST          None
                 0000000C     6B - IMPORT_NAME         'obj'
                 0000000F     5A - STORE_NAME          'obj'
                 00000012     67 - BUILD_LIST          r0000
                 00000015     5A - STORE_NAME          'HatAugments'
                 00000018     67 - BUILD_LIST          r0000
                 0000001B     5A - STORE_NAME          'GlassesAugments'
                 0000001E     67 - BUILD_LIST          r0000
                 00000021     5A - STORE_NAME          'ShirtAugments'
                 00000024     67 - BUILD_LIST          r0000
                 00000027     5A - STORE_NAME          'GlovesAugments'
                 0000002A     67 - BUILD_LIST          r0000
                 0000002D     5A - STORE_NAME          'CoatAugments'
                 00000030     67 - BUILD_LIST          r0000
                 00000033     5A - STORE_NAME          'PantsAugments'
                 00000036     67 - BUILD_LIST          r0000
                 00000039     5A - STORE_NAME          'ShoesAugments'
                 0000003C     67 - BUILD_LIST          r0000
                 0000003F     5A - STORE_NAME          'WeaponAugments'
                 00000042     67 - BUILD_LIST          r0000
                 00000045     5A - STORE_NAME          'HackerToolAugments'
                 00000048     67 - BUILD_LIST          r0000
                 0000004B     65 - LOAD_NAME           'HatAugments'
                 0000004E     65 - LOAD_NAME           'GlassesAugments'
                 00000051     65 - LOAD_NAME           'ShirtAugments'
                 00000054     65 - LOAD_NAME           'GlovesAugments'
                 00000057     65 - LOAD_NAME           'CoatAugments'
                 0000005A     65 - LOAD_NAME           'PantsAugments'
                 0000005D     67 - BUILD_LIST          r0000
                 00000060     65 - LOAD_NAME           'ShoesAugments'
                 00000063     65 - LOAD_NAME           'WeaponAugments'
                 00000066     65 - LOAD_NAME           'HackerToolAugments'
                 00000069     67 - BUILD_LIST          r000B
                 0000006C     5A - STORE_NAME          'MasterAugmentTable'
                 0000006F     64 - LOAD_CONST          CODE('GetAugmentTable')
                 00000072     84 - MAKE_FUNCTION       r0000
                 00000075     5A - STORE_NAME          'GetAugmentTable'
                 00000078     64 - LOAD_CONST          None
                 0000007B     53 - RETURN_VALUE        
             consts:
0000009A         TUPLE: (
0000009F             None (4E),
000000A0             CODE:
                         argcount:
000000A1                     LONG: 1L (01 00 00 00)
                         nlocals:
000000A5                     LONG: 1L (01 00 00 00)
                         stacksize:
000000A9                     LONG: 3L (03 00 00 00)
                         flags:
000000AD                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000000B1                     STR: '|\x00\x00t\x01\x00t\x02\x00\x83\x01\x00j\x05\x00o\x08\x00\x01g\x00\x00Sn\x01\x00\x01t\x02\x00|\x00\x00\x19Sd\x00\x00S' (27 00 00 00 7C 00 00 74 01 00 74 02 00 83 01 00 6A 05 00 6F 08 00 01 67 00 00 53 6E 01 00 01 74 02 00 7C 00 00 19 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'category'
                             00000003     74 - LOAD_GLOBAL         'len'
                             00000006     74 - LOAD_GLOBAL         'MasterAugmentTable'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     6A - COMPARE_OP          ">="
                             0000000F     6F - JUMP_IF_FALSE       -> 0000001A
                             00000012     01 - POP_TOP             
                             00000013     67 - BUILD_LIST          r0000
                             00000016     53 - RETURN_VALUE        
                             00000017     6E - JUMP_FORWARD        -> 0000001B
                             0000001A     01 - POP_TOP             
                             0000001B     74 - LOAD_GLOBAL         'MasterAugmentTable'
                             0000001E     7C - LOAD_FAST           'category'
                             00000021     19 - BINARY_SUBSCR       
                             00000022     53 - RETURN_VALUE        
                             00000023     64 - LOAD_CONST          None
                             00000026     53 - RETURN_VALUE        
                         consts:
000000DD                     TUPLE: (
000000E2                         None (4E)
                             )
                         names:
000000E3                     TUPLE: (
000000E8                         STR: 'category' (08 00 00 00 63 61 74 65 67 6F 72 79),
000000F5                         STR: 'len' (03 00 00 00 6C 65 6E),
000000FD                         STR: 'MasterAugmentTable' (12 00 00 00 4D 61 73 74 65 72 41 75 67 6D 65 6E 74 54 61 62 6C 65)
                             )
                         varnames:
00000114                     TUPLE: (
00000119                         STR: 'category' (08 00 00 00 63 61 74 65 67 6F 72 79)
                             )
                         freevars:
00000126                     TUPLE: ()
                         cellvars:
0000012B                     TUPLE: ()
                         filename:
00000130                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\augments.py' (40 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 75 67 6D 65 6E 74 73 2E 70 79)
                         name:
00000175                     STR: 'GetAugmentTable' (0F 00 00 00 47 65 74 41 75 67 6D 65 6E 74 54 61 62 6C 65)
                         firslineno:
00000189                     LONG: 66L (42 00 00 00)
                         lnotab:
0000018D                     STR: '\x00\x01\x13\x01\x08\x02' (06 00 00 00 00 01 13 01 08 02)
                 )
             names:
00000198         TUPLE: (
0000019D             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
000001AB             STR: 'obj' (03 00 00 00 6F 62 6A),
000001B3             STR: 'HatAugments' (0B 00 00 00 48 61 74 41 75 67 6D 65 6E 74 73),
000001C3             STR: 'GlassesAugments' (0F 00 00 00 47 6C 61 73 73 65 73 41 75 67 6D 65 6E 74 73),
000001D7             STR: 'ShirtAugments' (0D 00 00 00 53 68 69 72 74 41 75 67 6D 65 6E 74 73),
000001E9             STR: 'GlovesAugments' (0E 00 00 00 47 6C 6F 76 65 73 41 75 67 6D 65 6E 74 73),
000001FC             STR: 'CoatAugments' (0C 00 00 00 43 6F 61 74 41 75 67 6D 65 6E 74 73),
0000020D             STR: 'PantsAugments' (0D 00 00 00 50 61 6E 74 73 41 75 67 6D 65 6E 74 73),
0000021F             STR: 'ShoesAugments' (0D 00 00 00 53 68 6F 65 73 41 75 67 6D 65 6E 74 73),
00000231             STR: 'WeaponAugments' (0E 00 00 00 57 65 61 70 6F 6E 41 75 67 6D 65 6E 74 73),
00000244             STR: 'HackerToolAugments' (12 00 00 00 48 61 63 6B 65 72 54 6F 6F 6C 41 75 67 6D 65 6E 74 73),
0000025B             STR: 'MasterAugmentTable' (12 00 00 00 4D 61 73 74 65 72 41 75 67 6D 65 6E 74 54 61 62 6C 65),
00000272             STR: 'GetAugmentTable' (0F 00 00 00 47 65 74 41 75 67 6D 65 6E 74 54 61 62 6C 65)
                 )
             varnames:
00000286         TUPLE: (
0000028B             STR: 'GlovesAugments' (0E 00 00 00 47 6C 6F 76 65 73 41 75 67 6D 65 6E 74 73),
0000029E             STR: 'MasterAugmentTable' (12 00 00 00 4D 61 73 74 65 72 41 75 67 6D 65 6E 74 54 61 62 6C 65),
000002B5             STR: 'obj' (03 00 00 00 6F 62 6A),
000002BD             STR: 'HackerToolAugments' (12 00 00 00 48 61 63 6B 65 72 54 6F 6F 6C 41 75 67 6D 65 6E 74 73),
000002D4             STR: 'GlassesAugments' (0F 00 00 00 47 6C 61 73 73 65 73 41 75 67 6D 65 6E 74 73),
000002E8             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
000002F6             STR: 'ShoesAugments' (0D 00 00 00 53 68 6F 65 73 41 75 67 6D 65 6E 74 73),
00000308             STR: 'WeaponAugments' (0E 00 00 00 57 65 61 70 6F 6E 41 75 67 6D 65 6E 74 73),
0000031B             STR: 'HatAugments' (0B 00 00 00 48 61 74 41 75 67 6D 65 6E 74 73),
0000032B             STR: 'CoatAugments' (0C 00 00 00 43 6F 61 74 41 75 67 6D 65 6E 74 73),
0000033C             STR: 'PantsAugments' (0D 00 00 00 50 61 6E 74 73 41 75 67 6D 65 6E 74 73),
0000034E             STR: 'GetAugmentTable' (0F 00 00 00 47 65 74 41 75 67 6D 65 6E 74 54 61 62 6C 65),
00000362             STR: 'ShirtAugments' (0D 00 00 00 53 68 69 72 74 41 75 67 6D 65 6E 74 73)
                 )
             freevars:
00000374         TUPLE: ()
             cellvars:
00000379         TUPLE: ()
             filename:
0000037E         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\augments.py' (40 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 75 67 6D 65 6E 74 73 2E 70 79)
             name:
000003C3         STR: '?' (01 00 00 00 3F)
             firslineno:
000003C9         LONG: 2L (02 00 00 00)
             lnotab:
000003CD         STR: "\t\x01\t\x12\x06\x03\x06\x03\x06\x03\x06\x03\x06\x03\x06\x03\x06\x03\x06\x03\x06\x07'\x0e" (18 00 00 00 09 01 09 12 06 03 06 03 06 03 06 03 06 03 06 03 06 03 06 03 06 07 27 0E)

