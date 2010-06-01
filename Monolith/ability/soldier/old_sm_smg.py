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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00i\x03\x00Z\x04\x00d\x01\x00Z\x05\x00d\x02\x00Z\x06\x00d\x03\x00Z\x07\x00d\x04\x00Z\x08\x00d\x05\x00Z\t\x00d\x06\x00Z\n\x00d\x07\x00Z\x0b\x00d\x08\x00\x84\x00\x00Z\x0c\x00d\t\x00\x84\x00\x00Z\r\x00d\n\x00\x84\x00\x00Z\x0e\x00d\x0b\x00\x84\x00\x00Z\x0f\x00d\x0c\x00\x84\x00\x00Z\x10\x00d\r\x00\x84\x00\x00Z\x11\x00d\x0e\x00\x84\x00\x00Z\x12\x00d\x0f\x00\x84\x00\x00Z\x13\x00d\x00\x00S' (94 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 69 03 00 5A 04 00 64 01 00 5A 05 00 64 02 00 5A 06 00 64 03 00 5A 07 00 64 04 00 5A 08 00 64 05 00 5A 09 00 64 06 00 5A 0A 00 64 07 00 5A 0B 00 64 08 00 84 00 00 5A 0C 00 64 09 00 84 00 00 5A 0D 00 64 0A 00 84 00 00 5A 0E 00 64 0B 00 84 00 00 5A 0F 00 64 0C 00 84 00 00 5A 10 00 64 0D 00 84 00 00 5A 11 00 64 0E 00 84 00 00 5A 12 00 64 0F 00 84 00 00 5A 13 00 64 00 00 53)
                 00000000     64 - LOAD_CONST          None
                 00000003     6B - IMPORT_NAME         'traceback'
                 00000006     5A - STORE_NAME          'traceback'
                 00000009     64 - LOAD_CONST          None
                 0000000C     6B - IMPORT_NAME         'obj'
                 0000000F     5A - STORE_NAME          'obj'
                 00000012     64 - LOAD_CONST          None
                 00000015     6B - IMPORT_NAME         'ability.utility'
                 00000018     69 - LOAD_ATTR           'utility'
                 0000001B     5A - STORE_NAME          'Utility'
                 0000001E     64 - LOAD_CONST          75
                 00000021     5A - STORE_NAME          'SMG_SUPPRESSION_FIRE_DAMAGE'
                 00000024     64 - LOAD_CONST          250
                 00000027     5A - STORE_NAME          'SMG_FULL_AUTO_DAMAGE'
                 0000002A     64 - LOAD_CONST          300
                 0000002D     5A - STORE_NAME          'SMG_FULL_AUTO_REDUX_DAMAGE'
                 00000030     64 - LOAD_CONST          215
                 00000033     5A - STORE_NAME          'SMG_HEAVING_VOLLEY_DAMAGE'
                 00000036     64 - LOAD_CONST          100
                 00000039     5A - STORE_NAME          'SMG_SLIDING_VOLLEY_DAMAGE'
                 0000003C     64 - LOAD_CONST          90
                 0000003F     5A - STORE_NAME          'SMG_CONTROLLED_BURST_DAMAGE'
                 00000042     64 - LOAD_CONST          15
                 00000045     5A - STORE_NAME          'SMG_SUPPRESSION_FIRE_POWERLESS_EFFECT_DURATION'
                 00000048     64 - LOAD_CONST          CODE('SubmachineGunSuppressionFire_DirectObject')
                 0000004B     84 - MAKE_FUNCTION       r0000
                 0000004E     5A - STORE_NAME          'SubmachineGunSuppressionFire_DirectObject'
                 00000051     64 - LOAD_CONST          CODE('SubmachineGunSuppressionFire_Subject')
                 00000054     84 - MAKE_FUNCTION       r0000
                 00000057     5A - STORE_NAME          'SubmachineGunSuppressionFire_Subject'
                 0000005A     64 - LOAD_CONST          CODE('SubmachineGunCoveringFire_DirectObject')
                 0000005D     84 - MAKE_FUNCTION       r0000
                 00000060     5A - STORE_NAME          'SubmachineGunCoveringFire_DirectObject'
                 00000063     64 - LOAD_CONST          CODE('SubmachineGunFullAuto_DirectObject')
                 00000066     84 - MAKE_FUNCTION       r0000
                 00000069     5A - STORE_NAME          'SubmachineGunFullAuto_DirectObject'
                 0000006C     64 - LOAD_CONST          CODE('SubmachineGunFullAutoRedux_DirectObject')
                 0000006F     84 - MAKE_FUNCTION       r0000
                 00000072     5A - STORE_NAME          'SubmachineGunFullAutoRedux_DirectObject'
                 00000075     64 - LOAD_CONST          CODE('SubmachineGunHeavingVolley_DirectObject')
                 00000078     84 - MAKE_FUNCTION       r0000
                 0000007B     5A - STORE_NAME          'SubmachineGunHeavingVolley_DirectObject'
                 0000007E     64 - LOAD_CONST          CODE('SubmachineGunSlidingVolley_DirectObject')
                 00000081     84 - MAKE_FUNCTION       r0000
                 00000084     5A - STORE_NAME          'SubmachineGunSlidingVolley_DirectObject'
                 00000087     64 - LOAD_CONST          CODE('SubmachineGunControlledBurst_DirectObject')
                 0000008A     84 - MAKE_FUNCTION       r0000
                 0000008D     5A - STORE_NAME          'SubmachineGunControlledBurst_DirectObject'
                 00000090     64 - LOAD_CONST          None
                 00000093     53 - RETURN_VALUE        
             consts:
000000B2         TUPLE: (
000000B7             None (4E),
000000B8             INT: 75 (4B 00 00 00),
000000BD             INT: 250 (FA 00 00 00),
000000C2             INT: 300 (2C 01 00 00),
000000C7             INT: 215 (D7 00 00 00),
000000CC             INT: 100 (64 00 00 00),
000000D1             INT: 90 (5A 00 00 00),
000000D6             INT: 15 (0F 00 00 00),
000000DB             CODE:
                         argcount:
000000DC                     LONG: 2L (02 00 00 00)
                         nlocals:
000000E0                     LONG: 3L (03 00 00 00)
                         stacksize:
000000E4                     LONG: 6L (06 00 00 00)
                         flags:
000000E8                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000000EC                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'SubmachineGunSuppressionFire: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'SMG_SUPPRESSION_FIRE_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'SMG_SUPPRESSION_FIRE_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'SubmachineGunSuppressionFireAbility'
                             00000035     7C - LOAD_FAST           'msg'
                             00000038     69 - LOAD_ATTR           'subjectLocator'
                             0000003B     7C - LOAD_FAST           'msg'
                             0000003E     69 - LOAD_ATTR           'directObjectLocator'
                             00000041     7C - LOAD_FAST           'damage'
                             00000044     83 - CALL_FUNCTION       r0005
                             00000047     01 - POP_TOP             
                             00000048     64 - LOAD_CONST          None
                             0000004B     53 - RETURN_VALUE        
                         consts:
0000013D                     TUPLE: (
00000142                         None (4E),
00000143                         STR: 'SubmachineGunSuppressionFire: %d damage dealt' (2D 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 53 75 70 70 72 65 73 73 69 6F 6E 46 69 72 65 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
00000175                     TUPLE: (
0000017A                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000186                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
0000019D                         STR: 'SMG_SUPPRESSION_FIRE_DAMAGE' (1B 00 00 00 53 4D 47 5F 53 55 50 50 52 45 53 53 49 4F 4E 5F 46 49 52 45 5F 44 41 4D 41 47 45),
000001BD                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000001C9                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
000001D7                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
000001F5                         STR: 'msg' (03 00 00 00 6D 73 67),
000001FD                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00000210                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
0000021B                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00000239                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00000245                         STR: 'SubmachineGunSuppressionFireAbility' (23 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 53 75 70 70 72 65 73 73 69 6F 6E 46 69 72 65 41 62 69 6C 69 74 79),
0000026D                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00000285                     TUPLE: (
0000028A                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000296                         STR: 'msg' (03 00 00 00 6D 73 67),
0000029E                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
000002A9                     TUPLE: ()
                         cellvars:
000002AE                     TUPLE: ()
                         filename:
000002B3                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_smg.py' (52 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 73 6D 67 2E 70 79)
                         name:
0000030A                     STR: 'SubmachineGunSuppressionFire_DirectObject' (29 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 53 75 70 70 72 65 73 73 69 6F 6E 46 69 72 65 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000338                     LONG: 32L (20 00 00 00)
                         lnotab:
0000033C                     STR: '\x00\x01\x11\x04\x18\x01' (06 00 00 00 00 01 11 04 18 01),
00000347             CODE:
                         argcount:
00000348                     LONG: 2L (02 00 00 00)
                         nlocals:
0000034C                     LONG: 2L (02 00 00 00)
                         stacksize:
00000350                     LONG: 2L (02 00 00 00)
                         flags:
00000354                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000358                     STR: 't\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01d\x00\x00S' (11 00 00 00 74 00 00 69 01 00 64 01 00 83 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'SubmachineGunSuppressionFire: Subject'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     01 - POP_TOP             
                             0000000D     64 - LOAD_CONST          None
                             00000010     53 - RETURN_VALUE        
                         consts:
0000036E                     TUPLE: (
00000373                         None (4E),
00000374                         STR: 'SubmachineGunSuppressionFire: Subject' (25 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 53 75 70 70 72 65 73 73 69 6F 6E 46 69 72 65 3A 20 53 75 62 6A 65 63 74)
                             )
                         names:
0000039E                     TUPLE: (
000003A3                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000003AF                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67)
                             )
                         varnames:
000003C6                     TUPLE: (
000003CB                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000003D7                         STR: 'msg' (03 00 00 00 6D 73 67)
                             )
                         freevars:
000003DF                     TUPLE: ()
                         cellvars:
000003E4                     TUPLE: ()
                         filename:
000003E9                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_smg.py' (52 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 73 6D 67 2E 70 79)
                         name:
00000440                     STR: 'SubmachineGunSuppressionFire_Subject' (24 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 53 75 70 70 72 65 73 73 69 6F 6E 46 69 72 65 5F 53 75 62 6A 65 63 74)
                         firslineno:
00000469                     LONG: 40L (28 00 00 00)
                         lnotab:
0000046D                     STR: '\x00\x01' (02 00 00 00 00 01),
00000474             CODE:
                         argcount:
00000475                     LONG: 2L (02 00 00 00)
                         nlocals:
00000479                     LONG: 2L (02 00 00 00)
                         stacksize:
0000047D                     LONG: 2L (02 00 00 00)
                         flags:
00000481                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000485                     STR: 't\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01d\x00\x00S' (11 00 00 00 74 00 00 69 01 00 64 01 00 83 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'SubmachineGunCoveringFire: opponent forced to ground for 2 exchanges'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     01 - POP_TOP             
                             0000000D     64 - LOAD_CONST          None
                             00000010     53 - RETURN_VALUE        
                         consts:
0000049B                     TUPLE: (
000004A0                         None (4E),
000004A1                         STR: 'SubmachineGunCoveringFire: opponent forced to ground for 2 exchanges' (44 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 43 6F 76 65 72 69 6E 67 46 69 72 65 3A 20 6F 70 70 6F 6E 65 6E 74 20 66 6F 72 63 65 64 20 74 6F 20 67 72 6F 75 6E 64 20 66 6F 72 20 32 20 65 78 63 68 61 6E 67 65 73)
                             )
                         names:
000004EA                     TUPLE: (
000004EF                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000004FB                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67)
                             )
                         varnames:
00000512                     TUPLE: (
00000517                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000523                         STR: 'msg' (03 00 00 00 6D 73 67)
                             )
                         freevars:
0000052B                     TUPLE: ()
                         cellvars:
00000530                     TUPLE: ()
                         filename:
00000535                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_smg.py' (52 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 73 6D 67 2E 70 79)
                         name:
0000058C                     STR: 'SubmachineGunCoveringFire_DirectObject' (26 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 43 6F 76 65 72 69 6E 67 46 69 72 65 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
000005B7                     LONG: 46L (2E 00 00 00)
                         lnotab:
000005BB                     STR: '\x00\x01' (02 00 00 00 00 01),
000005C2             CODE:
                         argcount:
000005C3                     LONG: 2L (02 00 00 00)
                         nlocals:
000005C7                     LONG: 3L (03 00 00 00)
                         stacksize:
000005CB                     LONG: 6L (06 00 00 00)
                         flags:
000005CF                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000005D3                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'SubmachineGunFullAuto: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'SMG_FULL_AUTO_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'SMG_FULL_AUTO_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'SubmachineGunFullAutoAbility'
                             00000035     7C - LOAD_FAST           'msg'
                             00000038     69 - LOAD_ATTR           'subjectLocator'
                             0000003B     7C - LOAD_FAST           'msg'
                             0000003E     69 - LOAD_ATTR           'directObjectLocator'
                             00000041     7C - LOAD_FAST           'damage'
                             00000044     83 - CALL_FUNCTION       r0005
                             00000047     01 - POP_TOP             
                             00000048     64 - LOAD_CONST          None
                             0000004B     53 - RETURN_VALUE        
                         consts:
00000624                     TUPLE: (
00000629                         None (4E),
0000062A                         STR: 'SubmachineGunFullAuto: %d damage dealt' (26 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 46 75 6C 6C 41 75 74 6F 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
00000655                     TUPLE: (
0000065A                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000666                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
0000067D                         STR: 'SMG_FULL_AUTO_DAMAGE' (14 00 00 00 53 4D 47 5F 46 55 4C 4C 5F 41 55 54 4F 5F 44 41 4D 41 47 45),
00000696                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000006A2                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
000006B0                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
000006CE                         STR: 'msg' (03 00 00 00 6D 73 67),
000006D6                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
000006E9                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
000006F4                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00000712                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
0000071E                         STR: 'SubmachineGunFullAutoAbility' (1C 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 46 75 6C 6C 41 75 74 6F 41 62 69 6C 69 74 79),
0000073F                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00000757                     TUPLE: (
0000075C                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000768                         STR: 'msg' (03 00 00 00 6D 73 67),
00000770                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
0000077B                     TUPLE: ()
                         cellvars:
00000780                     TUPLE: ()
                         filename:
00000785                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_smg.py' (52 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 73 6D 67 2E 70 79)
                         name:
000007DC                     STR: 'SubmachineGunFullAuto_DirectObject' (22 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 46 75 6C 6C 41 75 74 6F 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000803                     LONG: 53L (35 00 00 00)
                         lnotab:
00000807                     STR: '\x00\x01\x11\x02\x18\x01' (06 00 00 00 00 01 11 02 18 01),
00000812             CODE:
                         argcount:
00000813                     LONG: 2L (02 00 00 00)
                         nlocals:
00000817                     LONG: 3L (03 00 00 00)
                         stacksize:
0000081B                     LONG: 6L (06 00 00 00)
                         flags:
0000081F                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000823                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'SubmachineGunFullAutoRedux: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'SMG_FULL_AUTO_REDUX_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'SMG_FULL_AUTO_REDUX_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'SubmachineGunFullAutoReduxAbility'
                             00000035     7C - LOAD_FAST           'msg'
                             00000038     69 - LOAD_ATTR           'subjectLocator'
                             0000003B     7C - LOAD_FAST           'msg'
                             0000003E     69 - LOAD_ATTR           'directObjectLocator'
                             00000041     7C - LOAD_FAST           'damage'
                             00000044     83 - CALL_FUNCTION       r0005
                             00000047     01 - POP_TOP             
                             00000048     64 - LOAD_CONST          None
                             0000004B     53 - RETURN_VALUE        
                         consts:
00000874                     TUPLE: (
00000879                         None (4E),
0000087A                         STR: 'SubmachineGunFullAutoRedux: %d damage dealt' (2B 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 46 75 6C 6C 41 75 74 6F 52 65 64 75 78 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
000008AA                     TUPLE: (
000008AF                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000008BB                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
000008D2                         STR: 'SMG_FULL_AUTO_REDUX_DAMAGE' (1A 00 00 00 53 4D 47 5F 46 55 4C 4C 5F 41 55 54 4F 5F 52 45 44 55 58 5F 44 41 4D 41 47 45),
000008F1                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000008FD                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
0000090B                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00000929                         STR: 'msg' (03 00 00 00 6D 73 67),
00000931                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00000944                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
0000094F                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
0000096D                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00000979                         STR: 'SubmachineGunFullAutoReduxAbility' (21 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 46 75 6C 6C 41 75 74 6F 52 65 64 75 78 41 62 69 6C 69 74 79),
0000099F                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
000009B7                     TUPLE: (
000009BC                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000009C8                         STR: 'msg' (03 00 00 00 6D 73 67),
000009D0                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
000009DB                     TUPLE: ()
                         cellvars:
000009E0                     TUPLE: ()
                         filename:
000009E5                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_smg.py' (52 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 73 6D 67 2E 70 79)
                         name:
00000A3C                     STR: 'SubmachineGunFullAutoRedux_DirectObject' (27 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 46 75 6C 6C 41 75 74 6F 52 65 64 75 78 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000A68                     LONG: 63L (3F 00 00 00)
                         lnotab:
00000A6C                     STR: '\x00\x01\x11\x02\x18\x01' (06 00 00 00 00 01 11 02 18 01),
00000A77             CODE:
                         argcount:
00000A78                     LONG: 2L (02 00 00 00)
                         nlocals:
00000A7C                     LONG: 3L (03 00 00 00)
                         stacksize:
00000A80                     LONG: 6L (06 00 00 00)
                         flags:
00000A84                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000A88                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'SubmachineGunHeavingVolley: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'SMG_HEAVING_VOLLEY_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'SMG_HEAVING_VOLLEY_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'SubmachineGunHeavingVolleyAbility'
                             00000035     7C - LOAD_FAST           'msg'
                             00000038     69 - LOAD_ATTR           'subjectLocator'
                             0000003B     7C - LOAD_FAST           'msg'
                             0000003E     69 - LOAD_ATTR           'directObjectLocator'
                             00000041     7C - LOAD_FAST           'damage'
                             00000044     83 - CALL_FUNCTION       r0005
                             00000047     01 - POP_TOP             
                             00000048     64 - LOAD_CONST          None
                             0000004B     53 - RETURN_VALUE        
                         consts:
00000AD9                     TUPLE: (
00000ADE                         None (4E),
00000ADF                         STR: 'SubmachineGunHeavingVolley: %d damage dealt' (2B 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 48 65 61 76 69 6E 67 56 6F 6C 6C 65 79 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
00000B0F                     TUPLE: (
00000B14                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000B20                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000B37                         STR: 'SMG_HEAVING_VOLLEY_DAMAGE' (19 00 00 00 53 4D 47 5F 48 45 41 56 49 4E 47 5F 56 4F 4C 4C 45 59 5F 44 41 4D 41 47 45),
00000B55                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000B61                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00000B6F                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00000B8D                         STR: 'msg' (03 00 00 00 6D 73 67),
00000B95                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00000BA8                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
00000BB3                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00000BD1                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00000BDD                         STR: 'SubmachineGunHeavingVolleyAbility' (21 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 48 65 61 76 69 6E 67 56 6F 6C 6C 65 79 41 62 69 6C 69 74 79),
00000C03                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00000C1B                     TUPLE: (
00000C20                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000C2C                         STR: 'msg' (03 00 00 00 6D 73 67),
00000C34                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00000C3F                     TUPLE: ()
                         cellvars:
00000C44                     TUPLE: ()
                         filename:
00000C49                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_smg.py' (52 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 73 6D 67 2E 70 79)
                         name:
00000CA0                     STR: 'SubmachineGunHeavingVolley_DirectObject' (27 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 48 65 61 76 69 6E 67 56 6F 6C 6C 65 79 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000CCC                     LONG: 72L (48 00 00 00)
                         lnotab:
00000CD0                     STR: '\x00\x01\x11\x02\x18\x01' (06 00 00 00 00 01 11 02 18 01),
00000CDB             CODE:
                         argcount:
00000CDC                     LONG: 2L (02 00 00 00)
                         nlocals:
00000CE0                     LONG: 3L (03 00 00 00)
                         stacksize:
00000CE4                     LONG: 6L (06 00 00 00)
                         flags:
00000CE8                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000CEC                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'SubmachineGunSlidingVolley: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'SMG_SLIDING_VOLLEY_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'SMG_SLIDING_VOLLEY_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'SubmachineGunSlidingVolleyAbility'
                             00000035     7C - LOAD_FAST           'msg'
                             00000038     69 - LOAD_ATTR           'subjectLocator'
                             0000003B     7C - LOAD_FAST           'msg'
                             0000003E     69 - LOAD_ATTR           'directObjectLocator'
                             00000041     7C - LOAD_FAST           'damage'
                             00000044     83 - CALL_FUNCTION       r0005
                             00000047     01 - POP_TOP             
                             00000048     64 - LOAD_CONST          None
                             0000004B     53 - RETURN_VALUE        
                         consts:
00000D3D                     TUPLE: (
00000D42                         None (4E),
00000D43                         STR: 'SubmachineGunSlidingVolley: %d damage dealt' (2B 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 53 6C 69 64 69 6E 67 56 6F 6C 6C 65 79 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
00000D73                     TUPLE: (
00000D78                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000D84                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000D9B                         STR: 'SMG_SLIDING_VOLLEY_DAMAGE' (19 00 00 00 53 4D 47 5F 53 4C 49 44 49 4E 47 5F 56 4F 4C 4C 45 59 5F 44 41 4D 41 47 45),
00000DB9                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000DC5                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00000DD3                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00000DF1                         STR: 'msg' (03 00 00 00 6D 73 67),
00000DF9                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00000E0C                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
00000E17                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00000E35                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00000E41                         STR: 'SubmachineGunSlidingVolleyAbility' (21 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 53 6C 69 64 69 6E 67 56 6F 6C 6C 65 79 41 62 69 6C 69 74 79),
00000E67                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00000E7F                     TUPLE: (
00000E84                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000E90                         STR: 'msg' (03 00 00 00 6D 73 67),
00000E98                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00000EA3                     TUPLE: ()
                         cellvars:
00000EA8                     TUPLE: ()
                         filename:
00000EAD                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_smg.py' (52 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 73 6D 67 2E 70 79)
                         name:
00000F04                     STR: 'SubmachineGunSlidingVolley_DirectObject' (27 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 53 6C 69 64 69 6E 67 56 6F 6C 6C 65 79 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000F30                     LONG: 81L (51 00 00 00)
                         lnotab:
00000F34                     STR: '\x00\x01\x11\x02\x18\x01' (06 00 00 00 00 01 11 02 18 01),
00000F3F             CODE:
                         argcount:
00000F40                     LONG: 2L (02 00 00 00)
                         nlocals:
00000F44                     LONG: 3L (03 00 00 00)
                         stacksize:
00000F48                     LONG: 6L (06 00 00 00)
                         flags:
00000F4C                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000F50                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'SubmachineGunControlledBurst: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'SMG_CONTROLLED_BURST_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'SMG_CONTROLLED_BURST_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'SubmachineGunControlledBurstAbility'
                             00000035     7C - LOAD_FAST           'msg'
                             00000038     69 - LOAD_ATTR           'subjectLocator'
                             0000003B     7C - LOAD_FAST           'msg'
                             0000003E     69 - LOAD_ATTR           'directObjectLocator'
                             00000041     7C - LOAD_FAST           'damage'
                             00000044     83 - CALL_FUNCTION       r0005
                             00000047     01 - POP_TOP             
                             00000048     64 - LOAD_CONST          None
                             0000004B     53 - RETURN_VALUE        
                         consts:
00000FA1                     TUPLE: (
00000FA6                         None (4E),
00000FA7                         STR: 'SubmachineGunControlledBurst: %d damage dealt' (2D 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 43 6F 6E 74 72 6F 6C 6C 65 64 42 75 72 73 74 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
00000FD9                     TUPLE: (
00000FDE                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000FEA                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00001001                         STR: 'SMG_CONTROLLED_BURST_DAMAGE' (1B 00 00 00 53 4D 47 5F 43 4F 4E 54 52 4F 4C 4C 45 44 5F 42 55 52 53 54 5F 44 41 4D 41 47 45),
00001021                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000102D                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
0000103B                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00001059                         STR: 'msg' (03 00 00 00 6D 73 67),
00001061                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00001074                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
0000107F                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
0000109D                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
000010A9                         STR: 'SubmachineGunControlledBurstAbility' (23 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 43 6F 6E 74 72 6F 6C 6C 65 64 42 75 72 73 74 41 62 69 6C 69 74 79),
000010D1                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
000010E9                     TUPLE: (
000010EE                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000010FA                         STR: 'msg' (03 00 00 00 6D 73 67),
00001102                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
0000110D                     TUPLE: ()
                         cellvars:
00001112                     TUPLE: ()
                         filename:
00001117                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_smg.py' (52 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 73 6D 67 2E 70 79)
                         name:
0000116E                     STR: 'SubmachineGunControlledBurst_DirectObject' (29 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 43 6F 6E 74 72 6F 6C 6C 65 64 42 75 72 73 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
0000119C                     LONG: 90L (5A 00 00 00)
                         lnotab:
000011A0                     STR: '\x00\x01\x11\x02\x18\x01' (06 00 00 00 00 01 11 02 18 01)
                 )
             names:
000011AB         TUPLE: (
000011B0             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
000011BE             STR: 'obj' (03 00 00 00 6F 62 6A),
000011C6             STR: 'ability.utility' (0F 00 00 00 61 62 69 6C 69 74 79 2E 75 74 69 6C 69 74 79),
000011DA             STR: 'utility' (07 00 00 00 75 74 69 6C 69 74 79),
000011E6             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000011F2             STR: 'SMG_SUPPRESSION_FIRE_DAMAGE' (1B 00 00 00 53 4D 47 5F 53 55 50 50 52 45 53 53 49 4F 4E 5F 46 49 52 45 5F 44 41 4D 41 47 45),
00001212             STR: 'SMG_FULL_AUTO_DAMAGE' (14 00 00 00 53 4D 47 5F 46 55 4C 4C 5F 41 55 54 4F 5F 44 41 4D 41 47 45),
0000122B             STR: 'SMG_FULL_AUTO_REDUX_DAMAGE' (1A 00 00 00 53 4D 47 5F 46 55 4C 4C 5F 41 55 54 4F 5F 52 45 44 55 58 5F 44 41 4D 41 47 45),
0000124A             STR: 'SMG_HEAVING_VOLLEY_DAMAGE' (19 00 00 00 53 4D 47 5F 48 45 41 56 49 4E 47 5F 56 4F 4C 4C 45 59 5F 44 41 4D 41 47 45),
00001268             STR: 'SMG_SLIDING_VOLLEY_DAMAGE' (19 00 00 00 53 4D 47 5F 53 4C 49 44 49 4E 47 5F 56 4F 4C 4C 45 59 5F 44 41 4D 41 47 45),
00001286             STR: 'SMG_CONTROLLED_BURST_DAMAGE' (1B 00 00 00 53 4D 47 5F 43 4F 4E 54 52 4F 4C 4C 45 44 5F 42 55 52 53 54 5F 44 41 4D 41 47 45),
000012A6             STR: 'SMG_SUPPRESSION_FIRE_POWERLESS_EFFECT_DURATION' (2E 00 00 00 53 4D 47 5F 53 55 50 50 52 45 53 53 49 4F 4E 5F 46 49 52 45 5F 50 4F 57 45 52 4C 45 53 53 5F 45 46 46 45 43 54 5F 44 55 52 41 54 49 4F 4E),
000012D9             STR: 'SubmachineGunSuppressionFire_DirectObject' (29 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 53 75 70 70 72 65 73 73 69 6F 6E 46 69 72 65 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001307             STR: 'SubmachineGunSuppressionFire_Subject' (24 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 53 75 70 70 72 65 73 73 69 6F 6E 46 69 72 65 5F 53 75 62 6A 65 63 74),
00001330             STR: 'SubmachineGunCoveringFire_DirectObject' (26 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 43 6F 76 65 72 69 6E 67 46 69 72 65 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
0000135B             STR: 'SubmachineGunFullAuto_DirectObject' (22 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 46 75 6C 6C 41 75 74 6F 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001382             STR: 'SubmachineGunFullAutoRedux_DirectObject' (27 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 46 75 6C 6C 41 75 74 6F 52 65 64 75 78 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
000013AE             STR: 'SubmachineGunHeavingVolley_DirectObject' (27 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 48 65 61 76 69 6E 67 56 6F 6C 6C 65 79 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
000013DA             STR: 'SubmachineGunSlidingVolley_DirectObject' (27 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 53 6C 69 64 69 6E 67 56 6F 6C 6C 65 79 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001406             STR: 'SubmachineGunControlledBurst_DirectObject' (29 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 43 6F 6E 74 72 6F 6C 6C 65 64 42 75 72 73 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                 )
             varnames:
00001434         TUPLE: (
00001439             STR: 'SubmachineGunSlidingVolley_DirectObject' (27 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 53 6C 69 64 69 6E 67 56 6F 6C 6C 65 79 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001465             STR: 'SubmachineGunControlledBurst_DirectObject' (29 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 43 6F 6E 74 72 6F 6C 6C 65 64 42 75 72 73 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001493             STR: 'SMG_HEAVING_VOLLEY_DAMAGE' (19 00 00 00 53 4D 47 5F 48 45 41 56 49 4E 47 5F 56 4F 4C 4C 45 59 5F 44 41 4D 41 47 45),
000014B1             STR: 'obj' (03 00 00 00 6F 62 6A),
000014B9             STR: 'SubmachineGunFullAuto_DirectObject' (22 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 46 75 6C 6C 41 75 74 6F 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
000014E0             STR: 'SMG_SUPPRESSION_FIRE_POWERLESS_EFFECT_DURATION' (2E 00 00 00 53 4D 47 5F 53 55 50 50 52 45 53 53 49 4F 4E 5F 46 49 52 45 5F 50 4F 57 45 52 4C 45 53 53 5F 45 46 46 45 43 54 5F 44 55 52 41 54 49 4F 4E),
00001513             STR: 'SubmachineGunFullAutoRedux_DirectObject' (27 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 46 75 6C 6C 41 75 74 6F 52 65 64 75 78 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
0000153F             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
0000154D             STR: 'SubmachineGunCoveringFire_DirectObject' (26 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 43 6F 76 65 72 69 6E 67 46 69 72 65 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001578             STR: 'SMG_CONTROLLED_BURST_DAMAGE' (1B 00 00 00 53 4D 47 5F 43 4F 4E 54 52 4F 4C 4C 45 44 5F 42 55 52 53 54 5F 44 41 4D 41 47 45),
00001598             STR: 'SMG_FULL_AUTO_DAMAGE' (14 00 00 00 53 4D 47 5F 46 55 4C 4C 5F 41 55 54 4F 5F 44 41 4D 41 47 45),
000015B1             STR: 'SubmachineGunSuppressionFire_DirectObject' (29 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 53 75 70 70 72 65 73 73 69 6F 6E 46 69 72 65 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
000015DF             STR: 'SMG_SUPPRESSION_FIRE_DAMAGE' (1B 00 00 00 53 4D 47 5F 53 55 50 50 52 45 53 53 49 4F 4E 5F 46 49 52 45 5F 44 41 4D 41 47 45),
000015FF             STR: 'SubmachineGunSuppressionFire_Subject' (24 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 53 75 70 70 72 65 73 73 69 6F 6E 46 69 72 65 5F 53 75 62 6A 65 63 74),
00001628             STR: 'SMG_FULL_AUTO_REDUX_DAMAGE' (1A 00 00 00 53 4D 47 5F 46 55 4C 4C 5F 41 55 54 4F 5F 52 45 44 55 58 5F 44 41 4D 41 47 45),
00001647             STR: 'SMG_SLIDING_VOLLEY_DAMAGE' (19 00 00 00 53 4D 47 5F 53 4C 49 44 49 4E 47 5F 56 4F 4C 4C 45 59 5F 44 41 4D 41 47 45),
00001665             STR: 'SubmachineGunHeavingVolley_DirectObject' (27 00 00 00 53 75 62 6D 61 63 68 69 6E 65 47 75 6E 48 65 61 76 69 6E 67 56 6F 6C 6C 65 79 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001691             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79)
                 )
             freevars:
0000169D         TUPLE: ()
             cellvars:
000016A2         TUPLE: ()
             filename:
000016A7         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_smg.py' (52 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 73 6D 67 2E 70 79)
             name:
000016FE         STR: '?' (01 00 00 00 3F)
             firslineno:
00001704         LONG: 1L (01 00 00 00)
             lnotab:
00001708         STR: '\t\x01\t\x01\x0c\x08\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x06\x06\n\t\x08\t\x06\t\x07\t\n\t\t\t\t\t\t' (22 00 00 00 09 01 09 01 0C 08 06 01 06 01 06 01 06 01 06 01 06 06 06 0A 09 08 09 06 09 07 09 0A 09 09 09 09 09 09)

