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
00000019         STR: 'd\x00\x00k\x00\x00i\x01\x00Z\x02\x00d\x01\x00\x84\x00\x00Z\x03\x00d\x02\x00\x84\x00\x00Z\x04\x00d\x03\x00\x84\x00\x00Z\x05\x00d\x04\x00\x84\x00\x00Z\x06\x00d\x00\x00S' (34 00 00 00 64 00 00 6B 00 00 69 01 00 5A 02 00 64 01 00 84 00 00 5A 03 00 64 02 00 84 00 00 5A 04 00 64 03 00 84 00 00 5A 05 00 64 04 00 84 00 00 5A 06 00 64 00 00 53)
                 00000000     64 - LOAD_CONST          None
                 00000003     6B - IMPORT_NAME         'ability.utility'
                 00000006     69 - LOAD_ATTR           'utility'
                 00000009     5A - STORE_NAME          'Utility'
                 0000000C     64 - LOAD_CONST          CODE('WriteCodeActivate_Subject')
                 0000000F     84 - MAKE_FUNCTION       r0000
                 00000012     5A - STORE_NAME          'WriteCodeActivate_Subject'
                 00000015     64 - LOAD_CONST          CODE('WriteCodeActivate_Deactivate')
                 00000018     84 - MAKE_FUNCTION       r0000
                 0000001B     5A - STORE_NAME          'WriteCodeActivate_Deactivate'
                 0000001E     64 - LOAD_CONST          CODE('CompileActivate_Subject')
                 00000021     84 - MAKE_FUNCTION       r0000
                 00000024     5A - STORE_NAME          'CompileActivate_Subject'
                 00000027     64 - LOAD_CONST          CODE('CompileActivate_Deactivate')
                 0000002A     84 - MAKE_FUNCTION       r0000
                 0000002D     5A - STORE_NAME          'CompileActivate_Deactivate'
                 00000030     64 - LOAD_CONST          None
                 00000033     53 - RETURN_VALUE        
             consts:
