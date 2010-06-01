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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00Z\x02\x00d\x01\x00Z\x03\x00d\x02\x00Z\x04\x00d\x03\x00Z\x05\x00d\x04\x00Z\x06\x00d\x05\x00d\x05\x00>Z\x07\x00d\x06\x00\x84\x00\x00Z\x08\x00d\x07\x00\x84\x00\x00Z\t\x00d\x08\x00\x84\x00\x00Z\n\x00d\t\x00\x84\x00\x00Z\x0b\x00d\n\x00\x84\x00\x00Z\x0c\x00d\x0b\x00\x84\x00\x00Z\r\x00d\x00\x00S' (77 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 5A 02 00 64 01 00 5A 03 00 64 02 00 5A 04 00 64 03 00 5A 05 00 64 04 00 5A 06 00 64 05 00 64 05 00 3E 5A 07 00 64 06 00 84 00 00 5A 08 00 64 07 00 84 00 00 5A 09 00 64 08 00 84 00 00 5A 0A 00 64 09 00 84 00 00 5A 0B 00 64 0A 00 84 00 00 5A 0C 00 64 0B 00 84 00 00 5A 0D 00 64 00 00 53)
                 00000000     64 - LOAD_CONST          None
                 00000003     6B - IMPORT_NAME         'traceback'
                 00000006     5A - STORE_NAME          'traceback'
                 00000009     64 - LOAD_CONST          None
                 0000000C     6B - IMPORT_NAME         'obj'
                 0000000F     5A - STORE_NAME          'obj'
                 00000012     64 - LOAD_CONST          None
                 00000015     6B - IMPORT_NAME         'math'
                 00000018     5A - STORE_NAME          'math'
                 0000001B     64 - LOAD_CONST          203
                 0000001E     5A - STORE_NAME          'RECAPTURE2_FEATURE'
                 00000021     64 - LOAD_CONST          202
                 00000024     5A - STORE_NAME          'RECAPTURE1_FEATURE'
                 00000027     64 - LOAD_CONST          201
                 0000002A     5A - STORE_NAME          'HYPER_JUMP_BETA_FEATURE'
                 0000002D     64 - LOAD_CONST          200
                 00000030     5A - STORE_NAME          'MOBIUS_CODE_CONVERSION_FEATURE'
                 00000033     64 - LOAD_CONST          1
                 00000036     64 - LOAD_CONST          1
                 00000039     3E - BINARY_LSHIFT       
                 0000003A     5A - STORE_NAME          'FREE_TRAIL_ACCOUNT_BIT'
                 0000003D     64 - LOAD_CONST          CODE('IsFreeTrail')
                 00000040     84 - MAKE_FUNCTION       r0000
                 00000043     5A - STORE_NAME          'IsFreeTrail'
                 00000046     64 - LOAD_CONST          CODE('EmailAbility')
                 00000049     84 - MAKE_FUNCTION       r0000
                 0000004C     5A - STORE_NAME          'EmailAbility'
                 0000004F     64 - LOAD_CONST          CODE('EmailItem')
                 00000052     84 - MAKE_FUNCTION       r0000
                 00000055     5A - STORE_NAME          'EmailItem'
                 00000058     64 - LOAD_CONST          CODE('HandleAction')
                 0000005B     84 - MAKE_FUNCTION       r0000
                 0000005E     5A - STORE_NAME          'HandleAction'
                 00000061     64 - LOAD_CONST          CODE('HandleConditional')
                 00000064     84 - MAKE_FUNCTION       r0000
                 00000067     5A - STORE_NAME          'HandleConditional'
                 0000006A     64 - LOAD_CONST          CODE('HandleOnGameFeatures')
                 0000006D     84 - MAKE_FUNCTION       r0000
                 00000070     5A - STORE_NAME          'HandleOnGameFeatures'
                 00000073     64 - LOAD_CONST          None
                 00000076     53 - RETURN_VALUE        
             consts:
00000095         TUPLE: (
0000009A             None (4E),
0000009B             INT: 203 (CB 00 00 00),
000000A0             INT: 202 (CA 00 00 00),
000000A5             INT: 201 (C9 00 00 00),
000000AA             INT: 200 (C8 00 00 00),
000000AF             INT: 1 (01 00 00 00),
000000B4             CODE:
                         argcount:
000000B5                     LONG: 1L (01 00 00 00)
                         nlocals:
000000B9                     LONG: 1L (01 00 00 00)
                         stacksize:
000000BD                     LONG: 2L (02 00 00 00)
                         flags:
000000C1                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000000C5                     STR: '|\x00\x00t\x01\x00@o\x08\x00\x01d\x01\x00Sn\x01\x00\x01d\x02\x00Sd\x00\x00S' (1B 00 00 00 7C 00 00 74 01 00 40 6F 08 00 01 64 01 00 53 6E 01 00 01 64 02 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'subscriptionData'
                             00000003     74 - LOAD_GLOBAL         'FREE_TRAIL_ACCOUNT_BIT'
                             00000006     40 - BINARY_AND          
                             00000007     6F - JUMP_IF_FALSE       -> 00000012
                             0000000A     01 - POP_TOP             
                             0000000B     64 - LOAD_CONST          1
                             0000000E     53 - RETURN_VALUE        
                             0000000F     6E - JUMP_FORWARD        -> 00000013
                             00000012     01 - POP_TOP             
                             00000013     64 - LOAD_CONST          0
                             00000016     53 - RETURN_VALUE        
                             00000017     64 - LOAD_CONST          None
                             0000001A     53 - RETURN_VALUE        
                         consts:
000000E5                     TUPLE: (
000000EA                         None (4E),
000000EB                         INT: 1 (01 00 00 00),
000000F0                         INT: 0 (00 00 00 00)
                             )
                         names:
000000F5                     TUPLE: (
000000FA                         STR: 'subscriptionData' (10 00 00 00 73 75 62 73 63 72 69 70 74 69 6F 6E 44 61 74 61),
0000010F                         STR: 'FREE_TRAIL_ACCOUNT_BIT' (16 00 00 00 46 52 45 45 5F 54 52 41 49 4C 5F 41 43 43 4F 55 4E 54 5F 42 49 54)
                             )
                         varnames:
0000012A                     TUPLE: (
0000012F                         STR: 'subscriptionData' (10 00 00 00 73 75 62 73 63 72 69 70 74 69 6F 6E 44 61 74 61)
                             )
                         freevars:
00000144                     TUPLE: ()
                         cellvars:
00000149                     TUPLE: ()
                         filename:
0000014E                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\gameFeatures.py' (44 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 67 61 6D 65 46 65 61 74 75 72 65 73 2E 70 79)
                         name:
00000197                     STR: 'IsFreeTrail' (0B 00 00 00 49 73 46 72 65 65 54 72 61 69 6C)
                         firslineno:
000001A7                     LONG: 12L (0C 00 00 00)
                         lnotab:
000001AB                     STR: '\x00\x02\x0b\x01\x08\x02' (06 00 00 00 00 02 0B 01 08 02),
000001B6             CODE:
                         argcount:
000001B7                     LONG: 2L (02 00 00 00)
                         nlocals:
000001BB                     LONG: 2L (02 00 00 00)
                         stacksize:
000001BF                     LONG: 2L (02 00 00 00)
                         flags:
000001C3                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000001C7                     STR: '|\x00\x00i\x01\x00i\x02\x00|\x01\x00\x83\x01\x00\x01d\x00\x00S' (14 00 00 00 7C 00 00 69 01 00 69 02 00 7C 01 00 83 01 00 01 64 00 00 53)
                             00000000     7C - LOAD_FAST           'character'
                             00000003     69 - LOAD_ATTR           'Inventory'
                             00000006     69 - LOAD_ATTR           'addAbilityCode'
                             00000009     7C - LOAD_FAST           'abilityID'
                             0000000C     83 - CALL_FUNCTION       r0001
                             0000000F     01 - POP_TOP             
                             00000010     64 - LOAD_CONST          None
                             00000013     53 - RETURN_VALUE        
                         consts:
000001E0                     TUPLE: (
000001E5                         None (4E)
                             )
                         names:
000001E6                     TUPLE: (
000001EB                         STR: 'character' (09 00 00 00 63 68 61 72 61 63 74 65 72),
000001F9                         STR: 'Inventory' (09 00 00 00 49 6E 76 65 6E 74 6F 72 79),
00000207                         STR: 'addAbilityCode' (0E 00 00 00 61 64 64 41 62 69 6C 69 74 79 43 6F 64 65),
0000021A                         STR: 'abilityID' (09 00 00 00 61 62 69 6C 69 74 79 49 44)
                             )
                         varnames:
00000228                     TUPLE: (
0000022D                         STR: 'character' (09 00 00 00 63 68 61 72 61 63 74 65 72),
0000023B                         STR: 'abilityID' (09 00 00 00 61 62 69 6C 69 74 79 49 44)
                             )
                         freevars:
00000249                     TUPLE: ()
                         cellvars:
0000024E                     TUPLE: ()
                         filename:
00000253                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\gameFeatures.py' (44 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 67 61 6D 65 46 65 61 74 75 72 65 73 2E 70 79)
                         name:
0000029C                     STR: 'EmailAbility' (0C 00 00 00 45 6D 61 69 6C 41 62 69 6C 69 74 79)
                         firslineno:
000002AD                     LONG: 19L (13 00 00 00)
                         lnotab:
000002B1                     STR: '\x00\x01' (02 00 00 00 00 01),
000002B8             CODE:
                         argcount:
000002B9                     LONG: 2L (02 00 00 00)
                         nlocals:
000002BD                     LONG: 2L (02 00 00 00)
                         stacksize:
000002C1                     LONG: 3L (03 00 00 00)
                         flags:
000002C5                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000002C9                     STR: '|\x00\x00i\x01\x00i\x02\x00|\x01\x00d\x01\x00\x83\x02\x00\x01d\x00\x00S' (17 00 00 00 7C 00 00 69 01 00 69 02 00 7C 01 00 64 01 00 83 02 00 01 64 00 00 53)
                             00000000     7C - LOAD_FAST           'character'
                             00000003     69 - LOAD_ATTR           'Inventory'
                             00000006     69 - LOAD_ATTR           'addItem'
                             00000009     7C - LOAD_FAST           'itemID'
                             0000000C     64 - LOAD_CONST          0
                             0000000F     83 - CALL_FUNCTION       r0002
                             00000012     01 - POP_TOP             
                             00000013     64 - LOAD_CONST          None
                             00000016     53 - RETURN_VALUE        
                         consts:
000002E5                     TUPLE: (
000002EA                         None (4E),
000002EB                         INT: 0 (00 00 00 00)
                             )
                         names:
000002F0                     TUPLE: (
000002F5                         STR: 'character' (09 00 00 00 63 68 61 72 61 63 74 65 72),
00000303                         STR: 'Inventory' (09 00 00 00 49 6E 76 65 6E 74 6F 72 79),
00000311                         STR: 'addItem' (07 00 00 00 61 64 64 49 74 65 6D),
0000031D                         STR: 'itemID' (06 00 00 00 69 74 65 6D 49 44)
                             )
                         varnames:
00000328                     TUPLE: (
0000032D                         STR: 'character' (09 00 00 00 63 68 61 72 61 63 74 65 72),
0000033B                         STR: 'itemID' (06 00 00 00 69 74 65 6D 49 44)
                             )
                         freevars:
00000346                     TUPLE: ()
                         cellvars:
0000034B                     TUPLE: ()
                         filename:
00000350                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\gameFeatures.py' (44 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 67 61 6D 65 46 65 61 74 75 72 65 73 2E 70 79)
                         name:
00000399                     STR: 'EmailItem' (09 00 00 00 45 6D 61 69 6C 49 74 65 6D)
                         firslineno:
000003A7                     LONG: 22L (16 00 00 00)
                         lnotab:
000003AB                     STR: '\x00\x01' (02 00 00 00 00 01),
000003B2             CODE:
                         argcount:
000003B3                     LONG: 2L (02 00 00 00)
                         nlocals:
000003B7                     LONG: 2L (02 00 00 00)
                         stacksize:
000003BB                     LONG: 3L (03 00 00 00)
                         flags:
000003BF                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000003C3                     STR: '|\x01\x00i\x01\x00t\x02\x00j\x02\x00o\x11\x00\x01t\x03\x00|\x00\x00t\x05\x00\x83\x02\x00Sn\xa6\x00\x01|\x01\x00i\x01\x00t\x06\x00j\x02\x00o\x11\x00\x01t\x03\x00|\x00\x00t\x07\x00\x83\x02\x00Sn\x85\x00\x01|\x01\x00i\x01\x00t\x08\x00j\x02\x00o2\x00\x01|\x00\x00i\t\x00i\n\x00\x83\x00\x00o\x11\x00\x01t\x0b\x00|\x00\x00d\x01\x00\x83\x02\x00Sq\xc6\x00\x01t\x0b\x00|\x00\x00d\x02\x00\x83\x02\x00SnC\x00\x01|\x01\x00i\x01\x00t\x0c\x00j\x02\x00o2\x00\x01|\x00\x00i\t\x00i\n\x00\x83\x00\x00o\x11\x00\x01t\x0b\x00|\x00\x00d\x03\x00\x83\x02\x00Sq\xc6\x00\x01t\x0b\x00|\x00\x00d\x04\x00\x83\x02\x00Sn\x01\x00\x01d\x00\x00S' (CA 00 00 00 7C 01 00 69 01 00 74 02 00 6A 02 00 6F 11 00 01 74 03 00 7C 00 00 74 05 00 83 02 00 53 6E A6 00 01 7C 01 00 69 01 00 74 06 00 6A 02 00 6F 11 00 01 74 03 00 7C 00 00 74 07 00 83 02 00 53 6E 85 00 01 7C 01 00 69 01 00 74 08 00 6A 02 00 6F 32 00 01 7C 00 00 69 09 00 69 0A 00 83 00 00 6F 11 00 01 74 0B 00 7C 00 00 64 01 00 83 02 00 53 71 C6 00 01 74 0B 00 7C 00 00 64 02 00 83 02 00 53 6E 43 00 01 7C 01 00 69 01 00 74 0C 00 6A 02 00 6F 32 00 01 7C 00 00 69 09 00 69 0A 00 83 00 00 6F 11 00 01 74 0B 00 7C 00 00 64 03 00 83 02 00 53 71 C6 00 01 74 0B 00 7C 00 00 64 04 00 83 02 00 53 6E 01 00 01 64 00 00 53)
                             00000000     7C - LOAD_FAST           'gameFeature'
                             00000003     69 - LOAD_ATTR           'featureID'
                             00000006     74 - LOAD_GLOBAL         'HYPER_JUMP_BETA_FEATURE'
                             00000009     6A - COMPARE_OP          "=="
                             0000000C     6F - JUMP_IF_FALSE       -> 00000020
                             0000000F     01 - POP_TOP             
                             00000010     74 - LOAD_GLOBAL         'EmailAbility'
                             00000013     7C - LOAD_FAST           'character'
                             00000016     74 - LOAD_GLOBAL         'PreOrderHyperLeapAbility'
                             00000019     83 - CALL_FUNCTION       r0002
                             0000001C     53 - RETURN_VALUE        
                             0000001D     6E - JUMP_FORWARD        -> 000000C6
                             00000020     01 - POP_TOP             
                             00000021     7C - LOAD_FAST           'gameFeature'
                             00000024     69 - LOAD_ATTR           'featureID'
                             00000027     74 - LOAD_GLOBAL         'MOBIUS_CODE_CONVERSION_FEATURE'
                             0000002A     6A - COMPARE_OP          "=="
                             0000002D     6F - JUMP_IF_FALSE       -> 00000041
                             00000030     01 - POP_TOP             
                             00000031     74 - LOAD_GLOBAL         'EmailAbility'
                             00000034     7C - LOAD_FAST           'character'
                             00000037     74 - LOAD_GLOBAL         'MobiusCodeAbility'
                             0000003A     83 - CALL_FUNCTION       r0002
                             0000003D     53 - RETURN_VALUE        
                             0000003E     6E - JUMP_FORWARD        -> 000000C6
                             00000041     01 - POP_TOP             
                             00000042     7C - LOAD_FAST           'gameFeature'
                             00000045     69 - LOAD_ATTR           'featureID'
                             00000048     74 - LOAD_GLOBAL         'RECAPTURE1_FEATURE'
                             0000004B     6A - COMPARE_OP          "=="
                             0000004E     6F - JUMP_IF_FALSE       -> 00000083
                             00000051     01 - POP_TOP             
                             00000052     7C - LOAD_FAST           'character'
                             00000055     69 - LOAD_ATTR           'Inventory'
                             00000058     69 - LOAD_ATTR           'isMale'
                             0000005B     83 - CALL_FUNCTION       r0000
                             0000005E     6F - JUMP_IF_FALSE       -> 00000072
                             00000061     01 - POP_TOP             
                             00000062     74 - LOAD_GLOBAL         'EmailItem'
                             00000065     7C - LOAD_FAST           'character'
                             00000068     64 - LOAD_CONST          48122
                             0000006B     83 - CALL_FUNCTION       r0002
                             0000006E     53 - RETURN_VALUE        
                             0000006F     71 - JUMP_ABSOLUTE       -> 000000C6
                             00000072     01 - POP_TOP             
                             00000073     74 - LOAD_GLOBAL         'EmailItem'
                             00000076     7C - LOAD_FAST           'character'
                             00000079     64 - LOAD_CONST          48120
                             0000007C     83 - CALL_FUNCTION       r0002
                             0000007F     53 - RETURN_VALUE        
                             00000080     6E - JUMP_FORWARD        -> 000000C6
                             00000083     01 - POP_TOP             
                             00000084     7C - LOAD_FAST           'gameFeature'
                             00000087     69 - LOAD_ATTR           'featureID'
                             0000008A     74 - LOAD_GLOBAL         'RECAPTURE2_FEATURE'
                             0000008D     6A - COMPARE_OP          "=="
                             00000090     6F - JUMP_IF_FALSE       -> 000000C5
                             00000093     01 - POP_TOP             
                             00000094     7C - LOAD_FAST           'character'
                             00000097     69 - LOAD_ATTR           'Inventory'
                             0000009A     69 - LOAD_ATTR           'isMale'
                             0000009D     83 - CALL_FUNCTION       r0000
                             000000A0     6F - JUMP_IF_FALSE       -> 000000B4
                             000000A3     01 - POP_TOP             
                             000000A4     74 - LOAD_GLOBAL         'EmailItem'
                             000000A7     7C - LOAD_FAST           'character'
                             000000AA     64 - LOAD_CONST          48123
                             000000AD     83 - CALL_FUNCTION       r0002
                             000000B0     53 - RETURN_VALUE        
                             000000B1     71 - JUMP_ABSOLUTE       -> 000000C6
                             000000B4     01 - POP_TOP             
                             000000B5     74 - LOAD_GLOBAL         'EmailItem'
                             000000B8     7C - LOAD_FAST           'character'
                             000000BB     64 - LOAD_CONST          48121
                             000000BE     83 - CALL_FUNCTION       r0002
                             000000C1     53 - RETURN_VALUE        
                             000000C2     6E - JUMP_FORWARD        -> 000000C6
                             000000C5     01 - POP_TOP             
                             000000C6     64 - LOAD_CONST          None
                             000000C9     53 - RETURN_VALUE        
                         consts:
00000492                     TUPLE: (
00000497                         None (4E),
00000498                         INT: 48122 (FA BB 00 00),
0000049D                         INT: 48120 (F8 BB 00 00),
000004A2                         INT: 48123 (FB BB 00 00),
000004A7                         INT: 48121 (F9 BB 00 00)
                             )
                         names:
000004AC                     TUPLE: (
000004B1                         STR: 'gameFeature' (0B 00 00 00 67 61 6D 65 46 65 61 74 75 72 65),
000004C1                         STR: 'featureID' (09 00 00 00 66 65 61 74 75 72 65 49 44),
000004CF                         STR: 'HYPER_JUMP_BETA_FEATURE' (17 00 00 00 48 59 50 45 52 5F 4A 55 4D 50 5F 42 45 54 41 5F 46 45 41 54 55 52 45),
000004EB                         STR: 'EmailAbility' (0C 00 00 00 45 6D 61 69 6C 41 62 69 6C 69 74 79),
000004FC                         STR: 'character' (09 00 00 00 63 68 61 72 61 63 74 65 72),
0000050A                         STR: 'PreOrderHyperLeapAbility' (18 00 00 00 50 72 65 4F 72 64 65 72 48 79 70 65 72 4C 65 61 70 41 62 69 6C 69 74 79),
00000527                         STR: 'MOBIUS_CODE_CONVERSION_FEATURE' (1E 00 00 00 4D 4F 42 49 55 53 5F 43 4F 44 45 5F 43 4F 4E 56 45 52 53 49 4F 4E 5F 46 45 41 54 55 52 45),
0000054A                         STR: 'MobiusCodeAbility' (11 00 00 00 4D 6F 62 69 75 73 43 6F 64 65 41 62 69 6C 69 74 79),
00000560                         STR: 'RECAPTURE1_FEATURE' (12 00 00 00 52 45 43 41 50 54 55 52 45 31 5F 46 45 41 54 55 52 45),
00000577                         STR: 'Inventory' (09 00 00 00 49 6E 76 65 6E 74 6F 72 79),
00000585                         STR: 'isMale' (06 00 00 00 69 73 4D 61 6C 65),
00000590                         STR: 'EmailItem' (09 00 00 00 45 6D 61 69 6C 49 74 65 6D),
0000059E                         STR: 'RECAPTURE2_FEATURE' (12 00 00 00 52 45 43 41 50 54 55 52 45 32 5F 46 45 41 54 55 52 45)
                             )
                         varnames:
000005B5                     TUPLE: (
000005BA                         STR: 'character' (09 00 00 00 63 68 61 72 61 63 74 65 72),
000005C8                         STR: 'gameFeature' (0B 00 00 00 67 61 6D 65 46 65 61 74 75 72 65)
                             )
                         freevars:
000005D8                     TUPLE: ()
                         cellvars:
000005DD                     TUPLE: ()
                         filename:
000005E2                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\gameFeatures.py' (44 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 67 61 6D 65 46 65 61 74 75 72 65 73 2E 70 79)
                         name:
0000062B                     STR: 'HandleAction' (0C 00 00 00 48 61 6E 64 6C 65 41 63 74 69 6F 6E)
                         firslineno:
0000063C                     LONG: 25L (19 00 00 00)
                         lnotab:
00000640                     STR: '\x00\x02\x10\x01\x11\x01\x10\x01\x11\x02\x10\x01\x10\x01\x11\x02\x11\x02\x10\x01\x10\x01\x11\x02' (18 00 00 00 00 02 10 01 11 01 10 01 11 02 10 01 10 01 11 02 11 02 10 01 10 01 11 02),
0000065D             CODE:
                         argcount:
0000065E                     LONG: 3L (03 00 00 00)
                         nlocals:
00000662                     LONG: 4L (04 00 00 00)
                         stacksize:
00000666                     LONG: 2L (02 00 00 00)
                         flags:
0000066A                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000066E                     STR: 't\x00\x00|\x02\x00\x83\x01\x00}\x03\x00|\x01\x00i\x04\x00t\x05\x00j\x02\x00o&\x00\x01|\x01\x00i\x06\x00o\r\x00\x01|\x01\x00i\x07\x00d\x01\x00j\x04\x00o\x08\x00\x01t\x08\x00Sq\xfc\x00\x01n\xbb\x00\x01|\x01\x00i\x04\x00t\t\x00j\x02\x00o.\x00\x01|\x03\x00\x0co\x17\x00\x01|\x01\x00i\x06\x00o\r\x00\x01|\x01\x00i\x07\x00d\x01\x00j\x04\x00o\x08\x00\x01t\x08\x00Sq\xfc\x00\x01n}\x00\x01|\x01\x00i\x04\x00t\n\x00j\x02\x00o.\x00\x01|\x03\x00\x0co\x17\x00\x01|\x01\x00i\x06\x00o\r\x00\x01|\x01\x00i\x07\x00d\x01\x00j\x04\x00o\x08\x00\x01t\x08\x00Sq\xfc\x00\x01n?\x00\x01|\x01\x00i\x04\x00t\x0b\x00j\x02\x00o.\x00\x01|\x03\x00\x0co\x17\x00\x01|\x01\x00i\x06\x00o\r\x00\x01|\x01\x00i\x07\x00d\x01\x00j\x04\x00o\x08\x00\x01t\x08\x00Sq\xfc\x00\x01n\x01\x00\x01t\x0c\x00Sd\x00\x00S' (04 01 00 00 74 00 00 7C 02 00 83 01 00 7D 03 00 7C 01 00 69 04 00 74 05 00 6A 02 00 6F 26 00 01 7C 01 00 69 06 00 6F 0D 00 01 7C 01 00 69 07 00 64 01 00 6A 04 00 6F 08 00 01 74 08 00 53 71 FC 00 01 6E BB 00 01 7C 01 00 69 04 00 74 09 00 6A 02 00 6F 2E 00 01 7C 03 00 0C 6F 17 00 01 7C 01 00 69 06 00 6F 0D 00 01 7C 01 00 69 07 00 64 01 00 6A 04 00 6F 08 00 01 74 08 00 53 71 FC 00 01 6E 7D 00 01 7C 01 00 69 04 00 74 0A 00 6A 02 00 6F 2E 00 01 7C 03 00 0C 6F 17 00 01 7C 01 00 69 06 00 6F 0D 00 01 7C 01 00 69 07 00 64 01 00 6A 04 00 6F 08 00 01 74 08 00 53 71 FC 00 01 6E 3F 00 01 7C 01 00 69 04 00 74 0B 00 6A 02 00 6F 2E 00 01 7C 03 00 0C 6F 17 00 01 7C 01 00 69 06 00 6F 0D 00 01 7C 01 00 69 07 00 64 01 00 6A 04 00 6F 08 00 01 74 08 00 53 71 FC 00 01 6E 01 00 01 74 0C 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'IsFreeTrail'
                             00000003     7C - LOAD_FAST           'subscriptionData'
                             00000006     83 - CALL_FUNCTION       r0001
                             00000009     7D - STORE_FAST          'isFreeTrailPlayer'
                             0000000C     7C - LOAD_FAST           'gameFeature'
                             0000000F     69 - LOAD_ATTR           'featureID'
                             00000012     74 - LOAD_GLOBAL         'HYPER_JUMP_BETA_FEATURE'
                             00000015     6A - COMPARE_OP          "=="
                             00000018     6F - JUMP_IF_FALSE       -> 00000041
                             0000001B     01 - POP_TOP             
                             0000001C     7C - LOAD_FAST           'gameFeature'
                             0000001F     69 - LOAD_ATTR           'isActive'
                             00000022     6F - JUMP_IF_FALSE       -> 00000032
                             00000025     01 - POP_TOP             
                             00000026     7C - LOAD_FAST           'gameFeature'
                             00000029     69 - LOAD_ATTR           'consumeCount'
                             0000002C     64 - LOAD_CONST          0
                             0000002F     6A - COMPARE_OP          ">"
                             00000032     6F - JUMP_IF_FALSE       -> 0000003D
                             00000035     01 - POP_TOP             
                             00000036     74 - LOAD_GLOBAL         'True'
                             00000039     53 - RETURN_VALUE        
                             0000003A     71 - JUMP_ABSOLUTE       -> 000000FC
                             0000003D     01 - POP_TOP             
                             0000003E     6E - JUMP_FORWARD        -> 000000FC
                             00000041     01 - POP_TOP             
                             00000042     7C - LOAD_FAST           'gameFeature'
                             00000045     69 - LOAD_ATTR           'featureID'
                             00000048     74 - LOAD_GLOBAL         'MOBIUS_CODE_CONVERSION_FEATURE'
                             0000004B     6A - COMPARE_OP          "=="
                             0000004E     6F - JUMP_IF_FALSE       -> 0000007F
                             00000051     01 - POP_TOP             
                             00000052     7C - LOAD_FAST           'isFreeTrailPlayer'
                             00000055     0C - UNARY_NOT           
                             00000056     6F - JUMP_IF_FALSE       -> 00000070
                             00000059     01 - POP_TOP             
                             0000005A     7C - LOAD_FAST           'gameFeature'
                             0000005D     69 - LOAD_ATTR           'isActive'
                             00000060     6F - JUMP_IF_FALSE       -> 00000070
                             00000063     01 - POP_TOP             
                             00000064     7C - LOAD_FAST           'gameFeature'
                             00000067     69 - LOAD_ATTR           'consumeCount'
                             0000006A     64 - LOAD_CONST          0
                             0000006D     6A - COMPARE_OP          ">"
                             00000070     6F - JUMP_IF_FALSE       -> 0000007B
                             00000073     01 - POP_TOP             
                             00000074     74 - LOAD_GLOBAL         'True'
                             00000077     53 - RETURN_VALUE        
                             00000078     71 - JUMP_ABSOLUTE       -> 000000FC
                             0000007B     01 - POP_TOP             
                             0000007C     6E - JUMP_FORWARD        -> 000000FC
                             0000007F     01 - POP_TOP             
                             00000080     7C - LOAD_FAST           'gameFeature'
                             00000083     69 - LOAD_ATTR           'featureID'
                             00000086     74 - LOAD_GLOBAL         'RECAPTURE1_FEATURE'
                             00000089     6A - COMPARE_OP          "=="
                             0000008C     6F - JUMP_IF_FALSE       -> 000000BD
                             0000008F     01 - POP_TOP             
                             00000090     7C - LOAD_FAST           'isFreeTrailPlayer'
                             00000093     0C - UNARY_NOT           
                             00000094     6F - JUMP_IF_FALSE       -> 000000AE
                             00000097     01 - POP_TOP             
                             00000098     7C - LOAD_FAST           'gameFeature'
                             0000009B     69 - LOAD_ATTR           'isActive'
                             0000009E     6F - JUMP_IF_FALSE       -> 000000AE
                             000000A1     01 - POP_TOP             
                             000000A2     7C - LOAD_FAST           'gameFeature'
                             000000A5     69 - LOAD_ATTR           'consumeCount'
                             000000A8     64 - LOAD_CONST          0
                             000000AB     6A - COMPARE_OP          ">"
                             000000AE     6F - JUMP_IF_FALSE       -> 000000B9
                             000000B1     01 - POP_TOP             
                             000000B2     74 - LOAD_GLOBAL         'True'
                             000000B5     53 - RETURN_VALUE        
                             000000B6     71 - JUMP_ABSOLUTE       -> 000000FC
                             000000B9     01 - POP_TOP             
                             000000BA     6E - JUMP_FORWARD        -> 000000FC
                             000000BD     01 - POP_TOP             
                             000000BE     7C - LOAD_FAST           'gameFeature'
                             000000C1     69 - LOAD_ATTR           'featureID'
                             000000C4     74 - LOAD_GLOBAL         'RECAPTURE2_FEATURE'
                             000000C7     6A - COMPARE_OP          "=="
                             000000CA     6F - JUMP_IF_FALSE       -> 000000FB
                             000000CD     01 - POP_TOP             
                             000000CE     7C - LOAD_FAST           'isFreeTrailPlayer'
                             000000D1     0C - UNARY_NOT           
                             000000D2     6F - JUMP_IF_FALSE       -> 000000EC
                             000000D5     01 - POP_TOP             
                             000000D6     7C - LOAD_FAST           'gameFeature'
                             000000D9     69 - LOAD_ATTR           'isActive'
                             000000DC     6F - JUMP_IF_FALSE       -> 000000EC
                             000000DF     01 - POP_TOP             
                             000000E0     7C - LOAD_FAST           'gameFeature'
                             000000E3     69 - LOAD_ATTR           'consumeCount'
                             000000E6     64 - LOAD_CONST          0
                             000000E9     6A - COMPARE_OP          ">"
                             000000EC     6F - JUMP_IF_FALSE       -> 000000F7
                             000000EF     01 - POP_TOP             
                             000000F0     74 - LOAD_GLOBAL         'True'
                             000000F3     53 - RETURN_VALUE        
                             000000F4     71 - JUMP_ABSOLUTE       -> 000000FC
                             000000F7     01 - POP_TOP             
                             000000F8     6E - JUMP_FORWARD        -> 000000FC
                             000000FB     01 - POP_TOP             
                             000000FC     74 - LOAD_GLOBAL         'False'
                             000000FF     53 - RETURN_VALUE        
                             00000100     64 - LOAD_CONST          None
                             00000103     53 - RETURN_VALUE        
                         consts:
00000777                     TUPLE: (
0000077C                         None (4E),
0000077D                         INT: 0 (00 00 00 00)
                             )
                         names:
00000782                     TUPLE: (
00000787                         STR: 'IsFreeTrail' (0B 00 00 00 49 73 46 72 65 65 54 72 61 69 6C),
00000797                         STR: 'subscriptionData' (10 00 00 00 73 75 62 73 63 72 69 70 74 69 6F 6E 44 61 74 61),
000007AC                         STR: 'isFreeTrailPlayer' (11 00 00 00 69 73 46 72 65 65 54 72 61 69 6C 50 6C 61 79 65 72),
000007C2                         STR: 'gameFeature' (0B 00 00 00 67 61 6D 65 46 65 61 74 75 72 65),
000007D2                         STR: 'featureID' (09 00 00 00 66 65 61 74 75 72 65 49 44),
000007E0                         STR: 'HYPER_JUMP_BETA_FEATURE' (17 00 00 00 48 59 50 45 52 5F 4A 55 4D 50 5F 42 45 54 41 5F 46 45 41 54 55 52 45),
000007FC                         STR: 'isActive' (08 00 00 00 69 73 41 63 74 69 76 65),
00000809                         STR: 'consumeCount' (0C 00 00 00 63 6F 6E 73 75 6D 65 43 6F 75 6E 74),
0000081A                         STR: 'True' (04 00 00 00 54 72 75 65),
00000823                         STR: 'MOBIUS_CODE_CONVERSION_FEATURE' (1E 00 00 00 4D 4F 42 49 55 53 5F 43 4F 44 45 5F 43 4F 4E 56 45 52 53 49 4F 4E 5F 46 45 41 54 55 52 45),
00000846                         STR: 'RECAPTURE1_FEATURE' (12 00 00 00 52 45 43 41 50 54 55 52 45 31 5F 46 45 41 54 55 52 45),
0000085D                         STR: 'RECAPTURE2_FEATURE' (12 00 00 00 52 45 43 41 50 54 55 52 45 32 5F 46 45 41 54 55 52 45),
00000874                         STR: 'False' (05 00 00 00 46 61 6C 73 65)
                             )
                         varnames:
0000087E                     TUPLE: (
00000883                         STR: 'character' (09 00 00 00 63 68 61 72 61 63 74 65 72),
00000891                         STR: 'gameFeature' (0B 00 00 00 67 61 6D 65 46 65 61 74 75 72 65),
000008A1                         STR: 'subscriptionData' (10 00 00 00 73 75 62 73 63 72 69 70 74 69 6F 6E 44 61 74 61),
000008B6                         STR: 'isFreeTrailPlayer' (11 00 00 00 69 73 46 72 65 65 54 72 61 69 6C 50 6C 61 79 65 72)
                             )
                         freevars:
000008CC                     TUPLE: ()
                         cellvars:
000008D1                     TUPLE: ()
                         filename:
000008D6                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\gameFeatures.py' (44 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 67 61 6D 65 46 65 61 74 75 72 65 73 2E 70 79)
                         name:
0000091F                     STR: 'HandleConditional' (11 00 00 00 48 61 6E 64 6C 65 43 6F 6E 64 69 74 69 6F 6E 61 6C)
                         firslineno:
00000935                     LONG: 44L (2C 00 00 00)
                         lnotab:
00000939                     STR: '\x00\x02\x0c\x03\x10\x01\x1a\x01\x0c\x03\x10\x01"\x01\x0c\x02\x10\x01"\x01\x0c\x02\x10\x01"\x01\x0c\x03' (1C 00 00 00 00 02 0C 03 10 01 1A 01 0C 03 10 01 22 01 0C 02 10 01 22 01 0C 02 10 01 22 01 0C 03),
0000095A             CODE:
                         argcount:
0000095B                     LONG: 3L (03 00 00 00)
                         nlocals:
0000095F                     LONG: 7L (07 00 00 00)
                         stacksize:
00000963                     LONG: 5L (05 00 00 00)
                         flags:
00000967                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000096B                     STR: 'g\x00\x00}\x05\x00t\x01\x00|\x02\x00\x83\x01\x00}\x04\x00xK\x00|\x01\x00D]C\x00}\x03\x00t\x06\x00|\x00\x00|\x03\x00|\x02\x00\x83\x03\x00}\x06\x00|\x06\x00t\t\x00j\x02\x00o\x1e\x00\x01t\n\x00|\x00\x00|\x03\x00\x83\x02\x00\x01|\x05\x00i\x0b\x00|\x03\x00\x83\x01\x00\x01q\x19\x00\x01q\x19\x00Wt\x0c\x00|\x05\x00\x83\x01\x00Sd\x00\x00S' (6E 00 00 00 67 00 00 7D 05 00 74 01 00 7C 02 00 83 01 00 7D 04 00 78 4B 00 7C 01 00 44 5D 43 00 7D 03 00 74 06 00 7C 00 00 7C 03 00 7C 02 00 83 03 00 7D 06 00 7C 06 00 74 09 00 6A 02 00 6F 1E 00 01 74 0A 00 7C 00 00 7C 03 00 83 02 00 01 7C 05 00 69 0B 00 7C 03 00 83 01 00 01 71 19 00 01 71 19 00 57 74 0C 00 7C 05 00 83 01 00 53 64 00 00 53)
                             00000000     67 - BUILD_LIST          r0000
                             00000003     7D - STORE_FAST          'usedGameFeatures_list'
                             00000006     74 - LOAD_GLOBAL         'IsFreeTrail'
                             00000009     7C - LOAD_FAST           'subscriptionData'
                             0000000C     83 - CALL_FUNCTION       r0001
                             0000000F     7D - STORE_FAST          'isFreeTrailPlayer'
                             00000012     78 - SETUP_LOOP          -> 00000060
                             00000015     7C - LOAD_FAST           'gameFeatureArray'
                             00000018     44 - GET_ITER            
                             00000019     5D - FOR_ITER            -> 0000005F
                             0000001C     7D - STORE_FAST          'curGameFeature'
                             0000001F     74 - LOAD_GLOBAL         'HandleConditional'
                             00000022     7C - LOAD_FAST           'character'
                             00000025     7C - LOAD_FAST           'curGameFeature'
                             00000028     7C - LOAD_FAST           'subscriptionData'
                             0000002B     83 - CALL_FUNCTION       r0003
                             0000002E     7D - STORE_FAST          'bCanBeUsed'
                             00000031     7C - LOAD_FAST           'bCanBeUsed'
                             00000034     74 - LOAD_GLOBAL         'True'
                             00000037     6A - COMPARE_OP          "=="
                             0000003A     6F - JUMP_IF_FALSE       -> 0000005B
                             0000003D     01 - POP_TOP             
                             0000003E     74 - LOAD_GLOBAL         'HandleAction'
                             00000041     7C - LOAD_FAST           'character'
                             00000044     7C - LOAD_FAST           'curGameFeature'
                             00000047     83 - CALL_FUNCTION       r0002
                             0000004A     01 - POP_TOP             
                             0000004B     7C - LOAD_FAST           'usedGameFeatures_list'
                             0000004E     69 - LOAD_ATTR           'append'
                             00000051     7C - LOAD_FAST           'curGameFeature'
                             00000054     83 - CALL_FUNCTION       r0001
                             00000057     01 - POP_TOP             
                             00000058     71 - JUMP_ABSOLUTE       -> 00000019
                             0000005B     01 - POP_TOP             
                             0000005C     71 - JUMP_ABSOLUTE       -> 00000019
                             0000005F     57 - POP_BLOCK           
                             00000060     74 - LOAD_GLOBAL         'tuple'
                             00000063     7C - LOAD_FAST           'usedGameFeatures_list'
                             00000066     83 - CALL_FUNCTION       r0001
                             00000069     53 - RETURN_VALUE        
                             0000006A     64 - LOAD_CONST          None
                             0000006D     53 - RETURN_VALUE        
                         consts:
000009DE                     TUPLE: (
000009E3                         None (4E)
                             )
                         names:
000009E4                     TUPLE: (
000009E9                         STR: 'usedGameFeatures_list' (15 00 00 00 75 73 65 64 47 61 6D 65 46 65 61 74 75 72 65 73 5F 6C 69 73 74),
00000A03                         STR: 'IsFreeTrail' (0B 00 00 00 49 73 46 72 65 65 54 72 61 69 6C),
00000A13                         STR: 'subscriptionData' (10 00 00 00 73 75 62 73 63 72 69 70 74 69 6F 6E 44 61 74 61),
00000A28                         STR: 'isFreeTrailPlayer' (11 00 00 00 69 73 46 72 65 65 54 72 61 69 6C 50 6C 61 79 65 72),
00000A3E                         STR: 'gameFeatureArray' (10 00 00 00 67 61 6D 65 46 65 61 74 75 72 65 41 72 72 61 79),
00000A53                         STR: 'curGameFeature' (0E 00 00 00 63 75 72 47 61 6D 65 46 65 61 74 75 72 65),
00000A66                         STR: 'HandleConditional' (11 00 00 00 48 61 6E 64 6C 65 43 6F 6E 64 69 74 69 6F 6E 61 6C),
00000A7C                         STR: 'character' (09 00 00 00 63 68 61 72 61 63 74 65 72),
00000A8A                         STR: 'bCanBeUsed' (0A 00 00 00 62 43 61 6E 42 65 55 73 65 64),
00000A99                         STR: 'True' (04 00 00 00 54 72 75 65),
00000AA2                         STR: 'HandleAction' (0C 00 00 00 48 61 6E 64 6C 65 41 63 74 69 6F 6E),
00000AB3                         STR: 'append' (06 00 00 00 61 70 70 65 6E 64),
00000ABE                         STR: 'tuple' (05 00 00 00 74 75 70 6C 65)
                             )
                         varnames:
00000AC8                     TUPLE: (
00000ACD                         STR: 'character' (09 00 00 00 63 68 61 72 61 63 74 65 72),
00000ADB                         STR: 'gameFeatureArray' (10 00 00 00 67 61 6D 65 46 65 61 74 75 72 65 41 72 72 61 79),
00000AF0                         STR: 'subscriptionData' (10 00 00 00 73 75 62 73 63 72 69 70 74 69 6F 6E 44 61 74 61),
00000B05                         STR: 'curGameFeature' (0E 00 00 00 63 75 72 47 61 6D 65 46 65 61 74 75 72 65),
00000B18                         STR: 'isFreeTrailPlayer' (11 00 00 00 69 73 46 72 65 65 54 72 61 69 6C 50 6C 61 79 65 72),
00000B2E                         STR: 'usedGameFeatures_list' (15 00 00 00 75 73 65 64 47 61 6D 65 46 65 61 74 75 72 65 73 5F 6C 69 73 74),
00000B48                         STR: 'bCanBeUsed' (0A 00 00 00 62 43 61 6E 42 65 55 73 65 64)
                             )
                         freevars:
00000B57                     TUPLE: ()
                         cellvars:
00000B5C                     TUPLE: ()
                         filename:
00000B61                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\gameFeatures.py' (44 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 67 61 6D 65 46 65 61 74 75 72 65 73 2E 70 79)
                         name:
00000BAA                     STR: 'HandleOnGameFeatures' (14 00 00 00 48 61 6E 64 6C 65 4F 6E 47 61 6D 65 46 65 61 74 75 72 65 73)
                         firslineno:
00000BC3                     LONG: 70L (46 00 00 00)
                         lnotab:
00000BC7                     STR: '\x00\x01\x06\x01\x0c\x02\x07\x00\x06\x02\x12\x01\r\x01\r\x01\x15\x02' (12 00 00 00 00 01 06 01 0C 02 07 00 06 02 12 01 0D 01 0D 01 15 02)
                 )
             names:
00000BDE         TUPLE: (
00000BE3             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00000BF1             STR: 'obj' (03 00 00 00 6F 62 6A),
00000BF9             STR: 'math' (04 00 00 00 6D 61 74 68),
00000C02             STR: 'RECAPTURE2_FEATURE' (12 00 00 00 52 45 43 41 50 54 55 52 45 32 5F 46 45 41 54 55 52 45),
00000C19             STR: 'RECAPTURE1_FEATURE' (12 00 00 00 52 45 43 41 50 54 55 52 45 31 5F 46 45 41 54 55 52 45),
00000C30             STR: 'HYPER_JUMP_BETA_FEATURE' (17 00 00 00 48 59 50 45 52 5F 4A 55 4D 50 5F 42 45 54 41 5F 46 45 41 54 55 52 45),
00000C4C             STR: 'MOBIUS_CODE_CONVERSION_FEATURE' (1E 00 00 00 4D 4F 42 49 55 53 5F 43 4F 44 45 5F 43 4F 4E 56 45 52 53 49 4F 4E 5F 46 45 41 54 55 52 45),
00000C6F             STR: 'FREE_TRAIL_ACCOUNT_BIT' (16 00 00 00 46 52 45 45 5F 54 52 41 49 4C 5F 41 43 43 4F 55 4E 54 5F 42 49 54),
00000C8A             STR: 'IsFreeTrail' (0B 00 00 00 49 73 46 72 65 65 54 72 61 69 6C),
00000C9A             STR: 'EmailAbility' (0C 00 00 00 45 6D 61 69 6C 41 62 69 6C 69 74 79),
00000CAB             STR: 'EmailItem' (09 00 00 00 45 6D 61 69 6C 49 74 65 6D),
00000CB9             STR: 'HandleAction' (0C 00 00 00 48 61 6E 64 6C 65 41 63 74 69 6F 6E),
00000CCA             STR: 'HandleConditional' (11 00 00 00 48 61 6E 64 6C 65 43 6F 6E 64 69 74 69 6F 6E 61 6C),
00000CE0             STR: 'HandleOnGameFeatures' (14 00 00 00 48 61 6E 64 6C 65 4F 6E 47 61 6D 65 46 65 61 74 75 72 65 73)
                 )
             varnames:
00000CF9         TUPLE: (
00000CFE             STR: 'HYPER_JUMP_BETA_FEATURE' (17 00 00 00 48 59 50 45 52 5F 4A 55 4D 50 5F 42 45 54 41 5F 46 45 41 54 55 52 45),
00000D1A             STR: 'HandleConditional' (11 00 00 00 48 61 6E 64 6C 65 43 6F 6E 64 69 74 69 6F 6E 61 6C),
00000D30             STR: 'obj' (03 00 00 00 6F 62 6A),
00000D38             STR: 'EmailAbility' (0C 00 00 00 45 6D 61 69 6C 41 62 69 6C 69 74 79),
00000D49             STR: 'HandleAction' (0C 00 00 00 48 61 6E 64 6C 65 41 63 74 69 6F 6E),
00000D5A             STR: 'RECAPTURE1_FEATURE' (12 00 00 00 52 45 43 41 50 54 55 52 45 31 5F 46 45 41 54 55 52 45),
00000D71             STR: 'HandleOnGameFeatures' (14 00 00 00 48 61 6E 64 6C 65 4F 6E 47 61 6D 65 46 65 61 74 75 72 65 73),
00000D8A             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00000D98             STR: 'FREE_TRAIL_ACCOUNT_BIT' (16 00 00 00 46 52 45 45 5F 54 52 41 49 4C 5F 41 43 43 4F 55 4E 54 5F 42 49 54),
00000DB3             STR: 'MOBIUS_CODE_CONVERSION_FEATURE' (1E 00 00 00 4D 4F 42 49 55 53 5F 43 4F 44 45 5F 43 4F 4E 56 45 52 53 49 4F 4E 5F 46 45 41 54 55 52 45),
00000DD6             STR: 'RECAPTURE2_FEATURE' (12 00 00 00 52 45 43 41 50 54 55 52 45 32 5F 46 45 41 54 55 52 45),
00000DED             STR: 'EmailItem' (09 00 00 00 45 6D 61 69 6C 49 74 65 6D),
00000DFB             STR: 'IsFreeTrail' (0B 00 00 00 49 73 46 72 65 65 54 72 61 69 6C),
00000E0B             STR: 'math' (04 00 00 00 6D 61 74 68)
                 )
             freevars:
00000E14         TUPLE: ()
             cellvars:
00000E19         TUPLE: ()
             filename:
00000E1E         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\gameFeatures.py' (44 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 67 61 6D 65 46 65 61 74 75 72 65 73 2E 70 79)
             name:
00000E67         STR: '?' (01 00 00 00 3F)
             firslineno:
00000E6D         LONG: 1L (01 00 00 00)
             lnotab:
00000E71         STR: '\t\x01\t\x01\t\x02\x06\x01\x06\x01\x06\x01\x06\x02\n\x02\t\x07\t\x03\t\x03\t\x13\t\x1a' (1A 00 00 00 09 01 09 01 09 02 06 01 06 01 06 01 06 02 0A 02 09 07 09 03 09 03 09 13 09 1A)

