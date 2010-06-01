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
00000019         STR: 'd\x00\x00d\x01\x00>Z\x00\x00d\x00\x00d\x00\x00>Z\x01\x00d\x00\x00d\x02\x00>Z\x02\x00d\x00\x00d\x03\x00>Z\x03\x00d\x00\x00d\x04\x00>Z\x04\x00d\x00\x00d\x05\x00>Z\x05\x00d\x00\x00d\x06\x00>Z\x06\x00d\x07\x00S' (4A 00 00 00 64 00 00 64 01 00 3E 5A 00 00 64 00 00 64 00 00 3E 5A 01 00 64 00 00 64 02 00 3E 5A 02 00 64 00 00 64 03 00 3E 5A 03 00 64 00 00 64 04 00 3E 5A 04 00 64 00 00 64 05 00 3E 5A 05 00 64 00 00 64 06 00 3E 5A 06 00 64 07 00 53)
                 00000000     64 - LOAD_CONST          1
                 00000003     64 - LOAD_CONST          0
                 00000006     3E - BINARY_LSHIFT       
                 00000007     5A - STORE_NAME          'DONT_USE'
                 0000000A     64 - LOAD_CONST          1
                 0000000D     64 - LOAD_CONST          1
                 00000010     3E - BINARY_LSHIFT       
                 00000011     5A - STORE_NAME          'Swat'
                 00000014     64 - LOAD_CONST          1
                 00000017     64 - LOAD_CONST          2
                 0000001A     3E - BINARY_LSHIFT       
                 0000001B     5A - STORE_NAME          'Guard'
                 0000001E     64 - LOAD_CONST          1
                 00000021     64 - LOAD_CONST          3
                 00000024     3E - BINARY_LSHIFT       
                 00000025     5A - STORE_NAME          'Werewolf'
                 00000028     64 - LOAD_CONST          1
                 0000002B     64 - LOAD_CONST          4
                 0000002E     3E - BINARY_LSHIFT       
                 0000002F     5A - STORE_NAME          'Vampire'
                 00000032     64 - LOAD_CONST          1
                 00000035     64 - LOAD_CONST          5
                 00000038     3E - BINARY_LSHIFT       
                 00000039     5A - STORE_NAME          'Groupie'
                 0000003C     64 - LOAD_CONST          1
                 0000003F     64 - LOAD_CONST          15
                 00000042     3E - BINARY_LSHIFT       
                 00000043     5A - STORE_NAME          'Invalid_Type'
                 00000046     64 - LOAD_CONST          None
                 00000049     53 - RETURN_VALUE        
             consts:
00000068         TUPLE: (
0000006D             INT: 1 (01 00 00 00),
00000072             INT: 0 (00 00 00 00),
00000077             INT: 2 (02 00 00 00),
0000007C             INT: 3 (03 00 00 00),
00000081             INT: 4 (04 00 00 00),
00000086             INT: 5 (05 00 00 00),
0000008B             INT: 15 (0F 00 00 00),
00000090             None (4E)
                 )
             names:
00000091         TUPLE: (
00000096             STR: 'DONT_USE' (08 00 00 00 44 4F 4E 54 5F 55 53 45),
000000A3             STR: 'Swat' (04 00 00 00 53 77 61 74),
000000AC             STR: 'Guard' (05 00 00 00 47 75 61 72 64),
000000B6             STR: 'Werewolf' (08 00 00 00 57 65 72 65 77 6F 6C 66),
000000C3             STR: 'Vampire' (07 00 00 00 56 61 6D 70 69 72 65),
000000CF             STR: 'Groupie' (07 00 00 00 47 72 6F 75 70 69 65),
000000DB             STR: 'Invalid_Type' (0C 00 00 00 49 6E 76 61 6C 69 64 5F 54 79 70 65)
                 )
             varnames:
000000EC         TUPLE: (
000000F1             STR: 'Invalid_Type' (0C 00 00 00 49 6E 76 61 6C 69 64 5F 54 79 70 65),
00000102             STR: 'Werewolf' (08 00 00 00 57 65 72 65 77 6F 6C 66),
0000010F             STR: 'Vampire' (07 00 00 00 56 61 6D 70 69 72 65),
0000011B             STR: 'Swat' (04 00 00 00 53 77 61 74),
00000124             STR: 'Guard' (05 00 00 00 47 75 61 72 64),
0000012E             STR: 'Groupie' (07 00 00 00 47 72 6F 75 70 69 65),
0000013A             STR: 'DONT_USE' (08 00 00 00 44 4F 4E 54 5F 55 53 45)
                 )
             freevars:
00000147         TUPLE: ()
             cellvars:
0000014C         TUPLE: ()
             filename:
00000151         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\NPCTypes.py' (40 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 4E 50 43 54 79 70 65 73 2E 70 79)
             name:
00000196         STR: '?' (01 00 00 00 3F)
             firslineno:
0000019C         LONG: 2L (02 00 00 00)
             lnotab:
000001A0         STR: '\n\x01\n\x01\n\x01\n\x01\n\x01\n\x02' (0C 00 00 00 0A 01 0A 01 0A 01 0A 01 0A 01 0A 02)

