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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00Z\x03\x00d\x00\x00k\x04\x00Z\x04\x00d\x00\x00k\x05\x00Z\x06\x00d\x01\x00k\x07\x00l\x07\x00Z\x07\x00\x01d\x00\x00k\x08\x00Z\t\x00d\x02\x00Z\n\x00d\x03\x00Z\x0b\x00d\x04\x00\x84\x00\x00Z\x0c\x00d\x05\x00\x84\x00\x00Z\r\x00d\x06\x00\x84\x00\x00Z\x0e\x00d\x07\x00e\x0e\x00_\x0f\x00d\x08\x00\x84\x00\x00Z\x10\x00d\t\x00\x84\x00\x00Z\x11\x00d\n\x00\x84\x00\x00Z\x12\x00d\x0b\x00\x84\x00\x00Z\x13\x00d\x0c\x00\x84\x00\x00Z\x14\x00d\r\x00\x84\x00\x00Z\x15\x00d\x0e\x00\x84\x00\x00Z\x16\x00d\x0f\x00\x84\x00\x00Z\x17\x00d\x10\x00\x84\x00\x00Z\x18\x00d\x11\x00\x84\x00\x00Z\x19\x00d\x12\x00\x84\x00\x00Z\x1a\x00d\x00\x00S' (DA 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 5A 03 00 64 00 00 6B 04 00 5A 04 00 64 00 00 6B 05 00 5A 06 00 64 01 00 6B 07 00 6C 07 00 5A 07 00 01 64 00 00 6B 08 00 5A 09 00 64 02 00 5A 0A 00 64 03 00 5A 0B 00 64 04 00 84 00 00 5A 0C 00 64 05 00 84 00 00 5A 0D 00 64 06 00 84 00 00 5A 0E 00 64 07 00 65 0E 00 5F 0F 00 64 08 00 84 00 00 5A 10 00 64 09 00 84 00 00 5A 11 00 64 0A 00 84 00 00 5A 12 00 64 0B 00 84 00 00 5A 13 00 64 0C 00 84 00 00 5A 14 00 64 0D 00 84 00 00 5A 15 00 64 0E 00 84 00 00 5A 16 00 64 0F 00 84 00 00 5A 17 00 64 10 00 84 00 00 5A 18 00 64 11 00 84 00 00 5A 19 00 64 12 00 84 00 00 5A 1A 00 64 00 00 53)
                 00000000     64 - LOAD_CONST          None
                 00000003     6B - IMPORT_NAME         'random'
                 00000006     5A - STORE_NAME          'random'
                 00000009     64 - LOAD_CONST          None
                 0000000C     6B - IMPORT_NAME         'traceback'
                 0000000F     5A - STORE_NAME          'traceback'
                 00000012     64 - LOAD_CONST          None
                 00000015     6B - IMPORT_NAME         'ability.utility'
                 00000018     5A - STORE_NAME          'ability'
                 0000001B     64 - LOAD_CONST          None
                 0000001E     6B - IMPORT_NAME         'obj'
                 00000021     5A - STORE_NAME          'obj'
                 00000024     64 - LOAD_CONST          None
                 00000027     6B - IMPORT_NAME         'stringtable_client'
                 0000002A     5A - STORE_NAME          'ST'
                 0000002D     64 - LOAD_CONST          ('RewardSelection')
                 00000030     6B - IMPORT_NAME         'RewardSelection'
                 00000033     6C - IMPORT_FROM         'RewardSelection'
                 00000036     5A - STORE_NAME          'RewardSelection'
                 00000039     01 - POP_TOP             
                 0000003A     64 - LOAD_CONST          None
                 0000003D     6B - IMPORT_NAME         'ltfxmap'
                 00000040     5A - STORE_NAME          'FX'
                 00000043     64 - LOAD_CONST          0.12
                 00000046     5A - STORE_NAME          'COMPILE_DISCOUNT'
                 00000049     64 - LOAD_CONST          60.0
                 0000004C     5A - STORE_NAME          'CODER_DURATION'
                 0000004F     64 - LOAD_CONST          CODE('craftingFeedback')
                 00000052     84 - MAKE_FUNCTION       r0000
                 00000055     5A - STORE_NAME          'craftingFeedback'
                 00000058     64 - LOAD_CONST          CODE('isPill')
                 0000005B     84 - MAKE_FUNCTION       r0000
                 0000005E     5A - STORE_NAME          'isPill'
                 00000061     64 - LOAD_CONST          CODE('gD100')
                 00000064     84 - MAKE_FUNCTION       r0000
                 00000067     5A - STORE_NAME          'gD100'
                 0000006A     64 - LOAD_CONST          16
                 0000006D     65 - LOAD_NAME           'gD100'
                 00000070     5F - STORE_ATTR          'stdDev'
                 00000073     64 - LOAD_CONST          CODE('toFourCC')
                 00000076     84 - MAKE_FUNCTION       r0000
                 00000079     5A - STORE_NAME          'toFourCC'
                 0000007C     64 - LOAD_CONST          CODE('DecompileInnerStrengthCost')
                 0000007F     84 - MAKE_FUNCTION       r0000
                 00000082     5A - STORE_NAME          'DecompileInnerStrengthCost'
                 00000085     64 - LOAD_CONST          CODE('DecompStabPurContrib')
                 00000088     84 - MAKE_FUNCTION       r0000
                 0000008B     5A - STORE_NAME          'DecompStabPurContrib'
                 0000008E     64 - LOAD_CONST          CODE('DecompileTest')
                 00000091     84 - MAKE_FUNCTION       r0000
                 00000094     5A - STORE_NAME          'DecompileTest'
                 00000097     64 - LOAD_CONST          CODE('DecompileFragmentRecoveryTest')
                 0000009A     84 - MAKE_FUNCTION       r0000
                 0000009D     5A - STORE_NAME          'DecompileFragmentRecoveryTest'
                 000000A0     64 - LOAD_CONST          CODE('CompileInfoCost')
                 000000A3     84 - MAKE_FUNCTION       r0000
                 000000A6     5A - STORE_NAME          'CompileInfoCost'
                 000000A9     64 - LOAD_CONST          CODE('GetAbilityBonusByCategory')
                 000000AC     84 - MAKE_FUNCTION       r0000
                 000000AF     5A - STORE_NAME          'GetAbilityBonusByCategory'
                 000000B2     64 - LOAD_CONST          CODE('CalcItemInfoCost')
                 000000B5     84 - MAKE_FUNCTION       r0000
                 000000B8     5A - STORE_NAME          'CalcItemInfoCost'
                 000000BB     64 - LOAD_CONST          CODE('CompileTest')
                 000000BE     84 - MAKE_FUNCTION       r0000
                 000000C1     5A - STORE_NAME          'CompileTest'
                 000000C4     64 - LOAD_CONST          CODE('WriteCodeTest')
                 000000C7     84 - MAKE_FUNCTION       r0000
                 000000CA     5A - STORE_NAME          'WriteCodeTest'
                 000000CD     64 - LOAD_CONST          CODE('CoderApplication')
                 000000D0     84 - MAKE_FUNCTION       r0000
                 000000D3     5A - STORE_NAME          'CoderApplication'
                 000000D6     64 - LOAD_CONST          None
                 000000D9     53 - RETURN_VALUE        
             consts:
000000F8         TUPLE: (
000000FD             None (4E),
000000FE             TUPLE: (
00000103                 STR: 'RewardSelection' (0F 00 00 00 52 65 77 61 72 64 53 65 6C 65 63 74 69 6F 6E)
                     ),
00000117             FLOAT: 0.12 (04 30 2E 31 32),
0000011D             FLOAT: 60.0 (04 36 30 2E 30),
00000123             CODE:
                         argcount:
00000124                     LONG: 2L (02 00 00 00)
                         nlocals:
00000128                     LONG: 2L (02 00 00 00)
                         stacksize:
0000012C                     LONG: 3L (03 00 00 00)
                         flags:
00000130                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000134                     STR: 't\x00\x00i\x01\x00d\x01\x00j\x04\x00o\x17\x00\x01|\x00\x00i\x03\x00i\x04\x00d\x02\x00|\x01\x00\x83\x02\x00\x01n\x01\x00\x01d\x00\x00S' (2B 00 00 00 74 00 00 69 01 00 64 01 00 6A 04 00 6F 17 00 01 7C 00 00 69 03 00 69 04 00 64 02 00 7C 01 00 83 02 00 01 6E 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consolevar'
                             00000003     69 - LOAD_ATTR           'CraftingDebugPrint'
                             00000006     64 - LOAD_CONST          0
                             00000009     6A - COMPARE_OP          ">"
                             0000000C     6F - JUMP_IF_FALSE       -> 00000026
                             0000000F     01 - POP_TOP             
                             00000010     7C - LOAD_FAST           'subject'
                             00000013     69 - LOAD_ATTR           'AbilityInv'
                             00000016     69 - LOAD_ATTR           'sendChat'
                             00000019     64 - LOAD_CONST          ''
                             0000001C     7C - LOAD_FAST           'str'
                             0000001F     83 - CALL_FUNCTION       r0002
                             00000022     01 - POP_TOP             
                             00000023     6E - JUMP_FORWARD        -> 00000027
                             00000026     01 - POP_TOP             
                             00000027     64 - LOAD_CONST          None
                             0000002A     53 - RETURN_VALUE        
                         consts:
00000164                     TUPLE: (
00000169                         None (4E),
0000016A                         INT: 0 (00 00 00 00),
0000016F                         STR: '' (00 00 00 00)
                             )
                         names:
00000174                     TUPLE: (
00000179                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
00000188                         STR: 'CraftingDebugPrint' (12 00 00 00 43 72 61 66 74 69 6E 67 44 65 62 75 67 50 72 69 6E 74),
0000019F                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000001AB                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
000001BA                         STR: 'sendChat' (08 00 00 00 73 65 6E 64 43 68 61 74),
000001C7                         STR: 'str' (03 00 00 00 73 74 72)
                             )
                         varnames:
000001CF                     TUPLE: (
000001D4                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000001E0                         STR: 'str' (03 00 00 00 73 74 72)
                             )
                         freevars:
000001E8                     TUPLE: ()
                         cellvars:
000001ED                     TUPLE: ()
                         filename:
000001F2                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\crafting_server.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 72 61 66 74 69 6E 67 5F 73 65 72 76 65 72 2E 70 79)
                         name:
0000023E                     STR: 'craftingFeedback' (10 00 00 00 63 72 61 66 74 69 6E 67 46 65 65 64 62 61 63 6B)
                         firslineno:
00000253                     LONG: 23L (17 00 00 00)
                         lnotab:
00000257                     STR: '\x00\x01\x10\x01' (04 00 00 00 00 01 10 01),
00000260             CODE:
                         argcount:
00000261                     LONG: 1L (01 00 00 00)
                         nlocals:
00000265                     LONG: 2L (02 00 00 00)
                         stacksize:
00000269                     LONG: 2L (02 00 00 00)
                         flags:
0000026D                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000271                     STR: 't\x00\x00|\x00\x00\x83\x01\x00}\x01\x00|\x01\x00d\x01\x00\x19d\x02\x00j\x02\x00o\x0e\x00\x01|\x01\x00d\x03\x00\x19d\x04\x00j\x02\x00o\x08\x00\x01d\x03\x00Sn\x01\x00\x01d\x01\x00Sd\x00\x00S' (3E 00 00 00 74 00 00 7C 00 00 83 01 00 7D 01 00 7C 01 00 64 01 00 19 64 02 00 6A 02 00 6F 0E 00 01 7C 01 00 64 03 00 19 64 04 00 6A 02 00 6F 08 00 01 64 03 00 53 6E 01 00 01 64 01 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'toFourCC'
                             00000003     7C - LOAD_FAST           'category'
                             00000006     83 - CALL_FUNCTION       r0001
                             00000009     7D - STORE_FAST          'cat'
                             0000000C     7C - LOAD_FAST           'cat'
                             0000000F     64 - LOAD_CONST          0
                             00000012     19 - BINARY_SUBSCR       
                             00000013     64 - LOAD_CONST          'I'
                             00000016     6A - COMPARE_OP          "=="
                             00000019     6F - JUMP_IF_FALSE       -> 0000002A
                             0000001C     01 - POP_TOP             
                             0000001D     7C - LOAD_FAST           'cat'
                             00000020     64 - LOAD_CONST          1
                             00000023     19 - BINARY_SUBSCR       
                             00000024     64 - LOAD_CONST          'C'
                             00000027     6A - COMPARE_OP          "=="
                             0000002A     6F - JUMP_IF_FALSE       -> 00000035
                             0000002D     01 - POP_TOP             
                             0000002E     64 - LOAD_CONST          1
                             00000031     53 - RETURN_VALUE        
                             00000032     6E - JUMP_FORWARD        -> 00000036
                             00000035     01 - POP_TOP             
                             00000036     64 - LOAD_CONST          0
                             00000039     53 - RETURN_VALUE        
                             0000003A     64 - LOAD_CONST          None
                             0000003D     53 - RETURN_VALUE        
                         consts:
000002B4                     TUPLE: (
000002B9                         None (4E),
000002BA                         INT: 0 (00 00 00 00),
000002BF                         STR: 'I' (01 00 00 00 49),
000002C5                         INT: 1 (01 00 00 00),
000002CA                         STR: 'C' (01 00 00 00 43)
                             )
                         names:
000002D0                     TUPLE: (
000002D5                         STR: 'toFourCC' (08 00 00 00 74 6F 46 6F 75 72 43 43),
000002E2                         STR: 'category' (08 00 00 00 63 61 74 65 67 6F 72 79),
000002EF                         STR: 'cat' (03 00 00 00 63 61 74)
                             )
                         varnames:
000002F7                     TUPLE: (
000002FC                         STR: 'category' (08 00 00 00 63 61 74 65 67 6F 72 79),
00000309                         STR: 'cat' (03 00 00 00 63 61 74)
                             )
                         freevars:
00000311                     TUPLE: ()
                         cellvars:
00000316                     TUPLE: ()
                         filename:
0000031B                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\crafting_server.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 72 61 66 74 69 6E 67 5F 73 65 72 76 65 72 2E 70 79)
                         name:
00000367                     STR: 'isPill' (06 00 00 00 69 73 50 69 6C 6C)
                         firslineno:
00000372                     LONG: 30L (1E 00 00 00)
                         lnotab:
00000376                     STR: '\x00\x01\x0c\x01"\x01\x08\x01' (08 00 00 00 00 01 0C 01 22 01 08 01),
00000383             CODE:
                         argcount:
00000384                     LONG: 0L (00 00 00 00)
                         nlocals:
00000388                     LONG: 0L (00 00 00 00)
                         stacksize:
0000038C                     LONG: 6L (06 00 00 00)
                         flags:
00000390                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000394                     STR: 't\x00\x00t\x01\x00i\x02\x00d\x01\x00t\x03\x00i\x04\x00d\x02\x00d\x03\x00\x83\x04\x00\x83\x01\x00Sd\x00\x00S' (23 00 00 00 74 00 00 74 01 00 69 02 00 64 01 00 74 03 00 69 04 00 64 02 00 64 03 00 83 04 00 83 01 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'int'
                             00000003     74 - LOAD_GLOBAL         'discovery'
                             00000006     69 - LOAD_ATTR           'getGaussianRandomClamped'
                             00000009     64 - LOAD_CONST          50
                             0000000C     74 - LOAD_GLOBAL         'gD100'
                             0000000F     69 - LOAD_ATTR           'stdDev'
                             00000012     64 - LOAD_CONST          0
                             00000015     64 - LOAD_CONST          100
                             00000018     83 - CALL_FUNCTION       r0004
                             0000001B     83 - CALL_FUNCTION       r0001
                             0000001E     53 - RETURN_VALUE        
                             0000001F     64 - LOAD_CONST          None
                             00000022     53 - RETURN_VALUE        
                         consts:
000003BC                     TUPLE: (
000003C1                         None (4E),
000003C2                         INT: 50 (32 00 00 00),
000003C7                         INT: 0 (00 00 00 00),
000003CC                         INT: 100 (64 00 00 00)
                             )
                         names:
000003D1                     TUPLE: (
000003D6                         STR: 'int' (03 00 00 00 69 6E 74),
000003DE                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
000003EC                         STR: 'getGaussianRandomClamped' (18 00 00 00 67 65 74 47 61 75 73 73 69 61 6E 52 61 6E 64 6F 6D 43 6C 61 6D 70 65 64),
00000409                         STR: 'gD100' (05 00 00 00 67 44 31 30 30),
00000413                         STR: 'stdDev' (06 00 00 00 73 74 64 44 65 76)
                             )
                         varnames:
0000041E                     TUPLE: ()
                         freevars:
00000423                     TUPLE: ()
                         cellvars:
00000428                     TUPLE: ()
                         filename:
0000042D                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\crafting_server.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 72 61 66 74 69 6E 67 5F 73 65 72 76 65 72 2E 70 79)
                         name:
00000479                     STR: 'gD100' (05 00 00 00 67 44 31 30 30)
                         firslineno:
00000483                     LONG: 39L (27 00 00 00)
                         lnotab:
00000487                     STR: '\x00\x01' (02 00 00 00 00 01),
0000048E             INT: 16 (10 00 00 00),
00000493             CODE:
                         argcount:
00000494                     LONG: 1L (01 00 00 00)
                         nlocals:
00000498                     LONG: 2L (02 00 00 00)
                         stacksize:
0000049C                     LONG: 4L (04 00 00 00)
                         flags:
000004A0                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000004A4                     STR: 'd\x01\x00d\x01\x00d\x01\x00d\x01\x00g\x04\x00}\x01\x00t\x01\x00|\x00\x00d\x02\x00@\x83\x01\x00|\x01\x00d\x01\x00<t\x01\x00|\x00\x00d\x03\x00@d\x04\x00?\x83\x01\x00|\x01\x00d\x05\x00<t\x01\x00|\x00\x00d\x06\x00@d\x07\x00?\x83\x01\x00|\x01\x00d\x08\x00<t\x01\x00|\x00\x00t\x03\x00d\t\x00\x83\x01\x00@d\n\x00?\x83\x01\x00|\x01\x00d\x0b\x00<|\x01\x00Sd\x00\x00S' (7C 00 00 00 64 01 00 64 01 00 64 01 00 64 01 00 67 04 00 7D 01 00 74 01 00 7C 00 00 64 02 00 40 83 01 00 7C 01 00 64 01 00 3C 74 01 00 7C 00 00 64 03 00 40 64 04 00 3F 83 01 00 7C 01 00 64 05 00 3C 74 01 00 7C 00 00 64 06 00 40 64 07 00 3F 83 01 00 7C 01 00 64 08 00 3C 74 01 00 7C 00 00 74 03 00 64 09 00 83 01 00 40 64 0A 00 3F 83 01 00 7C 01 00 64 0B 00 3C 7C 01 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          0
                             00000003     64 - LOAD_CONST          0
                             00000006     64 - LOAD_CONST          0
                             00000009     64 - LOAD_CONST          0
                             0000000C     67 - BUILD_LIST          r0004
                             0000000F     7D - STORE_FAST          't'
                             00000012     74 - LOAD_GLOBAL         'chr'
                             00000015     7C - LOAD_FAST           'val'
                             00000018     64 - LOAD_CONST          255
                             0000001B     40 - BINARY_AND          
                             0000001C     83 - CALL_FUNCTION       r0001
                             0000001F     7C - LOAD_FAST           't'
                             00000022     64 - LOAD_CONST          0
                             00000025     3C - STORE_SUBSCR        
                             00000026     74 - LOAD_GLOBAL         'chr'
                             00000029     7C - LOAD_FAST           'val'
                             0000002C     64 - LOAD_CONST          65280
                             0000002F     40 - BINARY_AND          
                             00000030     64 - LOAD_CONST          8
                             00000033     3F - BINARY_RSHIFT       
                             00000034     83 - CALL_FUNCTION       r0001
                             00000037     7C - LOAD_FAST           't'
                             0000003A     64 - LOAD_CONST          1
                             0000003D     3C - STORE_SUBSCR        
                             0000003E     74 - LOAD_GLOBAL         'chr'
                             00000041     7C - LOAD_FAST           'val'
                             00000044     64 - LOAD_CONST          16711680
                             00000047     40 - BINARY_AND          
                             00000048     64 - LOAD_CONST          16
                             0000004B     3F - BINARY_RSHIFT       
                             0000004C     83 - CALL_FUNCTION       r0001
                             0000004F     7C - LOAD_FAST           't'
                             00000052     64 - LOAD_CONST          2
                             00000055     3C - STORE_SUBSCR        
                             00000056     74 - LOAD_GLOBAL         'chr'
                             00000059     7C - LOAD_FAST           'val'
                             0000005C     74 - LOAD_GLOBAL         'long'
                             0000005F     64 - LOAD_CONST          -16777216
                             00000062     83 - CALL_FUNCTION       r0001
                             00000065     40 - BINARY_AND          
                             00000066     64 - LOAD_CONST          24
                             00000069     3F - BINARY_RSHIFT       
                             0000006A     83 - CALL_FUNCTION       r0001
                             0000006D     7C - LOAD_FAST           't'
                             00000070     64 - LOAD_CONST          3
                             00000073     3C - STORE_SUBSCR        
                             00000074     7C - LOAD_FAST           't'
                             00000077     53 - RETURN_VALUE        
                             00000078     64 - LOAD_CONST          None
                             0000007B     53 - RETURN_VALUE        
                         consts:
00000525                     TUPLE: (
0000052A                         None (4E),
0000052B                         INT: 0 (00 00 00 00),
00000530                         INT: 255 (FF 00 00 00),
00000535                         INT: 65280 (00 FF 00 00),
0000053A                         INT: 8 (08 00 00 00),
0000053F                         INT: 1 (01 00 00 00),
00000544                         INT: 16711680 (00 00 FF 00),
00000549                         INT: 16 (10 00 00 00),
0000054E                         INT: 2 (02 00 00 00),
00000553                         INT: -16777216 (00 00 00 FF),
00000558                         INT: 24 (18 00 00 00),
0000055D                         INT: 3 (03 00 00 00)
                             )
                         names:
00000562                     TUPLE: (
00000567                         STR: 't' (01 00 00 00 74),
0000056D                         STR: 'chr' (03 00 00 00 63 68 72),
00000575                         STR: 'val' (03 00 00 00 76 61 6C),
0000057D                         STR: 'long' (04 00 00 00 6C 6F 6E 67)
                             )
                         varnames:
00000586                     TUPLE: (
0000058B                         STR: 'val' (03 00 00 00 76 61 6C),
00000593                         STR: 't' (01 00 00 00 74)
                             )
                         freevars:
00000599                     TUPLE: ()
                         cellvars:
0000059E                     TUPLE: ()
                         filename:
000005A3                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\crafting_server.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 72 61 66 74 69 6E 67 5F 73 65 72 76 65 72 2E 70 79)
                         name:
000005EF                     STR: 'toFourCC' (08 00 00 00 74 6F 46 6F 75 72 43 43)
                         firslineno:
000005FC                     LONG: 47L (2F 00 00 00)
                         lnotab:
00000600                     STR: '\x00\x01\x12\x01\x14\x01\x18\x01\x18\x01\x1e\x01' (0C 00 00 00 00 01 12 01 14 01 18 01 18 01 1E 01),
00000611             CODE:
                         argcount:
00000612                     LONG: 1L (01 00 00 00)
                         nlocals:
00000616                     LONG: 1L (01 00 00 00)
                         stacksize:
0000061A                     LONG: 1L (01 00 00 00)
                         flags:
0000061E                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000622                     STR: 'd\x01\x00Sd\x00\x00S' (08 00 00 00 64 01 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          0
                             00000003     53 - RETURN_VALUE        
                             00000004     64 - LOAD_CONST          None
                             00000007     53 - RETURN_VALUE        
                         consts:
0000062F                     TUPLE: (
00000634                         None (4E),
00000635                         INT: 0 (00 00 00 00)
                             )
                         names:
0000063A                     TUPLE: ()
                         varnames:
0000063F                     TUPLE: (
00000644                         STR: 'object' (06 00 00 00 6F 62 6A 65 63 74)
                             )
                         freevars:
0000064F                     TUPLE: ()
                         cellvars:
00000654                     TUPLE: ()
                         filename:
00000659                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\crafting_server.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 72 61 66 74 69 6E 67 5F 73 65 72 76 65 72 2E 70 79)
                         name:
000006A5                     STR: 'DecompileInnerStrengthCost' (1A 00 00 00 44 65 63 6F 6D 70 69 6C 65 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 43 6F 73 74)
                         firslineno:
000006C4                     LONG: 58L (3A 00 00 00)
                         lnotab:
000006C8                     STR: '\x00\x01' (02 00 00 00 00 01),
000006CF             CODE:
                         argcount:
000006D0                     LONG: 1L (01 00 00 00)
                         nlocals:
000006D4                     LONG: 5L (05 00 00 00)
                         stacksize:
000006D8                     LONG: 4L (04 00 00 00)
                         flags:
000006DC                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000006E0                     STR: '|\x00\x00i\x01\x00}\x02\x00|\x00\x00i\x02\x00}\x03\x00d\x01\x00d\x02\x00d\x03\x00d\x04\x00g\x04\x00}\x01\x00|\x01\x00|\x03\x00\x19}\x01\x00|\x01\x00d\x02\x00j\x00\x00o\x0e\x00\x01d\x05\x00|\x02\x00\x18}\x02\x00n\x01\x00\x01|\x01\x00|\x02\x00d\x05\x00\x15|\x01\x00\x14\x17}\x04\x00t\x05\x00|\x00\x00i\x06\x00\x83\x01\x00o\n\x00\x01d\x02\x00}\x04\x00n\x01\x00\x01|\x04\x00Sd\x00\x00S' (7D 00 00 00 7C 00 00 69 01 00 7D 02 00 7C 00 00 69 02 00 7D 03 00 64 01 00 64 02 00 64 03 00 64 04 00 67 04 00 7D 01 00 7C 01 00 7C 03 00 19 7D 01 00 7C 01 00 64 02 00 6A 00 00 6F 0E 00 01 64 05 00 7C 02 00 18 7D 02 00 6E 01 00 01 7C 01 00 7C 02 00 64 05 00 15 7C 01 00 14 17 7D 04 00 74 05 00 7C 00 00 69 06 00 83 01 00 6F 0A 00 01 64 02 00 7D 04 00 6E 01 00 01 7C 04 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'object'
                             00000003     69 - LOAD_ATTR           'stability'
                             00000006     7D - STORE_FAST          'stability'
                             00000009     7C - LOAD_FAST           'object'
                             0000000C     69 - LOAD_ATTR           'purity'
                             0000000F     7D - STORE_FAST          'purity'
                             00000012     64 - LOAD_CONST          -10
                             00000015     64 - LOAD_CONST          0
                             00000018     64 - LOAD_CONST          10
                             0000001B     64 - LOAD_CONST          20
                             0000001E     67 - BUILD_LIST          r0004
                             00000021     7D - STORE_FAST          'pv'
                             00000024     7C - LOAD_FAST           'pv'
                             00000027     7C - LOAD_FAST           'purity'
                             0000002A     19 - BINARY_SUBSCR       
                             0000002B     7D - STORE_FAST          'pv'
                             0000002E     7C - LOAD_FAST           'pv'
                             00000031     64 - LOAD_CONST          0
                             00000034     6A - COMPARE_OP          "<"
                             00000037     6F - JUMP_IF_FALSE       -> 00000048
                             0000003A     01 - POP_TOP             
                             0000003B     64 - LOAD_CONST          7.0
                             0000003E     7C - LOAD_FAST           'stability'
                             00000041     18 - BINARY_SUBTRACT     
                             00000042     7D - STORE_FAST          'stability'
                             00000045     6E - JUMP_FORWARD        -> 00000049
                             00000048     01 - POP_TOP             
                             00000049     7C - LOAD_FAST           'pv'
                             0000004C     7C - LOAD_FAST           'stability'
                             0000004F     64 - LOAD_CONST          7.0
                             00000052     15 - BINARY_DIVIDE       
                             00000053     7C - LOAD_FAST           'pv'
                             00000056     14 - BINARY_MULTIPLY     
                             00000057     17 - BINARY_ADD          
                             00000058     7D - STORE_FAST          'contrib'
                             0000005B     74 - LOAD_GLOBAL         'isPill'
                             0000005E     7C - LOAD_FAST           'object'
                             00000061     69 - LOAD_ATTR           'GOCategoryID'
                             00000064     83 - CALL_FUNCTION       r0001
                             00000067     6F - JUMP_IF_FALSE       -> 00000074
                             0000006A     01 - POP_TOP             
                             0000006B     64 - LOAD_CONST          0
                             0000006E     7D - STORE_FAST          'contrib'
                             00000071     6E - JUMP_FORWARD        -> 00000075
                             00000074     01 - POP_TOP             
                             00000075     7C - LOAD_FAST           'contrib'
                             00000078     53 - RETURN_VALUE        
                             00000079     64 - LOAD_CONST          None
                             0000007C     53 - RETURN_VALUE        
                         consts:
00000762                     TUPLE: (
00000767                         None (4E),
00000768                         INT: -10 (F6 FF FF FF),
0000076D                         INT: 0 (00 00 00 00),
00000772                         INT: 10 (0A 00 00 00),
00000777                         INT: 20 (14 00 00 00),
0000077C                         FLOAT: 7.0 (03 37 2E 30)
                             )
                         names:
00000781                     TUPLE: (
00000786                         STR: 'object' (06 00 00 00 6F 62 6A 65 63 74),
00000791                         STR: 'stability' (09 00 00 00 73 74 61 62 69 6C 69 74 79),
0000079F                         STR: 'purity' (06 00 00 00 70 75 72 69 74 79),
000007AA                         STR: 'pv' (02 00 00 00 70 76),
000007B1                         STR: 'contrib' (07 00 00 00 63 6F 6E 74 72 69 62),
000007BD                         STR: 'isPill' (06 00 00 00 69 73 50 69 6C 6C),
000007C8                         STR: 'GOCategoryID' (0C 00 00 00 47 4F 43 61 74 65 67 6F 72 79 49 44)
                             )
                         varnames:
000007D9                     TUPLE: (
000007DE                         STR: 'object' (06 00 00 00 6F 62 6A 65 63 74),
000007E9                         STR: 'pv' (02 00 00 00 70 76),
000007F0                         STR: 'stability' (09 00 00 00 73 74 61 62 69 6C 69 74 79),
000007FE                         STR: 'purity' (06 00 00 00 70 75 72 69 74 79),
00000809                         STR: 'contrib' (07 00 00 00 63 6F 6E 74 72 69 62)
                             )
                         freevars:
00000815                     TUPLE: ()
                         cellvars:
0000081A                     TUPLE: ()
                         filename:
0000081F                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\crafting_server.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 72 61 66 74 69 6E 67 5F 73 65 72 76 65 72 2E 70 79)
                         name:
0000086B                     STR: 'DecompStabPurContrib' (14 00 00 00 44 65 63 6F 6D 70 53 74 61 62 50 75 72 43 6F 6E 74 72 69 62)
                         firslineno:
00000884                     LONG: 64L (40 00 00 00)
                         lnotab:
00000888                     STR: '\x00\x01\t\x01\t\x02\x12\x01\n\x02\r\x00\x0e\x02\x12\x02\x10\x01\n\x04' (14 00 00 00 00 01 09 01 09 02 12 01 0A 02 0D 00 0E 02 12 02 10 01 0A 04),
000008A1             CODE:
                         argcount:
000008A2                     LONG: 2L (02 00 00 00)
                         nlocals:
000008A6                     LONG: 8L (08 00 00 00)
                         stacksize:
000008AA                     LONG: 7L (07 00 00 00)
                         flags:
000008AE                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000008B2                     STR: 'd\x01\x00}\x02\x00t\x01\x00\x83\x00\x00}\x07\x00|\x00\x00i\x04\x00t\x05\x00\x19}\x05\x00d\x02\x00}\x04\x00|\x00\x00i\x08\x00i\t\x00|\x05\x00d\x03\x00\x14\x83\x01\x00}\x03\x00|\x02\x00t\x0b\x00i\x0c\x00|\x01\x00i\x0e\x00\x83\x01\x00\x17}\x02\x00|\x01\x00i\x0f\x00t\x10\x00j\t\x00o\r\x00\x01|\x01\x00i\x0f\x00}\x04\x00n\x0b\x00\x01|\x02\x00d\x04\x00\x17}\x02\x00|\x04\x00d\x02\x00j\x02\x00o\x15\x00\x01t\x11\x00|\x00\x00|\x02\x00\x83\x02\x00\x01d\x02\x00Sn\x01\x00\x01t\x12\x00|\x01\x00\x83\x01\x00}\x06\x00|\x05\x00|\x06\x00\x14d\x03\x00\x15}\x06\x00|\x05\x00|\x03\x00d\x02\x00\x19\x17}\x05\x00|\x02\x00d\x05\x00d\x06\x00|\x05\x00\x14d\x06\x00|\x06\x00\x14|\x07\x00d\x06\x00|\x04\x00\x14d\x07\x00\x17f\x04\x00\x16\x17}\x02\x00t\x11\x00|\x00\x00|\x02\x00\x83\x02\x00\x01|\x05\x00d\x02\x00j\x04\x00o1\x00\x01d\x06\x00|\x05\x00|\x06\x00\x17\x14|\x07\x00\x17d\x06\x00|\x04\x00\x14d\x07\x00\x17\x18d\x02\x00j\x04\x00o\x08\x00\x01d\x08\x00Sq4\x01\x01n\x01\x00\x01d\x02\x00Sd\x00\x00S' (3C 01 00 00 64 01 00 7D 02 00 74 01 00 83 00 00 7D 07 00 7C 00 00 69 04 00 74 05 00 19 7D 05 00 64 02 00 7D 04 00 7C 00 00 69 08 00 69 09 00 7C 05 00 64 03 00 14 83 01 00 7D 03 00 7C 02 00 74 0B 00 69 0C 00 7C 01 00 69 0E 00 83 01 00 17 7D 02 00 7C 01 00 69 0F 00 74 10 00 6A 09 00 6F 0D 00 01 7C 01 00 69 0F 00 7D 04 00 6E 0B 00 01 7C 02 00 64 04 00 17 7D 02 00 7C 04 00 64 02 00 6A 02 00 6F 15 00 01 74 11 00 7C 00 00 7C 02 00 83 02 00 01 64 02 00 53 6E 01 00 01 74 12 00 7C 01 00 83 01 00 7D 06 00 7C 05 00 7C 06 00 14 64 03 00 15 7D 06 00 7C 05 00 7C 03 00 64 02 00 19 17 7D 05 00 7C 02 00 64 05 00 64 06 00 7C 05 00 14 64 06 00 7C 06 00 14 7C 07 00 64 06 00 7C 04 00 14 64 07 00 17 66 04 00 16 17 7D 02 00 74 11 00 7C 00 00 7C 02 00 83 02 00 01 7C 05 00 64 02 00 6A 04 00 6F 31 00 01 64 06 00 7C 05 00 7C 06 00 17 14 7C 07 00 17 64 06 00 7C 04 00 14 64 07 00 17 18 64 02 00 6A 04 00 6F 08 00 01 64 08 00 53 71 34 01 01 6E 01 00 01 64 02 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          'Decompile '
                             00000003     7D - STORE_FAST          '_str'
                             00000006     74 - LOAD_GLOBAL         'gD100'
                             00000009     83 - CALL_FUNCTION       r0000
                             0000000C     7D - STORE_FAST          'roll'
                             0000000F     7C - LOAD_FAST           'subject'
                             00000012     69 - LOAD_ATTR           'abilities'
                             00000015     74 - LOAD_GLOBAL         'DecompileSkillAbility'
                             00000018     19 - BINARY_SUBSCR       
                             00000019     7D - STORE_FAST          'abil_level'
                             0000001C     64 - LOAD_CONST          0
                             0000001F     7D - STORE_FAST          'complexity'
                             00000022     7C - LOAD_FAST           'subject'
                             00000025     69 - LOAD_ATTR           'AbilityInv'
                             00000028     69 - LOAD_ATTR           'getSignalBoostBonus'
                             0000002B     7C - LOAD_FAST           'abil_level'
                             0000002E     64 - LOAD_CONST          100.0
                             00000031     14 - BINARY_MULTIPLY     
                             00000032     83 - CALL_FUNCTION       r0001
                             00000035     7D - STORE_FAST          'signalboost'
                             00000038     7C - LOAD_FAST           '_str'
                             0000003B     74 - LOAD_GLOBAL         'discovery'
                             0000003E     69 - LOAD_ATTR           'getGameObjectName'
                             00000041     7C - LOAD_FAST           'object'
                             00000044     69 - LOAD_ATTR           'type'
                             00000047     83 - CALL_FUNCTION       r0001
                             0000004A     17 - BINARY_ADD          
                             0000004B     7D - STORE_FAST          '_str'
                             0000004E     7C - LOAD_FAST           'object'
                             00000051     69 - LOAD_ATTR           'Complexity'
                             00000054     74 - LOAD_GLOBAL         'None'
                             00000057     6A - COMPARE_OP          "is not"
                             0000005A     6F - JUMP_IF_FALSE       -> 0000006A
                             0000005D     01 - POP_TOP             
                             0000005E     7C - LOAD_FAST           'object'
                             00000061     69 - LOAD_ATTR           'Complexity'
                             00000064     7D - STORE_FAST          'complexity'
                             00000067     6E - JUMP_FORWARD        -> 00000075
                             0000006A     01 - POP_TOP             
                             0000006B     7C - LOAD_FAST           '_str'
                             0000006E     64 - LOAD_CONST          'object has no complexity'
                             00000071     17 - BINARY_ADD          
                             00000072     7D - STORE_FAST          '_str'
                             00000075     7C - LOAD_FAST           'complexity'
                             00000078     64 - LOAD_CONST          0
                             0000007B     6A - COMPARE_OP          "=="
                             0000007E     6F - JUMP_IF_FALSE       -> 00000096
                             00000081     01 - POP_TOP             
                             00000082     74 - LOAD_GLOBAL         'craftingFeedback'
                             00000085     7C - LOAD_FAST           'subject'
                             00000088     7C - LOAD_FAST           '_str'
                             0000008B     83 - CALL_FUNCTION       r0002
                             0000008E     01 - POP_TOP             
                             0000008F     64 - LOAD_CONST          0
                             00000092     53 - RETURN_VALUE        
                             00000093     6E - JUMP_FORWARD        -> 00000097
                             00000096     01 - POP_TOP             
                             00000097     74 - LOAD_GLOBAL         'DecompStabPurContrib'
                             0000009A     7C - LOAD_FAST           'object'
                             0000009D     83 - CALL_FUNCTION       r0001
                             000000A0     7D - STORE_FAST          'contrib'
                             000000A3     7C - LOAD_FAST           'abil_level'
                             000000A6     7C - LOAD_FAST           'contrib'
                             000000A9     14 - BINARY_MULTIPLY     
                             000000AA     64 - LOAD_CONST          100.0
                             000000AD     15 - BINARY_DIVIDE       
                             000000AE     7D - STORE_FAST          'contrib'
                             000000B1     7C - LOAD_FAST           'abil_level'
                             000000B4     7C - LOAD_FAST           'signalboost'
                             000000B7     64 - LOAD_CONST          0
                             000000BA     19 - BINARY_SUBSCR       
                             000000BB     17 - BINARY_ADD          
                             000000BC     7D - STORE_FAST          'abil_level'
                             000000BF     7C - LOAD_FAST           '_str'
                             000000C2     64 - LOAD_CONST          'res : a%d + c%d + r%d > %d'
                             000000C5     64 - LOAD_CONST          4
                             000000C8     7C - LOAD_FAST           'abil_level'
                             000000CB     14 - BINARY_MULTIPLY     
                             000000CC     64 - LOAD_CONST          4
                             000000CF     7C - LOAD_FAST           'contrib'
                             000000D2     14 - BINARY_MULTIPLY     
                             000000D3     7C - LOAD_FAST           'roll'
                             000000D6     64 - LOAD_CONST          4
                             000000D9     7C - LOAD_FAST           'complexity'
                             000000DC     14 - BINARY_MULTIPLY     
                             000000DD     64 - LOAD_CONST          50
                             000000E0     17 - BINARY_ADD          
                             000000E1     66 - BUILD_TUPLE         r0004
                             000000E4     16 - BINARY_MODULO       
                             000000E5     17 - BINARY_ADD          
                             000000E6     7D - STORE_FAST          '_str'
                             000000E9     74 - LOAD_GLOBAL         'craftingFeedback'
                             000000EC     7C - LOAD_FAST           'subject'
                             000000EF     7C - LOAD_FAST           '_str'
                             000000F2     83 - CALL_FUNCTION       r0002
                             000000F5     01 - POP_TOP             
                             000000F6     7C - LOAD_FAST           'abil_level'
                             000000F9     64 - LOAD_CONST          0
                             000000FC     6A - COMPARE_OP          ">"
                             000000FF     6F - JUMP_IF_FALSE       -> 00000133
                             00000102     01 - POP_TOP             
                             00000103     64 - LOAD_CONST          4
                             00000106     7C - LOAD_FAST           'abil_level'
                             00000109     7C - LOAD_FAST           'contrib'
                             0000010C     17 - BINARY_ADD          
                             0000010D     14 - BINARY_MULTIPLY     
                             0000010E     7C - LOAD_FAST           'roll'
                             00000111     17 - BINARY_ADD          
                             00000112     64 - LOAD_CONST          4
                             00000115     7C - LOAD_FAST           'complexity'
                             00000118     14 - BINARY_MULTIPLY     
                             00000119     64 - LOAD_CONST          50
                             0000011C     17 - BINARY_ADD          
                             0000011D     18 - BINARY_SUBTRACT     
                             0000011E     64 - LOAD_CONST          0
                             00000121     6A - COMPARE_OP          ">"
                             00000124     6F - JUMP_IF_FALSE       -> 0000012F
                             00000127     01 - POP_TOP             
                             00000128     64 - LOAD_CONST          1
                             0000012B     53 - RETURN_VALUE        
                             0000012C     71 - JUMP_ABSOLUTE       -> 00000134
                             0000012F     01 - POP_TOP             
                             00000130     6E - JUMP_FORWARD        -> 00000134
                             00000133     01 - POP_TOP             
                             00000134     64 - LOAD_CONST          0
                             00000137     53 - RETURN_VALUE        
                             00000138     64 - LOAD_CONST          None
                             0000013B     53 - RETURN_VALUE        
                         consts:
000009F3                     TUPLE: (
000009F8                         None (4E),
000009F9                         STR: 'Decompile ' (0A 00 00 00 44 65 63 6F 6D 70 69 6C 65 20),
00000A08                         INT: 0 (00 00 00 00),
00000A0D                         FLOAT: 100.0 (05 31 30 30 2E 30),
00000A14                         STR: 'object has no complexity' (18 00 00 00 6F 62 6A 65 63 74 20 68 61 73 20 6E 6F 20 63 6F 6D 70 6C 65 78 69 74 79),
00000A31                         STR: 'res : a%d + c%d + r%d > %d' (1A 00 00 00 72 65 73 20 3A 20 61 25 64 20 2B 20 63 25 64 20 2B 20 72 25 64 20 3E 20 25 64),
00000A50                         INT: 4 (04 00 00 00),
00000A55                         INT: 50 (32 00 00 00),
00000A5A                         INT: 1 (01 00 00 00)
                             )
                         names:
00000A5F                     TUPLE: (
00000A64                         STR: '_str' (04 00 00 00 5F 73 74 72),
00000A6D                         STR: 'gD100' (05 00 00 00 67 44 31 30 30),
00000A77                         STR: 'roll' (04 00 00 00 72 6F 6C 6C),
00000A80                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000A8C                         STR: 'abilities' (09 00 00 00 61 62 69 6C 69 74 69 65 73),
00000A9A                         STR: 'DecompileSkillAbility' (15 00 00 00 44 65 63 6F 6D 70 69 6C 65 53 6B 69 6C 6C 41 62 69 6C 69 74 79),
00000AB4                         STR: 'abil_level' (0A 00 00 00 61 62 69 6C 5F 6C 65 76 65 6C),
00000AC3                         STR: 'complexity' (0A 00 00 00 63 6F 6D 70 6C 65 78 69 74 79),
00000AD2                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
00000AE1                         STR: 'getSignalBoostBonus' (13 00 00 00 67 65 74 53 69 67 6E 61 6C 42 6F 6F 73 74 42 6F 6E 75 73),
00000AF9                         STR: 'signalboost' (0B 00 00 00 73 69 67 6E 61 6C 62 6F 6F 73 74),
00000B09                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
00000B17                         STR: 'getGameObjectName' (11 00 00 00 67 65 74 47 61 6D 65 4F 62 6A 65 63 74 4E 61 6D 65),
00000B2D                         STR: 'object' (06 00 00 00 6F 62 6A 65 63 74),
00000B38                         STR: 'type' (04 00 00 00 74 79 70 65),
00000B41                         STR: 'Complexity' (0A 00 00 00 43 6F 6D 70 6C 65 78 69 74 79),
00000B50                         STR: 'None' (04 00 00 00 4E 6F 6E 65),
00000B59                         STR: 'craftingFeedback' (10 00 00 00 63 72 61 66 74 69 6E 67 46 65 65 64 62 61 63 6B),
00000B6E                         STR: 'DecompStabPurContrib' (14 00 00 00 44 65 63 6F 6D 70 53 74 61 62 50 75 72 43 6F 6E 74 72 69 62),
00000B87                         STR: 'contrib' (07 00 00 00 63 6F 6E 74 72 69 62)
                             )
                         varnames:
00000B93                     TUPLE: (
00000B98                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000BA4                         STR: 'object' (06 00 00 00 6F 62 6A 65 63 74),
00000BAF                         STR: '_str' (04 00 00 00 5F 73 74 72),
00000BB8                         STR: 'signalboost' (0B 00 00 00 73 69 67 6E 61 6C 62 6F 6F 73 74),
00000BC8                         STR: 'complexity' (0A 00 00 00 63 6F 6D 70 6C 65 78 69 74 79),
00000BD7                         STR: 'abil_level' (0A 00 00 00 61 62 69 6C 5F 6C 65 76 65 6C),
00000BE6                         STR: 'contrib' (07 00 00 00 63 6F 6E 74 72 69 62),
00000BF2                         STR: 'roll' (04 00 00 00 72 6F 6C 6C)
                             )
                         freevars:
00000BFB                     TUPLE: ()
                         cellvars:
00000C00                     TUPLE: ()
                         filename:
00000C05                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\crafting_server.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 72 61 66 74 69 6E 67 5F 73 65 72 76 65 72 2E 70 79)
                         name:
00000C51                     STR: 'DecompileTest' (0D 00 00 00 44 65 63 6F 6D 70 69 6C 65 54 65 73 74)
                         firslineno:
00000C63                     LONG: 85L (55 00 00 00)
                         lnotab:
00000C67                     STR: '\x00\x01\x06\x01\t\x01\r\x02\x06\x02\x16\x02\x16\x02\x10\x01\r\x02\n\x02\r\x02\r\x01\x08\x02\x0c\x01\x0e\x01\x0e\x02*\x01\r\x02\r\x01%\x01\x0c\x02' (2A 00 00 00 00 01 06 01 09 01 0D 02 06 02 16 02 16 02 10 01 0D 02 0A 02 0D 02 0D 01 08 02 0C 01 0E 01 0E 02 2A 01 0D 02 0D 01 25 01 0C 02),
00000C96             CODE:
                         argcount:
00000C97                     LONG: 3L (03 00 00 00)
                         nlocals:
00000C9B                     LONG: 8L (08 00 00 00)
                         stacksize:
00000C9F                     LONG: 6L (06 00 00 00)
                         flags:
00000CA3                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000CA7                     STR: 'd\x01\x00}\x03\x00t\x01\x00\x83\x00\x00}\x07\x00|\x00\x00i\x04\x00t\x05\x00\x19}\x06\x00d\x02\x00}\x05\x00|\x00\x00i\x08\x00i\t\x00t\n\x00|\x06\x00d\x03\x00\x14\x83\x01\x00\x83\x01\x00}\x04\x00|\x06\x00|\x04\x00d\x02\x00\x19\x17}\x06\x00|\x03\x00d\x04\x00t\x0c\x00i\r\x00|\x01\x00i\x0f\x00\x83\x01\x00|\x05\x00f\x02\x00\x16\x17}\x03\x00|\x01\x00i\x10\x00t\x11\x00j\t\x00o\r\x00\x01|\x01\x00i\x10\x00}\x05\x00n\x1c\x00\x01|\x03\x00d\x05\x00\x17}\x03\x00t\x12\x00|\x00\x00|\x03\x00\x83\x02\x00\x01d\x02\x00S|\x03\x00d\x06\x00d\x07\x00|\x06\x00\x14|\x07\x00d\x07\x00|\x05\x00\x14d\x08\x00\x17f\x03\x00\x16\x17}\x03\x00t\x12\x00|\x00\x00|\x03\x00\x83\x02\x00\x01|\x06\x00d\x02\x00j\x04\x00o\n\x00\x01|\x05\x00d\x02\x00j\x04\x00o-\x00\x01d\x07\x00|\x06\x00\x14|\x07\x00\x17d\x07\x00|\x05\x00\x14d\x08\x00\x17\x18d\x02\x00j\x04\x00o\x08\x00\x01d\t\x00Sq\x1b\x01\x01n\x01\x00\x01d\x02\x00Sd\x00\x00S' (23 01 00 00 64 01 00 7D 03 00 74 01 00 83 00 00 7D 07 00 7C 00 00 69 04 00 74 05 00 19 7D 06 00 64 02 00 7D 05 00 7C 00 00 69 08 00 69 09 00 74 0A 00 7C 06 00 64 03 00 14 83 01 00 83 01 00 7D 04 00 7C 06 00 7C 04 00 64 02 00 19 17 7D 06 00 7C 03 00 64 04 00 74 0C 00 69 0D 00 7C 01 00 69 0F 00 83 01 00 7C 05 00 66 02 00 16 17 7D 03 00 7C 01 00 69 10 00 74 11 00 6A 09 00 6F 0D 00 01 7C 01 00 69 10 00 7D 05 00 6E 1C 00 01 7C 03 00 64 05 00 17 7D 03 00 74 12 00 7C 00 00 7C 03 00 83 02 00 01 64 02 00 53 7C 03 00 64 06 00 64 07 00 7C 06 00 14 7C 07 00 64 07 00 7C 05 00 14 64 08 00 17 66 03 00 16 17 7D 03 00 74 12 00 7C 00 00 7C 03 00 83 02 00 01 7C 06 00 64 02 00 6A 04 00 6F 0A 00 01 7C 05 00 64 02 00 6A 04 00 6F 2D 00 01 64 07 00 7C 06 00 14 7C 07 00 17 64 07 00 7C 05 00 14 64 08 00 17 18 64 02 00 6A 04 00 6F 08 00 01 64 09 00 53 71 1B 01 01 6E 01 00 01 64 02 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          'Frag Recovery : '
                             00000003     7D - STORE_FAST          '_str'
                             00000006     74 - LOAD_GLOBAL         'gD100'
                             00000009     83 - CALL_FUNCTION       r0000
                             0000000C     7D - STORE_FAST          'roll'
                             0000000F     7C - LOAD_FAST           'subject'
                             00000012     69 - LOAD_ATTR           'abilities'
                             00000015     74 - LOAD_GLOBAL         'DecompileSkillAbility'
                             00000018     19 - BINARY_SUBSCR       
                             00000019     7D - STORE_FAST          'abil_level'
                             0000001C     64 - LOAD_CONST          0
                             0000001F     7D - STORE_FAST          'complexity'
                             00000022     7C - LOAD_FAST           'subject'
                             00000025     69 - LOAD_ATTR           'AbilityInv'
                             00000028     69 - LOAD_ATTR           'getSignalBoostBonus'
                             0000002B     74 - LOAD_GLOBAL         'float'
                             0000002E     7C - LOAD_FAST           'abil_level'
                             00000031     64 - LOAD_CONST          100
                             00000034     14 - BINARY_MULTIPLY     
                             00000035     83 - CALL_FUNCTION       r0001
                             00000038     83 - CALL_FUNCTION       r0001
                             0000003B     7D - STORE_FAST          'signalboost'
                             0000003E     7C - LOAD_FAST           'abil_level'
                             00000041     7C - LOAD_FAST           'signalboost'
                             00000044     64 - LOAD_CONST          0
                             00000047     19 - BINARY_SUBSCR       
                             00000048     17 - BINARY_ADD          
                             00000049     7D - STORE_FAST          'abil_level'
                             0000004C     7C - LOAD_FAST           '_str'
                             0000004F     64 - LOAD_CONST          'Decomp Recovery : %s C(%d) '
                             00000052     74 - LOAD_GLOBAL         'discovery'
                             00000055     69 - LOAD_ATTR           'getGameObjectName'
                             00000058     7C - LOAD_FAST           'fragment'
                             0000005B     69 - LOAD_ATTR           'type'
                             0000005E     83 - CALL_FUNCTION       r0001
                             00000061     7C - LOAD_FAST           'complexity'
                             00000064     66 - BUILD_TUPLE         r0002
                             00000067     16 - BINARY_MODULO       
                             00000068     17 - BINARY_ADD          
                             00000069     7D - STORE_FAST          '_str'
                             0000006C     7C - LOAD_FAST           'fragment'
                             0000006F     69 - LOAD_ATTR           'Complexity'
                             00000072     74 - LOAD_GLOBAL         'None'
                             00000075     6A - COMPARE_OP          "is not"
                             00000078     6F - JUMP_IF_FALSE       -> 00000088
                             0000007B     01 - POP_TOP             
                             0000007C     7C - LOAD_FAST           'fragment'
                             0000007F     69 - LOAD_ATTR           'Complexity'
                             00000082     7D - STORE_FAST          'complexity'
                             00000085     6E - JUMP_FORWARD        -> 000000A4
                             00000088     01 - POP_TOP             
                             00000089     7C - LOAD_FAST           '_str'
                             0000008C     64 - LOAD_CONST          'Object has no Complexity'
                             0000008F     17 - BINARY_ADD          
                             00000090     7D - STORE_FAST          '_str'
                             00000093     74 - LOAD_GLOBAL         'craftingFeedback'
                             00000096     7C - LOAD_FAST           'subject'
                             00000099     7C - LOAD_FAST           '_str'
                             0000009C     83 - CALL_FUNCTION       r0002
                             0000009F     01 - POP_TOP             
                             000000A0     64 - LOAD_CONST          0
                             000000A3     53 - RETURN_VALUE        
                             000000A4     7C - LOAD_FAST           '_str'
                             000000A7     64 - LOAD_CONST          ' abil %d + %d > %d'
                             000000AA     64 - LOAD_CONST          4
                             000000AD     7C - LOAD_FAST           'abil_level'
                             000000B0     14 - BINARY_MULTIPLY     
                             000000B1     7C - LOAD_FAST           'roll'
                             000000B4     64 - LOAD_CONST          4
                             000000B7     7C - LOAD_FAST           'complexity'
                             000000BA     14 - BINARY_MULTIPLY     
                             000000BB     64 - LOAD_CONST          50
                             000000BE     17 - BINARY_ADD          
                             000000BF     66 - BUILD_TUPLE         r0003
                             000000C2     16 - BINARY_MODULO       
                             000000C3     17 - BINARY_ADD          
                             000000C4     7D - STORE_FAST          '_str'
                             000000C7     74 - LOAD_GLOBAL         'craftingFeedback'
                             000000CA     7C - LOAD_FAST           'subject'
                             000000CD     7C - LOAD_FAST           '_str'
                             000000D0     83 - CALL_FUNCTION       r0002
                             000000D3     01 - POP_TOP             
                             000000D4     7C - LOAD_FAST           'abil_level'
                             000000D7     64 - LOAD_CONST          0
                             000000DA     6A - COMPARE_OP          ">"
                             000000DD     6F - JUMP_IF_FALSE       -> 000000EA
                             000000E0     01 - POP_TOP             
                             000000E1     7C - LOAD_FAST           'complexity'
                             000000E4     64 - LOAD_CONST          0
                             000000E7     6A - COMPARE_OP          ">"
                             000000EA     6F - JUMP_IF_FALSE       -> 0000011A
                             000000ED     01 - POP_TOP             
                             000000EE     64 - LOAD_CONST          4
                             000000F1     7C - LOAD_FAST           'abil_level'
                             000000F4     14 - BINARY_MULTIPLY     
                             000000F5     7C - LOAD_FAST           'roll'
                             000000F8     17 - BINARY_ADD          
                             000000F9     64 - LOAD_CONST          4
                             000000FC     7C - LOAD_FAST           'complexity'
                             000000FF     14 - BINARY_MULTIPLY     
                             00000100     64 - LOAD_CONST          50
                             00000103     17 - BINARY_ADD          
                             00000104     18 - BINARY_SUBTRACT     
                             00000105     64 - LOAD_CONST          0
                             00000108     6A - COMPARE_OP          ">"
                             0000010B     6F - JUMP_IF_FALSE       -> 00000116
                             0000010E     01 - POP_TOP             
                             0000010F     64 - LOAD_CONST          1
                             00000112     53 - RETURN_VALUE        
                             00000113     71 - JUMP_ABSOLUTE       -> 0000011B
                             00000116     01 - POP_TOP             
                             00000117     6E - JUMP_FORWARD        -> 0000011B
                             0000011A     01 - POP_TOP             
                             0000011B     64 - LOAD_CONST          0
                             0000011E     53 - RETURN_VALUE        
                             0000011F     64 - LOAD_CONST          None
                             00000122     53 - RETURN_VALUE        
                         consts:
00000DCF                     TUPLE: (
00000DD4                         None (4E),
00000DD5                         STR: 'Frag Recovery : ' (10 00 00 00 46 72 61 67 20 52 65 63 6F 76 65 72 79 20 3A 20),
00000DEA                         INT: 0 (00 00 00 00),
00000DEF                         INT: 100 (64 00 00 00),
00000DF4                         STR: 'Decomp Recovery : %s C(%d) ' (1B 00 00 00 44 65 63 6F 6D 70 20 52 65 63 6F 76 65 72 79 20 3A 20 25 73 20 43 28 25 64 29 20),
00000E14                         STR: 'Object has no Complexity' (18 00 00 00 4F 62 6A 65 63 74 20 68 61 73 20 6E 6F 20 43 6F 6D 70 6C 65 78 69 74 79),
00000E31                         STR: ' abil %d + %d > %d' (12 00 00 00 20 61 62 69 6C 20 25 64 20 2B 20 25 64 20 3E 20 25 64),
00000E48                         INT: 4 (04 00 00 00),
00000E4D                         INT: 50 (32 00 00 00),
00000E52                         INT: 1 (01 00 00 00)
                             )
                         names:
00000E57                     TUPLE: (
00000E5C                         STR: '_str' (04 00 00 00 5F 73 74 72),
00000E65                         STR: 'gD100' (05 00 00 00 67 44 31 30 30),
00000E6F                         STR: 'roll' (04 00 00 00 72 6F 6C 6C),
00000E78                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000E84                         STR: 'abilities' (09 00 00 00 61 62 69 6C 69 74 69 65 73),
00000E92                         STR: 'DecompileSkillAbility' (15 00 00 00 44 65 63 6F 6D 70 69 6C 65 53 6B 69 6C 6C 41 62 69 6C 69 74 79),
00000EAC                         STR: 'abil_level' (0A 00 00 00 61 62 69 6C 5F 6C 65 76 65 6C),
00000EBB                         STR: 'complexity' (0A 00 00 00 63 6F 6D 70 6C 65 78 69 74 79),
00000ECA                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
00000ED9                         STR: 'getSignalBoostBonus' (13 00 00 00 67 65 74 53 69 67 6E 61 6C 42 6F 6F 73 74 42 6F 6E 75 73),
00000EF1                         STR: 'float' (05 00 00 00 66 6C 6F 61 74),
00000EFB                         STR: 'signalboost' (0B 00 00 00 73 69 67 6E 61 6C 62 6F 6F 73 74),
00000F0B                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
00000F19                         STR: 'getGameObjectName' (11 00 00 00 67 65 74 47 61 6D 65 4F 62 6A 65 63 74 4E 61 6D 65),
00000F2F                         STR: 'fragment' (08 00 00 00 66 72 61 67 6D 65 6E 74),
00000F3C                         STR: 'type' (04 00 00 00 74 79 70 65),
00000F45                         STR: 'Complexity' (0A 00 00 00 43 6F 6D 70 6C 65 78 69 74 79),
00000F54                         STR: 'None' (04 00 00 00 4E 6F 6E 65),
00000F5D                         STR: 'craftingFeedback' (10 00 00 00 63 72 61 66 74 69 6E 67 46 65 65 64 62 61 63 6B)
                             )
                         varnames:
00000F72                     TUPLE: (
00000F77                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000F83                         STR: 'fragment' (08 00 00 00 66 72 61 67 6D 65 6E 74),
00000F90                         STR: 'stability' (09 00 00 00 73 74 61 62 69 6C 69 74 79),
00000F9E                         STR: '_str' (04 00 00 00 5F 73 74 72),
00000FA7                         STR: 'signalboost' (0B 00 00 00 73 69 67 6E 61 6C 62 6F 6F 73 74),
00000FB7                         STR: 'complexity' (0A 00 00 00 63 6F 6D 70 6C 65 78 69 74 79),
00000FC6                         STR: 'abil_level' (0A 00 00 00 61 62 69 6C 5F 6C 65 76 65 6C),
00000FD5                         STR: 'roll' (04 00 00 00 72 6F 6C 6C)
                             )
                         freevars:
00000FDE                     TUPLE: ()
                         cellvars:
00000FE3                     TUPLE: ()
                         filename:
00000FE8                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\crafting_server.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 72 61 66 74 69 6E 67 5F 73 65 72 76 65 72 2E 70 79)
                         name:
00001034                     STR: 'DecompileFragmentRecoveryTest' (1D 00 00 00 44 65 63 6F 6D 70 69 6C 65 46 72 61 67 6D 65 6E 74 52 65 63 6F 76 65 72 79 54 65 73 74)
                         firslineno:
00001056                     LONG: 124L (7C 00 00 00)
                         lnotab:
0000105A                     STR: '\x00\x01\x06\x01\t\x01\r\x02\x06\x02\x1c\x02\x0e\x02 \x01\x10\x01\r\x02\n\x01\r\x01\x04\x04#\x01\r\x02\x1a\x01!\x01\x0c\x02' (24 00 00 00 00 01 06 01 09 01 0D 02 06 02 1C 02 0E 02 20 01 10 01 0D 02 0A 01 0D 01 04 04 23 01 0D 02 1A 01 21 01 0C 02),
00001083             CODE:
                         argcount:
00001084                     LONG: 1L (01 00 00 00)
                         nlocals:
00001088                     LONG: 1L (01 00 00 00)
                         stacksize:
0000108C                     LONG: 2L (02 00 00 00)
                         flags:
00001090                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001094                     STR: '|\x00\x00i\x01\x00t\x02\x00j\t\x00o\x0f\x00\x01|\x00\x00i\x01\x00t\x03\x00\x14Sn\x01\x00\x01d\x01\x00t\x03\x00\x14Sd\x00\x00S' (2B 00 00 00 7C 00 00 69 01 00 74 02 00 6A 09 00 6F 0F 00 01 7C 00 00 69 01 00 74 03 00 14 53 6E 01 00 01 64 01 00 74 03 00 14 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'object'
                             00000003     69 - LOAD_ATTR           'VendorPrice'
                             00000006     74 - LOAD_GLOBAL         'None'
                             00000009     6A - COMPARE_OP          "is not"
                             0000000C     6F - JUMP_IF_FALSE       -> 0000001E
                             0000000F     01 - POP_TOP             
                             00000010     7C - LOAD_FAST           'object'
                             00000013     69 - LOAD_ATTR           'VendorPrice'
                             00000016     74 - LOAD_GLOBAL         'COMPILE_DISCOUNT'
                             00000019     14 - BINARY_MULTIPLY     
                             0000001A     53 - RETURN_VALUE        
                             0000001B     6E - JUMP_FORWARD        -> 0000001F
                             0000001E     01 - POP_TOP             
                             0000001F     64 - LOAD_CONST          1000
                             00000022     74 - LOAD_GLOBAL         'COMPILE_DISCOUNT'
                             00000025     14 - BINARY_MULTIPLY     
                             00000026     53 - RETURN_VALUE        
                             00000027     64 - LOAD_CONST          None
                             0000002A     53 - RETURN_VALUE        
                         consts:
000010C4                     TUPLE: (
000010C9                         None (4E),
000010CA                         INT: 1000 (E8 03 00 00)
                             )
                         names:
000010CF                     TUPLE: (
000010D4                         STR: 'object' (06 00 00 00 6F 62 6A 65 63 74),
000010DF                         STR: 'VendorPrice' (0B 00 00 00 56 65 6E 64 6F 72 50 72 69 63 65),
000010EF                         STR: 'None' (04 00 00 00 4E 6F 6E 65),
000010F8                         STR: 'COMPILE_DISCOUNT' (10 00 00 00 43 4F 4D 50 49 4C 45 5F 44 49 53 43 4F 55 4E 54)
                             )
                         varnames:
0000110D                     TUPLE: (
00001112                         STR: 'object' (06 00 00 00 6F 62 6A 65 63 74)
                             )
                         freevars:
0000111D                     TUPLE: ()
                         cellvars:
00001122                     TUPLE: ()
                         filename:
00001127                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\crafting_server.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 72 61 66 74 69 6E 67 5F 73 65 72 76 65 72 2E 70 79)
                         name:
00001173                     STR: 'CompileInfoCost' (0F 00 00 00 43 6F 6D 70 69 6C 65 49 6E 66 6F 43 6F 73 74)
                         firslineno:
00001187                     LONG: 158L (9E 00 00 00)
                         lnotab:
0000118B                     STR: '\x00\x01\x10\x01\x0f\x02' (06 00 00 00 00 01 10 01 0F 02),
00001196             CODE:
                         argcount:
00001197                     LONG: 2L (02 00 00 00)
                         nlocals:
0000119B                     LONG: 4L (04 00 00 00)
                         stacksize:
0000119F                     LONG: 2L (02 00 00 00)
                         flags:
000011A3                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000011A7                     STR: 'd\x01\x00}\x03\x00|\x01\x00o\xfe\x00\x01t\x02\x00|\x01\x00\x83\x01\x00}\x02\x00|\x02\x00d\x01\x00\x19d\x02\x00j\x02\x00o\x0e\x00\x01|\x02\x00d\x03\x00\x19d\x04\x00j\x02\x00o\x11\x00\x01|\x00\x00i\x05\x00t\x06\x00\x19}\x03\x00n\x01\x00\x01|\x02\x00d\x01\x00\x19d\x05\x00j\x02\x00o\x11\x00\x01|\x00\x00i\x05\x00t\x07\x00\x19}\x03\x00n\x01\x00\x01|\x02\x00d\x01\x00\x19d\x02\x00j\x02\x00o\x0e\x00\x01|\x02\x00d\x03\x00\x19d\x05\x00j\x02\x00o\x11\x00\x01|\x00\x00i\x05\x00t\x08\x00\x19}\x03\x00n\x01\x00\x01|\x02\x00d\x01\x00\x19d\x02\x00j\x02\x00o\x0e\x00\x01|\x02\x00d\x03\x00\x19d\x06\x00j\x02\x00o\x11\x00\x01|\x00\x00i\x05\x00t\t\x00\x19}\x03\x00n\x01\x00\x01|\x02\x00d\x01\x00\x19d\x02\x00j\x02\x00o\x0e\x00\x01|\x02\x00d\x03\x00\x19d\x07\x00j\x02\x00o\x11\x00\x01|\x00\x00i\x05\x00t\n\x00\x19}\x03\x00q\x0b\x01\x01n\x01\x00\x01|\x03\x00Sd\x00\x00S' (13 01 00 00 64 01 00 7D 03 00 7C 01 00 6F FE 00 01 74 02 00 7C 01 00 83 01 00 7D 02 00 7C 02 00 64 01 00 19 64 02 00 6A 02 00 6F 0E 00 01 7C 02 00 64 03 00 19 64 04 00 6A 02 00 6F 11 00 01 7C 00 00 69 05 00 74 06 00 19 7D 03 00 6E 01 00 01 7C 02 00 64 01 00 19 64 05 00 6A 02 00 6F 11 00 01 7C 00 00 69 05 00 74 07 00 19 7D 03 00 6E 01 00 01 7C 02 00 64 01 00 19 64 02 00 6A 02 00 6F 0E 00 01 7C 02 00 64 03 00 19 64 05 00 6A 02 00 6F 11 00 01 7C 00 00 69 05 00 74 08 00 19 7D 03 00 6E 01 00 01 7C 02 00 64 01 00 19 64 02 00 6A 02 00 6F 0E 00 01 7C 02 00 64 03 00 19 64 06 00 6A 02 00 6F 11 00 01 7C 00 00 69 05 00 74 09 00 19 7D 03 00 6E 01 00 01 7C 02 00 64 01 00 19 64 02 00 6A 02 00 6F 0E 00 01 7C 02 00 64 03 00 19 64 07 00 6A 02 00 6F 11 00 01 7C 00 00 69 05 00 74 0A 00 19 7D 03 00 71 0B 01 01 6E 01 00 01 7C 03 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          0
                             00000003     7D - STORE_FAST          'abil_level'
                             00000006     7C - LOAD_FAST           'GOCategoryID'
                             00000009     6F - JUMP_IF_FALSE       -> 0000010A
                             0000000C     01 - POP_TOP             
                             0000000D     74 - LOAD_GLOBAL         'toFourCC'
                             00000010     7C - LOAD_FAST           'GOCategoryID'
                             00000013     83 - CALL_FUNCTION       r0001
                             00000016     7D - STORE_FAST          'cat'
                             00000019     7C - LOAD_FAST           'cat'
                             0000001C     64 - LOAD_CONST          0
                             0000001F     19 - BINARY_SUBSCR       
                             00000020     64 - LOAD_CONST          'I'
                             00000023     6A - COMPARE_OP          "=="
                             00000026     6F - JUMP_IF_FALSE       -> 00000037
                             00000029     01 - POP_TOP             
                             0000002A     7C - LOAD_FAST           'cat'
                             0000002D     64 - LOAD_CONST          1
                             00000030     19 - BINARY_SUBSCR       
                             00000031     64 - LOAD_CONST          'W'
                             00000034     6A - COMPARE_OP          "=="
                             00000037     6F - JUMP_IF_FALSE       -> 0000004B
                             0000003A     01 - POP_TOP             
                             0000003B     7C - LOAD_FAST           'subject'
                             0000003E     69 - LOAD_ATTR           'abilities'
                             00000041     74 - LOAD_GLOBAL         'WeaponCraftingAbility'
                             00000044     19 - BINARY_SUBSCR       
                             00000045     7D - STORE_FAST          'abil_level'
                             00000048     6E - JUMP_FORWARD        -> 0000004C
                             0000004B     01 - POP_TOP             
                             0000004C     7C - LOAD_FAST           'cat'
                             0000004F     64 - LOAD_CONST          0
                             00000052     19 - BINARY_SUBSCR       
                             00000053     64 - LOAD_CONST          'A'
                             00000056     6A - COMPARE_OP          "=="
                             00000059     6F - JUMP_IF_FALSE       -> 0000006D
                             0000005C     01 - POP_TOP             
                             0000005D     7C - LOAD_FAST           'subject'
                             00000060     69 - LOAD_ATTR           'abilities'
                             00000063     74 - LOAD_GLOBAL         'AbilityCraftingAbility'
                             00000066     19 - BINARY_SUBSCR       
                             00000067     7D - STORE_FAST          'abil_level'
                             0000006A     6E - JUMP_FORWARD        -> 0000006E
                             0000006D     01 - POP_TOP             
                             0000006E     7C - LOAD_FAST           'cat'
                             00000071     64 - LOAD_CONST          0
                             00000074     19 - BINARY_SUBSCR       
                             00000075     64 - LOAD_CONST          'I'
                             00000078     6A - COMPARE_OP          "=="
                             0000007B     6F - JUMP_IF_FALSE       -> 0000008C
                             0000007E     01 - POP_TOP             
                             0000007F     7C - LOAD_FAST           'cat'
                             00000082     64 - LOAD_CONST          1
                             00000085     19 - BINARY_SUBSCR       
                             00000086     64 - LOAD_CONST          'A'
                             00000089     6A - COMPARE_OP          "=="
                             0000008C     6F - JUMP_IF_FALSE       -> 000000A0
                             0000008F     01 - POP_TOP             
                             00000090     7C - LOAD_FAST           'subject'
                             00000093     69 - LOAD_ATTR           'abilities'
                             00000096     74 - LOAD_GLOBAL         'ApparelCraftingAbility'
                             00000099     19 - BINARY_SUBSCR       
                             0000009A     7D - STORE_FAST          'abil_level'
                             0000009D     6E - JUMP_FORWARD        -> 000000A1
                             000000A0     01 - POP_TOP             
                             000000A1     7C - LOAD_FAST           'cat'
                             000000A4     64 - LOAD_CONST          0
                             000000A7     19 - BINARY_SUBSCR       
                             000000A8     64 - LOAD_CONST          'I'
                             000000AB     6A - COMPARE_OP          "=="
                             000000AE     6F - JUMP_IF_FALSE       -> 000000BF
                             000000B1     01 - POP_TOP             
                             000000B2     7C - LOAD_FAST           'cat'
                             000000B5     64 - LOAD_CONST          1
                             000000B8     19 - BINARY_SUBSCR       
                             000000B9     64 - LOAD_CONST          'T'
                             000000BC     6A - COMPARE_OP          "=="
                             000000BF     6F - JUMP_IF_FALSE       -> 000000D3
                             000000C2     01 - POP_TOP             
                             000000C3     7C - LOAD_FAST           'subject'
                             000000C6     69 - LOAD_ATTR           'abilities'
                             000000C9     74 - LOAD_GLOBAL         'ToolCraftingAbility'
                             000000CC     19 - BINARY_SUBSCR       
                             000000CD     7D - STORE_FAST          'abil_level'
                             000000D0     6E - JUMP_FORWARD        -> 000000D4
                             000000D3     01 - POP_TOP             
                             000000D4     7C - LOAD_FAST           'cat'
                             000000D7     64 - LOAD_CONST          0
                             000000DA     19 - BINARY_SUBSCR       
                             000000DB     64 - LOAD_CONST          'I'
                             000000DE     6A - COMPARE_OP          "=="
                             000000E1     6F - JUMP_IF_FALSE       -> 000000F2
                             000000E4     01 - POP_TOP             
                             000000E5     7C - LOAD_FAST           'cat'
                             000000E8     64 - LOAD_CONST          1
                             000000EB     19 - BINARY_SUBSCR       
                             000000EC     64 - LOAD_CONST          'C'
                             000000EF     6A - COMPARE_OP          "=="
                             000000F2     6F - JUMP_IF_FALSE       -> 00000106
                             000000F5     01 - POP_TOP             
                             000000F6     7C - LOAD_FAST           'subject'
                             000000F9     69 - LOAD_ATTR           'abilities'
                             000000FC     74 - LOAD_GLOBAL         'UpgradeCraftingAbility'
                             000000FF     19 - BINARY_SUBSCR       
                             00000100     7D - STORE_FAST          'abil_level'
                             00000103     71 - JUMP_ABSOLUTE       -> 0000010B
                             00000106     01 - POP_TOP             
                             00000107     6E - JUMP_FORWARD        -> 0000010B
                             0000010A     01 - POP_TOP             
                             0000010B     7C - LOAD_FAST           'abil_level'
                             0000010E     53 - RETURN_VALUE        
                             0000010F     64 - LOAD_CONST          None
                             00000112     53 - RETURN_VALUE        
                         consts:
000012BF                     TUPLE: (
000012C4                         None (4E),
000012C5                         INT: 0 (00 00 00 00),
000012CA                         STR: 'I' (01 00 00 00 49),
000012D0                         INT: 1 (01 00 00 00),
000012D5                         STR: 'W' (01 00 00 00 57),
000012DB                         STR: 'A' (01 00 00 00 41),
000012E1                         STR: 'T' (01 00 00 00 54),
000012E7                         STR: 'C' (01 00 00 00 43)
                             )
                         names:
000012ED                     TUPLE: (
000012F2                         STR: 'abil_level' (0A 00 00 00 61 62 69 6C 5F 6C 65 76 65 6C),
00001301                         STR: 'GOCategoryID' (0C 00 00 00 47 4F 43 61 74 65 67 6F 72 79 49 44),
00001312                         STR: 'toFourCC' (08 00 00 00 74 6F 46 6F 75 72 43 43),
0000131F                         STR: 'cat' (03 00 00 00 63 61 74),
00001327                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00001333                         STR: 'abilities' (09 00 00 00 61 62 69 6C 69 74 69 65 73),
00001341                         STR: 'WeaponCraftingAbility' (15 00 00 00 57 65 61 70 6F 6E 43 72 61 66 74 69 6E 67 41 62 69 6C 69 74 79),
0000135B                         STR: 'AbilityCraftingAbility' (16 00 00 00 41 62 69 6C 69 74 79 43 72 61 66 74 69 6E 67 41 62 69 6C 69 74 79),
00001376                         STR: 'ApparelCraftingAbility' (16 00 00 00 41 70 70 61 72 65 6C 43 72 61 66 74 69 6E 67 41 62 69 6C 69 74 79),
00001391                         STR: 'ToolCraftingAbility' (13 00 00 00 54 6F 6F 6C 43 72 61 66 74 69 6E 67 41 62 69 6C 69 74 79),
000013A9                         STR: 'UpgradeCraftingAbility' (16 00 00 00 55 70 67 72 61 64 65 43 72 61 66 74 69 6E 67 41 62 69 6C 69 74 79)
                             )
                         varnames:
000013C4                     TUPLE: (
000013C9                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000013D5                         STR: 'GOCategoryID' (0C 00 00 00 47 4F 43 61 74 65 67 6F 72 79 49 44),
000013E6                         STR: 'cat' (03 00 00 00 63 61 74),
000013EE                         STR: 'abil_level' (0A 00 00 00 61 62 69 6C 5F 6C 65 76 65 6C)
                             )
                         freevars:
000013FD                     TUPLE: ()
                         cellvars:
00001402                     TUPLE: ()
                         filename:
00001407                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\crafting_server.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 72 61 66 74 69 6E 67 5F 73 65 72 76 65 72 2E 70 79)
                         name:
00001453                     STR: 'GetAbilityBonusByCategory' (19 00 00 00 47 65 74 41 62 69 6C 69 74 79 42 6F 6E 75 73 42 79 43 61 74 65 67 6F 72 79)
                         firslineno:
00001471                     LONG: 167L (A7 00 00 00)
                         lnotab:
00001475                     STR: '\x00\x01\x06\x02\x07\x01\x0c\x01"\x01\x11\x01\x11\x01\x11\x01"\x01\x11\x01"\x01\x11\x01"\x01\x15\x02' (1C 00 00 00 00 01 06 02 07 01 0C 01 22 01 11 01 11 01 11 01 22 01 11 01 22 01 11 01 22 01 15 02),
00001496             CODE:
                         argcount:
00001497                     LONG: 2L (02 00 00 00)
                         nlocals:
0000149B                     LONG: 5L (05 00 00 00)
                         stacksize:
0000149F                     LONG: 3L (03 00 00 00)
                         flags:
000014A3                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000014A7                     STR: '|\x00\x00i\x01\x00i\x02\x00d\x01\x00\x83\x01\x00}\x03\x00d\x02\x00}\x02\x00d\x03\x00}\x04\x00|\x01\x00i\x07\x00t\x08\x00j\t\x00o\x17\x00\x01|\x01\x00i\x07\x00t\t\x00i\n\x00i\x0b\x00\x14}\x02\x00n\x11\x00\x01d\x04\x00t\t\x00i\n\x00i\x0b\x00\x14}\x02\x00|\x00\x00i\x0c\x00t\r\x00\x19o\x15\x00\x01|\x00\x00i\x0e\x00t\r\x00\x19d\x05\x00\x15}\x04\x00n\x01\x00\x01|\x04\x00|\x03\x00d\x06\x00\x197}\x04\x00|\x04\x00d\x07\x00j\x04\x00o\n\x00\x01d\x07\x00}\x04\x00n\x0b\x00\x01d\x07\x00|\x04\x00\x18}\x04\x00t\x0f\x00|\x02\x00|\x04\x00\x14\x83\x01\x00}\x02\x00|\x02\x00Sd\x00\x00S' (BF 00 00 00 7C 00 00 69 01 00 69 02 00 64 01 00 83 01 00 7D 03 00 64 02 00 7D 02 00 64 03 00 7D 04 00 7C 01 00 69 07 00 74 08 00 6A 09 00 6F 17 00 01 7C 01 00 69 07 00 74 09 00 69 0A 00 69 0B 00 14 7D 02 00 6E 11 00 01 64 04 00 74 09 00 69 0A 00 69 0B 00 14 7D 02 00 7C 00 00 69 0C 00 74 0D 00 19 6F 15 00 01 7C 00 00 69 0E 00 74 0D 00 19 64 05 00 15 7D 04 00 6E 01 00 01 7C 04 00 7C 03 00 64 06 00 19 37 7D 04 00 7C 04 00 64 07 00 6A 04 00 6F 0A 00 01 64 07 00 7D 04 00 6E 0B 00 01 64 07 00 7C 04 00 18 7D 04 00 74 0F 00 7C 02 00 7C 04 00 14 83 01 00 7D 02 00 7C 02 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'subject'
                             00000003     69 - LOAD_ATTR           'AbilityInv'
                             00000006     69 - LOAD_ATTR           'getSignalBoostBonus'
                             00000009     64 - LOAD_CONST          5000.0
                             0000000C     83 - CALL_FUNCTION       r0001
                             0000000F     7D - STORE_FAST          'signalboost'
                             00000012     64 - LOAD_CONST          0
                             00000015     7D - STORE_FAST          'info_cost'
                             00000018     64 - LOAD_CONST          0.0
                             0000001B     7D - STORE_FAST          'discount'
                             0000001E     7C - LOAD_FAST           'object'
                             00000021     69 - LOAD_ATTR           'VendorPrice'
                             00000024     74 - LOAD_GLOBAL         'None'
                             00000027     6A - COMPARE_OP          "is not"
                             0000002A     6F - JUMP_IF_FALSE       -> 00000044
                             0000002D     01 - POP_TOP             
                             0000002E     7C - LOAD_FAST           'object'
                             00000031     69 - LOAD_ATTR           'VendorPrice'
                             00000034     74 - LOAD_GLOBAL         'constants'
                             00000037     69 - LOAD_ATTR           'Crafting'
                             0000003A     69 - LOAD_ATTR           'CompileCompileCostMultiplier'
                             0000003D     14 - BINARY_MULTIPLY     
                             0000003E     7D - STORE_FAST          'info_cost'
                             00000041     6E - JUMP_FORWARD        -> 00000055
                             00000044     01 - POP_TOP             
                             00000045     64 - LOAD_CONST          1000
                             00000048     74 - LOAD_GLOBAL         'constants'
                             0000004B     69 - LOAD_ATTR           'Crafting'
                             0000004E     69 - LOAD_ATTR           'CompileCompileCostMultiplier'
                             00000051     14 - BINARY_MULTIPLY     
                             00000052     7D - STORE_FAST          'info_cost'
                             00000055     7C - LOAD_FAST           'subject'
                             00000058     69 - LOAD_ATTR           'hasAbility'
                             0000005B     74 - LOAD_GLOBAL         'CraftingCostDiscountAbility'
                             0000005E     19 - BINARY_SUBSCR       
                             0000005F     6F - JUMP_IF_FALSE       -> 00000077
                             00000062     01 - POP_TOP             
                             00000063     7C - LOAD_FAST           'subject'
                             00000066     69 - LOAD_ATTR           'abilities'
                             00000069     74 - LOAD_GLOBAL         'CraftingCostDiscountAbility'
                             0000006C     19 - BINARY_SUBSCR       
                             0000006D     64 - LOAD_CONST          100.0
                             00000070     15 - BINARY_DIVIDE       
                             00000071     7D - STORE_FAST          'discount'
                             00000074     6E - JUMP_FORWARD        -> 00000078
                             00000077     01 - POP_TOP             
                             00000078     7C - LOAD_FAST           'discount'
                             0000007B     7C - LOAD_FAST           'signalboost'
                             0000007E     64 - LOAD_CONST          1
                             00000081     19 - BINARY_SUBSCR       
                             00000082     37 - INPLACE_ADD         
                             00000083     7D - STORE_FAST          'discount'
                             00000086     7C - LOAD_FAST           'discount'
                             00000089     64 - LOAD_CONST          1.0
                             0000008C     6A - COMPARE_OP          ">"
                             0000008F     6F - JUMP_IF_FALSE       -> 0000009C
                             00000092     01 - POP_TOP             
                             00000093     64 - LOAD_CONST          1.0
                             00000096     7D - STORE_FAST          'discount'
                             00000099     6E - JUMP_FORWARD        -> 000000A7
                             0000009C     01 - POP_TOP             
                             0000009D     64 - LOAD_CONST          1.0
                             000000A0     7C - LOAD_FAST           'discount'
                             000000A3     18 - BINARY_SUBTRACT     
                             000000A4     7D - STORE_FAST          'discount'
                             000000A7     74 - LOAD_GLOBAL         'int'
                             000000AA     7C - LOAD_FAST           'info_cost'
                             000000AD     7C - LOAD_FAST           'discount'
                             000000B0     14 - BINARY_MULTIPLY     
                             000000B1     83 - CALL_FUNCTION       r0001
                             000000B4     7D - STORE_FAST          'info_cost'
                             000000B7     7C - LOAD_FAST           'info_cost'
                             000000BA     53 - RETURN_VALUE        
                             000000BB     64 - LOAD_CONST          None
                             000000BE     53 - RETURN_VALUE        
                         consts:
0000156B                     TUPLE: (
00001570                         None (4E),
00001571                         FLOAT: 5000.0 (06 35 30 30 30 2E 30),
00001579                         INT: 0 (00 00 00 00),
0000157E                         FLOAT: 0.0 (03 30 2E 30),
00001583                         INT: 1000 (E8 03 00 00),
00001588                         FLOAT: 100.0 (05 31 30 30 2E 30),
0000158F                         INT: 1 (01 00 00 00),
00001594                         FLOAT: 1.0 (03 31 2E 30)
                             )
                         names:
00001599                     TUPLE: (
0000159E                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000015AA                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
000015B9                         STR: 'getSignalBoostBonus' (13 00 00 00 67 65 74 53 69 67 6E 61 6C 42 6F 6F 73 74 42 6F 6E 75 73),
000015D1                         STR: 'signalboost' (0B 00 00 00 73 69 67 6E 61 6C 62 6F 6F 73 74),
000015E1                         STR: 'info_cost' (09 00 00 00 69 6E 66 6F 5F 63 6F 73 74),
000015EF                         STR: 'discount' (08 00 00 00 64 69 73 63 6F 75 6E 74),
000015FC                         STR: 'object' (06 00 00 00 6F 62 6A 65 63 74),
00001607                         STR: 'VendorPrice' (0B 00 00 00 56 65 6E 64 6F 72 50 72 69 63 65),
00001617                         STR: 'None' (04 00 00 00 4E 6F 6E 65),
00001620                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
0000162E                         STR: 'Crafting' (08 00 00 00 43 72 61 66 74 69 6E 67),
0000163B                         STR: 'CompileCompileCostMultiplier' (1C 00 00 00 43 6F 6D 70 69 6C 65 43 6F 6D 70 69 6C 65 43 6F 73 74 4D 75 6C 74 69 70 6C 69 65 72),
0000165C                         STR: 'hasAbility' (0A 00 00 00 68 61 73 41 62 69 6C 69 74 79),
0000166B                         STR: 'CraftingCostDiscountAbility' (1B 00 00 00 43 72 61 66 74 69 6E 67 43 6F 73 74 44 69 73 63 6F 75 6E 74 41 62 69 6C 69 74 79),
0000168B                         STR: 'abilities' (09 00 00 00 61 62 69 6C 69 74 69 65 73),
00001699                         STR: 'int' (03 00 00 00 69 6E 74)
                             )
                         varnames:
000016A1                     TUPLE: (
000016A6                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000016B2                         STR: 'object' (06 00 00 00 6F 62 6A 65 63 74),
000016BD                         STR: 'info_cost' (09 00 00 00 69 6E 66 6F 5F 63 6F 73 74),
000016CB                         STR: 'signalboost' (0B 00 00 00 73 69 67 6E 61 6C 62 6F 6F 73 74),
000016DB                         STR: 'discount' (08 00 00 00 64 69 73 63 6F 75 6E 74)
                             )
                         freevars:
000016E8                     TUPLE: ()
                         cellvars:
000016ED                     TUPLE: ()
                         filename:
000016F2                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\crafting_server.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 72 61 66 74 69 6E 67 5F 73 65 72 76 65 72 2E 70 79)
                         name:
0000173E                     STR: 'CalcItemInfoCost' (10 00 00 00 43 61 6C 63 49 74 65 6D 49 6E 66 6F 43 6F 73 74)
                         firslineno:
00001753                     LONG: 188L (BC 00 00 00)
                         lnotab:
00001757                     STR: '\x00\x01\x12\x01\x06\x01\x06\x02\x10\x01\x17\x02\x10\x03\x0e\x01\x15\x02\x0e\x03\r\x01\n\x02\n\x03\x10\x02' (1C 00 00 00 00 01 12 01 06 01 06 02 10 01 17 02 10 03 0E 01 15 02 0E 03 0D 01 0A 02 0A 03 10 02),
00001778             CODE:
                         argcount:
00001779                     LONG: 2L (02 00 00 00)
                         nlocals:
0000177D                     LONG: 10L (0A 00 00 00)
                         stacksize:
00001781                     LONG: 9L (09 00 00 00)
                         flags:
00001785                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001789                     STR: '|\x00\x00i\x01\x00t\x02\x00\x19}\x08\x00|\x00\x00i\x04\x00i\x05\x00d\x01\x00\x83\x01\x00}\x05\x00t\x07\x00|\x00\x00|\x01\x00\x83\x02\x00}\x04\x00d\x02\x00}\x06\x00t\x0b\x00i\x0c\x00|\x01\x00i\r\x00\x83\x01\x00}\x03\x00|\x04\x00|\x00\x00i\x0f\x00i\x10\x00j\x04\x00o,\x00\x01|\x00\x00i\x11\x00i\x12\x00t\x13\x00i\x14\x00\x83\x01\x00\x01t\x15\x00|\x00\x00|\x03\x00d\x03\x00\x17\x83\x02\x00\x01d\x04\x00Sn\x01\x00\x01t\x16\x00\x83\x00\x00}\t\x00d\x04\x00}\x07\x00|\x01\x00i\x19\x00t\x1a\x00j\t\x00o\r\x00\x01|\x01\x00i\x19\x00}\x07\x00n\x1c\x00\x01|\x03\x00d\x05\x00\x17}\x03\x00t\x15\x00|\x00\x00|\x03\x00\x83\x02\x00\x01d\x04\x00St\x1b\x00|\x00\x00|\x01\x00i\x1c\x00\x83\x02\x00}\x02\x00|\x02\x00d\x04\x00j\x04\x00o%\x00\x01t\x1e\x00|\x02\x00d\x06\x00\x14\x83\x01\x00}\x02\x00t\x15\x00|\x00\x00d\x07\x00|\x02\x00\x16\x83\x02\x00\x01n\x01\x00\x01|\x08\x00|\x02\x00\x17}\x08\x00|\x00\x00i\x0f\x00i\x1f\x00|\x04\x00\x0bt \x00i!\x00i"\x00\x83\x02\x00\x01t\x15\x00|\x00\x00d\x08\x00d\t\x00|\x08\x00\x14|\t\x00d\t\x00|\x08\x00\x14|\t\x00\x17d\t\x00|\x07\x00\x14d\t\x00|\x07\x00\x14d\n\x00\x17f\x05\x00\x16\x83\x02\x00\x01|\x08\x00d\x04\x00j\x04\x00o-\x00\x01d\t\x00|\x08\x00\x14|\t\x00\x17d\t\x00|\x07\x00\x14d\n\x00\x17\x18d\x04\x00j\x04\x00o\x08\x00\x01d\x0b\x00Sq\xa6\x01\x01n\x01\x00\x01|\x00\x00i\x11\x00i\x12\x00t\x13\x00i#\x00\x83\x01\x00\x01d\x04\x00Sd\x00\x00S' (C1 01 00 00 7C 00 00 69 01 00 74 02 00 19 7D 08 00 7C 00 00 69 04 00 69 05 00 64 01 00 83 01 00 7D 05 00 74 07 00 7C 00 00 7C 01 00 83 02 00 7D 04 00 64 02 00 7D 06 00 74 0B 00 69 0C 00 7C 01 00 69 0D 00 83 01 00 7D 03 00 7C 04 00 7C 00 00 69 0F 00 69 10 00 6A 04 00 6F 2C 00 01 7C 00 00 69 11 00 69 12 00 74 13 00 69 14 00 83 01 00 01 74 15 00 7C 00 00 7C 03 00 64 03 00 17 83 02 00 01 64 04 00 53 6E 01 00 01 74 16 00 83 00 00 7D 09 00 64 04 00 7D 07 00 7C 01 00 69 19 00 74 1A 00 6A 09 00 6F 0D 00 01 7C 01 00 69 19 00 7D 07 00 6E 1C 00 01 7C 03 00 64 05 00 17 7D 03 00 74 15 00 7C 00 00 7C 03 00 83 02 00 01 64 04 00 53 74 1B 00 7C 00 00 7C 01 00 69 1C 00 83 02 00 7D 02 00 7C 02 00 64 04 00 6A 04 00 6F 25 00 01 74 1E 00 7C 02 00 64 06 00 14 83 01 00 7D 02 00 74 15 00 7C 00 00 64 07 00 7C 02 00 16 83 02 00 01 6E 01 00 01 7C 08 00 7C 02 00 17 7D 08 00 7C 00 00 69 0F 00 69 1F 00 7C 04 00 0B 74 20 00 69 21 00 69 22 00 83 02 00 01 74 15 00 7C 00 00 64 08 00 64 09 00 7C 08 00 14 7C 09 00 64 09 00 7C 08 00 14 7C 09 00 17 64 09 00 7C 07 00 14 64 09 00 7C 07 00 14 64 0A 00 17 66 05 00 16 83 02 00 01 7C 08 00 64 04 00 6A 04 00 6F 2D 00 01 64 09 00 7C 08 00 14 7C 09 00 17 64 09 00 7C 07 00 14 64 0A 00 17 18 64 04 00 6A 04 00 6F 08 00 01 64 0B 00 53 71 A6 01 01 6E 01 00 01 7C 00 00 69 11 00 69 12 00 74 13 00 69 23 00 83 01 00 01 64 04 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'subject'
                             00000003     69 - LOAD_ATTR           'abilities'
                             00000006     74 - LOAD_GLOBAL         'CompileSkillAbility'
                             00000009     19 - BINARY_SUBSCR       
                             0000000A     7D - STORE_FAST          'abil_level'
                             0000000D     7C - LOAD_FAST           'subject'
                             00000010     69 - LOAD_ATTR           'AbilityInv'
                             00000013     69 - LOAD_ATTR           'getSignalBoostBonus'
                             00000016     64 - LOAD_CONST          5000.0
                             00000019     83 - CALL_FUNCTION       r0001
                             0000001C     7D - STORE_FAST          'signalboost'
                             0000001F     74 - LOAD_GLOBAL         'CalcItemInfoCost'
                             00000022     7C - LOAD_FAST           'subject'
                             00000025     7C - LOAD_FAST           'object'
                             00000028     83 - CALL_FUNCTION       r0002
                             0000002B     7D - STORE_FAST          'info_cost'
                             0000002E     64 - LOAD_CONST          0.0
                             00000031     7D - STORE_FAST          'discount'
                             00000034     74 - LOAD_GLOBAL         'discovery'
                             00000037     69 - LOAD_ATTR           'getGameObjectName'
                             0000003A     7C - LOAD_FAST           'object'
                             0000003D     69 - LOAD_ATTR           'type'
                             00000040     83 - CALL_FUNCTION       r0001
                             00000043     7D - STORE_FAST          '_str'
                             00000046     7C - LOAD_FAST           'info_cost'
                             00000049     7C - LOAD_FAST           'subject'
                             0000004C     69 - LOAD_ATTR           'PlayerCharacter'
                             0000004F     69 - LOAD_ATTR           'Information'
                             00000052     6A - COMPARE_OP          ">"
                             00000055     6F - JUMP_IF_FALSE       -> 00000084
                             00000058     01 - POP_TOP             
                             00000059     7C - LOAD_FAST           'subject'
                             0000005C     69 - LOAD_ATTR           'Inventory'
                             0000005F     69 - LOAD_ATTR           'craftUIFeedback'
                             00000062     74 - LOAD_GLOBAL         'ST'
                             00000065     69 - LOAD_ATTR           'ID_COMPILE_NOT_ENOUGH_INFO_TO_COMPILE_ITEM'
                             00000068     83 - CALL_FUNCTION       r0001
                             0000006B     01 - POP_TOP             
                             0000006C     74 - LOAD_GLOBAL         'craftingFeedback'
                             0000006F     7C - LOAD_FAST           'subject'
                             00000072     7C - LOAD_FAST           '_str'
                             00000075     64 - LOAD_CONST          ' Not enough Info to Compile .. '
                             00000078     17 - BINARY_ADD          
                             00000079     83 - CALL_FUNCTION       r0002
                             0000007C     01 - POP_TOP             
                             0000007D     64 - LOAD_CONST          0
                             00000080     53 - RETURN_VALUE        
                             00000081     6E - JUMP_FORWARD        -> 00000085
                             00000084     01 - POP_TOP             
                             00000085     74 - LOAD_GLOBAL         'gD100'
                             00000088     83 - CALL_FUNCTION       r0000
                             0000008B     7D - STORE_FAST          'roll'
                             0000008E     64 - LOAD_CONST          0
                             00000091     7D - STORE_FAST          'complexity'
                             00000094     7C - LOAD_FAST           'object'
                             00000097     69 - LOAD_ATTR           'Complexity'
                             0000009A     74 - LOAD_GLOBAL         'None'
                             0000009D     6A - COMPARE_OP          "is not"
                             000000A0     6F - JUMP_IF_FALSE       -> 000000B0
                             000000A3     01 - POP_TOP             
                             000000A4     7C - LOAD_FAST           'object'
                             000000A7     69 - LOAD_ATTR           'Complexity'
                             000000AA     7D - STORE_FAST          'complexity'
                             000000AD     6E - JUMP_FORWARD        -> 000000CC
                             000000B0     01 - POP_TOP             
                             000000B1     7C - LOAD_FAST           '_str'
                             000000B4     64 - LOAD_CONST          ' No Complexity failed to Compile'
                             000000B7     17 - BINARY_ADD          
                             000000B8     7D - STORE_FAST          '_str'
                             000000BB     74 - LOAD_GLOBAL         'craftingFeedback'
                             000000BE     7C - LOAD_FAST           'subject'
                             000000C1     7C - LOAD_FAST           '_str'
                             000000C4     83 - CALL_FUNCTION       r0002
                             000000C7     01 - POP_TOP             
                             000000C8     64 - LOAD_CONST          0
                             000000CB     53 - RETURN_VALUE        
                             000000CC     74 - LOAD_GLOBAL         'GetAbilityBonusByCategory'
                             000000CF     7C - LOAD_FAST           'subject'
                             000000D2     7C - LOAD_FAST           'object'
                             000000D5     69 - LOAD_ATTR           'GOCategoryID'
                             000000D8     83 - CALL_FUNCTION       r0002
                             000000DB     7D - STORE_FAST          'specializationBonus'
                             000000DE     7C - LOAD_FAST           'specializationBonus'
                             000000E1     64 - LOAD_CONST          0
                             000000E4     6A - COMPARE_OP          ">"
                             000000E7     6F - JUMP_IF_FALSE       -> 0000010F
                             000000EA     01 - POP_TOP             
                             000000EB     74 - LOAD_GLOBAL         'int'
                             000000EE     7C - LOAD_FAST           'specializationBonus'
                             000000F1     64 - LOAD_CONST          0.10000000000000001
                             000000F4     14 - BINARY_MULTIPLY     
                             000000F5     83 - CALL_FUNCTION       r0001
                             000000F8     7D - STORE_FAST          'specializationBonus'
                             000000FB     74 - LOAD_GLOBAL         'craftingFeedback'
                             000000FE     7C - LOAD_FAST           'subject'
                             00000101     64 - LOAD_CONST          'Specialization bonus : %d '
                             00000104     7C - LOAD_FAST           'specializationBonus'
                             00000107     16 - BINARY_MODULO       
                             00000108     83 - CALL_FUNCTION       r0002
                             0000010B     01 - POP_TOP             
                             0000010C     6E - JUMP_FORWARD        -> 00000110
                             0000010F     01 - POP_TOP             
                             00000110     7C - LOAD_FAST           'abil_level'
                             00000113     7C - LOAD_FAST           'specializationBonus'
                             00000116     17 - BINARY_ADD          
                             00000117     7D - STORE_FAST          'abil_level'
                             0000011A     7C - LOAD_FAST           'subject'
                             0000011D     69 - LOAD_ATTR           'PlayerCharacter'
                             00000120     69 - LOAD_ATTR           'addInformation'
                             00000123     7C - LOAD_FAST           'info_cost'
                             00000126     0B - UNARY_NEGATIVE      
                             00000127     74 - LOAD_GLOBAL         'constants'
                             0000012A     69 - LOAD_ATTR           'RST'
                             0000012D     69 - LOAD_ATTR           'COMPILE'
                             00000130     83 - CALL_FUNCTION       r0002
                             00000133     01 - POP_TOP             
                             00000134     74 - LOAD_GLOBAL         'craftingFeedback'
                             00000137     7C - LOAD_FAST           'subject'
                             0000013A     64 - LOAD_CONST          'Compile : roll : %d+%d (%d) v.s %d+50 (%d)'
                             0000013D     64 - LOAD_CONST          4
                             00000140     7C - LOAD_FAST           'abil_level'
                             00000143     14 - BINARY_MULTIPLY     
                             00000144     7C - LOAD_FAST           'roll'
                             00000147     64 - LOAD_CONST          4
                             0000014A     7C - LOAD_FAST           'abil_level'
                             0000014D     14 - BINARY_MULTIPLY     
                             0000014E     7C - LOAD_FAST           'roll'
                             00000151     17 - BINARY_ADD          
                             00000152     64 - LOAD_CONST          4
                             00000155     7C - LOAD_FAST           'complexity'
                             00000158     14 - BINARY_MULTIPLY     
                             00000159     64 - LOAD_CONST          4
                             0000015C     7C - LOAD_FAST           'complexity'
                             0000015F     14 - BINARY_MULTIPLY     
                             00000160     64 - LOAD_CONST          50
                             00000163     17 - BINARY_ADD          
                             00000164     66 - BUILD_TUPLE         r0005
                             00000167     16 - BINARY_MODULO       
                             00000168     83 - CALL_FUNCTION       r0002
                             0000016B     01 - POP_TOP             
                             0000016C     7C - LOAD_FAST           'abil_level'
                             0000016F     64 - LOAD_CONST          0
                             00000172     6A - COMPARE_OP          ">"
                             00000175     6F - JUMP_IF_FALSE       -> 000001A5
                             00000178     01 - POP_TOP             
                             00000179     64 - LOAD_CONST          4
                             0000017C     7C - LOAD_FAST           'abil_level'
                             0000017F     14 - BINARY_MULTIPLY     
                             00000180     7C - LOAD_FAST           'roll'
                             00000183     17 - BINARY_ADD          
                             00000184     64 - LOAD_CONST          4
                             00000187     7C - LOAD_FAST           'complexity'
                             0000018A     14 - BINARY_MULTIPLY     
                             0000018B     64 - LOAD_CONST          50
                             0000018E     17 - BINARY_ADD          
                             0000018F     18 - BINARY_SUBTRACT     
                             00000190     64 - LOAD_CONST          0
                             00000193     6A - COMPARE_OP          ">"
                             00000196     6F - JUMP_IF_FALSE       -> 000001A1
                             00000199     01 - POP_TOP             
                             0000019A     64 - LOAD_CONST          1
                             0000019D     53 - RETURN_VALUE        
                             0000019E     71 - JUMP_ABSOLUTE       -> 000001A6
                             000001A1     01 - POP_TOP             
                             000001A2     6E - JUMP_FORWARD        -> 000001A6
                             000001A5     01 - POP_TOP             
                             000001A6     7C - LOAD_FAST           'subject'
                             000001A9     69 - LOAD_ATTR           'Inventory'
                             000001AC     69 - LOAD_ATTR           'craftUIFeedback'
                             000001AF     74 - LOAD_GLOBAL         'ST'
                             000001B2     69 - LOAD_ATTR           'ID_COMPILE_FAILED_TO_COMPILE_ITEM'
                             000001B5     83 - CALL_FUNCTION       r0001
                             000001B8     01 - POP_TOP             
                             000001B9     64 - LOAD_CONST          0
                             000001BC     53 - RETURN_VALUE        
                             000001BD     64 - LOAD_CONST          None
                             000001C0     53 - RETURN_VALUE        
                         consts:
0000194F                     TUPLE: (
00001954                         None (4E),
00001955                         FLOAT: 5000.0 (06 35 30 30 30 2E 30),
0000195D                         FLOAT: 0.0 (03 30 2E 30),
00001962                         STR: ' Not enough Info to Compile .. ' (1F 00 00 00 20 4E 6F 74 20 65 6E 6F 75 67 68 20 49 6E 66 6F 20 74 6F 20 43 6F 6D 70 69 6C 65 20 2E 2E 20),
00001986                         INT: 0 (00 00 00 00),
0000198B                         STR: ' No Complexity failed to Compile' (20 00 00 00 20 4E 6F 20 43 6F 6D 70 6C 65 78 69 74 79 20 66 61 69 6C 65 64 20 74 6F 20 43 6F 6D 70 69 6C 65),
000019B0                         FLOAT: 0.10000000000000001 (13 30 2E 31 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 31),
000019C5                         STR: 'Specialization bonus : %d ' (1A 00 00 00 53 70 65 63 69 61 6C 69 7A 61 74 69 6F 6E 20 62 6F 6E 75 73 20 3A 20 25 64 20),
000019E4                         STR: 'Compile : roll : %d+%d (%d) v.s %d+50 (%d)' (2A 00 00 00 43 6F 6D 70 69 6C 65 20 3A 20 72 6F 6C 6C 20 3A 20 25 64 2B 25 64 20 28 25 64 29 20 76 2E 73 20 25 64 2B 35 30 20 28 25 64 29),
00001A13                         INT: 4 (04 00 00 00),
00001A18                         INT: 50 (32 00 00 00),
00001A1D                         INT: 1 (01 00 00 00)
                             )
                         names:
00001A22                     TUPLE: (
00001A27                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00001A33                         STR: 'abilities' (09 00 00 00 61 62 69 6C 69 74 69 65 73),
00001A41                         STR: 'CompileSkillAbility' (13 00 00 00 43 6F 6D 70 69 6C 65 53 6B 69 6C 6C 41 62 69 6C 69 74 79),
00001A59                         STR: 'abil_level' (0A 00 00 00 61 62 69 6C 5F 6C 65 76 65 6C),
00001A68                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
00001A77                         STR: 'getSignalBoostBonus' (13 00 00 00 67 65 74 53 69 67 6E 61 6C 42 6F 6F 73 74 42 6F 6E 75 73),
00001A8F                         STR: 'signalboost' (0B 00 00 00 73 69 67 6E 61 6C 62 6F 6F 73 74),
00001A9F                         STR: 'CalcItemInfoCost' (10 00 00 00 43 61 6C 63 49 74 65 6D 49 6E 66 6F 43 6F 73 74),
00001AB4                         STR: 'object' (06 00 00 00 6F 62 6A 65 63 74),
00001ABF                         STR: 'info_cost' (09 00 00 00 69 6E 66 6F 5F 63 6F 73 74),
00001ACD                         STR: 'discount' (08 00 00 00 64 69 73 63 6F 75 6E 74),
00001ADA                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
00001AE8                         STR: 'getGameObjectName' (11 00 00 00 67 65 74 47 61 6D 65 4F 62 6A 65 63 74 4E 61 6D 65),
00001AFE                         STR: 'type' (04 00 00 00 74 79 70 65),
00001B07                         STR: '_str' (04 00 00 00 5F 73 74 72),
00001B10                         STR: 'PlayerCharacter' (0F 00 00 00 50 6C 61 79 65 72 43 68 61 72 61 63 74 65 72),
00001B24                         STR: 'Information' (0B 00 00 00 49 6E 66 6F 72 6D 61 74 69 6F 6E),
00001B34                         STR: 'Inventory' (09 00 00 00 49 6E 76 65 6E 74 6F 72 79),
00001B42                         STR: 'craftUIFeedback' (0F 00 00 00 63 72 61 66 74 55 49 46 65 65 64 62 61 63 6B),
00001B56                         STR: 'ST' (02 00 00 00 53 54),
00001B5D                         STR: 'ID_COMPILE_NOT_ENOUGH_INFO_TO_COMPILE_ITEM' (2A 00 00 00 49 44 5F 43 4F 4D 50 49 4C 45 5F 4E 4F 54 5F 45 4E 4F 55 47 48 5F 49 4E 46 4F 5F 54 4F 5F 43 4F 4D 50 49 4C 45 5F 49 54 45 4D),
00001B8C                         STR: 'craftingFeedback' (10 00 00 00 63 72 61 66 74 69 6E 67 46 65 65 64 62 61 63 6B),
00001BA1                         STR: 'gD100' (05 00 00 00 67 44 31 30 30),
00001BAB                         STR: 'roll' (04 00 00 00 72 6F 6C 6C),
00001BB4                         STR: 'complexity' (0A 00 00 00 63 6F 6D 70 6C 65 78 69 74 79),
00001BC3                         STR: 'Complexity' (0A 00 00 00 43 6F 6D 70 6C 65 78 69 74 79),
00001BD2                         STR: 'None' (04 00 00 00 4E 6F 6E 65),
00001BDB                         STR: 'GetAbilityBonusByCategory' (19 00 00 00 47 65 74 41 62 69 6C 69 74 79 42 6F 6E 75 73 42 79 43 61 74 65 67 6F 72 79),
00001BF9                         STR: 'GOCategoryID' (0C 00 00 00 47 4F 43 61 74 65 67 6F 72 79 49 44),
00001C0A                         STR: 'specializationBonus' (13 00 00 00 73 70 65 63 69 61 6C 69 7A 61 74 69 6F 6E 42 6F 6E 75 73),
00001C22                         STR: 'int' (03 00 00 00 69 6E 74),
00001C2A                         STR: 'addInformation' (0E 00 00 00 61 64 64 49 6E 66 6F 72 6D 61 74 69 6F 6E),
00001C3D                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00001C4B                         STR: 'RST' (03 00 00 00 52 53 54),
00001C53                         STR: 'COMPILE' (07 00 00 00 43 4F 4D 50 49 4C 45),
00001C5F                         STR: 'ID_COMPILE_FAILED_TO_COMPILE_ITEM' (21 00 00 00 49 44 5F 43 4F 4D 50 49 4C 45 5F 46 41 49 4C 45 44 5F 54 4F 5F 43 4F 4D 50 49 4C 45 5F 49 54 45 4D)
                             )
                         varnames:
00001C85                     TUPLE: (
00001C8A                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00001C96                         STR: 'object' (06 00 00 00 6F 62 6A 65 63 74),
00001CA1                         STR: 'specializationBonus' (13 00 00 00 73 70 65 63 69 61 6C 69 7A 61 74 69 6F 6E 42 6F 6E 75 73),
00001CB9                         STR: '_str' (04 00 00 00 5F 73 74 72),
00001CC2                         STR: 'info_cost' (09 00 00 00 69 6E 66 6F 5F 63 6F 73 74),
00001CD0                         STR: 'signalboost' (0B 00 00 00 73 69 67 6E 61 6C 62 6F 6F 73 74),
00001CE0                         STR: 'discount' (08 00 00 00 64 69 73 63 6F 75 6E 74),
00001CED                         STR: 'complexity' (0A 00 00 00 63 6F 6D 70 6C 65 78 69 74 79),
00001CFC                         STR: 'abil_level' (0A 00 00 00 61 62 69 6C 5F 6C 65 76 65 6C),
00001D0B                         STR: 'roll' (04 00 00 00 72 6F 6C 6C)
                             )
                         freevars:
00001D14                     TUPLE: ()
                         cellvars:
00001D19                     TUPLE: ()
                         filename:
00001D1E                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\crafting_server.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 72 61 66 74 69 6E 67 5F 73 65 72 76 65 72 2E 70 79)
                         name:
00001D6A                     STR: 'CompileTest' (0B 00 00 00 43 6F 6D 70 69 6C 65 54 65 73 74)
                         firslineno:
00001D7A                     LONG: 218L (DA 00 00 00)
                         lnotab:
00001D7E                     STR: '\x00\x02\r\x01\x12\x01\x0f\x01\x06\x01\x12\x02\x13\x02\x13\x01\x11\x01\x08\x03\t\x01\x06\x02\x10\x01\r\x02\n\x01\r\x01\x04\x03\x12\x01\r\x01\x10\x01\x15\x02\n\x03\x1a\x038\x03\r\x01!\x01\x0c\x03\x13\x01' (38 00 00 00 00 02 0D 01 12 01 0F 01 06 01 12 02 13 02 13 01 11 01 08 03 09 01 06 02 10 01 0D 02 0A 01 0D 01 04 03 12 01 0D 01 10 01 15 02 0A 03 1A 03 38 03 0D 01 21 01 0C 03 13 01),
00001DBB             CODE:
                         argcount:
00001DBC                     LONG: 3L (03 00 00 00)
                         nlocals:
00001DC0                     LONG: 10L (0A 00 00 00)
                         stacksize:
00001DC4                     LONG: 6L (06 00 00 00)
                         flags:
00001DC8                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001DCC                     STR: 'd\x01\x00}\x05\x00|\x00\x00i\x02\x00t\x03\x00\x19}\x08\x00|\x00\x00i\x05\x00i\x06\x00|\x08\x00d\x02\x00\x14\x83\x01\x00}\x04\x00d\x03\x00d\x04\x00|\x00\x00i\x02\x00t\x08\x00\x19\x18\x14t\t\x00|\x00\x00|\x01\x00\x83\x02\x00\x14}\x06\x00|\x06\x00|\x00\x00i\x0c\x00i\r\x00j\x04\x00o,\x00\x01|\x00\x00i\x0e\x00i\x0f\x00t\x10\x00i\x11\x00\x83\x01\x00\x01t\x12\x00|\x00\x00|\x05\x00d\x05\x00\x17\x83\x02\x00\x01d\x06\x00Sn\x01\x00\x01t\x13\x00\x83\x00\x00}\t\x00|\x05\x00d\x07\x00|\t\x00\x167}\x05\x00|\t\x00|\x04\x00d\x06\x00\x19\x17}\t\x00|\x05\x00d\x08\x00|\x04\x00d\x06\x00\x19\x167}\x05\x00|\x01\x00i\x15\x00}\x07\x00|\x05\x00d\t\x00t\x17\x00|\x07\x00\x83\x01\x00\x167}\x05\x00t\x18\x00|\x00\x00|\x02\x00\x83\x02\x00}\x03\x00|\x05\x00d\n\x00|\x03\x00\x167}\x05\x00|\x05\x00d\x0b\x00|\x08\x00\x167}\x05\x00|\x05\x00d\x0c\x00t\x1b\x00|\x02\x00\x83\x01\x00\x167}\x05\x00|\x03\x00|\x08\x00j\x04\x00o\x12\x00\x01|\x03\x00|\x04\x00d\x06\x00\x19\x17}\x08\x00n\x0f\x00\x01|\x08\x00|\x04\x00d\x06\x00\x19\x17}\x08\x00t\x12\x00|\x00\x00|\x05\x00\x83\x02\x00\x01t\x12\x00|\x00\x00d\r\x00d\x0e\x00|\x08\x00\x14|\t\x00\x17d\x0e\x00|\x07\x00\x14d\x0f\x00\x17f\x02\x00\x16\x83\x02\x00\x01|\x08\x00d\x06\x00j\x04\x00oG\x00\x01d\x0e\x00|\x08\x00\x14|\t\x00\x17d\x0e\x00|\x07\x00\x14d\x0f\x00\x17\x18d\x06\x00j\x04\x00o"\x00\x01|\x00\x00i\x0c\x00i\x1c\x00|\x06\x00\x0bt\x1d\x00i\x1e\x00i\x1f\x00\x83\x02\x00\x01d\x10\x00Sq\xd2\x01\x01n\x01\x00\x01d\x06\x00Sd\x00\x00S' (DA 01 00 00 64 01 00 7D 05 00 7C 00 00 69 02 00 74 03 00 19 7D 08 00 7C 00 00 69 05 00 69 06 00 7C 08 00 64 02 00 14 83 01 00 7D 04 00 64 03 00 64 04 00 7C 00 00 69 02 00 74 08 00 19 18 14 74 09 00 7C 00 00 7C 01 00 83 02 00 14 7D 06 00 7C 06 00 7C 00 00 69 0C 00 69 0D 00 6A 04 00 6F 2C 00 01 7C 00 00 69 0E 00 69 0F 00 74 10 00 69 11 00 83 01 00 01 74 12 00 7C 00 00 7C 05 00 64 05 00 17 83 02 00 01 64 06 00 53 6E 01 00 01 74 13 00 83 00 00 7D 09 00 7C 05 00 64 07 00 7C 09 00 16 37 7D 05 00 7C 09 00 7C 04 00 64 06 00 19 17 7D 09 00 7C 05 00 64 08 00 7C 04 00 64 06 00 19 16 37 7D 05 00 7C 01 00 69 15 00 7D 07 00 7C 05 00 64 09 00 74 17 00 7C 07 00 83 01 00 16 37 7D 05 00 74 18 00 7C 00 00 7C 02 00 83 02 00 7D 03 00 7C 05 00 64 0A 00 7C 03 00 16 37 7D 05 00 7C 05 00 64 0B 00 7C 08 00 16 37 7D 05 00 7C 05 00 64 0C 00 74 1B 00 7C 02 00 83 01 00 16 37 7D 05 00 7C 03 00 7C 08 00 6A 04 00 6F 12 00 01 7C 03 00 7C 04 00 64 06 00 19 17 7D 08 00 6E 0F 00 01 7C 08 00 7C 04 00 64 06 00 19 17 7D 08 00 74 12 00 7C 00 00 7C 05 00 83 02 00 01 74 12 00 7C 00 00 64 0D 00 64 0E 00 7C 08 00 14 7C 09 00 17 64 0E 00 7C 07 00 14 64 0F 00 17 66 02 00 16 83 02 00 01 7C 08 00 64 06 00 6A 04 00 6F 47 00 01 64 0E 00 7C 08 00 14 7C 09 00 17 64 0E 00 7C 07 00 14 64 0F 00 17 18 64 06 00 6A 04 00 6F 22 00 01 7C 00 00 69 0C 00 69 1C 00 7C 06 00 0B 74 1D 00 69 1E 00 69 1F 00 83 02 00 01 64 10 00 53 71 D2 01 01 6E 01 00 01 64 06 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          'Write Code : '
                             00000003     7D - STORE_FAST          '_str'
                             00000006     7C - LOAD_FAST           'subject'
                             00000009     69 - LOAD_ATTR           'abilities'
                             0000000C     74 - LOAD_GLOBAL         'CodeWritingAbility'
                             0000000F     19 - BINARY_SUBSCR       
                             00000010     7D - STORE_FAST          'abil_level'
                             00000013     7C - LOAD_FAST           'subject'
                             00000016     69 - LOAD_ATTR           'AbilityInv'
                             00000019     69 - LOAD_ATTR           'getSignalBoostBonus'
                             0000001C     7C - LOAD_FAST           'abil_level'
                             0000001F     64 - LOAD_CONST          100.0
                             00000022     14 - BINARY_MULTIPLY     
                             00000023     83 - CALL_FUNCTION       r0001
                             00000026     7D - STORE_FAST          'boost'
                             00000029     64 - LOAD_CONST          0.01
                             0000002C     64 - LOAD_CONST          100
                             0000002F     7C - LOAD_FAST           'subject'
                             00000032     69 - LOAD_ATTR           'abilities'
                             00000035     74 - LOAD_GLOBAL         'CodeWritingDiscountAbility'
                             00000038     19 - BINARY_SUBSCR       
                             00000039     18 - BINARY_SUBTRACT     
                             0000003A     14 - BINARY_MULTIPLY     
                             0000003B     74 - LOAD_GLOBAL         'CalcItemInfoCost'
                             0000003E     7C - LOAD_FAST           'subject'
                             00000041     7C - LOAD_FAST           'invItem'
                             00000044     83 - CALL_FUNCTION       r0002
                             00000047     14 - BINARY_MULTIPLY     
                             00000048     7D - STORE_FAST          'info_cost'
                             0000004B     7C - LOAD_FAST           'info_cost'
                             0000004E     7C - LOAD_FAST           'subject'
                             00000051     69 - LOAD_ATTR           'PlayerCharacter'
                             00000054     69 - LOAD_ATTR           'Information'
                             00000057     6A - COMPARE_OP          ">"
                             0000005A     6F - JUMP_IF_FALSE       -> 00000089
                             0000005D     01 - POP_TOP             
                             0000005E     7C - LOAD_FAST           'subject'
                             00000061     69 - LOAD_ATTR           'Inventory'
                             00000064     69 - LOAD_ATTR           'craftUIFeedback'
                             00000067     74 - LOAD_GLOBAL         'ST'
                             0000006A     69 - LOAD_ATTR           'ID_COMPILE_NOT_ENOUGH_INFO_TO_WRITECODE_ITEM'
                             0000006D     83 - CALL_FUNCTION       r0001
                             00000070     01 - POP_TOP             
                             00000071     74 - LOAD_GLOBAL         'craftingFeedback'
                             00000074     7C - LOAD_FAST           'subject'
                             00000077     7C - LOAD_FAST           '_str'
                             0000007A     64 - LOAD_CONST          ' Not enough Info to WriteCode .. '
                             0000007D     17 - BINARY_ADD          
                             0000007E     83 - CALL_FUNCTION       r0002
                             00000081     01 - POP_TOP             
                             00000082     64 - LOAD_CONST          0
                             00000085     53 - RETURN_VALUE        
                             00000086     6E - JUMP_FORWARD        -> 0000008A
                             00000089     01 - POP_TOP             
                             0000008A     74 - LOAD_GLOBAL         'gD100'
                             0000008D     83 - CALL_FUNCTION       r0000
                             00000090     7D - STORE_FAST          'roll'
                             00000093     7C - LOAD_FAST           '_str'
                             00000096     64 - LOAD_CONST          ' roll : %d '
                             00000099     7C - LOAD_FAST           'roll'
                             0000009C     16 - BINARY_MODULO       
                             0000009D     37 - INPLACE_ADD         
                             0000009E     7D - STORE_FAST          '_str'
                             000000A1     7C - LOAD_FAST           'roll'
                             000000A4     7C - LOAD_FAST           'boost'
                             000000A7     64 - LOAD_CONST          0
                             000000AA     19 - BINARY_SUBSCR       
                             000000AB     17 - BINARY_ADD          
                             000000AC     7D - STORE_FAST          'roll'
                             000000AF     7C - LOAD_FAST           '_str'
                             000000B2     64 - LOAD_CONST          ' boost %d '
                             000000B5     7C - LOAD_FAST           'boost'
                             000000B8     64 - LOAD_CONST          0
                             000000BB     19 - BINARY_SUBSCR       
                             000000BC     16 - BINARY_MODULO       
                             000000BD     37 - INPLACE_ADD         
                             000000BE     7D - STORE_FAST          '_str'
                             000000C1     7C - LOAD_FAST           'invItem'
                             000000C4     69 - LOAD_ATTR           'Complexity'
                             000000C7     7D - STORE_FAST          'complexity'
                             000000CA     7C - LOAD_FAST           '_str'
                             000000CD     64 - LOAD_CONST          ' object diff %d '
                             000000D0     74 - LOAD_GLOBAL         'int'
                             000000D3     7C - LOAD_FAST           'complexity'
                             000000D6     83 - CALL_FUNCTION       r0001
                             000000D9     16 - BINARY_MODULO       
                             000000DA     37 - INPLACE_ADD         
                             000000DB     7D - STORE_FAST          '_str'
                             000000DE     74 - LOAD_GLOBAL         'GetAbilityBonusByCategory'
                             000000E1     7C - LOAD_FAST           'subject'
                             000000E4     7C - LOAD_FAST           'GOCatID'
                             000000E7     83 - CALL_FUNCTION       r0002
                             000000EA     7D - STORE_FAST          'cat_boost'
                             000000ED     7C - LOAD_FAST           '_str'
                             000000F0     64 - LOAD_CONST          ' cat_boost : %d '
                             000000F3     7C - LOAD_FAST           'cat_boost'
                             000000F6     16 - BINARY_MODULO       
                             000000F7     37 - INPLACE_ADD         
                             000000F8     7D - STORE_FAST          '_str'
                             000000FB     7C - LOAD_FAST           '_str'
                             000000FE     64 - LOAD_CONST          ' abil lvl  : %d '
                             00000101     7C - LOAD_FAST           'abil_level'
                             00000104     16 - BINARY_MODULO       
                             00000105     37 - INPLACE_ADD         
                             00000106     7D - STORE_FAST          '_str'
                             00000109     7C - LOAD_FAST           '_str'
                             0000010C     64 - LOAD_CONST          ' objcat : %s '
                             0000010F     74 - LOAD_GLOBAL         'toFourCC'
                             00000112     7C - LOAD_FAST           'GOCatID'
                             00000115     83 - CALL_FUNCTION       r0001
                             00000118     16 - BINARY_MODULO       
                             00000119     37 - INPLACE_ADD         
                             0000011A     7D - STORE_FAST          '_str'
                             0000011D     7C - LOAD_FAST           'cat_boost'
                             00000120     7C - LOAD_FAST           'abil_level'
                             00000123     6A - COMPARE_OP          ">"
                             00000126     6F - JUMP_IF_FALSE       -> 0000013B
                             00000129     01 - POP_TOP             
                             0000012A     7C - LOAD_FAST           'cat_boost'
                             0000012D     7C - LOAD_FAST           'boost'
                             00000130     64 - LOAD_CONST          0
                             00000133     19 - BINARY_SUBSCR       
                             00000134     17 - BINARY_ADD          
                             00000135     7D - STORE_FAST          'abil_level'
                             00000138     6E - JUMP_FORWARD        -> 0000014A
                             0000013B     01 - POP_TOP             
                             0000013C     7C - LOAD_FAST           'abil_level'
                             0000013F     7C - LOAD_FAST           'boost'
                             00000142     64 - LOAD_CONST          0
                             00000145     19 - BINARY_SUBSCR       
                             00000146     17 - BINARY_ADD          
                             00000147     7D - STORE_FAST          'abil_level'
                             0000014A     74 - LOAD_GLOBAL         'craftingFeedback'
                             0000014D     7C - LOAD_FAST           'subject'
                             00000150     7C - LOAD_FAST           '_str'
                             00000153     83 - CALL_FUNCTION       r0002
                             00000156     01 - POP_TOP             
                             00000157     74 - LOAD_GLOBAL         'craftingFeedback'
                             0000015A     7C - LOAD_FAST           'subject'
                             0000015D     64 - LOAD_CONST          'WC contest: %d v.s %d'
                             00000160     64 - LOAD_CONST          4
                             00000163     7C - LOAD_FAST           'abil_level'
                             00000166     14 - BINARY_MULTIPLY     
                             00000167     7C - LOAD_FAST           'roll'
                             0000016A     17 - BINARY_ADD          
                             0000016B     64 - LOAD_CONST          4
                             0000016E     7C - LOAD_FAST           'complexity'
                             00000171     14 - BINARY_MULTIPLY     
                             00000172     64 - LOAD_CONST          50
                             00000175     17 - BINARY_ADD          
                             00000176     66 - BUILD_TUPLE         r0002
                             00000179     16 - BINARY_MODULO       
                             0000017A     83 - CALL_FUNCTION       r0002
                             0000017D     01 - POP_TOP             
                             0000017E     7C - LOAD_FAST           'abil_level'
                             00000181     64 - LOAD_CONST          0
                             00000184     6A - COMPARE_OP          ">"
                             00000187     6F - JUMP_IF_FALSE       -> 000001D1
                             0000018A     01 - POP_TOP             
                             0000018B     64 - LOAD_CONST          4
                             0000018E     7C - LOAD_FAST           'abil_level'
                             00000191     14 - BINARY_MULTIPLY     
                             00000192     7C - LOAD_FAST           'roll'
                             00000195     17 - BINARY_ADD          
                             00000196     64 - LOAD_CONST          4
                             00000199     7C - LOAD_FAST           'complexity'
                             0000019C     14 - BINARY_MULTIPLY     
                             0000019D     64 - LOAD_CONST          50
                             000001A0     17 - BINARY_ADD          
                             000001A1     18 - BINARY_SUBTRACT     
                             000001A2     64 - LOAD_CONST          0
                             000001A5     6A - COMPARE_OP          ">"
                             000001A8     6F - JUMP_IF_FALSE       -> 000001CD
                             000001AB     01 - POP_TOP             
                             000001AC     7C - LOAD_FAST           'subject'
                             000001AF     69 - LOAD_ATTR           'PlayerCharacter'
                             000001B2     69 - LOAD_ATTR           'addInformation'
                             000001B5     7C - LOAD_FAST           'info_cost'
                             000001B8     0B - UNARY_NEGATIVE      
                             000001B9     74 - LOAD_GLOBAL         'constants'
                             000001BC     69 - LOAD_ATTR           'RST'
                             000001BF     69 - LOAD_ATTR           'WRITECODE'
                             000001C2     83 - CALL_FUNCTION       r0002
                             000001C5     01 - POP_TOP             
                             000001C6     64 - LOAD_CONST          1
                             000001C9     53 - RETURN_VALUE        
                             000001CA     71 - JUMP_ABSOLUTE       -> 000001D2
                             000001CD     01 - POP_TOP             
                             000001CE     6E - JUMP_FORWARD        -> 000001D2
                             000001D1     01 - POP_TOP             
                             000001D2     64 - LOAD_CONST          0
                             000001D5     53 - RETURN_VALUE        
                             000001D6     64 - LOAD_CONST          None
                             000001D9     53 - RETURN_VALUE        
                         consts:
00001FAB                     TUPLE: (
00001FB0                         None (4E),
00001FB1                         STR: 'Write Code : ' (0D 00 00 00 57 72 69 74 65 20 43 6F 64 65 20 3A 20),
00001FC3                         FLOAT: 100.0 (05 31 30 30 2E 30),
00001FCA                         FLOAT: 0.01 (04 30 2E 30 31),
00001FD0                         INT: 100 (64 00 00 00),
00001FD5                         STR: ' Not enough Info to WriteCode .. ' (21 00 00 00 20 4E 6F 74 20 65 6E 6F 75 67 68 20 49 6E 66 6F 20 74 6F 20 57 72 69 74 65 43 6F 64 65 20 2E 2E 20),
00001FFB                         INT: 0 (00 00 00 00),
00002000                         STR: ' roll : %d ' (0B 00 00 00 20 72 6F 6C 6C 20 3A 20 25 64 20),
00002010                         STR: ' boost %d ' (0A 00 00 00 20 62 6F 6F 73 74 20 25 64 20),
0000201F                         STR: ' object diff %d ' (10 00 00 00 20 6F 62 6A 65 63 74 20 64 69 66 66 20 25 64 20),
00002034                         STR: ' cat_boost : %d ' (10 00 00 00 20 63 61 74 5F 62 6F 6F 73 74 20 3A 20 25 64 20),
00002049                         STR: ' abil lvl  : %d ' (10 00 00 00 20 61 62 69 6C 20 6C 76 6C 20 20 3A 20 25 64 20),
0000205E                         STR: ' objcat : %s ' (0D 00 00 00 20 6F 62 6A 63 61 74 20 3A 20 25 73 20),
00002070                         STR: 'WC contest: %d v.s %d' (15 00 00 00 57 43 20 63 6F 6E 74 65 73 74 3A 20 25 64 20 76 2E 73 20 25 64),
0000208A                         INT: 4 (04 00 00 00),
0000208F                         INT: 50 (32 00 00 00),
00002094                         INT: 1 (01 00 00 00)
                             )
                         names:
00002099                     TUPLE: (
0000209E                         STR: '_str' (04 00 00 00 5F 73 74 72),
000020A7                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000020B3                         STR: 'abilities' (09 00 00 00 61 62 69 6C 69 74 69 65 73),
000020C1                         STR: 'CodeWritingAbility' (12 00 00 00 43 6F 64 65 57 72 69 74 69 6E 67 41 62 69 6C 69 74 79),
000020D8                         STR: 'abil_level' (0A 00 00 00 61 62 69 6C 5F 6C 65 76 65 6C),
000020E7                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
000020F6                         STR: 'getSignalBoostBonus' (13 00 00 00 67 65 74 53 69 67 6E 61 6C 42 6F 6F 73 74 42 6F 6E 75 73),
0000210E                         STR: 'boost' (05 00 00 00 62 6F 6F 73 74),
00002118                         STR: 'CodeWritingDiscountAbility' (1A 00 00 00 43 6F 64 65 57 72 69 74 69 6E 67 44 69 73 63 6F 75 6E 74 41 62 69 6C 69 74 79),
00002137                         STR: 'CalcItemInfoCost' (10 00 00 00 43 61 6C 63 49 74 65 6D 49 6E 66 6F 43 6F 73 74),
0000214C                         STR: 'invItem' (07 00 00 00 69 6E 76 49 74 65 6D),
00002158                         STR: 'info_cost' (09 00 00 00 69 6E 66 6F 5F 63 6F 73 74),
00002166                         STR: 'PlayerCharacter' (0F 00 00 00 50 6C 61 79 65 72 43 68 61 72 61 63 74 65 72),
0000217A                         STR: 'Information' (0B 00 00 00 49 6E 66 6F 72 6D 61 74 69 6F 6E),
0000218A                         STR: 'Inventory' (09 00 00 00 49 6E 76 65 6E 74 6F 72 79),
00002198                         STR: 'craftUIFeedback' (0F 00 00 00 63 72 61 66 74 55 49 46 65 65 64 62 61 63 6B),
000021AC                         STR: 'ST' (02 00 00 00 53 54),
000021B3                         STR: 'ID_COMPILE_NOT_ENOUGH_INFO_TO_WRITECODE_ITEM' (2C 00 00 00 49 44 5F 43 4F 4D 50 49 4C 45 5F 4E 4F 54 5F 45 4E 4F 55 47 48 5F 49 4E 46 4F 5F 54 4F 5F 57 52 49 54 45 43 4F 44 45 5F 49 54 45 4D),
000021E4                         STR: 'craftingFeedback' (10 00 00 00 63 72 61 66 74 69 6E 67 46 65 65 64 62 61 63 6B),
000021F9                         STR: 'gD100' (05 00 00 00 67 44 31 30 30),
00002203                         STR: 'roll' (04 00 00 00 72 6F 6C 6C),
0000220C                         STR: 'Complexity' (0A 00 00 00 43 6F 6D 70 6C 65 78 69 74 79),
0000221B                         STR: 'complexity' (0A 00 00 00 63 6F 6D 70 6C 65 78 69 74 79),
0000222A                         STR: 'int' (03 00 00 00 69 6E 74),
00002232                         STR: 'GetAbilityBonusByCategory' (19 00 00 00 47 65 74 41 62 69 6C 69 74 79 42 6F 6E 75 73 42 79 43 61 74 65 67 6F 72 79),
00002250                         STR: 'GOCatID' (07 00 00 00 47 4F 43 61 74 49 44),
0000225C                         STR: 'cat_boost' (09 00 00 00 63 61 74 5F 62 6F 6F 73 74),
0000226A                         STR: 'toFourCC' (08 00 00 00 74 6F 46 6F 75 72 43 43),
00002277                         STR: 'addInformation' (0E 00 00 00 61 64 64 49 6E 66 6F 72 6D 61 74 69 6F 6E),
0000228A                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00002298                         STR: 'RST' (03 00 00 00 52 53 54),
000022A0                         STR: 'WRITECODE' (09 00 00 00 57 52 49 54 45 43 4F 44 45)
                             )
                         varnames:
000022AE                     TUPLE: (
000022B3                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000022BF                         STR: 'invItem' (07 00 00 00 69 6E 76 49 74 65 6D),
000022CB                         STR: 'GOCatID' (07 00 00 00 47 4F 43 61 74 49 44),
000022D7                         STR: 'cat_boost' (09 00 00 00 63 61 74 5F 62 6F 6F 73 74),
000022E5                         STR: 'boost' (05 00 00 00 62 6F 6F 73 74),
000022EF                         STR: '_str' (04 00 00 00 5F 73 74 72),
000022F8                         STR: 'info_cost' (09 00 00 00 69 6E 66 6F 5F 63 6F 73 74),
00002306                         STR: 'complexity' (0A 00 00 00 63 6F 6D 70 6C 65 78 69 74 79),
00002315                         STR: 'abil_level' (0A 00 00 00 61 62 69 6C 5F 6C 65 76 65 6C),
00002324                         STR: 'roll' (04 00 00 00 72 6F 6C 6C)
                             )
                         freevars:
0000232D                     TUPLE: ()
                         cellvars:
00002332                     TUPLE: ()
                         filename:
00002337                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\crafting_server.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 72 61 66 74 69 6E 67 5F 73 65 72 76 65 72 2E 70 79)
                         name:
00002383                     STR: 'WriteCodeTest' (0D 00 00 00 57 72 69 74 65 43 6F 64 65 54 65 73 74)
                         firslineno:
00002395                     LONG: 275L (13 01 00 00)
                         lnotab:
00002399                     STR: '\x00\x02\x06\x02\r\x02\x16\x01"\x03\x13\x02\x13\x01\x11\x01\x08\x03\t\x02\x0e\x01\x0e\x01\x12\x02\t\x02\x14\x02\x0f\x01\x0e\x01\x0e\x01\x14\x02\r\x01\x12\x02\x0e\x02\r\x01\'\x02\r\x01!\x02\x1a\x01\x0c\x02' (38 00 00 00 00 02 06 02 0D 02 16 01 22 03 13 02 13 01 11 01 08 03 09 02 0E 01 0E 01 12 02 09 02 14 02 0F 01 0E 01 0E 01 14 02 0D 01 12 02 0E 02 0D 01 27 02 0D 01 21 02 1A 01 0C 02),
000023D6             CODE:
                         argcount:
000023D7                     LONG: 3L (03 00 00 00)
                         nlocals:
000023DB                     LONG: 3L (03 00 00 00)
                         stacksize:
000023DF                     LONG: 6L (06 00 00 00)
                         flags:
000023E3                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000023E7                     STR: '|\x02\x00d\x01\x00j\x04\x00o\xd8\x00\x01|\x00\x00i\x02\x00i\x03\x00t\x04\x00t\x05\x00|\x02\x00t\x06\x00\x83\x04\x00\x01|\x00\x00i\x02\x00i\x03\x00t\x04\x00t\x07\x00|\x02\x00t\x06\x00\x83\x04\x00\x01|\x00\x00i\x02\x00i\x03\x00t\x04\x00t\x08\x00|\x02\x00t\x06\x00\x83\x04\x00\x01|\x00\x00i\x02\x00i\x03\x00t\x04\x00t\t\x00|\x02\x00t\x06\x00\x83\x04\x00\x01|\x00\x00i\x02\x00i\x03\x00t\x04\x00t\n\x00|\x02\x00t\x06\x00\x83\x04\x00\x01|\x00\x00i\x02\x00i\x03\x00t\x04\x00t\x0b\x00|\x02\x00t\x06\x00\x83\x04\x00\x01|\x00\x00i\x02\x00i\x03\x00t\x04\x00t\x0c\x00|\x02\x00t\x06\x00\x83\x04\x00\x01t\r\x00i\x0e\x00i\x0f\x00t\x10\x00i\x11\x00t\x04\x00|\x00\x00i\x12\x00|\x00\x00i\x12\x00|\x02\x00\x83\x05\x00\x01n\x01\x00\x01d\x02\x00Sd\x00\x00S' (ED 00 00 00 7C 02 00 64 01 00 6A 04 00 6F D8 00 01 7C 00 00 69 02 00 69 03 00 74 04 00 74 05 00 7C 02 00 74 06 00 83 04 00 01 7C 00 00 69 02 00 69 03 00 74 04 00 74 07 00 7C 02 00 74 06 00 83 04 00 01 7C 00 00 69 02 00 69 03 00 74 04 00 74 08 00 7C 02 00 74 06 00 83 04 00 01 7C 00 00 69 02 00 69 03 00 74 04 00 74 09 00 7C 02 00 74 06 00 83 04 00 01 7C 00 00 69 02 00 69 03 00 74 04 00 74 0A 00 7C 02 00 74 06 00 83 04 00 01 7C 00 00 69 02 00 69 03 00 74 04 00 74 0B 00 7C 02 00 74 06 00 83 04 00 01 7C 00 00 69 02 00 69 03 00 74 04 00 74 0C 00 7C 02 00 74 06 00 83 04 00 01 74 0D 00 69 0E 00 69 0F 00 74 10 00 69 11 00 74 04 00 7C 00 00 69 12 00 7C 00 00 69 12 00 7C 02 00 83 05 00 01 6E 01 00 01 64 02 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'buffValue'
                             00000003     64 - LOAD_CONST          0
                             00000006     6A - COMPARE_OP          ">"
                             00000009     6F - JUMP_IF_FALSE       -> 000000E4
                             0000000C     01 - POP_TOP             
                             0000000D     7C - LOAD_FAST           'subject'
                             00000010     69 - LOAD_ATTR           'AbilityInv'
                             00000013     69 - LOAD_ATTR           'addTempMod'
                             00000016     74 - LOAD_GLOBAL         'CoderAbility'
                             00000019     74 - LOAD_GLOBAL         'CodeWritingAbility'
                             0000001C     7C - LOAD_FAST           'buffValue'
                             0000001F     74 - LOAD_GLOBAL         'CODER_DURATION'
                             00000022     83 - CALL_FUNCTION       r0004
                             00000025     01 - POP_TOP             
                             00000026     7C - LOAD_FAST           'subject'
                             00000029     69 - LOAD_ATTR           'AbilityInv'
                             0000002C     69 - LOAD_ATTR           'addTempMod'
                             0000002F     74 - LOAD_GLOBAL         'CoderAbility'
                             00000032     74 - LOAD_GLOBAL         'DecompileSkillAbility'
                             00000035     7C - LOAD_FAST           'buffValue'
                             00000038     74 - LOAD_GLOBAL         'CODER_DURATION'
                             0000003B     83 - CALL_FUNCTION       r0004
                             0000003E     01 - POP_TOP             
                             0000003F     7C - LOAD_FAST           'subject'
                             00000042     69 - LOAD_ATTR           'AbilityInv'
                             00000045     69 - LOAD_ATTR           'addTempMod'
                             00000048     74 - LOAD_GLOBAL         'CoderAbility'
                             0000004B     74 - LOAD_GLOBAL         'AbilityCraftingAbility'
                             0000004E     7C - LOAD_FAST           'buffValue'
                             00000051     74 - LOAD_GLOBAL         'CODER_DURATION'
                             00000054     83 - CALL_FUNCTION       r0004
                             00000057     01 - POP_TOP             
                             00000058     7C - LOAD_FAST           'subject'
                             0000005B     69 - LOAD_ATTR           'AbilityInv'
                             0000005E     69 - LOAD_ATTR           'addTempMod'
                             00000061     74 - LOAD_GLOBAL         'CoderAbility'
                             00000064     74 - LOAD_GLOBAL         'ApparelCraftingAbility'
                             00000067     7C - LOAD_FAST           'buffValue'
                             0000006A     74 - LOAD_GLOBAL         'CODER_DURATION'
                             0000006D     83 - CALL_FUNCTION       r0004
                             00000070     01 - POP_TOP             
                             00000071     7C - LOAD_FAST           'subject'
                             00000074     69 - LOAD_ATTR           'AbilityInv'
                             00000077     69 - LOAD_ATTR           'addTempMod'
                             0000007A     74 - LOAD_GLOBAL         'CoderAbility'
                             0000007D     74 - LOAD_GLOBAL         'ToolCraftingAbility'
                             00000080     7C - LOAD_FAST           'buffValue'
                             00000083     74 - LOAD_GLOBAL         'CODER_DURATION'
                             00000086     83 - CALL_FUNCTION       r0004
                             00000089     01 - POP_TOP             
                             0000008A     7C - LOAD_FAST           'subject'
                             0000008D     69 - LOAD_ATTR           'AbilityInv'
                             00000090     69 - LOAD_ATTR           'addTempMod'
                             00000093     74 - LOAD_GLOBAL         'CoderAbility'
                             00000096     74 - LOAD_GLOBAL         'UpgradeCraftingAbility'
                             00000099     7C - LOAD_FAST           'buffValue'
                             0000009C     74 - LOAD_GLOBAL         'CODER_DURATION'
                             0000009F     83 - CALL_FUNCTION       r0004
                             000000A2     01 - POP_TOP             
                             000000A3     7C - LOAD_FAST           'subject'
                             000000A6     69 - LOAD_ATTR           'AbilityInv'
                             000000A9     69 - LOAD_ATTR           'addTempMod'
                             000000AC     74 - LOAD_GLOBAL         'CoderAbility'
                             000000AF     74 - LOAD_GLOBAL         'WeaponCraftingAbility'
                             000000B2     7C - LOAD_FAST           'buffValue'
                             000000B5     74 - LOAD_GLOBAL         'CODER_DURATION'
                             000000B8     83 - CALL_FUNCTION       r0004
                             000000BB     01 - POP_TOP             
                             000000BC     74 - LOAD_GLOBAL         'ability'
                             000000BF     69 - LOAD_ATTR           'utility'
                             000000C2     69 - LOAD_ATTR           'SendAbilityOutputToCaster'
                             000000C5     74 - LOAD_GLOBAL         'ST'
                             000000C8     69 - LOAD_ATTR           'ID_CLIENT_ABILITY_CODER_SUBJECT'
                             000000CB     74 - LOAD_GLOBAL         'CoderAbility'
                             000000CE     7C - LOAD_FAST           'subject'
                             000000D1     69 - LOAD_ATTR           'locator'
                             000000D4     7C - LOAD_FAST           'subject'
                             000000D7     69 - LOAD_ATTR           'locator'
                             000000DA     7C - LOAD_FAST           'buffValue'
                             000000DD     83 - CALL_FUNCTION       r0005
                             000000E0     01 - POP_TOP             
                             000000E1     6E - JUMP_FORWARD        -> 000000E5
                             000000E4     01 - POP_TOP             
                             000000E5     64 - LOAD_CONST          1
                             000000E8     53 - RETURN_VALUE        
                             000000E9     64 - LOAD_CONST          None
                             000000EC     53 - RETURN_VALUE        
                         consts:
000024D9                     TUPLE: (
000024DE                         None (4E),
000024DF                         INT: 0 (00 00 00 00),
000024E4                         INT: 1 (01 00 00 00)
                             )
                         names:
000024E9                     TUPLE: (
000024EE                         STR: 'buffValue' (09 00 00 00 62 75 66 66 56 61 6C 75 65),
000024FC                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00002508                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
00002517                         STR: 'addTempMod' (0A 00 00 00 61 64 64 54 65 6D 70 4D 6F 64),
00002526                         STR: 'CoderAbility' (0C 00 00 00 43 6F 64 65 72 41 62 69 6C 69 74 79),
00002537                         STR: 'CodeWritingAbility' (12 00 00 00 43 6F 64 65 57 72 69 74 69 6E 67 41 62 69 6C 69 74 79),
0000254E                         STR: 'CODER_DURATION' (0E 00 00 00 43 4F 44 45 52 5F 44 55 52 41 54 49 4F 4E),
00002561                         STR: 'DecompileSkillAbility' (15 00 00 00 44 65 63 6F 6D 70 69 6C 65 53 6B 69 6C 6C 41 62 69 6C 69 74 79),
0000257B                         STR: 'AbilityCraftingAbility' (16 00 00 00 41 62 69 6C 69 74 79 43 72 61 66 74 69 6E 67 41 62 69 6C 69 74 79),
00002596                         STR: 'ApparelCraftingAbility' (16 00 00 00 41 70 70 61 72 65 6C 43 72 61 66 74 69 6E 67 41 62 69 6C 69 74 79),
000025B1                         STR: 'ToolCraftingAbility' (13 00 00 00 54 6F 6F 6C 43 72 61 66 74 69 6E 67 41 62 69 6C 69 74 79),
000025C9                         STR: 'UpgradeCraftingAbility' (16 00 00 00 55 70 67 72 61 64 65 43 72 61 66 74 69 6E 67 41 62 69 6C 69 74 79),
000025E4                         STR: 'WeaponCraftingAbility' (15 00 00 00 57 65 61 70 6F 6E 43 72 61 66 74 69 6E 67 41 62 69 6C 69 74 79),
000025FE                         STR: 'ability' (07 00 00 00 61 62 69 6C 69 74 79),
0000260A                         STR: 'utility' (07 00 00 00 75 74 69 6C 69 74 79),
00002616                         STR: 'SendAbilityOutputToCaster' (19 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 43 61 73 74 65 72),
00002634                         STR: 'ST' (02 00 00 00 53 54),
0000263B                         STR: 'ID_CLIENT_ABILITY_CODER_SUBJECT' (1F 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 41 42 49 4C 49 54 59 5F 43 4F 44 45 52 5F 53 55 42 4A 45 43 54),
0000265F                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72)
                             )
                         varnames:
0000266B                     TUPLE: (
00002670                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000267C                         STR: 'invItem' (07 00 00 00 69 6E 76 49 74 65 6D),
00002688                         STR: 'buffValue' (09 00 00 00 62 75 66 66 56 61 6C 75 65)
                             )
                         freevars:
00002696                     TUPLE: ()
                         cellvars:
0000269B                     TUPLE: ()
                         filename:
000026A0                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\crafting_server.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 72 61 66 74 69 6E 67 5F 73 65 72 76 65 72 2E 70 79)
                         name:
000026EC                     STR: 'CoderApplication' (10 00 00 00 43 6F 64 65 72 41 70 70 6C 69 63 61 74 69 6F 6E)
                         firslineno:
00002701                     LONG: 328L (48 01 00 00)
                         lnotab:
00002705                     STR: '\x00\x01\r\x01\x19\x01\x19\x01\x19\x01\x19\x01\x19\x01\x19\x01\x19\x01\x0f\x01\x03\x01\x06\x01\x06\x01\x0b\x01' (1C 00 00 00 00 01 0D 01 19 01 19 01 19 01 19 01 19 01 19 01 19 01 0F 01 03 01 06 01 06 01 0B 01)
                 )
             names:
00002726         TUPLE: (
0000272B             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00002736             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00002744             STR: 'ability.utility' (0F 00 00 00 61 62 69 6C 69 74 79 2E 75 74 69 6C 69 74 79),
00002758             STR: 'ability' (07 00 00 00 61 62 69 6C 69 74 79),
00002764             STR: 'obj' (03 00 00 00 6F 62 6A),
0000276C             STR: 'stringtable_client' (12 00 00 00 73 74 72 69 6E 67 74 61 62 6C 65 5F 63 6C 69 65 6E 74),
00002783             STR: 'ST' (02 00 00 00 53 54),
0000278A             STR: 'RewardSelection' (0F 00 00 00 52 65 77 61 72 64 53 65 6C 65 63 74 69 6F 6E),
0000279E             STR: 'ltfxmap' (07 00 00 00 6C 74 66 78 6D 61 70),
000027AA             STR: 'FX' (02 00 00 00 46 58),
000027B1             STR: 'COMPILE_DISCOUNT' (10 00 00 00 43 4F 4D 50 49 4C 45 5F 44 49 53 43 4F 55 4E 54),
000027C6             STR: 'CODER_DURATION' (0E 00 00 00 43 4F 44 45 52 5F 44 55 52 41 54 49 4F 4E),
000027D9             STR: 'craftingFeedback' (10 00 00 00 63 72 61 66 74 69 6E 67 46 65 65 64 62 61 63 6B),
000027EE             STR: 'isPill' (06 00 00 00 69 73 50 69 6C 6C),
000027F9             STR: 'gD100' (05 00 00 00 67 44 31 30 30),
00002803             STR: 'stdDev' (06 00 00 00 73 74 64 44 65 76),
0000280E             STR: 'toFourCC' (08 00 00 00 74 6F 46 6F 75 72 43 43),
0000281B             STR: 'DecompileInnerStrengthCost' (1A 00 00 00 44 65 63 6F 6D 70 69 6C 65 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 43 6F 73 74),
0000283A             STR: 'DecompStabPurContrib' (14 00 00 00 44 65 63 6F 6D 70 53 74 61 62 50 75 72 43 6F 6E 74 72 69 62),
00002853             STR: 'DecompileTest' (0D 00 00 00 44 65 63 6F 6D 70 69 6C 65 54 65 73 74),
00002865             STR: 'DecompileFragmentRecoveryTest' (1D 00 00 00 44 65 63 6F 6D 70 69 6C 65 46 72 61 67 6D 65 6E 74 52 65 63 6F 76 65 72 79 54 65 73 74),
00002887             STR: 'CompileInfoCost' (0F 00 00 00 43 6F 6D 70 69 6C 65 49 6E 66 6F 43 6F 73 74),
0000289B             STR: 'GetAbilityBonusByCategory' (19 00 00 00 47 65 74 41 62 69 6C 69 74 79 42 6F 6E 75 73 42 79 43 61 74 65 67 6F 72 79),
000028B9             STR: 'CalcItemInfoCost' (10 00 00 00 43 61 6C 63 49 74 65 6D 49 6E 66 6F 43 6F 73 74),
000028CE             STR: 'CompileTest' (0B 00 00 00 43 6F 6D 70 69 6C 65 54 65 73 74),
000028DE             STR: 'WriteCodeTest' (0D 00 00 00 57 72 69 74 65 43 6F 64 65 54 65 73 74),
000028F0             STR: 'CoderApplication' (10 00 00 00 43 6F 64 65 72 41 70 70 6C 69 63 61 74 69 6F 6E)
                 )
             varnames:
