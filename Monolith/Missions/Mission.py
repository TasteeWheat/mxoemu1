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
00000019         STR: 'd\x00\x00e\x00\x00f\x01\x00d\x01\x00\x84\x00\x00\x83\x00\x00YZ\x01\x00d\x02\x00S' (1A 00 00 00 64 00 00 65 00 00 66 01 00 64 01 00 84 00 00 83 00 00 59 5A 01 00 64 02 00 53)
                 00000000     64 - LOAD_CONST          'Mission'
                 00000003     65 - LOAD_NAME           'object'
                 00000006     66 - BUILD_TUPLE         r0001
                 00000009     64 - LOAD_CONST          CODE('Mission')
                 0000000C     84 - MAKE_FUNCTION       r0000
                 0000000F     83 - CALL_FUNCTION       r0000
                 00000012     59 - BUILD_CLASS         
                 00000013     5A - STORE_NAME          'Mission'
                 00000016     64 - LOAD_CONST          None
                 00000019     53 - RETURN_VALUE        
             consts:
00000038         TUPLE: (
0000003D             STR: 'Mission' (07 00 00 00 4D 69 73 73 69 6F 6E),
00000049             CODE:
                         argcount:
0000004A                     LONG: 0L (00 00 00 00)
                         nlocals:
0000004E                     LONG: 0L (00 00 00 00)
                         stacksize:
00000052                     LONG: 1L (01 00 00 00)
                         flags:
00000056                     LONG: 66L (42 00 00 00)
                             (NEWLOCALS, NOFREE)
                         code:
0000005A                     STR: 't\x00\x00Z\x01\x00d\x01\x00\x84\x00\x00Z\x02\x00d\x02\x00\x84\x00\x00Z\x03\x00d\x03\x00\x84\x00\x00Z\x04\x00d\x04\x00\x84\x00\x00Z\x05\x00d\x05\x00\x84\x00\x00Z\x06\x00d\x06\x00\x84\x00\x00Z\x07\x00d\x07\x00\x84\x00\x00Z\x08\x00d\x08\x00\x84\x00\x00Z\t\x00d\t\x00\x84\x00\x00Z\n\x00d\n\x00\x84\x00\x00Z\x0b\x00d\x0b\x00\x84\x00\x00Z\x0c\x00RS' (6B 00 00 00 74 00 00 5A 01 00 64 01 00 84 00 00 5A 02 00 64 02 00 84 00 00 5A 03 00 64 03 00 84 00 00 5A 04 00 64 04 00 84 00 00 5A 05 00 64 05 00 84 00 00 5A 06 00 64 06 00 84 00 00 5A 07 00 64 07 00 84 00 00 5A 08 00 64 08 00 84 00 00 5A 09 00 64 09 00 84 00 00 5A 0A 00 64 0A 00 84 00 00 5A 0B 00 64 0B 00 84 00 00 5A 0C 00 52 53)
                             00000000     74 - LOAD_GLOBAL         '__name__'
                             00000003     5A - STORE_NAME          '__module__'
                             00000006     64 - LOAD_CONST          CODE('OnModalDialogueAccepted')
                             00000009     84 - MAKE_FUNCTION       r0000
                             0000000C     5A - STORE_NAME          'OnModalDialogueAccepted'
                             0000000F     64 - LOAD_CONST          CODE('OnMissionEvent')
                             00000012     84 - MAKE_FUNCTION       r0000
                             00000015     5A - STORE_NAME          'OnMissionEvent'
                             00000018     64 - LOAD_CONST          CODE('OnObjectTargeted')
                             0000001B     84 - MAKE_FUNCTION       r0000
                             0000001E     5A - STORE_NAME          'OnObjectTargeted'
                             00000021     64 - LOAD_CONST          CODE('OnPlayerEnterZone')
                             00000024     84 - MAKE_FUNCTION       r0000
                             00000027     5A - STORE_NAME          'OnPlayerEnterZone'
                             0000002A     64 - LOAD_CONST          CODE('OnToggledViewActivated')
                             0000002D     84 - MAKE_FUNCTION       r0000
                             00000030     5A - STORE_NAME          'OnToggledViewActivated'
                             00000033     64 - LOAD_CONST          CODE('OnStartOfStage')
                             00000036     84 - MAKE_FUNCTION       r0000
                             00000039     5A - STORE_NAME          'OnStartOfStage'
                             0000003C     64 - LOAD_CONST          CODE('OnStartOfMission')
                             0000003F     84 - MAKE_FUNCTION       r0000
                             00000042     5A - STORE_NAME          'OnStartOfMission'
                             00000045     64 - LOAD_CONST          CODE('OnInventoryItemsSwapped')
                             00000048     84 - MAKE_FUNCTION       r0000
                             0000004B     5A - STORE_NAME          'OnInventoryItemsSwapped'
                             0000004E     64 - LOAD_CONST          CODE('OnShortcutAdded')
                             00000051     84 - MAKE_FUNCTION       r0000
                             00000054     5A - STORE_NAME          'OnShortcutAdded'
                             00000057     64 - LOAD_CONST          CODE('OnMovementUpdated')
                             0000005A     84 - MAKE_FUNCTION       r0000
                             0000005D     5A - STORE_NAME          'OnMovementUpdated'
                             00000060     64 - LOAD_CONST          CODE('OnGoalComplete')
                             00000063     84 - MAKE_FUNCTION       r0000
                             00000066     5A - STORE_NAME          'OnGoalComplete'
                             00000069     52 - LOAD_LOCALS         
                             0000006A     53 - RETURN_VALUE        
                         consts:
000000CA                     TUPLE: (
000000CF                         None (4E),
000000D0                         CODE:
                                     argcount:
000000D1                                 LONG: 3L (03 00 00 00)
                                     nlocals:
000000D5                                 LONG: 3L (03 00 00 00)
                                     stacksize:
000000D9                                 LONG: 1L (01 00 00 00)
                                     flags:
000000DD                                 LONG: 67L (43 00 00 00)
                                         (OPTIMIZED, NEWLOCALS, NOFREE)
                                     code:
000000E1                                 STR: 'd\x00\x00S' (04 00 00 00 64 00 00 53)
                                         00000000     64 - LOAD_CONST          None
                                         00000003     53 - RETURN_VALUE        
                                     consts:
000000EA                                 TUPLE: (
000000EF                                     None (4E)
                                         )
                                     names:
000000F0                                 TUPLE: ()
                                     varnames:
000000F5                                 TUPLE: (
000000FA                                     STR: 'phasenumber' (0B 00 00 00 70 68 61 73 65 6E 75 6D 62 65 72),
0000010A                                     STR: 'teamleader' (0A 00 00 00 74 65 61 6D 6C 65 61 64 65 72),
00000119                                     STR: 'messageid' (09 00 00 00 6D 65 73 73 61 67 65 69 64)
                                         )
                                     freevars:
00000127                                 TUPLE: ()
                                     cellvars:
0000012C                                 TUPLE: ()
                                     filename:
00000131                                 STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\Missions\\Mission.py' (48 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 4D 69 73 73 69 6F 6E 73 5C 4D 69 73 73 69 6F 6E 2E 70 79)
                                     name:
0000017E                                 STR: 'OnModalDialogueAccepted' (17 00 00 00 4F 6E 4D 6F 64 61 6C 44 69 61 6C 6F 67 75 65 41 63 63 65 70 74 65 64)
                                     firslineno:
0000019A                                 LONG: 4L (04 00 00 00)
                                     lnotab:
0000019E                                 STR: '\x00\x01' (02 00 00 00 00 01),
000001A5                         CODE:
                                     argcount:
000001A6                                 LONG: 3L (03 00 00 00)
                                     nlocals:
000001AA                                 LONG: 3L (03 00 00 00)
                                     stacksize:
000001AE                                 LONG: 1L (01 00 00 00)
                                     flags:
000001B2                                 LONG: 67L (43 00 00 00)
                                         (OPTIMIZED, NEWLOCALS, NOFREE)
                                     code:
000001B6                                 STR: 'd\x00\x00S' (04 00 00 00 64 00 00 53)
                                         00000000     64 - LOAD_CONST          None
                                         00000003     53 - RETURN_VALUE        
                                     consts:
000001BF                                 TUPLE: (
000001C4                                     None (4E)
                                         )
                                     names:
000001C5                                 TUPLE: ()
                                     varnames:
000001CA                                 TUPLE: (
000001CF                                     STR: 'phasenumber' (0B 00 00 00 70 68 61 73 65 6E 75 6D 62 65 72),
000001DF                                     STR: 'eventid' (07 00 00 00 65 76 65 6E 74 69 64),
000001EB                                     STR: 'teamids' (07 00 00 00 74 65 61 6D 69 64 73)
                                         )
                                     freevars:
000001F7                                 TUPLE: ()
                                     cellvars:
000001FC                                 TUPLE: ()
                                     filename:
00000201                                 STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\Missions\\Mission.py' (48 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 4D 69 73 73 69 6F 6E 73 5C 4D 69 73 73 69 6F 6E 2E 70 79)
                                     name:
0000024E                                 STR: 'OnMissionEvent' (0E 00 00 00 4F 6E 4D 69 73 73 69 6F 6E 45 76 65 6E 74)
                                     firslineno:
00000261                                 LONG: 8L (08 00 00 00)
                                     lnotab:
00000265                                 STR: '\x00\x01' (02 00 00 00 00 01),
0000026C                         CODE:
                                     argcount:
0000026D                                 LONG: 3L (03 00 00 00)
                                     nlocals:
00000271                                 LONG: 3L (03 00 00 00)
                                     stacksize:
00000275                                 LONG: 1L (01 00 00 00)
                                     flags:
00000279                                 LONG: 67L (43 00 00 00)
                                         (OPTIMIZED, NEWLOCALS, NOFREE)
                                     code:
0000027D                                 STR: 'd\x00\x00S' (04 00 00 00 64 00 00 53)
                                         00000000     64 - LOAD_CONST          None
                                         00000003     53 - RETURN_VALUE        
                                     consts:
00000286                                 TUPLE: (
0000028B                                     None (4E)
                                         )
                                     names:
0000028C                                 TUPLE: ()
                                     varnames:
00000291                                 TUPLE: (
00000296                                     STR: 'phasenumber' (0B 00 00 00 70 68 61 73 65 6E 75 6D 62 65 72),
000002A6                                     STR: 'teamleader' (0A 00 00 00 74 65 61 6D 6C 65 61 64 65 72),
000002B5                                     STR: 'itemname' (08 00 00 00 69 74 65 6D 6E 61 6D 65)
                                         )
                                     freevars:
000002C2                                 TUPLE: ()
                                     cellvars:
000002C7                                 TUPLE: ()
                                     filename:
000002CC                                 STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\Missions\\Mission.py' (48 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 4D 69 73 73 69 6F 6E 73 5C 4D 69 73 73 69 6F 6E 2E 70 79)
                                     name:
00000319                                 STR: 'OnObjectTargeted' (10 00 00 00 4F 6E 4F 62 6A 65 63 74 54 61 72 67 65 74 65 64)
                                     firslineno:
0000032E                                 LONG: 12L (0C 00 00 00)
                                     lnotab:
00000332                                 STR: '\x00\x01' (02 00 00 00 00 01),
00000339                         CODE:
                                     argcount:
0000033A                                 LONG: 3L (03 00 00 00)
                                     nlocals:
0000033E                                 LONG: 3L (03 00 00 00)
                                     stacksize:
00000342                                 LONG: 1L (01 00 00 00)
                                     flags:
00000346                                 LONG: 67L (43 00 00 00)
                                         (OPTIMIZED, NEWLOCALS, NOFREE)
                                     code:
0000034A                                 STR: 'd\x00\x00S' (04 00 00 00 64 00 00 53)
                                         00000000     64 - LOAD_CONST          None
                                         00000003     53 - RETURN_VALUE        
                                     consts:
00000353                                 TUPLE: (
00000358                                     None (4E)
                                         )
                                     names:
00000359                                 TUPLE: ()
                                     varnames:
0000035E                                 TUPLE: (
00000363                                     STR: 'phasenumber' (0B 00 00 00 70 68 61 73 65 6E 75 6D 62 65 72),
00000373                                     STR: 'teamleader' (0A 00 00 00 74 65 61 6D 6C 65 61 64 65 72),
00000382                                     STR: 'zoneid' (06 00 00 00 7A 6F 6E 65 69 64)
                                         )
                                     freevars:
0000038D                                 TUPLE: ()
                                     cellvars:
00000392                                 TUPLE: ()
                                     filename:
00000397                                 STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\Missions\\Mission.py' (48 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 4D 69 73 73 69 6F 6E 73 5C 4D 69 73 73 69 6F 6E 2E 70 79)
                                     name:
000003E4                                 STR: 'OnPlayerEnterZone' (11 00 00 00 4F 6E 50 6C 61 79 65 72 45 6E 74 65 72 5A 6F 6E 65)
                                     firslineno:
000003FA                                 LONG: 16L (10 00 00 00)
                                     lnotab:
000003FE                                 STR: '\x00\x01' (02 00 00 00 00 01),
00000405                         CODE:
                                     argcount:
00000406                                 LONG: 3L (03 00 00 00)
                                     nlocals:
0000040A                                 LONG: 3L (03 00 00 00)
                                     stacksize:
0000040E                                 LONG: 1L (01 00 00 00)
                                     flags:
00000412                                 LONG: 67L (43 00 00 00)
                                         (OPTIMIZED, NEWLOCALS, NOFREE)
                                     code:
00000416                                 STR: 'd\x00\x00S' (04 00 00 00 64 00 00 53)
                                         00000000     64 - LOAD_CONST          None
                                         00000003     53 - RETURN_VALUE        
                                     consts:
0000041F                                 TUPLE: (
00000424                                     None (4E)
                                         )
                                     names:
00000425                                 TUPLE: ()
                                     varnames:
0000042A                                 TUPLE: (
0000042F                                     STR: 'phasenumber' (0B 00 00 00 70 68 61 73 65 6E 75 6D 62 65 72),
0000043F                                     STR: 'teamleader' (0A 00 00 00 74 65 61 6D 6C 65 61 64 65 72),
0000044E                                     STR: 'viewid' (06 00 00 00 76 69 65 77 69 64)
                                         )
                                     freevars:
00000459                                 TUPLE: ()
                                     cellvars:
0000045E                                 TUPLE: ()
                                     filename:
00000463                                 STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\Missions\\Mission.py' (48 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 4D 69 73 73 69 6F 6E 73 5C 4D 69 73 73 69 6F 6E 2E 70 79)
                                     name:
000004B0                                 STR: 'OnToggledViewActivated' (16 00 00 00 4F 6E 54 6F 67 67 6C 65 64 56 69 65 77 41 63 74 69 76 61 74 65 64)
                                     firslineno:
000004CB                                 LONG: 20L (14 00 00 00)
                                     lnotab:
000004CF                                 STR: '\x00\x01' (02 00 00 00 00 01),
000004D6                         CODE:
                                     argcount:
000004D7                                 LONG: 3L (03 00 00 00)
                                     nlocals:
000004DB                                 LONG: 3L (03 00 00 00)
                                     stacksize:
000004DF                                 LONG: 1L (01 00 00 00)
                                     flags:
000004E3                                 LONG: 67L (43 00 00 00)
                                         (OPTIMIZED, NEWLOCALS, NOFREE)
                                     code:
000004E7                                 STR: 'd\x00\x00S' (04 00 00 00 64 00 00 53)
                                         00000000     64 - LOAD_CONST          None
                                         00000003     53 - RETURN_VALUE        
                                     consts:
000004F0                                 TUPLE: (
000004F5                                     None (4E)
                                         )
                                     names:
000004F6                                 TUPLE: ()
                                     varnames:
000004FB                                 TUPLE: (
00000500                                     STR: 'phasenumber' (0B 00 00 00 70 68 61 73 65 6E 75 6D 62 65 72),
00000510                                     STR: 'stagenumber' (0B 00 00 00 73 74 61 67 65 6E 75 6D 62 65 72),
00000520                                     STR: 'teamids' (07 00 00 00 74 65 61 6D 69 64 73)
                                         )
                                     freevars:
0000052C                                 TUPLE: ()
                                     cellvars:
00000531                                 TUPLE: ()
                                     filename:
00000536                                 STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\Missions\\Mission.py' (48 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 4D 69 73 73 69 6F 6E 73 5C 4D 69 73 73 69 6F 6E 2E 70 79)
                                     name:
00000583                                 STR: 'OnStartOfStage' (0E 00 00 00 4F 6E 53 74 61 72 74 4F 66 53 74 61 67 65)
                                     firslineno:
00000596                                 LONG: 24L (18 00 00 00)
                                     lnotab:
0000059A                                 STR: '\x00\x01' (02 00 00 00 00 01),
000005A1                         CODE:
                                     argcount:
000005A2                                 LONG: 1L (01 00 00 00)
                                     nlocals:
000005A6                                 LONG: 1L (01 00 00 00)
                                     stacksize:
000005AA                                 LONG: 1L (01 00 00 00)
                                     flags:
000005AE                                 LONG: 67L (43 00 00 00)
                                         (OPTIMIZED, NEWLOCALS, NOFREE)
                                     code:
000005B2                                 STR: 'd\x00\x00S' (04 00 00 00 64 00 00 53)
                                         00000000     64 - LOAD_CONST          None
                                         00000003     53 - RETURN_VALUE        
                                     consts:
000005BB                                 TUPLE: (
000005C0                                     None (4E)
                                         )
                                     names:
000005C1                                 TUPLE: ()
                                     varnames:
000005C6                                 TUPLE: (
000005CB                                     STR: 'teamids' (07 00 00 00 74 65 61 6D 69 64 73)
                                         )
                                     freevars:
000005D7                                 TUPLE: ()
                                     cellvars:
000005DC                                 TUPLE: ()
                                     filename:
000005E1                                 STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\Missions\\Mission.py' (48 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 4D 69 73 73 69 6F 6E 73 5C 4D 69 73 73 69 6F 6E 2E 70 79)
                                     name:
0000062E                                 STR: 'OnStartOfMission' (10 00 00 00 4F 6E 53 74 61 72 74 4F 66 4D 69 73 73 69 6F 6E)
                                     firslineno:
00000643                                 LONG: 28L (1C 00 00 00)
                                     lnotab:
00000647                                 STR: '\x00\x01' (02 00 00 00 00 01),
0000064E                         CODE:
                                     argcount:
0000064F                                 LONG: 8L (08 00 00 00)
                                     nlocals:
00000653                                 LONG: 8L (08 00 00 00)
                                     stacksize:
00000657                                 LONG: 1L (01 00 00 00)
                                     flags:
0000065B                                 LONG: 67L (43 00 00 00)
                                         (OPTIMIZED, NEWLOCALS, NOFREE)
                                     code:
0000065F                                 STR: 'd\x00\x00S' (04 00 00 00 64 00 00 53)
                                         00000000     64 - LOAD_CONST          None
                                         00000003     53 - RETURN_VALUE        
                                     consts:
00000668                                 TUPLE: (
0000066D                                     None (4E)
                                         )
                                     names:
0000066E                                 TUPLE: ()
                                     varnames:
00000673                                 TUPLE: (
00000678                                     STR: 'phasenumber' (0B 00 00 00 70 68 61 73 65 6E 75 6D 62 65 72),
00000688                                     STR: 'sender' (06 00 00 00 73 65 6E 64 65 72),
00000693                                     STR: 'destSlot' (08 00 00 00 64 65 73 74 53 6C 6F 74),
000006A0                                     STR: 'destID' (06 00 00 00 64 65 73 74 49 44),
000006AB                                     STR: 'destData' (08 00 00 00 64 65 73 74 44 61 74 61),
000006B8                                     STR: 'srcSlot' (07 00 00 00 73 72 63 53 6C 6F 74),
000006C4                                     STR: 'srcID' (05 00 00 00 73 72 63 49 44),
000006CE                                     STR: 'srcData' (07 00 00 00 73 72 63 44 61 74 61)
                                         )
                                     freevars:
000006DA                                 TUPLE: ()
                                     cellvars:
000006DF                                 TUPLE: ()
                                     filename:
000006E4                                 STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\Missions\\Mission.py' (48 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 4D 69 73 73 69 6F 6E 73 5C 4D 69 73 73 69 6F 6E 2E 70 79)
                                     name:
00000731                                 STR: 'OnInventoryItemsSwapped' (17 00 00 00 4F 6E 49 6E 76 65 6E 74 6F 72 79 49 74 65 6D 73 53 77 61 70 70 65 64)
                                     firslineno:
0000074D                                 LONG: 32L (20 00 00 00)
                                     lnotab:
00000751                                 STR: '\x00\x01' (02 00 00 00 00 01),
00000758                         CODE:
                                     argcount:
00000759                                 LONG: 6L (06 00 00 00)
                                     nlocals:
0000075D                                 LONG: 6L (06 00 00 00)
                                     stacksize:
00000761                                 LONG: 1L (01 00 00 00)
                                     flags:
00000765                                 LONG: 67L (43 00 00 00)
                                         (OPTIMIZED, NEWLOCALS, NOFREE)
                                     code:
00000769                                 STR: 'd\x00\x00S' (04 00 00 00 64 00 00 53)
                                         00000000     64 - LOAD_CONST          None
                                         00000003     53 - RETURN_VALUE        
                                     consts:
00000772                                 TUPLE: (
00000777                                     None (4E)
                                         )
                                     names:
00000778                                 TUPLE: ()
                                     varnames:
0000077D                                 TUPLE: (
00000782                                     STR: 'phasenumber' (0B 00 00 00 70 68 61 73 65 6E 75 6D 62 65 72),
00000792                                     STR: 'sender' (06 00 00 00 73 65 6E 64 65 72),
0000079D                                     STR: 'shortcutType' (0C 00 00 00 73 68 6F 72 74 63 75 74 54 79 70 65),
000007AE                                     STR: 'classData' (09 00 00 00 63 6C 61 73 73 44 61 74 61),
000007BC                                     STR: 'instanceData' (0C 00 00 00 69 6E 73 74 61 6E 63 65 44 61 74 61),
000007CD                                     STR: 'invSlot' (07 00 00 00 69 6E 76 53 6C 6F 74)
                                         )
                                     freevars:
000007D9                                 TUPLE: ()
                                     cellvars:
000007DE                                 TUPLE: ()
                                     filename:
000007E3                                 STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\Missions\\Mission.py' (48 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 4D 69 73 73 69 6F 6E 73 5C 4D 69 73 73 69 6F 6E 2E 70 79)
                                     name:
00000830                                 STR: 'OnShortcutAdded' (0F 00 00 00 4F 6E 53 68 6F 72 74 63 75 74 41 64 64 65 64)
                                     firslineno:
00000844                                 LONG: 36L (24 00 00 00)
                                     lnotab:
00000848                                 STR: '\x00\x01' (02 00 00 00 00 01),
0000084F                         CODE:
                                     argcount:
00000850                                 LONG: 6L (06 00 00 00)
                                     nlocals:
00000854                                 LONG: 6L (06 00 00 00)
                                     stacksize:
00000858                                 LONG: 1L (01 00 00 00)
                                     flags:
0000085C                                 LONG: 67L (43 00 00 00)
                                         (OPTIMIZED, NEWLOCALS, NOFREE)
                                     code:
00000860                                 STR: 'd\x00\x00S' (04 00 00 00 64 00 00 53)
                                         00000000     64 - LOAD_CONST          None
                                         00000003     53 - RETURN_VALUE        
                                     consts:
00000869                                 TUPLE: (
0000086E                                     None (4E)
                                         )
                                     names:
0000086F                                 TUPLE: ()
                                     varnames:
00000874                                 TUPLE: (
00000879                                     STR: 'phasenumber' (0B 00 00 00 70 68 61 73 65 6E 75 6D 62 65 72),
00000889                                     STR: 'sender' (06 00 00 00 73 65 6E 64 65 72),
00000894                                     STR: 'posX' (04 00 00 00 70 6F 73 58),
0000089D                                     STR: 'posY' (04 00 00 00 70 6F 73 59),
000008A6                                     STR: 'posZ' (04 00 00 00 70 6F 73 5A),
000008AF                                     STR: 'angleFacing' (0B 00 00 00 61 6E 67 6C 65 46 61 63 69 6E 67)
                                         )
                                     freevars:
000008BF                                 TUPLE: ()
                                     cellvars:
000008C4                                 TUPLE: ()
                                     filename:
000008C9                                 STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\Missions\\Mission.py' (48 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 4D 69 73 73 69 6F 6E 73 5C 4D 69 73 73 69 6F 6E 2E 70 79)
                                     name:
00000916                                 STR: 'OnMovementUpdated' (11 00 00 00 4F 6E 4D 6F 76 65 6D 65 6E 74 55 70 64 61 74 65 64)
                                     firslineno:
0000092C                                 LONG: 40L (28 00 00 00)
                                     lnotab:
00000930                                 STR: '\x00\x01' (02 00 00 00 00 01),
00000937                         CODE:
                                     argcount:
00000938                                 LONG: 4L (04 00 00 00)
                                     nlocals:
0000093C                                 LONG: 4L (04 00 00 00)
                                     stacksize:
00000940                                 LONG: 1L (01 00 00 00)
                                     flags:
00000944                                 LONG: 67L (43 00 00 00)
                                         (OPTIMIZED, NEWLOCALS, NOFREE)
                                     code:
00000948                                 STR: 'd\x00\x00S' (04 00 00 00 64 00 00 53)
                                         00000000     64 - LOAD_CONST          None
                                         00000003     53 - RETURN_VALUE        
                                     consts:
00000951                                 TUPLE: (
00000956                                     None (4E)
                                         )
                                     names:
00000957                                 TUPLE: ()
                                     varnames:
0000095C                                 TUPLE: (
00000961                                     STR: 'self' (04 00 00 00 73 65 6C 66),
0000096A                                     STR: 'phasenumber' (0B 00 00 00 70 68 61 73 65 6E 75 6D 62 65 72),
0000097A                                     STR: 'goalnumber' (0A 00 00 00 67 6F 61 6C 6E 75 6D 62 65 72),
00000989                                     STR: 'teamids' (07 00 00 00 74 65 61 6D 69 64 73)
                                         )
                                     freevars:
00000995                                 TUPLE: ()
                                     cellvars:
0000099A                                 TUPLE: ()
                                     filename:
0000099F                                 STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\Missions\\Mission.py' (48 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 4D 69 73 73 69 6F 6E 73 5C 4D 69 73 73 69 6F 6E 2E 70 79)
                                     name:
000009EC                                 STR: 'OnGoalComplete' (0E 00 00 00 4F 6E 47 6F 61 6C 43 6F 6D 70 6C 65 74 65)
                                     firslineno:
000009FF                                 LONG: 45L (2D 00 00 00)
                                     lnotab:
00000A03                                 STR: '\x00\x01' (02 00 00 00 00 01)
                             )
                         names:
00000A0A                     TUPLE: (
00000A0F                         STR: '__name__' (08 00 00 00 5F 5F 6E 61 6D 65 5F 5F),
00000A1C                         STR: '__module__' (0A 00 00 00 5F 5F 6D 6F 64 75 6C 65 5F 5F),
00000A2B                         STR: 'OnModalDialogueAccepted' (17 00 00 00 4F 6E 4D 6F 64 61 6C 44 69 61 6C 6F 67 75 65 41 63 63 65 70 74 65 64),
00000A47                         STR: 'OnMissionEvent' (0E 00 00 00 4F 6E 4D 69 73 73 69 6F 6E 45 76 65 6E 74),
00000A5A                         STR: 'OnObjectTargeted' (10 00 00 00 4F 6E 4F 62 6A 65 63 74 54 61 72 67 65 74 65 64),
00000A6F                         STR: 'OnPlayerEnterZone' (11 00 00 00 4F 6E 50 6C 61 79 65 72 45 6E 74 65 72 5A 6F 6E 65),
00000A85                         STR: 'OnToggledViewActivated' (16 00 00 00 4F 6E 54 6F 67 67 6C 65 64 56 69 65 77 41 63 74 69 76 61 74 65 64),
00000AA0                         STR: 'OnStartOfStage' (0E 00 00 00 4F 6E 53 74 61 72 74 4F 66 53 74 61 67 65),
00000AB3                         STR: 'OnStartOfMission' (10 00 00 00 4F 6E 53 74 61 72 74 4F 66 4D 69 73 73 69 6F 6E),
00000AC8                         STR: 'OnInventoryItemsSwapped' (17 00 00 00 4F 6E 49 6E 76 65 6E 74 6F 72 79 49 74 65 6D 73 53 77 61 70 70 65 64),
00000AE4                         STR: 'OnShortcutAdded' (0F 00 00 00 4F 6E 53 68 6F 72 74 63 75 74 41 64 64 65 64),
00000AF8                         STR: 'OnMovementUpdated' (11 00 00 00 4F 6E 4D 6F 76 65 6D 65 6E 74 55 70 64 61 74 65 64),
00000B0E                         STR: 'OnGoalComplete' (0E 00 00 00 4F 6E 47 6F 61 6C 43 6F 6D 70 6C 65 74 65)
                             )
                         varnames:
00000B21                     TUPLE: ()
                         freevars:
00000B26                     TUPLE: ()
                         cellvars:
00000B2B                     TUPLE: ()
                         filename:
00000B30                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\Missions\\Mission.py' (48 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 4D 69 73 73 69 6F 6E 73 5C 4D 69 73 73 69 6F 6E 2E 70 79)
                         name:
00000B7D                     STR: 'Mission' (07 00 00 00 4D 69 73 73 69 6F 6E)
                         firslineno:
00000B89                     LONG: 1L (01 00 00 00)
                         lnotab:
00000B8D                     STR: '\x06\x03\t\x04\t\x04\t\x04\t\x04\t\x04\t\x04\t\x04\t\x04\t\x04\t\x05' (16 00 00 00 06 03 09 04 09 04 09 04 09 04 09 04 09 04 09 04 09 04 09 04 09 05),
00000BA8             None (4E)
                 )
             names:
00000BA9         TUPLE: (
00000BAE             STR: 'object' (06 00 00 00 6F 62 6A 65 63 74),
00000BB9             STR: 'Mission' (07 00 00 00 4D 69 73 73 69 6F 6E)
                 )
             varnames:
00000BC5         TUPLE: (
00000BCA             STR: 'Mission' (07 00 00 00 4D 69 73 73 69 6F 6E)
                 )
             freevars:
00000BD6         TUPLE: ()
             cellvars:
00000BDB         TUPLE: ()
             filename:
00000BE0         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\Missions\\Mission.py' (48 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 4D 69 73 73 69 6F 6E 73 5C 4D 69 73 73 69 6F 6E 2E 70 79)
             name:
00000C2D         STR: '?' (01 00 00 00 3F)
             firslineno:
00000C33         LONG: 1L (01 00 00 00)
             lnotab:
00000C37         STR: '' (00 00 00 00)

