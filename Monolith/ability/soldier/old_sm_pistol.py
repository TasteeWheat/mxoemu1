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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00i\x03\x00Z\x04\x00d\x01\x00k\x05\x00Td\x02\x00Z\x06\x00d\x03\x00Z\x07\x00d\x04\x00Z\x08\x00d\x05\x00Z\t\x00d\x06\x00Z\n\x00d\x07\x00Z\x0b\x00d\x08\x00Z\x0c\x00d\t\x00Z\r\x00d\n\x00Z\x0e\x00d\x0b\x00Z\x0f\x00d\x0b\x00Z\x10\x00d\x0c\x00Z\x11\x00d\x06\x00Z\x12\x00d\r\x00\x84\x00\x00Z\x13\x00d\x0e\x00\x84\x00\x00Z\x14\x00d\x0f\x00\x84\x00\x00Z\x15\x00d\x10\x00\x84\x00\x00Z\x16\x00d\x11\x00\x84\x00\x00Z\x17\x00d\x12\x00\x84\x00\x00Z\x18\x00d\x13\x00\x84\x00\x00Z\x19\x00d\x14\x00\x84\x00\x00Z\x1a\x00d\x15\x00\x84\x00\x00Z\x1b\x00d\x16\x00\x84\x00\x00Z\x1c\x00d\x00\x00S' (D1 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 69 03 00 5A 04 00 64 01 00 6B 05 00 54 64 02 00 5A 06 00 64 03 00 5A 07 00 64 04 00 5A 08 00 64 05 00 5A 09 00 64 06 00 5A 0A 00 64 07 00 5A 0B 00 64 08 00 5A 0C 00 64 09 00 5A 0D 00 64 0A 00 5A 0E 00 64 0B 00 5A 0F 00 64 0B 00 5A 10 00 64 0C 00 5A 11 00 64 06 00 5A 12 00 64 0D 00 84 00 00 5A 13 00 64 0E 00 84 00 00 5A 14 00 64 0F 00 84 00 00 5A 15 00 64 10 00 84 00 00 5A 16 00 64 11 00 84 00 00 5A 17 00 64 12 00 84 00 00 5A 18 00 64 13 00 84 00 00 5A 19 00 64 14 00 84 00 00 5A 1A 00 64 15 00 84 00 00 5A 1B 00 64 16 00 84 00 00 5A 1C 00 64 00 00 53)
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
                 0000001E     64 - LOAD_CONST          ('*')
                 00000021     6B - IMPORT_NAME         'ability.defines'
                 00000024     54 - IMPORT_STAR         
                 00000025     64 - LOAD_CONST          250
                 00000028     5A - STORE_NAME          'PISTOL_AERIAL_DAMAGE'
                 0000002B     64 - LOAD_CONST          215
                 0000002E     5A - STORE_NAME          'PISTOL_BARRAGE_DAMAGE'
                 00000031     64 - LOAD_CONST          75
                 00000034     5A - STORE_NAME          'PISTOL_BLINDING_SHOT_DAMAGE'
                 00000037     64 - LOAD_CONST          325
                 0000003A     5A - STORE_NAME          'PISTOL_DASH_DAMAGE'
                 0000003D     64 - LOAD_CONST          50
                 00000040     5A - STORE_NAME          'PISTOL_DISARMING_SHOT_DAMAGE'
                 00000043     64 - LOAD_CONST          90
                 00000046     5A - STORE_NAME          'PISTOL_EVASIVE_DAMAGE'
                 00000049     64 - LOAD_CONST          300
                 0000004C     5A - STORE_NAME          'PISTOL_POINT_BLANK_DAMAGE'
                 0000004F     64 - LOAD_CONST          100
                 00000052     5A - STORE_NAME          'PISTOL_SLIDE_DAMAGE'
                 00000055     64 - LOAD_CONST          350
                 00000058     5A - STORE_NAME          'PISTOL_EXECUTION_DAMAGE'
                 0000005B     64 - LOAD_CONST          12
                 0000005E     5A - STORE_NAME          'PISTOL_EVASIVE_BLOCK_BOOST_DURATION'
                 00000061     64 - LOAD_CONST          12
                 00000064     5A - STORE_NAME          'PISTOL_BLINDING_SHOT_BLINDNESS_EFFECT_DURATION'
                 00000067     64 - LOAD_CONST          10
                 0000006A     5A - STORE_NAME          'PISTOL_AERIAL_EFFECT_DURATION'
                 0000006D     64 - LOAD_CONST          50
                 00000070     5A - STORE_NAME          'PISTOL_EVASIVE_BLOCK_BOOST'
                 00000073     64 - LOAD_CONST          CODE('PistolAerial_DirectObject')
                 00000076     84 - MAKE_FUNCTION       r0000
                 00000079     5A - STORE_NAME          'PistolAerial_DirectObject'
                 0000007C     64 - LOAD_CONST          CODE('PistolBarrage_DirectObject')
                 0000007F     84 - MAKE_FUNCTION       r0000
                 00000082     5A - STORE_NAME          'PistolBarrage_DirectObject'
                 00000085     64 - LOAD_CONST          CODE('PistolBlindingShot_DirectObject')
                 00000088     84 - MAKE_FUNCTION       r0000
                 0000008B     5A - STORE_NAME          'PistolBlindingShot_DirectObject'
                 0000008E     64 - LOAD_CONST          CODE('PistolDash_DirectObject')
                 00000091     84 - MAKE_FUNCTION       r0000
                 00000094     5A - STORE_NAME          'PistolDash_DirectObject'
                 00000097     64 - LOAD_CONST          CODE('PistolDisarmingShot_DirectObject')
                 0000009A     84 - MAKE_FUNCTION       r0000
                 0000009D     5A - STORE_NAME          'PistolDisarmingShot_DirectObject'
                 000000A0     64 - LOAD_CONST          CODE('PistolEvasive_DirectObject')
                 000000A3     84 - MAKE_FUNCTION       r0000
                 000000A6     5A - STORE_NAME          'PistolEvasive_DirectObject'
                 000000A9     64 - LOAD_CONST          CODE('PistolEvasive_Subject')
                 000000AC     84 - MAKE_FUNCTION       r0000
                 000000AF     5A - STORE_NAME          'PistolEvasive_Subject'
                 000000B2     64 - LOAD_CONST          CODE('PistolPointBlank_DirectObject')
                 000000B5     84 - MAKE_FUNCTION       r0000
                 000000B8     5A - STORE_NAME          'PistolPointBlank_DirectObject'
                 000000BB     64 - LOAD_CONST          CODE('PistolSlide_DirectObject')
                 000000BE     84 - MAKE_FUNCTION       r0000
                 000000C1     5A - STORE_NAME          'PistolSlide_DirectObject'
                 000000C4     64 - LOAD_CONST          CODE('PistolExecution_DirectObject')
                 000000C7     84 - MAKE_FUNCTION       r0000
                 000000CA     5A - STORE_NAME          'PistolExecution_DirectObject'
                 000000CD     64 - LOAD_CONST          None
                 000000D0     53 - RETURN_VALUE        
             consts:
000000EF         TUPLE: (
000000F4             None (4E),
000000F5             TUPLE: (
000000FA                 STR: '*' (01 00 00 00 2A)
                     ),
00000100             INT: 250 (FA 00 00 00),
00000105             INT: 215 (D7 00 00 00),
0000010A             INT: 75 (4B 00 00 00),
0000010F             INT: 325 (45 01 00 00),
00000114             INT: 50 (32 00 00 00),
00000119             INT: 90 (5A 00 00 00),
0000011E             INT: 300 (2C 01 00 00),
00000123             INT: 100 (64 00 00 00),
00000128             INT: 350 (5E 01 00 00),
0000012D             INT: 12 (0C 00 00 00),
00000132             INT: 10 (0A 00 00 00),
00000137             CODE:
                         argcount:
00000138                     LONG: 2L (02 00 00 00)
                         nlocals:
0000013C                     LONG: 3L (03 00 00 00)
                         stacksize:
00000140                     LONG: 6L (06 00 00 00)
                         flags:
00000144                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000148                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00t\x03\x00f\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x05\x00i\x06\x00|\x01\x00i\x08\x00t\x03\x00\x83\x02\x00}\x02\x00t\x00\x00i\n\x00t\x0b\x00t\x0c\x00|\x01\x00i\x08\x00|\x01\x00i\r\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (52 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 74 03 00 66 02 00 16 83 01 00 01 7C 00 00 69 05 00 69 06 00 7C 01 00 69 08 00 74 03 00 83 02 00 7D 02 00 74 00 00 69 0A 00 74 0B 00 74 0C 00 7C 01 00 69 08 00 7C 01 00 69 0D 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'PistolAerial: confused for %d seconds and %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'PISTOL_AERIAL_EFFECT_DURATION'
                             0000000C     74 - LOAD_GLOBAL         'PISTOL_AERIAL_DAMAGE'
                             0000000F     66 - BUILD_TUPLE         r0002
                             00000012     16 - BINARY_MODULO       
                             00000013     83 - CALL_FUNCTION       r0001
                             00000016     01 - POP_TOP             
                             00000017     7C - LOAD_FAST           'subject'
                             0000001A     69 - LOAD_ATTR           'Interlock'
                             0000001D     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             00000020     7C - LOAD_FAST           'msg'
                             00000023     69 - LOAD_ATTR           'subjectLocator'
                             00000026     74 - LOAD_GLOBAL         'PISTOL_AERIAL_DAMAGE'
                             00000029     83 - CALL_FUNCTION       r0002
                             0000002C     7D - STORE_FAST          'damage'
                             0000002F     74 - LOAD_GLOBAL         'Utility'
                             00000032     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             00000035     74 - LOAD_GLOBAL         'SUCCESS'
                             00000038     74 - LOAD_GLOBAL         'PistolAerialAbility'
                             0000003B     7C - LOAD_FAST           'msg'
                             0000003E     69 - LOAD_ATTR           'subjectLocator'
                             00000041     7C - LOAD_FAST           'msg'
                             00000044     69 - LOAD_ATTR           'directObjectLocator'
                             00000047     7C - LOAD_FAST           'damage'
                             0000004A     83 - CALL_FUNCTION       r0005
                             0000004D     01 - POP_TOP             
                             0000004E     64 - LOAD_CONST          None
                             00000051     53 - RETURN_VALUE        
                         consts:
0000019F                     TUPLE: (
000001A4                         None (4E),
000001A5                         STR: 'PistolAerial: confused for %d seconds and %d damage dealt' (39 00 00 00 50 69 73 74 6F 6C 41 65 72 69 61 6C 3A 20 63 6F 6E 66 75 73 65 64 20 66 6F 72 20 25 64 20 73 65 63 6F 6E 64 73 20 61 6E 64 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
000001E3                     TUPLE: (
000001E8                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000001F4                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
0000020B                         STR: 'PISTOL_AERIAL_EFFECT_DURATION' (1D 00 00 00 50 49 53 54 4F 4C 5F 41 45 52 49 41 4C 5F 45 46 46 45 43 54 5F 44 55 52 41 54 49 4F 4E),
0000022D                         STR: 'PISTOL_AERIAL_DAMAGE' (14 00 00 00 50 49 53 54 4F 4C 5F 41 45 52 49 41 4C 5F 44 41 4D 41 47 45),
00000246                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000252                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00000260                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
0000027E                         STR: 'msg' (03 00 00 00 6D 73 67),
00000286                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00000299                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
000002A4                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
000002C2                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
000002CE                         STR: 'PistolAerialAbility' (13 00 00 00 50 69 73 74 6F 6C 41 65 72 69 61 6C 41 62 69 6C 69 74 79),
000002E6                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
000002FE                     TUPLE: (
00000303                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000030F                         STR: 'msg' (03 00 00 00 6D 73 67),
00000317                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00000322                     TUPLE: ()
                         cellvars:
00000327                     TUPLE: ()
                         filename:
0000032C                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_pistol.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 70 69 73 74 6F 6C 2E 70 79)
                         name:
00000386                     STR: 'PistolAerial_DirectObject' (19 00 00 00 50 69 73 74 6F 6C 41 65 72 69 61 6C 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
000003A4                     LONG: 37L (25 00 00 00)
                         lnotab:
000003A8                     STR: '\x00\x01\x17\x01\x18\x02' (06 00 00 00 00 01 17 01 18 02),
000003B3             CODE:
                         argcount:
000003B4                     LONG: 2L (02 00 00 00)
                         nlocals:
000003B8                     LONG: 3L (03 00 00 00)
                         stacksize:
000003BC                     LONG: 6L (06 00 00 00)
                         flags:
000003C0                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000003C4                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'PistolBarrage: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'PISTOL_BARRAGE_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'PISTOL_BARRAGE_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'PistolBarrageAbility'
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
00000415                     TUPLE: (
0000041A                         None (4E),
0000041B                         STR: 'PistolBarrage: %d damage dealt' (1E 00 00 00 50 69 73 74 6F 6C 42 61 72 72 61 67 65 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
0000043E                     TUPLE: (
00000443                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
0000044F                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000466                         STR: 'PISTOL_BARRAGE_DAMAGE' (15 00 00 00 50 49 53 54 4F 4C 5F 42 41 52 52 41 47 45 5F 44 41 4D 41 47 45),
00000480                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000048C                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
0000049A                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
000004B8                         STR: 'msg' (03 00 00 00 6D 73 67),
000004C0                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
000004D3                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
000004DE                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
000004FC                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00000508                         STR: 'PistolBarrageAbility' (14 00 00 00 50 69 73 74 6F 6C 42 61 72 72 61 67 65 41 62 69 6C 69 74 79),
00000521                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00000539                     TUPLE: (
0000053E                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000054A                         STR: 'msg' (03 00 00 00 6D 73 67),
00000552                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
0000055D                     TUPLE: ()
                         cellvars:
00000562                     TUPLE: ()
                         filename:
00000567                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_pistol.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 70 69 73 74 6F 6C 2E 70 79)
                         name:
000005C1                     STR: 'PistolBarrage_DirectObject' (1A 00 00 00 50 69 73 74 6F 6C 42 61 72 72 61 67 65 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
000005E0                     LONG: 47L (2F 00 00 00)
                         lnotab:
000005E4                     STR: '\x00\x01\x11\x01\x18\x01' (06 00 00 00 00 01 11 01 18 01),
000005EF             CODE:
                         argcount:
000005F0                     LONG: 2L (02 00 00 00)
                         nlocals:
000005F4                     LONG: 3L (03 00 00 00)
                         stacksize:
000005F8                     LONG: 6L (06 00 00 00)
                         flags:
000005FC                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000600                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00t\x03\x00f\x02\x00\x16\x83\x01\x00\x01t\x04\x00i\x05\x00|\x00\x00|\x01\x00i\x08\x00t\t\x00t\x02\x00d\x02\x00\x83\x05\x00\x01|\x00\x00i\n\x00i\x0b\x00|\x01\x00i\x08\x00t\x03\x00\x83\x02\x00}\x02\x00t\x00\x00i\r\x00t\x0e\x00t\t\x00|\x01\x00i\x08\x00|\x01\x00i\x0f\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (6E 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 74 03 00 66 02 00 16 83 01 00 01 74 04 00 69 05 00 7C 00 00 7C 01 00 69 08 00 74 09 00 74 02 00 64 02 00 83 05 00 01 7C 00 00 69 0A 00 69 0B 00 7C 01 00 69 08 00 74 03 00 83 02 00 7D 02 00 74 00 00 69 0D 00 74 0E 00 74 09 00 7C 01 00 69 08 00 7C 01 00 69 0F 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'PistolBlindingShot: blinded for %d seconds and %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'PISTOL_BLINDING_SHOT_BLINDNESS_EFFECT_DURATION'
                             0000000C     74 - LOAD_GLOBAL         'PISTOL_BLINDING_SHOT_DAMAGE'
                             0000000F     66 - BUILD_TUPLE         r0002
                             00000012     16 - BINARY_MODULO       
                             00000013     83 - CALL_FUNCTION       r0001
                             00000016     01 - POP_TOP             
                             00000017     74 - LOAD_GLOBAL         'SE'
                             0000001A     69 - LOAD_ATTR           'EnableBlindness'
                             0000001D     7C - LOAD_FAST           'subject'
                             00000020     7C - LOAD_FAST           'msg'
                             00000023     69 - LOAD_ATTR           'subjectLocator'
                             00000026     74 - LOAD_GLOBAL         'PistolBlindingShotAbility'
                             00000029     74 - LOAD_GLOBAL         'PISTOL_BLINDING_SHOT_BLINDNESS_EFFECT_DURATION'
                             0000002C     64 - LOAD_CONST          0
                             0000002F     83 - CALL_FUNCTION       r0005
                             00000032     01 - POP_TOP             
                             00000033     7C - LOAD_FAST           'subject'
                             00000036     69 - LOAD_ATTR           'Interlock'
                             00000039     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000003C     7C - LOAD_FAST           'msg'
                             0000003F     69 - LOAD_ATTR           'subjectLocator'
                             00000042     74 - LOAD_GLOBAL         'PISTOL_BLINDING_SHOT_DAMAGE'
                             00000045     83 - CALL_FUNCTION       r0002
                             00000048     7D - STORE_FAST          'damage'
                             0000004B     74 - LOAD_GLOBAL         'Utility'
                             0000004E     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             00000051     74 - LOAD_GLOBAL         'SUCCESS'
                             00000054     74 - LOAD_GLOBAL         'PistolBlindingShotAbility'
                             00000057     7C - LOAD_FAST           'msg'
                             0000005A     69 - LOAD_ATTR           'subjectLocator'
                             0000005D     7C - LOAD_FAST           'msg'
                             00000060     69 - LOAD_ATTR           'directObjectLocator'
                             00000063     7C - LOAD_FAST           'damage'
                             00000066     83 - CALL_FUNCTION       r0005
                             00000069     01 - POP_TOP             
                             0000006A     64 - LOAD_CONST          None
                             0000006D     53 - RETURN_VALUE        
                         consts:
00000673                     TUPLE: (
00000678                         None (4E),
00000679                         STR: 'PistolBlindingShot: blinded for %d seconds and %d damage dealt' (3E 00 00 00 50 69 73 74 6F 6C 42 6C 69 6E 64 69 6E 67 53 68 6F 74 3A 20 62 6C 69 6E 64 65 64 20 66 6F 72 20 25 64 20 73 65 63 6F 6E 64 73 20 61 6E 64 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74),
000006BC                         INT: 0 (00 00 00 00)
                             )
                         names:
000006C1                     TUPLE: (
000006C6                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000006D2                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
000006E9                         STR: 'PISTOL_BLINDING_SHOT_BLINDNESS_EFFECT_DURATION' (2E 00 00 00 50 49 53 54 4F 4C 5F 42 4C 49 4E 44 49 4E 47 5F 53 48 4F 54 5F 42 4C 49 4E 44 4E 45 53 53 5F 45 46 46 45 43 54 5F 44 55 52 41 54 49 4F 4E),
0000071C                         STR: 'PISTOL_BLINDING_SHOT_DAMAGE' (1B 00 00 00 50 49 53 54 4F 4C 5F 42 4C 49 4E 44 49 4E 47 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
0000073C                         STR: 'SE' (02 00 00 00 53 45),
00000743                         STR: 'EnableBlindness' (0F 00 00 00 45 6E 61 62 6C 65 42 6C 69 6E 64 6E 65 73 73),
00000757                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000763                         STR: 'msg' (03 00 00 00 6D 73 67),
0000076B                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
0000077E                         STR: 'PistolBlindingShotAbility' (19 00 00 00 50 69 73 74 6F 6C 42 6C 69 6E 64 69 6E 67 53 68 6F 74 41 62 69 6C 69 74 79),
0000079C                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
000007AA                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
000007C8                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
000007D3                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
000007F1                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
000007FD                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00000815                     TUPLE: (
0000081A                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000826                         STR: 'msg' (03 00 00 00 6D 73 67),
0000082E                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00000839                     TUPLE: ()
                         cellvars:
0000083E                     TUPLE: ()
                         filename:
00000843                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_pistol.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 70 69 73 74 6F 6C 2E 70 79)
                         name:
0000089D                     STR: 'PistolBlindingShot_DirectObject' (1F 00 00 00 50 69 73 74 6F 6C 42 6C 69 6E 64 69 6E 67 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
000008C1                     LONG: 55L (37 00 00 00)
                         lnotab:
000008C5                     STR: '\x00\x01\x17\x04\x1c\x01\x18\x01' (08 00 00 00 00 01 17 04 1C 01 18 01),
000008D2             CODE:
                         argcount:
000008D3                     LONG: 2L (02 00 00 00)
                         nlocals:
000008D7                     LONG: 3L (03 00 00 00)
                         stacksize:
000008DB                     LONG: 6L (06 00 00 00)
                         flags:
000008DF                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000008E3                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'PistolDash: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'PISTOL_DASH_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'PISTOL_DASH_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'PistolDashAbility'
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
00000934                     TUPLE: (
00000939                         None (4E),
0000093A                         STR: 'PistolDash: %d damage dealt' (1B 00 00 00 50 69 73 74 6F 6C 44 61 73 68 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
0000095A                     TUPLE: (
0000095F                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
0000096B                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000982                         STR: 'PISTOL_DASH_DAMAGE' (12 00 00 00 50 49 53 54 4F 4C 5F 44 41 53 48 5F 44 41 4D 41 47 45),
00000999                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000009A5                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
000009B3                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
000009D1                         STR: 'msg' (03 00 00 00 6D 73 67),
000009D9                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
000009EC                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
000009F7                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00000A15                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00000A21                         STR: 'PistolDashAbility' (11 00 00 00 50 69 73 74 6F 6C 44 61 73 68 41 62 69 6C 69 74 79),
00000A37                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00000A4F                     TUPLE: (
00000A54                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000A60                         STR: 'msg' (03 00 00 00 6D 73 67),
00000A68                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00000A73                     TUPLE: ()
                         cellvars:
00000A78                     TUPLE: ()
                         filename:
00000A7D                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_pistol.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 70 69 73 74 6F 6C 2E 70 79)
                         name:
00000AD7                     STR: 'PistolDash_DirectObject' (17 00 00 00 50 69 73 74 6F 6C 44 61 73 68 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000AF3                     LONG: 67L (43 00 00 00)
                         lnotab:
00000AF7                     STR: '\x00\x01\x11\x01\x18\x01' (06 00 00 00 00 01 11 01 18 01),
00000B02             CODE:
                         argcount:
00000B03                     LONG: 2L (02 00 00 00)
                         nlocals:
00000B07                     LONG: 3L (03 00 00 00)
                         stacksize:
00000B0B                     LONG: 6L (06 00 00 00)
                         flags:
00000B0F                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000B13                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00\x83\x01\x00\x01|\x00\x00i\x04\x00i\x08\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\n\x00t\x0b\x00t\x0c\x00|\x01\x00i\x07\x00|\x01\x00i\r\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (5F 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 83 01 00 01 7C 00 00 69 04 00 69 08 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 0A 00 74 0B 00 74 0C 00 7C 01 00 69 07 00 7C 01 00 69 0D 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'PistolDisarmingShot: weapon unequipped and %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'PISTOL_DISARMING_SHOT_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'unequipWeapon'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     83 - CALL_FUNCTION       r0001
                             00000023     01 - POP_TOP             
                             00000024     7C - LOAD_FAST           'subject'
                             00000027     69 - LOAD_ATTR           'Interlock'
                             0000002A     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000002D     7C - LOAD_FAST           'msg'
                             00000030     69 - LOAD_ATTR           'subjectLocator'
                             00000033     74 - LOAD_GLOBAL         'PISTOL_DISARMING_SHOT_DAMAGE'
                             00000036     83 - CALL_FUNCTION       r0002
                             00000039     7D - STORE_FAST          'damage'
                             0000003C     74 - LOAD_GLOBAL         'Utility'
                             0000003F     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             00000042     74 - LOAD_GLOBAL         'SUCCESS'
                             00000045     74 - LOAD_GLOBAL         'PistolDisarmingShotAbility'
                             00000048     7C - LOAD_FAST           'msg'
                             0000004B     69 - LOAD_ATTR           'subjectLocator'
                             0000004E     7C - LOAD_FAST           'msg'
                             00000051     69 - LOAD_ATTR           'directObjectLocator'
                             00000054     7C - LOAD_FAST           'damage'
                             00000057     83 - CALL_FUNCTION       r0005
                             0000005A     01 - POP_TOP             
                             0000005B     64 - LOAD_CONST          None
                             0000005E     53 - RETURN_VALUE        
                         consts:
00000B77                     TUPLE: (
00000B7C                         None (4E),
00000B7D                         STR: 'PistolDisarmingShot: weapon unequipped and %d damage dealt' (3A 00 00 00 50 69 73 74 6F 6C 44 69 73 61 72 6D 69 6E 67 53 68 6F 74 3A 20 77 65 61 70 6F 6E 20 75 6E 65 71 75 69 70 70 65 64 20 61 6E 64 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
00000BBC                     TUPLE: (
00000BC1                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000BCD                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000BE4                         STR: 'PISTOL_DISARMING_SHOT_DAMAGE' (1C 00 00 00 50 49 53 54 4F 4C 5F 44 49 53 41 52 4D 49 4E 47 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
00000C05                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000C11                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00000C1F                         STR: 'unequipWeapon' (0D 00 00 00 75 6E 65 71 75 69 70 57 65 61 70 6F 6E),
00000C31                         STR: 'msg' (03 00 00 00 6D 73 67),
00000C39                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00000C4C                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00000C6A                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
00000C75                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00000C93                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00000C9F                         STR: 'PistolDisarmingShotAbility' (1A 00 00 00 50 69 73 74 6F 6C 44 69 73 61 72 6D 69 6E 67 53 68 6F 74 41 62 69 6C 69 74 79),
00000CBE                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00000CD6                     TUPLE: (
00000CDB                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000CE7                         STR: 'msg' (03 00 00 00 6D 73 67),
00000CEF                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00000CFA                     TUPLE: ()
                         cellvars:
00000CFF                     TUPLE: ()
                         filename:
00000D04                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_pistol.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 70 69 73 74 6F 6C 2E 70 79)
                         name:
00000D5E                     STR: 'PistolDisarmingShot_DirectObject' (20 00 00 00 50 69 73 74 6F 6C 44 69 73 61 72 6D 69 6E 67 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000D83                     LONG: 76L (4C 00 00 00)
                         lnotab:
00000D87                     STR: '\x00\x01\x11\x03\x13\x01\x18\x01' (08 00 00 00 00 01 11 03 13 01 18 01),
00000D94             CODE:
                         argcount:
00000D95                     LONG: 2L (02 00 00 00)
                         nlocals:
00000D99                     LONG: 3L (03 00 00 00)
                         stacksize:
00000D9D                     LONG: 6L (06 00 00 00)
                         flags:
00000DA1                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000DA5                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'PistolEvasive: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'PISTOL_EVASIVE_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'PISTOL_EVASIVE_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'PistolEvasiveAbility'
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
00000DF6                     TUPLE: (
00000DFB                         None (4E),
00000DFC                         STR: 'PistolEvasive: %d damage dealt' (1E 00 00 00 50 69 73 74 6F 6C 45 76 61 73 69 76 65 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
00000E1F                     TUPLE: (
00000E24                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000E30                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000E47                         STR: 'PISTOL_EVASIVE_DAMAGE' (15 00 00 00 50 49 53 54 4F 4C 5F 45 56 41 53 49 56 45 5F 44 41 4D 41 47 45),
00000E61                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000E6D                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00000E7B                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00000E99                         STR: 'msg' (03 00 00 00 6D 73 67),
00000EA1                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00000EB4                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
00000EBF                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00000EDD                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00000EE9                         STR: 'PistolEvasiveAbility' (14 00 00 00 50 69 73 74 6F 6C 45 76 61 73 69 76 65 41 62 69 6C 69 74 79),
00000F02                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00000F1A                     TUPLE: (
00000F1F                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000F2B                         STR: 'msg' (03 00 00 00 6D 73 67),
00000F33                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00000F3E                     TUPLE: ()
                         cellvars:
00000F43                     TUPLE: ()
                         filename:
00000F48                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_pistol.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 70 69 73 74 6F 6C 2E 70 79)
                         name:
00000FA2                     STR: 'PistolEvasive_DirectObject' (1A 00 00 00 50 69 73 74 6F 6C 45 76 61 73 69 76 65 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000FC1                     LONG: 87L (57 00 00 00)
                         lnotab:
00000FC5                     STR: '\x00\x01\x11\x01\x18\x01' (06 00 00 00 00 01 11 01 18 01),
00000FD0             CODE:
                         argcount:
00000FD1                     LONG: 2L (02 00 00 00)
                         nlocals:
00000FD5                     LONG: 4L (04 00 00 00)
                         stacksize:
00000FD9                     LONG: 7L (07 00 00 00)
                         flags:
00000FDD                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000FE1                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00t\x03\x00f\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x05\x00i\x06\x00t\x07\x00t\x08\x00t\x02\x00\x83\x03\x00}\x03\x00|\x00\x00i\x05\x00i\x06\x00t\n\x00t\x08\x00t\x02\x00\x83\x03\x00}\x02\x00|\x00\x00i\x05\x00i\x0c\x00t\r\x00t\x0e\x00|\x03\x00t\x03\x00d\x02\x00d\x02\x00\x83\x06\x00\x01|\x00\x00i\x05\x00i\x0c\x00t\r\x00t\x0e\x00|\x02\x00t\x03\x00d\x02\x00d\x02\x00\x83\x06\x00\x01d\x00\x00S' (89 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 74 03 00 66 02 00 16 83 01 00 01 7C 00 00 69 05 00 69 06 00 74 07 00 74 08 00 74 02 00 83 03 00 7D 03 00 7C 00 00 69 05 00 69 06 00 74 0A 00 74 08 00 74 02 00 83 03 00 7D 02 00 7C 00 00 69 05 00 69 0C 00 74 0D 00 74 0E 00 7C 03 00 74 03 00 64 02 00 64 02 00 83 06 00 01 7C 00 00 69 05 00 69 0C 00 74 0D 00 74 0E 00 7C 02 00 74 03 00 64 02 00 64 02 00 83 06 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'PistolEvasive: %d to Defense rolls for %d seconds'
                             00000009     74 - LOAD_GLOBAL         'PISTOL_EVASIVE_BLOCK_BOOST'
                             0000000C     74 - LOAD_GLOBAL         'PISTOL_EVASIVE_BLOCK_BOOST_DURATION'
                             0000000F     66 - BUILD_TUPLE         r0002
                             00000012     16 - BINARY_MODULO       
                             00000013     83 - CALL_FUNCTION       r0001
                             00000016     01 - POP_TOP             
                             00000017     7C - LOAD_FAST           'subject'
                             0000001A     69 - LOAD_ATTR           'AbilityInv'
                             0000001D     69 - LOAD_ATTR           'createSpecificMod'
                             00000020     74 - LOAD_GLOBAL         'MOD_AFFECTS_DEFENSEMOD'
                             00000023     74 - LOAD_GLOBAL         'MOD_BLOCK'
                             00000026     74 - LOAD_GLOBAL         'PISTOL_EVASIVE_BLOCK_BOOST'
                             00000029     83 - CALL_FUNCTION       r0003
                             0000002C     7D - STORE_FAST          'value'
                             0000002F     7C - LOAD_FAST           'subject'
                             00000032     69 - LOAD_ATTR           'AbilityInv'
                             00000035     69 - LOAD_ATTR           'createSpecificMod'
                             00000038     74 - LOAD_GLOBAL         'MOD_AFFECTS_ATTACKMOD'
                             0000003B     74 - LOAD_GLOBAL         'MOD_BLOCK'
                             0000003E     74 - LOAD_GLOBAL         'PISTOL_EVASIVE_BLOCK_BOOST'
                             00000041     83 - CALL_FUNCTION       r0003
                             00000044     7D - STORE_FAST          'value2'
                             00000047     7C - LOAD_FAST           'subject'
                             0000004A     69 - LOAD_ATTR           'AbilityInv'
                             0000004D     69 - LOAD_ATTR           'addTempMod'
                             00000050     74 - LOAD_GLOBAL         'PistolEvasiveAbility'
                             00000053     74 - LOAD_GLOBAL         'CombatModifierAbility'
                             00000056     7C - LOAD_FAST           'value'
                             00000059     74 - LOAD_GLOBAL         'PISTOL_EVASIVE_BLOCK_BOOST_DURATION'
                             0000005C     64 - LOAD_CONST          0
                             0000005F     64 - LOAD_CONST          0
                             00000062     83 - CALL_FUNCTION       r0006
                             00000065     01 - POP_TOP             
                             00000066     7C - LOAD_FAST           'subject'
                             00000069     69 - LOAD_ATTR           'AbilityInv'
                             0000006C     69 - LOAD_ATTR           'addTempMod'
                             0000006F     74 - LOAD_GLOBAL         'PistolEvasiveAbility'
                             00000072     74 - LOAD_GLOBAL         'CombatModifierAbility'
                             00000075     7C - LOAD_FAST           'value2'
                             00000078     74 - LOAD_GLOBAL         'PISTOL_EVASIVE_BLOCK_BOOST_DURATION'
                             0000007B     64 - LOAD_CONST          0
                             0000007E     64 - LOAD_CONST          0
                             00000081     83 - CALL_FUNCTION       r0006
                             00000084     01 - POP_TOP             
                             00000085     64 - LOAD_CONST          None
                             00000088     53 - RETURN_VALUE        
                         consts:
0000106F                     TUPLE: (
00001074                         None (4E),
00001075                         STR: 'PistolEvasive: %d to Defense rolls for %d seconds' (31 00 00 00 50 69 73 74 6F 6C 45 76 61 73 69 76 65 3A 20 25 64 20 74 6F 20 44 65 66 65 6E 73 65 20 72 6F 6C 6C 73 20 66 6F 72 20 25 64 20 73 65 63 6F 6E 64 73),
000010AB                         INT: 0 (00 00 00 00)
                             )
                         names:
000010B0                     TUPLE: (
000010B5                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000010C1                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
000010D8                         STR: 'PISTOL_EVASIVE_BLOCK_BOOST' (1A 00 00 00 50 49 53 54 4F 4C 5F 45 56 41 53 49 56 45 5F 42 4C 4F 43 4B 5F 42 4F 4F 53 54),
000010F7                         STR: 'PISTOL_EVASIVE_BLOCK_BOOST_DURATION' (23 00 00 00 50 49 53 54 4F 4C 5F 45 56 41 53 49 56 45 5F 42 4C 4F 43 4B 5F 42 4F 4F 53 54 5F 44 55 52 41 54 49 4F 4E),
0000111F                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000112B                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
0000113A                         STR: 'createSpecificMod' (11 00 00 00 63 72 65 61 74 65 53 70 65 63 69 66 69 63 4D 6F 64),
00001150                         STR: 'MOD_AFFECTS_DEFENSEMOD' (16 00 00 00 4D 4F 44 5F 41 46 46 45 43 54 53 5F 44 45 46 45 4E 53 45 4D 4F 44),
0000116B                         STR: 'MOD_BLOCK' (09 00 00 00 4D 4F 44 5F 42 4C 4F 43 4B),
00001179                         STR: 'value' (05 00 00 00 76 61 6C 75 65),
00001183                         STR: 'MOD_AFFECTS_ATTACKMOD' (15 00 00 00 4D 4F 44 5F 41 46 46 45 43 54 53 5F 41 54 54 41 43 4B 4D 4F 44),
0000119D                         STR: 'value2' (06 00 00 00 76 61 6C 75 65 32),
000011A8                         STR: 'addTempMod' (0A 00 00 00 61 64 64 54 65 6D 70 4D 6F 64),
000011B7                         STR: 'PistolEvasiveAbility' (14 00 00 00 50 69 73 74 6F 6C 45 76 61 73 69 76 65 41 62 69 6C 69 74 79),
000011D0                         STR: 'CombatModifierAbility' (15 00 00 00 43 6F 6D 62 61 74 4D 6F 64 69 66 69 65 72 41 62 69 6C 69 74 79)
                             )
                         varnames:
000011EA                     TUPLE: (
000011EF                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000011FB                         STR: 'msg' (03 00 00 00 6D 73 67),
00001203                         STR: 'value2' (06 00 00 00 76 61 6C 75 65 32),
0000120E                         STR: 'value' (05 00 00 00 76 61 6C 75 65)
                             )
                         freevars:
00001218                     TUPLE: ()
                         cellvars:
0000121D                     TUPLE: ()
                         filename:
00001222                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_pistol.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 70 69 73 74 6F 6C 2E 70 79)
                         name:
0000127C                     STR: 'PistolEvasive_Subject' (15 00 00 00 50 69 73 74 6F 6C 45 76 61 73 69 76 65 5F 53 75 62 6A 65 63 74)
                         firslineno:
00001296                     LONG: 92L (5C 00 00 00)
                         lnotab:
0000129A                     STR: '\x00\x01\x17\x04\x18\x01\x18\x02\x12\x01\r\x01\x12\x01' (0E 00 00 00 00 01 17 04 18 01 18 02 12 01 0D 01 12 01),
000012AD             CODE:
                         argcount:
000012AE                     LONG: 2L (02 00 00 00)
                         nlocals:
000012B2                     LONG: 3L (03 00 00 00)
                         stacksize:
000012B6                     LONG: 6L (06 00 00 00)
                         flags:
000012BA                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000012BE                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'PistolPointBlank: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'PISTOL_POINT_BLANK_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'PISTOL_POINT_BLANK_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'PistolPointBlankAbility'
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
0000130F                     TUPLE: (
00001314                         None (4E),
00001315                         STR: 'PistolPointBlank: %d damage dealt' (21 00 00 00 50 69 73 74 6F 6C 50 6F 69 6E 74 42 6C 61 6E 6B 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
0000133B                     TUPLE: (
00001340                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
0000134C                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00001363                         STR: 'PISTOL_POINT_BLANK_DAMAGE' (19 00 00 00 50 49 53 54 4F 4C 5F 50 4F 49 4E 54 5F 42 4C 41 4E 4B 5F 44 41 4D 41 47 45),
00001381                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000138D                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
0000139B                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
000013B9                         STR: 'msg' (03 00 00 00 6D 73 67),
000013C1                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
000013D4                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
000013DF                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
000013FD                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00001409                         STR: 'PistolPointBlankAbility' (17 00 00 00 50 69 73 74 6F 6C 50 6F 69 6E 74 42 6C 61 6E 6B 41 62 69 6C 69 74 79),
00001425                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
0000143D                     TUPLE: (
00001442                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000144E                         STR: 'msg' (03 00 00 00 6D 73 67),
00001456                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00001461                     TUPLE: ()
                         cellvars:
00001466                     TUPLE: ()
                         filename:
0000146B                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_pistol.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 70 69 73 74 6F 6C 2E 70 79)
                         name:
000014C5                     STR: 'PistolPointBlank_DirectObject' (1D 00 00 00 50 69 73 74 6F 6C 50 6F 69 6E 74 42 6C 61 6E 6B 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
000014E7                     LONG: 109L (6D 00 00 00)
                         lnotab:
000014EB                     STR: '\x00\x01\x11\x01\x18\x01' (06 00 00 00 00 01 11 01 18 01),
000014F6             CODE:
                         argcount:
000014F7                     LONG: 2L (02 00 00 00)
                         nlocals:
000014FB                     LONG: 3L (03 00 00 00)
                         stacksize:
000014FF                     LONG: 6L (06 00 00 00)
                         flags:
00001503                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001507                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'PistolSlide: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'PISTOL_SLIDE_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'PISTOL_SLIDE_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'PistolSlideAbility'
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
00001558                     TUPLE: (
0000155D                         None (4E),
0000155E                         STR: 'PistolSlide: %d damage dealt' (1C 00 00 00 50 69 73 74 6F 6C 53 6C 69 64 65 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
0000157F                     TUPLE: (
00001584                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00001590                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
000015A7                         STR: 'PISTOL_SLIDE_DAMAGE' (13 00 00 00 50 49 53 54 4F 4C 5F 53 4C 49 44 45 5F 44 41 4D 41 47 45),
000015BF                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000015CB                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
000015D9                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
000015F7                         STR: 'msg' (03 00 00 00 6D 73 67),
000015FF                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00001612                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
0000161D                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
0000163B                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00001647                         STR: 'PistolSlideAbility' (12 00 00 00 50 69 73 74 6F 6C 53 6C 69 64 65 41 62 69 6C 69 74 79),
0000165E                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00001676                     TUPLE: (
0000167B                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00001687                         STR: 'msg' (03 00 00 00 6D 73 67),
0000168F                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
0000169A                     TUPLE: ()
                         cellvars:
0000169F                     TUPLE: ()
                         filename:
000016A4                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_pistol.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 70 69 73 74 6F 6C 2E 70 79)
                         name:
000016FE                     STR: 'PistolSlide_DirectObject' (18 00 00 00 50 69 73 74 6F 6C 53 6C 69 64 65 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
0000171B                     LONG: 117L (75 00 00 00)
                         lnotab:
0000171F                     STR: '\x00\x01\x11\x01\x18\x01' (06 00 00 00 00 01 11 01 18 01),
0000172A             CODE:
                         argcount:
0000172B                     LONG: 2L (02 00 00 00)
                         nlocals:
0000172F                     LONG: 3L (03 00 00 00)
                         stacksize:
00001733                     LONG: 6L (06 00 00 00)
                         flags:
00001737                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000173B                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'PistolExecution: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'PISTOL_EXECUTION_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'PISTOL_EXECUTION_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'PistolExecutionAbility'
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
0000178C                     TUPLE: (
00001791                         None (4E),
00001792                         STR: 'PistolExecution: %d damage dealt' (20 00 00 00 50 69 73 74 6F 6C 45 78 65 63 75 74 69 6F 6E 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
000017B7                     TUPLE: (
000017BC                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000017C8                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
000017DF                         STR: 'PISTOL_EXECUTION_DAMAGE' (17 00 00 00 50 49 53 54 4F 4C 5F 45 58 45 43 55 54 49 4F 4E 5F 44 41 4D 41 47 45),
000017FB                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00001807                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00001815                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00001833                         STR: 'msg' (03 00 00 00 6D 73 67),
0000183B                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
0000184E                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
00001859                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00001877                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00001883                         STR: 'PistolExecutionAbility' (16 00 00 00 50 69 73 74 6F 6C 45 78 65 63 75 74 69 6F 6E 41 62 69 6C 69 74 79),
0000189E                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
000018B6                     TUPLE: (
000018BB                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000018C7                         STR: 'msg' (03 00 00 00 6D 73 67),
000018CF                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
000018DA                     TUPLE: ()
                         cellvars:
000018DF                     TUPLE: ()
                         filename:
000018E4                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_pistol.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 70 69 73 74 6F 6C 2E 70 79)
                         name:
0000193E                     STR: 'PistolExecution_DirectObject' (1C 00 00 00 50 69 73 74 6F 6C 45 78 65 63 75 74 69 6F 6E 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
0000195F                     LONG: 125L (7D 00 00 00)
                         lnotab:
00001963                     STR: '\x00\x01\x11\x01\x18\x01' (06 00 00 00 00 01 11 01 18 01)
                 )
             names:
0000196E         TUPLE: (
00001973             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00001981             STR: 'obj' (03 00 00 00 6F 62 6A),
00001989             STR: 'ability.utility' (0F 00 00 00 61 62 69 6C 69 74 79 2E 75 74 69 6C 69 74 79),
0000199D             STR: 'utility' (07 00 00 00 75 74 69 6C 69 74 79),
000019A9             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000019B5             STR: 'ability.defines' (0F 00 00 00 61 62 69 6C 69 74 79 2E 64 65 66 69 6E 65 73),
000019C9             STR: 'PISTOL_AERIAL_DAMAGE' (14 00 00 00 50 49 53 54 4F 4C 5F 41 45 52 49 41 4C 5F 44 41 4D 41 47 45),
000019E2             STR: 'PISTOL_BARRAGE_DAMAGE' (15 00 00 00 50 49 53 54 4F 4C 5F 42 41 52 52 41 47 45 5F 44 41 4D 41 47 45),
000019FC             STR: 'PISTOL_BLINDING_SHOT_DAMAGE' (1B 00 00 00 50 49 53 54 4F 4C 5F 42 4C 49 4E 44 49 4E 47 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
00001A1C             STR: 'PISTOL_DASH_DAMAGE' (12 00 00 00 50 49 53 54 4F 4C 5F 44 41 53 48 5F 44 41 4D 41 47 45),
00001A33             STR: 'PISTOL_DISARMING_SHOT_DAMAGE' (1C 00 00 00 50 49 53 54 4F 4C 5F 44 49 53 41 52 4D 49 4E 47 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
00001A54             STR: 'PISTOL_EVASIVE_DAMAGE' (15 00 00 00 50 49 53 54 4F 4C 5F 45 56 41 53 49 56 45 5F 44 41 4D 41 47 45),
00001A6E             STR: 'PISTOL_POINT_BLANK_DAMAGE' (19 00 00 00 50 49 53 54 4F 4C 5F 50 4F 49 4E 54 5F 42 4C 41 4E 4B 5F 44 41 4D 41 47 45),
00001A8C             STR: 'PISTOL_SLIDE_DAMAGE' (13 00 00 00 50 49 53 54 4F 4C 5F 53 4C 49 44 45 5F 44 41 4D 41 47 45),
00001AA4             STR: 'PISTOL_EXECUTION_DAMAGE' (17 00 00 00 50 49 53 54 4F 4C 5F 45 58 45 43 55 54 49 4F 4E 5F 44 41 4D 41 47 45),
00001AC0             STR: 'PISTOL_EVASIVE_BLOCK_BOOST_DURATION' (23 00 00 00 50 49 53 54 4F 4C 5F 45 56 41 53 49 56 45 5F 42 4C 4F 43 4B 5F 42 4F 4F 53 54 5F 44 55 52 41 54 49 4F 4E),
00001AE8             STR: 'PISTOL_BLINDING_SHOT_BLINDNESS_EFFECT_DURATION' (2E 00 00 00 50 49 53 54 4F 4C 5F 42 4C 49 4E 44 49 4E 47 5F 53 48 4F 54 5F 42 4C 49 4E 44 4E 45 53 53 5F 45 46 46 45 43 54 5F 44 55 52 41 54 49 4F 4E),
00001B1B             STR: 'PISTOL_AERIAL_EFFECT_DURATION' (1D 00 00 00 50 49 53 54 4F 4C 5F 41 45 52 49 41 4C 5F 45 46 46 45 43 54 5F 44 55 52 41 54 49 4F 4E),
00001B3D             STR: 'PISTOL_EVASIVE_BLOCK_BOOST' (1A 00 00 00 50 49 53 54 4F 4C 5F 45 56 41 53 49 56 45 5F 42 4C 4F 43 4B 5F 42 4F 4F 53 54),
00001B5C             STR: 'PistolAerial_DirectObject' (19 00 00 00 50 69 73 74 6F 6C 41 65 72 69 61 6C 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001B7A             STR: 'PistolBarrage_DirectObject' (1A 00 00 00 50 69 73 74 6F 6C 42 61 72 72 61 67 65 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001B99             STR: 'PistolBlindingShot_DirectObject' (1F 00 00 00 50 69 73 74 6F 6C 42 6C 69 6E 64 69 6E 67 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001BBD             STR: 'PistolDash_DirectObject' (17 00 00 00 50 69 73 74 6F 6C 44 61 73 68 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001BD9             STR: 'PistolDisarmingShot_DirectObject' (20 00 00 00 50 69 73 74 6F 6C 44 69 73 61 72 6D 69 6E 67 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001BFE             STR: 'PistolEvasive_DirectObject' (1A 00 00 00 50 69 73 74 6F 6C 45 76 61 73 69 76 65 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001C1D             STR: 'PistolEvasive_Subject' (15 00 00 00 50 69 73 74 6F 6C 45 76 61 73 69 76 65 5F 53 75 62 6A 65 63 74),
00001C37             STR: 'PistolPointBlank_DirectObject' (1D 00 00 00 50 69 73 74 6F 6C 50 6F 69 6E 74 42 6C 61 6E 6B 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001C59             STR: 'PistolSlide_DirectObject' (18 00 00 00 50 69 73 74 6F 6C 53 6C 69 64 65 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001C76             STR: 'PistolExecution_DirectObject' (1C 00 00 00 50 69 73 74 6F 6C 45 78 65 63 75 74 69 6F 6E 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                 )
             varnames:
00001C97         TUPLE: (
00001C9C             STR: 'PISTOL_DISARMING_SHOT_DAMAGE' (1C 00 00 00 50 49 53 54 4F 4C 5F 44 49 53 41 52 4D 49 4E 47 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
00001CBD             STR: 'PISTOL_EVASIVE_BLOCK_BOOST_DURATION' (23 00 00 00 50 49 53 54 4F 4C 5F 45 56 41 53 49 56 45 5F 42 4C 4F 43 4B 5F 42 4F 4F 53 54 5F 44 55 52 41 54 49 4F 4E),
00001CE5             STR: 'PistolEvasive_Subject' (15 00 00 00 50 69 73 74 6F 6C 45 76 61 73 69 76 65 5F 53 75 62 6A 65 63 74),
00001CFF             STR: 'PISTOL_AERIAL_EFFECT_DURATION' (1D 00 00 00 50 49 53 54 4F 4C 5F 41 45 52 49 41 4C 5F 45 46 46 45 43 54 5F 44 55 52 41 54 49 4F 4E),
00001D21             STR: 'PistolDash_DirectObject' (17 00 00 00 50 69 73 74 6F 6C 44 61 73 68 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001D3D             STR: 'PistolPointBlank_DirectObject' (1D 00 00 00 50 69 73 74 6F 6C 50 6F 69 6E 74 42 6C 61 6E 6B 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001D5F             STR: 'PISTOL_EXECUTION_DAMAGE' (17 00 00 00 50 49 53 54 4F 4C 5F 45 58 45 43 55 54 49 4F 4E 5F 44 41 4D 41 47 45),
00001D7B             STR: 'PistolBarrage_DirectObject' (1A 00 00 00 50 69 73 74 6F 6C 42 61 72 72 61 67 65 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001D9A             STR: 'PISTOL_BARRAGE_DAMAGE' (15 00 00 00 50 49 53 54 4F 4C 5F 42 41 52 52 41 47 45 5F 44 41 4D 41 47 45),
00001DB4             STR: 'PISTOL_SLIDE_DAMAGE' (13 00 00 00 50 49 53 54 4F 4C 5F 53 4C 49 44 45 5F 44 41 4D 41 47 45),
00001DCC             STR: 'PistolExecution_DirectObject' (1C 00 00 00 50 69 73 74 6F 6C 45 78 65 63 75 74 69 6F 6E 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001DED             STR: 'PISTOL_EVASIVE_DAMAGE' (15 00 00 00 50 49 53 54 4F 4C 5F 45 56 41 53 49 56 45 5F 44 41 4D 41 47 45),
00001E07             STR: 'PISTOL_AERIAL_DAMAGE' (14 00 00 00 50 49 53 54 4F 4C 5F 41 45 52 49 41 4C 5F 44 41 4D 41 47 45),
00001E20             STR: 'PistolBlindingShot_DirectObject' (1F 00 00 00 50 69 73 74 6F 6C 42 6C 69 6E 64 69 6E 67 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001E44             STR: 'PistolEvasive_DirectObject' (1A 00 00 00 50 69 73 74 6F 6C 45 76 61 73 69 76 65 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001E63             STR: 'PistolDisarmingShot_DirectObject' (20 00 00 00 50 69 73 74 6F 6C 44 69 73 61 72 6D 69 6E 67 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001E88             STR: 'PISTOL_DASH_DAMAGE' (12 00 00 00 50 49 53 54 4F 4C 5F 44 41 53 48 5F 44 41 4D 41 47 45),
00001E9F             STR: 'obj' (03 00 00 00 6F 62 6A),
00001EA7             STR: 'PistolSlide_DirectObject' (18 00 00 00 50 69 73 74 6F 6C 53 6C 69 64 65 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001EC4             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00001ED2             STR: 'PISTOL_POINT_BLANK_DAMAGE' (19 00 00 00 50 49 53 54 4F 4C 5F 50 4F 49 4E 54 5F 42 4C 41 4E 4B 5F 44 41 4D 41 47 45),
00001EF0             STR: 'PistolAerial_DirectObject' (19 00 00 00 50 69 73 74 6F 6C 41 65 72 69 61 6C 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001F0E             STR: 'PISTOL_EVASIVE_BLOCK_BOOST' (1A 00 00 00 50 49 53 54 4F 4C 5F 45 56 41 53 49 56 45 5F 42 4C 4F 43 4B 5F 42 4F 4F 53 54),
00001F2D             STR: 'PISTOL_BLINDING_SHOT_BLINDNESS_EFFECT_DURATION' (2E 00 00 00 50 49 53 54 4F 4C 5F 42 4C 49 4E 44 49 4E 47 5F 53 48 4F 54 5F 42 4C 49 4E 44 4E 45 53 53 5F 45 46 46 45 43 54 5F 44 55 52 41 54 49 4F 4E),
00001F60             STR: 'PISTOL_BLINDING_SHOT_DAMAGE' (1B 00 00 00 50 49 53 54 4F 4C 5F 42 4C 49 4E 44 49 4E 47 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
00001F80             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79)
                 )
             freevars:
00001F8C         TUPLE: ()
             cellvars:
00001F91         TUPLE: ()
             filename:
00001F96         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_pistol.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 70 69 73 74 6F 6C 2E 70 79)
             name:
00001FF0         STR: '?' (01 00 00 00 3F)
             firslineno:
00001FF6         LONG: 1L (01 00 00 00)
             lnotab:
00001FFA         STR: '\t\x01\t\x01\x0c\x03\x07\x06\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x05\x06\x01\x06\x01\x06\x05\x06\x05\t\n\t\x08\t\x0c\t\t\t\x0b\t\x05\t\x11\t\x08\t\x08' (34 00 00 00 09 01 09 01 0C 03 07 06 06 01 06 01 06 01 06 01 06 01 06 01 06 01 06 01 06 05 06 01 06 01 06 05 06 05 09 0A 09 08 09 0C 09 09 09 0B 09 05 09 11 09 08 09 08)

