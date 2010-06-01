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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00i\x03\x00Z\x04\x00d\x01\x00Z\x05\x00d\x02\x00Z\x06\x00d\x03\x00Z\x07\x00d\x04\x00Z\x08\x00d\x05\x00Z\t\x00d\x06\x00Z\n\x00d\x07\x00Z\x0b\x00d\x08\x00Z\x0c\x00d\x01\x00Z\r\x00d\t\x00Z\x0e\x00d\t\x00Z\x0f\x00d\t\x00Z\x10\x00d\n\x00Z\x11\x00d\x0b\x00Z\x12\x00d\x0c\x00Z\x13\x00d\r\x00Z\x14\x00d\x0e\x00\x84\x00\x00Z\x15\x00d\x0f\x00\x84\x00\x00Z\x16\x00d\x10\x00\x84\x00\x00Z\x17\x00d\x11\x00\x84\x00\x00Z\x18\x00d\x12\x00\x84\x00\x00Z\x19\x00d\x13\x00\x84\x00\x00Z\x1a\x00d\x14\x00\x84\x00\x00Z\x1b\x00d\x15\x00\x84\x00\x00Z\x1c\x00d\x00\x00S' (CA 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 69 03 00 5A 04 00 64 01 00 5A 05 00 64 02 00 5A 06 00 64 03 00 5A 07 00 64 04 00 5A 08 00 64 05 00 5A 09 00 64 06 00 5A 0A 00 64 07 00 5A 0B 00 64 08 00 5A 0C 00 64 01 00 5A 0D 00 64 09 00 5A 0E 00 64 09 00 5A 0F 00 64 09 00 5A 10 00 64 0A 00 5A 11 00 64 0B 00 5A 12 00 64 0C 00 5A 13 00 64 0D 00 5A 14 00 64 0E 00 84 00 00 5A 15 00 64 0F 00 84 00 00 5A 16 00 64 10 00 84 00 00 5A 17 00 64 11 00 84 00 00 5A 18 00 64 12 00 84 00 00 5A 19 00 64 13 00 84 00 00 5A 1A 00 64 14 00 84 00 00 5A 1B 00 64 15 00 84 00 00 5A 1C 00 64 00 00 53)
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
                 0000001E     64 - LOAD_CONST          50
                 00000021     5A - STORE_NAME          'RIFLE_BODY_SHOT_DAMAGE'
                 00000024     64 - LOAD_CONST          300
                 00000027     5A - STORE_NAME          'RIFLE_CRIPPLING_SHOT_DAMAGE'
                 0000002A     64 - LOAD_CONST          325
                 0000002D     5A - STORE_NAME          'RIFLE_DEADLY_SHOT_DAMAGE'
                 00000030     64 - LOAD_CONST          90
                 00000033     5A - STORE_NAME          'RIFLE_DISABLING_SHOT_DAMAGE'
                 00000036     64 - LOAD_CONST          75
                 00000039     5A - STORE_NAME          'RIFLE_IMMOBILIZING_SHOT_DAMAGE'
                 0000003C     64 - LOAD_CONST          215
                 0000003F     5A - STORE_NAME          'RIFLE_RIFLE_BUTT_DAMAGE'
                 00000042     64 - LOAD_CONST          100
                 00000045     5A - STORE_NAME          'RIFLE_THREE_ROUND_BURST_DAMAGE'
                 00000048     64 - LOAD_CONST          250
                 0000004B     5A - STORE_NAME          'RIFLE_WOUNDING_SHOT_DAMAGE'
                 0000004E     64 - LOAD_CONST          50
                 00000051     5A - STORE_NAME          'RIFLE_WOUNDING_SHOT_WOUND_DAMAGE_PER_5_SECONDS'
                 00000054     64 - LOAD_CONST          15
                 00000057     5A - STORE_NAME          'RIFLE_IMMOBILIZING_SHOT_STUN_DURATION'
                 0000005A     64 - LOAD_CONST          15
                 0000005D     5A - STORE_NAME          'RIFLE_DISABLING_SHOT_ABILITY_MOD_DURATION'
                 00000060     64 - LOAD_CONST          15
                 00000063     5A - STORE_NAME          'RIFLE_WOUNDING_SHOT_WOUND_WOUNDING_EFFECT_DURATION'
                 00000066     64 - LOAD_CONST          10
                 00000069     5A - STORE_NAME          'RIFLE_RIFLE_BUTT_CONFUSE_EFFECT_DURATION'
                 0000006C     64 - LOAD_CONST          20
                 0000006F     5A - STORE_NAME          'RIFLE_CRIPPLING_SHOT_ABILITY_MOD_DURATION'
                 00000072     64 - LOAD_CONST          -25
                 00000075     5A - STORE_NAME          'RIFLE_DISABLING_SHOT_ABILITY_MOD'
                 00000078     64 - LOAD_CONST          -50
                 0000007B     5A - STORE_NAME          'RIFLE_CRIPPLING_SHOT_ABILITY_MOD'
                 0000007E     64 - LOAD_CONST          CODE('RifleBodyShot_DirectObject')
                 00000081     84 - MAKE_FUNCTION       r0000
                 00000084     5A - STORE_NAME          'RifleBodyShot_DirectObject'
                 00000087     64 - LOAD_CONST          CODE('RifleCripplingShot_DirectObject')
                 0000008A     84 - MAKE_FUNCTION       r0000
                 0000008D     5A - STORE_NAME          'RifleCripplingShot_DirectObject'
                 00000090     64 - LOAD_CONST          CODE('RifleDeadlyShot_DirectObject')
                 00000093     84 - MAKE_FUNCTION       r0000
                 00000096     5A - STORE_NAME          'RifleDeadlyShot_DirectObject'
                 00000099     64 - LOAD_CONST          CODE('RifleDisablingShot_DirectObject')
                 0000009C     84 - MAKE_FUNCTION       r0000
                 0000009F     5A - STORE_NAME          'RifleDisablingShot_DirectObject'
                 000000A2     64 - LOAD_CONST          CODE('RifleImmobilizingShot_DirectObject')
                 000000A5     84 - MAKE_FUNCTION       r0000
                 000000A8     5A - STORE_NAME          'RifleImmobilizingShot_DirectObject'
                 000000AB     64 - LOAD_CONST          CODE('RifleRifleButt_DirectObject')
                 000000AE     84 - MAKE_FUNCTION       r0000
                 000000B1     5A - STORE_NAME          'RifleRifleButt_DirectObject'
                 000000B4     64 - LOAD_CONST          CODE('RifleThreeRoundBurst_DirectObject')
                 000000B7     84 - MAKE_FUNCTION       r0000
                 000000BA     5A - STORE_NAME          'RifleThreeRoundBurst_DirectObject'
                 000000BD     64 - LOAD_CONST          CODE('RifleWoundingShot_DirectObject')
                 000000C0     84 - MAKE_FUNCTION       r0000
                 000000C3     5A - STORE_NAME          'RifleWoundingShot_DirectObject'
                 000000C6     64 - LOAD_CONST          None
                 000000C9     53 - RETURN_VALUE        
             consts:
000000E8         TUPLE: (
000000ED             None (4E),
000000EE             INT: 50 (32 00 00 00),
000000F3             INT: 300 (2C 01 00 00),
000000F8             INT: 325 (45 01 00 00),
000000FD             INT: 90 (5A 00 00 00),
00000102             INT: 75 (4B 00 00 00),
00000107             INT: 215 (D7 00 00 00),
0000010C             INT: 100 (64 00 00 00),
00000111             INT: 250 (FA 00 00 00),
00000116             INT: 15 (0F 00 00 00),
0000011B             INT: 10 (0A 00 00 00),
00000120             INT: 20 (14 00 00 00),
00000125             INT: -25 (E7 FF FF FF),
0000012A             INT: -50 (CE FF FF FF),
0000012F             CODE:
                         argcount:
00000130                     LONG: 2L (02 00 00 00)
                         nlocals:
00000134                     LONG: 3L (03 00 00 00)
                         stacksize:
00000138                     LONG: 6L (06 00 00 00)
                         flags:
0000013C                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000140                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'RifleBodyShot: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'RIFLE_BODY_SHOT_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'RIFLE_BODY_SHOT_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'RifleBodyShotAbility'
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
00000191                     TUPLE: (
00000196                         None (4E),
00000197                         STR: 'RifleBodyShot: %d damage dealt' (1E 00 00 00 52 69 66 6C 65 42 6F 64 79 53 68 6F 74 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
000001BA                     TUPLE: (
000001BF                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000001CB                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
000001E2                         STR: 'RIFLE_BODY_SHOT_DAMAGE' (16 00 00 00 52 49 46 4C 45 5F 42 4F 44 59 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
000001FD                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000209                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00000217                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00000235                         STR: 'msg' (03 00 00 00 6D 73 67),
0000023D                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00000250                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
0000025B                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00000279                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00000285                         STR: 'RifleBodyShotAbility' (14 00 00 00 52 69 66 6C 65 42 6F 64 79 53 68 6F 74 41 62 69 6C 69 74 79),
0000029E                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
000002B6                     TUPLE: (
000002BB                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000002C7                         STR: 'msg' (03 00 00 00 6D 73 67),
000002CF                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
000002DA                     TUPLE: ()
                         cellvars:
000002DF                     TUPLE: ()
                         filename:
000002E4                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_rifle.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 72 69 66 6C 65 2E 70 79)
                         name:
0000033D                     STR: 'RifleBodyShot_DirectObject' (1A 00 00 00 52 69 66 6C 65 42 6F 64 79 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
0000035C                     LONG: 38L (26 00 00 00)
                         lnotab:
00000360                     STR: '\x00\x01\x11\x01\x18\x01' (06 00 00 00 00 01 11 01 18 01),
0000036B             CODE:
                         argcount:
0000036C                     LONG: 2L (02 00 00 00)
                         nlocals:
00000370                     LONG: 3L (03 00 00 00)
                         stacksize:
00000374                     LONG: 6L (06 00 00 00)
                         flags:
00000378                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000037C                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00t\x03\x00f\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x05\x00i\x06\x00t\x07\x00t\x02\x00t\x08\x00d\x02\x00\x83\x04\x00\x01|\x00\x00i\t\x00i\n\x00|\x01\x00i\x0c\x00t\x03\x00\x83\x02\x00}\x02\x00t\x00\x00i\x0e\x00t\x0f\x00t\x07\x00|\x01\x00i\x0c\x00|\x01\x00i\x10\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (6B 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 74 03 00 66 02 00 16 83 01 00 01 7C 00 00 69 05 00 69 06 00 74 07 00 74 02 00 74 08 00 64 02 00 83 04 00 01 7C 00 00 69 09 00 69 0A 00 7C 01 00 69 0C 00 74 03 00 83 02 00 7D 02 00 74 00 00 69 0E 00 74 0F 00 74 07 00 7C 01 00 69 0C 00 7C 01 00 69 10 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'RifleCripplingShot: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'RIFLE_CRIPPLING_SHOT_ABILITY_MOD'
                             0000000C     74 - LOAD_GLOBAL         'RIFLE_CRIPPLING_SHOT_DAMAGE'
                             0000000F     66 - BUILD_TUPLE         r0002
                             00000012     16 - BINARY_MODULO       
                             00000013     83 - CALL_FUNCTION       r0001
                             00000016     01 - POP_TOP             
                             00000017     7C - LOAD_FAST           'subject'
                             0000001A     69 - LOAD_ATTR           'AbilityInv'
                             0000001D     69 - LOAD_ATTR           'addTempModToAllActive'
                             00000020     74 - LOAD_GLOBAL         'RifleCripplingShotAbility'
                             00000023     74 - LOAD_GLOBAL         'RIFLE_CRIPPLING_SHOT_ABILITY_MOD'
                             00000026     74 - LOAD_GLOBAL         'RIFLE_CRIPPLING_SHOT_ABILITY_MOD_DURATION'
                             00000029     64 - LOAD_CONST          0
                             0000002C     83 - CALL_FUNCTION       r0004
                             0000002F     01 - POP_TOP             
                             00000030     7C - LOAD_FAST           'subject'
                             00000033     69 - LOAD_ATTR           'Interlock'
                             00000036     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             00000039     7C - LOAD_FAST           'msg'
                             0000003C     69 - LOAD_ATTR           'subjectLocator'
                             0000003F     74 - LOAD_GLOBAL         'RIFLE_CRIPPLING_SHOT_DAMAGE'
                             00000042     83 - CALL_FUNCTION       r0002
                             00000045     7D - STORE_FAST          'damage'
                             00000048     74 - LOAD_GLOBAL         'Utility'
                             0000004B     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000004E     74 - LOAD_GLOBAL         'SUCCESS'
                             00000051     74 - LOAD_GLOBAL         'RifleCripplingShotAbility'
                             00000054     7C - LOAD_FAST           'msg'
                             00000057     69 - LOAD_ATTR           'subjectLocator'
                             0000005A     7C - LOAD_FAST           'msg'
                             0000005D     69 - LOAD_ATTR           'directObjectLocator'
                             00000060     7C - LOAD_FAST           'damage'
                             00000063     83 - CALL_FUNCTION       r0005
                             00000066     01 - POP_TOP             
                             00000067     64 - LOAD_CONST          None
                             0000006A     53 - RETURN_VALUE        
                         consts:
000003EC                     TUPLE: (
000003F1                         None (4E),
000003F2                         STR: 'RifleCripplingShot: %d damage dealt' (23 00 00 00 52 69 66 6C 65 43 72 69 70 70 6C 69 6E 67 53 68 6F 74 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74),
0000041A                         INT: 0 (00 00 00 00)
                             )
                         names:
0000041F                     TUPLE: (
00000424                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000430                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000447                         STR: 'RIFLE_CRIPPLING_SHOT_ABILITY_MOD' (20 00 00 00 52 49 46 4C 45 5F 43 52 49 50 50 4C 49 4E 47 5F 53 48 4F 54 5F 41 42 49 4C 49 54 59 5F 4D 4F 44),
0000046C                         STR: 'RIFLE_CRIPPLING_SHOT_DAMAGE' (1B 00 00 00 52 49 46 4C 45 5F 43 52 49 50 50 4C 49 4E 47 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
0000048C                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000498                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
000004A7                         STR: 'addTempModToAllActive' (15 00 00 00 61 64 64 54 65 6D 70 4D 6F 64 54 6F 41 6C 6C 41 63 74 69 76 65),
000004C1                         STR: 'RifleCripplingShotAbility' (19 00 00 00 52 69 66 6C 65 43 72 69 70 70 6C 69 6E 67 53 68 6F 74 41 62 69 6C 69 74 79),
000004DF                         STR: 'RIFLE_CRIPPLING_SHOT_ABILITY_MOD_DURATION' (29 00 00 00 52 49 46 4C 45 5F 43 52 49 50 50 4C 49 4E 47 5F 53 48 4F 54 5F 41 42 49 4C 49 54 59 5F 4D 4F 44 5F 44 55 52 41 54 49 4F 4E),
0000050D                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
0000051B                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00000539                         STR: 'msg' (03 00 00 00 6D 73 67),
00000541                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00000554                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
0000055F                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
0000057D                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00000589                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
000005A1                     TUPLE: (
000005A6                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000005B2                         STR: 'msg' (03 00 00 00 6D 73 67),
000005BA                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
000005C5                     TUPLE: ()
                         cellvars:
000005CA                     TUPLE: ()
                         filename:
000005CF                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_rifle.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 72 69 66 6C 65 2E 70 79)
                         name:
00000628                     STR: 'RifleCripplingShot_DirectObject' (1F 00 00 00 52 69 66 6C 65 43 72 69 70 70 6C 69 6E 67 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
0000064C                     LONG: 46L (2E 00 00 00)
                         lnotab:
00000650                     STR: '\x00\x01\x17\x03\x19\x01\x18\x01' (08 00 00 00 00 01 17 03 19 01 18 01),
0000065D             CODE:
                         argcount:
0000065E                     LONG: 2L (02 00 00 00)
                         nlocals:
00000662                     LONG: 3L (03 00 00 00)
                         stacksize:
00000666                     LONG: 6L (06 00 00 00)
                         flags:
0000066A                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000066E                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'RifleDeadlyShot: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'RIFLE_DEADLY_SHOT_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'RIFLE_DEADLY_SHOT_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'RifleDeadlyShotAbility'
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
000006BF                     TUPLE: (
000006C4                         None (4E),
000006C5                         STR: 'RifleDeadlyShot: %d damage dealt' (20 00 00 00 52 69 66 6C 65 44 65 61 64 6C 79 53 68 6F 74 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
000006EA                     TUPLE: (
000006EF                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000006FB                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000712                         STR: 'RIFLE_DEADLY_SHOT_DAMAGE' (18 00 00 00 52 49 46 4C 45 5F 44 45 41 44 4C 59 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
0000072F                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000073B                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00000749                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00000767                         STR: 'msg' (03 00 00 00 6D 73 67),
0000076F                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00000782                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
0000078D                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
000007AB                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
000007B7                         STR: 'RifleDeadlyShotAbility' (16 00 00 00 52 69 66 6C 65 44 65 61 64 6C 79 53 68 6F 74 41 62 69 6C 69 74 79),
000007D2                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
000007EA                     TUPLE: (
000007EF                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000007FB                         STR: 'msg' (03 00 00 00 6D 73 67),
00000803                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
0000080E                     TUPLE: ()
                         cellvars:
00000813                     TUPLE: ()
                         filename:
00000818                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_rifle.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 72 69 66 6C 65 2E 70 79)
                         name:
00000871                     STR: 'RifleDeadlyShot_DirectObject' (1C 00 00 00 52 69 66 6C 65 44 65 61 64 6C 79 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000892                     LONG: 58L (3A 00 00 00)
                         lnotab:
00000896                     STR: '\x00\x01\x11\x01\x18\x01' (06 00 00 00 00 01 11 01 18 01),
000008A1             CODE:
                         argcount:
000008A2                     LONG: 2L (02 00 00 00)
                         nlocals:
000008A6                     LONG: 3L (03 00 00 00)
                         stacksize:
000008AA                     LONG: 6L (06 00 00 00)
                         flags:
000008AE                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000008B2                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00t\x03\x00f\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x05\x00i\x06\x00t\x07\x00t\x02\x00t\x08\x00d\x02\x00\x83\x04\x00\x01|\x00\x00i\t\x00i\n\x00|\x01\x00i\x0c\x00t\x03\x00\x83\x02\x00}\x02\x00t\x00\x00i\x0e\x00t\x0f\x00t\x07\x00|\x01\x00i\x0c\x00|\x01\x00i\x10\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (6B 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 74 03 00 66 02 00 16 83 01 00 01 7C 00 00 69 05 00 69 06 00 74 07 00 74 02 00 74 08 00 64 02 00 83 04 00 01 7C 00 00 69 09 00 69 0A 00 7C 01 00 69 0C 00 74 03 00 83 02 00 7D 02 00 74 00 00 69 0E 00 74 0F 00 74 07 00 7C 01 00 69 0C 00 7C 01 00 69 10 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'RifleDisablingShot: %d to all abilities and %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'RIFLE_DISABLING_SHOT_ABILITY_MOD'
                             0000000C     74 - LOAD_GLOBAL         'RIFLE_DISABLING_SHOT_DAMAGE'
                             0000000F     66 - BUILD_TUPLE         r0002
                             00000012     16 - BINARY_MODULO       
                             00000013     83 - CALL_FUNCTION       r0001
                             00000016     01 - POP_TOP             
                             00000017     7C - LOAD_FAST           'subject'
                             0000001A     69 - LOAD_ATTR           'AbilityInv'
                             0000001D     69 - LOAD_ATTR           'addTempModToAllActive'
                             00000020     74 - LOAD_GLOBAL         'RifleDisablingShotAbility'
                             00000023     74 - LOAD_GLOBAL         'RIFLE_DISABLING_SHOT_ABILITY_MOD'
                             00000026     74 - LOAD_GLOBAL         'RIFLE_DISABLING_SHOT_ABILITY_MOD_DURATION'
                             00000029     64 - LOAD_CONST          0
                             0000002C     83 - CALL_FUNCTION       r0004
                             0000002F     01 - POP_TOP             
                             00000030     7C - LOAD_FAST           'subject'
                             00000033     69 - LOAD_ATTR           'Interlock'
                             00000036     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             00000039     7C - LOAD_FAST           'msg'
                             0000003C     69 - LOAD_ATTR           'subjectLocator'
                             0000003F     74 - LOAD_GLOBAL         'RIFLE_DISABLING_SHOT_DAMAGE'
                             00000042     83 - CALL_FUNCTION       r0002
                             00000045     7D - STORE_FAST          'damage'
                             00000048     74 - LOAD_GLOBAL         'Utility'
                             0000004B     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000004E     74 - LOAD_GLOBAL         'SUCCESS'
                             00000051     74 - LOAD_GLOBAL         'RifleDisablingShotAbility'
                             00000054     7C - LOAD_FAST           'msg'
                             00000057     69 - LOAD_ATTR           'subjectLocator'
                             0000005A     7C - LOAD_FAST           'msg'
                             0000005D     69 - LOAD_ATTR           'directObjectLocator'
                             00000060     7C - LOAD_FAST           'damage'
                             00000063     83 - CALL_FUNCTION       r0005
                             00000066     01 - POP_TOP             
                             00000067     64 - LOAD_CONST          None
                             0000006A     53 - RETURN_VALUE        
                         consts:
00000922                     TUPLE: (
00000927                         None (4E),
00000928                         STR: 'RifleDisablingShot: %d to all abilities and %d damage dealt' (3B 00 00 00 52 69 66 6C 65 44 69 73 61 62 6C 69 6E 67 53 68 6F 74 3A 20 25 64 20 74 6F 20 61 6C 6C 20 61 62 69 6C 69 74 69 65 73 20 61 6E 64 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74),
00000968                         INT: 0 (00 00 00 00)
                             )
                         names:
0000096D                     TUPLE: (
00000972                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
0000097E                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000995                         STR: 'RIFLE_DISABLING_SHOT_ABILITY_MOD' (20 00 00 00 52 49 46 4C 45 5F 44 49 53 41 42 4C 49 4E 47 5F 53 48 4F 54 5F 41 42 49 4C 49 54 59 5F 4D 4F 44),
000009BA                         STR: 'RIFLE_DISABLING_SHOT_DAMAGE' (1B 00 00 00 52 49 46 4C 45 5F 44 49 53 41 42 4C 49 4E 47 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
000009DA                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000009E6                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
000009F5                         STR: 'addTempModToAllActive' (15 00 00 00 61 64 64 54 65 6D 70 4D 6F 64 54 6F 41 6C 6C 41 63 74 69 76 65),
00000A0F                         STR: 'RifleDisablingShotAbility' (19 00 00 00 52 69 66 6C 65 44 69 73 61 62 6C 69 6E 67 53 68 6F 74 41 62 69 6C 69 74 79),
00000A2D                         STR: 'RIFLE_DISABLING_SHOT_ABILITY_MOD_DURATION' (29 00 00 00 52 49 46 4C 45 5F 44 49 53 41 42 4C 49 4E 47 5F 53 48 4F 54 5F 41 42 49 4C 49 54 59 5F 4D 4F 44 5F 44 55 52 41 54 49 4F 4E),
00000A5B                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00000A69                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00000A87                         STR: 'msg' (03 00 00 00 6D 73 67),
00000A8F                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00000AA2                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
00000AAD                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00000ACB                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00000AD7                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00000AEF                     TUPLE: (
00000AF4                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000B00                         STR: 'msg' (03 00 00 00 6D 73 67),
00000B08                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00000B13                     TUPLE: ()
                         cellvars:
00000B18                     TUPLE: ()
                         filename:
00000B1D                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_rifle.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 72 69 66 6C 65 2E 70 79)
                         name:
00000B76                     STR: 'RifleDisablingShot_DirectObject' (1F 00 00 00 52 69 66 6C 65 44 69 73 61 62 6C 69 6E 67 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000B9A                     LONG: 67L (43 00 00 00)
                         lnotab:
00000B9E                     STR: '\x00\x01\x17\x03\x19\x01\x18\x01' (08 00 00 00 00 01 17 03 19 01 18 01),
00000BAB             CODE:
                         argcount:
00000BAC                     LONG: 2L (02 00 00 00)
                         nlocals:
00000BB0                     LONG: 3L (03 00 00 00)
                         stacksize:
00000BB4                     LONG: 6L (06 00 00 00)
                         flags:
00000BB8                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000BBC                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00t\x03\x00f\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x05\x00i\x06\x00|\x01\x00i\x08\x00t\t\x00\x83\x02\x00}\x02\x00t\x00\x00i\x0b\x00t\x0c\x00t\r\x00|\x01\x00i\x08\x00|\x01\x00i\x0e\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (52 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 74 03 00 66 02 00 16 83 01 00 01 7C 00 00 69 05 00 69 06 00 7C 01 00 69 08 00 74 09 00 83 02 00 7D 02 00 74 00 00 69 0B 00 74 0C 00 74 0D 00 7C 01 00 69 08 00 7C 01 00 69 0E 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'RifleImmobilizingShot: stunned for %d seconds and %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'RIFLE_IMMOBILIZING_SHOT_STUN_DURATION'
                             0000000C     74 - LOAD_GLOBAL         'RIFLE_DEADLY_SHOT_DAMAGE'
                             0000000F     66 - BUILD_TUPLE         r0002
                             00000012     16 - BINARY_MODULO       
                             00000013     83 - CALL_FUNCTION       r0001
                             00000016     01 - POP_TOP             
                             00000017     7C - LOAD_FAST           'subject'
                             0000001A     69 - LOAD_ATTR           'Interlock'
                             0000001D     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             00000020     7C - LOAD_FAST           'msg'
                             00000023     69 - LOAD_ATTR           'subjectLocator'
                             00000026     74 - LOAD_GLOBAL         'RIFLE_IMMOBILIZING_SHOT_DAMAGE'
                             00000029     83 - CALL_FUNCTION       r0002
                             0000002C     7D - STORE_FAST          'damage'
                             0000002F     74 - LOAD_GLOBAL         'Utility'
                             00000032     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             00000035     74 - LOAD_GLOBAL         'SUCCESS'
                             00000038     74 - LOAD_GLOBAL         'RifleImmobilizingShotAbility'
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
00000C13                     TUPLE: (
00000C18                         None (4E),
00000C19                         STR: 'RifleImmobilizingShot: stunned for %d seconds and %d damage dealt' (41 00 00 00 52 69 66 6C 65 49 6D 6D 6F 62 69 6C 69 7A 69 6E 67 53 68 6F 74 3A 20 73 74 75 6E 6E 65 64 20 66 6F 72 20 25 64 20 73 65 63 6F 6E 64 73 20 61 6E 64 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
00000C5F                     TUPLE: (
00000C64                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000C70                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000C87                         STR: 'RIFLE_IMMOBILIZING_SHOT_STUN_DURATION' (25 00 00 00 52 49 46 4C 45 5F 49 4D 4D 4F 42 49 4C 49 5A 49 4E 47 5F 53 48 4F 54 5F 53 54 55 4E 5F 44 55 52 41 54 49 4F 4E),
00000CB1                         STR: 'RIFLE_DEADLY_SHOT_DAMAGE' (18 00 00 00 52 49 46 4C 45 5F 44 45 41 44 4C 59 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
00000CCE                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000CDA                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00000CE8                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00000D06                         STR: 'msg' (03 00 00 00 6D 73 67),
00000D0E                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00000D21                         STR: 'RIFLE_IMMOBILIZING_SHOT_DAMAGE' (1E 00 00 00 52 49 46 4C 45 5F 49 4D 4D 4F 42 49 4C 49 5A 49 4E 47 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
00000D44                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
00000D4F                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00000D6D                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00000D79                         STR: 'RifleImmobilizingShotAbility' (1C 00 00 00 52 69 66 6C 65 49 6D 6D 6F 62 69 6C 69 7A 69 6E 67 53 68 6F 74 41 62 69 6C 69 74 79),
00000D9A                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00000DB2                     TUPLE: (
00000DB7                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000DC3                         STR: 'msg' (03 00 00 00 6D 73 67),
00000DCB                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00000DD6                     TUPLE: ()
                         cellvars:
00000DDB                     TUPLE: ()
                         filename:
00000DE0                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_rifle.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 72 69 66 6C 65 2E 70 79)
                         name:
00000E39                     STR: 'RifleImmobilizingShot_DirectObject' (22 00 00 00 52 69 66 6C 65 49 6D 6D 6F 62 69 6C 69 7A 69 6E 67 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000E60                     LONG: 78L (4E 00 00 00)
                         lnotab:
00000E64                     STR: '\x00\x01\x17\x04\x18\x01' (06 00 00 00 00 01 17 04 18 01),
00000E6F             CODE:
                         argcount:
00000E70                     LONG: 2L (02 00 00 00)
                         nlocals:
00000E74                     LONG: 3L (03 00 00 00)
                         stacksize:
00000E78                     LONG: 6L (06 00 00 00)
                         flags:
00000E7C                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000E80                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00t\x03\x00f\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x05\x00i\x06\x00|\x01\x00i\x08\x00t\x03\x00\x83\x02\x00}\x02\x00t\x00\x00i\n\x00t\x0b\x00t\x0c\x00|\x01\x00i\x08\x00|\x01\x00i\r\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (52 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 74 03 00 66 02 00 16 83 01 00 01 7C 00 00 69 05 00 69 06 00 7C 01 00 69 08 00 74 03 00 83 02 00 7D 02 00 74 00 00 69 0A 00 74 0B 00 74 0C 00 7C 01 00 69 08 00 7C 01 00 69 0D 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'RifleRifleButt: confused for %d seconds and %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'RIFLE_RIFLE_BUTT_CONFUSE_EFFECT_DURATION'
                             0000000C     74 - LOAD_GLOBAL         'RIFLE_RIFLE_BUTT_DAMAGE'
                             0000000F     66 - BUILD_TUPLE         r0002
                             00000012     16 - BINARY_MODULO       
                             00000013     83 - CALL_FUNCTION       r0001
                             00000016     01 - POP_TOP             
                             00000017     7C - LOAD_FAST           'subject'
                             0000001A     69 - LOAD_ATTR           'Interlock'
                             0000001D     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             00000020     7C - LOAD_FAST           'msg'
                             00000023     69 - LOAD_ATTR           'subjectLocator'
                             00000026     74 - LOAD_GLOBAL         'RIFLE_RIFLE_BUTT_DAMAGE'
                             00000029     83 - CALL_FUNCTION       r0002
                             0000002C     7D - STORE_FAST          'damage'
                             0000002F     74 - LOAD_GLOBAL         'Utility'
                             00000032     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             00000035     74 - LOAD_GLOBAL         'SUCCESS'
                             00000038     74 - LOAD_GLOBAL         'RifleRifleButtAbility'
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
00000ED7                     TUPLE: (
00000EDC                         None (4E),
00000EDD                         STR: 'RifleRifleButt: confused for %d seconds and %d damage dealt' (3B 00 00 00 52 69 66 6C 65 52 69 66 6C 65 42 75 74 74 3A 20 63 6F 6E 66 75 73 65 64 20 66 6F 72 20 25 64 20 73 65 63 6F 6E 64 73 20 61 6E 64 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
00000F1D                     TUPLE: (
00000F22                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000F2E                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000F45                         STR: 'RIFLE_RIFLE_BUTT_CONFUSE_EFFECT_DURATION' (28 00 00 00 52 49 46 4C 45 5F 52 49 46 4C 45 5F 42 55 54 54 5F 43 4F 4E 46 55 53 45 5F 45 46 46 45 43 54 5F 44 55 52 41 54 49 4F 4E),
00000F72                         STR: 'RIFLE_RIFLE_BUTT_DAMAGE' (17 00 00 00 52 49 46 4C 45 5F 52 49 46 4C 45 5F 42 55 54 54 5F 44 41 4D 41 47 45),
00000F8E                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000F9A                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00000FA8                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00000FC6                         STR: 'msg' (03 00 00 00 6D 73 67),
00000FCE                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00000FE1                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
00000FEC                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
0000100A                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00001016                         STR: 'RifleRifleButtAbility' (15 00 00 00 52 69 66 6C 65 52 69 66 6C 65 42 75 74 74 41 62 69 6C 69 74 79),
00001030                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00001048                     TUPLE: (
0000104D                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00001059                         STR: 'msg' (03 00 00 00 6D 73 67),
00001061                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
0000106C                     TUPLE: ()
                         cellvars:
00001071                     TUPLE: ()
                         filename:
00001076                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_rifle.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 72 69 66 6C 65 2E 70 79)
                         name:
000010CF                     STR: 'RifleRifleButt_DirectObject' (1B 00 00 00 52 69 66 6C 65 52 69 66 6C 65 42 75 74 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
000010EF                     LONG: 92L (5C 00 00 00)
                         lnotab:
000010F3                     STR: '\x00\x01\x17\x01\x18\x02' (06 00 00 00 00 01 17 01 18 02),
000010FE             CODE:
                         argcount:
000010FF                     LONG: 2L (02 00 00 00)
                         nlocals:
00001103                     LONG: 3L (03 00 00 00)
                         stacksize:
00001107                     LONG: 6L (06 00 00 00)
                         flags:
0000110B                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000110F                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'RifleThreeRoundBurst: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'RIFLE_THREE_ROUND_BURST_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'RIFLE_THREE_ROUND_BURST_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'RifleThreeRoundBurstAbility'
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
00001160                     TUPLE: (
00001165                         None (4E),
00001166                         STR: 'RifleThreeRoundBurst: %d damage dealt' (25 00 00 00 52 69 66 6C 65 54 68 72 65 65 52 6F 75 6E 64 42 75 72 73 74 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
00001190                     TUPLE: (
00001195                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000011A1                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
000011B8                         STR: 'RIFLE_THREE_ROUND_BURST_DAMAGE' (1E 00 00 00 52 49 46 4C 45 5F 54 48 52 45 45 5F 52 4F 55 4E 44 5F 42 55 52 53 54 5F 44 41 4D 41 47 45),
000011DB                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000011E7                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
000011F5                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00001213                         STR: 'msg' (03 00 00 00 6D 73 67),
0000121B                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
0000122E                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
00001239                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00001257                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00001263                         STR: 'RifleThreeRoundBurstAbility' (1B 00 00 00 52 69 66 6C 65 54 68 72 65 65 52 6F 75 6E 64 42 75 72 73 74 41 62 69 6C 69 74 79),
00001283                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
0000129B                     TUPLE: (
000012A0                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000012AC                         STR: 'msg' (03 00 00 00 6D 73 67),
000012B4                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
000012BF                     TUPLE: ()
                         cellvars:
000012C4                     TUPLE: ()
                         filename:
000012C9                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_rifle.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 72 69 66 6C 65 2E 70 79)
                         name:
00001322                     STR: 'RifleThreeRoundBurst_DirectObject' (21 00 00 00 52 69 66 6C 65 54 68 72 65 65 52 6F 75 6E 64 42 75 72 73 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00001348                     LONG: 101L (65 00 00 00)
                         lnotab:
0000134C                     STR: '\x00\x01\x11\x01\x18\x01' (06 00 00 00 00 01 11 01 18 01),
00001357             CODE:
                         argcount:
00001358                     LONG: 2L (02 00 00 00)
                         nlocals:
0000135C                     LONG: 3L (03 00 00 00)
                         stacksize:
00001360                     LONG: 6L (06 00 00 00)
                         flags:
00001364                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001368                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00t\x03\x00f\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x05\x00i\x06\x00|\x01\x00i\x08\x00t\x03\x00\x83\x02\x00}\x02\x00t\x00\x00i\n\x00t\x0b\x00t\x0c\x00|\x01\x00i\x08\x00|\x01\x00i\r\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (52 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 74 03 00 66 02 00 16 83 01 00 01 7C 00 00 69 05 00 69 06 00 7C 01 00 69 08 00 74 03 00 83 02 00 7D 02 00 74 00 00 69 0A 00 74 0B 00 74 0C 00 7C 01 00 69 08 00 7C 01 00 69 0D 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'RifleWoundingShot: wounded for %d seconds and %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'RIFLE_WOUNDING_SHOT_WOUND_WOUNDING_EFFECT_DURATION'
                             0000000C     74 - LOAD_GLOBAL         'RIFLE_WOUNDING_SHOT_DAMAGE'
                             0000000F     66 - BUILD_TUPLE         r0002
                             00000012     16 - BINARY_MODULO       
                             00000013     83 - CALL_FUNCTION       r0001
                             00000016     01 - POP_TOP             
                             00000017     7C - LOAD_FAST           'subject'
                             0000001A     69 - LOAD_ATTR           'Interlock'
                             0000001D     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             00000020     7C - LOAD_FAST           'msg'
                             00000023     69 - LOAD_ATTR           'subjectLocator'
                             00000026     74 - LOAD_GLOBAL         'RIFLE_WOUNDING_SHOT_DAMAGE'
                             00000029     83 - CALL_FUNCTION       r0002
                             0000002C     7D - STORE_FAST          'damage'
                             0000002F     74 - LOAD_GLOBAL         'Utility'
                             00000032     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             00000035     74 - LOAD_GLOBAL         'SUCCESS'
                             00000038     74 - LOAD_GLOBAL         'RifleWoundingShotAbility'
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
000013BF                     TUPLE: (
000013C4                         None (4E),
000013C5                         STR: 'RifleWoundingShot: wounded for %d seconds and %d damage dealt' (3D 00 00 00 52 69 66 6C 65 57 6F 75 6E 64 69 6E 67 53 68 6F 74 3A 20 77 6F 75 6E 64 65 64 20 66 6F 72 20 25 64 20 73 65 63 6F 6E 64 73 20 61 6E 64 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
00001407                     TUPLE: (
0000140C                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00001418                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
0000142F                         STR: 'RIFLE_WOUNDING_SHOT_WOUND_WOUNDING_EFFECT_DURATION' (32 00 00 00 52 49 46 4C 45 5F 57 4F 55 4E 44 49 4E 47 5F 53 48 4F 54 5F 57 4F 55 4E 44 5F 57 4F 55 4E 44 49 4E 47 5F 45 46 46 45 43 54 5F 44 55 52 41 54 49 4F 4E),
00001466                         STR: 'RIFLE_WOUNDING_SHOT_DAMAGE' (1A 00 00 00 52 49 46 4C 45 5F 57 4F 55 4E 44 49 4E 47 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
00001485                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00001491                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
0000149F                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
000014BD                         STR: 'msg' (03 00 00 00 6D 73 67),
000014C5                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
000014D8                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
000014E3                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00001501                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
0000150D                         STR: 'RifleWoundingShotAbility' (18 00 00 00 52 69 66 6C 65 57 6F 75 6E 64 69 6E 67 53 68 6F 74 41 62 69 6C 69 74 79),
0000152A                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00001542                     TUPLE: (
00001547                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00001553                         STR: 'msg' (03 00 00 00 6D 73 67),
0000155B                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00001566                     TUPLE: ()
                         cellvars:
0000156B                     TUPLE: ()
                         filename:
00001570                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_rifle.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 72 69 66 6C 65 2E 70 79)
                         name:
000015C9                     STR: 'RifleWoundingShot_DirectObject' (1E 00 00 00 52 69 66 6C 65 57 6F 75 6E 64 69 6E 67 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
000015EC                     LONG: 110L (6E 00 00 00)
                         lnotab:
000015F0                     STR: '\x00\x01\x17\x06\x18\x01' (06 00 00 00 00 01 17 06 18 01)
                 )
             names:
000015FB         TUPLE: (
00001600             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
0000160E             STR: 'obj' (03 00 00 00 6F 62 6A),
00001616             STR: 'ability.utility' (0F 00 00 00 61 62 69 6C 69 74 79 2E 75 74 69 6C 69 74 79),
0000162A             STR: 'utility' (07 00 00 00 75 74 69 6C 69 74 79),
00001636             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00001642             STR: 'RIFLE_BODY_SHOT_DAMAGE' (16 00 00 00 52 49 46 4C 45 5F 42 4F 44 59 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
0000165D             STR: 'RIFLE_CRIPPLING_SHOT_DAMAGE' (1B 00 00 00 52 49 46 4C 45 5F 43 52 49 50 50 4C 49 4E 47 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
0000167D             STR: 'RIFLE_DEADLY_SHOT_DAMAGE' (18 00 00 00 52 49 46 4C 45 5F 44 45 41 44 4C 59 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
0000169A             STR: 'RIFLE_DISABLING_SHOT_DAMAGE' (1B 00 00 00 52 49 46 4C 45 5F 44 49 53 41 42 4C 49 4E 47 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
000016BA             STR: 'RIFLE_IMMOBILIZING_SHOT_DAMAGE' (1E 00 00 00 52 49 46 4C 45 5F 49 4D 4D 4F 42 49 4C 49 5A 49 4E 47 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
000016DD             STR: 'RIFLE_RIFLE_BUTT_DAMAGE' (17 00 00 00 52 49 46 4C 45 5F 52 49 46 4C 45 5F 42 55 54 54 5F 44 41 4D 41 47 45),
000016F9             STR: 'RIFLE_THREE_ROUND_BURST_DAMAGE' (1E 00 00 00 52 49 46 4C 45 5F 54 48 52 45 45 5F 52 4F 55 4E 44 5F 42 55 52 53 54 5F 44 41 4D 41 47 45),
0000171C             STR: 'RIFLE_WOUNDING_SHOT_DAMAGE' (1A 00 00 00 52 49 46 4C 45 5F 57 4F 55 4E 44 49 4E 47 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
0000173B             STR: 'RIFLE_WOUNDING_SHOT_WOUND_DAMAGE_PER_5_SECONDS' (2E 00 00 00 52 49 46 4C 45 5F 57 4F 55 4E 44 49 4E 47 5F 53 48 4F 54 5F 57 4F 55 4E 44 5F 44 41 4D 41 47 45 5F 50 45 52 5F 35 5F 53 45 43 4F 4E 44 53),
0000176E             STR: 'RIFLE_IMMOBILIZING_SHOT_STUN_DURATION' (25 00 00 00 52 49 46 4C 45 5F 49 4D 4D 4F 42 49 4C 49 5A 49 4E 47 5F 53 48 4F 54 5F 53 54 55 4E 5F 44 55 52 41 54 49 4F 4E),
00001798             STR: 'RIFLE_DISABLING_SHOT_ABILITY_MOD_DURATION' (29 00 00 00 52 49 46 4C 45 5F 44 49 53 41 42 4C 49 4E 47 5F 53 48 4F 54 5F 41 42 49 4C 49 54 59 5F 4D 4F 44 5F 44 55 52 41 54 49 4F 4E),
000017C6             STR: 'RIFLE_WOUNDING_SHOT_WOUND_WOUNDING_EFFECT_DURATION' (32 00 00 00 52 49 46 4C 45 5F 57 4F 55 4E 44 49 4E 47 5F 53 48 4F 54 5F 57 4F 55 4E 44 5F 57 4F 55 4E 44 49 4E 47 5F 45 46 46 45 43 54 5F 44 55 52 41 54 49 4F 4E),
000017FD             STR: 'RIFLE_RIFLE_BUTT_CONFUSE_EFFECT_DURATION' (28 00 00 00 52 49 46 4C 45 5F 52 49 46 4C 45 5F 42 55 54 54 5F 43 4F 4E 46 55 53 45 5F 45 46 46 45 43 54 5F 44 55 52 41 54 49 4F 4E),
0000182A             STR: 'RIFLE_CRIPPLING_SHOT_ABILITY_MOD_DURATION' (29 00 00 00 52 49 46 4C 45 5F 43 52 49 50 50 4C 49 4E 47 5F 53 48 4F 54 5F 41 42 49 4C 49 54 59 5F 4D 4F 44 5F 44 55 52 41 54 49 4F 4E),
00001858             STR: 'RIFLE_DISABLING_SHOT_ABILITY_MOD' (20 00 00 00 52 49 46 4C 45 5F 44 49 53 41 42 4C 49 4E 47 5F 53 48 4F 54 5F 41 42 49 4C 49 54 59 5F 4D 4F 44),
0000187D             STR: 'RIFLE_CRIPPLING_SHOT_ABILITY_MOD' (20 00 00 00 52 49 46 4C 45 5F 43 52 49 50 50 4C 49 4E 47 5F 53 48 4F 54 5F 41 42 49 4C 49 54 59 5F 4D 4F 44),
000018A2             STR: 'RifleBodyShot_DirectObject' (1A 00 00 00 52 69 66 6C 65 42 6F 64 79 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
000018C1             STR: 'RifleCripplingShot_DirectObject' (1F 00 00 00 52 69 66 6C 65 43 72 69 70 70 6C 69 6E 67 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
000018E5             STR: 'RifleDeadlyShot_DirectObject' (1C 00 00 00 52 69 66 6C 65 44 65 61 64 6C 79 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001906             STR: 'RifleDisablingShot_DirectObject' (1F 00 00 00 52 69 66 6C 65 44 69 73 61 62 6C 69 6E 67 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
0000192A             STR: 'RifleImmobilizingShot_DirectObject' (22 00 00 00 52 69 66 6C 65 49 6D 6D 6F 62 69 6C 69 7A 69 6E 67 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001951             STR: 'RifleRifleButt_DirectObject' (1B 00 00 00 52 69 66 6C 65 52 69 66 6C 65 42 75 74 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001971             STR: 'RifleThreeRoundBurst_DirectObject' (21 00 00 00 52 69 66 6C 65 54 68 72 65 65 52 6F 75 6E 64 42 75 72 73 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001997             STR: 'RifleWoundingShot_DirectObject' (1E 00 00 00 52 69 66 6C 65 57 6F 75 6E 64 69 6E 67 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                 )
             varnames:
000019BA         TUPLE: (
000019BF             STR: 'RIFLE_WOUNDING_SHOT_WOUND_DAMAGE_PER_5_SECONDS' (2E 00 00 00 52 49 46 4C 45 5F 57 4F 55 4E 44 49 4E 47 5F 53 48 4F 54 5F 57 4F 55 4E 44 5F 44 41 4D 41 47 45 5F 50 45 52 5F 35 5F 53 45 43 4F 4E 44 53),
000019F2             STR: 'RifleWoundingShot_DirectObject' (1E 00 00 00 52 69 66 6C 65 57 6F 75 6E 64 69 6E 67 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001A15             STR: 'RIFLE_DISABLING_SHOT_ABILITY_MOD' (20 00 00 00 52 49 46 4C 45 5F 44 49 53 41 42 4C 49 4E 47 5F 53 48 4F 54 5F 41 42 49 4C 49 54 59 5F 4D 4F 44),
00001A3A             STR: 'RifleCripplingShot_DirectObject' (1F 00 00 00 52 69 66 6C 65 43 72 69 70 70 6C 69 6E 67 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001A5E             STR: 'RIFLE_BODY_SHOT_DAMAGE' (16 00 00 00 52 49 46 4C 45 5F 42 4F 44 59 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
00001A79             STR: 'RIFLE_WOUNDING_SHOT_WOUND_WOUNDING_EFFECT_DURATION' (32 00 00 00 52 49 46 4C 45 5F 57 4F 55 4E 44 49 4E 47 5F 53 48 4F 54 5F 57 4F 55 4E 44 5F 57 4F 55 4E 44 49 4E 47 5F 45 46 46 45 43 54 5F 44 55 52 41 54 49 4F 4E),
00001AB0             STR: 'RIFLE_RIFLE_BUTT_DAMAGE' (17 00 00 00 52 49 46 4C 45 5F 52 49 46 4C 45 5F 42 55 54 54 5F 44 41 4D 41 47 45),
00001ACC             STR: 'RIFLE_CRIPPLING_SHOT_ABILITY_MOD' (20 00 00 00 52 49 46 4C 45 5F 43 52 49 50 50 4C 49 4E 47 5F 53 48 4F 54 5F 41 42 49 4C 49 54 59 5F 4D 4F 44),
00001AF1             STR: 'RifleImmobilizingShot_DirectObject' (22 00 00 00 52 69 66 6C 65 49 6D 6D 6F 62 69 6C 69 7A 69 6E 67 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001B18             STR: 'RifleBodyShot_DirectObject' (1A 00 00 00 52 69 66 6C 65 42 6F 64 79 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001B37             STR: 'RIFLE_DISABLING_SHOT_ABILITY_MOD_DURATION' (29 00 00 00 52 49 46 4C 45 5F 44 49 53 41 42 4C 49 4E 47 5F 53 48 4F 54 5F 41 42 49 4C 49 54 59 5F 4D 4F 44 5F 44 55 52 41 54 49 4F 4E),
00001B65             STR: 'RIFLE_THREE_ROUND_BURST_DAMAGE' (1E 00 00 00 52 49 46 4C 45 5F 54 48 52 45 45 5F 52 4F 55 4E 44 5F 42 55 52 53 54 5F 44 41 4D 41 47 45),
00001B88             STR: 'RIFLE_RIFLE_BUTT_CONFUSE_EFFECT_DURATION' (28 00 00 00 52 49 46 4C 45 5F 52 49 46 4C 45 5F 42 55 54 54 5F 43 4F 4E 46 55 53 45 5F 45 46 46 45 43 54 5F 44 55 52 41 54 49 4F 4E),
00001BB5             STR: 'RifleRifleButt_DirectObject' (1B 00 00 00 52 69 66 6C 65 52 69 66 6C 65 42 75 74 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001BD5             STR: 'RifleThreeRoundBurst_DirectObject' (21 00 00 00 52 69 66 6C 65 54 68 72 65 65 52 6F 75 6E 64 42 75 72 73 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001BFB             STR: 'RIFLE_CRIPPLING_SHOT_DAMAGE' (1B 00 00 00 52 49 46 4C 45 5F 43 52 49 50 50 4C 49 4E 47 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
00001C1B             STR: 'RIFLE_IMMOBILIZING_SHOT_DAMAGE' (1E 00 00 00 52 49 46 4C 45 5F 49 4D 4D 4F 42 49 4C 49 5A 49 4E 47 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
00001C3E             STR: 'RifleDeadlyShot_DirectObject' (1C 00 00 00 52 69 66 6C 65 44 65 61 64 6C 79 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001C5F             STR: 'RIFLE_DEADLY_SHOT_DAMAGE' (18 00 00 00 52 49 46 4C 45 5F 44 45 41 44 4C 59 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
00001C7C             STR: 'RIFLE_WOUNDING_SHOT_DAMAGE' (1A 00 00 00 52 49 46 4C 45 5F 57 4F 55 4E 44 49 4E 47 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
00001C9B             STR: 'obj' (03 00 00 00 6F 62 6A),
00001CA3             STR: 'RIFLE_IMMOBILIZING_SHOT_STUN_DURATION' (25 00 00 00 52 49 46 4C 45 5F 49 4D 4D 4F 42 49 4C 49 5A 49 4E 47 5F 53 48 4F 54 5F 53 54 55 4E 5F 44 55 52 41 54 49 4F 4E),
00001CCD             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00001CDB             STR: 'RIFLE_DISABLING_SHOT_DAMAGE' (1B 00 00 00 52 49 46 4C 45 5F 44 49 53 41 42 4C 49 4E 47 5F 53 48 4F 54 5F 44 41 4D 41 47 45),
00001CFB             STR: 'RifleDisablingShot_DirectObject' (1F 00 00 00 52 69 66 6C 65 44 69 73 61 62 6C 69 6E 67 53 68 6F 74 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001D1F             STR: 'RIFLE_CRIPPLING_SHOT_ABILITY_MOD_DURATION' (29 00 00 00 52 49 46 4C 45 5F 43 52 49 50 50 4C 49 4E 47 5F 53 48 4F 54 5F 41 42 49 4C 49 54 59 5F 4D 4F 44 5F 44 55 52 41 54 49 4F 4E),
00001D4D             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79)
                 )
             freevars:
00001D59         TUPLE: ()
             cellvars:
00001D5E         TUPLE: ()
             filename:
00001D63         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_rifle.py' (54 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 72 69 66 6C 65 2E 70 79)
             name:
00001DBC         STR: '?' (01 00 00 00 3F)
             firslineno:
00001DC2         LONG: 1L (01 00 00 00)
             lnotab:
00001DC6         STR: '\t\x01\t\x01\x0c\x07\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x05\x06\x01\x06\x01\x06\x01\x06\x01\x06\x05\x06\x01\x06\x05\t\x08\t\x0c\t\t\t\x0b\t\x0e\t\t\t\t' (34 00 00 00 09 01 09 01 0C 07 06 01 06 01 06 01 06 01 06 01 06 01 06 01 06 01 06 05 06 01 06 01 06 01 06 01 06 05 06 01 06 05 09 08 09 0C 09 09 09 0B 09 0E 09 09 09 09)