00002905         TUPLE: (
0000290A             STR: 'DecompStabPurContrib' (14 00 00 00 44 65 63 6F 6D 70 53 74 61 62 50 75 72 43 6F 6E 74 72 69 62),
00002923             STR: 'FX' (02 00 00 00 46 58),
0000292A             STR: 'DecompileTest' (0D 00 00 00 44 65 63 6F 6D 70 69 6C 65 54 65 73 74),
0000293C             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00002947             STR: 'DecompileInnerStrengthCost' (1A 00 00 00 44 65 63 6F 6D 70 69 6C 65 49 6E 6E 65 72 53 74 72 65 6E 67 74 68 43 6F 73 74),
00002966             STR: 'COMPILE_DISCOUNT' (10 00 00 00 43 4F 4D 50 49 4C 45 5F 44 49 53 43 4F 55 4E 54),
0000297B             STR: 'CalcItemInfoCost' (10 00 00 00 43 61 6C 63 49 74 65 6D 49 6E 66 6F 43 6F 73 74),
00002990             STR: 'isPill' (06 00 00 00 69 73 50 69 6C 6C),
0000299B             STR: 'CompileInfoCost' (0F 00 00 00 43 6F 6D 70 69 6C 65 49 6E 66 6F 43 6F 73 74),
000029AF             STR: 'CompileTest' (0B 00 00 00 43 6F 6D 70 69 6C 65 54 65 73 74),
000029BF             STR: 'ability' (07 00 00 00 61 62 69 6C 69 74 79),
000029CB             STR: 'CoderApplication' (10 00 00 00 43 6F 64 65 72 41 70 70 6C 69 63 61 74 69 6F 6E),
000029E0             STR: 'WriteCodeTest' (0D 00 00 00 57 72 69 74 65 43 6F 64 65 54 65 73 74),
000029F2             STR: 'DecompileFragmentRecoveryTest' (1D 00 00 00 44 65 63 6F 6D 70 69 6C 65 46 72 61 67 6D 65 6E 74 52 65 63 6F 76 65 72 79 54 65 73 74),
00002A14             STR: 'GetAbilityBonusByCategory' (19 00 00 00 47 65 74 41 62 69 6C 69 74 79 42 6F 6E 75 73 42 79 43 61 74 65 67 6F 72 79),
00002A32             STR: 'CODER_DURATION' (0E 00 00 00 43 4F 44 45 52 5F 44 55 52 41 54 49 4F 4E),
00002A45             STR: 'obj' (03 00 00 00 6F 62 6A),
00002A4D             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00002A5B             STR: 'ST' (02 00 00 00 53 54),
00002A62             STR: 'craftingFeedback' (10 00 00 00 63 72 61 66 74 69 6E 67 46 65 65 64 62 61 63 6B),
00002A77             STR: 'gD100' (05 00 00 00 67 44 31 30 30),
00002A81             STR: 'toFourCC' (08 00 00 00 74 6F 46 6F 75 72 43 43),
00002A8E             STR: 'RewardSelection' (0F 00 00 00 52 65 77 61 72 64 53 65 6C 65 63 74 69 6F 6E)
                 )
             freevars:
00002AA2         TUPLE: ()
             cellvars:
00002AA7         TUPLE: ()
             filename:
00002AAC         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\crafting_server.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 72 61 66 74 69 6E 67 5F 73 65 72 76 65 72 2E 70 79)
             name:
00002AF8         STR: '?' (01 00 00 00 3F)
             firslineno:
00002AFE         LONG: 7L (07 00 00 00)
             lnotab:
00002B02         STR: '\t\x01\t\x01\t\x01\t\x02\t\x01\r\x01\t\x05\x06\x01\x06\x03\t\x07\t\t\t\x03\t\x05\t\x0b\t\x06\t\x15\t\'\t"\t\t\t\x15\t\x1e\t9\t5' (2E 00 00 00 09 01 09 01 09 01 09 02 09 01 0D 01 09 05 06 01 06 03 09 07 09 09 09 03 09 05 09 0B 09 06 09 15 09 27 09 22 09 09 09 15 09 1E 09 39 09 35)

