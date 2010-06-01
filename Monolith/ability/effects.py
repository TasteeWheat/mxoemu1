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
00000019         STR: 'd\x00\x00k\x00\x00Z\x01\x00d\x00\x00k\x02\x00i\x03\x00Z\x04\x00d\x00\x00k\x05\x00Z\x06\x00d\x01\x00k\x07\x00Td\x00\x00k\x08\x00Z\t\x00d\x02\x00\x84\x00\x00Z\n\x00d\x03\x00\x84\x00\x00Z\x0b\x00e\x06\x00i\x0c\x00Z\r\x00d\x04\x00\x84\x00\x00Z\x0e\x00e\x0f\x00d\x05\x00\x84\x01\x00Z\x10\x00d\x00\x00S' (62 00 00 00 64 00 00 6B 00 00 5A 01 00 64 00 00 6B 02 00 69 03 00 5A 04 00 64 00 00 6B 05 00 5A 06 00 64 01 00 6B 07 00 54 64 00 00 6B 08 00 5A 09 00 64 02 00 84 00 00 5A 0A 00 64 03 00 84 00 00 5A 0B 00 65 06 00 69 0C 00 5A 0D 00 64 04 00 84 00 00 5A 0E 00 65 0F 00 64 05 00 84 01 00 5A 10 00 64 00 00 53)
                 00000000     64 - LOAD_CONST          None
                 00000003     6B - IMPORT_NAME         'combat_defines'
                 00000006     5A - STORE_NAME          'CD'
                 00000009     64 - LOAD_CONST          None
                 0000000C     6B - IMPORT_NAME         'ability.utility'
                 0000000F     69 - LOAD_ATTR           'utility'
                 00000012     5A - STORE_NAME          'Utility'
                 00000015     64 - LOAD_CONST          None
                 00000018     6B - IMPORT_NAME         'ltfxmap'
                 0000001B     5A - STORE_NAME          'FX'
                 0000001E     64 - LOAD_CONST          ('*')
                 00000021     6B - IMPORT_NAME         'ability.defines'
                 00000024     54 - IMPORT_STAR         
                 00000025     64 - LOAD_CONST          None
                 00000028     6B - IMPORT_NAME         'stringtable_client'
                 0000002B     5A - STORE_NAME          'StringTable'
                 0000002E     64 - LOAD_CONST          CODE('CorrodeItem')
                 00000031     84 - MAKE_FUNCTION       r0000
                 00000034     5A - STORE_NAME          'CorrodeItem'
                 00000037     64 - LOAD_CONST          CODE('DestroyItem')
                 0000003A     84 - MAKE_FUNCTION       r0000
                 0000003D     5A - STORE_NAME          'DestroyItem'
                 00000040     65 - LOAD_NAME           'FX'
                 00000043     69 - LOAD_ATTR           'FX_CHARACTER_GENERIC_ABILITY_DOWNGRADE'
                 00000046     5A - STORE_NAME          'DISABLE_FX'
                 00000049     64 - LOAD_CONST          CODE('DisableDependents')
                 0000004C     84 - MAKE_FUNCTION       r0000
                 0000004F     5A - STORE_NAME          'DisableDependents'
                 00000052     65 - LOAD_NAME           'True'
                 00000055     64 - LOAD_CONST          CODE('DisableAbility')
                 00000058     84 - MAKE_FUNCTION       r0001
                 0000005B     5A - STORE_NAME          'DisableAbility'
                 0000005E     64 - LOAD_CONST          None
                 00000061     53 - RETURN_VALUE        
             consts:
