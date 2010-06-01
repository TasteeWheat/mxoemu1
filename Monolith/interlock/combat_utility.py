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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00Z\x02\x00d\x00\x00k\x03\x00Z\x04\x00d\x00\x00k\x05\x00Z\x05\x00d\x01\x00\x84\x00\x00Z\x06\x00d\x02\x00\x84\x00\x00Z\x07\x00e\x08\x00e\x08\x00d\x03\x00\x84\x02\x00Z\t\x00d\x04\x00\x84\x00\x00Z\n\x00d\x05\x00\x84\x00\x00Z\x0b\x00d\x06\x00\x84\x00\x00Z\x0c\x00d\x07\x00\x84\x00\x00Z\r\x00d\x08\x00\x84\x00\x00Z\x0e\x00d\t\x00\x84\x00\x00Z\x0f\x00d\n\x00\x84\x00\x00Z\x10\x00d\x0b\x00\x84\x00\x00Z\x11\x00d\x0c\x00\x84\x00\x00Z\x12\x00d\r\x00\x84\x00\x00Z\x13\x00e\x14\x00d\x0e\x00\x84\x01\x00Z\x15\x00d\x0f\x00\x84\x00\x00Z\x16\x00d\x10\x00\x84\x00\x00Z\x17\x00d\x11\x00\x84\x00\x00Z\x18\x00d\x12\x00\x84\x00\x00Z\x19\x00d\x13\x00\x84\x00\x00Z\x1a\x00d\x00\x00S' (E5 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 5A 02 00 64 00 00 6B 03 00 5A 04 00 64 00 00 6B 05 00 5A 05 00 64 01 00 84 00 00 5A 06 00 64 02 00 84 00 00 5A 07 00 65 08 00 65 08 00 64 03 00 84 02 00 5A 09 00 64 04 00 84 00 00 5A 0A 00 64 05 00 84 00 00 5A 0B 00 64 06 00 84 00 00 5A 0C 00 64 07 00 84 00 00 5A 0D 00 64 08 00 84 00 00 5A 0E 00 64 09 00 84 00 00 5A 0F 00 64 0A 00 84 00 00 5A 10 00 64 0B 00 84 00 00 5A 11 00 64 0C 00 84 00 00 5A 12 00 64 0D 00 84 00 00 5A 13 00 65 14 00 64 0E 00 84 01 00 5A 15 00 64 0F 00 84 00 00 5A 16 00 64 10 00 84 00 00 5A 17 00 64 11 00 84 00 00 5A 18 00 64 12 00 84 00 00 5A 19 00 64 13 00 84 00 00 5A 1A 00 64 00 00 53)
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
                 0000001E     6B - IMPORT_NAME         'combat_defines'
                 00000021     5A - STORE_NAME          'CD'
                 00000024     64 - LOAD_CONST          None
                 00000027     6B - IMPORT_NAME         'math'
                 0000002A     5A - STORE_NAME          'math'
                 0000002D     64 - LOAD_CONST          CODE('outputToAll')
                 00000030     84 - MAKE_FUNCTION       r0000
                 00000033     5A - STORE_NAME          'outputToAll'
                 00000036     64 - LOAD_CONST          CODE('outputCombatDebugMessage')
                 00000039     84 - MAKE_FUNCTION       r0000
                 0000003C     5A - STORE_NAME          'outputCombatDebugMessage'
                 0000003F     65 - LOAD_NAME           'None'
                 00000042     65 - LOAD_NAME           'None'
                 00000045     64 - LOAD_CONST          CODE('outputCombatDebugMessageAll')
                 00000048     84 - MAKE_FUNCTION       r0002
                 0000004B     5A - STORE_NAME          'outputCombatDebugMessageAll'
                 0000004E     64 - LOAD_CONST          CODE('outputCombatDebugMessageOnMatch')
                 00000051     84 - MAKE_FUNCTION       r0000
                 00000054     5A - STORE_NAME          'outputCombatDebugMessageOnMatch'
                 00000057     64 - LOAD_CONST          CODE('isAbilityMartialArt')
                 0000005A     84 - MAKE_FUNCTION       r0000
                 0000005D     5A - STORE_NAME          'isAbilityMartialArt'
                 00000060     64 - LOAD_CONST          CODE('isPreferredTactical')
                 00000063     84 - MAKE_FUNCTION       r0000
                 00000066     5A - STORE_NAME          'isPreferredTactical'
                 00000069     64 - LOAD_CONST          CODE('isPreferredFinishingTactical')
                 0000006C     84 - MAKE_FUNCTION       r0000
                 0000006F     5A - STORE_NAME          'isPreferredFinishingTactical'
                 00000072     64 - LOAD_CONST          CODE('isUsingWeapon')
                 00000075     84 - MAKE_FUNCTION       r0000
                 00000078     5A - STORE_NAME          'isUsingWeapon'
                 0000007B     64 - LOAD_CONST          CODE('isEscapeAbility')
                 0000007E     84 - MAKE_FUNCTION       r0000
                 00000081     5A - STORE_NAME          'isEscapeAbility'
                 00000084     64 - LOAD_CONST          CODE('isSpecialMove')
                 00000087     84 - MAKE_FUNCTION       r0000
                 0000008A     5A - STORE_NAME          'isSpecialMove'
                 0000008D     64 - LOAD_CONST          CODE('isPlayerWithdrawing')
                 00000090     84 - MAKE_FUNCTION       r0000
                 00000093     5A - STORE_NAME          'isPlayerWithdrawing'
                 00000096     64 - LOAD_CONST          CODE('isPlayerCombatProne')
                 00000099     84 - MAKE_FUNCTION       r0000
                 0000009C     5A - STORE_NAME          'isPlayerCombatProne'
                 0000009F     64 - LOAD_CONST          CODE('isPlayerBeingGanged')
                 000000A2     84 - MAKE_FUNCTION       r0000
                 000000A5     5A - STORE_NAME          'isPlayerBeingGanged'
                 000000A8     65 - LOAD_NAME           'False'
                 000000AB     64 - LOAD_CONST          CODE('determineBulletTime')
                 000000AE     84 - MAKE_FUNCTION       r0001
                 000000B1     5A - STORE_NAME          'determineBulletTime'
                 000000B4     64 - LOAD_CONST          CODE('finishingMoveAllowed')
                 000000B7     84 - MAKE_FUNCTION       r0000
                 000000BA     5A - STORE_NAME          'finishingMoveAllowed'
                 000000BD     64 - LOAD_CONST          CODE('killingMoveAllowed')
                 000000C0     84 - MAKE_FUNCTION       r0000
                 000000C3     5A - STORE_NAME          'killingMoveAllowed'
                 000000C6     64 - LOAD_CONST          CODE('possibleDisarmMove')
                 000000C9     84 - MAKE_FUNCTION       r0000
                 000000CC     5A - STORE_NAME          'possibleDisarmMove'
                 000000CF     64 - LOAD_CONST          CODE('shortMoveAllowed')
                 000000D2     84 - MAKE_FUNCTION       r0000
                 000000D5     5A - STORE_NAME          'shortMoveAllowed'
                 000000D8     64 - LOAD_CONST          CODE('safeAbVal')
                 000000DB     84 - MAKE_FUNCTION       r0000
                 000000DE     5A - STORE_NAME          'safeAbVal'
                 000000E1     64 - LOAD_CONST          None
                 000000E4     53 - RETURN_VALUE        
             consts:
00000103         TUPLE: (
00000108             None (4E),
00000109             CODE:
                         argcount:
0000010A                     LONG: 1L (01 00 00 00)
                         nlocals:
0000010E                     LONG: 1L (01 00 00 00)
                         stacksize:
00000112                     LONG: 2L (02 00 00 00)
                         flags:
00000116                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000011A                     STR: 't\x00\x00i\x01\x00|\x00\x00\x83\x01\x00\x01t\x00\x00i\x03\x00|\x00\x00\x83\x01\x00\x01d\x00\x00S' (1E 00 00 00 74 00 00 69 01 00 7C 00 00 83 01 00 01 74 00 00 69 03 00 7C 00 00 83 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'discovery'
                             00000003     69 - LOAD_ATTR           'outputDebugString'
                             00000006     7C - LOAD_FAST           'msg'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     01 - POP_TOP             
                             0000000D     74 - LOAD_GLOBAL         'discovery'
                             00000010     69 - LOAD_ATTR           'serverPrint'
                             00000013     7C - LOAD_FAST           'msg'
                             00000016     83 - CALL_FUNCTION       r0001
                             00000019     01 - POP_TOP             
                             0000001A     64 - LOAD_CONST          None
                             0000001D     53 - RETURN_VALUE        
                         consts:
0000013D                     TUPLE: (
00000142                         None (4E)
                             )
                         names:
00000143                     TUPLE: (
00000148                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
00000156                         STR: 'outputDebugString' (11 00 00 00 6F 75 74 70 75 74 44 65 62 75 67 53 74 72 69 6E 67),
0000016C                         STR: 'msg' (03 00 00 00 6D 73 67),
00000174                         STR: 'serverPrint' (0B 00 00 00 73 65 72 76 65 72 50 72 69 6E 74)
                             )
                         varnames:
00000184                     TUPLE: (
00000189                         STR: 'msg' (03 00 00 00 6D 73 67)
                             )
                         freevars:
00000191                     TUPLE: ()
                         cellvars:
00000196                     TUPLE: ()
                         filename:
0000019B                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_utility.py' (50 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79 2E 70 79)
                         name:
000001F0                     STR: 'outputToAll' (0B 00 00 00 6F 75 74 70 75 74 54 6F 41 6C 6C)
                         firslineno:
00000200                     LONG: 7L (07 00 00 00)
                         lnotab:
00000204                     STR: '\x00\x01\r\x01' (04 00 00 00 00 01 0D 01),
0000020D             CODE:
                         argcount:
0000020E                     LONG: 2L (02 00 00 00)
                         nlocals:
00000212                     LONG: 2L (02 00 00 00)
                         stacksize:
00000216                     LONG: 2L (02 00 00 00)
                         flags:
0000021A                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000021E                     STR: 't\x00\x00i\x01\x00t\x02\x00j\x08\x00o\x08\x00\x01d\x00\x00Sn\x01\x00\x01t\x00\x00i\x01\x00|\x01\x00j\x05\x00o\x0e\x00\x01t\x04\x00|\x00\x00\x83\x01\x00\x01n\x01\x00\x01d\x00\x00S' (3A 00 00 00 74 00 00 69 01 00 74 02 00 6A 08 00 6F 08 00 01 64 00 00 53 6E 01 00 01 74 00 00 69 01 00 7C 01 00 6A 05 00 6F 0E 00 01 74 04 00 7C 00 00 83 01 00 01 6E 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consolevar'
                             00000003     69 - LOAD_ATTR           'CombatVerbosity'
                             00000006     74 - LOAD_GLOBAL         'None'
                             00000009     6A - COMPARE_OP          "is"
                             0000000C     6F - JUMP_IF_FALSE       -> 00000017
                             0000000F     01 - POP_TOP             
                             00000010     64 - LOAD_CONST          None
                             00000013     53 - RETURN_VALUE        
                             00000014     6E - JUMP_FORWARD        -> 00000018
                             00000017     01 - POP_TOP             
                             00000018     74 - LOAD_GLOBAL         'consolevar'
                             0000001B     69 - LOAD_ATTR           'CombatVerbosity'
                             0000001E     7C - LOAD_FAST           'warning_level'
                             00000021     6A - COMPARE_OP          ">="
                             00000024     6F - JUMP_IF_FALSE       -> 00000035
                             00000027     01 - POP_TOP             
                             00000028     74 - LOAD_GLOBAL         'outputToAll'
                             0000002B     7C - LOAD_FAST           'debug_test'
                             0000002E     83 - CALL_FUNCTION       r0001
                             00000031     01 - POP_TOP             
                             00000032     6E - JUMP_FORWARD        -> 00000036
                             00000035     01 - POP_TOP             
                             00000036     64 - LOAD_CONST          None
                             00000039     53 - RETURN_VALUE        
                         consts:
0000025D                     TUPLE: (
00000262                         None (4E)
                             )
                         names:
00000263                     TUPLE: (
00000268                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
00000277                         STR: 'CombatVerbosity' (0F 00 00 00 43 6F 6D 62 61 74 56 65 72 62 6F 73 69 74 79),
0000028B                         STR: 'None' (04 00 00 00 4E 6F 6E 65),
00000294                         STR: 'warning_level' (0D 00 00 00 77 61 72 6E 69 6E 67 5F 6C 65 76 65 6C),
000002A6                         STR: 'outputToAll' (0B 00 00 00 6F 75 74 70 75 74 54 6F 41 6C 6C),
000002B6                         STR: 'debug_test' (0A 00 00 00 64 65 62 75 67 5F 74 65 73 74)
                             )
                         varnames:
000002C5                     TUPLE: (
000002CA                         STR: 'debug_test' (0A 00 00 00 64 65 62 75 67 5F 74 65 73 74),
000002D9                         STR: 'warning_level' (0D 00 00 00 77 61 72 6E 69 6E 67 5F 6C 65 76 65 6C)
                             )
                         freevars:
000002EB                     TUPLE: ()
                         cellvars:
000002F0                     TUPLE: ()
                         filename:
000002F5                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_utility.py' (50 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79 2E 70 79)
                         name:
0000034A                     STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65)
                         firslineno:
00000367                     LONG: 12L (0C 00 00 00)
                         lnotab:
0000036B                     STR: '\x00\x01\x10\x01\x08\x02\x10\x01' (08 00 00 00 00 01 10 01 08 02 10 01),
00000378             CODE:
                         argcount:
00000379                     LONG: 4L (04 00 00 00)
                         nlocals:
0000037D                     LONG: 4L (04 00 00 00)
                         stacksize:
00000381                     LONG: 4L (04 00 00 00)
                         flags:
00000385                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000389                     STR: 't\x00\x00|\x00\x00|\x01\x00\x83\x02\x00\x01t\x03\x00i\x04\x00|\x01\x00j\x05\x00o\xa4\x00\x01|\x02\x00t\x06\x00j\t\x00o\r\x00\x01|\x02\x00i\x07\x00t\x06\x00j\x08\x00o\t\x00\x01d\x01\x00GHn\x01\x00\x01|\x02\x00t\x06\x00j\t\x00o\r\x00\x01|\x02\x00i\x07\x00t\x06\x00j\t\x00o \x00\x01t\x08\x00i\t\x00|\x02\x00i\x07\x00|\x00\x00t\n\x00i\x0b\x00i\x0c\x00\x83\x03\x00\x01n\x01\x00\x01|\x03\x00t\x06\x00j\t\x00o\r\x00\x01|\x03\x00i\x07\x00t\x06\x00j\t\x00o \x00\x01t\x08\x00i\t\x00|\x03\x00i\x07\x00|\x00\x00t\n\x00i\x0b\x00i\x0c\x00\x83\x03\x00\x01q\xc1\x00\x01n\x01\x00\x01d\x00\x00S' (C5 00 00 00 74 00 00 7C 00 00 7C 01 00 83 02 00 01 74 03 00 69 04 00 7C 01 00 6A 05 00 6F A4 00 01 7C 02 00 74 06 00 6A 09 00 6F 0D 00 01 7C 02 00 69 07 00 74 06 00 6A 08 00 6F 09 00 01 64 01 00 47 48 6E 01 00 01 7C 02 00 74 06 00 6A 09 00 6F 0D 00 01 7C 02 00 69 07 00 74 06 00 6A 09 00 6F 20 00 01 74 08 00 69 09 00 7C 02 00 69 07 00 7C 00 00 74 0A 00 69 0B 00 69 0C 00 83 03 00 01 6E 01 00 01 7C 03 00 74 06 00 6A 09 00 6F 0D 00 01 7C 03 00 69 07 00 74 06 00 6A 09 00 6F 20 00 01 74 08 00 69 09 00 7C 03 00 69 07 00 7C 00 00 74 0A 00 69 0B 00 69 0C 00 83 03 00 01 71 C1 00 01 6E 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'outputCombatDebugMessage'
                             00000003     7C - LOAD_FAST           'debug_test'
                             00000006     7C - LOAD_FAST           'warning_level'
                             00000009     83 - CALL_FUNCTION       r0002
                             0000000C     01 - POP_TOP             
                             0000000D     74 - LOAD_GLOBAL         'consolevar'
                             00000010     69 - LOAD_ATTR           'SendClientCombatData'
                             00000013     7C - LOAD_FAST           'warning_level'
                             00000016     6A - COMPARE_OP          ">="
                             00000019     6F - JUMP_IF_FALSE       -> 000000C0
                             0000001C     01 - POP_TOP             
                             0000001D     7C - LOAD_FAST           'obj1'
                             00000020     74 - LOAD_GLOBAL         'None'
                             00000023     6A - COMPARE_OP          "is not"
                             00000026     6F - JUMP_IF_FALSE       -> 00000036
                             00000029     01 - POP_TOP             
                             0000002A     7C - LOAD_FAST           'obj1'
                             0000002D     69 - LOAD_ATTR           'locator'
                             00000030     74 - LOAD_GLOBAL         'None'
                             00000033     6A - COMPARE_OP          "is"
                             00000036     6F - JUMP_IF_FALSE       -> 00000042
                             00000039     01 - POP_TOP             
                             0000003A     64 - LOAD_CONST          'obj1.locator is None'
                             0000003D     47 - PRINT_ITEM          
                             0000003E     48 - PRINT_NEWLINE       
                             0000003F     6E - JUMP_FORWARD        -> 00000043
                             00000042     01 - POP_TOP             
                             00000043     7C - LOAD_FAST           'obj1'
                             00000046     74 - LOAD_GLOBAL         'None'
                             00000049     6A - COMPARE_OP          "is not"
                             0000004C     6F - JUMP_IF_FALSE       -> 0000005C
                             0000004F     01 - POP_TOP             
                             00000050     7C - LOAD_FAST           'obj1'
                             00000053     69 - LOAD_ATTR           'locator'
                             00000056     74 - LOAD_GLOBAL         'None'
                             00000059     6A - COMPARE_OP          "is not"
                             0000005C     6F - JUMP_IF_FALSE       -> 0000007F
                             0000005F     01 - POP_TOP             
                             00000060     74 - LOAD_GLOBAL         'discovery'
                             00000063     69 - LOAD_ATTR           'clientSystemMessage2'
                             00000066     7C - LOAD_FAST           'obj1'
                             00000069     69 - LOAD_ATTR           'locator'
                             0000006C     7C - LOAD_FAST           'debug_test'
                             0000006F     74 - LOAD_GLOBAL         'constants'
                             00000072     69 - LOAD_ATTR           'Chat'
                             00000075     69 - LOAD_ATTR           'CT_SYS_DEBUG'
                             00000078     83 - CALL_FUNCTION       r0003
                             0000007B     01 - POP_TOP             
                             0000007C     6E - JUMP_FORWARD        -> 00000080
                             0000007F     01 - POP_TOP             
                             00000080     7C - LOAD_FAST           'obj2'
                             00000083     74 - LOAD_GLOBAL         'None'
                             00000086     6A - COMPARE_OP          "is not"
                             00000089     6F - JUMP_IF_FALSE       -> 00000099
                             0000008C     01 - POP_TOP             
                             0000008D     7C - LOAD_FAST           'obj2'
                             00000090     69 - LOAD_ATTR           'locator'
                             00000093     74 - LOAD_GLOBAL         'None'
                             00000096     6A - COMPARE_OP          "is not"
                             00000099     6F - JUMP_IF_FALSE       -> 000000BC
                             0000009C     01 - POP_TOP             
                             0000009D     74 - LOAD_GLOBAL         'discovery'
                             000000A0     69 - LOAD_ATTR           'clientSystemMessage2'
                             000000A3     7C - LOAD_FAST           'obj2'
                             000000A6     69 - LOAD_ATTR           'locator'
                             000000A9     7C - LOAD_FAST           'debug_test'
                             000000AC     74 - LOAD_GLOBAL         'constants'
                             000000AF     69 - LOAD_ATTR           'Chat'
                             000000B2     69 - LOAD_ATTR           'CT_SYS_DEBUG'
                             000000B5     83 - CALL_FUNCTION       r0003
                             000000B8     01 - POP_TOP             
                             000000B9     71 - JUMP_ABSOLUTE       -> 000000C1
                             000000BC     01 - POP_TOP             
                             000000BD     6E - JUMP_FORWARD        -> 000000C1
                             000000C0     01 - POP_TOP             
                             000000C1     64 - LOAD_CONST          None
                             000000C4     53 - RETURN_VALUE        
                         consts:
00000453                     TUPLE: (
00000458                         None (4E),
00000459                         STR: 'obj1.locator is None' (14 00 00 00 6F 62 6A 31 2E 6C 6F 63 61 74 6F 72 20 69 73 20 4E 6F 6E 65)
                             )
                         names:
00000472                     TUPLE: (
00000477                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
00000494                         STR: 'debug_test' (0A 00 00 00 64 65 62 75 67 5F 74 65 73 74),
000004A3                         STR: 'warning_level' (0D 00 00 00 77 61 72 6E 69 6E 67 5F 6C 65 76 65 6C),
000004B5                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
000004C4                         STR: 'SendClientCombatData' (14 00 00 00 53 65 6E 64 43 6C 69 65 6E 74 43 6F 6D 62 61 74 44 61 74 61),
000004DD                         STR: 'obj1' (04 00 00 00 6F 62 6A 31),
000004E6                         STR: 'None' (04 00 00 00 4E 6F 6E 65),
000004EF                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
000004FB                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
00000509                         STR: 'clientSystemMessage2' (14 00 00 00 63 6C 69 65 6E 74 53 79 73 74 65 6D 4D 65 73 73 61 67 65 32),
00000522                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00000530                         STR: 'Chat' (04 00 00 00 43 68 61 74),
00000539                         STR: 'CT_SYS_DEBUG' (0C 00 00 00 43 54 5F 53 59 53 5F 44 45 42 55 47),
0000054A                         STR: 'obj2' (04 00 00 00 6F 62 6A 32)
                             )
                         varnames:
00000553                     TUPLE: (
00000558                         STR: 'debug_test' (0A 00 00 00 64 65 62 75 67 5F 74 65 73 74),
00000567                         STR: 'warning_level' (0D 00 00 00 77 61 72 6E 69 6E 67 5F 6C 65 76 65 6C),
00000579                         STR: 'obj1' (04 00 00 00 6F 62 6A 31),
00000582                         STR: 'obj2' (04 00 00 00 6F 62 6A 32)
                             )
                         freevars:
0000058B                     TUPLE: ()
                         cellvars:
00000590                     TUPLE: ()
                         filename:
00000595                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_utility.py' (50 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79 2E 70 79)
                         name:
000005EA                     STR: 'outputCombatDebugMessageAll' (1B 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 41 6C 6C)
                         firslineno:
0000060A                     LONG: 19L (13 00 00 00)
                         lnotab:
0000060E                     STR: '\x00\x01\r\x01\x10\x01\x1d\x01\t\x01\x1d\x01 \x01\x1d\x01' (10 00 00 00 00 01 0D 01 10 01 1D 01 09 01 1D 01 20 01 1D 01),
00000623             CODE:
                         argcount:
00000624                     LONG: 2L (02 00 00 00)
                         nlocals:
00000628                     LONG: 2L (02 00 00 00)
                         stacksize:
0000062C                     LONG: 2L (02 00 00 00)
                         flags:
00000630                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000634                     STR: 't\x00\x00i\x01\x00|\x01\x00j\x02\x00o\x0e\x00\x01t\x03\x00|\x00\x00\x83\x01\x00\x01n\x01\x00\x01d\x00\x00S' (22 00 00 00 74 00 00 69 01 00 7C 01 00 6A 02 00 6F 0E 00 01 74 03 00 7C 00 00 83 01 00 01 6E 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consolevar'
                             00000003     69 - LOAD_ATTR           'CombatVerbosity'
                             00000006     7C - LOAD_FAST           'warning_level'
                             00000009     6A - COMPARE_OP          "=="
                             0000000C     6F - JUMP_IF_FALSE       -> 0000001D
                             0000000F     01 - POP_TOP             
                             00000010     74 - LOAD_GLOBAL         'outputToAll'
                             00000013     7C - LOAD_FAST           'debug_test'
                             00000016     83 - CALL_FUNCTION       r0001
                             00000019     01 - POP_TOP             
                             0000001A     6E - JUMP_FORWARD        -> 0000001E
                             0000001D     01 - POP_TOP             
                             0000001E     64 - LOAD_CONST          None
                             00000021     53 - RETURN_VALUE        
                         consts:
0000065B                     TUPLE: (
00000660                         None (4E)
                             )
                         names:
00000661                     TUPLE: (
00000666                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
00000675                         STR: 'CombatVerbosity' (0F 00 00 00 43 6F 6D 62 61 74 56 65 72 62 6F 73 69 74 79),
00000689                         STR: 'warning_level' (0D 00 00 00 77 61 72 6E 69 6E 67 5F 6C 65 76 65 6C),
0000069B                         STR: 'outputToAll' (0B 00 00 00 6F 75 74 70 75 74 54 6F 41 6C 6C),
000006AB                         STR: 'debug_test' (0A 00 00 00 64 65 62 75 67 5F 74 65 73 74)
                             )
                         varnames:
000006BA                     TUPLE: (
000006BF                         STR: 'debug_test' (0A 00 00 00 64 65 62 75 67 5F 74 65 73 74),
000006CE                         STR: 'warning_level' (0D 00 00 00 77 61 72 6E 69 6E 67 5F 6C 65 76 65 6C)
                             )
                         freevars:
000006E0                     TUPLE: ()
                         cellvars:
000006E5                     TUPLE: ()
                         filename:
000006EA                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_utility.py' (50 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79 2E 70 79)
                         name:
0000073F                     STR: 'outputCombatDebugMessageOnMatch' (1F 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 4F 6E 4D 61 74 63 68)
                         firslineno:
00000763                     LONG: 30L (1E 00 00 00)
                         lnotab:
00000767                     STR: '\x00\x01\x10\x01' (04 00 00 00 00 01 10 01),
00000770             CODE:
                         argcount:
00000771                     LONG: 1L (01 00 00 00)
                         nlocals:
00000775                     LONG: 1L (01 00 00 00)
                         stacksize:
00000779                     LONG: 2L (02 00 00 00)
                         flags:
0000077D                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000781                     STR: '|\x00\x00t\x01\x00j\x02\x00o\x08\x00\x01t\x02\x00Sn/\x00\x01|\x00\x00t\x03\x00j\x02\x00o\x08\x00\x01t\x02\x00Sn\x1a\x00\x01|\x00\x00t\x04\x00j\x02\x00o\x08\x00\x01t\x02\x00Sn\x05\x00\x01t\x05\x00Sd\x00\x00S' (47 00 00 00 7C 00 00 74 01 00 6A 02 00 6F 08 00 01 74 02 00 53 6E 2F 00 01 7C 00 00 74 03 00 6A 02 00 6F 08 00 01 74 02 00 53 6E 1A 00 01 7C 00 00 74 04 00 6A 02 00 6F 08 00 01 74 02 00 53 6E 05 00 01 74 05 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'ability'
                             00000003     74 - LOAD_GLOBAL         'AikidoAbility'
                             00000006     6A - COMPARE_OP          "=="
                             00000009     6F - JUMP_IF_FALSE       -> 00000014
                             0000000C     01 - POP_TOP             
                             0000000D     74 - LOAD_GLOBAL         'True'
                             00000010     53 - RETURN_VALUE        
                             00000011     6E - JUMP_FORWARD        -> 00000043
                             00000014     01 - POP_TOP             
                             00000015     7C - LOAD_FAST           'ability'
                             00000018     74 - LOAD_GLOBAL         'KarateAbility'
                             0000001B     6A - COMPARE_OP          "=="
                             0000001E     6F - JUMP_IF_FALSE       -> 00000029
                             00000021     01 - POP_TOP             
                             00000022     74 - LOAD_GLOBAL         'True'
                             00000025     53 - RETURN_VALUE        
                             00000026     6E - JUMP_FORWARD        -> 00000043
                             00000029     01 - POP_TOP             
                             0000002A     7C - LOAD_FAST           'ability'
                             0000002D     74 - LOAD_GLOBAL         'KungFuAbility'
                             00000030     6A - COMPARE_OP          "=="
                             00000033     6F - JUMP_IF_FALSE       -> 0000003E
                             00000036     01 - POP_TOP             
                             00000037     74 - LOAD_GLOBAL         'True'
                             0000003A     53 - RETURN_VALUE        
                             0000003B     6E - JUMP_FORWARD        -> 00000043
                             0000003E     01 - POP_TOP             
                             0000003F     74 - LOAD_GLOBAL         'False'
                             00000042     53 - RETURN_VALUE        
                             00000043     64 - LOAD_CONST          None
                             00000046     53 - RETURN_VALUE        
                         consts:
000007CD                     TUPLE: (
000007D2                         None (4E)
                             )
                         names:
000007D3                     TUPLE: (
000007D8                         STR: 'ability' (07 00 00 00 61 62 69 6C 69 74 79),
000007E4                         STR: 'AikidoAbility' (0D 00 00 00 41 69 6B 69 64 6F 41 62 69 6C 69 74 79),
000007F6                         STR: 'True' (04 00 00 00 54 72 75 65),
000007FF                         STR: 'KarateAbility' (0D 00 00 00 4B 61 72 61 74 65 41 62 69 6C 69 74 79),
00000811                         STR: 'KungFuAbility' (0D 00 00 00 4B 75 6E 67 46 75 41 62 69 6C 69 74 79),
00000823                         STR: 'False' (05 00 00 00 46 61 6C 73 65)
                             )
                         varnames:
0000082D                     TUPLE: (
00000832                         STR: 'ability' (07 00 00 00 61 62 69 6C 69 74 79)
                             )
                         freevars:
0000083E                     TUPLE: ()
                         cellvars:
00000843                     TUPLE: ()
                         filename:
00000848                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_utility.py' (50 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79 2E 70 79)
                         name:
0000089D                     STR: 'isAbilityMartialArt' (13 00 00 00 69 73 41 62 69 6C 69 74 79 4D 61 72 74 69 61 6C 41 72 74)
                         firslineno:
000008B5                     LONG: 34L (22 00 00 00)
                         lnotab:
000008B9                     STR: '\x00\x01\r\x01\x08\x01\r\x01\x08\x01\r\x01\x08\x02' (0E 00 00 00 00 01 0D 01 08 01 0D 01 08 01 0D 01 08 02),
000008CC             CODE:
                         argcount:
000008CD                     LONG: 2L (02 00 00 00)
                         nlocals:
000008D1                     LONG: 2L (02 00 00 00)
                         stacksize:
000008D5                     LONG: 2L (02 00 00 00)
                         flags:
000008D9                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000008DD                     STR: '|\x01\x00t\x01\x00i\x02\x00i\x03\x00j\x02\x00o\x14\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x05\x00j\x02\x00Snv\x00\x01|\x01\x00t\x01\x00i\x02\x00i\x05\x00j\x02\x00o\x14\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x06\x00j\x02\x00SnO\x00\x01|\x01\x00t\x01\x00i\x02\x00i\x06\x00j\x02\x00o\x14\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x03\x00j\x02\x00Sn(\x00\x01|\x01\x00t\x01\x00i\x02\x00i\x07\x00j\x02\x00o\x14\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x07\x00j\x03\x00Sn\x01\x00\x01d\x00\x00S' (A0 00 00 00 7C 01 00 74 01 00 69 02 00 69 03 00 6A 02 00 6F 14 00 01 7C 00 00 74 01 00 69 02 00 69 05 00 6A 02 00 53 6E 76 00 01 7C 01 00 74 01 00 69 02 00 69 05 00 6A 02 00 6F 14 00 01 7C 00 00 74 01 00 69 02 00 69 06 00 6A 02 00 53 6E 4F 00 01 7C 01 00 74 01 00 69 02 00 69 06 00 6A 02 00 6F 14 00 01 7C 00 00 74 01 00 69 02 00 69 03 00 6A 02 00 53 6E 28 00 01 7C 01 00 74 01 00 69 02 00 69 07 00 6A 02 00 6F 14 00 01 7C 00 00 74 01 00 69 02 00 69 07 00 6A 03 00 53 6E 01 00 01 64 00 00 53)
                             00000000     7C - LOAD_FAST           's2'
                             00000003     74 - LOAD_GLOBAL         'constants'
                             00000006     69 - LOAD_ATTR           'combat'
                             00000009     69 - LOAD_ATTR           'SPEED'
                             0000000C     6A - COMPARE_OP          "=="
                             0000000F     6F - JUMP_IF_FALSE       -> 00000026
                             00000012     01 - POP_TOP             
                             00000013     7C - LOAD_FAST           's1'
                             00000016     74 - LOAD_GLOBAL         'constants'
                             00000019     69 - LOAD_ATTR           'combat'
                             0000001C     69 - LOAD_ATTR           'POWER'
                             0000001F     6A - COMPARE_OP          "=="
                             00000022     53 - RETURN_VALUE        
                             00000023     6E - JUMP_FORWARD        -> 0000009C
                             00000026     01 - POP_TOP             
                             00000027     7C - LOAD_FAST           's2'
                             0000002A     74 - LOAD_GLOBAL         'constants'
                             0000002D     69 - LOAD_ATTR           'combat'
                             00000030     69 - LOAD_ATTR           'POWER'
                             00000033     6A - COMPARE_OP          "=="
                             00000036     6F - JUMP_IF_FALSE       -> 0000004D
                             00000039     01 - POP_TOP             
                             0000003A     7C - LOAD_FAST           's1'
                             0000003D     74 - LOAD_GLOBAL         'constants'
                             00000040     69 - LOAD_ATTR           'combat'
                             00000043     69 - LOAD_ATTR           'DEFENSE'
                             00000046     6A - COMPARE_OP          "=="
                             00000049     53 - RETURN_VALUE        
                             0000004A     6E - JUMP_FORWARD        -> 0000009C
                             0000004D     01 - POP_TOP             
                             0000004E     7C - LOAD_FAST           's2'
                             00000051     74 - LOAD_GLOBAL         'constants'
                             00000054     69 - LOAD_ATTR           'combat'
                             00000057     69 - LOAD_ATTR           'DEFENSE'
                             0000005A     6A - COMPARE_OP          "=="
                             0000005D     6F - JUMP_IF_FALSE       -> 00000074
                             00000060     01 - POP_TOP             
                             00000061     7C - LOAD_FAST           's1'
                             00000064     74 - LOAD_GLOBAL         'constants'
                             00000067     69 - LOAD_ATTR           'combat'
                             0000006A     69 - LOAD_ATTR           'SPEED'
                             0000006D     6A - COMPARE_OP          "=="
                             00000070     53 - RETURN_VALUE        
                             00000071     6E - JUMP_FORWARD        -> 0000009C
                             00000074     01 - POP_TOP             
                             00000075     7C - LOAD_FAST           's2'
                             00000078     74 - LOAD_GLOBAL         'constants'
                             0000007B     69 - LOAD_ATTR           'combat'
                             0000007E     69 - LOAD_ATTR           'BLOCK'
                             00000081     6A - COMPARE_OP          "=="
                             00000084     6F - JUMP_IF_FALSE       -> 0000009B
                             00000087     01 - POP_TOP             
                             00000088     7C - LOAD_FAST           's1'
                             0000008B     74 - LOAD_GLOBAL         'constants'
                             0000008E     69 - LOAD_ATTR           'combat'
                             00000091     69 - LOAD_ATTR           'BLOCK'
                             00000094     6A - COMPARE_OP          "!="
                             00000097     53 - RETURN_VALUE        
                             00000098     6E - JUMP_FORWARD        -> 0000009C
                             0000009B     01 - POP_TOP             
                             0000009C     64 - LOAD_CONST          None
                             0000009F     53 - RETURN_VALUE        
                         consts:
00000982                     TUPLE: (
00000987                         None (4E)
                             )
                         names:
00000988                     TUPLE: (
0000098D                         STR: 's2' (02 00 00 00 73 32),
00000994                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
000009A2                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
000009AD                         STR: 'SPEED' (05 00 00 00 53 50 45 45 44),
000009B7                         STR: 's1' (02 00 00 00 73 31),
000009BE                         STR: 'POWER' (05 00 00 00 50 4F 57 45 52),
000009C8                         STR: 'DEFENSE' (07 00 00 00 44 45 46 45 4E 53 45),
000009D4                         STR: 'BLOCK' (05 00 00 00 42 4C 4F 43 4B)
                             )
                         varnames:
000009DE                     TUPLE: (
000009E3                         STR: 's1' (02 00 00 00 73 31),
000009EA                         STR: 's2' (02 00 00 00 73 32)
                             )
                         freevars:
000009F1                     TUPLE: ()
                         cellvars:
000009F6                     TUPLE: ()
                         filename:
000009FB                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_utility.py' (50 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79 2E 70 79)
                         name:
00000A50                     STR: 'isPreferredTactical' (13 00 00 00 69 73 50 72 65 66 65 72 72 65 64 54 61 63 74 69 63 61 6C)
                         firslineno:
00000A68                     LONG: 44L (2C 00 00 00)
                         lnotab:
00000A6C                     STR: '\x00\x02\x13\x01\x14\x01\x13\x01\x14\x01\x13\x01\x14\x01\x13\x01' (10 00 00 00 00 02 13 01 14 01 13 01 14 01 13 01 14 01 13 01),
00000A81             CODE:
                         argcount:
00000A82                     LONG: 2L (02 00 00 00)
                         nlocals:
00000A86                     LONG: 2L (02 00 00 00)
                         stacksize:
00000A8A                     LONG: 2L (02 00 00 00)
                         flags:
00000A8E                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000A92                     STR: '|\x00\x00t\x01\x00i\x02\x00i\x03\x00j\x02\x00o\x14\x00\x01|\x01\x00t\x01\x00i\x02\x00i\x05\x00j\x02\x00Sn\x01\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x06\x00j\x02\x00o\x14\x00\x01|\x01\x00t\x01\x00i\x02\x00i\x03\x00j\x02\x00Sn\x01\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x05\x00j\x02\x00o\x14\x00\x01|\x01\x00t\x01\x00i\x02\x00i\x07\x00j\x02\x00Sn\x01\x00\x01d\x00\x00S' (79 00 00 00 7C 00 00 74 01 00 69 02 00 69 03 00 6A 02 00 6F 14 00 01 7C 01 00 74 01 00 69 02 00 69 05 00 6A 02 00 53 6E 01 00 01 7C 00 00 74 01 00 69 02 00 69 06 00 6A 02 00 6F 14 00 01 7C 01 00 74 01 00 69 02 00 69 03 00 6A 02 00 53 6E 01 00 01 7C 00 00 74 01 00 69 02 00 69 05 00 6A 02 00 6F 14 00 01 7C 01 00 74 01 00 69 02 00 69 07 00 6A 02 00 53 6E 01 00 01 64 00 00 53)
                             00000000     7C - LOAD_FAST           'attacker'
                             00000003     74 - LOAD_GLOBAL         'constants'
                             00000006     69 - LOAD_ATTR           'combat'
                             00000009     69 - LOAD_ATTR           'DEFENSE'
                             0000000C     6A - COMPARE_OP          "=="
                             0000000F     6F - JUMP_IF_FALSE       -> 00000026
                             00000012     01 - POP_TOP             
                             00000013     7C - LOAD_FAST           'defender'
                             00000016     74 - LOAD_GLOBAL         'constants'
                             00000019     69 - LOAD_ATTR           'combat'
                             0000001C     69 - LOAD_ATTR           'POWER'
                             0000001F     6A - COMPARE_OP          "=="
                             00000022     53 - RETURN_VALUE        
                             00000023     6E - JUMP_FORWARD        -> 00000027
                             00000026     01 - POP_TOP             
                             00000027     7C - LOAD_FAST           'attacker'
                             0000002A     74 - LOAD_GLOBAL         'constants'
                             0000002D     69 - LOAD_ATTR           'combat'
                             00000030     69 - LOAD_ATTR           'SPEED'
                             00000033     6A - COMPARE_OP          "=="
                             00000036     6F - JUMP_IF_FALSE       -> 0000004D
                             00000039     01 - POP_TOP             
                             0000003A     7C - LOAD_FAST           'defender'
                             0000003D     74 - LOAD_GLOBAL         'constants'
                             00000040     69 - LOAD_ATTR           'combat'
                             00000043     69 - LOAD_ATTR           'DEFENSE'
                             00000046     6A - COMPARE_OP          "=="
                             00000049     53 - RETURN_VALUE        
                             0000004A     6E - JUMP_FORWARD        -> 0000004E
                             0000004D     01 - POP_TOP             
                             0000004E     7C - LOAD_FAST           'attacker'
                             00000051     74 - LOAD_GLOBAL         'constants'
                             00000054     69 - LOAD_ATTR           'combat'
                             00000057     69 - LOAD_ATTR           'POWER'
                             0000005A     6A - COMPARE_OP          "=="
                             0000005D     6F - JUMP_IF_FALSE       -> 00000074
                             00000060     01 - POP_TOP             
                             00000061     7C - LOAD_FAST           'defender'
                             00000064     74 - LOAD_GLOBAL         'constants'
                             00000067     69 - LOAD_ATTR           'combat'
                             0000006A     69 - LOAD_ATTR           'BLOCK'
                             0000006D     6A - COMPARE_OP          "=="
                             00000070     53 - RETURN_VALUE        
                             00000071     6E - JUMP_FORWARD        -> 00000075
                             00000074     01 - POP_TOP             
                             00000075     64 - LOAD_CONST          None
                             00000078     53 - RETURN_VALUE        
                         consts:
00000B10                     TUPLE: (
00000B15                         None (4E)
                             )
                         names:
00000B16                     TUPLE: (
00000B1B                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
00000B28                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00000B36                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
00000B41                         STR: 'DEFENSE' (07 00 00 00 44 45 46 45 4E 53 45),
00000B4D                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
00000B5A                         STR: 'POWER' (05 00 00 00 50 4F 57 45 52),
00000B64                         STR: 'SPEED' (05 00 00 00 53 50 45 45 44),
00000B6E                         STR: 'BLOCK' (05 00 00 00 42 4C 4F 43 4B)
                             )
                         varnames:
00000B78                     TUPLE: (
00000B7D                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
00000B8A                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72)
                             )
                         freevars:
00000B97                     TUPLE: ()
                         cellvars:
00000B9C                     TUPLE: ()
                         filename:
00000BA1                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_utility.py' (50 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79 2E 70 79)
                         name:
00000BF6                     STR: 'isPreferredFinishingTactical' (1C 00 00 00 69 73 50 72 65 66 65 72 72 65 64 46 69 6E 69 73 68 69 6E 67 54 61 63 74 69 63 61 6C)
                         firslineno:
00000C17                     LONG: 58L (3A 00 00 00)
                         lnotab:
00000C1B                     STR: '\x00\x01\x13\x01\x14\x01\x13\x01\x14\x01\x13\x01' (0C 00 00 00 00 01 13 01 14 01 13 01 14 01 13 01),
00000C2C             CODE:
                         argcount:
00000C2D                     LONG: 1L (01 00 00 00)
                         nlocals:
00000C31                     LONG: 1L (01 00 00 00)
                         stacksize:
00000C35                     LONG: 3L (03 00 00 00)
                         flags:
00000C39                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000C3D                     STR: '|\x00\x00t\x01\x00i\x02\x00i\x03\x00j\x02\x00o\x19\x00\x01t\x04\x00d\x01\x00|\x00\x00\x16d\x02\x00\x83\x02\x00\x01t\x05\x00Sn\xdd\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x06\x00j\x02\x00o\x19\x00\x01t\x04\x00d\x03\x00|\x00\x00\x16d\x02\x00\x83\x02\x00\x01t\x05\x00Sn\xb1\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x07\x00j\x02\x00o\x19\x00\x01t\x04\x00d\x04\x00|\x00\x00\x16d\x02\x00\x83\x02\x00\x01t\x05\x00Sn\x85\x00\x01|\x00\x00t\x01\x00i\x02\x00i\x08\x00j\x02\x00o\x19\x00\x01t\x04\x00d\x05\x00|\x00\x00\x16d\x02\x00\x83\x02\x00\x01t\x05\x00SnY\x00\x01|\x00\x00t\x01\x00i\x02\x00i\t\x00j\x02\x00o\x19\x00\x01t\x04\x00d\x06\x00|\x00\x00\x16d\x02\x00\x83\x02\x00\x01t\x05\x00Sn-\x00\x01|\x00\x00t\x01\x00i\x02\x00i\n\x00j\x02\x00o\x19\x00\x01t\x04\x00d\x07\x00|\x00\x00\x16d\x02\x00\x83\x02\x00\x01t\x05\x00Sn\x01\x00\x01|\x00\x00d\x08\x00j\x02\x00o\x15\x00\x01t\x04\x00d\t\x00|\x00\x00\x16d\x02\x00\x83\x02\x00\x01n\x12\x00\x01t\x04\x00d\n\x00|\x00\x00\x16d\x02\x00\x83\x02\x00\x01t\x0b\x00Sd\x00\x00S' (43 01 00 00 7C 00 00 74 01 00 69 02 00 69 03 00 6A 02 00 6F 19 00 01 74 04 00 64 01 00 7C 00 00 16 64 02 00 83 02 00 01 74 05 00 53 6E DD 00 01 7C 00 00 74 01 00 69 02 00 69 06 00 6A 02 00 6F 19 00 01 74 04 00 64 03 00 7C 00 00 16 64 02 00 83 02 00 01 74 05 00 53 6E B1 00 01 7C 00 00 74 01 00 69 02 00 69 07 00 6A 02 00 6F 19 00 01 74 04 00 64 04 00 7C 00 00 16 64 02 00 83 02 00 01 74 05 00 53 6E 85 00 01 7C 00 00 74 01 00 69 02 00 69 08 00 6A 02 00 6F 19 00 01 74 04 00 64 05 00 7C 00 00 16 64 02 00 83 02 00 01 74 05 00 53 6E 59 00 01 7C 00 00 74 01 00 69 02 00 69 09 00 6A 02 00 6F 19 00 01 74 04 00 64 06 00 7C 00 00 16 64 02 00 83 02 00 01 74 05 00 53 6E 2D 00 01 7C 00 00 74 01 00 69 02 00 69 0A 00 6A 02 00 6F 19 00 01 74 04 00 64 07 00 7C 00 00 16 64 02 00 83 02 00 01 74 05 00 53 6E 01 00 01 7C 00 00 64 08 00 6A 02 00 6F 15 00 01 74 04 00 64 09 00 7C 00 00 16 64 02 00 83 02 00 01 6E 12 00 01 74 04 00 64 0A 00 7C 00 00 16 64 02 00 83 02 00 01 74 0B 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'equippedItem'
                             00000003     74 - LOAD_GLOBAL         'constants'
                             00000006     69 - LOAD_ATTR           'combat'
                             00000009     69 - LOAD_ATTR           'RANGED_DOUBLE_PISTOL'
                             0000000C     6A - COMPARE_OP          "=="
                             0000000F     6F - JUMP_IF_FALSE       -> 0000002B
                             00000012     01 - POP_TOP             
                             00000013     74 - LOAD_GLOBAL         'outputCombatDebugMessage'
                             00000016     64 - LOAD_CONST          'weapon is dual pistol: %d '
                             00000019     7C - LOAD_FAST           'equippedItem'
                             0000001C     16 - BINARY_MODULO       
                             0000001D     64 - LOAD_CONST          20
                             00000020     83 - CALL_FUNCTION       r0002
                             00000023     01 - POP_TOP             
                             00000024     74 - LOAD_GLOBAL         'True'
                             00000027     53 - RETURN_VALUE        
                             00000028     6E - JUMP_FORWARD        -> 00000108
                             0000002B     01 - POP_TOP             
                             0000002C     7C - LOAD_FAST           'equippedItem'
                             0000002F     74 - LOAD_GLOBAL         'constants'
                             00000032     69 - LOAD_ATTR           'combat'
                             00000035     69 - LOAD_ATTR           'RANGED_SINGLE_PISTOL'
                             00000038     6A - COMPARE_OP          "=="
                             0000003B     6F - JUMP_IF_FALSE       -> 00000057
                             0000003E     01 - POP_TOP             
                             0000003F     74 - LOAD_GLOBAL         'outputCombatDebugMessage'
                             00000042     64 - LOAD_CONST          'weapon is pistol: %d '
                             00000045     7C - LOAD_FAST           'equippedItem'
                             00000048     16 - BINARY_MODULO       
                             00000049     64 - LOAD_CONST          20
                             0000004C     83 - CALL_FUNCTION       r0002
                             0000004F     01 - POP_TOP             
                             00000050     74 - LOAD_GLOBAL         'True'
                             00000053     53 - RETURN_VALUE        
                             00000054     6E - JUMP_FORWARD        -> 00000108
                             00000057     01 - POP_TOP             
                             00000058     7C - LOAD_FAST           'equippedItem'
                             0000005B     74 - LOAD_GLOBAL         'constants'
                             0000005E     69 - LOAD_ATTR           'combat'
                             00000061     69 - LOAD_ATTR           'RANGED_SHOTGUN'
                             00000064     6A - COMPARE_OP          "=="
                             00000067     6F - JUMP_IF_FALSE       -> 00000083
                             0000006A     01 - POP_TOP             
                             0000006B     74 - LOAD_GLOBAL         'outputCombatDebugMessage'
                             0000006E     64 - LOAD_CONST          'weapon is shotgun: %d '
                             00000071     7C - LOAD_FAST           'equippedItem'
                             00000074     16 - BINARY_MODULO       
                             00000075     64 - LOAD_CONST          20
                             00000078     83 - CALL_FUNCTION       r0002
                             0000007B     01 - POP_TOP             
                             0000007C     74 - LOAD_GLOBAL         'True'
                             0000007F     53 - RETURN_VALUE        
                             00000080     6E - JUMP_FORWARD        -> 00000108
                             00000083     01 - POP_TOP             
                             00000084     7C - LOAD_FAST           'equippedItem'
                             00000087     74 - LOAD_GLOBAL         'constants'
                             0000008A     69 - LOAD_ATTR           'combat'
                             0000008D     69 - LOAD_ATTR           'RANGED_MACHINE_GUN'
                             00000090     6A - COMPARE_OP          "=="
                             00000093     6F - JUMP_IF_FALSE       -> 000000AF
                             00000096     01 - POP_TOP             
                             00000097     74 - LOAD_GLOBAL         'outputCombatDebugMessage'
                             0000009A     64 - LOAD_CONST          'weapon is machine gun: %d '
                             0000009D     7C - LOAD_FAST           'equippedItem'
                             000000A0     16 - BINARY_MODULO       
                             000000A1     64 - LOAD_CONST          20
                             000000A4     83 - CALL_FUNCTION       r0002
                             000000A7     01 - POP_TOP             
                             000000A8     74 - LOAD_GLOBAL         'True'
                             000000AB     53 - RETURN_VALUE        
                             000000AC     6E - JUMP_FORWARD        -> 00000108
                             000000AF     01 - POP_TOP             
                             000000B0     7C - LOAD_FAST           'equippedItem'
                             000000B3     74 - LOAD_GLOBAL         'constants'
                             000000B6     69 - LOAD_ATTR           'combat'
                             000000B9     69 - LOAD_ATTR           'RANGED_RIFLE'
                             000000BC     6A - COMPARE_OP          "=="
                             000000BF     6F - JUMP_IF_FALSE       -> 000000DB
                             000000C2     01 - POP_TOP             
                             000000C3     74 - LOAD_GLOBAL         'outputCombatDebugMessage'
                             000000C6     64 - LOAD_CONST          'weapon is rifle: %d '
                             000000C9     7C - LOAD_FAST           'equippedItem'
                             000000CC     16 - BINARY_MODULO       
                             000000CD     64 - LOAD_CONST          20
                             000000D0     83 - CALL_FUNCTION       r0002
                             000000D3     01 - POP_TOP             
                             000000D4     74 - LOAD_GLOBAL         'True'
                             000000D7     53 - RETURN_VALUE        
                             000000D8     6E - JUMP_FORWARD        -> 00000108
                             000000DB     01 - POP_TOP             
                             000000DC     7C - LOAD_FAST           'equippedItem'
                             000000DF     74 - LOAD_GLOBAL         'constants'
                             000000E2     69 - LOAD_ATTR           'combat'
                             000000E5     69 - LOAD_ATTR           'RANGED_DBL_MACHINE_GUN'
                             000000E8     6A - COMPARE_OP          "=="
                             000000EB     6F - JUMP_IF_FALSE       -> 00000107
                             000000EE     01 - POP_TOP             
                             000000EF     74 - LOAD_GLOBAL         'outputCombatDebugMessage'
                             000000F2     64 - LOAD_CONST          'weapon is dual submahine gun: %d '
                             000000F5     7C - LOAD_FAST           'equippedItem'
                             000000F8     16 - BINARY_MODULO       
                             000000F9     64 - LOAD_CONST          20
                             000000FC     83 - CALL_FUNCTION       r0002
                             000000FF     01 - POP_TOP             
                             00000100     74 - LOAD_GLOBAL         'True'
                             00000103     53 - RETURN_VALUE        
                             00000104     6E - JUMP_FORWARD        -> 00000108
                             00000107     01 - POP_TOP             
                             00000108     7C - LOAD_FAST           'equippedItem'
                             0000010B     64 - LOAD_CONST          0
                             0000010E     6A - COMPARE_OP          "=="
                             00000111     6F - JUMP_IF_FALSE       -> 00000129
                             00000114     01 - POP_TOP             
                             00000115     74 - LOAD_GLOBAL         'outputCombatDebugMessage'
                             00000118     64 - LOAD_CONST          'weapon type invalid: %d '
                             0000011B     7C - LOAD_FAST           'equippedItem'
                             0000011E     16 - BINARY_MODULO       
                             0000011F     64 - LOAD_CONST          20
                             00000122     83 - CALL_FUNCTION       r0002
                             00000125     01 - POP_TOP             
                             00000126     6E - JUMP_FORWARD        -> 0000013B
                             00000129     01 - POP_TOP             
                             0000012A     74 - LOAD_GLOBAL         'outputCombatDebugMessage'
                             0000012D     64 - LOAD_CONST          'weapon type not found: %d '
                             00000130     7C - LOAD_FAST           'equippedItem'
                             00000133     16 - BINARY_MODULO       
                             00000134     64 - LOAD_CONST          20
                             00000137     83 - CALL_FUNCTION       r0002
                             0000013A     01 - POP_TOP             
                             0000013B     74 - LOAD_GLOBAL         'False'
                             0000013E     53 - RETURN_VALUE        
                             0000013F     64 - LOAD_CONST          None
                             00000142     53 - RETURN_VALUE        
                         consts:
00000D85                     TUPLE: (
00000D8A                         None (4E),
00000D8B                         STR: 'weapon is dual pistol: %d ' (1A 00 00 00 77 65 61 70 6F 6E 20 69 73 20 64 75 61 6C 20 70 69 73 74 6F 6C 3A 20 25 64 20),
00000DAA                         INT: 20 (14 00 00 00),
00000DAF                         STR: 'weapon is pistol: %d ' (15 00 00 00 77 65 61 70 6F 6E 20 69 73 20 70 69 73 74 6F 6C 3A 20 25 64 20),
00000DC9                         STR: 'weapon is shotgun: %d ' (16 00 00 00 77 65 61 70 6F 6E 20 69 73 20 73 68 6F 74 67 75 6E 3A 20 25 64 20),
00000DE4                         STR: 'weapon is machine gun: %d ' (1A 00 00 00 77 65 61 70 6F 6E 20 69 73 20 6D 61 63 68 69 6E 65 20 67 75 6E 3A 20 25 64 20),
00000E03                         STR: 'weapon is rifle: %d ' (14 00 00 00 77 65 61 70 6F 6E 20 69 73 20 72 69 66 6C 65 3A 20 25 64 20),
00000E1C                         STR: 'weapon is dual submahine gun: %d ' (21 00 00 00 77 65 61 70 6F 6E 20 69 73 20 64 75 61 6C 20 73 75 62 6D 61 68 69 6E 65 20 67 75 6E 3A 20 25 64 20),
00000E42                         INT: 0 (00 00 00 00),
00000E47                         STR: 'weapon type invalid: %d ' (18 00 00 00 77 65 61 70 6F 6E 20 74 79 70 65 20 69 6E 76 61 6C 69 64 3A 20 25 64 20),
00000E64                         STR: 'weapon type not found: %d ' (1A 00 00 00 77 65 61 70 6F 6E 20 74 79 70 65 20 6E 6F 74 20 66 6F 75 6E 64 3A 20 25 64 20)
                             )
                         names:
00000E83                     TUPLE: (
00000E88                         STR: 'equippedItem' (0C 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D),
00000E99                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00000EA7                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
00000EB2                         STR: 'RANGED_DOUBLE_PISTOL' (14 00 00 00 52 41 4E 47 45 44 5F 44 4F 55 42 4C 45 5F 50 49 53 54 4F 4C),
00000ECB                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
00000EE8                         STR: 'True' (04 00 00 00 54 72 75 65),
00000EF1                         STR: 'RANGED_SINGLE_PISTOL' (14 00 00 00 52 41 4E 47 45 44 5F 53 49 4E 47 4C 45 5F 50 49 53 54 4F 4C),
00000F0A                         STR: 'RANGED_SHOTGUN' (0E 00 00 00 52 41 4E 47 45 44 5F 53 48 4F 54 47 55 4E),
00000F1D                         STR: 'RANGED_MACHINE_GUN' (12 00 00 00 52 41 4E 47 45 44 5F 4D 41 43 48 49 4E 45 5F 47 55 4E),
00000F34                         STR: 'RANGED_RIFLE' (0C 00 00 00 52 41 4E 47 45 44 5F 52 49 46 4C 45),
00000F45                         STR: 'RANGED_DBL_MACHINE_GUN' (16 00 00 00 52 41 4E 47 45 44 5F 44 42 4C 5F 4D 41 43 48 49 4E 45 5F 47 55 4E),
00000F60                         STR: 'False' (05 00 00 00 46 61 6C 73 65)
                             )
                         varnames:
00000F6A                     TUPLE: (
00000F6F                         STR: 'equippedItem' (0C 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D)
                             )
                         freevars:
00000F80                     TUPLE: ()
                         cellvars:
00000F85                     TUPLE: ()
                         filename:
00000F8A                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_utility.py' (50 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79 2E 70 79)
                         name:
00000FDF                     STR: 'isUsingWeapon' (0D 00 00 00 69 73 55 73 69 6E 67 57 65 61 70 6F 6E)
                         firslineno:
00000FF1                     LONG: 67L (43 00 00 00)
                         lnotab:
00000FF5                     STR: '\x00\x01\x13\x01\x11\x01\x08\x01\x13\x01\x11\x01\x08\x01\x13\x01\x11\x01\x08\x01\x13\x01\x11\x01\x08\x01\x13\x01\x11\x01\x08\x01\x13\x01\x11\x01\x08\x02\r\x01\x15\x02\x11\x01' (2C 00 00 00 00 01 13 01 11 01 08 01 13 01 11 01 08 01 13 01 11 01 08 01 13 01 11 01 08 01 13 01 11 01 08 01 13 01 11 01 08 02 0D 01 15 02 11 01),
00001026             CODE:
                         argcount:
00001027                     LONG: 1L (01 00 00 00)
                         nlocals:
0000102B                     LONG: 1L (01 00 00 00)
                         stacksize:
0000102F                     LONG: 2L (02 00 00 00)
                         flags:
00001033                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001037                     STR: '|\x00\x00t\x01\x00j\x02\x00p\n\x00\x01|\x00\x00t\x02\x00j\x02\x00o\x08\x00\x01t\x03\x00Sn\x01\x00\x01t\x04\x00i\x05\x00|\x00\x00\x83\x01\x00d\x01\x00j\x02\x00o\x08\x00\x01t\x06\x00Sn\x01\x00\x01t\x03\x00Sd\x00\x00S' (48 00 00 00 7C 00 00 74 01 00 6A 02 00 70 0A 00 01 7C 00 00 74 02 00 6A 02 00 6F 08 00 01 74 03 00 53 6E 01 00 01 74 04 00 69 05 00 7C 00 00 83 01 00 64 01 00 6A 02 00 6F 08 00 01 74 06 00 53 6E 01 00 01 74 03 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'ability'
                             00000003     74 - LOAD_GLOBAL         'InvalidAbility'
                             00000006     6A - COMPARE_OP          "=="
                             00000009     70 - JUMP_IF_TRUE        -> 00000016
                             0000000C     01 - POP_TOP             
                             0000000D     7C - LOAD_FAST           'ability'
                             00000010     74 - LOAD_GLOBAL         'NoneAbility'
                             00000013     6A - COMPARE_OP          "=="
                             00000016     6F - JUMP_IF_FALSE       -> 00000021
                             00000019     01 - POP_TOP             
                             0000001A     74 - LOAD_GLOBAL         'False'
                             0000001D     53 - RETURN_VALUE        
                             0000001E     6E - JUMP_FORWARD        -> 00000022
                             00000021     01 - POP_TOP             
                             00000022     74 - LOAD_GLOBAL         'abilitylib'
                             00000025     69 - LOAD_ATTR           'isEscapeAbility'
                             00000028     7C - LOAD_FAST           'ability'
                             0000002B     83 - CALL_FUNCTION       r0001
                             0000002E     64 - LOAD_CONST          1
                             00000031     6A - COMPARE_OP          "=="
                             00000034     6F - JUMP_IF_FALSE       -> 0000003F
                             00000037     01 - POP_TOP             
                             00000038     74 - LOAD_GLOBAL         'True'
                             0000003B     53 - RETURN_VALUE        
                             0000003C     6E - JUMP_FORWARD        -> 00000040
                             0000003F     01 - POP_TOP             
                             00000040     74 - LOAD_GLOBAL         'False'
                             00000043     53 - RETURN_VALUE        
                             00000044     64 - LOAD_CONST          None
                             00000047     53 - RETURN_VALUE        
                         consts:
00001084                     TUPLE: (
00001089                         None (4E),
0000108A                         INT: 1 (01 00 00 00)
                             )
                         names:
0000108F                     TUPLE: (
00001094                         STR: 'ability' (07 00 00 00 61 62 69 6C 69 74 79),
000010A0                         STR: 'InvalidAbility' (0E 00 00 00 49 6E 76 61 6C 69 64 41 62 69 6C 69 74 79),
000010B3                         STR: 'NoneAbility' (0B 00 00 00 4E 6F 6E 65 41 62 69 6C 69 74 79),
000010C3                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
000010CD                         STR: 'abilitylib' (0A 00 00 00 61 62 69 6C 69 74 79 6C 69 62),
000010DC                         STR: 'isEscapeAbility' (0F 00 00 00 69 73 45 73 63 61 70 65 41 62 69 6C 69 74 79),
000010F0                         STR: 'True' (04 00 00 00 54 72 75 65)
                             )
                         varnames:
000010F9                     TUPLE: (
000010FE                         STR: 'ability' (07 00 00 00 61 62 69 6C 69 74 79)
                             )
                         freevars:
0000110A                     TUPLE: ()
                         cellvars:
0000110F                     TUPLE: ()
                         filename:
00001114                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_utility.py' (50 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79 2E 70 79)
                         name:
00001169                     STR: 'isEscapeAbility' (0F 00 00 00 69 73 45 73 63 61 70 65 41 62 69 6C 69 74 79)
                         firslineno:
0000117D                     LONG: 93L (5D 00 00 00)
                         lnotab:
00001181                     STR: '\x00\x01\x1a\x01\x08\x02\x16\x01\x08\x13' (0A 00 00 00 00 01 1A 01 08 02 16 01 08 13),
00001190             CODE:
                         argcount:
00001191                     LONG: 1L (01 00 00 00)
                         nlocals:
00001195                     LONG: 1L (01 00 00 00)
                         stacksize:
00001199                     LONG: 2L (02 00 00 00)
                         flags:
0000119D                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000011A1                     STR: '|\x00\x00t\x01\x00j\x02\x00p\n\x00\x01|\x00\x00t\x02\x00j\x02\x00o\x08\x00\x01t\x03\x00Sn\x01\x00\x01t\x04\x00|\x00\x00\x83\x01\x00t\x05\x00j\x02\x00o\x08\x00\x01t\x03\x00Sn\x01\x00\x01t\x05\x00Sd\x00\x00S' (45 00 00 00 7C 00 00 74 01 00 6A 02 00 70 0A 00 01 7C 00 00 74 02 00 6A 02 00 6F 08 00 01 74 03 00 53 6E 01 00 01 74 04 00 7C 00 00 83 01 00 74 05 00 6A 02 00 6F 08 00 01 74 03 00 53 6E 01 00 01 74 05 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'ability'
                             00000003     74 - LOAD_GLOBAL         'InvalidAbility'
                             00000006     6A - COMPARE_OP          "=="
                             00000009     70 - JUMP_IF_TRUE        -> 00000016
                             0000000C     01 - POP_TOP             
                             0000000D     7C - LOAD_FAST           'ability'
                             00000010     74 - LOAD_GLOBAL         'NoneAbility'
                             00000013     6A - COMPARE_OP          "=="
                             00000016     6F - JUMP_IF_FALSE       -> 00000021
                             00000019     01 - POP_TOP             
                             0000001A     74 - LOAD_GLOBAL         'False'
                             0000001D     53 - RETURN_VALUE        
                             0000001E     6E - JUMP_FORWARD        -> 00000022
                             00000021     01 - POP_TOP             
                             00000022     74 - LOAD_GLOBAL         'isEscapeAbility'
                             00000025     7C - LOAD_FAST           'ability'
                             00000028     83 - CALL_FUNCTION       r0001
                             0000002B     74 - LOAD_GLOBAL         'True'
                             0000002E     6A - COMPARE_OP          "=="
                             00000031     6F - JUMP_IF_FALSE       -> 0000003C
                             00000034     01 - POP_TOP             
                             00000035     74 - LOAD_GLOBAL         'False'
                             00000038     53 - RETURN_VALUE        
                             00000039     6E - JUMP_FORWARD        -> 0000003D
                             0000003C     01 - POP_TOP             
                             0000003D     74 - LOAD_GLOBAL         'True'
                             00000040     53 - RETURN_VALUE        
                             00000041     64 - LOAD_CONST          None
                             00000044     53 - RETURN_VALUE        
                         consts:
000011EB                     TUPLE: (
000011F0                         None (4E)
                             )
                         names:
000011F1                     TUPLE: (
000011F6                         STR: 'ability' (07 00 00 00 61 62 69 6C 69 74 79),
00001202                         STR: 'InvalidAbility' (0E 00 00 00 49 6E 76 61 6C 69 64 41 62 69 6C 69 74 79),
00001215                         STR: 'NoneAbility' (0B 00 00 00 4E 6F 6E 65 41 62 69 6C 69 74 79),
00001225                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
0000122F                         STR: 'isEscapeAbility' (0F 00 00 00 69 73 45 73 63 61 70 65 41 62 69 6C 69 74 79),
00001243                         STR: 'True' (04 00 00 00 54 72 75 65)
                             )
                         varnames:
0000124C                     TUPLE: (
00001251                         STR: 'ability' (07 00 00 00 61 62 69 6C 69 74 79)
                             )
                         freevars:
0000125D                     TUPLE: ()
                         cellvars:
00001262                     TUPLE: ()
                         filename:
00001267                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_utility.py' (50 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79 2E 70 79)
                         name:
000012BC                     STR: 'isSpecialMove' (0D 00 00 00 69 73 53 70 65 63 69 61 6C 4D 6F 76 65)
                         firslineno:
000012CE                     LONG: 119L (77 00 00 00)
                         lnotab:
000012D2                     STR: '\x00\x01\x1a\x01\x08\x01\x13\x01\x08\x02' (0A 00 00 00 00 01 1A 01 08 01 13 01 08 02),
000012E1             CODE:
                         argcount:
000012E2                     LONG: 1L (01 00 00 00)
                         nlocals:
000012E6                     LONG: 1L (01 00 00 00)
                         stacksize:
000012EA                     LONG: 2L (02 00 00 00)
                         flags:
000012EE                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000012F2                     STR: '|\x00\x00i\x01\x00o\x08\x00\x01t\x02\x00Sn\x01\x00\x01t\x03\x00|\x00\x00i\x04\x00\x83\x01\x00t\x02\x00j\x02\x00o\x08\x00\x01t\x02\x00Sn\x01\x00\x01t\x05\x00Sd\x00\x00S' (38 00 00 00 7C 00 00 69 01 00 6F 08 00 01 74 02 00 53 6E 01 00 01 74 03 00 7C 00 00 69 04 00 83 01 00 74 02 00 6A 02 00 6F 08 00 01 74 02 00 53 6E 01 00 01 74 05 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'player'
                             00000003     69 - LOAD_ATTR           'isAttemptingWithdraw'
                             00000006     6F - JUMP_IF_FALSE       -> 00000011
                             00000009     01 - POP_TOP             
                             0000000A     74 - LOAD_GLOBAL         'True'
                             0000000D     53 - RETURN_VALUE        
                             0000000E     6E - JUMP_FORWARD        -> 00000012
                             00000011     01 - POP_TOP             
                             00000012     74 - LOAD_GLOBAL         'isEscapeAbility'
                             00000015     7C - LOAD_FAST           'player'
                             00000018     69 - LOAD_ATTR           'requestedSpecialMove'
                             0000001B     83 - CALL_FUNCTION       r0001
                             0000001E     74 - LOAD_GLOBAL         'True'
                             00000021     6A - COMPARE_OP          "=="
                             00000024     6F - JUMP_IF_FALSE       -> 0000002F
                             00000027     01 - POP_TOP             
                             00000028     74 - LOAD_GLOBAL         'True'
                             0000002B     53 - RETURN_VALUE        
                             0000002C     6E - JUMP_FORWARD        -> 00000030
                             0000002F     01 - POP_TOP             
                             00000030     74 - LOAD_GLOBAL         'False'
                             00000033     53 - RETURN_VALUE        
                             00000034     64 - LOAD_CONST          None
                             00000037     53 - RETURN_VALUE        
                         consts:
0000132F                     TUPLE: (
00001334                         None (4E)
                             )
                         names:
00001335                     TUPLE: (
0000133A                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00001345                         STR: 'isAttemptingWithdraw' (14 00 00 00 69 73 41 74 74 65 6D 70 74 69 6E 67 57 69 74 68 64 72 61 77),
0000135E                         STR: 'True' (04 00 00 00 54 72 75 65),
00001367                         STR: 'isEscapeAbility' (0F 00 00 00 69 73 45 73 63 61 70 65 41 62 69 6C 69 74 79),
0000137B                         STR: 'requestedSpecialMove' (14 00 00 00 72 65 71 75 65 73 74 65 64 53 70 65 63 69 61 6C 4D 6F 76 65),
00001394                         STR: 'False' (05 00 00 00 46 61 6C 73 65)
                             )
                         varnames:
0000139E                     TUPLE: (
000013A3                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72)
                             )
                         freevars:
000013AE                     TUPLE: ()
                         cellvars:
000013B3                     TUPLE: ()
                         filename:
000013B8                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_utility.py' (50 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79 2E 70 79)
                         name:
0000140D                     STR: 'isPlayerWithdrawing' (13 00 00 00 69 73 50 6C 61 79 65 72 57 69 74 68 64 72 61 77 69 6E 67)
                         firslineno:
00001425                     LONG: 127L (7F 00 00 00)
                         lnotab:
00001429                     STR: '\x00\x01\n\x01\x08\x02\x16\x01\x08\x02' (0A 00 00 00 00 01 0A 01 08 02 16 01 08 02),
00001438             CODE:
                         argcount:
00001439                     LONG: 1L (01 00 00 00)
                         nlocals:
0000143D                     LONG: 1L (01 00 00 00)
                         stacksize:
00001441                     LONG: 5L (05 00 00 00)
                         flags:
00001445                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001449                     STR: '|\x00\x00i\x01\x00t\x02\x00i\x03\x00i\x04\x00@o+\x00\x01t\x05\x00d\x01\x00|\x00\x00i\x06\x00|\x00\x00i\x01\x00t\x07\x00i\x08\x00f\x03\x00\x16d\x02\x00\x83\x02\x00\x01t\t\x00Sn\x01\x00\x01t\x05\x00d\x03\x00|\x00\x00i\x06\x00|\x00\x00i\x01\x00t\x07\x00i\x08\x00f\x03\x00\x16d\x02\x00\x83\x02\x00\x01t\n\x00Sd\x00\x00S' (6A 00 00 00 7C 00 00 69 01 00 74 02 00 69 03 00 69 04 00 40 6F 2B 00 01 74 05 00 64 01 00 7C 00 00 69 06 00 7C 00 00 69 01 00 74 07 00 69 08 00 66 03 00 16 64 02 00 83 02 00 01 74 09 00 53 6E 01 00 01 74 05 00 64 03 00 7C 00 00 69 06 00 7C 00 00 69 01 00 74 07 00 69 08 00 66 03 00 16 64 02 00 83 02 00 01 74 0A 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'player'
                             00000003     69 - LOAD_ATTR           'proneState'
                             00000006     74 - LOAD_GLOBAL         'constants'
                             00000009     69 - LOAD_ATTR           'combat_prone'
                             0000000C     69 - LOAD_ATTR           'COMBAT_PRONE_MASK'
                             0000000F     40 - BINARY_AND          
                             00000010     6F - JUMP_IF_FALSE       -> 0000003E
                             00000013     01 - POP_TOP             
                             00000014     74 - LOAD_GLOBAL         'outputCombatDebugMessage'
                             00000017     64 - LOAD_CONST          'player %d combat prone 0x%x 0x%x'
                             0000001A     7C - LOAD_FAST           'player'
                             0000001D     69 - LOAD_ATTR           'slot'
                             00000020     7C - LOAD_FAST           'player'
                             00000023     69 - LOAD_ATTR           'proneState'
                             00000026     74 - LOAD_GLOBAL         'CD'
                             00000029     69 - LOAD_ATTR           'ABILITY_CONTROLLED_MASK'
                             0000002C     66 - BUILD_TUPLE         r0003
                             0000002F     16 - BINARY_MODULO       
                             00000030     64 - LOAD_CONST          5
                             00000033     83 - CALL_FUNCTION       r0002
                             00000036     01 - POP_TOP             
                             00000037     74 - LOAD_GLOBAL         'True'
                             0000003A     53 - RETURN_VALUE        
                             0000003B     6E - JUMP_FORWARD        -> 0000003F
                             0000003E     01 - POP_TOP             
                             0000003F     74 - LOAD_GLOBAL         'outputCombatDebugMessage'
                             00000042     64 - LOAD_CONST          'player %d not combat prone 0x%x 0x%x'
                             00000045     7C - LOAD_FAST           'player'
                             00000048     69 - LOAD_ATTR           'slot'
                             0000004B     7C - LOAD_FAST           'player'
                             0000004E     69 - LOAD_ATTR           'proneState'
                             00000051     74 - LOAD_GLOBAL         'CD'
                             00000054     69 - LOAD_ATTR           'ABILITY_CONTROLLED_MASK'
                             00000057     66 - BUILD_TUPLE         r0003
                             0000005A     16 - BINARY_MODULO       
                             0000005B     64 - LOAD_CONST          5
                             0000005E     83 - CALL_FUNCTION       r0002
                             00000061     01 - POP_TOP             
                             00000062     74 - LOAD_GLOBAL         'False'
                             00000065     53 - RETURN_VALUE        
                             00000066     64 - LOAD_CONST          None
                             00000069     53 - RETURN_VALUE        
                         consts:
000014B8                     TUPLE: (
000014BD                         None (4E),
000014BE                         STR: 'player %d combat prone 0x%x 0x%x' (20 00 00 00 70 6C 61 79 65 72 20 25 64 20 63 6F 6D 62 61 74 20 70 72 6F 6E 65 20 30 78 25 78 20 30 78 25 78),
000014E3                         INT: 5 (05 00 00 00),
000014E8                         STR: 'player %d not combat prone 0x%x 0x%x' (24 00 00 00 70 6C 61 79 65 72 20 25 64 20 6E 6F 74 20 63 6F 6D 62 61 74 20 70 72 6F 6E 65 20 30 78 25 78 20 30 78 25 78)
                             )
                         names:
00001511                     TUPLE: (
00001516                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00001521                         STR: 'proneState' (0A 00 00 00 70 72 6F 6E 65 53 74 61 74 65),
00001530                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
0000153E                         STR: 'combat_prone' (0C 00 00 00 63 6F 6D 62 61 74 5F 70 72 6F 6E 65),
0000154F                         STR: 'COMBAT_PRONE_MASK' (11 00 00 00 43 4F 4D 42 41 54 5F 50 52 4F 4E 45 5F 4D 41 53 4B),
00001565                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
00001582                         STR: 'slot' (04 00 00 00 73 6C 6F 74),
0000158B                         STR: 'CD' (02 00 00 00 43 44),
00001592                         STR: 'ABILITY_CONTROLLED_MASK' (17 00 00 00 41 42 49 4C 49 54 59 5F 43 4F 4E 54 52 4F 4C 4C 45 44 5F 4D 41 53 4B),
000015AE                         STR: 'True' (04 00 00 00 54 72 75 65),
000015B7                         STR: 'False' (05 00 00 00 46 61 6C 73 65)
                             )
                         varnames:
000015C1                     TUPLE: (
000015C6                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72)
                             )
                         freevars:
000015D1                     TUPLE: ()
                         cellvars:
000015D6                     TUPLE: ()
                         filename:
000015DB                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_utility.py' (50 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79 2E 70 79)
                         name:
00001630                     STR: 'isPlayerCombatProne' (13 00 00 00 69 73 50 6C 61 79 65 72 43 6F 6D 62 61 74 50 72 6F 6E 65)
                         firslineno:
00001648                     LONG: 136L (88 00 00 00)
                         lnotab:
0000164C                     STR: '\x00\x01\x14\x01#\x01\x08\x02#\x01' (0A 00 00 00 00 01 14 01 23 01 08 02 23 01),
0000165B             CODE:
                         argcount:
0000165C                     LONG: 1L (01 00 00 00)
                         nlocals:
00001660                     LONG: 1L (01 00 00 00)
                         stacksize:
00001664                     LONG: 2L (02 00 00 00)
                         flags:
00001668                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000166C                     STR: '|\x00\x00i\x01\x00t\x02\x00i\x03\x00j\x04\x00Sd\x00\x00S' (14 00 00 00 7C 00 00 69 01 00 74 02 00 69 03 00 6A 04 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'player'
                             00000003     69 - LOAD_ATTR           'opponentCount'
                             00000006     74 - LOAD_GLOBAL         'consolevar'
                             00000009     69 - LOAD_ATTR           'CombatShortMoveCount'
                             0000000C     6A - COMPARE_OP          ">"
                             0000000F     53 - RETURN_VALUE        
                             00000010     64 - LOAD_CONST          None
                             00000013     53 - RETURN_VALUE        
                         consts:
00001685                     TUPLE: (
0000168A                         None (4E)
                             )
                         names:
0000168B                     TUPLE: (
00001690                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
0000169B                         STR: 'opponentCount' (0D 00 00 00 6F 70 70 6F 6E 65 6E 74 43 6F 75 6E 74),
000016AD                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
000016BC                         STR: 'CombatShortMoveCount' (14 00 00 00 43 6F 6D 62 61 74 53 68 6F 72 74 4D 6F 76 65 43 6F 75 6E 74)
                             )
                         varnames:
000016D5                     TUPLE: (
000016DA                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72)
                             )
                         freevars:
000016E5                     TUPLE: ()
                         cellvars:
000016EA                     TUPLE: ()
                         filename:
000016EF                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_utility.py' (50 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79 2E 70 79)
                         name:
00001744                     STR: 'isPlayerBeingGanged' (13 00 00 00 69 73 50 6C 61 79 65 72 42 65 69 6E 67 47 61 6E 67 65 64)
                         firslineno:
0000175C                     LONG: 145L (91 00 00 00)
                         lnotab:
00001760                     STR: '\x00\x01' (02 00 00 00 00 01),
00001767             CODE:
                         argcount:
00001768                     LONG: 4L (04 00 00 00)
                         nlocals:
0000176C                     LONG: 5L (05 00 00 00)
                         stacksize:
00001770                     LONG: 4L (04 00 00 00)
                         flags:
00001774                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001778                     STR: 't\x00\x00i\x01\x00d\x01\x00\x83\x01\x00}\x04\x00t\x03\x00d\x02\x00|\x01\x00i\x05\x00\x16d\x03\x00\x83\x02\x00\x01|\x01\x00i\x05\x00t\x06\x00i\x07\x00i\x08\x00@o2\x00\x01t\x03\x00d\x04\x00|\x01\x00i\x05\x00\x16d\x03\x00\x83\x02\x00\x01|\x04\x00d\x05\x00j\x00\x00o\r\x00\x01d\x06\x00|\x02\x00_\n\x00qi\x00\x01n\x01\x00\x01|\x01\x00i\x05\x00t\x06\x00i\x07\x00i\x0b\x00@o2\x00\x01t\x03\x00d\x07\x00|\x01\x00i\x05\x00\x16d\x03\x00\x83\x02\x00\x01|\x04\x00d\x05\x00j\x00\x00o\r\x00\x01d\x06\x00|\x02\x00_\n\x00q\xaf\x00\x01n\x01\x00\x01|\x01\x00i\x05\x00t\x06\x00i\x07\x00i\x0c\x00@o2\x00\x01t\x03\x00d\x08\x00|\x01\x00i\x05\x00\x16d\x03\x00\x83\x02\x00\x01|\x04\x00d\x05\x00j\x00\x00o\r\x00\x01d\x06\x00|\x02\x00_\n\x00q\xf5\x00\x01n\x01\x00\x01|\x01\x00i\x05\x00t\x06\x00i\x07\x00i\r\x00@o\x11\x00\x01|\x00\x00i\x05\x00t\x06\x00i\x07\x00i\r\x00@o2\x00\x01t\x03\x00d\t\x00|\x01\x00i\x05\x00\x16d\x03\x00\x83\x02\x00\x01|\x04\x00d\n\x00j\x00\x00o\r\x00\x01d\x06\x00|\x02\x00_\n\x00qO\x01\x01n\x01\x00\x01|\x04\x00d\x0b\x00j\x00\x00o!\x00\x01t\x03\x00d\x0c\x00|\x01\x00i\x05\x00\x16d\x03\x00\x83\x02\x00\x01d\x06\x00|\x02\x00_\n\x00n\x01\x00\x01t\x03\x00d\r\x00|\x02\x00i\n\x00|\x04\x00f\x02\x00\x16d\x03\x00\x83\x02\x00\x01d\x00\x00S' (9B 01 00 00 74 00 00 69 01 00 64 01 00 83 01 00 7D 04 00 74 03 00 64 02 00 7C 01 00 69 05 00 16 64 03 00 83 02 00 01 7C 01 00 69 05 00 74 06 00 69 07 00 69 08 00 40 6F 32 00 01 74 03 00 64 04 00 7C 01 00 69 05 00 16 64 03 00 83 02 00 01 7C 04 00 64 05 00 6A 00 00 6F 0D 00 01 64 06 00 7C 02 00 5F 0A 00 71 69 00 01 6E 01 00 01 7C 01 00 69 05 00 74 06 00 69 07 00 69 0B 00 40 6F 32 00 01 74 03 00 64 07 00 7C 01 00 69 05 00 16 64 03 00 83 02 00 01 7C 04 00 64 05 00 6A 00 00 6F 0D 00 01 64 06 00 7C 02 00 5F 0A 00 71 AF 00 01 6E 01 00 01 7C 01 00 69 05 00 74 06 00 69 07 00 69 0C 00 40 6F 32 00 01 74 03 00 64 08 00 7C 01 00 69 05 00 16 64 03 00 83 02 00 01 7C 04 00 64 05 00 6A 00 00 6F 0D 00 01 64 06 00 7C 02 00 5F 0A 00 71 F5 00 01 6E 01 00 01 7C 01 00 69 05 00 74 06 00 69 07 00 69 0D 00 40 6F 11 00 01 7C 00 00 69 05 00 74 06 00 69 07 00 69 0D 00 40 6F 32 00 01 74 03 00 64 09 00 7C 01 00 69 05 00 16 64 03 00 83 02 00 01 7C 04 00 64 0A 00 6A 00 00 6F 0D 00 01 64 06 00 7C 02 00 5F 0A 00 71 4F 01 01 6E 01 00 01 7C 04 00 64 0B 00 6A 00 00 6F 21 00 01 74 03 00 64 0C 00 7C 01 00 69 05 00 16 64 03 00 83 02 00 01 64 06 00 7C 02 00 5F 0A 00 6E 01 00 01 74 03 00 64 0D 00 7C 02 00 69 0A 00 7C 04 00 66 02 00 16 64 03 00 83 02 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'random'
                             00000003     69 - LOAD_ATTR           'randrange'
                             00000006     64 - LOAD_CONST          100
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     7D - STORE_FAST          'roll'
                             0000000F     74 - LOAD_GLOBAL         'outputCombatDebugMessage'
                             00000012     64 - LOAD_CONST          'bullet time determine: %d'
                             00000015     7C - LOAD_FAST           'defender'
                             00000018     69 - LOAD_ATTR           'combatantType'
                             0000001B     16 - BINARY_MODULO       
                             0000001C     64 - LOAD_CONST          7
                             0000001F     83 - CALL_FUNCTION       r0002
                             00000022     01 - POP_TOP             
                             00000023     7C - LOAD_FAST           'defender'
                             00000026     69 - LOAD_ATTR           'combatantType'
                             00000029     74 - LOAD_GLOBAL         'constants'
                             0000002C     69 - LOAD_ATTR           'combat'
                             0000002F     69 - LOAD_ATTR           'BOSS'
                             00000032     40 - BINARY_AND          
                             00000033     6F - JUMP_IF_FALSE       -> 00000068
                             00000036     01 - POP_TOP             
                             00000037     74 - LOAD_GLOBAL         'outputCombatDebugMessage'
                             0000003A     64 - LOAD_CONST          'BOSS: %d'
                             0000003D     7C - LOAD_FAST           'defender'
                             00000040     69 - LOAD_ATTR           'combatantType'
                             00000043     16 - BINARY_MODULO       
                             00000044     64 - LOAD_CONST          7
                             00000047     83 - CALL_FUNCTION       r0002
                             0000004A     01 - POP_TOP             
                             0000004B     7C - LOAD_FAST           'roll'
                             0000004E     64 - LOAD_CONST          60
                             00000051     6A - COMPARE_OP          "<"
                             00000054     6F - JUMP_IF_FALSE       -> 00000064
                             00000057     01 - POP_TOP             
                             00000058     64 - LOAD_CONST          1
                             0000005B     7C - LOAD_FAST           'result'
                             0000005E     5F - STORE_ATTR          'bullet_time'
                             00000061     71 - JUMP_ABSOLUTE       -> 00000069
                             00000064     01 - POP_TOP             
                             00000065     6E - JUMP_FORWARD        -> 00000069
                             00000068     01 - POP_TOP             
                             00000069     7C - LOAD_FAST           'defender'
                             0000006C     69 - LOAD_ATTR           'combatantType'
                             0000006F     74 - LOAD_GLOBAL         'constants'
                             00000072     69 - LOAD_ATTR           'combat'
                             00000075     69 - LOAD_ATTR           'PVPCAPTAIN'
                             00000078     40 - BINARY_AND          
                             00000079     6F - JUMP_IF_FALSE       -> 000000AE
                             0000007C     01 - POP_TOP             
                             0000007D     74 - LOAD_GLOBAL         'outputCombatDebugMessage'
                             00000080     64 - LOAD_CONST          'PVPCAPTAIN: %d'
                             00000083     7C - LOAD_FAST           'defender'
                             00000086     69 - LOAD_ATTR           'combatantType'
                             00000089     16 - BINARY_MODULO       
                             0000008A     64 - LOAD_CONST          7
                             0000008D     83 - CALL_FUNCTION       r0002
                             00000090     01 - POP_TOP             
                             00000091     7C - LOAD_FAST           'roll'
                             00000094     64 - LOAD_CONST          60
                             00000097     6A - COMPARE_OP          "<"
                             0000009A     6F - JUMP_IF_FALSE       -> 000000AA
                             0000009D     01 - POP_TOP             
                             0000009E     64 - LOAD_CONST          1
                             000000A1     7C - LOAD_FAST           'result'
                             000000A4     5F - STORE_ATTR          'bullet_time'
                             000000A7     71 - JUMP_ABSOLUTE       -> 000000AF
                             000000AA     01 - POP_TOP             
                             000000AB     6E - JUMP_FORWARD        -> 000000AF
                             000000AE     01 - POP_TOP             
                             000000AF     7C - LOAD_FAST           'defender'
                             000000B2     69 - LOAD_ATTR           'combatantType'
                             000000B5     74 - LOAD_GLOBAL         'constants'
                             000000B8     69 - LOAD_ATTR           'combat'
                             000000BB     69 - LOAD_ATTR           'MISSIONTARGET'
                             000000BE     40 - BINARY_AND          
                             000000BF     6F - JUMP_IF_FALSE       -> 000000F4
                             000000C2     01 - POP_TOP             
                             000000C3     74 - LOAD_GLOBAL         'outputCombatDebugMessage'
                             000000C6     64 - LOAD_CONST          'MISSIONTARGET: %d'
                             000000C9     7C - LOAD_FAST           'defender'
                             000000CC     69 - LOAD_ATTR           'combatantType'
                             000000CF     16 - BINARY_MODULO       
                             000000D0     64 - LOAD_CONST          7
                             000000D3     83 - CALL_FUNCTION       r0002
                             000000D6     01 - POP_TOP             
                             000000D7     7C - LOAD_FAST           'roll'
                             000000DA     64 - LOAD_CONST          60
                             000000DD     6A - COMPARE_OP          "<"
                             000000E0     6F - JUMP_IF_FALSE       -> 000000F0
                             000000E3     01 - POP_TOP             
                             000000E4     64 - LOAD_CONST          1
                             000000E7     7C - LOAD_FAST           'result'
                             000000EA     5F - STORE_ATTR          'bullet_time'
                             000000ED     71 - JUMP_ABSOLUTE       -> 000000F5
                             000000F0     01 - POP_TOP             
                             000000F1     6E - JUMP_FORWARD        -> 000000F5
                             000000F4     01 - POP_TOP             
                             000000F5     7C - LOAD_FAST           'defender'
                             000000F8     69 - LOAD_ATTR           'combatantType'
                             000000FB     74 - LOAD_GLOBAL         'constants'
                             000000FE     69 - LOAD_ATTR           'combat'
                             00000101     69 - LOAD_ATTR           'PLAYER'
                             00000104     40 - BINARY_AND          
                             00000105     6F - JUMP_IF_FALSE       -> 00000119
                             00000108     01 - POP_TOP             
                             00000109     7C - LOAD_FAST           'attacker'
                             0000010C     69 - LOAD_ATTR           'combatantType'
                             0000010F     74 - LOAD_GLOBAL         'constants'
                             00000112     69 - LOAD_ATTR           'combat'
                             00000115     69 - LOAD_ATTR           'PLAYER'
                             00000118     40 - BINARY_AND          
                             00000119     6F - JUMP_IF_FALSE       -> 0000014E
                             0000011C     01 - POP_TOP             
                             0000011D     74 - LOAD_GLOBAL         'outputCombatDebugMessage'
                             00000120     64 - LOAD_CONST          'PLAYERs: %d'
                             00000123     7C - LOAD_FAST           'defender'
                             00000126     69 - LOAD_ATTR           'combatantType'
                             00000129     16 - BINARY_MODULO       
                             0000012A     64 - LOAD_CONST          7
                             0000012D     83 - CALL_FUNCTION       r0002
                             00000130     01 - POP_TOP             
                             00000131     7C - LOAD_FAST           'roll'
                             00000134     64 - LOAD_CONST          75
                             00000137     6A - COMPARE_OP          "<"
                             0000013A     6F - JUMP_IF_FALSE       -> 0000014A
                             0000013D     01 - POP_TOP             
                             0000013E     64 - LOAD_CONST          1
                             00000141     7C - LOAD_FAST           'result'
                             00000144     5F - STORE_ATTR          'bullet_time'
                             00000147     71 - JUMP_ABSOLUTE       -> 0000014F
                             0000014A     01 - POP_TOP             
                             0000014B     6E - JUMP_FORWARD        -> 0000014F
                             0000014E     01 - POP_TOP             
                             0000014F     7C - LOAD_FAST           'roll'
                             00000152     64 - LOAD_CONST          10
                             00000155     6A - COMPARE_OP          "<"
                             00000158     6F - JUMP_IF_FALSE       -> 0000017C
                             0000015B     01 - POP_TOP             
                             0000015C     74 - LOAD_GLOBAL         'outputCombatDebugMessage'
                             0000015F     64 - LOAD_CONST          'normal: %d'
                             00000162     7C - LOAD_FAST           'defender'
                             00000165     69 - LOAD_ATTR           'combatantType'
                             00000168     16 - BINARY_MODULO       
                             00000169     64 - LOAD_CONST          7
                             0000016C     83 - CALL_FUNCTION       r0002
                             0000016F     01 - POP_TOP             
                             00000170     64 - LOAD_CONST          1
                             00000173     7C - LOAD_FAST           'result'
                             00000176     5F - STORE_ATTR          'bullet_time'
                             00000179     6E - JUMP_FORWARD        -> 0000017D
                             0000017C     01 - POP_TOP             
                             0000017D     74 - LOAD_GLOBAL         'outputCombatDebugMessage'
                             00000180     64 - LOAD_CONST          'bullet time enabled(%d): %d'
                             00000183     7C - LOAD_FAST           'result'
                             00000186     69 - LOAD_ATTR           'bullet_time'
                             00000189     7C - LOAD_FAST           'roll'
                             0000018C     66 - BUILD_TUPLE         r0002
                             0000018F     16 - BINARY_MODULO       
                             00000190     64 - LOAD_CONST          7
                             00000193     83 - CALL_FUNCTION       r0002
                             00000196     01 - POP_TOP             
                             00000197     64 - LOAD_CONST          None
                             0000019A     53 - RETURN_VALUE        
                         consts:
00001918                     TUPLE: (
0000191D                         None (4E),
0000191E                         INT: 100 (64 00 00 00),
00001923                         STR: 'bullet time determine: %d' (19 00 00 00 62 75 6C 6C 65 74 20 74 69 6D 65 20 64 65 74 65 72 6D 69 6E 65 3A 20 25 64),
00001941                         INT: 7 (07 00 00 00),
00001946                         STR: 'BOSS: %d' (08 00 00 00 42 4F 53 53 3A 20 25 64),
00001953                         INT: 60 (3C 00 00 00),
00001958                         INT: 1 (01 00 00 00),
0000195D                         STR: 'PVPCAPTAIN: %d' (0E 00 00 00 50 56 50 43 41 50 54 41 49 4E 3A 20 25 64),
00001970                         STR: 'MISSIONTARGET: %d' (11 00 00 00 4D 49 53 53 49 4F 4E 54 41 52 47 45 54 3A 20 25 64),
00001986                         STR: 'PLAYERs: %d' (0B 00 00 00 50 4C 41 59 45 52 73 3A 20 25 64),
00001996                         INT: 75 (4B 00 00 00),
0000199B                         INT: 10 (0A 00 00 00),
000019A0                         STR: 'normal: %d' (0A 00 00 00 6E 6F 72 6D 61 6C 3A 20 25 64),
000019AF                         STR: 'bullet time enabled(%d): %d' (1B 00 00 00 62 75 6C 6C 65 74 20 74 69 6D 65 20 65 6E 61 62 6C 65 64 28 25 64 29 3A 20 25 64)
                             )
                         names:
000019CF                     TUPLE: (
000019D4                         STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
000019DF                         STR: 'randrange' (09 00 00 00 72 61 6E 64 72 61 6E 67 65),
000019ED                         STR: 'roll' (04 00 00 00 72 6F 6C 6C),
000019F6                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
00001A13                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
00001A20                         STR: 'combatantType' (0D 00 00 00 63 6F 6D 62 61 74 61 6E 74 54 79 70 65),
00001A32                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00001A40                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
00001A4B                         STR: 'BOSS' (04 00 00 00 42 4F 53 53),
00001A54                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00001A5F                         STR: 'bullet_time' (0B 00 00 00 62 75 6C 6C 65 74 5F 74 69 6D 65),
00001A6F                         STR: 'PVPCAPTAIN' (0A 00 00 00 50 56 50 43 41 50 54 41 49 4E),
00001A7E                         STR: 'MISSIONTARGET' (0D 00 00 00 4D 49 53 53 49 4F 4E 54 41 52 47 45 54),
00001A90                         STR: 'PLAYER' (06 00 00 00 50 4C 41 59 45 52),
00001A9B                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72)
                             )
                         varnames:
00001AA8                     TUPLE: (
00001AAD                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
00001ABA                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
00001AC7                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00001AD2                         STR: 'special_move' (0C 00 00 00 73 70 65 63 69 61 6C 5F 6D 6F 76 65),
00001AE3                         STR: 'roll' (04 00 00 00 72 6F 6C 6C)
                             )
                         freevars:
00001AEC                     TUPLE: ()
                         cellvars:
00001AF1                     TUPLE: ()
                         filename:
00001AF6                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_utility.py' (50 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79 2E 70 79)
                         name:
00001B4B                     STR: 'determineBulletTime' (13 00 00 00 64 65 74 65 72 6D 69 6E 65 42 75 6C 6C 65 74 54 69 6D 65)
                         firslineno:
00001B63                     LONG: 149L (95 00 00 00)
                         lnotab:
00001B67                     STR: '\x00\x02\x0f\x01\x14\x01\x14\x01\x14\x01\r\x01\x11\x02\x14\x01\x14\x01\r\x01\x11\x02\x14\x01\x14\x01\r\x01\x11\x02(\x01\x14\x01\r\x01\x11\x02\r\x01\x14\x01\r\x03' (2C 00 00 00 00 02 0F 01 14 01 14 01 14 01 0D 01 11 02 14 01 14 01 0D 01 11 02 14 01 14 01 0D 01 11 02 28 01 14 01 0D 01 11 02 0D 01 14 01 0D 03),
00001B98             CODE:
                         argcount:
00001B99                     LONG: 4L (04 00 00 00)
                         nlocals:
00001B9D                     LONG: 7L (07 00 00 00)
                         stacksize:
00001BA1                     LONG: 4L (04 00 00 00)
                         flags:
00001BA5                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001BA9                     STR: '|\x00\x00}\x06\x00|\x01\x00}\x04\x00|\x02\x00i\x05\x00}\x05\x00|\x03\x00o\x19\x00\x01|\x01\x00}\x06\x00|\x00\x00}\x04\x00|\x02\x00i\x08\x00}\x05\x00n\x01\x00\x01|\x02\x00i\t\x00t\n\x00i\x0b\x00i\x0c\x00j\x03\x00o\x08\x00\x01t\r\x00Sn\x01\x00\x01t\x0e\x00|\x04\x00\x83\x01\x00o\x08\x00\x01t\r\x00Sn\x01\x00\x01|\x05\x00|\x04\x00i\x0f\x00j\x00\x00o\x08\x00\x01t\r\x00Sn\x01\x00\x01t\x10\x00|\x06\x00|\x04\x00|\x02\x00\x83\x03\x00\x01t\x11\x00Sd\x00\x00S' (98 00 00 00 7C 00 00 7D 06 00 7C 01 00 7D 04 00 7C 02 00 69 05 00 7D 05 00 7C 03 00 6F 19 00 01 7C 01 00 7D 06 00 7C 00 00 7D 04 00 7C 02 00 69 08 00 7D 05 00 6E 01 00 01 7C 02 00 69 09 00 74 0A 00 69 0B 00 69 0C 00 6A 03 00 6F 08 00 01 74 0D 00 53 6E 01 00 01 74 0E 00 7C 04 00 83 01 00 6F 08 00 01 74 0D 00 53 6E 01 00 01 7C 05 00 7C 04 00 69 0F 00 6A 00 00 6F 08 00 01 74 0D 00 53 6E 01 00 01 74 10 00 7C 06 00 7C 04 00 7C 02 00 83 03 00 01 74 11 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'attacker'
                             00000003     7D - STORE_FAST          'dmger'
                             00000006     7C - LOAD_FAST           'defender'
                             00000009     7D - STORE_FAST          'vic'
                             0000000C     7C - LOAD_FAST           'result'
                             0000000F     69 - LOAD_ATTR           'loserDamage'
                             00000012     7D - STORE_FAST          'dmgDone'
                             00000015     7C - LOAD_FAST           'checkDefender'
                             00000018     6F - JUMP_IF_FALSE       -> 00000034
                             0000001B     01 - POP_TOP             
                             0000001C     7C - LOAD_FAST           'defender'
                             0000001F     7D - STORE_FAST          'dmger'
                             00000022     7C - LOAD_FAST           'attacker'
                             00000025     7D - STORE_FAST          'vic'
                             00000028     7C - LOAD_FAST           'result'
                             0000002B     69 - LOAD_ATTR           'winnerDamage'
                             0000002E     7D - STORE_FAST          'dmgDone'
                             00000031     6E - JUMP_FORWARD        -> 00000035
                             00000034     01 - POP_TOP             
                             00000035     7C - LOAD_FAST           'result'
                             00000038     69 - LOAD_ATTR           'distance'
                             0000003B     74 - LOAD_GLOBAL         'constants'
                             0000003E     69 - LOAD_ATTR           'combat'
                             00000041     69 - LOAD_ATTR           'SHORT_RANGE'
                             00000044     6A - COMPARE_OP          "!="
                             00000047     6F - JUMP_IF_FALSE       -> 00000052
                             0000004A     01 - POP_TOP             
                             0000004B     74 - LOAD_GLOBAL         'False'
                             0000004E     53 - RETURN_VALUE        
                             0000004F     6E - JUMP_FORWARD        -> 00000053
                             00000052     01 - POP_TOP             
                             00000053     74 - LOAD_GLOBAL         'isPlayerCombatProne'
                             00000056     7C - LOAD_FAST           'vic'
                             00000059     83 - CALL_FUNCTION       r0001
                             0000005C     6F - JUMP_IF_FALSE       -> 00000067
                             0000005F     01 - POP_TOP             
                             00000060     74 - LOAD_GLOBAL         'False'
                             00000063     53 - RETURN_VALUE        
                             00000064     6E - JUMP_FORWARD        -> 00000068
                             00000067     01 - POP_TOP             
                             00000068     7C - LOAD_FAST           'dmgDone'
                             0000006B     7C - LOAD_FAST           'vic'
                             0000006E     69 - LOAD_ATTR           'health'
                             00000071     6A - COMPARE_OP          "<"
                             00000074     6F - JUMP_IF_FALSE       -> 0000007F
                             00000077     01 - POP_TOP             
                             00000078     74 - LOAD_GLOBAL         'False'
                             0000007B     53 - RETURN_VALUE        
                             0000007C     6E - JUMP_FORWARD        -> 00000080
                             0000007F     01 - POP_TOP             
                             00000080     74 - LOAD_GLOBAL         'determineBulletTime'
                             00000083     7C - LOAD_FAST           'dmger'
                             00000086     7C - LOAD_FAST           'vic'
                             00000089     7C - LOAD_FAST           'result'
                             0000008C     83 - CALL_FUNCTION       r0003
                             0000008F     01 - POP_TOP             
                             00000090     74 - LOAD_GLOBAL         'True'
                             00000093     53 - RETURN_VALUE        
                             00000094     64 - LOAD_CONST          None
                             00000097     53 - RETURN_VALUE        
                         consts:
00001C46                     TUPLE: (
00001C4B                         None (4E)
                             )
                         names:
00001C4C                     TUPLE: (
00001C51                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
00001C5E                         STR: 'dmger' (05 00 00 00 64 6D 67 65 72),
00001C68                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
00001C75                         STR: 'vic' (03 00 00 00 76 69 63),
00001C7D                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00001C88                         STR: 'loserDamage' (0B 00 00 00 6C 6F 73 65 72 44 61 6D 61 67 65),
00001C98                         STR: 'dmgDone' (07 00 00 00 64 6D 67 44 6F 6E 65),
00001CA4                         STR: 'checkDefender' (0D 00 00 00 63 68 65 63 6B 44 65 66 65 6E 64 65 72),
00001CB6                         STR: 'winnerDamage' (0C 00 00 00 77 69 6E 6E 65 72 44 61 6D 61 67 65),
00001CC7                         STR: 'distance' (08 00 00 00 64 69 73 74 61 6E 63 65),
00001CD4                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00001CE2                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
00001CED                         STR: 'SHORT_RANGE' (0B 00 00 00 53 48 4F 52 54 5F 52 41 4E 47 45),
00001CFD                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
00001D07                         STR: 'isPlayerCombatProne' (13 00 00 00 69 73 50 6C 61 79 65 72 43 6F 6D 62 61 74 50 72 6F 6E 65),
00001D1F                         STR: 'health' (06 00 00 00 68 65 61 6C 74 68),
00001D2A                         STR: 'determineBulletTime' (13 00 00 00 64 65 74 65 72 6D 69 6E 65 42 75 6C 6C 65 74 54 69 6D 65),
00001D42                         STR: 'True' (04 00 00 00 54 72 75 65)
                             )
                         varnames:
00001D4B                     TUPLE: (
00001D50                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
00001D5D                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
00001D6A                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00001D75                         STR: 'checkDefender' (0D 00 00 00 63 68 65 63 6B 44 65 66 65 6E 64 65 72),
00001D87                         STR: 'vic' (03 00 00 00 76 69 63),
00001D8F                         STR: 'dmgDone' (07 00 00 00 64 6D 67 44 6F 6E 65),
00001D9B                         STR: 'dmger' (05 00 00 00 64 6D 67 65 72)
                             )
                         freevars:
00001DA5                     TUPLE: ()
                         cellvars:
00001DAA                     TUPLE: ()
                         filename:
00001DAF                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_utility.py' (50 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79 2E 70 79)
                         name:
00001E04                     STR: 'finishingMoveAllowed' (14 00 00 00 66 69 6E 69 73 68 69 6E 67 4D 6F 76 65 41 6C 6C 6F 77 65 64)
                         firslineno:
00001E1D                     LONG: 181L (B5 00 00 00)
                         lnotab:
00001E21                     STR: '\x00\x03\x06\x01\x06\x01\t\x02\x07\x01\x06\x01\x06\x01\r\x02\x16\x01\x08\x03\r\x01\x08\x02\x10\x01\x08\x02\x10\x01' (1E 00 00 00 00 03 06 01 06 01 09 02 07 01 06 01 06 01 0D 02 16 01 08 03 0D 01 08 02 10 01 08 02 10 01),
00001E44             CODE:
                         argcount:
00001E45                     LONG: 3L (03 00 00 00)
                         nlocals:
00001E49                     LONG: 3L (03 00 00 00)
                         stacksize:
00001E4D                     LONG: 4L (04 00 00 00)
                         flags:
00001E51                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001E55                     STR: '|\x02\x00i\x01\x00|\x01\x00i\x03\x00j\x05\x00o\x18\x00\x01t\x04\x00|\x00\x00|\x01\x00|\x02\x00\x83\x03\x00\x01t\x06\x00Sn\x01\x00\x01t\x07\x00Sd\x00\x00S' (33 00 00 00 7C 02 00 69 01 00 7C 01 00 69 03 00 6A 05 00 6F 18 00 01 74 04 00 7C 00 00 7C 01 00 7C 02 00 83 03 00 01 74 06 00 53 6E 01 00 01 74 07 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'result'
                             00000003     69 - LOAD_ATTR           'loserDamage'
                             00000006     7C - LOAD_FAST           'loser'
                             00000009     69 - LOAD_ATTR           'health'
                             0000000C     6A - COMPARE_OP          ">="
                             0000000F     6F - JUMP_IF_FALSE       -> 0000002A
                             00000012     01 - POP_TOP             
                             00000013     74 - LOAD_GLOBAL         'determineBulletTime'
                             00000016     7C - LOAD_FAST           'winner'
                             00000019     7C - LOAD_FAST           'loser'
                             0000001C     7C - LOAD_FAST           'result'
                             0000001F     83 - CALL_FUNCTION       r0003
                             00000022     01 - POP_TOP             
                             00000023     74 - LOAD_GLOBAL         'True'
                             00000026     53 - RETURN_VALUE        
                             00000027     6E - JUMP_FORWARD        -> 0000002B
                             0000002A     01 - POP_TOP             
                             0000002B     74 - LOAD_GLOBAL         'False'
                             0000002E     53 - RETURN_VALUE        
                             0000002F     64 - LOAD_CONST          None
                             00000032     53 - RETURN_VALUE        
                         consts:
00001E8D                     TUPLE: (
00001E92                         None (4E)
                             )
                         names:
00001E93                     TUPLE: (
00001E98                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00001EA3                         STR: 'loserDamage' (0B 00 00 00 6C 6F 73 65 72 44 61 6D 61 67 65),
00001EB3                         STR: 'loser' (05 00 00 00 6C 6F 73 65 72),
00001EBD                         STR: 'health' (06 00 00 00 68 65 61 6C 74 68),
00001EC8                         STR: 'determineBulletTime' (13 00 00 00 64 65 74 65 72 6D 69 6E 65 42 75 6C 6C 65 74 54 69 6D 65),
00001EE0                         STR: 'winner' (06 00 00 00 77 69 6E 6E 65 72),
00001EEB                         STR: 'True' (04 00 00 00 54 72 75 65),
00001EF4                         STR: 'False' (05 00 00 00 46 61 6C 73 65)
                             )
                         varnames:
00001EFE                     TUPLE: (
00001F03                         STR: 'winner' (06 00 00 00 77 69 6E 6E 65 72),
00001F0E                         STR: 'loser' (05 00 00 00 6C 6F 73 65 72),
00001F18                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74)
                             )
                         freevars:
00001F23                     TUPLE: ()
                         cellvars:
00001F28                     TUPLE: ()
                         filename:
00001F2D                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_utility.py' (50 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79 2E 70 79)
                         name:
00001F82                     STR: 'killingMoveAllowed' (12 00 00 00 6B 69 6C 6C 69 6E 67 4D 6F 76 65 41 6C 6C 6F 77 65 64)
                         firslineno:
00001F99                     LONG: 207L (CF 00 00 00)
                         lnotab:
00001F9D                     STR: '\x00\x02\x13\x01\x10\x01\x08\x02' (08 00 00 00 00 02 13 01 10 01 08 02),
00001FAA             CODE:
                         argcount:
00001FAB                     LONG: 3L (03 00 00 00)
                         nlocals:
00001FAF                     LONG: 3L (03 00 00 00)
                         stacksize:
00001FB3                     LONG: 2L (02 00 00 00)
                         flags:
00001FB7                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001FBB                     STR: '|\x02\x00i\x01\x00t\x02\x00i\x03\x00i\x04\x00j\x03\x00o\x08\x00\x01t\x05\x00Sn\x01\x00\x01t\x06\x00|\x01\x00i\x08\x00\x83\x01\x00o\x10\x00\x01|\x00\x00i\n\x00t\x0b\x00i\x0c\x00j\x04\x00o\x17\x00\x01|\x02\x00i\r\x00t\x02\x00i\x03\x00i\x0e\x00j\x02\x00Sn\x01\x00\x01t\x05\x00Sd\x00\x00S' (60 00 00 00 7C 02 00 69 01 00 74 02 00 69 03 00 69 04 00 6A 03 00 6F 08 00 01 74 05 00 53 6E 01 00 01 74 06 00 7C 01 00 69 08 00 83 01 00 6F 10 00 01 7C 00 00 69 0A 00 74 0B 00 69 0C 00 6A 04 00 6F 17 00 01 7C 02 00 69 0D 00 74 02 00 69 03 00 69 0E 00 6A 02 00 53 6E 01 00 01 74 05 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'result'
                             00000003     69 - LOAD_ATTR           'outcomeFlag'
                             00000006     74 - LOAD_GLOBAL         'constants'
                             00000009     69 - LOAD_ATTR           'combat'
                             0000000C     69 - LOAD_ATTR           'ATTACKER_WINS'
                             0000000F     6A - COMPARE_OP          "!="
                             00000012     6F - JUMP_IF_FALSE       -> 0000001D
                             00000015     01 - POP_TOP             
                             00000016     74 - LOAD_GLOBAL         'False'
                             00000019     53 - RETURN_VALUE        
                             0000001A     6E - JUMP_FORWARD        -> 0000001E
                             0000001D     01 - POP_TOP             
                             0000001E     74 - LOAD_GLOBAL         'isUsingWeapon'
                             00000021     7C - LOAD_FAST           'loser'
                             00000024     69 - LOAD_ATTR           'equippedItemType'
                             00000027     83 - CALL_FUNCTION       r0001
                             0000002A     6F - JUMP_IF_FALSE       -> 0000003D
                             0000002D     01 - POP_TOP             
                             0000002E     7C - LOAD_FAST           'winner'
                             00000031     69 - LOAD_ATTR           'opponentCount'
                             00000034     74 - LOAD_GLOBAL         'consolevar'
                             00000037     69 - LOAD_ATTR           'CombatShortMoveCount'
                             0000003A     6A - COMPARE_OP          ">"
                             0000003D     6F - JUMP_IF_FALSE       -> 00000057
                             00000040     01 - POP_TOP             
                             00000041     7C - LOAD_FAST           'result'
                             00000044     69 - LOAD_ATTR           'distance'
                             00000047     74 - LOAD_GLOBAL         'constants'
                             0000004A     69 - LOAD_ATTR           'combat'
                             0000004D     69 - LOAD_ATTR           'SHORT_RANGE'
                             00000050     6A - COMPARE_OP          "=="
                             00000053     53 - RETURN_VALUE        
                             00000054     6E - JUMP_FORWARD        -> 00000058
                             00000057     01 - POP_TOP             
                             00000058     74 - LOAD_GLOBAL         'False'
                             0000005B     53 - RETURN_VALUE        
                             0000005C     64 - LOAD_CONST          None
                             0000005F     53 - RETURN_VALUE        
                         consts:
00002020                     TUPLE: (
00002025                         None (4E)
                             )
                         names:
00002026                     TUPLE: (
0000202B                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00002036                         STR: 'outcomeFlag' (0B 00 00 00 6F 75 74 63 6F 6D 65 46 6C 61 67),
00002046                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00002054                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
0000205F                         STR: 'ATTACKER_WINS' (0D 00 00 00 41 54 54 41 43 4B 45 52 5F 57 49 4E 53),
00002071                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
0000207B                         STR: 'isUsingWeapon' (0D 00 00 00 69 73 55 73 69 6E 67 57 65 61 70 6F 6E),
0000208D                         STR: 'loser' (05 00 00 00 6C 6F 73 65 72),
00002097                         STR: 'equippedItemType' (10 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D 54 79 70 65),
000020AC                         STR: 'winner' (06 00 00 00 77 69 6E 6E 65 72),
000020B7                         STR: 'opponentCount' (0D 00 00 00 6F 70 70 6F 6E 65 6E 74 43 6F 75 6E 74),
000020C9                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
000020D8                         STR: 'CombatShortMoveCount' (14 00 00 00 43 6F 6D 62 61 74 53 68 6F 72 74 4D 6F 76 65 43 6F 75 6E 74),
000020F1                         STR: 'distance' (08 00 00 00 64 69 73 74 61 6E 63 65),
000020FE                         STR: 'SHORT_RANGE' (0B 00 00 00 53 48 4F 52 54 5F 52 41 4E 47 45)
                             )
                         varnames:
0000210E                     TUPLE: (
00002113                         STR: 'winner' (06 00 00 00 77 69 6E 6E 65 72),
0000211E                         STR: 'loser' (05 00 00 00 6C 6F 73 65 72),
00002128                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74)
                             )
                         freevars:
00002133                     TUPLE: ()
                         cellvars:
00002138                     TUPLE: ()
                         filename:
0000213D                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_utility.py' (50 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79 2E 70 79)
                         name:
00002192                     STR: 'possibleDisarmMove' (12 00 00 00 70 6F 73 73 69 62 6C 65 44 69 73 61 72 6D 4D 6F 76 65)
                         firslineno:
000021A9                     LONG: 215L (D7 00 00 00)
                         lnotab:
000021AD                     STR: '\x00\x03\x16\x01\x08\x03#\x01\x17\x02' (0A 00 00 00 00 03 16 01 08 03 23 01 17 02),
000021BC             CODE:
                         argcount:
000021BD                     LONG: 3L (03 00 00 00)
                         nlocals:
000021C1                     LONG: 3L (03 00 00 00)
                         stacksize:
000021C5                     LONG: 5L (05 00 00 00)
                         flags:
000021C9                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000021CD                     STR: '|\x02\x00i\x01\x00t\x02\x00i\x03\x00i\x04\x00j\x02\x00p)\x00\x01|\x02\x00i\x01\x00t\x02\x00i\x03\x00i\x05\x00j\x02\x00p\x13\x00\x01|\x02\x00i\x01\x00t\x02\x00i\x03\x00i\x06\x00j\x02\x00o\xd4\x00\x01t\x07\x00d\x01\x00|\x00\x00i\t\x00|\x01\x00i\t\x00t\x0b\x00i\x0c\x00f\x03\x00\x16d\x02\x00\x83\x02\x00\x01|\x00\x00i\t\x00t\x0b\x00i\x0c\x00j\x01\x00o\x10\x00\x01|\x01\x00i\t\x00t\x0b\x00i\x0c\x00j\x01\x00o\x15\x00\x01t\x07\x00d\x03\x00d\x02\x00\x83\x02\x00\x01t\r\x00Sn\x01\x00\x01t\x0e\x00|\x00\x00|\x01\x00|\x02\x00\x83\x03\x00o\x08\x00\x01t\r\x00Sn\x01\x00\x01t\x07\x00d\x04\x00|\x02\x00i\x0f\x00t\x02\x00i\x03\x00i\x10\x00j\x02\x00\x16d\x02\x00\x83\x02\x00\x01t\x11\x00|\x00\x00i\x12\x00\x83\x01\x00o#\x00\x01|\x00\x00i\t\x00t\x0b\x00i\x0c\x00j\x01\x00o\x08\x00\x01t\r\x00Sq\x12\x01\x01t\x13\x00Sq\x1a\x01\x01t\x13\x00Sn\x05\x00\x01t\r\x00Sd\x00\x00S' (1E 01 00 00 7C 02 00 69 01 00 74 02 00 69 03 00 69 04 00 6A 02 00 70 29 00 01 7C 02 00 69 01 00 74 02 00 69 03 00 69 05 00 6A 02 00 70 13 00 01 7C 02 00 69 01 00 74 02 00 69 03 00 69 06 00 6A 02 00 6F D4 00 01 74 07 00 64 01 00 7C 00 00 69 09 00 7C 01 00 69 09 00 74 0B 00 69 0C 00 66 03 00 16 64 02 00 83 02 00 01 7C 00 00 69 09 00 74 0B 00 69 0C 00 6A 01 00 6F 10 00 01 7C 01 00 69 09 00 74 0B 00 69 0C 00 6A 01 00 6F 15 00 01 74 07 00 64 03 00 64 02 00 83 02 00 01 74 0D 00 53 6E 01 00 01 74 0E 00 7C 00 00 7C 01 00 7C 02 00 83 03 00 6F 08 00 01 74 0D 00 53 6E 01 00 01 74 07 00 64 04 00 7C 02 00 69 0F 00 74 02 00 69 03 00 69 10 00 6A 02 00 16 64 02 00 83 02 00 01 74 11 00 7C 00 00 69 12 00 83 01 00 6F 23 00 01 7C 00 00 69 09 00 74 0B 00 69 0C 00 6A 01 00 6F 08 00 01 74 0D 00 53 71 12 01 01 74 13 00 53 71 1A 01 01 74 13 00 53 6E 05 00 01 74 0D 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'result'
                             00000003     69 - LOAD_ATTR           'outcomeFlag'
                             00000006     74 - LOAD_GLOBAL         'constants'
                             00000009     69 - LOAD_ATTR           'combat'
                             0000000C     69 - LOAD_ATTR           'DRAW'
                             0000000F     6A - COMPARE_OP          "=="
                             00000012     70 - JUMP_IF_TRUE        -> 0000003E
                             00000015     01 - POP_TOP             
                             00000016     7C - LOAD_FAST           'result'
                             00000019     69 - LOAD_ATTR           'outcomeFlag'
                             0000001C     74 - LOAD_GLOBAL         'constants'
                             0000001F     69 - LOAD_ATTR           'combat'
                             00000022     69 - LOAD_ATTR           'ATTACKER_WINS'
                             00000025     6A - COMPARE_OP          "=="
                             00000028     70 - JUMP_IF_TRUE        -> 0000003E
                             0000002B     01 - POP_TOP             
                             0000002C     7C - LOAD_FAST           'result'
                             0000002F     69 - LOAD_ATTR           'outcomeFlag'
                             00000032     74 - LOAD_GLOBAL         'constants'
                             00000035     69 - LOAD_ATTR           'combat'
                             00000038     69 - LOAD_ATTR           'FINISHING_MOVE'
                             0000003B     6A - COMPARE_OP          "=="
                             0000003E     6F - JUMP_IF_FALSE       -> 00000115
                             00000041     01 - POP_TOP             
                             00000042     74 - LOAD_GLOBAL         'outputCombatDebugMessage'
                             00000045     64 - LOAD_CONST          'short move w:%d l:%d count:%d?'
                             00000048     7C - LOAD_FAST           'winner'
                             0000004B     69 - LOAD_ATTR           'opponentCount'
                             0000004E     7C - LOAD_FAST           'loser'
                             00000051     69 - LOAD_ATTR           'opponentCount'
                             00000054     74 - LOAD_GLOBAL         'consolevar'
                             00000057     69 - LOAD_ATTR           'CombatShortMoveCount'
                             0000005A     66 - BUILD_TUPLE         r0003
                             0000005D     16 - BINARY_MODULO       
                             0000005E     64 - LOAD_CONST          2
                             00000061     83 - CALL_FUNCTION       r0002
                             00000064     01 - POP_TOP             
                             00000065     7C - LOAD_FAST           'winner'
                             00000068     69 - LOAD_ATTR           'opponentCount'
                             0000006B     74 - LOAD_GLOBAL         'consolevar'
                             0000006E     69 - LOAD_ATTR           'CombatShortMoveCount'
                             00000071     6A - COMPARE_OP          "<="
                             00000074     6F - JUMP_IF_FALSE       -> 00000087
                             00000077     01 - POP_TOP             
                             00000078     7C - LOAD_FAST           'loser'
                             0000007B     69 - LOAD_ATTR           'opponentCount'
                             0000007E     74 - LOAD_GLOBAL         'consolevar'
                             00000081     69 - LOAD_ATTR           'CombatShortMoveCount'
                             00000084     6A - COMPARE_OP          "<="
                             00000087     6F - JUMP_IF_FALSE       -> 0000009F
                             0000008A     01 - POP_TOP             
                             0000008B     74 - LOAD_GLOBAL         'outputCombatDebugMessage'
                             0000008E     64 - LOAD_CONST          'combatants not in multi-on-one'
                             00000091     64 - LOAD_CONST          2
                             00000094     83 - CALL_FUNCTION       r0002
                             00000097     01 - POP_TOP             
                             00000098     74 - LOAD_GLOBAL         'False'
                             0000009B     53 - RETURN_VALUE        
                             0000009C     6E - JUMP_FORWARD        -> 000000A0
                             0000009F     01 - POP_TOP             
                             000000A0     74 - LOAD_GLOBAL         'possibleDisarmMove'
                             000000A3     7C - LOAD_FAST           'winner'
                             000000A6     7C - LOAD_FAST           'loser'
                             000000A9     7C - LOAD_FAST           'result'
                             000000AC     83 - CALL_FUNCTION       r0003
                             000000AF     6F - JUMP_IF_FALSE       -> 000000BA
                             000000B2     01 - POP_TOP             
                             000000B3     74 - LOAD_GLOBAL         'False'
                             000000B6     53 - RETURN_VALUE        
                             000000B7     6E - JUMP_FORWARD        -> 000000BB
                             000000BA     01 - POP_TOP             
                             000000BB     74 - LOAD_GLOBAL         'outputCombatDebugMessage'
                             000000BE     64 - LOAD_CONST          'at short range? %d'
                             000000C1     7C - LOAD_FAST           'result'
                             000000C4     69 - LOAD_ATTR           'distance'
                             000000C7     74 - LOAD_GLOBAL         'constants'
                             000000CA     69 - LOAD_ATTR           'combat'
                             000000CD     69 - LOAD_ATTR           'SHORT_RANGE'
                             000000D0     6A - COMPARE_OP          "=="
                             000000D3     16 - BINARY_MODULO       
                             000000D4     64 - LOAD_CONST          2
                             000000D7     83 - CALL_FUNCTION       r0002
                             000000DA     01 - POP_TOP             
                             000000DB     74 - LOAD_GLOBAL         'isUsingWeapon'
                             000000DE     7C - LOAD_FAST           'winner'
                             000000E1     69 - LOAD_ATTR           'equippedItemType'
                             000000E4     83 - CALL_FUNCTION       r0001
                             000000E7     6F - JUMP_IF_FALSE       -> 0000010D
                             000000EA     01 - POP_TOP             
                             000000EB     7C - LOAD_FAST           'winner'
                             000000EE     69 - LOAD_ATTR           'opponentCount'
                             000000F1     74 - LOAD_GLOBAL         'consolevar'
                             000000F4     69 - LOAD_ATTR           'CombatShortMoveCount'
                             000000F7     6A - COMPARE_OP          "<="
                             000000FA     6F - JUMP_IF_FALSE       -> 00000105
                             000000FD     01 - POP_TOP             
                             000000FE     74 - LOAD_GLOBAL         'False'
                             00000101     53 - RETURN_VALUE        
                             00000102     71 - JUMP_ABSOLUTE       -> 00000112
                             00000105     01 - POP_TOP             
                             00000106     74 - LOAD_GLOBAL         'True'
                             00000109     53 - RETURN_VALUE        
                             0000010A     71 - JUMP_ABSOLUTE       -> 0000011A
                             0000010D     01 - POP_TOP             
                             0000010E     74 - LOAD_GLOBAL         'True'
                             00000111     53 - RETURN_VALUE        
                             00000112     6E - JUMP_FORWARD        -> 0000011A
                             00000115     01 - POP_TOP             
                             00000116     74 - LOAD_GLOBAL         'False'
                             00000119     53 - RETURN_VALUE        
                             0000011A     64 - LOAD_CONST          None
                             0000011D     53 - RETURN_VALUE        
                         consts:
000022F0                     TUPLE: (
000022F5                         None (4E),
000022F6                         STR: 'short move w:%d l:%d count:%d?' (1E 00 00 00 73 68 6F 72 74 20 6D 6F 76 65 20 77 3A 25 64 20 6C 3A 25 64 20 63 6F 75 6E 74 3A 25 64 3F),
00002319                         INT: 2 (02 00 00 00),
0000231E                         STR: 'combatants not in multi-on-one' (1E 00 00 00 63 6F 6D 62 61 74 61 6E 74 73 20 6E 6F 74 20 69 6E 20 6D 75 6C 74 69 2D 6F 6E 2D 6F 6E 65),
00002341                         STR: 'at short range? %d' (12 00 00 00 61 74 20 73 68 6F 72 74 20 72 61 6E 67 65 3F 20 25 64)
                             )
                         names:
00002358                     TUPLE: (
0000235D                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00002368                         STR: 'outcomeFlag' (0B 00 00 00 6F 75 74 63 6F 6D 65 46 6C 61 67),
00002378                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00002386                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
00002391                         STR: 'DRAW' (04 00 00 00 44 52 41 57),
0000239A                         STR: 'ATTACKER_WINS' (0D 00 00 00 41 54 54 41 43 4B 45 52 5F 57 49 4E 53),
000023AC                         STR: 'FINISHING_MOVE' (0E 00 00 00 46 49 4E 49 53 48 49 4E 47 5F 4D 4F 56 45),
000023BF                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
000023DC                         STR: 'winner' (06 00 00 00 77 69 6E 6E 65 72),
000023E7                         STR: 'opponentCount' (0D 00 00 00 6F 70 70 6F 6E 65 6E 74 43 6F 75 6E 74),
000023F9                         STR: 'loser' (05 00 00 00 6C 6F 73 65 72),
00002403                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
00002412                         STR: 'CombatShortMoveCount' (14 00 00 00 43 6F 6D 62 61 74 53 68 6F 72 74 4D 6F 76 65 43 6F 75 6E 74),
0000242B                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
00002435                         STR: 'possibleDisarmMove' (12 00 00 00 70 6F 73 73 69 62 6C 65 44 69 73 61 72 6D 4D 6F 76 65),
0000244C                         STR: 'distance' (08 00 00 00 64 69 73 74 61 6E 63 65),
00002459                         STR: 'SHORT_RANGE' (0B 00 00 00 53 48 4F 52 54 5F 52 41 4E 47 45),
00002469                         STR: 'isUsingWeapon' (0D 00 00 00 69 73 55 73 69 6E 67 57 65 61 70 6F 6E),
0000247B                         STR: 'equippedItemType' (10 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D 54 79 70 65),
00002490                         STR: 'True' (04 00 00 00 54 72 75 65)
                             )
                         varnames:
00002499                     TUPLE: (
0000249E                         STR: 'winner' (06 00 00 00 77 69 6E 6E 65 72),
000024A9                         STR: 'loser' (05 00 00 00 6C 6F 73 65 72),
000024B3                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74)
                             )
                         freevars:
000024BE                     TUPLE: ()
                         cellvars:
000024C3                     TUPLE: ()
                         filename:
000024C8                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_utility.py' (50 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79 2E 70 79)
                         name:
0000251D                     STR: 'shortMoveAllowed' (10 00 00 00 73 68 6F 72 74 4D 6F 76 65 41 6C 6C 6F 77 65 64)
                         firslineno:
00002532                     LONG: 228L (E4 00 00 00)
                         lnotab:
00002536                     STR: '\x00\x01B\x01#\x03&\x01\r\x01\x08\x02\x13\x01\x08\x03 \x01\x10\x01\x13\x01\x08\x02\x08\x02\x08\x03' (1C 00 00 00 00 01 42 01 23 03 26 01 0D 01 08 02 13 01 08 03 20 01 10 01 13 01 08 02 08 02 08 03),
00002557             CODE:
                         argcount:
00002558                     LONG: 1L (01 00 00 00)
                         nlocals:
0000255C                     LONG: 1L (01 00 00 00)
                         stacksize:
00002560                     LONG: 2L (02 00 00 00)
                         flags:
00002564                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00002568                     STR: '|\x00\x00t\x01\x00j\x08\x00o\x08\x00\x01d\x01\x00Sn\x01\x00\x01|\x00\x00Sd\x00\x00S' (1D 00 00 00 7C 00 00 74 01 00 6A 08 00 6F 08 00 01 64 01 00 53 6E 01 00 01 7C 00 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'possible'
                             00000003     74 - LOAD_GLOBAL         'None'
                             00000006     6A - COMPARE_OP          "is"
                             00000009     6F - JUMP_IF_FALSE       -> 00000014
                             0000000C     01 - POP_TOP             
                             0000000D     64 - LOAD_CONST          0
                             00000010     53 - RETURN_VALUE        
                             00000011     6E - JUMP_FORWARD        -> 00000015
                             00000014     01 - POP_TOP             
                             00000015     7C - LOAD_FAST           'possible'
                             00000018     53 - RETURN_VALUE        
                             00000019     64 - LOAD_CONST          None
                             0000001C     53 - RETURN_VALUE        
                         consts:
0000258A                     TUPLE: (
0000258F                         None (4E),
00002590                         INT: 0 (00 00 00 00)
                             )
                         names:
00002595                     TUPLE: (
0000259A                         STR: 'possible' (08 00 00 00 70 6F 73 73 69 62 6C 65),
000025A7                         STR: 'None' (04 00 00 00 4E 6F 6E 65)
                             )
                         varnames:
000025B0                     TUPLE: (
000025B5                         STR: 'possible' (08 00 00 00 70 6F 73 73 69 62 6C 65)
                             )
                         freevars:
000025C2                     TUPLE: ()
                         cellvars:
000025C7                     TUPLE: ()
                         filename:
000025CC                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_utility.py' (50 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79 2E 70 79)
                         name:
00002621                     STR: 'safeAbVal' (09 00 00 00 73 61 66 65 41 62 56 61 6C)
                         firslineno:
0000262F                     LONG: 253L (FD 00 00 00)
                         lnotab:
00002633                     STR: '\x00\x01\r\x01\x08\x02' (06 00 00 00 00 01 0D 01 08 02)
                 )
             names:
0000263E         TUPLE: (
00002643             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
0000264E             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
0000265C             STR: 'obj' (03 00 00 00 6F 62 6A),
00002664             STR: 'combat_defines' (0E 00 00 00 63 6F 6D 62 61 74 5F 64 65 66 69 6E 65 73),
00002677             STR: 'CD' (02 00 00 00 43 44),
0000267E             STR: 'math' (04 00 00 00 6D 61 74 68),
00002687             STR: 'outputToAll' (0B 00 00 00 6F 75 74 70 75 74 54 6F 41 6C 6C),
00002697             STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
000026B4             STR: 'None' (04 00 00 00 4E 6F 6E 65),
000026BD             STR: 'outputCombatDebugMessageAll' (1B 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 41 6C 6C),
000026DD             STR: 'outputCombatDebugMessageOnMatch' (1F 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 4F 6E 4D 61 74 63 68),
00002701             STR: 'isAbilityMartialArt' (13 00 00 00 69 73 41 62 69 6C 69 74 79 4D 61 72 74 69 61 6C 41 72 74),
00002719             STR: 'isPreferredTactical' (13 00 00 00 69 73 50 72 65 66 65 72 72 65 64 54 61 63 74 69 63 61 6C),
00002731             STR: 'isPreferredFinishingTactical' (1C 00 00 00 69 73 50 72 65 66 65 72 72 65 64 46 69 6E 69 73 68 69 6E 67 54 61 63 74 69 63 61 6C),
00002752             STR: 'isUsingWeapon' (0D 00 00 00 69 73 55 73 69 6E 67 57 65 61 70 6F 6E),
00002764             STR: 'isEscapeAbility' (0F 00 00 00 69 73 45 73 63 61 70 65 41 62 69 6C 69 74 79),
00002778             STR: 'isSpecialMove' (0D 00 00 00 69 73 53 70 65 63 69 61 6C 4D 6F 76 65),
0000278A             STR: 'isPlayerWithdrawing' (13 00 00 00 69 73 50 6C 61 79 65 72 57 69 74 68 64 72 61 77 69 6E 67),
000027A2             STR: 'isPlayerCombatProne' (13 00 00 00 69 73 50 6C 61 79 65 72 43 6F 6D 62 61 74 50 72 6F 6E 65),
000027BA             STR: 'isPlayerBeingGanged' (13 00 00 00 69 73 50 6C 61 79 65 72 42 65 69 6E 67 47 61 6E 67 65 64),
000027D2             STR: 'False' (05 00 00 00 46 61 6C 73 65),
000027DC             STR: 'determineBulletTime' (13 00 00 00 64 65 74 65 72 6D 69 6E 65 42 75 6C 6C 65 74 54 69 6D 65),
000027F4             STR: 'finishingMoveAllowed' (14 00 00 00 66 69 6E 69 73 68 69 6E 67 4D 6F 76 65 41 6C 6C 6F 77 65 64),
0000280D             STR: 'killingMoveAllowed' (12 00 00 00 6B 69 6C 6C 69 6E 67 4D 6F 76 65 41 6C 6C 6F 77 65 64),
00002824             STR: 'possibleDisarmMove' (12 00 00 00 70 6F 73 73 69 62 6C 65 44 69 73 61 72 6D 4D 6F 76 65),
0000283B             STR: 'shortMoveAllowed' (10 00 00 00 73 68 6F 72 74 4D 6F 76 65 41 6C 6C 6F 77 65 64),
00002850             STR: 'safeAbVal' (09 00 00 00 73 61 66 65 41 62 56 61 6C)
                 )
             varnames:
0000285E         TUPLE: (
00002863             STR: 'safeAbVal' (09 00 00 00 73 61 66 65 41 62 56 61 6C),
00002871             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
0000287C             STR: 'isEscapeAbility' (0F 00 00 00 69 73 45 73 63 61 70 65 41 62 69 6C 69 74 79),
00002890             STR: 'isPreferredTactical' (13 00 00 00 69 73 50 72 65 66 65 72 72 65 64 54 61 63 74 69 63 61 6C),
000028A8             STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
000028C5             STR: 'isUsingWeapon' (0D 00 00 00 69 73 55 73 69 6E 67 57 65 61 70 6F 6E),
000028D7             STR: 'possibleDisarmMove' (12 00 00 00 70 6F 73 73 69 62 6C 65 44 69 73 61 72 6D 4D 6F 76 65),
000028EE             STR: 'shortMoveAllowed' (10 00 00 00 73 68 6F 72 74 4D 6F 76 65 41 6C 6C 6F 77 65 64),
00002903             STR: 'isPreferredFinishingTactical' (1C 00 00 00 69 73 50 72 65 66 65 72 72 65 64 46 69 6E 69 73 68 69 6E 67 54 61 63 74 69 63 61 6C),
00002924             STR: 'finishingMoveAllowed' (14 00 00 00 66 69 6E 69 73 68 69 6E 67 4D 6F 76 65 41 6C 6C 6F 77 65 64),
0000293D             STR: 'outputCombatDebugMessageOnMatch' (1F 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 4F 6E 4D 61 74 63 68),
00002961             STR: 'isSpecialMove' (0D 00 00 00 69 73 53 70 65 63 69 61 6C 4D 6F 76 65),
00002973             STR: 'isPlayerBeingGanged' (13 00 00 00 69 73 50 6C 61 79 65 72 42 65 69 6E 67 47 61 6E 67 65 64),
0000298B             STR: 'outputToAll' (0B 00 00 00 6F 75 74 70 75 74 54 6F 41 6C 6C),
0000299B             STR: 'math' (04 00 00 00 6D 61 74 68),
000029A4             STR: 'outputCombatDebugMessageAll' (1B 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 41 6C 6C),
000029C4             STR: 'CD' (02 00 00 00 43 44),
000029CB             STR: 'isPlayerCombatProne' (13 00 00 00 69 73 50 6C 61 79 65 72 43 6F 6D 62 61 74 50 72 6F 6E 65),
000029E3             STR: 'isAbilityMartialArt' (13 00 00 00 69 73 41 62 69 6C 69 74 79 4D 61 72 74 69 61 6C 41 72 74),
000029FB             STR: 'obj' (03 00 00 00 6F 62 6A),
00002A03             STR: 'determineBulletTime' (13 00 00 00 64 65 74 65 72 6D 69 6E 65 42 75 6C 6C 65 74 54 69 6D 65),
00002A1B             STR: 'isPlayerWithdrawing' (13 00 00 00 69 73 50 6C 61 79 65 72 57 69 74 68 64 72 61 77 69 6E 67),
00002A33             STR: 'killingMoveAllowed' (12 00 00 00 6B 69 6C 6C 69 6E 67 4D 6F 76 65 41 6C 6C 6F 77 65 64),
00002A4A             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B)
                 )
             freevars:
00002A58         TUPLE: ()
             cellvars:
00002A5D         TUPLE: ()
             filename:
00002A62         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_utility.py' (50 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79 2E 70 79)
             name:
00002AB7         STR: '?' (01 00 00 00 3F)
             firslineno:
00002ABD         LONG: 1L (01 00 00 00)
             lnotab:
00002AC1         STR: '\t\x01\t\x01\t\x01\t\x01\t\x02\t\x05\t\x07\x0f\x0b\t\x04\t\n\t\x0e\t\t\t\x1a\t\x1a\t\x08\t\t\t\t\t\x04\x0c \t\x1a\t\x08\t\r\t\x19' (2E 00 00 00 09 01 09 01 09 01 09 01 09 02 09 05 09 07 0F 0B 09 04 09 0A 09 0E 09 09 09 1A 09 1A 09 08 09 09 09 09 09 04 0C 20 09 1A 09 08 09 0D 09 19)

