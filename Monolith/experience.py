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
00000019         STR: 'h\x00\x00Z\x00\x00h\x00\x00Z\x01\x00d\x00\x00\x84\x00\x00Z\x02\x00d\x01\x00\x84\x00\x00Z\x03\x00d\x02\x00\x84\x00\x00Z\x04\x00d\x03\x00\x84\x00\x00Z\x05\x00d\x04\x00\x84\x00\x00Z\x06\x00e\x07\x00i\x08\x00i\t\x00d\x05\x00\x84\x01\x00Z\n\x00d\x06\x00S' (4F 00 00 00 68 00 00 5A 00 00 68 00 00 5A 01 00 64 00 00 84 00 00 5A 02 00 64 01 00 84 00 00 5A 03 00 64 02 00 84 00 00 5A 04 00 64 03 00 84 00 00 5A 05 00 64 04 00 84 00 00 5A 06 00 65 07 00 69 08 00 69 09 00 64 05 00 84 01 00 5A 0A 00 64 06 00 53)
                 00000000     68 - BUILD_MAP           r0000
                 00000003     5A - STORE_NAME          'experienceBaseMap'
                 00000006     68 - BUILD_MAP           r0000
                 00000009     5A - STORE_NAME          'groupXPMap'
                 0000000C     64 - LOAD_CONST          CODE('Init')
                 0000000F     84 - MAKE_FUNCTION       r0000
                 00000012     5A - STORE_NAME          'Init'
                 00000015     64 - LOAD_CONST          CODE('ComputeExperience')
                 00000018     84 - MAKE_FUNCTION       r0000
                 0000001B     5A - STORE_NAME          'ComputeExperience'
                 0000001E     64 - LOAD_CONST          CODE('ComputeGroupBonus')
                 00000021     84 - MAKE_FUNCTION       r0000
                 00000024     5A - STORE_NAME          'ComputeGroupBonus'
                 00000027     64 - LOAD_CONST          CODE('ComputeExperienceDecompile')
                 0000002A     84 - MAKE_FUNCTION       r0000
                 0000002D     5A - STORE_NAME          'ComputeExperienceDecompile'
                 00000030     64 - LOAD_CONST          CODE('ComputeExperienceWriteCode')
                 00000033     84 - MAKE_FUNCTION       r0000
                 00000036     5A - STORE_NAME          'ComputeExperienceWriteCode'
                 00000039     65 - LOAD_NAME           'constants'
                 0000003C     69 - LOAD_ATTR           'AI'
                 0000003F     69 - LOAD_ATTR           'WEAKLING'
                 00000042     64 - LOAD_CONST          CODE('ComputeGenericExperience')
                 00000045     84 - MAKE_FUNCTION       r0001
                 00000048     5A - STORE_NAME          'ComputeGenericExperience'
                 0000004B     64 - LOAD_CONST          None
                 0000004E     53 - RETURN_VALUE        
             consts:
0000006D         TUPLE: (
00000072             CODE:
                         argcount:
00000073                     LONG: 0L (00 00 00 00)
                         nlocals:
00000077                     LONG: 0L (00 00 00 00)
                         stacksize:
0000007B                     LONG: 3L (03 00 00 00)
                         flags:
0000007F                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000083                     STR: 't\x00\x00i\x01\x00t\x02\x00t\x03\x00i\x04\x00i\x05\x00<t\x00\x00i\x06\x00t\x02\x00t\x03\x00i\x04\x00i\x07\x00<t\x00\x00i\x08\x00t\x02\x00t\x03\x00i\x04\x00i\t\x00<d\x01\x00t\n\x00d\x02\x00<d\x03\x00t\n\x00d\x04\x00<d\x05\x00t\n\x00d\x06\x00<d\x07\x00t\n\x00d\x08\x00<d\t\x00t\n\x00d\n\x00<d\x0b\x00t\n\x00d\x0c\x00<d\r\x00GHd\x00\x00S' (7E 00 00 00 74 00 00 69 01 00 74 02 00 74 03 00 69 04 00 69 05 00 3C 74 00 00 69 06 00 74 02 00 74 03 00 69 04 00 69 07 00 3C 74 00 00 69 08 00 74 02 00 74 03 00 69 04 00 69 09 00 3C 64 01 00 74 0A 00 64 02 00 3C 64 03 00 74 0A 00 64 04 00 3C 64 05 00 74 0A 00 64 06 00 3C 64 07 00 74 0A 00 64 08 00 3C 64 09 00 74 0A 00 64 0A 00 3C 64 0B 00 74 0A 00 64 0C 00 3C 64 0D 00 47 48 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consolevar'
                             00000003     69 - LOAD_ATTR           'WeaklingKillMultiplier'
                             00000006     74 - LOAD_GLOBAL         'experienceBaseMap'
                             00000009     74 - LOAD_GLOBAL         'constants'
                             0000000C     69 - LOAD_ATTR           'AI'
                             0000000F     69 - LOAD_ATTR           'WEAKLING'
                             00000012     3C - STORE_SUBSCR        
                             00000013     74 - LOAD_GLOBAL         'consolevar'
                             00000016     69 - LOAD_ATTR           'ToughKillMultiplier'
                             00000019     74 - LOAD_GLOBAL         'experienceBaseMap'
                             0000001C     74 - LOAD_GLOBAL         'constants'
                             0000001F     69 - LOAD_ATTR           'AI'
                             00000022     69 - LOAD_ATTR           'TOUGH'
                             00000025     3C - STORE_SUBSCR        
                             00000026     74 - LOAD_GLOBAL         'consolevar'
                             00000029     69 - LOAD_ATTR           'BossKillMultiplier'
                             0000002C     74 - LOAD_GLOBAL         'experienceBaseMap'
                             0000002F     74 - LOAD_GLOBAL         'constants'
                             00000032     69 - LOAD_ATTR           'AI'
                             00000035     69 - LOAD_ATTR           'BOSS'
                             00000038     3C - STORE_SUBSCR        
                             00000039     64 - LOAD_CONST          1.0
                             0000003C     74 - LOAD_GLOBAL         'groupXPMap'
                             0000003F     64 - LOAD_CONST          1
                             00000042     3C - STORE_SUBSCR        
                             00000043     64 - LOAD_CONST          1.2
                             00000046     74 - LOAD_GLOBAL         'groupXPMap'
                             00000049     64 - LOAD_CONST          2
                             0000004C     3C - STORE_SUBSCR        
                             0000004D     64 - LOAD_CONST          1.5
                             00000050     74 - LOAD_GLOBAL         'groupXPMap'
                             00000053     64 - LOAD_CONST          3
                             00000056     3C - STORE_SUBSCR        
                             00000057     64 - LOAD_CONST          1.6000000000000001
                             0000005A     74 - LOAD_GLOBAL         'groupXPMap'
                             0000005D     64 - LOAD_CONST          4
                             00000060     3C - STORE_SUBSCR        
                             00000061     64 - LOAD_CONST          1.75
                             00000064     74 - LOAD_GLOBAL         'groupXPMap'
                             00000067     64 - LOAD_CONST          5
                             0000006A     3C - STORE_SUBSCR        
                             0000006B     64 - LOAD_CONST          2.1000000000000001
                             0000006E     74 - LOAD_GLOBAL         'groupXPMap'
                             00000071     64 - LOAD_CONST          6
                             00000074     3C - STORE_SUBSCR        
                             00000075     64 - LOAD_CONST          'Experience system Inited'
                             00000078     47 - PRINT_ITEM          
                             00000079     48 - PRINT_NEWLINE       
                             0000007A     64 - LOAD_CONST          None
                             0000007D     53 - RETURN_VALUE        
                         consts:
00000106                     TUPLE: (
0000010B                         None (4E),
0000010C                         FLOAT: 1.0 (03 31 2E 30),
00000111                         INT: 1 (01 00 00 00),
00000116                         FLOAT: 1.2 (03 31 2E 32),
0000011B                         INT: 2 (02 00 00 00),
00000120                         FLOAT: 1.5 (03 31 2E 35),
00000125                         INT: 3 (03 00 00 00),
0000012A                         FLOAT: 1.6000000000000001 (12 31 2E 36 30 30 30 30 30 30 30 30 30 30 30 30 30 30 31),
0000013E                         INT: 4 (04 00 00 00),
00000143                         FLOAT: 1.75 (04 31 2E 37 35),
00000149                         INT: 5 (05 00 00 00),
0000014E                         FLOAT: 2.1000000000000001 (12 32 2E 31 30 30 30 30 30 30 30 30 30 30 30 30 30 30 31),
00000162                         INT: 6 (06 00 00 00),
00000167                         STR: 'Experience system Inited' (18 00 00 00 45 78 70 65 72 69 65 6E 63 65 20 73 79 73 74 65 6D 20 49 6E 69 74 65 64)
                             )
                         names:
00000184                     TUPLE: (
00000189                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
00000198                         STR: 'WeaklingKillMultiplier' (16 00 00 00 57 65 61 6B 6C 69 6E 67 4B 69 6C 6C 4D 75 6C 74 69 70 6C 69 65 72),
000001B3                         STR: 'experienceBaseMap' (11 00 00 00 65 78 70 65 72 69 65 6E 63 65 42 61 73 65 4D 61 70),
000001C9                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
000001D7                         STR: 'AI' (02 00 00 00 41 49),
000001DE                         STR: 'WEAKLING' (08 00 00 00 57 45 41 4B 4C 49 4E 47),
000001EB                         STR: 'ToughKillMultiplier' (13 00 00 00 54 6F 75 67 68 4B 69 6C 6C 4D 75 6C 74 69 70 6C 69 65 72),
00000203                         STR: 'TOUGH' (05 00 00 00 54 4F 55 47 48),
0000020D                         STR: 'BossKillMultiplier' (12 00 00 00 42 6F 73 73 4B 69 6C 6C 4D 75 6C 74 69 70 6C 69 65 72),
00000224                         STR: 'BOSS' (04 00 00 00 42 4F 53 53),
0000022D                         STR: 'groupXPMap' (0A 00 00 00 67 72 6F 75 70 58 50 4D 61 70)
                             )
                         varnames:
0000023C                     TUPLE: ()
                         freevars:
00000241                     TUPLE: ()
                         cellvars:
00000246                     TUPLE: ()
                         filename:
0000024B                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\experience.py' (42 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 65 78 70 65 72 69 65 6E 63 65 2E 70 79)
                         name:
00000292                     STR: 'Init' (04 00 00 00 49 6E 69 74)
                         firslineno:
0000029B                     LONG: 4L (04 00 00 00)
                         lnotab:
0000029F                     STR: '\x00\x01\x13\x01\x13\x01\x13\x02\n\x01\n\x01\n\x01\n\x01\n\x01\n\x02' (14 00 00 00 00 01 13 01 13 01 13 02 0A 01 0A 01 0A 01 0A 01 0A 01 0A 02),
000002B8             CODE:
                         argcount:
000002B9                     LONG: 4L (04 00 00 00)
                         nlocals:
000002BD                     LONG: 10L (0A 00 00 00)
                         stacksize:
000002C1                     LONG: 4L (04 00 00 00)
                         flags:
000002C5                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000002C9                     STR: '|\x00\x00i\x01\x00t\x02\x00j\x08\x00o\x08\x00\x01t\x02\x00Sn\x01\x00\x01|\x00\x00i\x03\x00o\x0e\x00\x01t\x04\x00d\x01\x00\x83\x01\x00Sn\x01\x00\x01t\x05\x00i\x01\x00i\x06\x00}\x08\x00|\x00\x00i\x01\x00i\x07\x00t\x02\x00j\t\x00o\x13\x00\x01t\x08\x00i\t\x00|\x00\x00i\x01\x00i\x07\x00\x83\x01\x00o\x10\x00\x01|\x00\x00i\x01\x00i\x07\x00}\x08\x00n\x01\x00\x01|\x02\x00|\x03\x00\x15}\x06\x00d\x02\x00|\x00\x00i\r\x00i\x0e\x00|\x01\x00\x18\x17}\x05\x00|\x05\x00d\x03\x00\x15}\x04\x00t\x08\x00|\x08\x00\x19}\t\x00|\t\x00t\x13\x00d\x04\x00|\x04\x00\x83\x02\x00\x14|\x06\x00\x14}\x07\x00|\x01\x00d\x02\x00j\x03\x00o\x0e\x00\x01|\x01\x00d\x02\x00\x18}\x01\x00n\x01\x00\x01|\x07\x00t\x15\x00i\x16\x00|\x01\x00|\x07\x00\x14t\x15\x00i\x17\x00\x14|\x07\x00\x18\x14\x17}\x07\x00t\x04\x00|\x07\x00\x83\x01\x00Sd\x00\x00S' (07 01 00 00 7C 00 00 69 01 00 74 02 00 6A 08 00 6F 08 00 01 74 02 00 53 6E 01 00 01 7C 00 00 69 03 00 6F 0E 00 01 74 04 00 64 01 00 83 01 00 53 6E 01 00 01 74 05 00 69 01 00 69 06 00 7D 08 00 7C 00 00 69 01 00 69 07 00 74 02 00 6A 09 00 6F 13 00 01 74 08 00 69 09 00 7C 00 00 69 01 00 69 07 00 83 01 00 6F 10 00 01 7C 00 00 69 01 00 69 07 00 7D 08 00 6E 01 00 01 7C 02 00 7C 03 00 15 7D 06 00 64 02 00 7C 00 00 69 0D 00 69 0E 00 7C 01 00 18 17 7D 05 00 7C 05 00 64 03 00 15 7D 04 00 74 08 00 7C 08 00 19 7D 09 00 7C 09 00 74 13 00 64 04 00 7C 04 00 83 02 00 14 7C 06 00 14 7D 07 00 7C 01 00 64 02 00 6A 03 00 6F 0E 00 01 7C 01 00 64 02 00 18 7D 01 00 6E 01 00 01 7C 07 00 74 15 00 69 16 00 7C 01 00 7C 07 00 14 74 15 00 69 17 00 14 7C 07 00 18 14 17 7D 07 00 74 04 00 7C 07 00 83 01 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'pParent'
                             00000003     69 - LOAD_ATTR           'AI'
                             00000006     74 - LOAD_GLOBAL         'None'
                             00000009     6A - COMPARE_OP          "is"
                             0000000C     6F - JUMP_IF_FALSE       -> 00000017
                             0000000F     01 - POP_TOP             
                             00000010     74 - LOAD_GLOBAL         'None'
                             00000013     53 - RETURN_VALUE        
                             00000014     6E - JUMP_FORWARD        -> 00000018
                             00000017     01 - POP_TOP             
                             00000018     7C - LOAD_FAST           'pParent'
                             0000001B     69 - LOAD_ATTR           'OwnerCharacterID'
                             0000001E     6F - JUMP_IF_FALSE       -> 0000002F
                             00000021     01 - POP_TOP             
                             00000022     74 - LOAD_GLOBAL         'float'
                             00000025     64 - LOAD_CONST          0
                             00000028     83 - CALL_FUNCTION       r0001
                             0000002B     53 - RETURN_VALUE        
                             0000002C     6E - JUMP_FORWARD        -> 00000030
                             0000002F     01 - POP_TOP             
                             00000030     74 - LOAD_GLOBAL         'constants'
                             00000033     69 - LOAD_ATTR           'AI'
                             00000036     69 - LOAD_ATTR           'WEAKLING'
                             00000039     7D - STORE_FAST          'NPCRank'
                             0000003C     7C - LOAD_FAST           'pParent'
                             0000003F     69 - LOAD_ATTR           'AI'
                             00000042     69 - LOAD_ATTR           'NPCRank'
                             00000045     74 - LOAD_GLOBAL         'None'
                             00000048     6A - COMPARE_OP          "is not"
                             0000004B     6F - JUMP_IF_FALSE       -> 00000061
                             0000004E     01 - POP_TOP             
                             0000004F     74 - LOAD_GLOBAL         'experienceBaseMap'
                             00000052     69 - LOAD_ATTR           'has_key'
                             00000055     7C - LOAD_FAST           'pParent'
                             00000058     69 - LOAD_ATTR           'AI'
                             0000005B     69 - LOAD_ATTR           'NPCRank'
                             0000005E     83 - CALL_FUNCTION       r0001
                             00000061     6F - JUMP_IF_FALSE       -> 00000074
                             00000064     01 - POP_TOP             
                             00000065     7C - LOAD_FAST           'pParent'
                             00000068     69 - LOAD_ATTR           'AI'
                             0000006B     69 - LOAD_ATTR           'NPCRank'
                             0000006E     7D - STORE_FAST          'NPCRank'
                             00000071     6E - JUMP_FORWARD        -> 00000075
                             00000074     01 - POP_TOP             
                             00000075     7C - LOAD_FAST           'playerDamage'
                             00000078     7C - LOAD_FAST           'totalDamage'
                             0000007B     15 - BINARY_DIVIDE       
                             0000007C     7D - STORE_FAST          'percent'
                             0000007F     64 - LOAD_CONST          1
                             00000082     7C - LOAD_FAST           'pParent'
                             00000085     69 - LOAD_ATTR           'CharacterBase'
                             00000088     69 - LOAD_ATTR           'Level'
                             0000008B     7C - LOAD_FAST           'playerLevel'
                             0000008E     18 - BINARY_SUBTRACT     
                             0000008F     17 - BINARY_ADD          
                             00000090     7D - STORE_FAST          'numerator'
                             00000093     7C - LOAD_FAST           'numerator'
                             00000096     64 - LOAD_CONST          7
                             00000099     15 - BINARY_DIVIDE       
                             0000009A     7D - STORE_FAST          'exponent'
                             0000009D     74 - LOAD_GLOBAL         'experienceBaseMap'
                             000000A0     7C - LOAD_FAST           'NPCRank'
                             000000A3     19 - BINARY_SUBSCR       
                             000000A4     7D - STORE_FAST          'rankConstant'
                             000000A7     7C - LOAD_FAST           'rankConstant'
                             000000AA     74 - LOAD_GLOBAL         'pow'
                             000000AD     64 - LOAD_CONST          3
                             000000B0     7C - LOAD_FAST           'exponent'
                             000000B3     83 - CALL_FUNCTION       r0002
                             000000B6     14 - BINARY_MULTIPLY     
                             000000B7     7C - LOAD_FAST           'percent'
                             000000BA     14 - BINARY_MULTIPLY     
                             000000BB     7D - STORE_FAST          'experience'
                             000000BE     7C - LOAD_FAST           'playerLevel'
                             000000C1     64 - LOAD_CONST          1
                             000000C4     6A - COMPARE_OP          "!="
                             000000C7     6F - JUMP_IF_FALSE       -> 000000D8
                             000000CA     01 - POP_TOP             
                             000000CB     7C - LOAD_FAST           'playerLevel'
                             000000CE     64 - LOAD_CONST          1
                             000000D1     18 - BINARY_SUBTRACT     
                             000000D2     7D - STORE_FAST          'playerLevel'
                             000000D5     6E - JUMP_FORWARD        -> 000000D9
                             000000D8     01 - POP_TOP             
                             000000D9     7C - LOAD_FAST           'experience'
                             000000DC     74 - LOAD_GLOBAL         'consolevar'
                             000000DF     69 - LOAD_ATTR           'XPKnob'
                             000000E2     7C - LOAD_FAST           'playerLevel'
                             000000E5     7C - LOAD_FAST           'experience'
                             000000E8     14 - BINARY_MULTIPLY     
                             000000E9     74 - LOAD_GLOBAL         'consolevar'
                             000000EC     69 - LOAD_ATTR           'XPConstantMultiplier'
                             000000EF     14 - BINARY_MULTIPLY     
                             000000F0     7C - LOAD_FAST           'experience'
                             000000F3     18 - BINARY_SUBTRACT     
                             000000F4     14 - BINARY_MULTIPLY     
                             000000F5     17 - BINARY_ADD          
                             000000F6     7D - STORE_FAST          'experience'
                             000000F9     74 - LOAD_GLOBAL         'float'
                             000000FC     7C - LOAD_FAST           'experience'
                             000000FF     83 - CALL_FUNCTION       r0001
                             00000102     53 - RETURN_VALUE        
                             00000103     64 - LOAD_CONST          None
                             00000106     53 - RETURN_VALUE        
                         consts:
000003D5                     TUPLE: (
000003DA                         None (4E),
000003DB                         INT: 0 (00 00 00 00),
000003E0                         INT: 1 (01 00 00 00),
000003E5                         INT: 7 (07 00 00 00),
000003EA                         INT: 3 (03 00 00 00)
                             )
                         names:
000003EF                     TUPLE: (
000003F4                         STR: 'pParent' (07 00 00 00 70 50 61 72 65 6E 74),
00000400                         STR: 'AI' (02 00 00 00 41 49),
00000407                         STR: 'None' (04 00 00 00 4E 6F 6E 65),
00000410                         STR: 'OwnerCharacterID' (10 00 00 00 4F 77 6E 65 72 43 68 61 72 61 63 74 65 72 49 44),
00000425                         STR: 'float' (05 00 00 00 66 6C 6F 61 74),
0000042F                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
0000043D                         STR: 'WEAKLING' (08 00 00 00 57 45 41 4B 4C 49 4E 47),
0000044A                         STR: 'NPCRank' (07 00 00 00 4E 50 43 52 61 6E 6B),
00000456                         STR: 'experienceBaseMap' (11 00 00 00 65 78 70 65 72 69 65 6E 63 65 42 61 73 65 4D 61 70),
0000046C                         STR: 'has_key' (07 00 00 00 68 61 73 5F 6B 65 79),
00000478                         STR: 'playerDamage' (0C 00 00 00 70 6C 61 79 65 72 44 61 6D 61 67 65),
00000489                         STR: 'totalDamage' (0B 00 00 00 74 6F 74 61 6C 44 61 6D 61 67 65),
00000499                         STR: 'percent' (07 00 00 00 70 65 72 63 65 6E 74),
000004A5                         STR: 'CharacterBase' (0D 00 00 00 43 68 61 72 61 63 74 65 72 42 61 73 65),
000004B7                         STR: 'Level' (05 00 00 00 4C 65 76 65 6C),
000004C1                         STR: 'playerLevel' (0B 00 00 00 70 6C 61 79 65 72 4C 65 76 65 6C),
000004D1                         STR: 'numerator' (09 00 00 00 6E 75 6D 65 72 61 74 6F 72),
000004DF                         STR: 'exponent' (08 00 00 00 65 78 70 6F 6E 65 6E 74),
000004EC                         STR: 'rankConstant' (0C 00 00 00 72 61 6E 6B 43 6F 6E 73 74 61 6E 74),
000004FD                         STR: 'pow' (03 00 00 00 70 6F 77),
00000505                         STR: 'experience' (0A 00 00 00 65 78 70 65 72 69 65 6E 63 65),
00000514                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
00000523                         STR: 'XPKnob' (06 00 00 00 58 50 4B 6E 6F 62),
0000052E                         STR: 'XPConstantMultiplier' (14 00 00 00 58 50 43 6F 6E 73 74 61 6E 74 4D 75 6C 74 69 70 6C 69 65 72)
                             )
                         varnames:
00000547                     TUPLE: (
0000054C                         STR: 'pParent' (07 00 00 00 70 50 61 72 65 6E 74),
00000558                         STR: 'playerLevel' (0B 00 00 00 70 6C 61 79 65 72 4C 65 76 65 6C),
00000568                         STR: 'playerDamage' (0C 00 00 00 70 6C 61 79 65 72 44 61 6D 61 67 65),
00000579                         STR: 'totalDamage' (0B 00 00 00 74 6F 74 61 6C 44 61 6D 61 67 65),
00000589                         STR: 'exponent' (08 00 00 00 65 78 70 6F 6E 65 6E 74),
00000596                         STR: 'numerator' (09 00 00 00 6E 75 6D 65 72 61 74 6F 72),
000005A4                         STR: 'percent' (07 00 00 00 70 65 72 63 65 6E 74),
000005B0                         STR: 'experience' (0A 00 00 00 65 78 70 65 72 69 65 6E 63 65),
000005BF                         STR: 'NPCRank' (07 00 00 00 4E 50 43 52 61 6E 6B),
000005CB                         STR: 'rankConstant' (0C 00 00 00 72 61 6E 6B 43 6F 6E 73 74 61 6E 74)
                             )
                         freevars:
000005DC                     TUPLE: ()
                         cellvars:
000005E1                     TUPLE: ()
                         filename:
000005E6                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\experience.py' (42 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 65 78 70 65 72 69 65 6E 63 65 2E 70 79)
                         name:
0000062D                     STR: 'ComputeExperience' (11 00 00 00 43 6F 6D 70 75 74 65 45 78 70 65 72 69 65 6E 63 65)
                         firslineno:
00000643                     LONG: 18L (12 00 00 00)
                         lnotab:
00000647                     STR: '\x00\x04\x10\x01\x08\x03\n\x01\x0e\x03\x0c\x01)\x01\x10\x04\n\x02\x14\x02\n\x02\n\x02\x17\x02\r\x01\x0e\x02 \x02' (20 00 00 00 00 04 10 01 08 03 0A 01 0E 03 0C 01 29 01 10 04 0A 02 14 02 0A 02 0A 02 17 02 0D 01 0E 02 20 02),
0000066C             CODE:
                         argcount:
0000066D                     LONG: 2L (02 00 00 00)
                         nlocals:
00000671                     LONG: 3L (03 00 00 00)
                         stacksize:
00000675                     LONG: 3L (03 00 00 00)
                         flags:
00000679                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000067D                     STR: '|\x00\x00}\x02\x00t\x02\x00i\x03\x00|\x01\x00\x83\x01\x00o\x12\x00\x01|\x00\x00t\x02\x00|\x01\x00\x19\x14}\x02\x00n\x01\x00\x01t\x05\x00|\x02\x00\x83\x01\x00Sd\x00\x00S' (36 00 00 00 7C 00 00 7D 02 00 74 02 00 69 03 00 7C 01 00 83 01 00 6F 12 00 01 7C 00 00 74 02 00 7C 01 00 19 14 7D 02 00 6E 01 00 01 74 05 00 7C 02 00 83 01 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'currentExperience'
                             00000003     7D - STORE_FAST          'experience'
                             00000006     74 - LOAD_GLOBAL         'groupXPMap'
                             00000009     69 - LOAD_ATTR           'has_key'
                             0000000C     7C - LOAD_FAST           'numberPlayers'
                             0000000F     83 - CALL_FUNCTION       r0001
                             00000012     6F - JUMP_IF_FALSE       -> 00000027
                             00000015     01 - POP_TOP             
                             00000016     7C - LOAD_FAST           'currentExperience'
                             00000019     74 - LOAD_GLOBAL         'groupXPMap'
                             0000001C     7C - LOAD_FAST           'numberPlayers'
                             0000001F     19 - BINARY_SUBSCR       
                             00000020     14 - BINARY_MULTIPLY     
                             00000021     7D - STORE_FAST          'experience'
                             00000024     6E - JUMP_FORWARD        -> 00000028
                             00000027     01 - POP_TOP             
                             00000028     74 - LOAD_GLOBAL         'float'
                             0000002B     7C - LOAD_FAST           'experience'
                             0000002E     83 - CALL_FUNCTION       r0001
                             00000031     53 - RETURN_VALUE        
                             00000032     64 - LOAD_CONST          None
                             00000035     53 - RETURN_VALUE        
                         consts:
000006B8                     TUPLE: (
000006BD                         None (4E)
                             )
                         names:
000006BE                     TUPLE: (
000006C3                         STR: 'currentExperience' (11 00 00 00 63 75 72 72 65 6E 74 45 78 70 65 72 69 65 6E 63 65),
000006D9                         STR: 'experience' (0A 00 00 00 65 78 70 65 72 69 65 6E 63 65),
000006E8                         STR: 'groupXPMap' (0A 00 00 00 67 72 6F 75 70 58 50 4D 61 70),
000006F7                         STR: 'has_key' (07 00 00 00 68 61 73 5F 6B 65 79),
00000703                         STR: 'numberPlayers' (0D 00 00 00 6E 75 6D 62 65 72 50 6C 61 79 65 72 73),
00000715                         STR: 'float' (05 00 00 00 66 6C 6F 61 74)
                             )
                         varnames:
0000071F                     TUPLE: (
00000724                         STR: 'currentExperience' (11 00 00 00 63 75 72 72 65 6E 74 45 78 70 65 72 69 65 6E 63 65),
0000073A                         STR: 'numberPlayers' (0D 00 00 00 6E 75 6D 62 65 72 50 6C 61 79 65 72 73),
0000074C                         STR: 'experience' (0A 00 00 00 65 78 70 65 72 69 65 6E 63 65)
                             )
                         freevars:
0000075B                     TUPLE: ()
                         cellvars:
00000760                     TUPLE: ()
                         filename:
00000765                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\experience.py' (42 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 65 78 70 65 72 69 65 6E 63 65 2E 70 79)
                         name:
000007AC                     STR: 'ComputeGroupBonus' (11 00 00 00 43 6F 6D 70 75 74 65 47 72 6F 75 70 42 6F 6E 75 73)
                         firslineno:
000007C2                     LONG: 56L (38 00 00 00)
                         lnotab:
000007C6                     STR: '\x00\x02\x06\x02\x10\x01\x12\x02' (08 00 00 00 00 02 06 02 10 01 12 02),
000007D3             CODE:
                         argcount:
000007D4                     LONG: 2L (02 00 00 00)
                         nlocals:
000007D8                     LONG: 6L (06 00 00 00)
                         stacksize:
000007DC                     LONG: 4L (04 00 00 00)
                         flags:
000007E0                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000007E4                     STR: 'd\x01\x00|\x01\x00|\x00\x00\x18\x17}\x04\x00|\x04\x00d\x02\x00\x15}\x03\x00t\x04\x00t\x05\x00i\x06\x00i\x07\x00\x19}\x02\x00|\x02\x00t\t\x00d\x03\x00|\x03\x00\x83\x02\x00\x14}\x05\x00|\x00\x00d\x01\x00j\x03\x00o\x0e\x00\x01|\x00\x00d\x01\x00\x18}\x00\x00n\x01\x00\x01|\x05\x00t\x0b\x00i\x0c\x00|\x00\x00|\x05\x00\x14t\x0b\x00i\r\x00\x14|\x05\x00\x18\x14\x17}\x05\x00t\x0e\x00|\x05\x00\x83\x01\x00Sd\x00\x00S' (84 00 00 00 64 01 00 7C 01 00 7C 00 00 18 17 7D 04 00 7C 04 00 64 02 00 15 7D 03 00 74 04 00 74 05 00 69 06 00 69 07 00 19 7D 02 00 7C 02 00 74 09 00 64 03 00 7C 03 00 83 02 00 14 7D 05 00 7C 00 00 64 01 00 6A 03 00 6F 0E 00 01 7C 00 00 64 01 00 18 7D 00 00 6E 01 00 01 7C 05 00 74 0B 00 69 0C 00 7C 00 00 7C 05 00 14 74 0B 00 69 0D 00 14 7C 05 00 18 14 17 7D 05 00 74 0E 00 7C 05 00 83 01 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          1
                             00000003     7C - LOAD_FAST           'itemComplexity'
                             00000006     7C - LOAD_FAST           'playerLevel'
                             00000009     18 - BINARY_SUBTRACT     
                             0000000A     17 - BINARY_ADD          
                             0000000B     7D - STORE_FAST          'numerator'
                             0000000E     7C - LOAD_FAST           'numerator'
                             00000011     64 - LOAD_CONST          10
                             00000014     15 - BINARY_DIVIDE       
                             00000015     7D - STORE_FAST          'exponent'
                             00000018     74 - LOAD_GLOBAL         'experienceBaseMap'
                             0000001B     74 - LOAD_GLOBAL         'constants'
                             0000001E     69 - LOAD_ATTR           'AI'
                             00000021     69 - LOAD_ATTR           'WEAKLING'
                             00000024     19 - BINARY_SUBSCR       
                             00000025     7D - STORE_FAST          'constant'
                             00000028     7C - LOAD_FAST           'constant'
                             0000002B     74 - LOAD_GLOBAL         'pow'
                             0000002E     64 - LOAD_CONST          3
                             00000031     7C - LOAD_FAST           'exponent'
                             00000034     83 - CALL_FUNCTION       r0002
                             00000037     14 - BINARY_MULTIPLY     
                             00000038     7D - STORE_FAST          'experience'
                             0000003B     7C - LOAD_FAST           'playerLevel'
                             0000003E     64 - LOAD_CONST          1
                             00000041     6A - COMPARE_OP          "!="
                             00000044     6F - JUMP_IF_FALSE       -> 00000055
                             00000047     01 - POP_TOP             
                             00000048     7C - LOAD_FAST           'playerLevel'
                             0000004B     64 - LOAD_CONST          1
                             0000004E     18 - BINARY_SUBTRACT     
                             0000004F     7D - STORE_FAST          'playerLevel'
                             00000052     6E - JUMP_FORWARD        -> 00000056
                             00000055     01 - POP_TOP             
                             00000056     7C - LOAD_FAST           'experience'
                             00000059     74 - LOAD_GLOBAL         'consolevar'
                             0000005C     69 - LOAD_ATTR           'XPKnob'
                             0000005F     7C - LOAD_FAST           'playerLevel'
                             00000062     7C - LOAD_FAST           'experience'
                             00000065     14 - BINARY_MULTIPLY     
                             00000066     74 - LOAD_GLOBAL         'consolevar'
                             00000069     69 - LOAD_ATTR           'XPConstantMultiplier'
                             0000006C     14 - BINARY_MULTIPLY     
                             0000006D     7C - LOAD_FAST           'experience'
                             00000070     18 - BINARY_SUBTRACT     
                             00000071     14 - BINARY_MULTIPLY     
                             00000072     17 - BINARY_ADD          
                             00000073     7D - STORE_FAST          'experience'
                             00000076     74 - LOAD_GLOBAL         'float'
                             00000079     7C - LOAD_FAST           'experience'
                             0000007C     83 - CALL_FUNCTION       r0001
                             0000007F     53 - RETURN_VALUE        
                             00000080     64 - LOAD_CONST          None
                             00000083     53 - RETURN_VALUE        
                         consts:
0000086D                     TUPLE: (
00000872                         None (4E),
00000873                         INT: 1 (01 00 00 00),
00000878                         INT: 10 (0A 00 00 00),
0000087D                         INT: 3 (03 00 00 00)
                             )
                         names:
00000882                     TUPLE: (
00000887                         STR: 'itemComplexity' (0E 00 00 00 69 74 65 6D 43 6F 6D 70 6C 65 78 69 74 79),
0000089A                         STR: 'playerLevel' (0B 00 00 00 70 6C 61 79 65 72 4C 65 76 65 6C),
000008AA                         STR: 'numerator' (09 00 00 00 6E 75 6D 65 72 61 74 6F 72),
000008B8                         STR: 'exponent' (08 00 00 00 65 78 70 6F 6E 65 6E 74),
000008C5                         STR: 'experienceBaseMap' (11 00 00 00 65 78 70 65 72 69 65 6E 63 65 42 61 73 65 4D 61 70),
000008DB                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
000008E9                         STR: 'AI' (02 00 00 00 41 49),
000008F0                         STR: 'WEAKLING' (08 00 00 00 57 45 41 4B 4C 49 4E 47),
000008FD                         STR: 'constant' (08 00 00 00 63 6F 6E 73 74 61 6E 74),
0000090A                         STR: 'pow' (03 00 00 00 70 6F 77),
00000912                         STR: 'experience' (0A 00 00 00 65 78 70 65 72 69 65 6E 63 65),
00000921                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
00000930                         STR: 'XPKnob' (06 00 00 00 58 50 4B 6E 6F 62),
0000093B                         STR: 'XPConstantMultiplier' (14 00 00 00 58 50 43 6F 6E 73 74 61 6E 74 4D 75 6C 74 69 70 6C 69 65 72),
00000954                         STR: 'float' (05 00 00 00 66 6C 6F 61 74)
                             )
                         varnames:
0000095E                     TUPLE: (
00000963                         STR: 'playerLevel' (0B 00 00 00 70 6C 61 79 65 72 4C 65 76 65 6C),
00000973                         STR: 'itemComplexity' (0E 00 00 00 69 74 65 6D 43 6F 6D 70 6C 65 78 69 74 79),
00000986                         STR: 'constant' (08 00 00 00 63 6F 6E 73 74 61 6E 74),
00000993                         STR: 'exponent' (08 00 00 00 65 78 70 6F 6E 65 6E 74),
000009A0                         STR: 'numerator' (09 00 00 00 6E 75 6D 65 72 61 74 6F 72),
000009AE                         STR: 'experience' (0A 00 00 00 65 78 70 65 72 69 65 6E 63 65)
                             )
                         freevars:
000009BD                     TUPLE: ()
                         cellvars:
000009C2                     TUPLE: ()
                         filename:
000009C7                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\experience.py' (42 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 65 78 70 65 72 69 65 6E 63 65 2E 70 79)
                         name:
00000A0E                     STR: 'ComputeExperienceDecompile' (1A 00 00 00 43 6F 6D 70 75 74 65 45 78 70 65 72 69 65 6E 63 65 44 65 63 6F 6D 70 69 6C 65)
                         firslineno:
00000A2D                     LONG: 72L (48 00 00 00)
                         lnotab:
00000A31                     STR: '\x00\x02\x0e\x01\n\x02\x10\x02\x13\x02\r\x01\x0e\x02 \x02' (10 00 00 00 00 02 0E 01 0A 02 10 02 13 02 0D 01 0E 02 20 02),
00000A46             CODE:
                         argcount:
00000A47                     LONG: 2L (02 00 00 00)
                         nlocals:
00000A4B                     LONG: 6L (06 00 00 00)
                         stacksize:
00000A4F                     LONG: 4L (04 00 00 00)
                         flags:
00000A53                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000A57                     STR: 'd\x01\x00|\x01\x00|\x00\x00\x18\x17}\x04\x00|\x04\x00d\x02\x00\x15}\x03\x00t\x04\x00t\x05\x00i\x06\x00i\x07\x00\x19}\x02\x00|\x02\x00t\t\x00d\x03\x00|\x03\x00\x83\x02\x00\x14}\x05\x00|\x00\x00d\x01\x00j\x03\x00o\x0e\x00\x01|\x00\x00d\x01\x00\x18}\x00\x00n\x01\x00\x01|\x05\x00t\x0b\x00i\x0c\x00|\x00\x00|\x05\x00\x14t\x0b\x00i\r\x00\x14|\x05\x00\x18\x14\x17}\x05\x00t\x0e\x00|\x05\x00\x83\x01\x00Sd\x00\x00S' (84 00 00 00 64 01 00 7C 01 00 7C 00 00 18 17 7D 04 00 7C 04 00 64 02 00 15 7D 03 00 74 04 00 74 05 00 69 06 00 69 07 00 19 7D 02 00 7C 02 00 74 09 00 64 03 00 7C 03 00 83 02 00 14 7D 05 00 7C 00 00 64 01 00 6A 03 00 6F 0E 00 01 7C 00 00 64 01 00 18 7D 00 00 6E 01 00 01 7C 05 00 74 0B 00 69 0C 00 7C 00 00 7C 05 00 14 74 0B 00 69 0D 00 14 7C 05 00 18 14 17 7D 05 00 74 0E 00 7C 05 00 83 01 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          1
                             00000003     7C - LOAD_FAST           'itemComplexity'
                             00000006     7C - LOAD_FAST           'playerLevel'
                             00000009     18 - BINARY_SUBTRACT     
                             0000000A     17 - BINARY_ADD          
                             0000000B     7D - STORE_FAST          'numerator'
                             0000000E     7C - LOAD_FAST           'numerator'
                             00000011     64 - LOAD_CONST          10
                             00000014     15 - BINARY_DIVIDE       
                             00000015     7D - STORE_FAST          'exponent'
                             00000018     74 - LOAD_GLOBAL         'experienceBaseMap'
                             0000001B     74 - LOAD_GLOBAL         'constants'
                             0000001E     69 - LOAD_ATTR           'AI'
                             00000021     69 - LOAD_ATTR           'WEAKLING'
                             00000024     19 - BINARY_SUBSCR       
                             00000025     7D - STORE_FAST          'constant'
                             00000028     7C - LOAD_FAST           'constant'
                             0000002B     74 - LOAD_GLOBAL         'pow'
                             0000002E     64 - LOAD_CONST          3
                             00000031     7C - LOAD_FAST           'exponent'
                             00000034     83 - CALL_FUNCTION       r0002
                             00000037     14 - BINARY_MULTIPLY     
                             00000038     7D - STORE_FAST          'experience'
                             0000003B     7C - LOAD_FAST           'playerLevel'
                             0000003E     64 - LOAD_CONST          1
                             00000041     6A - COMPARE_OP          "!="
                             00000044     6F - JUMP_IF_FALSE       -> 00000055
                             00000047     01 - POP_TOP             
                             00000048     7C - LOAD_FAST           'playerLevel'
                             0000004B     64 - LOAD_CONST          1
                             0000004E     18 - BINARY_SUBTRACT     
                             0000004F     7D - STORE_FAST          'playerLevel'
                             00000052     6E - JUMP_FORWARD        -> 00000056
                             00000055     01 - POP_TOP             
                             00000056     7C - LOAD_FAST           'experience'
                             00000059     74 - LOAD_GLOBAL         'consolevar'
                             0000005C     69 - LOAD_ATTR           'XPKnob'
                             0000005F     7C - LOAD_FAST           'playerLevel'
                             00000062     7C - LOAD_FAST           'experience'
                             00000065     14 - BINARY_MULTIPLY     
                             00000066     74 - LOAD_GLOBAL         'consolevar'
                             00000069     69 - LOAD_ATTR           'XPConstantMultiplier'
                             0000006C     14 - BINARY_MULTIPLY     
                             0000006D     7C - LOAD_FAST           'experience'
                             00000070     18 - BINARY_SUBTRACT     
                             00000071     14 - BINARY_MULTIPLY     
                             00000072     17 - BINARY_ADD          
                             00000073     7D - STORE_FAST          'experience'
                             00000076     74 - LOAD_GLOBAL         'float'
                             00000079     7C - LOAD_FAST           'experience'
                             0000007C     83 - CALL_FUNCTION       r0001
                             0000007F     53 - RETURN_VALUE        
                             00000080     64 - LOAD_CONST          None
                             00000083     53 - RETURN_VALUE        
                         consts:
00000AE0                     TUPLE: (
00000AE5                         None (4E),
00000AE6                         INT: 1 (01 00 00 00),
00000AEB                         INT: 10 (0A 00 00 00),
00000AF0                         INT: 3 (03 00 00 00)
                             )
                         names:
00000AF5                     TUPLE: (
00000AFA                         STR: 'itemComplexity' (0E 00 00 00 69 74 65 6D 43 6F 6D 70 6C 65 78 69 74 79),
00000B0D                         STR: 'playerLevel' (0B 00 00 00 70 6C 61 79 65 72 4C 65 76 65 6C),
00000B1D                         STR: 'numerator' (09 00 00 00 6E 75 6D 65 72 61 74 6F 72),
00000B2B                         STR: 'exponent' (08 00 00 00 65 78 70 6F 6E 65 6E 74),
00000B38                         STR: 'experienceBaseMap' (11 00 00 00 65 78 70 65 72 69 65 6E 63 65 42 61 73 65 4D 61 70),
00000B4E                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00000B5C                         STR: 'AI' (02 00 00 00 41 49),
00000B63                         STR: 'WEAKLING' (08 00 00 00 57 45 41 4B 4C 49 4E 47),
00000B70                         STR: 'constant' (08 00 00 00 63 6F 6E 73 74 61 6E 74),
00000B7D                         STR: 'pow' (03 00 00 00 70 6F 77),
00000B85                         STR: 'experience' (0A 00 00 00 65 78 70 65 72 69 65 6E 63 65),
00000B94                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
00000BA3                         STR: 'XPKnob' (06 00 00 00 58 50 4B 6E 6F 62),
00000BAE                         STR: 'XPConstantMultiplier' (14 00 00 00 58 50 43 6F 6E 73 74 61 6E 74 4D 75 6C 74 69 70 6C 69 65 72),
00000BC7                         STR: 'float' (05 00 00 00 66 6C 6F 61 74)
                             )
                         varnames:
00000BD1                     TUPLE: (
00000BD6                         STR: 'playerLevel' (0B 00 00 00 70 6C 61 79 65 72 4C 65 76 65 6C),
00000BE6                         STR: 'itemComplexity' (0E 00 00 00 69 74 65 6D 43 6F 6D 70 6C 65 78 69 74 79),
00000BF9                         STR: 'constant' (08 00 00 00 63 6F 6E 73 74 61 6E 74),
00000C06                         STR: 'exponent' (08 00 00 00 65 78 70 6F 6E 65 6E 74),
00000C13                         STR: 'numerator' (09 00 00 00 6E 75 6D 65 72 61 74 6F 72),
00000C21                         STR: 'experience' (0A 00 00 00 65 78 70 65 72 69 65 6E 63 65)
                             )
                         freevars:
00000C30                     TUPLE: ()
                         cellvars:
00000C35                     TUPLE: ()
                         filename:
00000C3A                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\experience.py' (42 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 65 78 70 65 72 69 65 6E 63 65 2E 70 79)
                         name:
00000C81                     STR: 'ComputeExperienceWriteCode' (1A 00 00 00 43 6F 6D 70 75 74 65 45 78 70 65 72 69 65 6E 63 65 57 72 69 74 65 43 6F 64 65)
                         firslineno:
00000CA0                     LONG: 89L (59 00 00 00)
                         lnotab:
00000CA4                     STR: '\x00\x02\x0e\x01\n\x02\x10\x02\x13\x02\r\x01\x0e\x02 \x02' (10 00 00 00 00 02 0E 01 0A 02 10 02 13 02 0D 01 0E 02 20 02),
00000CB9             CODE:
                         argcount:
00000CBA                     LONG: 3L (03 00 00 00)
                         nlocals:
00000CBE                     LONG: 7L (07 00 00 00)
                         stacksize:
00000CC2                     LONG: 4L (04 00 00 00)
                         flags:
00000CC6                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000CCA                     STR: 'd\x01\x00|\x01\x00|\x00\x00\x18\x17}\x05\x00|\x05\x00d\x02\x00\x15}\x04\x00t\x04\x00|\x02\x00\x19}\x03\x00|\x03\x00t\x07\x00d\x03\x00|\x04\x00\x83\x02\x00\x14}\x06\x00|\x00\x00d\x01\x00j\x03\x00o\x0e\x00\x01|\x00\x00d\x01\x00\x18}\x00\x00n\x01\x00\x01|\x06\x00t\t\x00i\n\x00|\x00\x00|\x06\x00\x14t\t\x00i\x0b\x00\x14|\x06\x00\x18\x14\x17}\x06\x00t\x0c\x00|\x06\x00\x83\x01\x00Sd\x00\x00S' (7E 00 00 00 64 01 00 7C 01 00 7C 00 00 18 17 7D 05 00 7C 05 00 64 02 00 15 7D 04 00 74 04 00 7C 02 00 19 7D 03 00 7C 03 00 74 07 00 64 03 00 7C 04 00 83 02 00 14 7D 06 00 7C 00 00 64 01 00 6A 03 00 6F 0E 00 01 7C 00 00 64 01 00 18 7D 00 00 6E 01 00 01 7C 06 00 74 09 00 69 0A 00 7C 00 00 7C 06 00 14 74 09 00 69 0B 00 14 7C 06 00 18 14 17 7D 06 00 74 0C 00 7C 06 00 83 01 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          1
                             00000003     7C - LOAD_FAST           'taskLevel'
                             00000006     7C - LOAD_FAST           'playerLevel'
                             00000009     18 - BINARY_SUBTRACT     
                             0000000A     17 - BINARY_ADD          
                             0000000B     7D - STORE_FAST          'numerator'
                             0000000E     7C - LOAD_FAST           'numerator'
                             00000011     64 - LOAD_CONST          10
                             00000014     15 - BINARY_DIVIDE       
                             00000015     7D - STORE_FAST          'exponent'
                             00000018     74 - LOAD_GLOBAL         'experienceBaseMap'
                             0000001B     7C - LOAD_FAST           'rank'
                             0000001E     19 - BINARY_SUBSCR       
                             0000001F     7D - STORE_FAST          'constant'
                             00000022     7C - LOAD_FAST           'constant'
                             00000025     74 - LOAD_GLOBAL         'pow'
                             00000028     64 - LOAD_CONST          3
                             0000002B     7C - LOAD_FAST           'exponent'
                             0000002E     83 - CALL_FUNCTION       r0002
                             00000031     14 - BINARY_MULTIPLY     
                             00000032     7D - STORE_FAST          'experience'
                             00000035     7C - LOAD_FAST           'playerLevel'
                             00000038     64 - LOAD_CONST          1
                             0000003B     6A - COMPARE_OP          "!="
                             0000003E     6F - JUMP_IF_FALSE       -> 0000004F
                             00000041     01 - POP_TOP             
                             00000042     7C - LOAD_FAST           'playerLevel'
                             00000045     64 - LOAD_CONST          1
                             00000048     18 - BINARY_SUBTRACT     
                             00000049     7D - STORE_FAST          'playerLevel'
                             0000004C     6E - JUMP_FORWARD        -> 00000050
                             0000004F     01 - POP_TOP             
                             00000050     7C - LOAD_FAST           'experience'
                             00000053     74 - LOAD_GLOBAL         'consolevar'
                             00000056     69 - LOAD_ATTR           'XPKnob'
                             00000059     7C - LOAD_FAST           'playerLevel'
                             0000005C     7C - LOAD_FAST           'experience'
                             0000005F     14 - BINARY_MULTIPLY     
                             00000060     74 - LOAD_GLOBAL         'consolevar'
                             00000063     69 - LOAD_ATTR           'XPConstantMultiplier'
                             00000066     14 - BINARY_MULTIPLY     
                             00000067     7C - LOAD_FAST           'experience'
                             0000006A     18 - BINARY_SUBTRACT     
                             0000006B     14 - BINARY_MULTIPLY     
                             0000006C     17 - BINARY_ADD          
                             0000006D     7D - STORE_FAST          'experience'
                             00000070     74 - LOAD_GLOBAL         'float'
                             00000073     7C - LOAD_FAST           'experience'
                             00000076     83 - CALL_FUNCTION       r0001
                             00000079     53 - RETURN_VALUE        
                             0000007A     64 - LOAD_CONST          None
                             0000007D     53 - RETURN_VALUE        
                         consts:
00000D4D                     TUPLE: (
00000D52                         None (4E),
00000D53                         INT: 1 (01 00 00 00),
00000D58                         INT: 10 (0A 00 00 00),
00000D5D                         INT: 3 (03 00 00 00)
                             )
                         names:
00000D62                     TUPLE: (
00000D67                         STR: 'taskLevel' (09 00 00 00 74 61 73 6B 4C 65 76 65 6C),
00000D75                         STR: 'playerLevel' (0B 00 00 00 70 6C 61 79 65 72 4C 65 76 65 6C),
00000D85                         STR: 'numerator' (09 00 00 00 6E 75 6D 65 72 61 74 6F 72),
00000D93                         STR: 'exponent' (08 00 00 00 65 78 70 6F 6E 65 6E 74),
00000DA0                         STR: 'experienceBaseMap' (11 00 00 00 65 78 70 65 72 69 65 6E 63 65 42 61 73 65 4D 61 70),
00000DB6                         STR: 'rank' (04 00 00 00 72 61 6E 6B),
00000DBF                         STR: 'constant' (08 00 00 00 63 6F 6E 73 74 61 6E 74),
00000DCC                         STR: 'pow' (03 00 00 00 70 6F 77),
00000DD4                         STR: 'experience' (0A 00 00 00 65 78 70 65 72 69 65 6E 63 65),
00000DE3                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
00000DF2                         STR: 'XPKnob' (06 00 00 00 58 50 4B 6E 6F 62),
00000DFD                         STR: 'XPConstantMultiplier' (14 00 00 00 58 50 43 6F 6E 73 74 61 6E 74 4D 75 6C 74 69 70 6C 69 65 72),
00000E16                         STR: 'float' (05 00 00 00 66 6C 6F 61 74)
                             )
                         varnames:
00000E20                     TUPLE: (
00000E25                         STR: 'playerLevel' (0B 00 00 00 70 6C 61 79 65 72 4C 65 76 65 6C),
00000E35                         STR: 'taskLevel' (09 00 00 00 74 61 73 6B 4C 65 76 65 6C),
00000E43                         STR: 'rank' (04 00 00 00 72 61 6E 6B),
00000E4C                         STR: 'constant' (08 00 00 00 63 6F 6E 73 74 61 6E 74),
00000E59                         STR: 'exponent' (08 00 00 00 65 78 70 6F 6E 65 6E 74),
00000E66                         STR: 'numerator' (09 00 00 00 6E 75 6D 65 72 61 74 6F 72),
00000E74                         STR: 'experience' (0A 00 00 00 65 78 70 65 72 69 65 6E 63 65)
                             )
                         freevars:
00000E83                     TUPLE: ()
                         cellvars:
00000E88                     TUPLE: ()
                         filename:
00000E8D                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\experience.py' (42 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 65 78 70 65 72 69 65 6E 63 65 2E 70 79)
                         name:
00000ED4                     STR: 'ComputeGenericExperience' (18 00 00 00 43 6F 6D 70 75 74 65 47 65 6E 65 72 69 63 45 78 70 65 72 69 65 6E 63 65)
                         firslineno:
00000EF1                     LONG: 111L (6F 00 00 00)
                         lnotab:
00000EF5                     STR: '\x00\x03\x0e\x01\n\x02\n\x02\x13\x02\r\x01\x0e\x02 \x02' (10 00 00 00 00 03 0E 01 0A 02 0A 02 13 02 0D 01 0E 02 20 02),
00000F0A             None (4E)
                 )
             names:
00000F0B         TUPLE: (
00000F10             STR: 'experienceBaseMap' (11 00 00 00 65 78 70 65 72 69 65 6E 63 65 42 61 73 65 4D 61 70),
00000F26             STR: 'groupXPMap' (0A 00 00 00 67 72 6F 75 70 58 50 4D 61 70),
00000F35             STR: 'Init' (04 00 00 00 49 6E 69 74),
00000F3E             STR: 'ComputeExperience' (11 00 00 00 43 6F 6D 70 75 74 65 45 78 70 65 72 69 65 6E 63 65),
00000F54             STR: 'ComputeGroupBonus' (11 00 00 00 43 6F 6D 70 75 74 65 47 72 6F 75 70 42 6F 6E 75 73),
00000F6A             STR: 'ComputeExperienceDecompile' (1A 00 00 00 43 6F 6D 70 75 74 65 45 78 70 65 72 69 65 6E 63 65 44 65 63 6F 6D 70 69 6C 65),
00000F89             STR: 'ComputeExperienceWriteCode' (1A 00 00 00 43 6F 6D 70 75 74 65 45 78 70 65 72 69 65 6E 63 65 57 72 69 74 65 43 6F 64 65),
00000FA8             STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00000FB6             STR: 'AI' (02 00 00 00 41 49),
00000FBD             STR: 'WEAKLING' (08 00 00 00 57 45 41 4B 4C 49 4E 47),
00000FCA             STR: 'ComputeGenericExperience' (18 00 00 00 43 6F 6D 70 75 74 65 47 65 6E 65 72 69 63 45 78 70 65 72 69 65 6E 63 65)
                 )
             varnames:
00000FE7         TUPLE: (
00000FEC             STR: 'ComputeExperience' (11 00 00 00 43 6F 6D 70 75 74 65 45 78 70 65 72 69 65 6E 63 65),
00001002             STR: 'ComputeExperienceWriteCode' (1A 00 00 00 43 6F 6D 70 75 74 65 45 78 70 65 72 69 65 6E 63 65 57 72 69 74 65 43 6F 64 65),
00001021             STR: 'ComputeGroupBonus' (11 00 00 00 43 6F 6D 70 75 74 65 47 72 6F 75 70 42 6F 6E 75 73),
00001037             STR: 'ComputeGenericExperience' (18 00 00 00 43 6F 6D 70 75 74 65 47 65 6E 65 72 69 63 45 78 70 65 72 69 65 6E 63 65),
00001054             STR: 'Init' (04 00 00 00 49 6E 69 74),
0000105D             STR: 'ComputeExperienceDecompile' (1A 00 00 00 43 6F 6D 70 75 74 65 45 78 70 65 72 69 65 6E 63 65 44 65 63 6F 6D 70 69 6C 65),
0000107C             STR: 'experienceBaseMap' (11 00 00 00 65 78 70 65 72 69 65 6E 63 65 42 61 73 65 4D 61 70),
00001092             STR: 'groupXPMap' (0A 00 00 00 67 72 6F 75 70 58 50 4D 61 70)
                 )
             freevars:
000010A1         TUPLE: ()
             cellvars:
000010A6         TUPLE: ()
             filename:
000010AB         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\experience.py' (42 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 65 78 70 65 72 69 65 6E 63 65 2E 70 79)
             name:
000010F2         STR: '?' (01 00 00 00 3F)
             firslineno:
000010F8         LONG: 1L (01 00 00 00)
             lnotab:
000010FC         STR: '\x06\x01\x06\x02\t\x0e\t&\t\x10\t\x11\t\x16' (0E 00 00 00 06 01 06 02 09 0E 09 26 09 10 09 11 09 16)