00000052         TUPLE: (
00000057             None (4E),
00000058             CODE:
                         argcount:
00000059                     LONG: 2L (02 00 00 00)
                         nlocals:
0000005D                     LONG: 2L (02 00 00 00)
                         stacksize:
00000061                     LONG: 4L (04 00 00 00)
                         flags:
00000065                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000069                     STR: 't\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01|\x00\x00i\x03\x00i\x04\x00t\x05\x00t\x06\x00d\x02\x00\x83\x03\x00\x01d\x00\x00S' (27 00 00 00 74 00 00 69 01 00 64 01 00 83 01 00 01 7C 00 00 69 03 00 69 04 00 74 05 00 74 06 00 64 02 00 83 03 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          ' Write Code subject '
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     01 - POP_TOP             
                             0000000D     7C - LOAD_FAST           'subject'
                             00000010     69 - LOAD_ATTR           'CharMvt'
                             00000013     69 - LOAD_ATTR           'playScript'
                             00000016     74 - LOAD_GLOBAL         'Stance_StandType'
                             00000019     74 - LOAD_GLOBAL         'Action_Idle'
                             0000001C     64 - LOAD_CONST          1
                             0000001F     83 - CALL_FUNCTION       r0003
                             00000022     01 - POP_TOP             
                             00000023     64 - LOAD_CONST          None
                             00000026     53 - RETURN_VALUE        
                         consts:
00000095                     TUPLE: (
0000009A                         None (4E),
0000009B                         STR: ' Write Code subject ' (14 00 00 00 20 57 72 69 74 65 20 43 6F 64 65 20 73 75 62 6A 65 63 74 20),
000000B4                         INT: 1 (01 00 00 00)
                             )
                         names:
000000B9                     TUPLE: (
000000BE                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000000CA                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
000000E1                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000000ED                         STR: 'CharMvt' (07 00 00 00 43 68 61 72 4D 76 74),
000000F9                         STR: 'playScript' (0A 00 00 00 70 6C 61 79 53 63 72 69 70 74),
00000108                         STR: 'Stance_StandType' (10 00 00 00 53 74 61 6E 63 65 5F 53 74 61 6E 64 54 79 70 65),
0000011D                         STR: 'Action_Idle' (0B 00 00 00 41 63 74 69 6F 6E 5F 49 64 6C 65)
                             )
                         varnames:
0000012D                     TUPLE: (
00000132                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000013E                         STR: 'msg' (03 00 00 00 6D 73 67)
                             )
                         freevars:
00000146                     TUPLE: ()
                         cellvars:
0000014B                     TUPLE: ()
                         filename:
00000150                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\crafting.py' (4F 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 63 72 61 66 74 69 6E 67 2E 70 79)
                         name:
000001A4                     STR: 'WriteCodeActivate_Subject' (19 00 00 00 57 72 69 74 65 43 6F 64 65 41 63 74 69 76 61 74 65 5F 53 75 62 6A 65 63 74)
                         firslineno:
000001C2                     LONG: 8L (08 00 00 00)
                         lnotab:
000001C6                     STR: '\x00\x01\r\x01' (04 00 00 00 00 01 0D 01),
000001CF             CODE:
                         argcount:
000001D0                     LONG: 1L (01 00 00 00)
                         nlocals:
000001D4                     LONG: 1L (01 00 00 00)
                         stacksize:
000001D8                     LONG: 4L (04 00 00 00)
                         flags:
000001DC                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000001E0                     STR: 't\x00\x00i\x01\x00d\x01\x00|\x00\x00i\x03\x00t\x04\x00f\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x03\x00t\x04\x00j\x02\x00o\x17\x00\x01|\x00\x00i\x05\x00i\x06\x00t\x07\x00t\x08\x00\x83\x02\x00\x01n\x01\x00\x01d\x00\x00S' (45 00 00 00 74 00 00 69 01 00 64 01 00 7C 00 00 69 03 00 74 04 00 66 02 00 16 83 01 00 01 7C 00 00 69 03 00 74 04 00 6A 02 00 6F 17 00 01 7C 00 00 69 05 00 69 06 00 74 07 00 74 08 00 83 02 00 01 6E 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          ' Write Code deactivate %d %d'
                             00000009     7C - LOAD_FAST           'subject'
                             0000000C     69 - LOAD_ATTR           'Stance'
                             0000000F     74 - LOAD_GLOBAL         'Stance_StandType'
                             00000012     66 - BUILD_TUPLE         r0002
                             00000015     16 - BINARY_MODULO       
                             00000016     83 - CALL_FUNCTION       r0001
                             00000019     01 - POP_TOP             
                             0000001A     7C - LOAD_FAST           'subject'
                             0000001D     69 - LOAD_ATTR           'Stance'
                             00000020     74 - LOAD_GLOBAL         'Stance_StandType'
                             00000023     6A - COMPARE_OP          "=="
                             00000026     6F - JUMP_IF_FALSE       -> 00000040
                             00000029     01 - POP_TOP             
                             0000002A     7C - LOAD_FAST           'subject'
                             0000002D     69 - LOAD_ATTR           'CharMvt'
                             00000030     69 - LOAD_ATTR           'playScript'
                             00000033     74 - LOAD_GLOBAL         'Stance_Stand'
                             00000036     74 - LOAD_GLOBAL         'Action_Idle'
                             00000039     83 - CALL_FUNCTION       r0002
                             0000003C     01 - POP_TOP             
                             0000003D     6E - JUMP_FORWARD        -> 00000041
                             00000040     01 - POP_TOP             
                             00000041     64 - LOAD_CONST          None
                             00000044     53 - RETURN_VALUE        
                         consts:
0000022A                     TUPLE: (
0000022F                         None (4E),
00000230                         STR: ' Write Code deactivate %d %d' (1C 00 00 00 20 57 72 69 74 65 20 43 6F 64 65 20 64 65 61 63 74 69 76 61 74 65 20 25 64 20 25 64)
                             )
                         names:
00000251                     TUPLE: (
00000256                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000262                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000279                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000285                         STR: 'Stance' (06 00 00 00 53 74 61 6E 63 65),
00000290                         STR: 'Stance_StandType' (10 00 00 00 53 74 61 6E 63 65 5F 53 74 61 6E 64 54 79 70 65),
000002A5                         STR: 'CharMvt' (07 00 00 00 43 68 61 72 4D 76 74),
000002B1                         STR: 'playScript' (0A 00 00 00 70 6C 61 79 53 63 72 69 70 74),
000002C0                         STR: 'Stance_Stand' (0C 00 00 00 53 74 61 6E 63 65 5F 53 74 61 6E 64),
000002D1                         STR: 'Action_Idle' (0B 00 00 00 41 63 74 69 6F 6E 5F 49 64 6C 65)
                             )
                         varnames:
000002E1                     TUPLE: (
000002E6                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74)
                             )
                         freevars:
000002F2                     TUPLE: ()
                         cellvars:
000002F7                     TUPLE: ()
                         filename:
000002FC                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\crafting.py' (4F 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 63 72 61 66 74 69 6E 67 2E 70 79)
                         name:
00000350                     STR: 'WriteCodeActivate_Deactivate' (1C 00 00 00 57 72 69 74 65 43 6F 64 65 41 63 74 69 76 61 74 65 5F 44 65 61 63 74 69 76 61 74 65)
                         firslineno:
00000371                     LONG: 12L (0C 00 00 00)
                         lnotab:
00000375                     STR: '\x00\x01\x1a\x01\x10\x01' (06 00 00 00 00 01 1A 01 10 01),
00000380             CODE:
                         argcount:
00000381                     LONG: 2L (02 00 00 00)
                         nlocals:
00000385                     LONG: 2L (02 00 00 00)
                         stacksize:
00000389                     LONG: 4L (04 00 00 00)
                         flags:
0000038D                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000391                     STR: 't\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01|\x00\x00i\x03\x00i\x04\x00t\x05\x00t\x06\x00d\x02\x00\x83\x03\x00\x01d\x00\x00S' (27 00 00 00 74 00 00 69 01 00 64 01 00 83 01 00 01 7C 00 00 69 03 00 69 04 00 74 05 00 74 06 00 64 02 00 83 03 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          ' Compile subject '
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     01 - POP_TOP             
                             0000000D     7C - LOAD_FAST           'subject'
                             00000010     69 - LOAD_ATTR           'CharMvt'
                             00000013     69 - LOAD_ATTR           'playScript'
                             00000016     74 - LOAD_GLOBAL         'Stance_StandType'
                             00000019     74 - LOAD_GLOBAL         'Action_Idle'
                             0000001C     64 - LOAD_CONST          1
                             0000001F     83 - CALL_FUNCTION       r0003
                             00000022     01 - POP_TOP             
                             00000023     64 - LOAD_CONST          None
                             00000026     53 - RETURN_VALUE        
                         consts:
000003BD                     TUPLE: (
000003C2                         None (4E),
000003C3                         STR: ' Compile subject ' (11 00 00 00 20 43 6F 6D 70 69 6C 65 20 73 75 62 6A 65 63 74 20),
000003D9                         INT: 1 (01 00 00 00)
                             )
                         names:
000003DE                     TUPLE: (
000003E3                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000003EF                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000406                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000412                         STR: 'CharMvt' (07 00 00 00 43 68 61 72 4D 76 74),
0000041E                         STR: 'playScript' (0A 00 00 00 70 6C 61 79 53 63 72 69 70 74),
0000042D                         STR: 'Stance_StandType' (10 00 00 00 53 74 61 6E 63 65 5F 53 74 61 6E 64 54 79 70 65),
00000442                         STR: 'Action_Idle' (0B 00 00 00 41 63 74 69 6F 6E 5F 49 64 6C 65)
                             )
                         varnames:
00000452                     TUPLE: (
00000457                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000463                         STR: 'msg' (03 00 00 00 6D 73 67)
                             )
                         freevars:
0000046B                     TUPLE: ()
                         cellvars:
00000470                     TUPLE: ()
                         filename:
00000475                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\crafting.py' (4F 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 63 72 61 66 74 69 6E 67 2E 70 79)
                         name:
000004C9                     STR: 'CompileActivate_Subject' (17 00 00 00 43 6F 6D 70 69 6C 65 41 63 74 69 76 61 74 65 5F 53 75 62 6A 65 63 74)
                         firslineno:
000004E5                     LONG: 18L (12 00 00 00)
                         lnotab:
000004E9                     STR: '\x00\x01\r\x01' (04 00 00 00 00 01 0D 01),
000004F2             CODE:
                         argcount:
000004F3                     LONG: 1L (01 00 00 00)
                         nlocals:
000004F7                     LONG: 1L (01 00 00 00)
                         stacksize:
000004FB                     LONG: 3L (03 00 00 00)
                         flags:
000004FF                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000503                     STR: 't\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01|\x00\x00i\x03\x00t\x04\x00j\x02\x00o\x17\x00\x01|\x00\x00i\x05\x00i\x06\x00t\x07\x00t\x08\x00\x83\x02\x00\x01n\x01\x00\x01d\x00\x00S' (38 00 00 00 74 00 00 69 01 00 64 01 00 83 01 00 01 7C 00 00 69 03 00 74 04 00 6A 02 00 6F 17 00 01 7C 00 00 69 05 00 69 06 00 74 07 00 74 08 00 83 02 00 01 6E 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          ' Compile deactivate '
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     01 - POP_TOP             
                             0000000D     7C - LOAD_FAST           'subject'
                             00000010     69 - LOAD_ATTR           'Stance'
                             00000013     74 - LOAD_GLOBAL         'Stance_StandType'
                             00000016     6A - COMPARE_OP          "=="
                             00000019     6F - JUMP_IF_FALSE       -> 00000033
                             0000001C     01 - POP_TOP             
                             0000001D     7C - LOAD_FAST           'subject'
                             00000020     69 - LOAD_ATTR           'CharMvt'
                             00000023     69 - LOAD_ATTR           'playScript'
                             00000026     74 - LOAD_GLOBAL         'Stance_Stand'
                             00000029     74 - LOAD_GLOBAL         'Action_Idle'
                             0000002C     83 - CALL_FUNCTION       r0002
                             0000002F     01 - POP_TOP             
                             00000030     6E - JUMP_FORWARD        -> 00000034
                             00000033     01 - POP_TOP             
                             00000034     64 - LOAD_CONST          None
                             00000037     53 - RETURN_VALUE        
                         consts:
00000540                     TUPLE: (
00000545                         None (4E),
00000546                         STR: ' Compile deactivate ' (14 00 00 00 20 43 6F 6D 70 69 6C 65 20 64 65 61 63 74 69 76 61 74 65 20)
                             )
                         names:
0000055F                     TUPLE: (
00000564                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000570                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000587                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000593                         STR: 'Stance' (06 00 00 00 53 74 61 6E 63 65),
0000059E                         STR: 'Stance_StandType' (10 00 00 00 53 74 61 6E 63 65 5F 53 74 61 6E 64 54 79 70 65),
000005B3                         STR: 'CharMvt' (07 00 00 00 43 68 61 72 4D 76 74),
000005BF                         STR: 'playScript' (0A 00 00 00 70 6C 61 79 53 63 72 69 70 74),
000005CE                         STR: 'Stance_Stand' (0C 00 00 00 53 74 61 6E 63 65 5F 53 74 61 6E 64),
000005DF                         STR: 'Action_Idle' (0B 00 00 00 41 63 74 69 6F 6E 5F 49 64 6C 65)
                             )
                         varnames:
000005EF                     TUPLE: (
000005F4                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74)
                             )
                         freevars:
00000600                     TUPLE: ()
                         cellvars:
00000605                     TUPLE: ()
                         filename:
0000060A                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\crafting.py' (4F 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 63 72 61 66 74 69 6E 67 2E 70 79)
                         name:
0000065E                     STR: 'CompileActivate_Deactivate' (1A 00 00 00 43 6F 6D 70 69 6C 65 41 63 74 69 76 61 74 65 5F 44 65 61 63 74 69 76 61 74 65)
                         firslineno:
0000067D                     LONG: 22L (16 00 00 00)
                         lnotab:
00000681                     STR: '\x00\x01\r\x01\x10\x01' (06 00 00 00 00 01 0D 01 10 01)
                 )
             names:
0000068C         TUPLE: (
00000691             STR: 'ability.utility' (0F 00 00 00 61 62 69 6C 69 74 79 2E 75 74 69 6C 69 74 79),
000006A5             STR: 'utility' (07 00 00 00 75 74 69 6C 69 74 79),
000006B1             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000006BD             STR: 'WriteCodeActivate_Subject' (19 00 00 00 57 72 69 74 65 43 6F 64 65 41 63 74 69 76 61 74 65 5F 53 75 62 6A 65 63 74),
000006DB             STR: 'WriteCodeActivate_Deactivate' (1C 00 00 00 57 72 69 74 65 43 6F 64 65 41 63 74 69 76 61 74 65 5F 44 65 61 63 74 69 76 61 74 65),
000006FC             STR: 'CompileActivate_Subject' (17 00 00 00 43 6F 6D 70 69 6C 65 41 63 74 69 76 61 74 65 5F 53 75 62 6A 65 63 74),
00000718             STR: 'CompileActivate_Deactivate' (1A 00 00 00 43 6F 6D 70 69 6C 65 41 63 74 69 76 61 74 65 5F 44 65 61 63 74 69 76 61 74 65)
                 )
             varnames:
00000737         TUPLE: (
0000073C             STR: 'WriteCodeActivate_Subject' (19 00 00 00 57 72 69 74 65 43 6F 64 65 41 63 74 69 76 61 74 65 5F 53 75 62 6A 65 63 74),
0000075A             STR: 'CompileActivate_Subject' (17 00 00 00 43 6F 6D 70 69 6C 65 41 63 74 69 76 61 74 65 5F 53 75 62 6A 65 63 74),
00000776             STR: 'CompileActivate_Deactivate' (1A 00 00 00 43 6F 6D 70 69 6C 65 41 63 74 69 76 61 74 65 5F 44 65 61 63 74 69 76 61 74 65),
00000795             STR: 'WriteCodeActivate_Deactivate' (1C 00 00 00 57 72 69 74 65 43 6F 64 65 41 63 74 69 76 61 74 65 5F 44 65 61 63 74 69 76 61 74 65),
000007B6             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79)
                 )
             freevars:
000007C2         TUPLE: ()
             cellvars:
000007C7         TUPLE: ()
             filename:
000007CC         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\crafting.py' (4F 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 63 72 61 66 74 69 6E 67 2E 70 79)
             name:
00000820         STR: '?' (01 00 00 00 3F)
             firslineno:
00000826         LONG: 4L (04 00 00 00)
             lnotab:
0000082A         STR: '\x0c\x04\t\x04\t\x06\t\x04' (08 00 00 00 0C 04 09 04 09 06 09 04)

