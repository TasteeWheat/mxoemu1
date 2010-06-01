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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00e\x01\x00d\x01\x00d\x02\x00\x83\x02\x00Z\x02\x00e\x00\x00i\x03\x00Z\x04\x00e\x02\x00e\x00\x00_\x03\x00d\x03\x00\x84\x00\x00Z\x05\x00d\x04\x00\x84\x00\x00Z\x06\x00d\x00\x00S' (40 00 00 00 64 00 00 6B 00 00 5A 00 00 65 01 00 64 01 00 64 02 00 83 02 00 5A 02 00 65 00 00 69 03 00 5A 04 00 65 02 00 65 00 00 5F 03 00 64 03 00 84 00 00 5A 05 00 64 04 00 84 00 00 5A 06 00 64 00 00 53)
                 00000000     64 - LOAD_CONST          None
                 00000003     6B - IMPORT_NAME         'sys'
                 00000006     5A - STORE_NAME          'sys'
                 00000009     65 - LOAD_NAME           'file'
                 0000000C     64 - LOAD_CONST          'pyerrors.txt'
                 0000000F     64 - LOAD_CONST          'w'
                 00000012     83 - CALL_FUNCTION       r0002
                 00000015     5A - STORE_NAME          'gNewError'
                 00000018     65 - LOAD_NAME           'sys'
                 0000001B     69 - LOAD_ATTR           'stderr'
                 0000001E     5A - STORE_NAME          'gOldError'
                 00000021     65 - LOAD_NAME           'gNewError'
                 00000024     65 - LOAD_NAME           'sys'
                 00000027     5F - STORE_ATTR          'stderr'
                 0000002A     64 - LOAD_CONST          CODE('flush')
                 0000002D     84 - MAKE_FUNCTION       r0000
                 00000030     5A - STORE_NAME          'flush'
                 00000033     64 - LOAD_CONST          CODE('close')
                 00000036     84 - MAKE_FUNCTION       r0000
                 00000039     5A - STORE_NAME          'close'
                 0000003C     64 - LOAD_CONST          None
                 0000003F     53 - RETURN_VALUE        
             consts:
