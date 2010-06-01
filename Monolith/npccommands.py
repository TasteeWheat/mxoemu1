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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x02\x00d\x01\x00\x84\x00\x00Z\x03\x00d\x02\x00\x84\x00\x00Z\x04\x00d\x03\x00\x84\x00\x00Z\x05\x00d\x04\x00\x84\x00\x00Z\x06\x00d\x05\x00\x84\x00\x00Z\x07\x00e\x08\x00d\x06\x00\x84\x01\x00Z\t\x00e\x08\x00d\x07\x00\x84\x01\x00Z\n\x00d\x08\x00\x84\x00\x00Z\x0b\x00d\t\x00\x84\x00\x00Z\x0c\x00e\x08\x00d\n\x00\x84\x01\x00Z\r\x00d\x0b\x00\x84\x00\x00Z\x0e\x00d\x0c\x00\x84\x00\x00Z\x0f\x00d\r\x00\x84\x00\x00Z\x10\x00d\x0e\x00\x84\x00\x00Z\x11\x00d\x0f\x00\x84\x00\x00Z\x12\x00d\x10\x00\x84\x00\x00Z\x13\x00d\x11\x00\x84\x00\x00Z\x14\x00d\x12\x00\x84\x00\x00Z\x15\x00d\x13\x00\x84\x00\x00Z\x16\x00d\x14\x00\x84\x00\x00Z\x17\x00d\x15\x00\x84\x00\x00Z\x18\x00d\x00\x00S' (DC 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 02 00 64 01 00 84 00 00 5A 03 00 64 02 00 84 00 00 5A 04 00 64 03 00 84 00 00 5A 05 00 64 04 00 84 00 00 5A 06 00 64 05 00 84 00 00 5A 07 00 65 08 00 64 06 00 84 01 00 5A 09 00 65 08 00 64 07 00 84 01 00 5A 0A 00 64 08 00 84 00 00 5A 0B 00 64 09 00 84 00 00 5A 0C 00 65 08 00 64 0A 00 84 01 00 5A 0D 00 64 0B 00 84 00 00 5A 0E 00 64 0C 00 84 00 00 5A 0F 00 64 0D 00 84 00 00 5A 10 00 64 0E 00 84 00 00 5A 11 00 64 0F 00 84 00 00 5A 12 00 64 10 00 84 00 00 5A 13 00 64 11 00 84 00 00 5A 14 00 64 12 00 84 00 00 5A 15 00 64 13 00 84 00 00 5A 16 00 64 14 00 84 00 00 5A 17 00 64 15 00 84 00 00 5A 18 00 64 00 00 53)
                 00000000     64 - LOAD_CONST          None
                 00000003     6B - IMPORT_NAME         'traceback'
                 00000006     5A - STORE_NAME          'traceback'
                 00000009     64 - LOAD_CONST          None
                 0000000C     6B - IMPORT_NAME         'movement'
                 0000000F     5A - STORE_NAME          'Movement'
                 00000012     64 - LOAD_CONST          CODE('AttackNearestPlayer')
                 00000015     84 - MAKE_FUNCTION       r0000
                 00000018     5A - STORE_NAME          'AttackNearestPlayer'
                 0000001B     64 - LOAD_CONST          CODE('AttackNearestAI')
                 0000001E     84 - MAKE_FUNCTION       r0000
                 00000021     5A - STORE_NAME          'AttackNearestAI'
                 00000024     64 - LOAD_CONST          CODE('AttackMe')
                 00000027     84 - MAKE_FUNCTION       r0000
                 0000002A     5A - STORE_NAME          'AttackMe'
                 0000002D     64 - LOAD_CONST          CODE('FollowMe')
                 00000030     84 - MAKE_FUNCTION       r0000
                 00000033     5A - STORE_NAME          'FollowMe'
                 00000036     64 - LOAD_CONST          CODE('SetMood')
                 00000039     84 - MAKE_FUNCTION       r0000
                 0000003C     5A - STORE_NAME          'SetMood'
                 0000003F     65 - LOAD_NAME           'None'
                 00000042     64 - LOAD_CONST          CODE('NPCType')
                 00000045     84 - MAKE_FUNCTION       r0001
                 00000048     5A - STORE_NAME          'NPCType'
                 0000004B     65 - LOAD_NAME           'None'
                 0000004E     64 - LOAD_CONST          CODE('Behaviour')
                 00000051     84 - MAKE_FUNCTION       r0001
                 00000054     5A - STORE_NAME          'Behaviour'
                 00000057     64 - LOAD_CONST          CODE('AddUnkeyedItem')
                 0000005A     84 - MAKE_FUNCTION       r0000
                 0000005D     5A - STORE_NAME          'AddUnkeyedItem'
                 00000060     64 - LOAD_CONST          CODE('AddRewardItem')
                 00000063     84 - MAKE_FUNCTION       r0000
                 00000066     5A - STORE_NAME          'AddRewardItem'
                 00000069     65 - LOAD_NAME           'None'
                 0000006C     64 - LOAD_CONST          CODE('AddRewardGroup')
                 0000006F     84 - MAKE_FUNCTION       r0001
                 00000072     5A - STORE_NAME          'AddRewardGroup'
                 00000075     64 - LOAD_CONST          CODE('SetName')
                 00000078     84 - MAKE_FUNCTION       r0000
                 0000007B     5A - STORE_NAME          'SetName'
                 0000007E     64 - LOAD_CONST          CODE('NoLoot')
                 00000081     84 - MAKE_FUNCTION       r0000
                 00000084     5A - STORE_NAME          'NoLoot'
                 00000087     64 - LOAD_CONST          CODE('Immortal')
                 0000008A     84 - MAKE_FUNCTION       r0000
                 0000008D     5A - STORE_NAME          'Immortal'
                 00000090     64 - LOAD_CONST          CODE('Healthy')
                 00000093     84 - MAKE_FUNCTION       r0000
                 00000096     5A - STORE_NAME          'Healthy'
                 00000099     64 - LOAD_CONST          CODE('Wounded')
                 0000009C     84 - MAKE_FUNCTION       r0000
                 0000009F     5A - STORE_NAME          'Wounded'
                 000000A2     64 - LOAD_CONST          CODE('NearDead')
                 000000A5     84 - MAKE_FUNCTION       r0000
                 000000A8     5A - STORE_NAME          'NearDead'
                 000000AB     64 - LOAD_CONST          CODE('Dead')
                 000000AE     84 - MAKE_FUNCTION       r0000
                 000000B1     5A - STORE_NAME          'Dead'
                 000000B4     64 - LOAD_CONST          CODE('SetPermanentExclusion')
                 000000B7     84 - MAKE_FUNCTION       r0000
                 000000BA     5A - STORE_NAME          'SetPermanentExclusion'
                 000000BD     64 - LOAD_CONST          CODE('ExecuteAbilityOnNearestAI')
                 000000C0     84 - MAKE_FUNCTION       r0000
                 000000C3     5A - STORE_NAME          'ExecuteAbilityOnNearestAI'
                 000000C6     64 - LOAD_CONST          CODE('ExecuteAbilityOnSelf')
                 000000C9     84 - MAKE_FUNCTION       r0000
                 000000CC     5A - STORE_NAME          'ExecuteAbilityOnSelf'
                 000000CF     64 - LOAD_CONST          CODE('ExecuteAbilityOnMe')
                 000000D2     84 - MAKE_FUNCTION       r0000
                 000000D5     5A - STORE_NAME          'ExecuteAbilityOnMe'
                 000000D8     64 - LOAD_CONST          None
                 000000DB     53 - RETURN_VALUE        
             consts:
000000FA         TUPLE: (
000000FF             None (4E),
00000100             CODE:
                         argcount:
00000101                     LONG: 0L (00 00 00 00)
                         nlocals:
00000105                     LONG: 1L (01 00 00 00)
                         stacksize:
00000109                     LONG: 3L (03 00 00 00)
                         flags:
0000010D                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000111                     STR: 't\x00\x00i\x01\x00t\x02\x00i\x03\x00t\x02\x00i\x04\x00\x83\x02\x00}\x00\x00|\x00\x00o\x14\x00\x01t\x02\x00i\x06\x00i\x07\x00|\x00\x00\x83\x01\x00\x01n\x01\x00\x01d\x00\x00S' (37 00 00 00 74 00 00 69 01 00 74 02 00 69 03 00 74 02 00 69 04 00 83 02 00 7D 00 00 7C 00 00 6F 14 00 01 74 02 00 69 06 00 69 07 00 7C 00 00 83 01 00 01 6E 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'physics'
                             00000003     69 - LOAD_ATTR           'findNearestPlayer'
                             00000006     74 - LOAD_GLOBAL         'consoletarget'
                             00000009     69 - LOAD_ATTR           'Position'
                             0000000C     74 - LOAD_GLOBAL         'consoletarget'
                             0000000F     69 - LOAD_ATTR           'locator'
                             00000012     83 - CALL_FUNCTION       r0002
                             00000015     7D - STORE_FAST          'nearest_player'
                             00000018     7C - LOAD_FAST           'nearest_player'
                             0000001B     6F - JUMP_IF_FALSE       -> 00000032
                             0000001E     01 - POP_TOP             
                             0000001F     74 - LOAD_GLOBAL         'consoletarget'
                             00000022     69 - LOAD_ATTR           'AI'
                             00000025     69 - LOAD_ATTR           'attack'
                             00000028     7C - LOAD_FAST           'nearest_player'
                             0000002B     83 - CALL_FUNCTION       r0001
                             0000002E     01 - POP_TOP             
                             0000002F     6E - JUMP_FORWARD        -> 00000033
                             00000032     01 - POP_TOP             
                             00000033     64 - LOAD_CONST          None
                             00000036     53 - RETURN_VALUE        
                         consts:
0000014D                     TUPLE: (
00000152                         None (4E)
                             )
                         names:
00000153                     TUPLE: (
00000158                         STR: 'physics' (07 00 00 00 70 68 79 73 69 63 73),
00000164                         STR: 'findNearestPlayer' (11 00 00 00 66 69 6E 64 4E 65 61 72 65 73 74 50 6C 61 79 65 72),
0000017A                         STR: 'consoletarget' (0D 00 00 00 63 6F 6E 73 6F 6C 65 74 61 72 67 65 74),
0000018C                         STR: 'Position' (08 00 00 00 50 6F 73 69 74 69 6F 6E),
00000199                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
000001A5                         STR: 'nearest_player' (0E 00 00 00 6E 65 61 72 65 73 74 5F 70 6C 61 79 65 72),
000001B8                         STR: 'AI' (02 00 00 00 41 49),
000001BF                         STR: 'attack' (06 00 00 00 61 74 74 61 63 6B)
                             )
                         varnames:
000001CA                     TUPLE: (
000001CF                         STR: 'nearest_player' (0E 00 00 00 6E 65 61 72 65 73 74 5F 70 6C 61 79 65 72)
                             )
                         freevars:
000001E2                     TUPLE: ()
                         cellvars:
000001E7                     TUPLE: ()
                         filename:
000001EC                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
                         name:
00000234                     STR: 'AttackNearestPlayer' (13 00 00 00 41 74 74 61 63 6B 4E 65 61 72 65 73 74 50 6C 61 79 65 72)
                         firslineno:
0000024C                     LONG: 4L (04 00 00 00)
                         lnotab:
00000250                     STR: '\x00\x01\x18\x01\x07\x01' (06 00 00 00 00 01 18 01 07 01),
0000025B             CODE:
                         argcount:
0000025C                     LONG: 0L (00 00 00 00)
                         nlocals:
00000260                     LONG: 1L (01 00 00 00)
                         stacksize:
00000264                     LONG: 3L (03 00 00 00)
                         flags:
00000268                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000026C                     STR: 't\x00\x00i\x01\x00t\x02\x00i\x03\x00t\x02\x00i\x04\x00\x83\x02\x00}\x00\x00|\x00\x00o\x14\x00\x01t\x02\x00i\x06\x00i\x07\x00|\x00\x00\x83\x01\x00\x01n\x01\x00\x01d\x00\x00S' (37 00 00 00 74 00 00 69 01 00 74 02 00 69 03 00 74 02 00 69 04 00 83 02 00 7D 00 00 7C 00 00 6F 14 00 01 74 02 00 69 06 00 69 07 00 7C 00 00 83 01 00 01 6E 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'physics'
                             00000003     69 - LOAD_ATTR           'findNearestAI'
                             00000006     74 - LOAD_GLOBAL         'consoletarget'
                             00000009     69 - LOAD_ATTR           'Position'
                             0000000C     74 - LOAD_GLOBAL         'consoletarget'
                             0000000F     69 - LOAD_ATTR           'locator'
                             00000012     83 - CALL_FUNCTION       r0002
                             00000015     7D - STORE_FAST          'nearest_ai'
                             00000018     7C - LOAD_FAST           'nearest_ai'
                             0000001B     6F - JUMP_IF_FALSE       -> 00000032
                             0000001E     01 - POP_TOP             
                             0000001F     74 - LOAD_GLOBAL         'consoletarget'
                             00000022     69 - LOAD_ATTR           'AI'
                             00000025     69 - LOAD_ATTR           'attack'
                             00000028     7C - LOAD_FAST           'nearest_ai'
                             0000002B     83 - CALL_FUNCTION       r0001
                             0000002E     01 - POP_TOP             
                             0000002F     6E - JUMP_FORWARD        -> 00000033
                             00000032     01 - POP_TOP             
                             00000033     64 - LOAD_CONST          None
                             00000036     53 - RETURN_VALUE        
                         consts:
000002A8                     TUPLE: (
000002AD                         None (4E)
                             )
                         names:
000002AE                     TUPLE: (
000002B3                         STR: 'physics' (07 00 00 00 70 68 79 73 69 63 73),
000002BF                         STR: 'findNearestAI' (0D 00 00 00 66 69 6E 64 4E 65 61 72 65 73 74 41 49),
000002D1                         STR: 'consoletarget' (0D 00 00 00 63 6F 6E 73 6F 6C 65 74 61 72 67 65 74),
000002E3                         STR: 'Position' (08 00 00 00 50 6F 73 69 74 69 6F 6E),
000002F0                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
000002FC                         STR: 'nearest_ai' (0A 00 00 00 6E 65 61 72 65 73 74 5F 61 69),
0000030B                         STR: 'AI' (02 00 00 00 41 49),
00000312                         STR: 'attack' (06 00 00 00 61 74 74 61 63 6B)
                             )
                         varnames:
0000031D                     TUPLE: (
00000322                         STR: 'nearest_ai' (0A 00 00 00 6E 65 61 72 65 73 74 5F 61 69)
                             )
                         freevars:
00000331                     TUPLE: ()
                         cellvars:
00000336                     TUPLE: ()
                         filename:
0000033B                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
                         name:
00000383                     STR: 'AttackNearestAI' (0F 00 00 00 41 74 74 61 63 6B 4E 65 61 72 65 73 74 41 49)
                         firslineno:
00000397                     LONG: 9L (09 00 00 00)
                         lnotab:
0000039B                     STR: '\x00\x01\x18\x01\x07\x01' (06 00 00 00 00 01 18 01 07 01),
000003A6             CODE:
                         argcount:
000003A7                     LONG: 0L (00 00 00 00)
                         nlocals:
000003AB                     LONG: 0L (00 00 00 00)
                         stacksize:
000003AF                     LONG: 2L (02 00 00 00)
                         flags:
000003B3                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000003B7                     STR: 't\x00\x00i\x01\x00i\x02\x00t\x03\x00i\x04\x00\x83\x01\x00\x01d\x00\x00S' (17 00 00 00 74 00 00 69 01 00 69 02 00 74 03 00 69 04 00 83 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consoletarget'
                             00000003     69 - LOAD_ATTR           'AI'
                             00000006     69 - LOAD_ATTR           'attack'
                             00000009     74 - LOAD_GLOBAL         'consoleplayer'
                             0000000C     69 - LOAD_ATTR           'locator'
                             0000000F     83 - CALL_FUNCTION       r0001
                             00000012     01 - POP_TOP             
                             00000013     64 - LOAD_CONST          None
                             00000016     53 - RETURN_VALUE        
                         consts:
000003D3                     TUPLE: (
000003D8                         None (4E)
                             )
                         names:
000003D9                     TUPLE: (
000003DE                         STR: 'consoletarget' (0D 00 00 00 63 6F 6E 73 6F 6C 65 74 61 72 67 65 74),
000003F0                         STR: 'AI' (02 00 00 00 41 49),
000003F7                         STR: 'attack' (06 00 00 00 61 74 74 61 63 6B),
00000402                         STR: 'consoleplayer' (0D 00 00 00 63 6F 6E 73 6F 6C 65 70 6C 61 79 65 72),
00000414                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72)
                             )
                         varnames:
00000420                     TUPLE: ()
                         freevars:
00000425                     TUPLE: ()
                         cellvars:
0000042A                     TUPLE: ()
                         filename:
0000042F                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
                         name:
00000477                     STR: 'AttackMe' (08 00 00 00 41 74 74 61 63 6B 4D 65)
                         firslineno:
00000484                     LONG: 14L (0E 00 00 00)
                         lnotab:
00000488                     STR: '\x00\x01' (02 00 00 00 00 01),
0000048F             CODE:
                         argcount:
00000490                     LONG: 0L (00 00 00 00)
                         nlocals:
00000494                     LONG: 0L (00 00 00 00)
                         stacksize:
00000498                     LONG: 2L (02 00 00 00)
                         flags:
0000049C                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000004A0                     STR: 't\x00\x00i\x01\x00i\x02\x00t\x03\x00i\x04\x00\x83\x01\x00\x01d\x00\x00S' (17 00 00 00 74 00 00 69 01 00 69 02 00 74 03 00 69 04 00 83 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consoletarget'
                             00000003     69 - LOAD_ATTR           'AI'
                             00000006     69 - LOAD_ATTR           'followTarget'
                             00000009     74 - LOAD_GLOBAL         'consoleplayer'
                             0000000C     69 - LOAD_ATTR           'locator'
                             0000000F     83 - CALL_FUNCTION       r0001
                             00000012     01 - POP_TOP             
                             00000013     64 - LOAD_CONST          None
                             00000016     53 - RETURN_VALUE        
                         consts:
000004BC                     TUPLE: (
000004C1                         None (4E)
                             )
                         names:
000004C2                     TUPLE: (
000004C7                         STR: 'consoletarget' (0D 00 00 00 63 6F 6E 73 6F 6C 65 74 61 72 67 65 74),
000004D9                         STR: 'AI' (02 00 00 00 41 49),
000004E0                         STR: 'followTarget' (0C 00 00 00 66 6F 6C 6C 6F 77 54 61 72 67 65 74),
000004F1                         STR: 'consoleplayer' (0D 00 00 00 63 6F 6E 73 6F 6C 65 70 6C 61 79 65 72),
00000503                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72)
                             )
                         varnames:
0000050F                     TUPLE: ()
                         freevars:
00000514                     TUPLE: ()
                         cellvars:
00000519                     TUPLE: ()
                         filename:
0000051E                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
                         name:
00000566                     STR: 'FollowMe' (08 00 00 00 46 6F 6C 6C 6F 77 4D 65)
                         firslineno:
00000573                     LONG: 17L (11 00 00 00)
                         lnotab:
00000577                     STR: '\x00\x01' (02 00 00 00 00 01),
0000057E             CODE:
                         argcount:
0000057F                     LONG: 1L (01 00 00 00)
                         nlocals:
00000583                     LONG: 1L (01 00 00 00)
                         stacksize:
00000587                     LONG: 2L (02 00 00 00)
                         flags:
0000058B                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000058F                     STR: 't\x00\x00i\x01\x00i\x02\x00|\x00\x00\x83\x01\x00\x01d\x00\x00S' (14 00 00 00 74 00 00 69 01 00 69 02 00 7C 00 00 83 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consoletarget'
                             00000003     69 - LOAD_ATTR           'CharMvt'
                             00000006     69 - LOAD_ATTR           'setDemeanor'
                             00000009     7C - LOAD_FAST           'mood'
                             0000000C     83 - CALL_FUNCTION       r0001
                             0000000F     01 - POP_TOP             
                             00000010     64 - LOAD_CONST          None
                             00000013     53 - RETURN_VALUE        
                         consts:
000005A8                     TUPLE: (
000005AD                         None (4E)
                             )
                         names:
000005AE                     TUPLE: (
000005B3                         STR: 'consoletarget' (0D 00 00 00 63 6F 6E 73 6F 6C 65 74 61 72 67 65 74),
000005C5                         STR: 'CharMvt' (07 00 00 00 43 68 61 72 4D 76 74),
000005D1                         STR: 'setDemeanor' (0B 00 00 00 73 65 74 44 65 6D 65 61 6E 6F 72),
000005E1                         STR: 'mood' (04 00 00 00 6D 6F 6F 64)
                             )
                         varnames:
000005EA                     TUPLE: (
000005EF                         STR: 'mood' (04 00 00 00 6D 6F 6F 64)
                             )
                         freevars:
000005F8                     TUPLE: ()
                         cellvars:
000005FD                     TUPLE: ()
                         filename:
00000602                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
                         name:
0000064A                     STR: 'SetMood' (07 00 00 00 53 65 74 4D 6F 6F 64)
                         firslineno:
00000656                     LONG: 20L (14 00 00 00)
                         lnotab:
0000065A                     STR: '\x00\x01' (02 00 00 00 00 01),
00000661             CODE:
                         argcount:
00000662                     LONG: 1L (01 00 00 00)
                         nlocals:
00000666                     LONG: 1L (01 00 00 00)
                         stacksize:
0000066A                     LONG: 2L (02 00 00 00)
                         flags:
0000066E                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000672                     STR: 't\x00\x00i\x01\x00i\x02\x00|\x00\x00\x83\x01\x00\x01d\x00\x00S' (14 00 00 00 74 00 00 69 01 00 69 02 00 7C 00 00 83 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consoletarget'
                             00000003     69 - LOAD_ATTR           'AI'
                             00000006     69 - LOAD_ATTR           'NPCType'
                             00000009     7C - LOAD_FAST           'config'
                             0000000C     83 - CALL_FUNCTION       r0001
                             0000000F     01 - POP_TOP             
                             00000010     64 - LOAD_CONST          None
                             00000013     53 - RETURN_VALUE        
                         consts:
0000068B                     TUPLE: (
00000690                         None (4E)
                             )
                         names:
00000691                     TUPLE: (
00000696                         STR: 'consoletarget' (0D 00 00 00 63 6F 6E 73 6F 6C 65 74 61 72 67 65 74),
000006A8                         STR: 'AI' (02 00 00 00 41 49),
000006AF                         STR: 'NPCType' (07 00 00 00 4E 50 43 54 79 70 65),
000006BB                         STR: 'config' (06 00 00 00 63 6F 6E 66 69 67)
                             )
                         varnames:
000006C6                     TUPLE: (
000006CB                         STR: 'config' (06 00 00 00 63 6F 6E 66 69 67)
                             )
                         freevars:
000006D6                     TUPLE: ()
                         cellvars:
000006DB                     TUPLE: ()
                         filename:
000006E0                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
                         name:
00000728                     STR: 'NPCType' (07 00 00 00 4E 50 43 54 79 70 65)
                         firslineno:
00000734                     LONG: 23L (17 00 00 00)
                         lnotab:
00000738                     STR: '\x00\x01' (02 00 00 00 00 01),
0000073F             CODE:
                         argcount:
00000740                     LONG: 1L (01 00 00 00)
                         nlocals:
00000744                     LONG: 1L (01 00 00 00)
                         stacksize:
00000748                     LONG: 2L (02 00 00 00)
                         flags:
0000074C                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000750                     STR: 't\x00\x00i\x01\x00i\x02\x00|\x00\x00\x83\x01\x00\x01d\x00\x00S' (14 00 00 00 74 00 00 69 01 00 69 02 00 7C 00 00 83 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consoletarget'
                             00000003     69 - LOAD_ATTR           'AI'
                             00000006     69 - LOAD_ATTR           'behavior'
                             00000009     7C - LOAD_FAST           'config'
                             0000000C     83 - CALL_FUNCTION       r0001
                             0000000F     01 - POP_TOP             
                             00000010     64 - LOAD_CONST          None
                             00000013     53 - RETURN_VALUE        
                         consts:
00000769                     TUPLE: (
0000076E                         None (4E)
                             )
                         names:
0000076F                     TUPLE: (
00000774                         STR: 'consoletarget' (0D 00 00 00 63 6F 6E 73 6F 6C 65 74 61 72 67 65 74),
00000786                         STR: 'AI' (02 00 00 00 41 49),
0000078D                         STR: 'behavior' (08 00 00 00 62 65 68 61 76 69 6F 72),
0000079A                         STR: 'config' (06 00 00 00 63 6F 6E 66 69 67)
                             )
                         varnames:
000007A5                     TUPLE: (
000007AA                         STR: 'config' (06 00 00 00 63 6F 6E 66 69 67)
                             )
                         freevars:
000007B5                     TUPLE: ()
                         cellvars:
000007BA                     TUPLE: ()
                         filename:
000007BF                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
                         name:
00000807                     STR: 'Behaviour' (09 00 00 00 42 65 68 61 76 69 6F 75 72)
                         firslineno:
00000815                     LONG: 26L (1A 00 00 00)
                         lnotab:
00000819                     STR: '\x00\x01' (02 00 00 00 00 01),
00000820             CODE:
                         argcount:
00000821                     LONG: 1L (01 00 00 00)
                         nlocals:
00000825                     LONG: 1L (01 00 00 00)
                         stacksize:
00000829                     LONG: 2L (02 00 00 00)
                         flags:
0000082D                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000831                     STR: 't\x00\x00i\x01\x00i\x02\x00|\x00\x00\x83\x01\x00\x01d\x00\x00S' (14 00 00 00 74 00 00 69 01 00 69 02 00 7C 00 00 83 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consoletarget'
                             00000003     69 - LOAD_ATTR           'Container'
                             00000006     69 - LOAD_ATTR           'addStableItem'
                             00000009     7C - LOAD_FAST           'item'
                             0000000C     83 - CALL_FUNCTION       r0001
                             0000000F     01 - POP_TOP             
                             00000010     64 - LOAD_CONST          None
                             00000013     53 - RETURN_VALUE        
                         consts:
0000084A                     TUPLE: (
0000084F                         None (4E)
                             )
                         names:
00000850                     TUPLE: (
00000855                         STR: 'consoletarget' (0D 00 00 00 63 6F 6E 73 6F 6C 65 74 61 72 67 65 74),
00000867                         STR: 'Container' (09 00 00 00 43 6F 6E 74 61 69 6E 65 72),
00000875                         STR: 'addStableItem' (0D 00 00 00 61 64 64 53 74 61 62 6C 65 49 74 65 6D),
00000887                         STR: 'item' (04 00 00 00 69 74 65 6D)
                             )
                         varnames:
00000890                     TUPLE: (
00000895                         STR: 'item' (04 00 00 00 69 74 65 6D)
                             )
                         freevars:
0000089E                     TUPLE: ()
                         cellvars:
000008A3                     TUPLE: ()
                         filename:
000008A8                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
                         name:
000008F0                     STR: 'AddUnkeyedItem' (0E 00 00 00 41 64 64 55 6E 6B 65 79 65 64 49 74 65 6D)
                         firslineno:
00000903                     LONG: 29L (1D 00 00 00)
                         lnotab:
00000907                     STR: '\x00\x01' (02 00 00 00 00 01),
0000090E             CODE:
                         argcount:
0000090F                     LONG: 1L (01 00 00 00)
                         nlocals:
00000913                     LONG: 3L (03 00 00 00)
                         stacksize:
00000917                     LONG: 4L (04 00 00 00)
                         flags:
0000091B                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000091F                     STR: 't\x00\x00\x83\x00\x00}\x02\x00|\x02\x00i\x02\x00|\x00\x00\x83\x01\x00}\x01\x00|\x02\x00i\x05\x00|\x01\x00t\x06\x00i\x07\x00\x83\x02\x00\x01t\x06\x00i\x08\x00t\t\x00j\t\x00o\x1d\x00\x01t\x06\x00i\x08\x00i\n\x00t\x0b\x00t\x0c\x00d\x01\x00\x83\x02\x00\x83\x01\x00\x01n\x01\x00\x01d\x00\x00S' (5C 00 00 00 74 00 00 83 00 00 7D 02 00 7C 02 00 69 02 00 7C 00 00 83 01 00 7D 01 00 7C 02 00 69 05 00 7C 01 00 74 06 00 69 07 00 83 02 00 01 74 06 00 69 08 00 74 09 00 6A 09 00 6F 1D 00 01 74 06 00 69 08 00 69 0A 00 74 0B 00 74 0C 00 64 01 00 83 02 00 83 01 00 01 6E 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'RewardSelection'
                             00000003     83 - CALL_FUNCTION       r0000
                             00000006     7D - STORE_FAST          'rewardselection'
                             00000009     7C - LOAD_FAST           'rewardselection'
                             0000000C     69 - LOAD_ATTR           'Decode_Reward'
                             0000000F     7C - LOAD_FAST           'encodedReward'
                             00000012     83 - CALL_FUNCTION       r0001
                             00000015     7D - STORE_FAST          'rewards'
                             00000018     7C - LOAD_FAST           'rewardselection'
                             0000001B     69 - LOAD_ATTR           'Apply_Rewards'
                             0000001E     7C - LOAD_FAST           'rewards'
                             00000021     74 - LOAD_GLOBAL         'consoletarget'
                             00000024     69 - LOAD_ATTR           'Container'
                             00000027     83 - CALL_FUNCTION       r0002
                             0000002A     01 - POP_TOP             
                             0000002B     74 - LOAD_GLOBAL         'consoletarget'
                             0000002E     69 - LOAD_ATTR           'MissionElement'
                             00000031     74 - LOAD_GLOBAL         'None'
                             00000034     6A - COMPARE_OP          "is not"
                             00000037     6F - JUMP_IF_FALSE       -> 00000057
                             0000003A     01 - POP_TOP             
                             0000003B     74 - LOAD_GLOBAL         'consoletarget'
                             0000003E     69 - LOAD_ATTR           'MissionElement'
                             00000041     69 - LOAD_ATTR           'setMissionKey'
                             00000044     74 - LOAD_GLOBAL         'AddKeyOffset'
                             00000047     74 - LOAD_GLOBAL         'missionkey'
                             0000004A     64 - LOAD_CONST          255
                             0000004D     83 - CALL_FUNCTION       r0002
                             00000050     83 - CALL_FUNCTION       r0001
                             00000053     01 - POP_TOP             
                             00000054     6E - JUMP_FORWARD        -> 00000058
                             00000057     01 - POP_TOP             
                             00000058     64 - LOAD_CONST          None
                             0000005B     53 - RETURN_VALUE        
                         consts:
00000980                     TUPLE: (
00000985                         None (4E),
00000986                         INT: 255 (FF 00 00 00)
                             )
                         names:
0000098B                     TUPLE: (
00000990                         STR: 'RewardSelection' (0F 00 00 00 52 65 77 61 72 64 53 65 6C 65 63 74 69 6F 6E),
000009A4                         STR: 'rewardselection' (0F 00 00 00 72 65 77 61 72 64 73 65 6C 65 63 74 69 6F 6E),
000009B8                         STR: 'Decode_Reward' (0D 00 00 00 44 65 63 6F 64 65 5F 52 65 77 61 72 64),
000009CA                         STR: 'encodedReward' (0D 00 00 00 65 6E 63 6F 64 65 64 52 65 77 61 72 64),
000009DC                         STR: 'rewards' (07 00 00 00 72 65 77 61 72 64 73),
000009E8                         STR: 'Apply_Rewards' (0D 00 00 00 41 70 70 6C 79 5F 52 65 77 61 72 64 73),
000009FA                         STR: 'consoletarget' (0D 00 00 00 63 6F 6E 73 6F 6C 65 74 61 72 67 65 74),
00000A0C                         STR: 'Container' (09 00 00 00 43 6F 6E 74 61 69 6E 65 72),
00000A1A                         STR: 'MissionElement' (0E 00 00 00 4D 69 73 73 69 6F 6E 45 6C 65 6D 65 6E 74),
00000A2D                         STR: 'None' (04 00 00 00 4E 6F 6E 65),
00000A36                         STR: 'setMissionKey' (0D 00 00 00 73 65 74 4D 69 73 73 69 6F 6E 4B 65 79),
00000A48                         STR: 'AddKeyOffset' (0C 00 00 00 41 64 64 4B 65 79 4F 66 66 73 65 74),
00000A59                         STR: 'missionkey' (0A 00 00 00 6D 69 73 73 69 6F 6E 6B 65 79)
                             )
                         varnames:
00000A68                     TUPLE: (
00000A6D                         STR: 'encodedReward' (0D 00 00 00 65 6E 63 6F 64 65 64 52 65 77 61 72 64),
00000A7F                         STR: 'rewards' (07 00 00 00 72 65 77 61 72 64 73),
00000A8B                         STR: 'rewardselection' (0F 00 00 00 72 65 77 61 72 64 73 65 6C 65 63 74 69 6F 6E)
                             )
                         freevars:
00000A9F                     TUPLE: ()
                         cellvars:
00000AA4                     TUPLE: ()
                         filename:
00000AA9                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
                         name:
00000AF1                     STR: 'AddRewardItem' (0D 00 00 00 41 64 64 52 65 77 61 72 64 49 74 65 6D)
                         firslineno:
00000B03                     LONG: 32L (20 00 00 00)
                         lnotab:
00000B07                     STR: '\x00\x01\t\x01\x0f\x01\x13\x01\x10\x01' (0A 00 00 00 00 01 09 01 0F 01 13 01 10 01),
00000B16             CODE:
                         argcount:
00000B17                     LONG: 2L (02 00 00 00)
                         nlocals:
00000B1B                     LONG: 3L (03 00 00 00)
                         stacksize:
00000B1F                     LONG: 4L (04 00 00 00)
                         flags:
00000B23                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000B27                     STR: '|\x01\x00t\x01\x00j\t\x00o\r\x00\x01|\x01\x00t\x02\x00_\x03\x00n\x01\x00\x01t\x04\x00\x83\x00\x00}\x02\x00|\x02\x00i\x06\x00d\x01\x00|\x00\x00t\x02\x00i\x08\x00\x83\x03\x00\x01t\x02\x00i\t\x00t\x01\x00j\t\x00o\x1d\x00\x01t\x02\x00i\t\x00i\n\x00t\x0b\x00t\x0c\x00d\x02\x00\x83\x02\x00\x83\x01\x00\x01n\x01\x00\x01d\x00\x00S' (6A 00 00 00 7C 01 00 74 01 00 6A 09 00 6F 0D 00 01 7C 01 00 74 02 00 5F 03 00 6E 01 00 01 74 04 00 83 00 00 7D 02 00 7C 02 00 69 06 00 64 01 00 7C 00 00 74 02 00 69 08 00 83 03 00 01 74 02 00 69 09 00 74 01 00 6A 09 00 6F 1D 00 01 74 02 00 69 09 00 69 0A 00 74 0B 00 74 0C 00 64 02 00 83 02 00 83 01 00 01 6E 01 00 01 64 00 00 53)
                             00000000     7C - LOAD_FAST           'teamlevel'
                             00000003     74 - LOAD_GLOBAL         'None'
                             00000006     6A - COMPARE_OP          "is not"
                             00000009     6F - JUMP_IF_FALSE       -> 00000019
                             0000000C     01 - POP_TOP             
                             0000000D     7C - LOAD_FAST           'teamlevel'
                             00000010     74 - LOAD_GLOBAL         'consoletarget'
                             00000013     5F - STORE_ATTR          'TeamLevel'
                             00000016     6E - JUMP_FORWARD        -> 0000001A
                             00000019     01 - POP_TOP             
                             0000001A     74 - LOAD_GLOBAL         'RewardSelection'
                             0000001D     83 - CALL_FUNCTION       r0000
                             00000020     7D - STORE_FAST          'rewardselection'
                             00000023     7C - LOAD_FAST           'rewardselection'
                             00000026     69 - LOAD_ATTR           'DeterminePopulateReward'
                             00000029     64 - LOAD_CONST          'TeamLevelRewardRule'
                             0000002C     7C - LOAD_FAST           'rewardtable'
                             0000002F     74 - LOAD_GLOBAL         'consoletarget'
                             00000032     69 - LOAD_ATTR           'Container'
                             00000035     83 - CALL_FUNCTION       r0003
                             00000038     01 - POP_TOP             
                             00000039     74 - LOAD_GLOBAL         'consoletarget'
                             0000003C     69 - LOAD_ATTR           'MissionElement'
                             0000003F     74 - LOAD_GLOBAL         'None'
                             00000042     6A - COMPARE_OP          "is not"
                             00000045     6F - JUMP_IF_FALSE       -> 00000065
                             00000048     01 - POP_TOP             
                             00000049     74 - LOAD_GLOBAL         'consoletarget'
                             0000004C     69 - LOAD_ATTR           'MissionElement'
                             0000004F     69 - LOAD_ATTR           'setMissionKey'
                             00000052     74 - LOAD_GLOBAL         'AddKeyOffset'
                             00000055     74 - LOAD_GLOBAL         'missionkey'
                             00000058     64 - LOAD_CONST          255
                             0000005B     83 - CALL_FUNCTION       r0002
                             0000005E     83 - CALL_FUNCTION       r0001
                             00000061     01 - POP_TOP             
                             00000062     6E - JUMP_FORWARD        -> 00000066
                             00000065     01 - POP_TOP             
                             00000066     64 - LOAD_CONST          None
                             00000069     53 - RETURN_VALUE        
                         consts:
00000B96                     TUPLE: (
00000B9B                         None (4E),
00000B9C                         STR: 'TeamLevelRewardRule' (13 00 00 00 54 65 61 6D 4C 65 76 65 6C 52 65 77 61 72 64 52 75 6C 65),
00000BB4                         INT: 255 (FF 00 00 00)
                             )
                         names:
00000BB9                     TUPLE: (
00000BBE                         STR: 'teamlevel' (09 00 00 00 74 65 61 6D 6C 65 76 65 6C),
00000BCC                         STR: 'None' (04 00 00 00 4E 6F 6E 65),
00000BD5                         STR: 'consoletarget' (0D 00 00 00 63 6F 6E 73 6F 6C 65 74 61 72 67 65 74),
00000BE7                         STR: 'TeamLevel' (09 00 00 00 54 65 61 6D 4C 65 76 65 6C),
00000BF5                         STR: 'RewardSelection' (0F 00 00 00 52 65 77 61 72 64 53 65 6C 65 63 74 69 6F 6E),
00000C09                         STR: 'rewardselection' (0F 00 00 00 72 65 77 61 72 64 73 65 6C 65 63 74 69 6F 6E),
00000C1D                         STR: 'DeterminePopulateReward' (17 00 00 00 44 65 74 65 72 6D 69 6E 65 50 6F 70 75 6C 61 74 65 52 65 77 61 72 64),
00000C39                         STR: 'rewardtable' (0B 00 00 00 72 65 77 61 72 64 74 61 62 6C 65),
00000C49                         STR: 'Container' (09 00 00 00 43 6F 6E 74 61 69 6E 65 72),
00000C57                         STR: 'MissionElement' (0E 00 00 00 4D 69 73 73 69 6F 6E 45 6C 65 6D 65 6E 74),
00000C6A                         STR: 'setMissionKey' (0D 00 00 00 73 65 74 4D 69 73 73 69 6F 6E 4B 65 79),
00000C7C                         STR: 'AddKeyOffset' (0C 00 00 00 41 64 64 4B 65 79 4F 66 66 73 65 74),
00000C8D                         STR: 'missionkey' (0A 00 00 00 6D 69 73 73 69 6F 6E 6B 65 79)
                             )
                         varnames:
00000C9C                     TUPLE: (
00000CA1                         STR: 'rewardtable' (0B 00 00 00 72 65 77 61 72 64 74 61 62 6C 65),
00000CB1                         STR: 'teamlevel' (09 00 00 00 74 65 61 6D 6C 65 76 65 6C),
00000CBF                         STR: 'rewardselection' (0F 00 00 00 72 65 77 61 72 64 73 65 6C 65 63 74 69 6F 6E)
                             )
                         freevars:
00000CD3                     TUPLE: ()
                         cellvars:
00000CD8                     TUPLE: ()
                         filename:
00000CDD                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
                         name:
00000D25                     STR: 'AddRewardGroup' (0E 00 00 00 41 64 64 52 65 77 61 72 64 47 72 6F 75 70)
                         firslineno:
00000D38                     LONG: 39L (27 00 00 00)
                         lnotab:
00000D3C                     STR: '\x00\x02\r\x01\r\x02\t\x01\x16\x01\x10\x01' (0C 00 00 00 00 02 0D 01 0D 02 09 01 16 01 10 01),
00000D4D             CODE:
                         argcount:
00000D4E                     LONG: 1L (01 00 00 00)
                         nlocals:
00000D52                     LONG: 1L (01 00 00 00)
                         stacksize:
00000D56                     LONG: 2L (02 00 00 00)
                         flags:
00000D5A                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000D5E                     STR: 'd\x01\x00t\x00\x00i\x01\x00_\x02\x00t\x00\x00i\x03\x00i\x04\x00|\x00\x00\x83\x01\x00\x01d\x00\x00S' (20 00 00 00 64 01 00 74 00 00 69 01 00 5F 02 00 74 00 00 69 03 00 69 04 00 7C 00 00 83 01 00 01 64 00 00 53)
                             00000000     64 - LOAD_CONST          1
                             00000003     74 - LOAD_GLOBAL         'consoletarget'
                             00000006     69 - LOAD_ATTR           'AI'
                             00000009     5F - STORE_ATTR          'NamedCharacterChat'
                             0000000C     74 - LOAD_GLOBAL         'consoletarget'
                             0000000F     69 - LOAD_ATTR           'CharacterBase'
                             00000012     69 - LOAD_ATTR           'setName'
                             00000015     7C - LOAD_FAST           'npcname'
                             00000018     83 - CALL_FUNCTION       r0001
                             0000001B     01 - POP_TOP             
                             0000001C     64 - LOAD_CONST          None
                             0000001F     53 - RETURN_VALUE        
                         consts:
00000D83                     TUPLE: (
00000D88                         None (4E),
00000D89                         INT: 1 (01 00 00 00)
                             )
                         names:
00000D8E                     TUPLE: (
00000D93                         STR: 'consoletarget' (0D 00 00 00 63 6F 6E 73 6F 6C 65 74 61 72 67 65 74),
00000DA5                         STR: 'AI' (02 00 00 00 41 49),
00000DAC                         STR: 'NamedCharacterChat' (12 00 00 00 4E 61 6D 65 64 43 68 61 72 61 63 74 65 72 43 68 61 74),
00000DC3                         STR: 'CharacterBase' (0D 00 00 00 43 68 61 72 61 63 74 65 72 42 61 73 65),
00000DD5                         STR: 'setName' (07 00 00 00 73 65 74 4E 61 6D 65),
00000DE1                         STR: 'npcname' (07 00 00 00 6E 70 63 6E 61 6D 65)
                             )
                         varnames:
00000DED                     TUPLE: (
00000DF2                         STR: 'npcname' (07 00 00 00 6E 70 63 6E 61 6D 65)
                             )
                         freevars:
00000DFE                     TUPLE: ()
                         cellvars:
00000E03                     TUPLE: ()
                         filename:
00000E08                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
                         name:
00000E50                     STR: 'SetName' (07 00 00 00 53 65 74 4E 61 6D 65)
                         firslineno:
00000E5C                     LONG: 49L (31 00 00 00)
                         lnotab:
00000E60                     STR: '\x00\x01\x0c\x01' (04 00 00 00 00 01 0C 01),
00000E69             CODE:
                         argcount:
00000E6A                     LONG: 0L (00 00 00 00)
                         nlocals:
00000E6E                     LONG: 0L (00 00 00 00)
                         stacksize:
00000E72                     LONG: 2L (02 00 00 00)
                         flags:
00000E76                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000E7A                     STR: 't\x00\x00t\x01\x00i\x02\x00_\x03\x00t\x00\x00t\x01\x00i\x02\x00_\x04\x00d\x00\x00S' (1C 00 00 00 74 00 00 74 01 00 69 02 00 5F 03 00 74 00 00 74 01 00 69 02 00 5F 04 00 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'None'
                             00000003     74 - LOAD_GLOBAL         'consoletarget'
                             00000006     69 - LOAD_ATTR           'Rewards'
                             00000009     5F - STORE_ATTR          'RewardTable'
                             0000000C     74 - LOAD_GLOBAL         'None'
                             0000000F     74 - LOAD_GLOBAL         'consoletarget'
                             00000012     69 - LOAD_ATTR           'Rewards'
                             00000015     5F - STORE_ATTR          'RewardRule'
                             00000018     64 - LOAD_CONST          None
                             0000001B     53 - RETURN_VALUE        
                         consts:
00000E9B                     TUPLE: (
00000EA0                         None (4E)
                             )
                         names:
00000EA1                     TUPLE: (
00000EA6                         STR: 'None' (04 00 00 00 4E 6F 6E 65),
00000EAF                         STR: 'consoletarget' (0D 00 00 00 63 6F 6E 73 6F 6C 65 74 61 72 67 65 74),
00000EC1                         STR: 'Rewards' (07 00 00 00 52 65 77 61 72 64 73),
00000ECD                         STR: 'RewardTable' (0B 00 00 00 52 65 77 61 72 64 54 61 62 6C 65),
00000EDD                         STR: 'RewardRule' (0A 00 00 00 52 65 77 61 72 64 52 75 6C 65)
                             )
                         varnames:
00000EEC                     TUPLE: ()
                         freevars:
00000EF1                     TUPLE: ()
                         cellvars:
00000EF6                     TUPLE: ()
                         filename:
00000EFB                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
                         name:
00000F43                     STR: 'NoLoot' (06 00 00 00 4E 6F 4C 6F 6F 74)
                         firslineno:
00000F4E                     LONG: 53L (35 00 00 00)
                         lnotab:
00000F52                     STR: '\x00\x01\x0c\x01' (04 00 00 00 00 01 0C 01),
00000F5B             CODE:
                         argcount:
00000F5C                     LONG: 0L (00 00 00 00)
                         nlocals:
00000F60                     LONG: 0L (00 00 00 00)
                         stacksize:
00000F64                     LONG: 1L (01 00 00 00)
                         flags:
00000F68                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000F6C                     STR: 't\x00\x00i\x01\x00i\x02\x00\x83\x00\x00\x01d\x00\x00S' (11 00 00 00 74 00 00 69 01 00 69 02 00 83 00 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consoletarget'
                             00000003     69 - LOAD_ATTR           'AI'
                             00000006     69 - LOAD_ATTR           'immortal'
                             00000009     83 - CALL_FUNCTION       r0000
                             0000000C     01 - POP_TOP             
                             0000000D     64 - LOAD_CONST          None
                             00000010     53 - RETURN_VALUE        
                         consts:
00000F82                     TUPLE: (
00000F87                         None (4E)
                             )
                         names:
00000F88                     TUPLE: (
00000F8D                         STR: 'consoletarget' (0D 00 00 00 63 6F 6E 73 6F 6C 65 74 61 72 67 65 74),
00000F9F                         STR: 'AI' (02 00 00 00 41 49),
00000FA6                         STR: 'immortal' (08 00 00 00 69 6D 6D 6F 72 74 61 6C)
                             )
                         varnames:
00000FB3                     TUPLE: ()
                         freevars:
00000FB8                     TUPLE: ()
                         cellvars:
00000FBD                     TUPLE: ()
                         filename:
00000FC2                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
                         name:
0000100A                     STR: 'Immortal' (08 00 00 00 49 6D 6D 6F 72 74 61 6C)
                         firslineno:
00001017                     LONG: 57L (39 00 00 00)
                         lnotab:
0000101B                     STR: '\x00\x01' (02 00 00 00 00 01),
00001022             CODE:
                         argcount:
00001023                     LONG: 0L (00 00 00 00)
                         nlocals:
00001027                     LONG: 0L (00 00 00 00)
                         stacksize:
0000102B                     LONG: 1L (01 00 00 00)
                         flags:
0000102F                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001033                     STR: 't\x00\x00i\x01\x00i\x02\x00\x83\x00\x00\x01d\x00\x00S' (11 00 00 00 74 00 00 69 01 00 69 02 00 83 00 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consoletarget'
                             00000003     69 - LOAD_ATTR           'AI'
                             00000006     69 - LOAD_ATTR           'healthy'
                             00000009     83 - CALL_FUNCTION       r0000
                             0000000C     01 - POP_TOP             
                             0000000D     64 - LOAD_CONST          None
                             00000010     53 - RETURN_VALUE        
                         consts:
00001049                     TUPLE: (
0000104E                         None (4E)
                             )
                         names:
0000104F                     TUPLE: (
00001054                         STR: 'consoletarget' (0D 00 00 00 63 6F 6E 73 6F 6C 65 74 61 72 67 65 74),
00001066                         STR: 'AI' (02 00 00 00 41 49),
0000106D                         STR: 'healthy' (07 00 00 00 68 65 61 6C 74 68 79)
                             )
                         varnames:
00001079                     TUPLE: ()
                         freevars:
0000107E                     TUPLE: ()
                         cellvars:
00001083                     TUPLE: ()
                         filename:
00001088                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
                         name:
000010D0                     STR: 'Healthy' (07 00 00 00 48 65 61 6C 74 68 79)
                         firslineno:
000010DC                     LONG: 60L (3C 00 00 00)
                         lnotab:
000010E0                     STR: '\x00\x01' (02 00 00 00 00 01),
000010E7             CODE:
                         argcount:
000010E8                     LONG: 0L (00 00 00 00)
                         nlocals:
000010EC                     LONG: 0L (00 00 00 00)
                         stacksize:
000010F0                     LONG: 1L (01 00 00 00)
                         flags:
000010F4                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000010F8                     STR: 't\x00\x00i\x01\x00i\x02\x00\x83\x00\x00\x01d\x00\x00S' (11 00 00 00 74 00 00 69 01 00 69 02 00 83 00 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consoletarget'
                             00000003     69 - LOAD_ATTR           'AI'
                             00000006     69 - LOAD_ATTR           'wounded'
                             00000009     83 - CALL_FUNCTION       r0000
                             0000000C     01 - POP_TOP             
                             0000000D     64 - LOAD_CONST          None
                             00000010     53 - RETURN_VALUE        
                         consts:
0000110E                     TUPLE: (
00001113                         None (4E)
                             )
                         names:
00001114                     TUPLE: (
00001119                         STR: 'consoletarget' (0D 00 00 00 63 6F 6E 73 6F 6C 65 74 61 72 67 65 74),
0000112B                         STR: 'AI' (02 00 00 00 41 49),
00001132                         STR: 'wounded' (07 00 00 00 77 6F 75 6E 64 65 64)
                             )
                         varnames:
0000113E                     TUPLE: ()
                         freevars:
00001143                     TUPLE: ()
                         cellvars:
00001148                     TUPLE: ()
                         filename:
0000114D                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
                         name:
00001195                     STR: 'Wounded' (07 00 00 00 57 6F 75 6E 64 65 64)
                         firslineno:
000011A1                     LONG: 63L (3F 00 00 00)
                         lnotab:
000011A5                     STR: '\x00\x01' (02 00 00 00 00 01),
000011AC             CODE:
                         argcount:
000011AD                     LONG: 0L (00 00 00 00)
                         nlocals:
000011B1                     LONG: 0L (00 00 00 00)
                         stacksize:
000011B5                     LONG: 1L (01 00 00 00)
                         flags:
000011B9                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000011BD                     STR: 't\x00\x00i\x01\x00i\x02\x00\x83\x00\x00\x01d\x00\x00S' (11 00 00 00 74 00 00 69 01 00 69 02 00 83 00 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consoletarget'
                             00000003     69 - LOAD_ATTR           'AI'
                             00000006     69 - LOAD_ATTR           'neardead'
                             00000009     83 - CALL_FUNCTION       r0000
                             0000000C     01 - POP_TOP             
                             0000000D     64 - LOAD_CONST          None
                             00000010     53 - RETURN_VALUE        
                         consts:
000011D3                     TUPLE: (
000011D8                         None (4E)
                             )
                         names:
000011D9                     TUPLE: (
000011DE                         STR: 'consoletarget' (0D 00 00 00 63 6F 6E 73 6F 6C 65 74 61 72 67 65 74),
000011F0                         STR: 'AI' (02 00 00 00 41 49),
000011F7                         STR: 'neardead' (08 00 00 00 6E 65 61 72 64 65 61 64)
                             )
                         varnames:
00001204                     TUPLE: ()
                         freevars:
00001209                     TUPLE: ()
                         cellvars:
0000120E                     TUPLE: ()
                         filename:
00001213                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
                         name:
0000125B                     STR: 'NearDead' (08 00 00 00 4E 65 61 72 44 65 61 64)
                         firslineno:
00001268                     LONG: 66L (42 00 00 00)
                         lnotab:
0000126C                     STR: '\x00\x01' (02 00 00 00 00 01),
00001273             CODE:
                         argcount:
00001274                     LONG: 0L (00 00 00 00)
                         nlocals:
00001278                     LONG: 0L (00 00 00 00)
                         stacksize:
0000127C                     LONG: 1L (01 00 00 00)
                         flags:
00001280                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001284                     STR: 't\x00\x00i\x01\x00i\x02\x00\x83\x00\x00\x01d\x00\x00S' (11 00 00 00 74 00 00 69 01 00 69 02 00 83 00 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consoletarget'
                             00000003     69 - LOAD_ATTR           'AI'
                             00000006     69 - LOAD_ATTR           'dead'
                             00000009     83 - CALL_FUNCTION       r0000
                             0000000C     01 - POP_TOP             
                             0000000D     64 - LOAD_CONST          None
                             00000010     53 - RETURN_VALUE        
                         consts:
0000129A                     TUPLE: (
0000129F                         None (4E)
                             )
                         names:
000012A0                     TUPLE: (
000012A5                         STR: 'consoletarget' (0D 00 00 00 63 6F 6E 73 6F 6C 65 74 61 72 67 65 74),
000012B7                         STR: 'AI' (02 00 00 00 41 49),
000012BE                         STR: 'dead' (04 00 00 00 64 65 61 64)
                             )
                         varnames:
000012C7                     TUPLE: ()
                         freevars:
000012CC                     TUPLE: ()
                         cellvars:
000012D1                     TUPLE: ()
                         filename:
000012D6                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
                         name:
0000131E                     STR: 'Dead' (04 00 00 00 44 65 61 64)
                         firslineno:
00001327                     LONG: 69L (45 00 00 00)
                         lnotab:
0000132B                     STR: '\x00\x01' (02 00 00 00 00 01),
00001332             CODE:
                         argcount:
00001333                     LONG: 1L (01 00 00 00)
                         nlocals:
00001337                     LONG: 1L (01 00 00 00)
                         stacksize:
0000133B                     LONG: 2L (02 00 00 00)
                         flags:
0000133F                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001343                     STR: 't\x00\x00i\x01\x00i\x02\x00|\x00\x00\x83\x01\x00\x01d\x00\x00S' (14 00 00 00 74 00 00 69 01 00 69 02 00 7C 00 00 83 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consoletarget'
                             00000003     69 - LOAD_ATTR           'Container'
                             00000006     69 - LOAD_ATTR           'setPermanentExclusion'
                             00000009     7C - LOAD_FAST           'playerid'
                             0000000C     83 - CALL_FUNCTION       r0001
                             0000000F     01 - POP_TOP             
                             00000010     64 - LOAD_CONST          None
                             00000013     53 - RETURN_VALUE        
                         consts:
0000135C                     TUPLE: (
00001361                         None (4E)
                             )
                         names:
00001362                     TUPLE: (
00001367                         STR: 'consoletarget' (0D 00 00 00 63 6F 6E 73 6F 6C 65 74 61 72 67 65 74),
00001379                         STR: 'Container' (09 00 00 00 43 6F 6E 74 61 69 6E 65 72),
00001387                         STR: 'setPermanentExclusion' (15 00 00 00 73 65 74 50 65 72 6D 61 6E 65 6E 74 45 78 63 6C 75 73 69 6F 6E),
000013A1                         STR: 'playerid' (08 00 00 00 70 6C 61 79 65 72 69 64)
                             )
                         varnames:
000013AE                     TUPLE: (
000013B3                         STR: 'playerid' (08 00 00 00 70 6C 61 79 65 72 69 64)
                             )
                         freevars:
000013C0                     TUPLE: ()
                         cellvars:
000013C5                     TUPLE: ()
                         filename:
000013CA                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
                         name:
00001412                     STR: 'SetPermanentExclusion' (15 00 00 00 53 65 74 50 65 72 6D 61 6E 65 6E 74 45 78 63 6C 75 73 69 6F 6E)
                         firslineno:
0000142C                     LONG: 72L (48 00 00 00)
                         lnotab:
00001430                     STR: '\x00\x01' (02 00 00 00 00 01),
00001437             CODE:
                         argcount:
00001438                     LONG: 1L (01 00 00 00)
                         nlocals:
0000143C                     LONG: 2L (02 00 00 00)
                         stacksize:
00001440                     LONG: 3L (03 00 00 00)
                         flags:
00001444                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001448                     STR: 't\x00\x00i\x01\x00t\x02\x00i\x03\x00t\x02\x00i\x04\x00\x83\x02\x00}\x01\x00|\x01\x00o\x17\x00\x01t\x02\x00i\x06\x00i\x07\x00|\x00\x00|\x01\x00\x83\x02\x00\x01n\x01\x00\x01d\x00\x00S' (3A 00 00 00 74 00 00 69 01 00 74 02 00 69 03 00 74 02 00 69 04 00 83 02 00 7D 01 00 7C 01 00 6F 17 00 01 74 02 00 69 06 00 69 07 00 7C 00 00 7C 01 00 83 02 00 01 6E 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'physics'
                             00000003     69 - LOAD_ATTR           'findNearestAI'
                             00000006     74 - LOAD_GLOBAL         'consoletarget'
                             00000009     69 - LOAD_ATTR           'Position'
                             0000000C     74 - LOAD_GLOBAL         'consoletarget'
                             0000000F     69 - LOAD_ATTR           'locator'
                             00000012     83 - CALL_FUNCTION       r0002
                             00000015     7D - STORE_FAST          'nearest_ai'
                             00000018     7C - LOAD_FAST           'nearest_ai'
                             0000001B     6F - JUMP_IF_FALSE       -> 00000035
                             0000001E     01 - POP_TOP             
                             0000001F     74 - LOAD_GLOBAL         'consoletarget'
                             00000022     69 - LOAD_ATTR           'AI'
                             00000025     69 - LOAD_ATTR           'executeAbility'
                             00000028     7C - LOAD_FAST           'abilityid'
                             0000002B     7C - LOAD_FAST           'nearest_ai'
                             0000002E     83 - CALL_FUNCTION       r0002
                             00000031     01 - POP_TOP             
                             00000032     6E - JUMP_FORWARD        -> 00000036
                             00000035     01 - POP_TOP             
                             00000036     64 - LOAD_CONST          None
                             00000039     53 - RETURN_VALUE        
                         consts:
00001487                     TUPLE: (
0000148C                         None (4E)
                             )
                         names:
0000148D                     TUPLE: (
00001492                         STR: 'physics' (07 00 00 00 70 68 79 73 69 63 73),
0000149E                         STR: 'findNearestAI' (0D 00 00 00 66 69 6E 64 4E 65 61 72 65 73 74 41 49),
000014B0                         STR: 'consoletarget' (0D 00 00 00 63 6F 6E 73 6F 6C 65 74 61 72 67 65 74),
000014C2                         STR: 'Position' (08 00 00 00 50 6F 73 69 74 69 6F 6E),
000014CF                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
000014DB                         STR: 'nearest_ai' (0A 00 00 00 6E 65 61 72 65 73 74 5F 61 69),
000014EA                         STR: 'AI' (02 00 00 00 41 49),
000014F1                         STR: 'executeAbility' (0E 00 00 00 65 78 65 63 75 74 65 41 62 69 6C 69 74 79),
00001504                         STR: 'abilityid' (09 00 00 00 61 62 69 6C 69 74 79 69 64)
                             )
                         varnames:
00001512                     TUPLE: (
00001517                         STR: 'abilityid' (09 00 00 00 61 62 69 6C 69 74 79 69 64),
00001525                         STR: 'nearest_ai' (0A 00 00 00 6E 65 61 72 65 73 74 5F 61 69)
                             )
                         freevars:
00001534                     TUPLE: ()
                         cellvars:
00001539                     TUPLE: ()
                         filename:
0000153E                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
                         name:
00001586                     STR: 'ExecuteAbilityOnNearestAI' (19 00 00 00 45 78 65 63 75 74 65 41 62 69 6C 69 74 79 4F 6E 4E 65 61 72 65 73 74 41 49)
                         firslineno:
000015A4                     LONG: 75L (4B 00 00 00)
                         lnotab:
000015A8                     STR: '\x00\x01\x18\x01\x07\x01' (06 00 00 00 00 01 18 01 07 01),
000015B3             CODE:
                         argcount:
000015B4                     LONG: 1L (01 00 00 00)
                         nlocals:
000015B8                     LONG: 1L (01 00 00 00)
                         stacksize:
000015BC                     LONG: 3L (03 00 00 00)
                         flags:
000015C0                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000015C4                     STR: 't\x00\x00i\x01\x00i\x02\x00|\x00\x00t\x00\x00i\x04\x00\x83\x02\x00\x01d\x00\x00S' (1A 00 00 00 74 00 00 69 01 00 69 02 00 7C 00 00 74 00 00 69 04 00 83 02 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consoletarget'
                             00000003     69 - LOAD_ATTR           'AI'
                             00000006     69 - LOAD_ATTR           'executeAbility'
                             00000009     7C - LOAD_FAST           'abilityid'
                             0000000C     74 - LOAD_GLOBAL         'consoletarget'
                             0000000F     69 - LOAD_ATTR           'locator'
                             00000012     83 - CALL_FUNCTION       r0002
                             00000015     01 - POP_TOP             
                             00000016     64 - LOAD_CONST          None
                             00000019     53 - RETURN_VALUE        
                         consts:
000015E3                     TUPLE: (
000015E8                         None (4E)
                             )
                         names:
000015E9                     TUPLE: (
000015EE                         STR: 'consoletarget' (0D 00 00 00 63 6F 6E 73 6F 6C 65 74 61 72 67 65 74),
00001600                         STR: 'AI' (02 00 00 00 41 49),
00001607                         STR: 'executeAbility' (0E 00 00 00 65 78 65 63 75 74 65 41 62 69 6C 69 74 79),
0000161A                         STR: 'abilityid' (09 00 00 00 61 62 69 6C 69 74 79 69 64),
00001628                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72)
                             )
                         varnames:
00001634                     TUPLE: (
00001639                         STR: 'abilityid' (09 00 00 00 61 62 69 6C 69 74 79 69 64)
                             )
                         freevars:
00001647                     TUPLE: ()
                         cellvars:
0000164C                     TUPLE: ()
                         filename:
00001651                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
                         name:
00001699                     STR: 'ExecuteAbilityOnSelf' (14 00 00 00 45 78 65 63 75 74 65 41 62 69 6C 69 74 79 4F 6E 53 65 6C 66)
                         firslineno:
000016B2                     LONG: 80L (50 00 00 00)
                         lnotab:
000016B6                     STR: '\x00\x01' (02 00 00 00 00 01),
000016BD             CODE:
                         argcount:
000016BE                     LONG: 1L (01 00 00 00)
                         nlocals:
000016C2                     LONG: 1L (01 00 00 00)
                         stacksize:
000016C6                     LONG: 3L (03 00 00 00)
                         flags:
000016CA                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000016CE                     STR: 't\x00\x00i\x01\x00i\x02\x00|\x00\x00t\x04\x00i\x05\x00\x83\x02\x00\x01d\x00\x00S' (1A 00 00 00 74 00 00 69 01 00 69 02 00 7C 00 00 74 04 00 69 05 00 83 02 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consoletarget'
                             00000003     69 - LOAD_ATTR           'AI'
                             00000006     69 - LOAD_ATTR           'executeAbility'
                             00000009     7C - LOAD_FAST           'abilityid'
                             0000000C     74 - LOAD_GLOBAL         'consoleplayer'
                             0000000F     69 - LOAD_ATTR           'locator'
                             00000012     83 - CALL_FUNCTION       r0002
                             00000015     01 - POP_TOP             
                             00000016     64 - LOAD_CONST          None
                             00000019     53 - RETURN_VALUE        
                         consts:
000016ED                     TUPLE: (
000016F2                         None (4E)
                             )
                         names:
000016F3                     TUPLE: (
000016F8                         STR: 'consoletarget' (0D 00 00 00 63 6F 6E 73 6F 6C 65 74 61 72 67 65 74),
0000170A                         STR: 'AI' (02 00 00 00 41 49),
00001711                         STR: 'executeAbility' (0E 00 00 00 65 78 65 63 75 74 65 41 62 69 6C 69 74 79),
00001724                         STR: 'abilityid' (09 00 00 00 61 62 69 6C 69 74 79 69 64),
00001732                         STR: 'consoleplayer' (0D 00 00 00 63 6F 6E 73 6F 6C 65 70 6C 61 79 65 72),
00001744                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72)
                             )
                         varnames:
00001750                     TUPLE: (
00001755                         STR: 'abilityid' (09 00 00 00 61 62 69 6C 69 74 79 69 64)
                             )
                         freevars:
00001763                     TUPLE: ()
                         cellvars:
00001768                     TUPLE: ()
                         filename:
0000176D                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
                         name:
000017B5                     STR: 'ExecuteAbilityOnMe' (12 00 00 00 45 78 65 63 75 74 65 41 62 69 6C 69 74 79 4F 6E 4D 65)
                         firslineno:
000017CC                     LONG: 83L (53 00 00 00)
                         lnotab:
000017D0                     STR: '\x00\x01' (02 00 00 00 00 01)
                 )
             names:
000017D7         TUPLE: (
000017DC             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
000017EA             STR: 'movement' (08 00 00 00 6D 6F 76 65 6D 65 6E 74),
000017F7             STR: 'Movement' (08 00 00 00 4D 6F 76 65 6D 65 6E 74),
00001804             STR: 'AttackNearestPlayer' (13 00 00 00 41 74 74 61 63 6B 4E 65 61 72 65 73 74 50 6C 61 79 65 72),
0000181C             STR: 'AttackNearestAI' (0F 00 00 00 41 74 74 61 63 6B 4E 65 61 72 65 73 74 41 49),
00001830             STR: 'AttackMe' (08 00 00 00 41 74 74 61 63 6B 4D 65),
0000183D             STR: 'FollowMe' (08 00 00 00 46 6F 6C 6C 6F 77 4D 65),
0000184A             STR: 'SetMood' (07 00 00 00 53 65 74 4D 6F 6F 64),
00001856             STR: 'None' (04 00 00 00 4E 6F 6E 65),
0000185F             STR: 'NPCType' (07 00 00 00 4E 50 43 54 79 70 65),
0000186B             STR: 'Behaviour' (09 00 00 00 42 65 68 61 76 69 6F 75 72),
00001879             STR: 'AddUnkeyedItem' (0E 00 00 00 41 64 64 55 6E 6B 65 79 65 64 49 74 65 6D),
0000188C             STR: 'AddRewardItem' (0D 00 00 00 41 64 64 52 65 77 61 72 64 49 74 65 6D),
0000189E             STR: 'AddRewardGroup' (0E 00 00 00 41 64 64 52 65 77 61 72 64 47 72 6F 75 70),
000018B1             STR: 'SetName' (07 00 00 00 53 65 74 4E 61 6D 65),
000018BD             STR: 'NoLoot' (06 00 00 00 4E 6F 4C 6F 6F 74),
000018C8             STR: 'Immortal' (08 00 00 00 49 6D 6D 6F 72 74 61 6C),
000018D5             STR: 'Healthy' (07 00 00 00 48 65 61 6C 74 68 79),
000018E1             STR: 'Wounded' (07 00 00 00 57 6F 75 6E 64 65 64),
000018ED             STR: 'NearDead' (08 00 00 00 4E 65 61 72 44 65 61 64),
000018FA             STR: 'Dead' (04 00 00 00 44 65 61 64),
00001903             STR: 'SetPermanentExclusion' (15 00 00 00 53 65 74 50 65 72 6D 61 6E 65 6E 74 45 78 63 6C 75 73 69 6F 6E),
0000191D             STR: 'ExecuteAbilityOnNearestAI' (19 00 00 00 45 78 65 63 75 74 65 41 62 69 6C 69 74 79 4F 6E 4E 65 61 72 65 73 74 41 49),
0000193B             STR: 'ExecuteAbilityOnSelf' (14 00 00 00 45 78 65 63 75 74 65 41 62 69 6C 69 74 79 4F 6E 53 65 6C 66),
00001954             STR: 'ExecuteAbilityOnMe' (12 00 00 00 45 78 65 63 75 74 65 41 62 69 6C 69 74 79 4F 6E 4D 65)
                 )
             varnames:
0000196B         TUPLE: (
00001970             STR: 'ExecuteAbilityOnNearestAI' (19 00 00 00 45 78 65 63 75 74 65 41 62 69 6C 69 74 79 4F 6E 4E 65 61 72 65 73 74 41 49),
0000198E             STR: 'SetPermanentExclusion' (15 00 00 00 53 65 74 50 65 72 6D 61 6E 65 6E 74 45 78 63 6C 75 73 69 6F 6E),
000019A8             STR: 'ExecuteAbilityOnMe' (12 00 00 00 45 78 65 63 75 74 65 41 62 69 6C 69 74 79 4F 6E 4D 65),
000019BF             STR: 'Movement' (08 00 00 00 4D 6F 76 65 6D 65 6E 74),
000019CC             STR: 'SetMood' (07 00 00 00 53 65 74 4D 6F 6F 64),
000019D8             STR: 'ExecuteAbilityOnSelf' (14 00 00 00 45 78 65 63 75 74 65 41 62 69 6C 69 74 79 4F 6E 53 65 6C 66),
000019F1             STR: 'Behaviour' (09 00 00 00 42 65 68 61 76 69 6F 75 72),
000019FF             STR: 'AttackNearestAI' (0F 00 00 00 41 74 74 61 63 6B 4E 65 61 72 65 73 74 41 49),
00001A13             STR: 'FollowMe' (08 00 00 00 46 6F 6C 6C 6F 77 4D 65),
00001A20             STR: 'Healthy' (07 00 00 00 48 65 61 6C 74 68 79),
00001A2C             STR: 'Wounded' (07 00 00 00 57 6F 75 6E 64 65 64),
00001A38             STR: 'NearDead' (08 00 00 00 4E 65 61 72 44 65 61 64),
00001A45             STR: 'AttackNearestPlayer' (13 00 00 00 41 74 74 61 63 6B 4E 65 61 72 65 73 74 50 6C 61 79 65 72),
00001A5D             STR: 'NoLoot' (06 00 00 00 4E 6F 4C 6F 6F 74),
00001A68             STR: 'SetName' (07 00 00 00 53 65 74 4E 61 6D 65),
00001A74             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00001A82             STR: 'Dead' (04 00 00 00 44 65 61 64),
00001A8B             STR: 'Immortal' (08 00 00 00 49 6D 6D 6F 72 74 61 6C),
00001A98             STR: 'NPCType' (07 00 00 00 4E 50 43 54 79 70 65),
00001AA4             STR: 'AddRewardGroup' (0E 00 00 00 41 64 64 52 65 77 61 72 64 47 72 6F 75 70),
00001AB7             STR: 'AddRewardItem' (0D 00 00 00 41 64 64 52 65 77 61 72 64 49 74 65 6D),
00001AC9             STR: 'AddUnkeyedItem' (0E 00 00 00 41 64 64 55 6E 6B 65 79 65 64 49 74 65 6D),
00001ADC             STR: 'AttackMe' (08 00 00 00 41 74 74 61 63 6B 4D 65)
                 )
             freevars:
00001AE9         TUPLE: ()
             cellvars:
00001AEE         TUPLE: ()
             filename:
00001AF3         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\npccommands.py' (43 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 6E 70 63 63 6F 6D 6D 61 6E 64 73 2E 70 79)
             name:
00001B3B         STR: '?' (01 00 00 00 3F)
             firslineno:
00001B41         LONG: 1L (01 00 00 00)
             lnotab:
00001B45         STR: '\t\x01\t\x02\t\x05\t\x05\t\x03\t\x03\t\x03\x0c\x03\x0c\x03\t\x03\t\x07\x0c\n\t\x04\t\x04\t\x03\t\x03\t\x03\t\x03\t\x03\t\x03\t\x05\t\x03' (2C 00 00 00 09 01 09 02 09 05 09 05 09 03 09 03 09 03 0C 03 0C 03 09 03 09 07 0C 0A 09 04 09 04 09 03 09 03 09 03 09 03 09 03 09 03 09 05 09 03)

