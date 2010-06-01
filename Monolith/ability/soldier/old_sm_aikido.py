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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00i\x03\x00Z\x04\x00d\x01\x00k\x05\x00Td\x02\x00Z\x06\x00d\x03\x00Z\x07\x00d\x04\x00Z\x08\x00d\x05\x00Z\t\x00d\x06\x00Z\n\x00d\x07\x00Z\x0b\x00d\x08\x00Z\x0c\x00d\t\x00Z\r\x00d\n\x00Z\x0e\x00d\n\x00Z\x0f\x00d\x0b\x00Z\x10\x00d\x0c\x00Z\x11\x00d\r\x00Z\x12\x00d\x0b\x00Z\x13\x00d\x0e\x00Z\x14\x00d\n\x00Z\x15\x00d\x0f\x00Z\x16\x00d\x10\x00Z\x17\x00d\x11\x00Z\x18\x00d\x11\x00Z\x19\x00d\x11\x00Z\x1a\x00d\x0c\x00Z\x1b\x00d\x11\x00Z\x1c\x00d\x12\x00\x84\x00\x00Z\x1d\x00d\x13\x00\x84\x00\x00Z\x1e\x00d\x14\x00\x84\x00\x00Z\x1f\x00d\x15\x00\x84\x00\x00Z \x00d\x16\x00\x84\x00\x00Z!\x00d\x17\x00\x84\x00\x00Z"\x00d\x18\x00\x84\x00\x00Z#\x00d\x19\x00\x84\x00\x00Z$\x00d\x1a\x00\x84\x00\x00Z%\x00d\x1b\x00\x84\x00\x00Z&\x00d\x00\x00S' (0D 01 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 69 03 00 5A 04 00 64 01 00 6B 05 00 54 64 02 00 5A 06 00 64 03 00 5A 07 00 64 04 00 5A 08 00 64 05 00 5A 09 00 64 06 00 5A 0A 00 64 07 00 5A 0B 00 64 08 00 5A 0C 00 64 09 00 5A 0D 00 64 0A 00 5A 0E 00 64 0A 00 5A 0F 00 64 0B 00 5A 10 00 64 0C 00 5A 11 00 64 0D 00 5A 12 00 64 0B 00 5A 13 00 64 0E 00 5A 14 00 64 0A 00 5A 15 00 64 0F 00 5A 16 00 64 10 00 5A 17 00 64 11 00 5A 18 00 64 11 00 5A 19 00 64 11 00 5A 1A 00 64 0C 00 5A 1B 00 64 11 00 5A 1C 00 64 12 00 84 00 00 5A 1D 00 64 13 00 84 00 00 5A 1E 00 64 14 00 84 00 00 5A 1F 00 64 15 00 84 00 00 5A 20 00 64 16 00 84 00 00 5A 21 00 64 17 00 84 00 00 5A 22 00 64 18 00 84 00 00 5A 23 00 64 19 00 84 00 00 5A 24 00 64 1A 00 84 00 00 5A 25 00 64 1B 00 84 00 00 5A 26 00 64 00 00 53)
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
                 00000025     64 - LOAD_CONST          75
                 00000028     5A - STORE_NAME          'AIKIDO_COUNTER_THROW_DAMAGE'
                 0000002B     64 - LOAD_CONST          90
                 0000002E     5A - STORE_NAME          'AIKIDO_SPINNING_PIGEON_DAMAGE'
                 00000031     64 - LOAD_CONST          300
                 00000034     5A - STORE_NAME          'AIKIDO_AERIAL_TAKEDOWN_DAMAGE'
                 00000037     64 - LOAD_CONST          325
                 0000003A     5A - STORE_NAME          'AIKIDO_PUNCH_REVERSAL_CATCH_SLAM_DAMAGE'
                 0000003D     64 - LOAD_CONST          250
                 00000040     5A - STORE_NAME          'AIKIDO_SWORD_ATTACK_DAMAGE'
                 00000043     64 - LOAD_CONST          100
                 00000046     5A - STORE_NAME          'AIKIDO_ARM_BAR_DAMAGE'
                 00000049     64 - LOAD_CONST          350
                 0000004C     5A - STORE_NAME          'AIKIDO_TOMO_NAGE_DAMAGE'
                 0000004F     64 - LOAD_CONST          215
                 00000052     5A - STORE_NAME          'AIKIDO_MAKI_ONASHI_DAMAGE'
                 00000055     64 - LOAD_CONST          15
                 00000058     5A - STORE_NAME          'AIKIDO_BEND_LIKE_REED_DAMAGE'
                 0000005B     64 - LOAD_CONST          15
                 0000005E     5A - STORE_NAME          'AIKIDO_SPINNING_PIGEON_POWERLESS_TIME'
                 00000061     64 - LOAD_CONST          30
                 00000064     5A - STORE_NAME          'AIKIDO_PUNCH_REVERSAL_CATCH_SLAM_ENRAGE_TIME'
                 00000067     64 - LOAD_CONST          50
                 0000006A     5A - STORE_NAME          'AIKIDO_IRON_GUARD_BLOCK_BOOST'
                 0000006D     64 - LOAD_CONST          60
                 00000070     5A - STORE_NAME          'AIKIDO_IRON_GUARD_BLOCK_EFFECT_DURATION'
                 00000073     64 - LOAD_CONST          30
                 00000076     5A - STORE_NAME          'AIKIDO_TOMO_NAGE_STUN_DURATION'
                 00000079     64 - LOAD_CONST          10
                 0000007C     5A - STORE_NAME          'AIKIDO_COUNTER_THROW_CONFUSE_DURATION'
                 0000007F     64 - LOAD_CONST          15
                 00000082     5A - STORE_NAME          'AIKIDO_ARM_BAR_ENRAGE_DURATION'
                 00000085     64 - LOAD_CONST          25
                 00000088     5A - STORE_NAME          'AIKIDO_SWORD_ATTACK_CONFUSE_DURATION'
                 0000008B     64 - LOAD_CONST          1
                 0000008E     5A - STORE_NAME          'AIKIDO_COUNTER_THROW_POWER_POINT_BOOST'
                 00000091     64 - LOAD_CONST          2
                 00000094     5A - STORE_NAME          'AIKIDO_SWORD_ATTACK_SPEED_POINT_LOSS'
                 00000097     64 - LOAD_CONST          2
                 0000009A     5A - STORE_NAME          'AIKIDO_PERFECT_SELF_DEFENSE_POINT_BOOST'
                 0000009D     64 - LOAD_CONST          2
                 000000A0     5A - STORE_NAME          'AIKIDO_ARM_BAR_POWER_POINT_LOSS'
                 000000A3     64 - LOAD_CONST          50
                 000000A6     5A - STORE_NAME          'AIKIDO_IRON_GUARD_DEFENSE_SETTING_BOOST'
                 000000A9     64 - LOAD_CONST          2
                 000000AC     5A - STORE_NAME          'AIKIDO_BEND_LIKE_REED_POWER_POINT_LOSS'
                 000000AF     64 - LOAD_CONST          CODE('AikidoAerialTakedown_DirectObject')
                 000000B2     84 - MAKE_FUNCTION       r0000
                 000000B5     5A - STORE_NAME          'AikidoAerialTakedown_DirectObject'
                 000000B8     64 - LOAD_CONST          CODE('AikidoCounterThrow_DirectObject')
                 000000BB     84 - MAKE_FUNCTION       r0000
                 000000BE     5A - STORE_NAME          'AikidoCounterThrow_DirectObject'
                 000000C1     64 - LOAD_CONST          CODE('AikidoArmBar_DirectObject')
                 000000C4     84 - MAKE_FUNCTION       r0000
                 000000C7     5A - STORE_NAME          'AikidoArmBar_DirectObject'
                 000000CA     64 - LOAD_CONST          CODE('AikidoIronGuard_Subject')
                 000000CD     84 - MAKE_FUNCTION       r0000
                 000000D0     5A - STORE_NAME          'AikidoIronGuard_Subject'
                 000000D3     64 - LOAD_CONST          CODE('AikidoTomoNage_DirectObject')
                 000000D6     84 - MAKE_FUNCTION       r0000
                 000000D9     5A - STORE_NAME          'AikidoTomoNage_DirectObject'
                 000000DC     64 - LOAD_CONST          CODE('AikidoMakiOnashi_DirectObject')
                 000000DF     84 - MAKE_FUNCTION       r0000
                 000000E2     5A - STORE_NAME          'AikidoMakiOnashi_DirectObject'
                 000000E5     64 - LOAD_CONST          CODE('AikidoPunchReversalCatchSlam_DirectObject')
                 000000E8     84 - MAKE_FUNCTION       r0000
                 000000EB     5A - STORE_NAME          'AikidoPunchReversalCatchSlam_DirectObject'
                 000000EE     64 - LOAD_CONST          CODE('AikidoSpinningClayPigeon_DirectObject')
                 000000F1     84 - MAKE_FUNCTION       r0000
                 000000F4     5A - STORE_NAME          'AikidoSpinningClayPigeon_DirectObject'
                 000000F7     64 - LOAD_CONST          CODE('AikidoSpinningClayPigeon_Deactivate')
                 000000FA     84 - MAKE_FUNCTION       r0000
                 000000FD     5A - STORE_NAME          'AikidoSpinningClayPigeon_Deactivate'
                 00000100     64 - LOAD_CONST          CODE('AikidoSwordAttack_DirectObject')
                 00000103     84 - MAKE_FUNCTION       r0000
                 00000106     5A - STORE_NAME          'AikidoSwordAttack_DirectObject'
                 00000109     64 - LOAD_CONST          None
                 0000010C     53 - RETURN_VALUE        
             consts:
0000012B         TUPLE: (
00000130             None (4E),
00000131             TUPLE: (
00000136                 STR: '*' (01 00 00 00 2A)
                     ),
0000013C             INT: 75 (4B 00 00 00),
00000141             INT: 90 (5A 00 00 00),
00000146             INT: 300 (2C 01 00 00),
0000014B             INT: 325 (45 01 00 00),
00000150             INT: 250 (FA 00 00 00),
00000155             INT: 100 (64 00 00 00),
0000015A             INT: 350 (5E 01 00 00),
0000015F             INT: 215 (D7 00 00 00),
00000164             INT: 15 (0F 00 00 00),
00000169             INT: 30 (1E 00 00 00),
0000016E             INT: 50 (32 00 00 00),
00000173             INT: 60 (3C 00 00 00),
00000178             INT: 10 (0A 00 00 00),
0000017D             INT: 25 (19 00 00 00),
00000182             INT: 1 (01 00 00 00),
00000187             INT: 2 (02 00 00 00),
0000018C             CODE:
                         argcount:
0000018D                     LONG: 2L (02 00 00 00)
                         nlocals:
00000191                     LONG: 3L (03 00 00 00)
                         stacksize:
00000195                     LONG: 6L (06 00 00 00)
                         flags:
00000199                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000019D                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'AikidoAerialTakedown: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'AIKIDO_AERIAL_TAKEDOWN_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'AIKIDO_AERIAL_TAKEDOWN_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'AikidoAerialTakedownAbility'
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
000001EE                     TUPLE: (
000001F3                         None (4E),
000001F4                         STR: 'AikidoAerialTakedown: %d damage dealt' (25 00 00 00 41 69 6B 69 64 6F 41 65 72 69 61 6C 54 61 6B 65 64 6F 77 6E 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
0000021E                     TUPLE: (
00000223                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
0000022F                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000246                         STR: 'AIKIDO_AERIAL_TAKEDOWN_DAMAGE' (1D 00 00 00 41 49 4B 49 44 4F 5F 41 45 52 49 41 4C 5F 54 41 4B 45 44 4F 57 4E 5F 44 41 4D 41 47 45),
00000268                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000274                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00000282                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
000002A0                         STR: 'msg' (03 00 00 00 6D 73 67),
000002A8                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
000002BB                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
000002C6                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
000002E4                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
000002F0                         STR: 'AikidoAerialTakedownAbility' (1B 00 00 00 41 69 6B 69 64 6F 41 65 72 69 61 6C 54 61 6B 65 64 6F 77 6E 41 62 69 6C 69 74 79),
00000310                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00000328                     TUPLE: (
0000032D                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000339                         STR: 'msg' (03 00 00 00 6D 73 67),
00000341                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
0000034C                     TUPLE: ()
                         cellvars:
00000351                     TUPLE: ()
                         filename:
00000356                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_aikido.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 61 69 6B 69 64 6F 2E 70 79)
                         name:
000003B0                     STR: 'AikidoAerialTakedown_DirectObject' (21 00 00 00 41 69 6B 69 64 6F 41 65 72 69 61 6C 54 61 6B 65 64 6F 77 6E 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
000003D6                     LONG: 49L (31 00 00 00)
                         lnotab:
000003DA                     STR: '\x00\x01\x11\x03\x18\x01' (06 00 00 00 00 01 11 03 18 01),
000003E5             CODE:
                         argcount:
000003E6                     LONG: 2L (02 00 00 00)
                         nlocals:
000003EA                     LONG: 3L (03 00 00 00)
                         stacksize:
000003EE                     LONG: 6L (06 00 00 00)
                         flags:
000003F2                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000003F6                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'AikidoCounterThrow: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'AIKIDO_COUNTER_THROW_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'AIKIDO_COUNTER_THROW_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'AikidoCounterThrowAbility'
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
00000447                     TUPLE: (
0000044C                         None (4E),
0000044D                         STR: 'AikidoCounterThrow: %d damage dealt' (23 00 00 00 41 69 6B 69 64 6F 43 6F 75 6E 74 65 72 54 68 72 6F 77 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
00000475                     TUPLE: (
0000047A                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000486                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
0000049D                         STR: 'AIKIDO_COUNTER_THROW_DAMAGE' (1B 00 00 00 41 49 4B 49 44 4F 5F 43 4F 55 4E 54 45 52 5F 54 48 52 4F 57 5F 44 41 4D 41 47 45),
000004BD                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000004C9                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
000004D7                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
000004F5                         STR: 'msg' (03 00 00 00 6D 73 67),
000004FD                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00000510                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
0000051B                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00000539                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00000545                         STR: 'AikidoCounterThrowAbility' (19 00 00 00 41 69 6B 69 64 6F 43 6F 75 6E 74 65 72 54 68 72 6F 77 41 62 69 6C 69 74 79),
00000563                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
0000057B                     TUPLE: (
00000580                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000058C                         STR: 'msg' (03 00 00 00 6D 73 67),
00000594                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
0000059F                     TUPLE: ()
                         cellvars:
000005A4                     TUPLE: ()
                         filename:
000005A9                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_aikido.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 61 69 6B 69 64 6F 2E 70 79)
                         name:
00000603                     STR: 'AikidoCounterThrow_DirectObject' (1F 00 00 00 41 69 6B 69 64 6F 43 6F 75 6E 74 65 72 54 68 72 6F 77 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000627                     LONG: 60L (3C 00 00 00)
                         lnotab:
0000062B                     STR: '\x00\x01\x11\x03\x18\x01' (06 00 00 00 00 01 11 03 18 01),
00000636             CODE:
                         argcount:
00000637                     LONG: 2L (02 00 00 00)
                         nlocals:
0000063B                     LONG: 3L (03 00 00 00)
                         stacksize:
0000063F                     LONG: 6L (06 00 00 00)
                         flags:
00000643                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000647                     STR: '|\x00\x00i\x01\x00i\x02\x00|\x01\x00i\x04\x00t\x05\x00\x83\x02\x00}\x02\x00t\x07\x00i\x08\x00t\t\x00t\n\x00|\x01\x00i\x04\x00|\x01\x00i\x0b\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (3B 00 00 00 7C 00 00 69 01 00 69 02 00 7C 01 00 69 04 00 74 05 00 83 02 00 7D 02 00 74 07 00 69 08 00 74 09 00 74 0A 00 7C 01 00 69 04 00 7C 01 00 69 0B 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     7C - LOAD_FAST           'subject'
                             00000003     69 - LOAD_ATTR           'Interlock'
                             00000006     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             00000009     7C - LOAD_FAST           'msg'
                             0000000C     69 - LOAD_ATTR           'subjectLocator'
                             0000000F     74 - LOAD_GLOBAL         'AIKIDO_ARM_BAR_DAMAGE'
                             00000012     83 - CALL_FUNCTION       r0002
                             00000015     7D - STORE_FAST          'damage'
                             00000018     74 - LOAD_GLOBAL         'Utility'
                             0000001B     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000001E     74 - LOAD_GLOBAL         'SUCCESS'
                             00000021     74 - LOAD_GLOBAL         'AikidoArmBarAbility'
                             00000024     7C - LOAD_FAST           'msg'
                             00000027     69 - LOAD_ATTR           'subjectLocator'
                             0000002A     7C - LOAD_FAST           'msg'
                             0000002D     69 - LOAD_ATTR           'directObjectLocator'
                             00000030     7C - LOAD_FAST           'damage'
                             00000033     83 - CALL_FUNCTION       r0005
                             00000036     01 - POP_TOP             
                             00000037     64 - LOAD_CONST          None
                             0000003A     53 - RETURN_VALUE        
                         consts:
00000687                     TUPLE: (
0000068C                         None (4E)
                             )
                         names:
0000068D                     TUPLE: (
00000692                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000069E                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
000006AC                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
000006CA                         STR: 'msg' (03 00 00 00 6D 73 67),
000006D2                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
000006E5                         STR: 'AIKIDO_ARM_BAR_DAMAGE' (15 00 00 00 41 49 4B 49 44 4F 5F 41 52 4D 5F 42 41 52 5F 44 41 4D 41 47 45),
000006FF                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
0000070A                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000716                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00000734                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00000740                         STR: 'AikidoArmBarAbility' (13 00 00 00 41 69 6B 69 64 6F 41 72 6D 42 61 72 41 62 69 6C 69 74 79),
00000758                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00000770                     TUPLE: (
00000775                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000781                         STR: 'msg' (03 00 00 00 6D 73 67),
00000789                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00000794                     TUPLE: ()
                         cellvars:
00000799                     TUPLE: ()
                         filename:
0000079E                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_aikido.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 61 69 6B 69 64 6F 2E 70 79)
                         name:
000007F8                     STR: 'AikidoArmBar_DirectObject' (19 00 00 00 41 69 6B 69 64 6F 41 72 6D 42 61 72 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000816                     LONG: 74L (4A 00 00 00)
                         lnotab:
0000081A                     STR: '\x00\x01\x18\x01' (04 00 00 00 00 01 18 01),
00000823             CODE:
                         argcount:
00000824                     LONG: 2L (02 00 00 00)
                         nlocals:
00000828                     LONG: 4L (04 00 00 00)
                         stacksize:
0000082C                     LONG: 7L (07 00 00 00)
                         flags:
00000830                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000834                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00t\x06\x00t\x07\x00t\x02\x00\x83\x03\x00}\x02\x00|\x00\x00i\x04\x00i\x05\x00t\t\x00t\x07\x00t\x02\x00\x83\x03\x00}\x03\x00|\x00\x00i\x04\x00i\x0b\x00t\x0c\x00t\r\x00|\x02\x00t\x0e\x00d\x02\x00d\x02\x00\x83\x06\x00\x01|\x00\x00i\x04\x00i\x0b\x00t\x0c\x00t\r\x00|\x03\x00t\x0e\x00d\x02\x00d\x02\x00\x83\x06\x00\x01d\x00\x00S' (83 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 74 06 00 74 07 00 74 02 00 83 03 00 7D 02 00 7C 00 00 69 04 00 69 05 00 74 09 00 74 07 00 74 02 00 83 03 00 7D 03 00 7C 00 00 69 04 00 69 0B 00 74 0C 00 74 0D 00 7C 02 00 74 0E 00 64 02 00 64 02 00 83 06 00 01 7C 00 00 69 04 00 69 0B 00 74 0C 00 74 0D 00 7C 03 00 74 0E 00 64 02 00 64 02 00 83 06 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'AikidoIronGuard: %d to Defense tactical setting'
                             00000009     74 - LOAD_GLOBAL         'AIKIDO_IRON_GUARD_BLOCK_BOOST'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'AbilityInv'
                             00000017     69 - LOAD_ATTR           'createSpecificMod'
                             0000001A     74 - LOAD_GLOBAL         'MOD_AFFECTS_DEFENSEMOD'
                             0000001D     74 - LOAD_GLOBAL         'MOD_BLOCK'
                             00000020     74 - LOAD_GLOBAL         'AIKIDO_IRON_GUARD_BLOCK_BOOST'
                             00000023     83 - CALL_FUNCTION       r0003
                             00000026     7D - STORE_FAST          'value'
                             00000029     7C - LOAD_FAST           'subject'
                             0000002C     69 - LOAD_ATTR           'AbilityInv'
                             0000002F     69 - LOAD_ATTR           'createSpecificMod'
                             00000032     74 - LOAD_GLOBAL         'MOD_AFFECTS_ATTACKMOD'
                             00000035     74 - LOAD_GLOBAL         'MOD_BLOCK'
                             00000038     74 - LOAD_GLOBAL         'AIKIDO_IRON_GUARD_BLOCK_BOOST'
                             0000003B     83 - CALL_FUNCTION       r0003
                             0000003E     7D - STORE_FAST          'value2'
                             00000041     7C - LOAD_FAST           'subject'
                             00000044     69 - LOAD_ATTR           'AbilityInv'
                             00000047     69 - LOAD_ATTR           'addTempMod'
                             0000004A     74 - LOAD_GLOBAL         'AikidoIronGuardAbility'
                             0000004D     74 - LOAD_GLOBAL         'CombatModifierAbility'
                             00000050     7C - LOAD_FAST           'value'
                             00000053     74 - LOAD_GLOBAL         'AIKIDO_IRON_GUARD_BLOCK_EFFECT_DURATION'
                             00000056     64 - LOAD_CONST          0
                             00000059     64 - LOAD_CONST          0
                             0000005C     83 - CALL_FUNCTION       r0006
                             0000005F     01 - POP_TOP             
                             00000060     7C - LOAD_FAST           'subject'
                             00000063     69 - LOAD_ATTR           'AbilityInv'
                             00000066     69 - LOAD_ATTR           'addTempMod'
                             00000069     74 - LOAD_GLOBAL         'AikidoIronGuardAbility'
                             0000006C     74 - LOAD_GLOBAL         'CombatModifierAbility'
                             0000006F     7C - LOAD_FAST           'value2'
                             00000072     74 - LOAD_GLOBAL         'AIKIDO_IRON_GUARD_BLOCK_EFFECT_DURATION'
                             00000075     64 - LOAD_CONST          0
                             00000078     64 - LOAD_CONST          0
                             0000007B     83 - CALL_FUNCTION       r0006
                             0000007E     01 - POP_TOP             
                             0000007F     64 - LOAD_CONST          None
                             00000082     53 - RETURN_VALUE        
                         consts:
000008BC                     TUPLE: (
000008C1                         None (4E),
000008C2                         STR: 'AikidoIronGuard: %d to Defense tactical setting' (2F 00 00 00 41 69 6B 69 64 6F 49 72 6F 6E 47 75 61 72 64 3A 20 25 64 20 74 6F 20 44 65 66 65 6E 73 65 20 74 61 63 74 69 63 61 6C 20 73 65 74 74 69 6E 67),
000008F6                         INT: 0 (00 00 00 00)
                             )
                         names:
000008FB                     TUPLE: (
00000900                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
0000090C                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000923                         STR: 'AIKIDO_IRON_GUARD_BLOCK_BOOST' (1D 00 00 00 41 49 4B 49 44 4F 5F 49 52 4F 4E 5F 47 55 41 52 44 5F 42 4C 4F 43 4B 5F 42 4F 4F 53 54),
00000945                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000951                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
00000960                         STR: 'createSpecificMod' (11 00 00 00 63 72 65 61 74 65 53 70 65 63 69 66 69 63 4D 6F 64),
00000976                         STR: 'MOD_AFFECTS_DEFENSEMOD' (16 00 00 00 4D 4F 44 5F 41 46 46 45 43 54 53 5F 44 45 46 45 4E 53 45 4D 4F 44),
00000991                         STR: 'MOD_BLOCK' (09 00 00 00 4D 4F 44 5F 42 4C 4F 43 4B),
0000099F                         STR: 'value' (05 00 00 00 76 61 6C 75 65),
000009A9                         STR: 'MOD_AFFECTS_ATTACKMOD' (15 00 00 00 4D 4F 44 5F 41 46 46 45 43 54 53 5F 41 54 54 41 43 4B 4D 4F 44),
000009C3                         STR: 'value2' (06 00 00 00 76 61 6C 75 65 32),
000009CE                         STR: 'addTempMod' (0A 00 00 00 61 64 64 54 65 6D 70 4D 6F 64),
000009DD                         STR: 'AikidoIronGuardAbility' (16 00 00 00 41 69 6B 69 64 6F 49 72 6F 6E 47 75 61 72 64 41 62 69 6C 69 74 79),
000009F8                         STR: 'CombatModifierAbility' (15 00 00 00 43 6F 6D 62 61 74 4D 6F 64 69 66 69 65 72 41 62 69 6C 69 74 79),
00000A12                         STR: 'AIKIDO_IRON_GUARD_BLOCK_EFFECT_DURATION' (27 00 00 00 41 49 4B 49 44 4F 5F 49 52 4F 4E 5F 47 55 41 52 44 5F 42 4C 4F 43 4B 5F 45 46 46 45 43 54 5F 44 55 52 41 54 49 4F 4E)
                             )
                         varnames:
00000A3E                     TUPLE: (
00000A43                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000A4F                         STR: 'msg' (03 00 00 00 6D 73 67),
00000A57                         STR: 'value' (05 00 00 00 76 61 6C 75 65),
00000A61                         STR: 'value2' (06 00 00 00 76 61 6C 75 65 32)
                             )
                         freevars:
00000A6C                     TUPLE: ()
                         cellvars:
00000A71                     TUPLE: ()
                         filename:
00000A76                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_aikido.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 61 69 6B 69 64 6F 2E 70 79)
                         name:
00000AD0                     STR: 'AikidoIronGuard_Subject' (17 00 00 00 41 69 6B 69 64 6F 49 72 6F 6E 47 75 61 72 64 5F 53 75 62 6A 65 63 74)
                         firslineno:
00000AEC                     LONG: 85L (55 00 00 00)
                         lnotab:
00000AF0                     STR: '\x00\x01\x11\x03\x18\x01\x18\x03\x12\x01\r\x01\x12\x01' (0E 00 00 00 00 01 11 03 18 01 18 03 12 01 0D 01 12 01),
00000B03             CODE:
                         argcount:
00000B04                     LONG: 2L (02 00 00 00)
                         nlocals:
00000B08                     LONG: 3L (03 00 00 00)
                         stacksize:
00000B0C                     LONG: 6L (06 00 00 00)
                         flags:
00000B10                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000B14                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'AikidoTomoNage: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'AIKIDO_TOMO_NAGE_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'AIKIDO_TOMO_NAGE_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'AikidoTomoNageAbility'
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
00000B65                     TUPLE: (
00000B6A                         None (4E),
00000B6B                         STR: 'AikidoTomoNage: %d damage dealt' (1F 00 00 00 41 69 6B 69 64 6F 54 6F 6D 6F 4E 61 67 65 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
00000B8F                     TUPLE: (
00000B94                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000BA0                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000BB7                         STR: 'AIKIDO_TOMO_NAGE_DAMAGE' (17 00 00 00 41 49 4B 49 44 4F 5F 54 4F 4D 4F 5F 4E 41 47 45 5F 44 41 4D 41 47 45),
00000BD3                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000BDF                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00000BED                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00000C0B                         STR: 'msg' (03 00 00 00 6D 73 67),
00000C13                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00000C26                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
00000C31                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00000C4F                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00000C5B                         STR: 'AikidoTomoNageAbility' (15 00 00 00 41 69 6B 69 64 6F 54 6F 6D 6F 4E 61 67 65 41 62 69 6C 69 74 79),
00000C75                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00000C8D                     TUPLE: (
00000C92                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000C9E                         STR: 'msg' (03 00 00 00 6D 73 67),
00000CA6                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00000CB1                     TUPLE: ()
                         cellvars:
00000CB6                     TUPLE: ()
                         filename:
00000CBB                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_aikido.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 61 69 6B 69 64 6F 2E 70 79)
                         name:
00000D15                     STR: 'AikidoTomoNage_DirectObject' (1B 00 00 00 41 69 6B 69 64 6F 54 6F 6D 6F 4E 61 67 65 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000D35                     LONG: 102L (66 00 00 00)
                         lnotab:
00000D39                     STR: '\x00\x01\x11\x03\x18\x01' (06 00 00 00 00 01 11 03 18 01),
00000D44             CODE:
                         argcount:
00000D45                     LONG: 2L (02 00 00 00)
                         nlocals:
00000D49                     LONG: 3L (03 00 00 00)
                         stacksize:
00000D4D                     LONG: 6L (06 00 00 00)
                         flags:
00000D51                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000D55                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'AikidoMakiOnashi: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'AIKIDO_MAKI_ONASHI_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'AIKIDO_MAKI_ONASHI_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'AikidoMakiOnashiAbility'
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
00000DA6                     TUPLE: (
00000DAB                         None (4E),
00000DAC                         STR: 'AikidoMakiOnashi: %d damage dealt' (21 00 00 00 41 69 6B 69 64 6F 4D 61 6B 69 4F 6E 61 73 68 69 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
00000DD2                     TUPLE: (
00000DD7                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000DE3                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000DFA                         STR: 'AIKIDO_MAKI_ONASHI_DAMAGE' (19 00 00 00 41 49 4B 49 44 4F 5F 4D 41 4B 49 5F 4F 4E 41 53 48 49 5F 44 41 4D 41 47 45),
00000E18                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000E24                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00000E32                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00000E50                         STR: 'msg' (03 00 00 00 6D 73 67),
00000E58                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00000E6B                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
00000E76                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00000E94                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00000EA0                         STR: 'AikidoMakiOnashiAbility' (17 00 00 00 41 69 6B 69 64 6F 4D 61 6B 69 4F 6E 61 73 68 69 41 62 69 6C 69 74 79),
00000EBC                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00000ED4                     TUPLE: (
00000ED9                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000EE5                         STR: 'msg' (03 00 00 00 6D 73 67),
00000EED                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00000EF8                     TUPLE: ()
                         cellvars:
00000EFD                     TUPLE: ()
                         filename:
00000F02                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_aikido.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 61 69 6B 69 64 6F 2E 70 79)
                         name:
00000F5C                     STR: 'AikidoMakiOnashi_DirectObject' (1D 00 00 00 41 69 6B 69 64 6F 4D 61 6B 69 4F 6E 61 73 68 69 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000F7E                     LONG: 114L (72 00 00 00)
                         lnotab:
00000F82                     STR: '\x00\x01\x11\x01\x18\x01' (06 00 00 00 00 01 11 01 18 01),
00000F8D             CODE:
                         argcount:
00000F8E                     LONG: 2L (02 00 00 00)
                         nlocals:
00000F92                     LONG: 3L (03 00 00 00)
                         stacksize:
00000F96                     LONG: 6L (06 00 00 00)
                         flags:
00000F9A                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000F9E                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'AikidoPunchReversalCatchSlam: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'AIKIDO_PUNCH_REVERSAL_CATCH_SLAM_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'AIKIDO_PUNCH_REVERSAL_CATCH_SLAM_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'AikidoPunchReversalCatchSlamAbility'
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
00000FEF                     TUPLE: (
00000FF4                         None (4E),
00000FF5                         STR: 'AikidoPunchReversalCatchSlam: %d damage dealt' (2D 00 00 00 41 69 6B 69 64 6F 50 75 6E 63 68 52 65 76 65 72 73 61 6C 43 61 74 63 68 53 6C 61 6D 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
00001027                     TUPLE: (
0000102C                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00001038                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
0000104F                         STR: 'AIKIDO_PUNCH_REVERSAL_CATCH_SLAM_DAMAGE' (27 00 00 00 41 49 4B 49 44 4F 5F 50 55 4E 43 48 5F 52 45 56 45 52 53 41 4C 5F 43 41 54 43 48 5F 53 4C 41 4D 5F 44 41 4D 41 47 45),
0000107B                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00001087                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00001095                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
000010B3                         STR: 'msg' (03 00 00 00 6D 73 67),
000010BB                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
000010CE                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
000010D9                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
000010F7                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00001103                         STR: 'AikidoPunchReversalCatchSlamAbility' (23 00 00 00 41 69 6B 69 64 6F 50 75 6E 63 68 52 65 76 65 72 73 61 6C 43 61 74 63 68 53 6C 61 6D 41 62 69 6C 69 74 79),
0000112B                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00001143                     TUPLE: (
00001148                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00001154                         STR: 'msg' (03 00 00 00 6D 73 67),
0000115C                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00001167                     TUPLE: ()
                         cellvars:
0000116C                     TUPLE: ()
                         filename:
00001171                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_aikido.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 61 69 6B 69 64 6F 2E 70 79)
                         name:
000011CB                     STR: 'AikidoPunchReversalCatchSlam_DirectObject' (29 00 00 00 41 69 6B 69 64 6F 50 75 6E 63 68 52 65 76 65 72 73 61 6C 43 61 74 63 68 53 6C 61 6D 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
000011F9                     LONG: 122L (7A 00 00 00)
                         lnotab:
000011FD                     STR: '\x00\x01\x11\x03\x18\x01' (06 00 00 00 00 01 11 03 18 01),
00001208             CODE:
                         argcount:
00001209                     LONG: 2L (02 00 00 00)
                         nlocals:
0000120D                     LONG: 3L (03 00 00 00)
                         stacksize:
00001211                     LONG: 6L (06 00 00 00)
                         flags:
00001215                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001219                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01|\x00\x00i\r\x00i\x0e\x00t\x0b\x00t\x0f\x00\x83\x02\x00\x01d\x00\x00S' (5F 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 7C 00 00 69 0D 00 69 0E 00 74 0B 00 74 0F 00 83 02 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'AikidoCSpinningClayPigeon: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'AIKIDO_SPINNING_PIGEON_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'AIKIDO_SPINNING_PIGEON_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'AikidoSpinningClayPigeonAbility'
                             00000035     7C - LOAD_FAST           'msg'
                             00000038     69 - LOAD_ATTR           'subjectLocator'
                             0000003B     7C - LOAD_FAST           'msg'
                             0000003E     69 - LOAD_ATTR           'directObjectLocator'
                             00000041     7C - LOAD_FAST           'damage'
                             00000044     83 - CALL_FUNCTION       r0005
                             00000047     01 - POP_TOP             
                             00000048     7C - LOAD_FAST           'subject'
                             0000004B     69 - LOAD_ATTR           'AbilityInv'
                             0000004E     69 - LOAD_ATTR           'setDeactivateDelay'
                             00000051     74 - LOAD_GLOBAL         'AikidoSpinningClayPigeonAbility'
                             00000054     74 - LOAD_GLOBAL         'AIKIDO_SPINNING_PIGEON_POWERLESS_TIME'
                             00000057     83 - CALL_FUNCTION       r0002
                             0000005A     01 - POP_TOP             
                             0000005B     64 - LOAD_CONST          None
                             0000005E     53 - RETURN_VALUE        
                         consts:
0000127D                     TUPLE: (
00001282                         None (4E),
00001283                         STR: 'AikidoCSpinningClayPigeon: %d damage dealt' (2A 00 00 00 41 69 6B 69 64 6F 43 53 70 69 6E 6E 69 6E 67 43 6C 61 79 50 69 67 65 6F 6E 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
000012B2                     TUPLE: (
000012B7                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000012C3                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
000012DA                         STR: 'AIKIDO_SPINNING_PIGEON_DAMAGE' (1D 00 00 00 41 49 4B 49 44 4F 5F 53 50 49 4E 4E 49 4E 47 5F 50 49 47 45 4F 4E 5F 44 41 4D 41 47 45),
000012FC                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00001308                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00001316                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00001334                         STR: 'msg' (03 00 00 00 6D 73 67),
0000133C                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
0000134F                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
0000135A                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00001378                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00001384                         STR: 'AikidoSpinningClayPigeonAbility' (1F 00 00 00 41 69 6B 69 64 6F 53 70 69 6E 6E 69 6E 67 43 6C 61 79 50 69 67 65 6F 6E 41 62 69 6C 69 74 79),
000013A8                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
000013C0                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
000013CF                         STR: 'setDeactivateDelay' (12 00 00 00 73 65 74 44 65 61 63 74 69 76 61 74 65 44 65 6C 61 79),
000013E6                         STR: 'AIKIDO_SPINNING_PIGEON_POWERLESS_TIME' (25 00 00 00 41 49 4B 49 44 4F 5F 53 50 49 4E 4E 49 4E 47 5F 50 49 47 45 4F 4E 5F 50 4F 57 45 52 4C 45 53 53 5F 54 49 4D 45)
                             )
                         varnames:
00001410                     TUPLE: (
00001415                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00001421                         STR: 'msg' (03 00 00 00 6D 73 67),
00001429                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00001434                     TUPLE: ()
                         cellvars:
00001439                     TUPLE: ()
                         filename:
0000143E                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_aikido.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 61 69 6B 69 64 6F 2E 70 79)
                         name:
00001498                     STR: 'AikidoSpinningClayPigeon_DirectObject' (25 00 00 00 41 69 6B 69 64 6F 53 70 69 6E 6E 69 6E 67 43 6C 61 79 50 69 67 65 6F 6E 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
000014C2                     LONG: 136L (88 00 00 00)
                         lnotab:
000014C6                     STR: '\x00\x01\x11\x03\x18\x01\x1f\x04' (08 00 00 00 00 01 11 03 18 01 1F 04),
000014D3             CODE:
                         argcount:
000014D4                     LONG: 1L (01 00 00 00)
                         nlocals:
000014D8                     LONG: 1L (01 00 00 00)
                         stacksize:
000014DC                     LONG: 2L (02 00 00 00)
                         flags:
000014E0                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000014E4                     STR: 't\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01d\x00\x00S' (11 00 00 00 74 00 00 69 01 00 64 01 00 83 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'AikidoSpinningClayPigeonAbility: powerless disabling'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     01 - POP_TOP             
                             0000000D     64 - LOAD_CONST          None
                             00000010     53 - RETURN_VALUE        
                         consts:
000014FA                     TUPLE: (
000014FF                         None (4E),
00001500                         STR: 'AikidoSpinningClayPigeonAbility: powerless disabling' (34 00 00 00 41 69 6B 69 64 6F 53 70 69 6E 6E 69 6E 67 43 6C 61 79 50 69 67 65 6F 6E 41 62 69 6C 69 74 79 3A 20 70 6F 77 65 72 6C 65 73 73 20 64 69 73 61 62 6C 69 6E 67)
                             )
                         names:
00001539                     TUPLE: (
0000153E                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
0000154A                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67)
                             )
                         varnames:
00001561                     TUPLE: (
00001566                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74)
                             )
                         freevars:
00001572                     TUPLE: ()
                         cellvars:
00001577                     TUPLE: ()
                         filename:
0000157C                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_aikido.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 61 69 6B 69 64 6F 2E 70 79)
                         name:
000015D6                     STR: 'AikidoSpinningClayPigeon_Deactivate' (23 00 00 00 41 69 6B 69 64 6F 53 70 69 6E 6E 69 6E 67 43 6C 61 79 50 69 67 65 6F 6E 5F 44 65 61 63 74 69 76 61 74 65)
                         firslineno:
000015FE                     LONG: 147L (93 00 00 00)
                         lnotab:
00001602                     STR: '\x00\x01' (02 00 00 00 00 01),
00001609             CODE:
                         argcount:
0000160A                     LONG: 2L (02 00 00 00)
                         nlocals:
0000160E                     LONG: 3L (03 00 00 00)
                         stacksize:
00001612                     LONG: 6L (06 00 00 00)
                         flags:
00001616                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000161A                     STR: '|\x00\x00i\x01\x00i\x02\x00|\x01\x00i\x04\x00t\x05\x00\x83\x02\x00}\x02\x00t\x07\x00i\x08\x00t\t\x00t\n\x00|\x01\x00i\x04\x00|\x01\x00i\x0b\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (3B 00 00 00 7C 00 00 69 01 00 69 02 00 7C 01 00 69 04 00 74 05 00 83 02 00 7D 02 00 74 07 00 69 08 00 74 09 00 74 0A 00 7C 01 00 69 04 00 7C 01 00 69 0B 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     7C - LOAD_FAST           'subject'
                             00000003     69 - LOAD_ATTR           'Interlock'
                             00000006     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             00000009     7C - LOAD_FAST           'msg'
                             0000000C     69 - LOAD_ATTR           'subjectLocator'
                             0000000F     74 - LOAD_GLOBAL         'AIKIDO_SWORD_ATTACK_DAMAGE'
                             00000012     83 - CALL_FUNCTION       r0002
                             00000015     7D - STORE_FAST          'damage'
                             00000018     74 - LOAD_GLOBAL         'Utility'
                             0000001B     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000001E     74 - LOAD_GLOBAL         'SUCCESS'
                             00000021     74 - LOAD_GLOBAL         'AikidoSwordAttackAbility'
                             00000024     7C - LOAD_FAST           'msg'
                             00000027     69 - LOAD_ATTR           'subjectLocator'
                             0000002A     7C - LOAD_FAST           'msg'
                             0000002D     69 - LOAD_ATTR           'directObjectLocator'
                             00000030     7C - LOAD_FAST           'damage'
                             00000033     83 - CALL_FUNCTION       r0005
                             00000036     01 - POP_TOP             
                             00000037     64 - LOAD_CONST          None
                             0000003A     53 - RETURN_VALUE        
                         consts:
0000165A                     TUPLE: (
0000165F                         None (4E)
                             )
                         names:
00001660                     TUPLE: (
00001665                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00001671                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
0000167F                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
0000169D                         STR: 'msg' (03 00 00 00 6D 73 67),
000016A5                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
000016B8                         STR: 'AIKIDO_SWORD_ATTACK_DAMAGE' (1A 00 00 00 41 49 4B 49 44 4F 5F 53 57 4F 52 44 5F 41 54 54 41 43 4B 5F 44 41 4D 41 47 45),
000016D7                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
000016E2                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000016EE                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
0000170C                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00001718                         STR: 'AikidoSwordAttackAbility' (18 00 00 00 41 69 6B 69 64 6F 53 77 6F 72 64 41 74 74 61 63 6B 41 62 69 6C 69 74 79),
00001735                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
0000174D                     TUPLE: (
00001752                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000175E                         STR: 'msg' (03 00 00 00 6D 73 67),
00001766                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00001771                     TUPLE: ()
                         cellvars:
00001776                     TUPLE: ()
                         filename:
0000177B                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_aikido.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 61 69 6B 69 64 6F 2E 70 79)
                         name:
000017D5                     STR: 'AikidoSwordAttack_DirectObject' (1E 00 00 00 41 69 6B 69 64 6F 53 77 6F 72 64 41 74 74 61 63 6B 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
000017F8                     LONG: 155L (9B 00 00 00)
                         lnotab:
000017FC                     STR: '\x00\x02\x18\x01' (04 00 00 00 00 02 18 01)
                 )
             names:
00001805         TUPLE: (
0000180A             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00001818             STR: 'obj' (03 00 00 00 6F 62 6A),
00001820             STR: 'ability.utility' (0F 00 00 00 61 62 69 6C 69 74 79 2E 75 74 69 6C 69 74 79),
00001834             STR: 'utility' (07 00 00 00 75 74 69 6C 69 74 79),
00001840             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
0000184C             STR: 'ability.defines' (0F 00 00 00 61 62 69 6C 69 74 79 2E 64 65 66 69 6E 65 73),
00001860             STR: 'AIKIDO_COUNTER_THROW_DAMAGE' (1B 00 00 00 41 49 4B 49 44 4F 5F 43 4F 55 4E 54 45 52 5F 54 48 52 4F 57 5F 44 41 4D 41 47 45),
00001880             STR: 'AIKIDO_SPINNING_PIGEON_DAMAGE' (1D 00 00 00 41 49 4B 49 44 4F 5F 53 50 49 4E 4E 49 4E 47 5F 50 49 47 45 4F 4E 5F 44 41 4D 41 47 45),
000018A2             STR: 'AIKIDO_AERIAL_TAKEDOWN_DAMAGE' (1D 00 00 00 41 49 4B 49 44 4F 5F 41 45 52 49 41 4C 5F 54 41 4B 45 44 4F 57 4E 5F 44 41 4D 41 47 45),
000018C4             STR: 'AIKIDO_PUNCH_REVERSAL_CATCH_SLAM_DAMAGE' (27 00 00 00 41 49 4B 49 44 4F 5F 50 55 4E 43 48 5F 52 45 56 45 52 53 41 4C 5F 43 41 54 43 48 5F 53 4C 41 4D 5F 44 41 4D 41 47 45),
000018F0             STR: 'AIKIDO_SWORD_ATTACK_DAMAGE' (1A 00 00 00 41 49 4B 49 44 4F 5F 53 57 4F 52 44 5F 41 54 54 41 43 4B 5F 44 41 4D 41 47 45),
0000190F             STR: 'AIKIDO_ARM_BAR_DAMAGE' (15 00 00 00 41 49 4B 49 44 4F 5F 41 52 4D 5F 42 41 52 5F 44 41 4D 41 47 45),
00001929             STR: 'AIKIDO_TOMO_NAGE_DAMAGE' (17 00 00 00 41 49 4B 49 44 4F 5F 54 4F 4D 4F 5F 4E 41 47 45 5F 44 41 4D 41 47 45),
00001945             STR: 'AIKIDO_MAKI_ONASHI_DAMAGE' (19 00 00 00 41 49 4B 49 44 4F 5F 4D 41 4B 49 5F 4F 4E 41 53 48 49 5F 44 41 4D 41 47 45),
00001963             STR: 'AIKIDO_BEND_LIKE_REED_DAMAGE' (1C 00 00 00 41 49 4B 49 44 4F 5F 42 45 4E 44 5F 4C 49 4B 45 5F 52 45 45 44 5F 44 41 4D 41 47 45),
00001984             STR: 'AIKIDO_SPINNING_PIGEON_POWERLESS_TIME' (25 00 00 00 41 49 4B 49 44 4F 5F 53 50 49 4E 4E 49 4E 47 5F 50 49 47 45 4F 4E 5F 50 4F 57 45 52 4C 45 53 53 5F 54 49 4D 45),
000019AE             STR: 'AIKIDO_PUNCH_REVERSAL_CATCH_SLAM_ENRAGE_TIME' (2C 00 00 00 41 49 4B 49 44 4F 5F 50 55 4E 43 48 5F 52 45 56 45 52 53 41 4C 5F 43 41 54 43 48 5F 53 4C 41 4D 5F 45 4E 52 41 47 45 5F 54 49 4D 45),
000019DF             STR: 'AIKIDO_IRON_GUARD_BLOCK_BOOST' (1D 00 00 00 41 49 4B 49 44 4F 5F 49 52 4F 4E 5F 47 55 41 52 44 5F 42 4C 4F 43 4B 5F 42 4F 4F 53 54),
00001A01             STR: 'AIKIDO_IRON_GUARD_BLOCK_EFFECT_DURATION' (27 00 00 00 41 49 4B 49 44 4F 5F 49 52 4F 4E 5F 47 55 41 52 44 5F 42 4C 4F 43 4B 5F 45 46 46 45 43 54 5F 44 55 52 41 54 49 4F 4E),
00001A2D             STR: 'AIKIDO_TOMO_NAGE_STUN_DURATION' (1E 00 00 00 41 49 4B 49 44 4F 5F 54 4F 4D 4F 5F 4E 41 47 45 5F 53 54 55 4E 5F 44 55 52 41 54 49 4F 4E),
00001A50             STR: 'AIKIDO_COUNTER_THROW_CONFUSE_DURATION' (25 00 00 00 41 49 4B 49 44 4F 5F 43 4F 55 4E 54 45 52 5F 54 48 52 4F 57 5F 43 4F 4E 46 55 53 45 5F 44 55 52 41 54 49 4F 4E),
00001A7A             STR: 'AIKIDO_ARM_BAR_ENRAGE_DURATION' (1E 00 00 00 41 49 4B 49 44 4F 5F 41 52 4D 5F 42 41 52 5F 45 4E 52 41 47 45 5F 44 55 52 41 54 49 4F 4E),
00001A9D             STR: 'AIKIDO_SWORD_ATTACK_CONFUSE_DURATION' (24 00 00 00 41 49 4B 49 44 4F 5F 53 57 4F 52 44 5F 41 54 54 41 43 4B 5F 43 4F 4E 46 55 53 45 5F 44 55 52 41 54 49 4F 4E),
00001AC6             STR: 'AIKIDO_COUNTER_THROW_POWER_POINT_BOOST' (26 00 00 00 41 49 4B 49 44 4F 5F 43 4F 55 4E 54 45 52 5F 54 48 52 4F 57 5F 50 4F 57 45 52 5F 50 4F 49 4E 54 5F 42 4F 4F 53 54),
00001AF1             STR: 'AIKIDO_SWORD_ATTACK_SPEED_POINT_LOSS' (24 00 00 00 41 49 4B 49 44 4F 5F 53 57 4F 52 44 5F 41 54 54 41 43 4B 5F 53 50 45 45 44 5F 50 4F 49 4E 54 5F 4C 4F 53 53),
00001B1A             STR: 'AIKIDO_PERFECT_SELF_DEFENSE_POINT_BOOST' (27 00 00 00 41 49 4B 49 44 4F 5F 50 45 52 46 45 43 54 5F 53 45 4C 46 5F 44 45 46 45 4E 53 45 5F 50 4F 49 4E 54 5F 42 4F 4F 53 54),
00001B46             STR: 'AIKIDO_ARM_BAR_POWER_POINT_LOSS' (1F 00 00 00 41 49 4B 49 44 4F 5F 41 52 4D 5F 42 41 52 5F 50 4F 57 45 52 5F 50 4F 49 4E 54 5F 4C 4F 53 53),
00001B6A             STR: 'AIKIDO_IRON_GUARD_DEFENSE_SETTING_BOOST' (27 00 00 00 41 49 4B 49 44 4F 5F 49 52 4F 4E 5F 47 55 41 52 44 5F 44 45 46 45 4E 53 45 5F 53 45 54 54 49 4E 47 5F 42 4F 4F 53 54),
00001B96             STR: 'AIKIDO_BEND_LIKE_REED_POWER_POINT_LOSS' (26 00 00 00 41 49 4B 49 44 4F 5F 42 45 4E 44 5F 4C 49 4B 45 5F 52 45 45 44 5F 50 4F 57 45 52 5F 50 4F 49 4E 54 5F 4C 4F 53 53),
00001BC1             STR: 'AikidoAerialTakedown_DirectObject' (21 00 00 00 41 69 6B 69 64 6F 41 65 72 69 61 6C 54 61 6B 65 64 6F 77 6E 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001BE7             STR: 'AikidoCounterThrow_DirectObject' (1F 00 00 00 41 69 6B 69 64 6F 43 6F 75 6E 74 65 72 54 68 72 6F 77 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001C0B             STR: 'AikidoArmBar_DirectObject' (19 00 00 00 41 69 6B 69 64 6F 41 72 6D 42 61 72 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001C29             STR: 'AikidoIronGuard_Subject' (17 00 00 00 41 69 6B 69 64 6F 49 72 6F 6E 47 75 61 72 64 5F 53 75 62 6A 65 63 74),
00001C45             STR: 'AikidoTomoNage_DirectObject' (1B 00 00 00 41 69 6B 69 64 6F 54 6F 6D 6F 4E 61 67 65 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001C65             STR: 'AikidoMakiOnashi_DirectObject' (1D 00 00 00 41 69 6B 69 64 6F 4D 61 6B 69 4F 6E 61 73 68 69 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001C87             STR: 'AikidoPunchReversalCatchSlam_DirectObject' (29 00 00 00 41 69 6B 69 64 6F 50 75 6E 63 68 52 65 76 65 72 73 61 6C 43 61 74 63 68 53 6C 61 6D 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001CB5             STR: 'AikidoSpinningClayPigeon_DirectObject' (25 00 00 00 41 69 6B 69 64 6F 53 70 69 6E 6E 69 6E 67 43 6C 61 79 50 69 67 65 6F 6E 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001CDF             STR: 'AikidoSpinningClayPigeon_Deactivate' (23 00 00 00 41 69 6B 69 64 6F 53 70 69 6E 6E 69 6E 67 43 6C 61 79 50 69 67 65 6F 6E 5F 44 65 61 63 74 69 76 61 74 65),
00001D07             STR: 'AikidoSwordAttack_DirectObject' (1E 00 00 00 41 69 6B 69 64 6F 53 77 6F 72 64 41 74 74 61 63 6B 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                 )
             varnames:
00001D2A         TUPLE: (
00001D2F             STR: 'AIKIDO_SPINNING_PIGEON_DAMAGE' (1D 00 00 00 41 49 4B 49 44 4F 5F 53 50 49 4E 4E 49 4E 47 5F 50 49 47 45 4F 4E 5F 44 41 4D 41 47 45),
00001D51             STR: 'AikidoArmBar_DirectObject' (19 00 00 00 41 69 6B 69 64 6F 41 72 6D 42 61 72 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001D6F             STR: 'AIKIDO_PUNCH_REVERSAL_CATCH_SLAM_ENRAGE_TIME' (2C 00 00 00 41 49 4B 49 44 4F 5F 50 55 4E 43 48 5F 52 45 56 45 52 53 41 4C 5F 43 41 54 43 48 5F 53 4C 41 4D 5F 45 4E 52 41 47 45 5F 54 49 4D 45),
00001DA0             STR: 'AIKIDO_SWORD_ATTACK_CONFUSE_DURATION' (24 00 00 00 41 49 4B 49 44 4F 5F 53 57 4F 52 44 5F 41 54 54 41 43 4B 5F 43 4F 4E 46 55 53 45 5F 44 55 52 41 54 49 4F 4E),
00001DC9             STR: 'AIKIDO_COUNTER_THROW_POWER_POINT_BOOST' (26 00 00 00 41 49 4B 49 44 4F 5F 43 4F 55 4E 54 45 52 5F 54 48 52 4F 57 5F 50 4F 57 45 52 5F 50 4F 49 4E 54 5F 42 4F 4F 53 54),
00001DF4             STR: 'AikidoMakiOnashi_DirectObject' (1D 00 00 00 41 69 6B 69 64 6F 4D 61 6B 69 4F 6E 61 73 68 69 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001E16             STR: 'AikidoIronGuard_Subject' (17 00 00 00 41 69 6B 69 64 6F 49 72 6F 6E 47 75 61 72 64 5F 53 75 62 6A 65 63 74),
00001E32             STR: 'AikidoSwordAttack_DirectObject' (1E 00 00 00 41 69 6B 69 64 6F 53 77 6F 72 64 41 74 74 61 63 6B 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001E55             STR: 'AIKIDO_SPINNING_PIGEON_POWERLESS_TIME' (25 00 00 00 41 49 4B 49 44 4F 5F 53 50 49 4E 4E 49 4E 47 5F 50 49 47 45 4F 4E 5F 50 4F 57 45 52 4C 45 53 53 5F 54 49 4D 45),
00001E7F             STR: 'AikidoSpinningClayPigeon_Deactivate' (23 00 00 00 41 69 6B 69 64 6F 53 70 69 6E 6E 69 6E 67 43 6C 61 79 50 69 67 65 6F 6E 5F 44 65 61 63 74 69 76 61 74 65),
00001EA7             STR: 'AIKIDO_PERFECT_SELF_DEFENSE_POINT_BOOST' (27 00 00 00 41 49 4B 49 44 4F 5F 50 45 52 46 45 43 54 5F 53 45 4C 46 5F 44 45 46 45 4E 53 45 5F 50 4F 49 4E 54 5F 42 4F 4F 53 54),
00001ED3             STR: 'AIKIDO_TOMO_NAGE_DAMAGE' (17 00 00 00 41 49 4B 49 44 4F 5F 54 4F 4D 4F 5F 4E 41 47 45 5F 44 41 4D 41 47 45),
00001EEF             STR: 'AikidoSpinningClayPigeon_DirectObject' (25 00 00 00 41 69 6B 69 64 6F 53 70 69 6E 6E 69 6E 67 43 6C 61 79 50 69 67 65 6F 6E 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001F19             STR: 'AikidoAerialTakedown_DirectObject' (21 00 00 00 41 69 6B 69 64 6F 41 65 72 69 61 6C 54 61 6B 65 64 6F 77 6E 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001F3F             STR: 'AIKIDO_SWORD_ATTACK_DAMAGE' (1A 00 00 00 41 49 4B 49 44 4F 5F 53 57 4F 52 44 5F 41 54 54 41 43 4B 5F 44 41 4D 41 47 45),
00001F5E             STR: 'AIKIDO_ARM_BAR_DAMAGE' (15 00 00 00 41 49 4B 49 44 4F 5F 41 52 4D 5F 42 41 52 5F 44 41 4D 41 47 45),
00001F78             STR: 'AIKIDO_MAKI_ONASHI_DAMAGE' (19 00 00 00 41 49 4B 49 44 4F 5F 4D 41 4B 49 5F 4F 4E 41 53 48 49 5F 44 41 4D 41 47 45),
00001F96             STR: 'AikidoCounterThrow_DirectObject' (1F 00 00 00 41 69 6B 69 64 6F 43 6F 75 6E 74 65 72 54 68 72 6F 77 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001FBA             STR: 'AIKIDO_ARM_BAR_ENRAGE_DURATION' (1E 00 00 00 41 49 4B 49 44 4F 5F 41 52 4D 5F 42 41 52 5F 45 4E 52 41 47 45 5F 44 55 52 41 54 49 4F 4E),
00001FDD             STR: 'AikidoPunchReversalCatchSlam_DirectObject' (29 00 00 00 41 69 6B 69 64 6F 50 75 6E 63 68 52 65 76 65 72 73 61 6C 43 61 74 63 68 53 6C 61 6D 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
0000200B             STR: 'AIKIDO_BEND_LIKE_REED_POWER_POINT_LOSS' (26 00 00 00 41 49 4B 49 44 4F 5F 42 45 4E 44 5F 4C 49 4B 45 5F 52 45 45 44 5F 50 4F 57 45 52 5F 50 4F 49 4E 54 5F 4C 4F 53 53),
00002036             STR: 'AIKIDO_IRON_GUARD_DEFENSE_SETTING_BOOST' (27 00 00 00 41 49 4B 49 44 4F 5F 49 52 4F 4E 5F 47 55 41 52 44 5F 44 45 46 45 4E 53 45 5F 53 45 54 54 49 4E 47 5F 42 4F 4F 53 54),
00002062             STR: 'AIKIDO_BEND_LIKE_REED_DAMAGE' (1C 00 00 00 41 49 4B 49 44 4F 5F 42 45 4E 44 5F 4C 49 4B 45 5F 52 45 45 44 5F 44 41 4D 41 47 45),
00002083             STR: 'AIKIDO_IRON_GUARD_BLOCK_EFFECT_DURATION' (27 00 00 00 41 49 4B 49 44 4F 5F 49 52 4F 4E 5F 47 55 41 52 44 5F 42 4C 4F 43 4B 5F 45 46 46 45 43 54 5F 44 55 52 41 54 49 4F 4E),
000020AF             STR: 'AIKIDO_TOMO_NAGE_STUN_DURATION' (1E 00 00 00 41 49 4B 49 44 4F 5F 54 4F 4D 4F 5F 4E 41 47 45 5F 53 54 55 4E 5F 44 55 52 41 54 49 4F 4E),
000020D2             STR: 'obj' (03 00 00 00 6F 62 6A),
000020DA             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
000020E8             STR: 'AikidoTomoNage_DirectObject' (1B 00 00 00 41 69 6B 69 64 6F 54 6F 6D 6F 4E 61 67 65 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00002108             STR: 'AIKIDO_ARM_BAR_POWER_POINT_LOSS' (1F 00 00 00 41 49 4B 49 44 4F 5F 41 52 4D 5F 42 41 52 5F 50 4F 57 45 52 5F 50 4F 49 4E 54 5F 4C 4F 53 53),
0000212C             STR: 'AIKIDO_AERIAL_TAKEDOWN_DAMAGE' (1D 00 00 00 41 49 4B 49 44 4F 5F 41 45 52 49 41 4C 5F 54 41 4B 45 44 4F 57 4E 5F 44 41 4D 41 47 45),
0000214E             STR: 'AIKIDO_COUNTER_THROW_CONFUSE_DURATION' (25 00 00 00 41 49 4B 49 44 4F 5F 43 4F 55 4E 54 45 52 5F 54 48 52 4F 57 5F 43 4F 4E 46 55 53 45 5F 44 55 52 41 54 49 4F 4E),
00002178             STR: 'AIKIDO_SWORD_ATTACK_SPEED_POINT_LOSS' (24 00 00 00 41 49 4B 49 44 4F 5F 53 57 4F 52 44 5F 41 54 54 41 43 4B 5F 53 50 45 45 44 5F 50 4F 49 4E 54 5F 4C 4F 53 53),
000021A1             STR: 'AIKIDO_IRON_GUARD_BLOCK_BOOST' (1D 00 00 00 41 49 4B 49 44 4F 5F 49 52 4F 4E 5F 47 55 41 52 44 5F 42 4C 4F 43 4B 5F 42 4F 4F 53 54),
000021C3             STR: 'AIKIDO_COUNTER_THROW_DAMAGE' (1B 00 00 00 41 49 4B 49 44 4F 5F 43 4F 55 4E 54 45 52 5F 54 48 52 4F 57 5F 44 41 4D 41 47 45),
000021E3             STR: 'AIKIDO_PUNCH_REVERSAL_CATCH_SLAM_DAMAGE' (27 00 00 00 41 49 4B 49 44 4F 5F 50 55 4E 43 48 5F 52 45 56 45 52 53 41 4C 5F 43 41 54 43 48 5F 53 4C 41 4D 5F 44 41 4D 41 47 45),
0000220F             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79)
                 )
             freevars:
0000221B         TUPLE: ()
             cellvars:
00002220         TUPLE: ()
             filename:
00002225         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_aikido.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 61 69 6B 69 64 6F 2E 70 79)
             name:
0000227F         STR: '?' (01 00 00 00 3F)
             firslineno:
00002285         LONG: 1L (01 00 00 00)
             lnotab:
00002289         STR: '\t\x01\t\x01\x0c\x03\x07\x06\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x05\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x05\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x07\t\x0b\t\x0e\t\x0b\t\x11\t\x0c\t\x08\t\x0e\t\x0b\t\x08' (48 00 00 00 09 01 09 01 0C 03 07 06 06 01 06 01 06 01 06 01 06 01 06 01 06 01 06 01 06 05 06 01 06 01 06 01 06 01 06 01 06 01 06 01 06 05 06 01 06 01 06 01 06 01 06 01 06 07 09 0B 09 0E 09 0B 09 11 09 0C 09 08 09 0E 09 0B 09 08)