0000005E         TUPLE: (
00000063             None (4E),
00000064             STR: 'pyerrors.txt' (0C 00 00 00 70 79 65 72 72 6F 72 73 2E 74 78 74),
00000075             STR: 'w' (01 00 00 00 77),
0000007B             CODE:
                         argcount:
0000007C                     LONG: 0L (00 00 00 00)
                         nlocals:
00000080                     LONG: 0L (00 00 00 00)
                         stacksize:
00000084                     LONG: 1L (01 00 00 00)
                         flags:
00000088                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000008C                     STR: 't\x00\x00i\x01\x00\x83\x00\x00\x01d\x00\x00S' (0E 00 00 00 74 00 00 69 01 00 83 00 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'gNewError'
                             00000003     69 - LOAD_ATTR           'flush'
                             00000006     83 - CALL_FUNCTION       r0000
                             00000009     01 - POP_TOP             
                             0000000A     64 - LOAD_CONST          None
                             0000000D     53 - RETURN_VALUE        
                         consts:
0000009F                     TUPLE: (
000000A4                         None (4E)
                             )
                         names:
000000A5                     TUPLE: (
000000AA                         STR: 'gNewError' (09 00 00 00 67 4E 65 77 45 72 72 6F 72),
000000B8                         STR: 'flush' (05 00 00 00 66 6C 75 73 68)
                             )
                         varnames:
000000C2                     TUPLE: ()
                         freevars:
000000C7                     TUPLE: ()
                         cellvars:
000000CC                     TUPLE: ()
                         filename:
000000D1                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\errtofile.py' (41 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 65 72 72 74 6F 66 69 6C 65 2E 70 79)
                         name:
00000117                     STR: 'flush' (05 00 00 00 66 6C 75 73 68)
                         firslineno:
00000121                     LONG: 7L (07 00 00 00)
                         lnotab:
00000125                     STR: '\x00\x01' (02 00 00 00 00 01),
0000012C             CODE:
                         argcount:
0000012D                     LONG: 0L (00 00 00 00)
                         nlocals:
00000131                     LONG: 0L (00 00 00 00)
                         stacksize:
00000135                     LONG: 2L (02 00 00 00)
                         flags:
00000139                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000013D                     STR: 't\x00\x00i\x01\x00\x83\x00\x00\x01t\x02\x00t\x03\x00_\x04\x00d\x00\x00S' (17 00 00 00 74 00 00 69 01 00 83 00 00 01 74 02 00 74 03 00 5F 04 00 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'gNewError'
                             00000003     69 - LOAD_ATTR           'close'
                             00000006     83 - CALL_FUNCTION       r0000
                             00000009     01 - POP_TOP             
                             0000000A     74 - LOAD_GLOBAL         'gOldError'
                             0000000D     74 - LOAD_GLOBAL         'sys'
                             00000010     5F - STORE_ATTR          'stderr'
                             00000013     64 - LOAD_CONST          None
                             00000016     53 - RETURN_VALUE        
                         consts:
00000159                     TUPLE: (
0000015E                         None (4E)
                             )
                         names:
0000015F                     TUPLE: (
00000164                         STR: 'gNewError' (09 00 00 00 67 4E 65 77 45 72 72 6F 72),
00000172                         STR: 'close' (05 00 00 00 63 6C 6F 73 65),
0000017C                         STR: 'gOldError' (09 00 00 00 67 4F 6C 64 45 72 72 6F 72),
0000018A                         STR: 'sys' (03 00 00 00 73 79 73),
00000192                         STR: 'stderr' (06 00 00 00 73 74 64 65 72 72)
                             )
                         varnames:
0000019D                     TUPLE: ()
                         freevars:
000001A2                     TUPLE: ()
                         cellvars:
000001A7                     TUPLE: ()
                         filename:
000001AC                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\errtofile.py' (41 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 65 72 72 74 6F 66 69 6C 65 2E 70 79)
                         name:
000001F2                     STR: 'close' (05 00 00 00 63 6C 6F 73 65)
                         firslineno:
000001FC                     LONG: 10L (0A 00 00 00)
                         lnotab:
00000200                     STR: '\x00\x01\n\x01' (04 00 00 00 00 01 0A 01)
                 )
             names:
00000209         TUPLE: (
0000020E             STR: 'sys' (03 00 00 00 73 79 73),
00000216             STR: 'file' (04 00 00 00 66 69 6C 65),
0000021F             STR: 'gNewError' (09 00 00 00 67 4E 65 77 45 72 72 6F 72),
0000022D             STR: 'stderr' (06 00 00 00 73 74 64 65 72 72),
00000238             STR: 'gOldError' (09 00 00 00 67 4F 6C 64 45 72 72 6F 72),
00000246             STR: 'flush' (05 00 00 00 66 6C 75 73 68),
00000250             STR: 'close' (05 00 00 00 63 6C 6F 73 65)
                 )
             varnames:
0000025A         TUPLE: (
0000025F             STR: 'gOldError' (09 00 00 00 67 4F 6C 64 45 72 72 6F 72),
0000026D             STR: 'sys' (03 00 00 00 73 79 73),
00000275             STR: 'flush' (05 00 00 00 66 6C 75 73 68),
0000027F             STR: 'close' (05 00 00 00 63 6C 6F 73 65),
00000289             STR: 'gNewError' (09 00 00 00 67 4E 65 77 45 72 72 6F 72)
                 )
             freevars:
00000297         TUPLE: ()
             cellvars:
0000029C         TUPLE: ()
             filename:
000002A1         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\errtofile.py' (41 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 65 72 72 74 6F 66 69 6C 65 2E 70 79)
             name:
000002E7         STR: '?' (01 00 00 00 3F)
             firslineno:
000002ED         LONG: 1L (01 00 00 00)
             lnotab:
000002F1         STR: '\t\x02\x0f\x01\t\x01\t\x02\t\x03' (0A 00 00 00 09 02 0F 01 09 01 09 02 09 03)