00000080         TUPLE: (
00000085             None (4E),
00000086             TUPLE: (
0000008B                 STR: '*' (01 00 00 00 2A)
                     ),
00000091             CODE:
                         argcount:
00000092                     LONG: 2L (02 00 00 00)
                         nlocals:
00000096                     LONG: 3L (03 00 00 00)
                         stacksize:
0000009A                     LONG: 3L (03 00 00 00)
                         flags:
0000009E                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000000A2                     STR: '|\x00\x00o\x87\x00\x01|\x00\x00i\x01\x00}\x02\x00t\x02\x00i\x03\x00d\x01\x00|\x02\x00\r\x17d\x02\x00\x17\x83\x01\x00\x01|\x02\x00d\x03\x00j\x02\x00o\x15\x00\x01t\x02\x00i\x03\x00d\x04\x00\x83\x01\x00\x01d\x00\x00Sn\x01\x00\x01|\x02\x00|\x01\x008}\x02\x00|\x02\x00|\x00\x00_\x01\x00|\x02\x00d\x03\x00j\x01\x00p\n\x00\x01|\x02\x00d\x05\x00j\x04\x00o\x11\x00\x01t\x02\x00i\x03\x00d\x06\x00\x83\x01\x00\x01n\x01\x00\x01t\x05\x00Sn\x12\x00\x01t\x02\x00i\x03\x00d\x07\x00\x83\x01\x00\x01t\x06\x00Sd\x00\x00S' (A3 00 00 00 7C 00 00 6F 87 00 01 7C 00 00 69 01 00 7D 02 00 74 02 00 69 03 00 64 01 00 7C 02 00 0D 17 64 02 00 17 83 01 00 01 7C 02 00 64 03 00 6A 02 00 6F 15 00 01 74 02 00 69 03 00 64 04 00 83 01 00 01 64 00 00 53 6E 01 00 01 7C 02 00 7C 01 00 38 7D 02 00 7C 02 00 7C 00 00 5F 01 00 7C 02 00 64 03 00 6A 01 00 70 0A 00 01 7C 02 00 64 05 00 6A 04 00 6F 11 00 01 74 02 00 69 03 00 64 06 00 83 01 00 01 6E 01 00 01 74 05 00 53 6E 12 00 01 74 02 00 69 03 00 64 07 00 83 01 00 01 74 06 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'item'
                             00000003     6F - JUMP_IF_FALSE       -> 0000008D
                             00000006     01 - POP_TOP             
                             00000007     7C - LOAD_FAST           'item'
                             0000000A     69 - LOAD_ATTR           'stability'
                             0000000D     7D - STORE_FAST          'stability'
                             00000010     74 - LOAD_GLOBAL         'Utility'
                             00000013     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000016     64 - LOAD_CONST          'CorrodeItem: item has '
                             00000019     7C - LOAD_FAST           'stability'
                             0000001C     0D - UNARY_CONVERT       
                             0000001D     17 - BINARY_ADD          
                             0000001E     64 - LOAD_CONST          ' stability.'
                             00000021     17 - BINARY_ADD          
                             00000022     83 - CALL_FUNCTION       r0001
                             00000025     01 - POP_TOP             
                             00000026     7C - LOAD_FAST           'stability'
                             00000029     64 - LOAD_CONST          0
                             0000002C     6A - COMPARE_OP          "=="
                             0000002F     6F - JUMP_IF_FALSE       -> 00000047
                             00000032     01 - POP_TOP             
                             00000033     74 - LOAD_GLOBAL         'Utility'
                             00000036     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000039     64 - LOAD_CONST          'CorrodeItem: Item is industructable.'
                             0000003C     83 - CALL_FUNCTION       r0001
                             0000003F     01 - POP_TOP             
                             00000040     64 - LOAD_CONST          None
                             00000043     53 - RETURN_VALUE        
                             00000044     6E - JUMP_FORWARD        -> 00000048
                             00000047     01 - POP_TOP             
                             00000048     7C - LOAD_FAST           'stability'
                             0000004B     7C - LOAD_FAST           'corrosionAmount'
                             0000004E     38 - INPLACE_SUBTRACT    
                             0000004F     7D - STORE_FAST          'stability'
                             00000052     7C - LOAD_FAST           'stability'
                             00000055     7C - LOAD_FAST           'item'
                             00000058     5F - STORE_ATTR          'stability'
                             0000005B     7C - LOAD_FAST           'stability'
                             0000005E     64 - LOAD_CONST          0
                             00000061     6A - COMPARE_OP          "<="
                             00000064     70 - JUMP_IF_TRUE        -> 00000071
                             00000067     01 - POP_TOP             
                             00000068     7C - LOAD_FAST           'stability'
                             0000006B     64 - LOAD_CONST          7
                             0000006E     6A - COMPARE_OP          ">"
                             00000071     6F - JUMP_IF_FALSE       -> 00000085
                             00000074     01 - POP_TOP             
                             00000075     74 - LOAD_GLOBAL         'Utility'
                             00000078     69 - LOAD_ATTR           'outputAbilityDebug'
                             0000007B     64 - LOAD_CONST          'CorrodeItem: Item has no stability left.'
                             0000007E     83 - CALL_FUNCTION       r0001
                             00000081     01 - POP_TOP             
                             00000082     6E - JUMP_FORWARD        -> 00000086
                             00000085     01 - POP_TOP             
                             00000086     74 - LOAD_GLOBAL         'True'
                             00000089     53 - RETURN_VALUE        
                             0000008A     6E - JUMP_FORWARD        -> 0000009F
                             0000008D     01 - POP_TOP             
                             0000008E     74 - LOAD_GLOBAL         'Utility'
                             00000091     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000094     64 - LOAD_CONST          'CorrodeItem: No item given to corrode.'
                             00000097     83 - CALL_FUNCTION       r0001
                             0000009A     01 - POP_TOP             
                             0000009B     74 - LOAD_GLOBAL         'False'
                             0000009E     53 - RETURN_VALUE        
                             0000009F     64 - LOAD_CONST          None
                             000000A2     53 - RETURN_VALUE        
                         consts:
0000014A                     TUPLE: (
0000014F                         None (4E),
00000150                         STR: 'CorrodeItem: item has ' (16 00 00 00 43 6F 72 72 6F 64 65 49 74 65 6D 3A 20 69 74 65 6D 20 68 61 73 20),
0000016B                         STR: ' stability.' (0B 00 00 00 20 73 74 61 62 69 6C 69 74 79 2E),
0000017B                         INT: 0 (00 00 00 00),
00000180                         STR: 'CorrodeItem: Item is industructable.' (24 00 00 00 43 6F 72 72 6F 64 65 49 74 65 6D 3A 20 49 74 65 6D 20 69 73 20 69 6E 64 75 73 74 72 75 63 74 61 62 6C 65 2E),
000001A9                         INT: 7 (07 00 00 00),
000001AE                         STR: 'CorrodeItem: Item has no stability left.' (28 00 00 00 43 6F 72 72 6F 64 65 49 74 65 6D 3A 20 49 74 65 6D 20 68 61 73 20 6E 6F 20 73 74 61 62 69 6C 69 74 79 20 6C 65 66 74 2E),
000001DB                         STR: 'CorrodeItem: No item given to corrode.' (26 00 00 00 43 6F 72 72 6F 64 65 49 74 65 6D 3A 20 4E 6F 20 69 74 65 6D 20 67 69 76 65 6E 20 74 6F 20 63 6F 72 72 6F 64 65 2E)
                             )
                         names:
00000206                     TUPLE: (
0000020B                         STR: 'item' (04 00 00 00 69 74 65 6D),
00000214                         STR: 'stability' (09 00 00 00 73 74 61 62 69 6C 69 74 79),
00000222                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
0000022E                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000245                         STR: 'corrosionAmount' (0F 00 00 00 63 6F 72 72 6F 73 69 6F 6E 41 6D 6F 75 6E 74),
00000259                         STR: 'True' (04 00 00 00 54 72 75 65),
00000262                         STR: 'False' (05 00 00 00 46 61 6C 73 65)
                             )
                         varnames:
0000026C                     TUPLE: (
00000271                         STR: 'item' (04 00 00 00 69 74 65 6D),
0000027A                         STR: 'corrosionAmount' (0F 00 00 00 63 6F 72 72 6F 73 69 6F 6E 41 6D 6F 75 6E 74),
0000028E                         STR: 'stability' (09 00 00 00 73 74 61 62 69 6C 69 74 79)
                             )
                         freevars:
0000029C                     TUPLE: ()
                         cellvars:
000002A1                     TUPLE: ()
                         filename:
000002A6                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\effects.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 65 66 66 65 63 74 73 2E 70 79)
                         name:
000002F2                     STR: 'CorrodeItem' (0B 00 00 00 43 6F 72 72 6F 64 65 49 74 65 6D)
                         firslineno:
00000302                     LONG: 13L (0D 00 00 00)
                         lnotab:
00000306                     STR: '\x00\x03\x07\x01\t\x01\x16\x02\r\x01\r\x01\x08\x03\n\x01\t\x03\x1a\x01\x11\x03\x08\x02\r\x01' (1A 00 00 00 00 03 07 01 09 01 16 02 0D 01 0D 01 08 03 0A 01 09 03 1A 01 11 03 08 02 0D 01),
00000325             CODE:
                         argcount:
00000326                     LONG: 3L (03 00 00 00)
                         nlocals:
0000032A                     LONG: 3L (03 00 00 00)
                         stacksize:
0000032E                     LONG: 3L (03 00 00 00)
                         flags:
00000332                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000336                     STR: 't\x00\x00i\x01\x00|\x00\x00\x83\x01\x00oh\x00\x01t\x00\x00i\x03\x00d\x01\x00|\x02\x00\r\x17d\x02\x00\x17|\x01\x00i\x06\x00\r\x17d\x03\x00\x17\x83\x01\x00\x01|\x01\x00i\x06\x00d\x04\x00j\x02\x00o\x15\x00\x01t\x00\x00i\x03\x00d\x05\x00\x83\x01\x00\x01t\x07\x00Sn\x01\x00\x01t\x00\x00i\x03\x00d\x06\x00\x83\x01\x00\x01|\x00\x00i\x08\x00i\t\x00|\x02\x00\x83\x01\x00\x01n9\x00\x01|\x02\x00d\x07\x00j\x02\x00o\x1e\x00\x01t\x00\x00i\x03\x00d\x08\x00\x83\x01\x00\x01|\x00\x00i\n\x00i\x0b\x00\x83\x00\x00\x01n\x0e\x00\x01t\x00\x00i\x03\x00d\t\x00\x83\x01\x00\x01t\x0c\x00Sd\x00\x00S' (B8 00 00 00 74 00 00 69 01 00 7C 00 00 83 01 00 6F 68 00 01 74 00 00 69 03 00 64 01 00 7C 02 00 0D 17 64 02 00 17 7C 01 00 69 06 00 0D 17 64 03 00 17 83 01 00 01 7C 01 00 69 06 00 64 04 00 6A 02 00 6F 15 00 01 74 00 00 69 03 00 64 05 00 83 01 00 01 74 07 00 53 6E 01 00 01 74 00 00 69 03 00 64 06 00 83 01 00 01 7C 00 00 69 08 00 69 09 00 7C 02 00 83 01 00 01 6E 39 00 01 7C 02 00 64 07 00 6A 02 00 6F 1E 00 01 74 00 00 69 03 00 64 08 00 83 01 00 01 7C 00 00 69 0A 00 69 0B 00 83 00 00 01 6E 0E 00 01 74 00 00 69 03 00 64 09 00 83 01 00 01 74 0C 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'IsAPlayer'
                             00000006     7C - LOAD_FAST           'subject'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     6F - JUMP_IF_FALSE       -> 00000077
                             0000000F     01 - POP_TOP             
                             00000010     74 - LOAD_GLOBAL         'Utility'
                             00000013     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000016     64 - LOAD_CONST          'DestroyItem: slot'
                             00000019     7C - LOAD_FAST           'slot'
                             0000001C     0D - UNARY_CONVERT       
                             0000001D     17 - BINARY_ADD          
                             0000001E     64 - LOAD_CONST          "'s item.stability = "
                             00000021     17 - BINARY_ADD          
                             00000022     7C - LOAD_FAST           'item'
                             00000025     69 - LOAD_ATTR           'stability'
                             00000028     0D - UNARY_CONVERT       
                             00000029     17 - BINARY_ADD          
                             0000002A     64 - LOAD_CONST          '.'
                             0000002D     17 - BINARY_ADD          
                             0000002E     83 - CALL_FUNCTION       r0001
                             00000031     01 - POP_TOP             
                             00000032     7C - LOAD_FAST           'item'
                             00000035     69 - LOAD_ATTR           'stability'
                             00000038     64 - LOAD_CONST          0
                             0000003B     6A - COMPARE_OP          "=="
                             0000003E     6F - JUMP_IF_FALSE       -> 00000056
                             00000041     01 - POP_TOP             
                             00000042     74 - LOAD_GLOBAL         'Utility'
                             00000045     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000048     64 - LOAD_CONST          'DestroyItem: Item is indestructable.'
                             0000004B     83 - CALL_FUNCTION       r0001
                             0000004E     01 - POP_TOP             
                             0000004F     74 - LOAD_GLOBAL         'DEFLECTED'
                             00000052     53 - RETURN_VALUE        
                             00000053     6E - JUMP_FORWARD        -> 00000057
                             00000056     01 - POP_TOP             
                             00000057     74 - LOAD_GLOBAL         'Utility'
                             0000005A     69 - LOAD_ATTR           'outputAbilityDebug'
                             0000005D     64 - LOAD_CONST          "DestroyItem: Player's item destroyed."
                             00000060     83 - CALL_FUNCTION       r0001
                             00000063     01 - POP_TOP             
                             00000064     7C - LOAD_FAST           'subject'
                             00000067     69 - LOAD_ATTR           'Inventory'
                             0000006A     69 - LOAD_ATTR           'rmvItem'
                             0000006D     7C - LOAD_FAST           'slot'
                             00000070     83 - CALL_FUNCTION       r0001
                             00000073     01 - POP_TOP             
                             00000074     6E - JUMP_FORWARD        -> 000000B0
                             00000077     01 - POP_TOP             
                             00000078     7C - LOAD_FAST           'slot'
                             0000007B     64 - LOAD_CONST          109
                             0000007E     6A - COMPARE_OP          "=="
                             00000081     6F - JUMP_IF_FALSE       -> 000000A2
                             00000084     01 - POP_TOP             
                             00000085     74 - LOAD_GLOBAL         'Utility'
                             00000088     69 - LOAD_ATTR           'outputAbilityDebug'
                             0000008B     64 - LOAD_CONST          "DestroyItem: NPC's weapon destroyed."
                             0000008E     83 - CALL_FUNCTION       r0001
                             00000091     01 - POP_TOP             
                             00000092     7C - LOAD_FAST           'subject'
                             00000095     69 - LOAD_ATTR           'AI'
                             00000098     69 - LOAD_ATTR           'rmvWeapon'
                             0000009B     83 - CALL_FUNCTION       r0000
                             0000009E     01 - POP_TOP             
                             0000009F     6E - JUMP_FORWARD        -> 000000B0
                             000000A2     01 - POP_TOP             
                             000000A3     74 - LOAD_GLOBAL         'Utility'
                             000000A6     69 - LOAD_ATTR           'outputAbilityDebug'
                             000000A9     64 - LOAD_CONST          "DestroyItem: NPC's doesn't have that slot."
                             000000AC     83 - CALL_FUNCTION       r0001
                             000000AF     01 - POP_TOP             
                             000000B0     74 - LOAD_GLOBAL         'SUCCESS'
                             000000B3     53 - RETURN_VALUE        
                             000000B4     64 - LOAD_CONST          None
                             000000B7     53 - RETURN_VALUE        
                         consts:
000003F3                     TUPLE: (
000003F8                         None (4E),
000003F9                         STR: 'DestroyItem: slot' (11 00 00 00 44 65 73 74 72 6F 79 49 74 65 6D 3A 20 73 6C 6F 74),
0000040F                         STR: "'s item.stability = " (14 00 00 00 27 73 20 69 74 65 6D 2E 73 74 61 62 69 6C 69 74 79 20 3D 20),
00000428                         STR: '.' (01 00 00 00 2E),
0000042E                         INT: 0 (00 00 00 00),
00000433                         STR: 'DestroyItem: Item is indestructable.' (24 00 00 00 44 65 73 74 72 6F 79 49 74 65 6D 3A 20 49 74 65 6D 20 69 73 20 69 6E 64 65 73 74 72 75 63 74 61 62 6C 65 2E),
0000045C                         STR: "DestroyItem: Player's item destroyed." (25 00 00 00 44 65 73 74 72 6F 79 49 74 65 6D 3A 20 50 6C 61 79 65 72 27 73 20 69 74 65 6D 20 64 65 73 74 72 6F 79 65 64 2E),
00000486                         INT: 109 (6D 00 00 00),
0000048B                         STR: "DestroyItem: NPC's weapon destroyed." (24 00 00 00 44 65 73 74 72 6F 79 49 74 65 6D 3A 20 4E 50 43 27 73 20 77 65 61 70 6F 6E 20 64 65 73 74 72 6F 79 65 64 2E),
000004B4                         STR: "DestroyItem: NPC's doesn't have that slot." (2A 00 00 00 44 65 73 74 72 6F 79 49 74 65 6D 3A 20 4E 50 43 27 73 20 64 6F 65 73 6E 27 74 20 68 61 76 65 20 74 68 61 74 20 73 6C 6F 74 2E)
                             )
                         names:
000004E3                     TUPLE: (
000004E8                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000004F4                         STR: 'IsAPlayer' (09 00 00 00 49 73 41 50 6C 61 79 65 72),
00000502                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000050E                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000525                         STR: 'slot' (04 00 00 00 73 6C 6F 74),
0000052E                         STR: 'item' (04 00 00 00 69 74 65 6D),
00000537                         STR: 'stability' (09 00 00 00 73 74 61 62 69 6C 69 74 79),
00000545                         STR: 'DEFLECTED' (09 00 00 00 44 45 46 4C 45 43 54 45 44),
00000553                         STR: 'Inventory' (09 00 00 00 49 6E 76 65 6E 74 6F 72 79),
00000561                         STR: 'rmvItem' (07 00 00 00 72 6D 76 49 74 65 6D),
0000056D                         STR: 'AI' (02 00 00 00 41 49),
00000574                         STR: 'rmvWeapon' (09 00 00 00 72 6D 76 57 65 61 70 6F 6E),
00000582                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53)
                             )
                         varnames:
0000058E                     TUPLE: (
00000593                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000059F                         STR: 'item' (04 00 00 00 69 74 65 6D),
000005A8                         STR: 'slot' (04 00 00 00 73 6C 6F 74)
                             )
                         freevars:
000005B1                     TUPLE: ()
                         cellvars:
000005B6                     TUPLE: ()
                         filename:
000005BB                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\effects.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 65 66 66 65 63 74 73 2E 70 79)
                         name:
00000607                     STR: 'DestroyItem' (0B 00 00 00 44 65 73 74 72 6F 79 49 74 65 6D)
                         firslineno:
00000617                     LONG: 45L (2D 00 00 00)
                         lnotab:
0000061B                     STR: '\x00\x03\x10\x02"\x01\x10\x01\r\x01\x08\x01\r\x01\x14\x03\r\x01\r\x01\x11\x02\r\x03' (18 00 00 00 00 03 10 02 22 01 10 01 0D 01 08 01 0D 01 14 03 0D 01 0D 01 11 02 0D 03),
00000638             CODE:
                         argcount:
00000639                     LONG: 3L (03 00 00 00)
                         nlocals:
0000063D                     LONG: 7L (07 00 00 00)
                         stacksize:
00000641                     LONG: 8L (08 00 00 00)
                         flags:
00000645                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000649                     STR: 't\x00\x00i\x01\x00|\x01\x00\x83\x01\x00}\x04\x00t\x04\x00i\x05\x00d\x01\x00\x83\x01\x00\x01t\x06\x00|\x04\x00\x83\x01\x00o\x8f\x00\x01x\x8c\x00|\x04\x00D]\x80\x00}\x05\x00t\x04\x00i\x08\x00|\x05\x00\x83\x01\x00}\x03\x00t\x04\x00i\x05\x00d\x02\x00|\x03\x00\x16\x83\x01\x00\x01|\x00\x00i\x0b\x00|\x05\x00\x19oL\x00\x01t\x04\x00i\x05\x00d\x03\x00|\x03\x00\x16\x83\x01\x00\x01d\x04\x00d\x05\x00d\x06\x00d\x06\x00d\x06\x00f\x05\x00}\x06\x00|\x00\x00i\r\x00i\x0e\x00|\x06\x00t\x00\x00i\x0f\x00|\x05\x00|\x02\x00d\x07\x00d\x07\x00\x83\x06\x00\x01q0\x00\x01q0\x00Wn\x01\x00\x01d\x00\x00S' (BC 00 00 00 74 00 00 69 01 00 7C 01 00 83 01 00 7D 04 00 74 04 00 69 05 00 64 01 00 83 01 00 01 74 06 00 7C 04 00 83 01 00 6F 8F 00 01 78 8C 00 7C 04 00 44 5D 80 00 7D 05 00 74 04 00 69 08 00 7C 05 00 83 01 00 7D 03 00 74 04 00 69 05 00 64 02 00 7C 03 00 16 83 01 00 01 7C 00 00 69 0B 00 7C 05 00 19 6F 4C 00 01 74 04 00 69 05 00 64 03 00 7C 03 00 16 83 01 00 01 64 04 00 64 05 00 64 06 00 64 06 00 64 06 00 66 05 00 7D 06 00 7C 00 00 69 0D 00 69 0E 00 7C 06 00 74 00 00 69 0F 00 7C 05 00 7C 02 00 64 07 00 64 07 00 83 06 00 01 71 30 00 01 71 30 00 57 6E 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'abilitylib'
                             00000003     69 - LOAD_ATTR           'getAbilityDependents'
                             00000006     7C - LOAD_FAST           'src_abil'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     7D - STORE_FAST          'abil_list'
                             0000000F     74 - LOAD_GLOBAL         'Utility'
                             00000012     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000015     64 - LOAD_CONST          'DisableDependents:'
                             00000018     83 - CALL_FUNCTION       r0001
                             0000001B     01 - POP_TOP             
                             0000001C     74 - LOAD_GLOBAL         'len'
                             0000001F     7C - LOAD_FAST           'abil_list'
                             00000022     83 - CALL_FUNCTION       r0001
                             00000025     6F - JUMP_IF_FALSE       -> 000000B7
                             00000028     01 - POP_TOP             
                             00000029     78 - SETUP_LOOP          -> 000000B8
                             0000002C     7C - LOAD_FAST           'abil_list'
                             0000002F     44 - GET_ITER            
                             00000030     5D - FOR_ITER            -> 000000B3
                             00000033     7D - STORE_FAST          'abil'
                             00000036     74 - LOAD_GLOBAL         'Utility'
                             00000039     69 - LOAD_ATTR           'getAbilityName'
                             0000003C     7C - LOAD_FAST           'abil'
                             0000003F     83 - CALL_FUNCTION       r0001
                             00000042     7D - STORE_FAST          'ab_name'
                             00000045     74 - LOAD_GLOBAL         'Utility'
                             00000048     69 - LOAD_ATTR           'outputAbilityDebug'
                             0000004B     64 - LOAD_CONST          '%s '
                             0000004E     7C - LOAD_FAST           'ab_name'
                             00000051     16 - BINARY_MODULO       
                             00000052     83 - CALL_FUNCTION       r0001
                             00000055     01 - POP_TOP             
                             00000056     7C - LOAD_FAST           'subject'
                             00000059     69 - LOAD_ATTR           'hasAbility'
                             0000005C     7C - LOAD_FAST           'abil'
                             0000005F     19 - BINARY_SUBSCR       
                             00000060     6F - JUMP_IF_FALSE       -> 000000AF
                             00000063     01 - POP_TOP             
                             00000064     74 - LOAD_GLOBAL         'Utility'
                             00000067     69 - LOAD_ATTR           'outputAbilityDebug'
                             0000006A     64 - LOAD_CONST          ' - disabling %s   '
                             0000006D     7C - LOAD_FAST           'ab_name'
                             00000070     16 - BINARY_MODULO       
                             00000071     83 - CALL_FUNCTION       r0001
                             00000074     01 - POP_TOP             
                             00000075     64 - LOAD_CONST          'GenericDisableInit'
                             00000078     64 - LOAD_CONST          'GenericDisableTerm'
                             0000007B     64 - LOAD_CONST          ''
                             0000007E     64 - LOAD_CONST          ''
                             00000081     64 - LOAD_CONST          ''
                             00000084     66 - BUILD_TUPLE         r0005
                             00000087     7D - STORE_FAST          'procs'
                             0000008A     7C - LOAD_FAST           'subject'
                             0000008D     69 - LOAD_ATTR           'AbilityInv'
                             00000090     69 - LOAD_ATTR           'addTempModProcs'
                             00000093     7C - LOAD_FAST           'procs'
                             00000096     74 - LOAD_GLOBAL         'abilitylib'
                             00000099     69 - LOAD_ATTR           'Disabled'
                             0000009C     7C - LOAD_FAST           'abil'
                             0000009F     7C - LOAD_FAST           'duration'
                             000000A2     64 - LOAD_CONST          0
                             000000A5     64 - LOAD_CONST          0
                             000000A8     83 - CALL_FUNCTION       r0006
                             000000AB     01 - POP_TOP             
                             000000AC     71 - JUMP_ABSOLUTE       -> 00000030
                             000000AF     01 - POP_TOP             
                             000000B0     71 - JUMP_ABSOLUTE       -> 00000030
                             000000B3     57 - POP_BLOCK           
                             000000B4     6E - JUMP_FORWARD        -> 000000B8
                             000000B7     01 - POP_TOP             
                             000000B8     64 - LOAD_CONST          None
                             000000BB     53 - RETURN_VALUE        
                         consts:
0000070A                     TUPLE: (
0000070F                         None (4E),
00000710                         STR: 'DisableDependents:' (12 00 00 00 44 69 73 61 62 6C 65 44 65 70 65 6E 64 65 6E 74 73 3A),
00000727                         STR: '%s ' (03 00 00 00 25 73 20),
0000072F                         STR: ' - disabling %s   ' (12 00 00 00 20 2D 20 64 69 73 61 62 6C 69 6E 67 20 25 73 20 20 20),
00000746                         STR: 'GenericDisableInit' (12 00 00 00 47 65 6E 65 72 69 63 44 69 73 61 62 6C 65 49 6E 69 74),
0000075D                         STR: 'GenericDisableTerm' (12 00 00 00 47 65 6E 65 72 69 63 44 69 73 61 62 6C 65 54 65 72 6D),
00000774                         STR: '' (00 00 00 00),
00000779                         INT: 0 (00 00 00 00)
                             )
                         names:
0000077E                     TUPLE: (
00000783                         STR: 'abilitylib' (0A 00 00 00 61 62 69 6C 69 74 79 6C 69 62),
00000792                         STR: 'getAbilityDependents' (14 00 00 00 67 65 74 41 62 69 6C 69 74 79 44 65 70 65 6E 64 65 6E 74 73),
000007AB                         STR: 'src_abil' (08 00 00 00 73 72 63 5F 61 62 69 6C),
000007B8                         STR: 'abil_list' (09 00 00 00 61 62 69 6C 5F 6C 69 73 74),
000007C6                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000007D2                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
000007E9                         STR: 'len' (03 00 00 00 6C 65 6E),
000007F1                         STR: 'abil' (04 00 00 00 61 62 69 6C),
000007FA                         STR: 'getAbilityName' (0E 00 00 00 67 65 74 41 62 69 6C 69 74 79 4E 61 6D 65),
0000080D                         STR: 'ab_name' (07 00 00 00 61 62 5F 6E 61 6D 65),
00000819                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000825                         STR: 'hasAbility' (0A 00 00 00 68 61 73 41 62 69 6C 69 74 79),
00000834                         STR: 'procs' (05 00 00 00 70 72 6F 63 73),
0000083E                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
0000084D                         STR: 'addTempModProcs' (0F 00 00 00 61 64 64 54 65 6D 70 4D 6F 64 50 72 6F 63 73),
00000861                         STR: 'Disabled' (08 00 00 00 44 69 73 61 62 6C 65 64),
0000086E                         STR: 'duration' (08 00 00 00 64 75 72 61 74 69 6F 6E)
                             )
                         varnames:
0000087B                     TUPLE: (
00000880                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000088C                         STR: 'src_abil' (08 00 00 00 73 72 63 5F 61 62 69 6C),
00000899                         STR: 'duration' (08 00 00 00 64 75 72 61 74 69 6F 6E),
000008A6                         STR: 'ab_name' (07 00 00 00 61 62 5F 6E 61 6D 65),
000008B2                         STR: 'abil_list' (09 00 00 00 61 62 69 6C 5F 6C 69 73 74),
000008C0                         STR: 'abil' (04 00 00 00 61 62 69 6C),
000008C9                         STR: 'procs' (05 00 00 00 70 72 6F 63 73)
                             )
                         freevars:
000008D3                     TUPLE: ()
                         cellvars:
000008D8                     TUPLE: ()
                         filename:
000008DD                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\effects.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 65 66 66 65 63 74 73 2E 70 79)
                         name:
00000929                     STR: 'DisableDependents' (11 00 00 00 44 69 73 61 62 6C 65 44 65 70 65 6E 64 65 6E 74 73)
                         firslineno:
0000093F                     LONG: 75L (4B 00 00 00)
                         lnotab:
00000943                     STR: '\x00\x03\x0f\x01\r\x03\r\x03\x07\x00\x06\x03\x0f\x01\x11\x03\x0e\x03\x11\x01\x15\x01\x0c\x01\x06\x01\x03\x01' (1C 00 00 00 00 03 0F 01 0D 03 0D 03 07 00 06 03 0F 01 11 03 0E 03 11 01 15 01 0C 01 06 01 03 01),
00000964             CODE:
                         argcount:
00000965                     LONG: 7L (07 00 00 00)
                         nlocals:
00000969                     LONG: 10L (0A 00 00 00)
                         stacksize:
0000096D                     LONG: 7L (07 00 00 00)
                         flags:
00000971                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000975                     STR: 't\x00\x00|\x00\x00|\x01\x00|\x03\x00\x83\x03\x00\x01t\x04\x00i\x05\x00|\x01\x00\x83\x01\x00}\x08\x00t\x04\x00i\x07\x00d\x01\x00|\x08\x00\x16\x83\x01\x00\x01d\x02\x00d\x03\x00d\x04\x00d\x04\x00d\x04\x00f\x05\x00}\t\x00|\x00\x00i\t\x00i\n\x00|\t\x00t\x0b\x00i\x0c\x00|\x01\x00|\x03\x00d\x05\x00d\x05\x00\x83\x06\x00\x01d\x05\x00}\x07\x00|\x05\x00o\n\x00\x01|\x01\x00}\x07\x00n\x10\x00\x01t\x0f\x00i\x10\x00|\x01\x00\x83\x01\x00}\x07\x00t\x0f\x00i\x11\x00|\x00\x00i\x12\x00|\x00\x00i\x12\x00t\x13\x00d\x05\x00\x83\x04\x00\x01d\x00\x00S' (AD 00 00 00 74 00 00 7C 00 00 7C 01 00 7C 03 00 83 03 00 01 74 04 00 69 05 00 7C 01 00 83 01 00 7D 08 00 74 04 00 69 07 00 64 01 00 7C 08 00 16 83 01 00 01 64 02 00 64 03 00 64 04 00 64 04 00 64 04 00 66 05 00 7D 09 00 7C 00 00 69 09 00 69 0A 00 7C 09 00 74 0B 00 69 0C 00 7C 01 00 7C 03 00 64 05 00 64 05 00 83 06 00 01 64 05 00 7D 07 00 7C 05 00 6F 0A 00 01 7C 01 00 7D 07 00 6E 10 00 01 74 0F 00 69 10 00 7C 01 00 83 01 00 7D 07 00 74 0F 00 69 11 00 7C 00 00 69 12 00 7C 00 00 69 12 00 74 13 00 64 05 00 83 04 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'DisableDependents'
                             00000003     7C - LOAD_FAST           'subject'
                             00000006     7C - LOAD_FAST           'targetAbility'
                             00000009     7C - LOAD_FAST           'duration'
                             0000000C     83 - CALL_FUNCTION       r0003
                             0000000F     01 - POP_TOP             
                             00000010     74 - LOAD_GLOBAL         'Utility'
                             00000013     69 - LOAD_ATTR           'getAbilityName'
                             00000016     7C - LOAD_FAST           'targetAbility'
                             00000019     83 - CALL_FUNCTION       r0001
                             0000001C     7D - STORE_FAST          'ab_name'
                             0000001F     74 - LOAD_GLOBAL         'Utility'
                             00000022     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000025     64 - LOAD_CONST          'DisableAbility: - disabling %s   '
                             00000028     7C - LOAD_FAST           'ab_name'
                             0000002B     16 - BINARY_MODULO       
                             0000002C     83 - CALL_FUNCTION       r0001
                             0000002F     01 - POP_TOP             
                             00000030     64 - LOAD_CONST          'GenericDisableInit'
                             00000033     64 - LOAD_CONST          'GenericDisableTerm'
                             00000036     64 - LOAD_CONST          ''
                             00000039     64 - LOAD_CONST          ''
                             0000003C     64 - LOAD_CONST          ''
                             0000003F     66 - BUILD_TUPLE         r0005
                             00000042     7D - STORE_FAST          'procs'
                             00000045     7C - LOAD_FAST           'subject'
                             00000048     69 - LOAD_ATTR           'AbilityInv'
                             0000004B     69 - LOAD_ATTR           'addTempModProcs'
                             0000004E     7C - LOAD_FAST           'procs'
                             00000051     74 - LOAD_GLOBAL         'abilitylib'
                             00000054     69 - LOAD_ATTR           'Disabled'
                             00000057     7C - LOAD_FAST           'targetAbility'
                             0000005A     7C - LOAD_FAST           'duration'
                             0000005D     64 - LOAD_CONST          0
                             00000060     64 - LOAD_CONST          0
                             00000063     83 - CALL_FUNCTION       r0006
                             00000066     01 - POP_TOP             
                             00000067     64 - LOAD_CONST          0
                             0000006A     7D - STORE_FAST          'type_id'
                             0000006D     7C - LOAD_FAST           'srcIsObject'
                             00000070     6F - JUMP_IF_FALSE       -> 0000007D
                             00000073     01 - POP_TOP             
                             00000074     7C - LOAD_FAST           'targetAbility'
                             00000077     7D - STORE_FAST          'type_id'
                             0000007A     6E - JUMP_FORWARD        -> 0000008D
                             0000007D     01 - POP_TOP             
                             0000007E     74 - LOAD_GLOBAL         'discovery'
                             00000081     69 - LOAD_ATTR           'abilityIDToGameObjectID'
                             00000084     7C - LOAD_FAST           'targetAbility'
                             00000087     83 - CALL_FUNCTION       r0001
                             0000008A     7D - STORE_FAST          'type_id'
                             0000008D     74 - LOAD_GLOBAL         'discovery'
                             00000090     69 - LOAD_ATTR           'playEffect'
                             00000093     7C - LOAD_FAST           'subject'
                             00000096     69 - LOAD_ATTR           'locator'
                             00000099     7C - LOAD_FAST           'subject'
                             0000009C     69 - LOAD_ATTR           'locator'
                             0000009F     74 - LOAD_GLOBAL         'DISABLE_FX'
                             000000A2     64 - LOAD_CONST          0
                             000000A5     83 - CALL_FUNCTION       r0004
                             000000A8     01 - POP_TOP             
                             000000A9     64 - LOAD_CONST          None
                             000000AC     53 - RETURN_VALUE        
                         consts:
00000A27                     TUPLE: (
00000A2C                         None (4E),
00000A2D                         STR: 'DisableAbility: - disabling %s   ' (21 00 00 00 44 69 73 61 62 6C 65 41 62 69 6C 69 74 79 3A 20 2D 20 64 69 73 61 62 6C 69 6E 67 20 25 73 20 20 20),
00000A53                         STR: 'GenericDisableInit' (12 00 00 00 47 65 6E 65 72 69 63 44 69 73 61 62 6C 65 49 6E 69 74),
00000A6A                         STR: 'GenericDisableTerm' (12 00 00 00 47 65 6E 65 72 69 63 44 69 73 61 62 6C 65 54 65 72 6D),
00000A81                         STR: '' (00 00 00 00),
00000A86                         INT: 0 (00 00 00 00)
                             )
                         names:
00000A8B                     TUPLE: (
00000A90                         STR: 'DisableDependents' (11 00 00 00 44 69 73 61 62 6C 65 44 65 70 65 6E 64 65 6E 74 73),
00000AA6                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000AB2                         STR: 'targetAbility' (0D 00 00 00 74 61 72 67 65 74 41 62 69 6C 69 74 79),
00000AC4                         STR: 'duration' (08 00 00 00 64 75 72 61 74 69 6F 6E),
00000AD1                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000ADD                         STR: 'getAbilityName' (0E 00 00 00 67 65 74 41 62 69 6C 69 74 79 4E 61 6D 65),
00000AF0                         STR: 'ab_name' (07 00 00 00 61 62 5F 6E 61 6D 65),
00000AFC                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000B13                         STR: 'procs' (05 00 00 00 70 72 6F 63 73),
00000B1D                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
00000B2C                         STR: 'addTempModProcs' (0F 00 00 00 61 64 64 54 65 6D 70 4D 6F 64 50 72 6F 63 73),
00000B40                         STR: 'abilitylib' (0A 00 00 00 61 62 69 6C 69 74 79 6C 69 62),
00000B4F                         STR: 'Disabled' (08 00 00 00 44 69 73 61 62 6C 65 64),
00000B5C                         STR: 'type_id' (07 00 00 00 74 79 70 65 5F 69 64),
00000B68                         STR: 'srcIsObject' (0B 00 00 00 73 72 63 49 73 4F 62 6A 65 63 74),
00000B78                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
00000B86                         STR: 'abilityIDToGameObjectID' (17 00 00 00 61 62 69 6C 69 74 79 49 44 54 6F 47 61 6D 65 4F 62 6A 65 63 74 49 44),
00000BA2                         STR: 'playEffect' (0A 00 00 00 70 6C 61 79 45 66 66 65 63 74),
00000BB1                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
00000BBD                         STR: 'DISABLE_FX' (0A 00 00 00 44 49 53 41 42 4C 45 5F 46 58)
                             )
                         varnames:
00000BCC                     TUPLE: (
00000BD1                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000BDD                         STR: 'targetAbility' (0D 00 00 00 74 61 72 67 65 74 41 62 69 6C 69 74 79),
00000BEF                         STR: 'src' (03 00 00 00 73 72 63),
00000BF7                         STR: 'duration' (08 00 00 00 64 75 72 61 74 69 6F 6E),
00000C04                         STR: 'casterLocator' (0D 00 00 00 63 61 73 74 65 72 4C 6F 63 61 74 6F 72),
00000C16                         STR: 'srcIsObject' (0B 00 00 00 73 72 63 49 73 4F 62 6A 65 63 74),
00000C26                         STR: 'sendMessage' (0B 00 00 00 73 65 6E 64 4D 65 73 73 61 67 65),
00000C36                         STR: 'type_id' (07 00 00 00 74 79 70 65 5F 69 64),
00000C42                         STR: 'ab_name' (07 00 00 00 61 62 5F 6E 61 6D 65),
00000C4E                         STR: 'procs' (05 00 00 00 70 72 6F 63 73)
                             )
                         freevars:
00000C58                     TUPLE: ()
                         cellvars:
00000C5D                     TUPLE: ()
                         filename:
00000C62                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\effects.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 65 66 66 65 63 74 73 2E 70 79)
                         name:
00000CAE                     STR: 'DisableAbility' (0E 00 00 00 44 69 73 61 62 6C 65 41 62 69 6C 69 74 79)
                         firslineno:
00000CC1                     LONG: 103L (67 00 00 00)
                         lnotab:
00000CC5                     STR: '\x00\x03\x10\x03\x0f\x01\x11\x02\x15\x01"\x03\x06\x01\x07\x01\n\x02\x0f\x02' (14 00 00 00 00 03 10 03 0F 01 11 02 15 01 22 03 06 01 07 01 0A 02 0F 02)
                 )
             names:
00000CDE         TUPLE: (
00000CE3             STR: 'combat_defines' (0E 00 00 00 63 6F 6D 62 61 74 5F 64 65 66 69 6E 65 73),
00000CF6             STR: 'CD' (02 00 00 00 43 44),
00000CFD             STR: 'ability.utility' (0F 00 00 00 61 62 69 6C 69 74 79 2E 75 74 69 6C 69 74 79),
00000D11             STR: 'utility' (07 00 00 00 75 74 69 6C 69 74 79),
00000D1D             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000D29             STR: 'ltfxmap' (07 00 00 00 6C 74 66 78 6D 61 70),
00000D35             STR: 'FX' (02 00 00 00 46 58),
00000D3C             STR: 'ability.defines' (0F 00 00 00 61 62 69 6C 69 74 79 2E 64 65 66 69 6E 65 73),
00000D50             STR: 'stringtable_client' (12 00 00 00 73 74 72 69 6E 67 74 61 62 6C 65 5F 63 6C 69 65 6E 74),
00000D67             STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00000D77             STR: 'CorrodeItem' (0B 00 00 00 43 6F 72 72 6F 64 65 49 74 65 6D),
00000D87             STR: 'DestroyItem' (0B 00 00 00 44 65 73 74 72 6F 79 49 74 65 6D),
00000D97             STR: 'FX_CHARACTER_GENERIC_ABILITY_DOWNGRADE' (26 00 00 00 46 58 5F 43 48 41 52 41 43 54 45 52 5F 47 45 4E 45 52 49 43 5F 41 42 49 4C 49 54 59 5F 44 4F 57 4E 47 52 41 44 45),
00000DC2             STR: 'DISABLE_FX' (0A 00 00 00 44 49 53 41 42 4C 45 5F 46 58),
00000DD1             STR: 'DisableDependents' (11 00 00 00 44 69 73 61 62 6C 65 44 65 70 65 6E 64 65 6E 74 73),
00000DE7             STR: 'True' (04 00 00 00 54 72 75 65),
00000DF0             STR: 'DisableAbility' (0E 00 00 00 44 69 73 61 62 6C 65 41 62 69 6C 69 74 79)
                 )
             varnames:
00000E03         TUPLE: (
00000E08             STR: 'DestroyItem' (0B 00 00 00 44 65 73 74 72 6F 79 49 74 65 6D),
00000E18             STR: 'DisableAbility' (0E 00 00 00 44 69 73 61 62 6C 65 41 62 69 6C 69 74 79),
00000E2B             STR: 'FX' (02 00 00 00 46 58),
00000E32             STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00000E42             STR: 'CD' (02 00 00 00 43 44),
00000E49             STR: 'DisableDependents' (11 00 00 00 44 69 73 61 62 6C 65 44 65 70 65 6E 64 65 6E 74 73),
00000E5F             STR: 'CorrodeItem' (0B 00 00 00 43 6F 72 72 6F 64 65 49 74 65 6D),
00000E6F             STR: 'DISABLE_FX' (0A 00 00 00 44 49 53 41 42 4C 45 5F 46 58),
00000E7E             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79)
                 )
             freevars:
00000E8A         TUPLE: ()
             cellvars:
00000E8F         TUPLE: ()
             filename:
00000E94         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\effects.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 65 66 66 65 63 74 73 2E 70 79)
             name:
00000EE0         STR: '?' (01 00 00 00 3F)
             firslineno:
00000EE6         LONG: 2L (02 00 00 00)
             lnotab:
00000EEA         STR: '\t\x01\x0c\x01\t\x01\x07\x01\t\x07\t \t\x1d\t\x01\t\x1c' (12 00 00 00 09 01 0C 01 09 01 07 01 09 07 09 20 09 1D 09 01 09 1C)

