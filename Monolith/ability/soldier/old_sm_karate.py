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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00i\x03\x00Z\x04\x00d\x01\x00k\x05\x00Td\x00\x00k\x06\x00Z\x07\x00d\x02\x00Z\x08\x00d\x03\x00Z\t\x00d\x04\x00Z\n\x00d\x05\x00Z\x0b\x00d\x06\x00Z\x0c\x00d\x07\x00Z\r\x00d\x08\x00Z\x0e\x00d\t\x00Z\x0f\x00d\n\x00Z\x10\x00d\n\x00Z\x11\x00d\n\x00Z\x12\x00d\x0b\x00Z\x13\x00d\x02\x00Z\x14\x00d\x03\x00Z\x15\x00d\x03\x00Z\x16\x00d\x0c\x00Z\x17\x00d\r\x00Z\x18\x00d\x0e\x00Z\x19\x00d\x0e\x00Z\x1a\x00d\x0f\x00Z\x1b\x00d\x10\x00Z\x1c\x00d\x11\x00\x84\x00\x00Z\x1d\x00d\x12\x00\x84\x00\x00Z\x1e\x00e\x04\x00i\x1f\x00e\x1e\x00_ \x00d\x13\x00\x84\x00\x00Z!\x00d\x14\x00\x84\x00\x00Z"\x00d\x15\x00\x84\x00\x00Z#\x00d\x16\x00\x84\x00\x00Z$\x00d\x17\x00\x84\x00\x00Z%\x00d\x18\x00\x84\x00\x00Z&\x00d\x19\x00\x84\x00\x00Z\'\x00d\x00\x00S' (0D 01 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 69 03 00 5A 04 00 64 01 00 6B 05 00 54 64 00 00 6B 06 00 5A 07 00 64 02 00 5A 08 00 64 03 00 5A 09 00 64 04 00 5A 0A 00 64 05 00 5A 0B 00 64 06 00 5A 0C 00 64 07 00 5A 0D 00 64 08 00 5A 0E 00 64 09 00 5A 0F 00 64 0A 00 5A 10 00 64 0A 00 5A 11 00 64 0A 00 5A 12 00 64 0B 00 5A 13 00 64 02 00 5A 14 00 64 03 00 5A 15 00 64 03 00 5A 16 00 64 0C 00 5A 17 00 64 0D 00 5A 18 00 64 0E 00 5A 19 00 64 0E 00 5A 1A 00 64 0F 00 5A 1B 00 64 10 00 5A 1C 00 64 11 00 84 00 00 5A 1D 00 64 12 00 84 00 00 5A 1E 00 65 04 00 69 1F 00 65 1E 00 5F 20 00 64 13 00 84 00 00 5A 21 00 64 14 00 84 00 00 5A 22 00 64 15 00 84 00 00 5A 23 00 64 16 00 84 00 00 5A 24 00 64 17 00 84 00 00 5A 25 00 64 18 00 84 00 00 5A 26 00 64 19 00 84 00 00 5A 27 00 64 00 00 53)
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
                 00000025     64 - LOAD_CONST          None
                 00000028     6B - IMPORT_NAME         'stringtable_client'
                 0000002B     5A - STORE_NAME          'StringTable'
                 0000002E     64 - LOAD_CONST          10
                 00000031     5A - STORE_NAME          'KUNGFU_DIMMAK_STRIKE_DAMAGE'
                 00000034     64 - LOAD_CONST          50
                 00000037     5A - STORE_NAME          'KARATE_GUARD_BREAKER_DAMAGE'
                 0000003A     64 - LOAD_CONST          75
                 0000003D     5A - STORE_NAME          'KARATE_SWIRLING_KI_SUMMON_DAMAGE'
                 00000040     64 - LOAD_CONST          215
                 00000043     5A - STORE_NAME          'KARATE_JUMP_SIDEKICK_DAMAGE'
                 00000046     64 - LOAD_CONST          300
                 00000049     5A - STORE_NAME          'KARATE_KI_CHARGED_REVERSE_PUNCH_DAMAGE'
                 0000004C     64 - LOAD_CONST          325
                 0000004F     5A - STORE_NAME          'KARATE_MACHINEGUN_KICK_DAMAGE'
                 00000052     64 - LOAD_CONST          150
                 00000055     5A - STORE_NAME          'KARATE_POWER_SWEEP_TO_KI_CHARGED_PUNCH_DAMAGE'
                 00000058     64 - LOAD_CONST          250
                 0000005B     5A - STORE_NAME          'KARATE_SKY_HIGH_SIDE_KICK_DAMAGE'
                 0000005E     64 - LOAD_CONST          15
                 00000061     5A - STORE_NAME          'KARATE_BERSERKER_MODS_DURATION'
                 00000064     64 - LOAD_CONST          15
                 00000067     5A - STORE_NAME          'KARATE_GUARD_BREAKER_BLOCK_BOOST_DURATION'
                 0000006A     64 - LOAD_CONST          15
                 0000006D     5A - STORE_NAME          'KARATE_SKY_HIGH_SIDE_KICK_STUN_DURATION'
                 00000070     64 - LOAD_CONST          12
                 00000073     5A - STORE_NAME          'KARATE_POWER_SWEEP_TO_KI_CHARGED_PUNCH_BLOCK_BOOST_DURATION'
                 00000076     64 - LOAD_CONST          10
                 00000079     5A - STORE_NAME          'KARATE_SWIRLING_KI_SUMMON_DURATION'
                 0000007C     64 - LOAD_CONST          50
                 0000007F     5A - STORE_NAME          'KARATE_BERSERKER_ATTACK_MOD'
                 00000082     64 - LOAD_CONST          50
                 00000085     5A - STORE_NAME          'KARATE_BERSERKER_DEFENSE_MOD'
                 00000088     64 - LOAD_CONST          30
                 0000008B     5A - STORE_NAME          'KARATE_BERSERKER_DAMAGE_BONUS_MOD'
                 0000008E     64 - LOAD_CONST          60
                 00000091     5A - STORE_NAME          'KARATE_BERSERKER_LIFE_COST'
                 00000094     64 - LOAD_CONST          -50
                 00000097     5A - STORE_NAME          'KARATE_GUARD_BREAKER_BLOCK_BOOST'
                 0000009A     64 - LOAD_CONST          -50
                 0000009D     5A - STORE_NAME          'KARATE_POWER_SWEEP_TO_KI_CHARGED_PUNCH_BLOCK_BOOST'
                 000000A0     64 - LOAD_CONST          1
                 000000A3     5A - STORE_NAME          'KARATE_SWIRLING_KI_SUMMON_SPEED_EFFECT_MOD'
                 000000A6     64 - LOAD_CONST          2
                 000000A9     5A - STORE_NAME          'KARATE_SWIRLING_KI_SUMMON_SPEED_DEFENSE'
                 000000AC     64 - LOAD_CONST          CODE('KarateBerserkerAttack_Subject')
                 000000AF     84 - MAKE_FUNCTION       r0000
                 000000B2     5A - STORE_NAME          'KarateBerserkerAttack_Subject'
                 000000B5     64 - LOAD_CONST          CODE('KarateBerserkerAttack_Test')
                 000000B8     84 - MAKE_FUNCTION       r0000
                 000000BB     5A - STORE_NAME          'KarateBerserkerAttack_Test'
                 000000BE     65 - LOAD_NAME           'Utility'
                 000000C1     69 - LOAD_ATTR           'BaseCombatSpecialMoveDepAttr'
                 000000C4     65 - LOAD_NAME           'KarateBerserkerAttack_Test'
                 000000C7     5F - STORE_ATTR          'depAttr'
                 000000CA     64 - LOAD_CONST          CODE('KarateGuardBreaker_DirectObject')
                 000000CD     84 - MAKE_FUNCTION       r0000
                 000000D0     5A - STORE_NAME          'KarateGuardBreaker_DirectObject'
                 000000D3     64 - LOAD_CONST          CODE('KarateSidekickCombo_DirectObject')
                 000000D6     84 - MAKE_FUNCTION       r0000
                 000000D9     5A - STORE_NAME          'KarateSidekickCombo_DirectObject'
                 000000DC     64 - LOAD_CONST          CODE('KarateKiChargedReversePunch_DirectObject')
                 000000DF     84 - MAKE_FUNCTION       r0000
                 000000E2     5A - STORE_NAME          'KarateKiChargedReversePunch_DirectObject'
                 000000E5     64 - LOAD_CONST          CODE('KarateMachinegunKick_DirectObject')
                 000000E8     84 - MAKE_FUNCTION       r0000
                 000000EB     5A - STORE_NAME          'KarateMachinegunKick_DirectObject'
                 000000EE     64 - LOAD_CONST          CODE('KaratePowerSweepToKiChargedPunch_DirectObject')
                 000000F1     84 - MAKE_FUNCTION       r0000
                 000000F4     5A - STORE_NAME          'KaratePowerSweepToKiChargedPunch_DirectObject'
                 000000F7     64 - LOAD_CONST          CODE('KarateSkyHighSideKick_DirectObject')
                 000000FA     84 - MAKE_FUNCTION       r0000
                 000000FD     5A - STORE_NAME          'KarateSkyHighSideKick_DirectObject'
                 00000100     64 - LOAD_CONST          CODE('KarateSwirlingKiSummon_DirectObject')
                 00000103     84 - MAKE_FUNCTION       r0000
                 00000106     5A - STORE_NAME          'KarateSwirlingKiSummon_DirectObject'
                 00000109     64 - LOAD_CONST          None
                 0000010C     53 - RETURN_VALUE        
             consts:
0000012B         TUPLE: (
00000130             None (4E),
00000131             TUPLE: (
00000136                 STR: '*' (01 00 00 00 2A)
                     ),
0000013C             INT: 10 (0A 00 00 00),
00000141             INT: 50 (32 00 00 00),
00000146             INT: 75 (4B 00 00 00),
0000014B             INT: 215 (D7 00 00 00),
00000150             INT: 300 (2C 01 00 00),
00000155             INT: 325 (45 01 00 00),
0000015A             INT: 150 (96 00 00 00),
0000015F             INT: 250 (FA 00 00 00),
00000164             INT: 15 (0F 00 00 00),
00000169             INT: 12 (0C 00 00 00),
0000016E             INT: 30 (1E 00 00 00),
00000173             INT: 60 (3C 00 00 00),
00000178             INT: -50 (CE FF FF FF),
0000017D             INT: 1 (01 00 00 00),
00000182             INT: 2 (02 00 00 00),
00000187             CODE:
                         argcount:
00000188                     LONG: 2L (02 00 00 00)
                         nlocals:
0000018C                     LONG: 3L (03 00 00 00)
                         stacksize:
00000190                     LONG: 7L (07 00 00 00)
                         flags:
00000194                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000198                     STR: '|\x01\x00i\x01\x00t\x02\x00j\x02\x00o*\x00\x01t\x03\x00i\x04\x00t\x05\x00i\x06\x00t\x07\x00|\x01\x00i\x08\x00|\x01\x00i\t\x00d\x01\x00\x83\x05\x00\x01d\x00\x00Sn\x01\x00\x01|\x00\x00i\x0b\x00i\x0c\x00t\x07\x00t\r\x00t\x0e\x00t\x0f\x00d\x01\x00d\x01\x00\x83\x06\x00\x01|\x00\x00i\x0b\x00i\x0c\x00t\x07\x00t\x10\x00t\x11\x00t\x0f\x00d\x01\x00d\x01\x00\x83\x06\x00\x01|\x00\x00i\x0b\x00i\x0c\x00t\x07\x00t\x12\x00t\x13\x00t\x0f\x00d\x01\x00d\x01\x00\x83\x06\x00\x01t\x03\x00i\x14\x00d\x02\x00t\x11\x00t\x0e\x00t\x13\x00t\x15\x00f\x04\x00\x16\x83\x01\x00\x01t\x03\x00i\x14\x00d\x03\x00|\x00\x00i\x0b\x00i\x16\x00\x16\x83\x01\x00\x01|\x00\x00i\x0b\x00i\x16\x00t\x15\x00j\x01\x00oU\x00\x01|\x00\x00i\x17\x00i\x18\x00|\x01\x00i\x08\x00|\x00\x00i\x0b\x00i\x16\x00d\x04\x00\x18\x83\x02\x00}\x02\x00t\x03\x00i\x04\x00t\x05\x00i\x1a\x00t\x07\x00|\x01\x00i\x08\x00|\x01\x00i\t\x00|\x02\x00\x83\x05\x00\x01t\x03\x00i\x14\x00d\x05\x00\x83\x01\x00\x01n;\x00\x01|\x00\x00i\x17\x00i\x18\x00|\x01\x00i\x08\x00t\x15\x00\x83\x02\x00}\x02\x00t\x03\x00i\x04\x00t\x05\x00i\x1a\x00t\x07\x00|\x01\x00i\x08\x00|\x01\x00i\t\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (71 01 00 00 7C 01 00 69 01 00 74 02 00 6A 02 00 6F 2A 00 01 74 03 00 69 04 00 74 05 00 69 06 00 74 07 00 7C 01 00 69 08 00 7C 01 00 69 09 00 64 01 00 83 05 00 01 64 00 00 53 6E 01 00 01 7C 00 00 69 0B 00 69 0C 00 74 07 00 74 0D 00 74 0E 00 74 0F 00 64 01 00 64 01 00 83 06 00 01 7C 00 00 69 0B 00 69 0C 00 74 07 00 74 10 00 74 11 00 74 0F 00 64 01 00 64 01 00 83 06 00 01 7C 00 00 69 0B 00 69 0C 00 74 07 00 74 12 00 74 13 00 74 0F 00 64 01 00 64 01 00 83 06 00 01 74 03 00 69 14 00 64 02 00 74 11 00 74 0E 00 74 13 00 74 15 00 66 04 00 16 83 01 00 01 74 03 00 69 14 00 64 03 00 7C 00 00 69 0B 00 69 16 00 16 83 01 00 01 7C 00 00 69 0B 00 69 16 00 74 15 00 6A 01 00 6F 55 00 01 7C 00 00 69 17 00 69 18 00 7C 01 00 69 08 00 7C 00 00 69 0B 00 69 16 00 64 04 00 18 83 02 00 7D 02 00 74 03 00 69 04 00 74 05 00 69 1A 00 74 07 00 7C 01 00 69 08 00 7C 01 00 69 09 00 7C 02 00 83 05 00 01 74 03 00 69 14 00 64 05 00 83 01 00 01 6E 3B 00 01 7C 00 00 69 17 00 69 18 00 7C 01 00 69 08 00 74 15 00 83 02 00 7D 02 00 74 03 00 69 04 00 74 05 00 69 1A 00 74 07 00 7C 01 00 69 08 00 7C 01 00 69 09 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     7C - LOAD_FAST           'msg'
                             00000003     69 - LOAD_ATTR           'result'
                             00000006     74 - LOAD_GLOBAL         'DEFLECTED'
                             00000009     6A - COMPARE_OP          "=="
                             0000000C     6F - JUMP_IF_FALSE       -> 00000039
                             0000000F     01 - POP_TOP             
                             00000010     74 - LOAD_GLOBAL         'Utility'
                             00000013     69 - LOAD_ATTR           'SendAbilityOutputToCaster'
                             00000016     74 - LOAD_GLOBAL         'StringTable'
                             00000019     69 - LOAD_ATTR           'ID_ABILITY_NOT_ENOUGH_LIFE'
                             0000001C     74 - LOAD_GLOBAL         'KarateBerserkerAttackAbility'
                             0000001F     7C - LOAD_FAST           'msg'
                             00000022     69 - LOAD_ATTR           'subjectLocator'
                             00000025     7C - LOAD_FAST           'msg'
                             00000028     69 - LOAD_ATTR           'directObjectLocator'
                             0000002B     64 - LOAD_CONST          0
                             0000002E     83 - CALL_FUNCTION       r0005
                             00000031     01 - POP_TOP             
                             00000032     64 - LOAD_CONST          None
                             00000035     53 - RETURN_VALUE        
                             00000036     6E - JUMP_FORWARD        -> 0000003A
                             00000039     01 - POP_TOP             
                             0000003A     7C - LOAD_FAST           'subject'
                             0000003D     69 - LOAD_ATTR           'AbilityInv'
                             00000040     69 - LOAD_ATTR           'addTempMod'
                             00000043     74 - LOAD_GLOBAL         'KarateBerserkerAttackAbility'
                             00000046     74 - LOAD_GLOBAL         'DefenseAbility'
                             00000049     74 - LOAD_GLOBAL         'KARATE_BERSERKER_DEFENSE_MOD'
                             0000004C     74 - LOAD_GLOBAL         'KARATE_BERSERKER_MODS_DURATION'
                             0000004F     64 - LOAD_CONST          0
                             00000052     64 - LOAD_CONST          0
                             00000055     83 - CALL_FUNCTION       r0006
                             00000058     01 - POP_TOP             
                             00000059     7C - LOAD_FAST           'subject'
                             0000005C     69 - LOAD_ATTR           'AbilityInv'
                             0000005F     69 - LOAD_ATTR           'addTempMod'
                             00000062     74 - LOAD_GLOBAL         'KarateBerserkerAttackAbility'
                             00000065     74 - LOAD_GLOBAL         'AttackAbility'
                             00000068     74 - LOAD_GLOBAL         'KARATE_BERSERKER_ATTACK_MOD'
                             0000006B     74 - LOAD_GLOBAL         'KARATE_BERSERKER_MODS_DURATION'
                             0000006E     64 - LOAD_CONST          0
                             00000071     64 - LOAD_CONST          0
                             00000074     83 - CALL_FUNCTION       r0006
                             00000077     01 - POP_TOP             
                             00000078     7C - LOAD_FAST           'subject'
                             0000007B     69 - LOAD_ATTR           'AbilityInv'
                             0000007E     69 - LOAD_ATTR           'addTempMod'
                             00000081     74 - LOAD_GLOBAL         'KarateBerserkerAttackAbility'
                             00000084     74 - LOAD_GLOBAL         'DamageBonus'
                             00000087     74 - LOAD_GLOBAL         'KARATE_BERSERKER_DAMAGE_BONUS_MOD'
                             0000008A     74 - LOAD_GLOBAL         'KARATE_BERSERKER_MODS_DURATION'
                             0000008D     64 - LOAD_CONST          0
                             00000090     64 - LOAD_CONST          0
                             00000093     83 - CALL_FUNCTION       r0006
                             00000096     01 - POP_TOP             
                             00000097     74 - LOAD_GLOBAL         'Utility'
                             0000009A     69 - LOAD_ATTR           'outputAbilityDebug'
                             0000009D     64 - LOAD_CONST          'KarateBerserkerAttack: %d to Attack & %d to Defense rolls, %d BonusDamage  ,and -%d health.'
                             000000A0     74 - LOAD_GLOBAL         'KARATE_BERSERKER_ATTACK_MOD'
                             000000A3     74 - LOAD_GLOBAL         'KARATE_BERSERKER_DEFENSE_MOD'
                             000000A6     74 - LOAD_GLOBAL         'KARATE_BERSERKER_DAMAGE_BONUS_MOD'
                             000000A9     74 - LOAD_GLOBAL         'KARATE_BERSERKER_LIFE_COST'
                             000000AC     66 - BUILD_TUPLE         r0004
                             000000AF     16 - BINARY_MODULO       
                             000000B0     83 - CALL_FUNCTION       r0001
                             000000B3     01 - POP_TOP             
                             000000B4     74 - LOAD_GLOBAL         'Utility'
                             000000B7     69 - LOAD_ATTR           'outputAbilityDebug'
                             000000BA     64 - LOAD_CONST          'KarateBerserkerAttack: Health is currently %d'
                             000000BD     7C - LOAD_FAST           'subject'
                             000000C0     69 - LOAD_ATTR           'AbilityInv'
                             000000C3     69 - LOAD_ATTR           'Health'
                             000000C6     16 - BINARY_MODULO       
                             000000C7     83 - CALL_FUNCTION       r0001
                             000000CA     01 - POP_TOP             
                             000000CB     7C - LOAD_FAST           'subject'
                             000000CE     69 - LOAD_ATTR           'AbilityInv'
                             000000D1     69 - LOAD_ATTR           'Health'
                             000000D4     74 - LOAD_GLOBAL         'KARATE_BERSERKER_LIFE_COST'
                             000000D7     6A - COMPARE_OP          "<="
                             000000DA     6F - JUMP_IF_FALSE       -> 00000132
                             000000DD     01 - POP_TOP             
                             000000DE     7C - LOAD_FAST           'subject'
                             000000E1     69 - LOAD_ATTR           'Interlock'
                             000000E4     69 - LOAD_ATTR           'specialityDamageFromAbility'
                             000000E7     7C - LOAD_FAST           'msg'
                             000000EA     69 - LOAD_ATTR           'subjectLocator'
                             000000ED     7C - LOAD_FAST           'subject'
                             000000F0     69 - LOAD_ATTR           'AbilityInv'
                             000000F3     69 - LOAD_ATTR           'Health'
                             000000F6     64 - LOAD_CONST          1
                             000000F9     18 - BINARY_SUBTRACT     
                             000000FA     83 - CALL_FUNCTION       r0002
                             000000FD     7D - STORE_FAST          'damage'
                             00000100     74 - LOAD_GLOBAL         'Utility'
                             00000103     69 - LOAD_ATTR           'SendAbilityOutputToCaster'
                             00000106     74 - LOAD_GLOBAL         'StringTable'
                             00000109     69 - LOAD_ATTR           'ID_APPLY_DAMGE_TO_SELF'
                             0000010C     74 - LOAD_GLOBAL         'KarateBerserkerAttackAbility'
                             0000010F     7C - LOAD_FAST           'msg'
                             00000112     69 - LOAD_ATTR           'subjectLocator'
                             00000115     7C - LOAD_FAST           'msg'
                             00000118     69 - LOAD_ATTR           'directObjectLocator'
                             0000011B     7C - LOAD_FAST           'damage'
                             0000011E     83 - CALL_FUNCTION       r0005
                             00000121     01 - POP_TOP             
                             00000122     74 - LOAD_GLOBAL         'Utility'
                             00000125     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000128     64 - LOAD_CONST          "KarateBerserkerAttack: Health set to 1 to ensure charater doesn't die. (Temp Solution)"
                             0000012B     83 - CALL_FUNCTION       r0001
                             0000012E     01 - POP_TOP             
                             0000012F     6E - JUMP_FORWARD        -> 0000016D
                             00000132     01 - POP_TOP             
                             00000133     7C - LOAD_FAST           'subject'
                             00000136     69 - LOAD_ATTR           'Interlock'
                             00000139     69 - LOAD_ATTR           'specialityDamageFromAbility'
                             0000013C     7C - LOAD_FAST           'msg'
                             0000013F     69 - LOAD_ATTR           'subjectLocator'
                             00000142     74 - LOAD_GLOBAL         'KARATE_BERSERKER_LIFE_COST'
                             00000145     83 - CALL_FUNCTION       r0002
                             00000148     7D - STORE_FAST          'damage'
                             0000014B     74 - LOAD_GLOBAL         'Utility'
                             0000014E     69 - LOAD_ATTR           'SendAbilityOutputToCaster'
                             00000151     74 - LOAD_GLOBAL         'StringTable'
                             00000154     69 - LOAD_ATTR           'ID_APPLY_DAMGE_TO_SELF'
                             00000157     74 - LOAD_GLOBAL         'KarateBerserkerAttackAbility'
                             0000015A     7C - LOAD_FAST           'msg'
                             0000015D     69 - LOAD_ATTR           'subjectLocator'
                             00000160     7C - LOAD_FAST           'msg'
                             00000163     69 - LOAD_ATTR           'directObjectLocator'
                             00000166     7C - LOAD_FAST           'damage'
                             00000169     83 - CALL_FUNCTION       r0005
                             0000016C     01 - POP_TOP             
                             0000016D     64 - LOAD_CONST          None
                             00000170     53 - RETURN_VALUE        
                         consts:
0000030E                     TUPLE: (
00000313                         None (4E),
00000314                         INT: 0 (00 00 00 00),
00000319                         STR: 'KarateBerserkerAttack: %d to Attack & %d to Defense rolls, %d BonusDamage  ,and -%d health.' (5B 00 00 00 4B 61 72 61 74 65 42 65 72 73 65 72 6B 65 72 41 74 74 61 63 6B 3A 20 25 64 20 74 6F 20 41 74 74 61 63 6B 20 26 20 25 64 20 74 6F 20 44 65 66 65 6E 73 65 20 72 6F 6C 6C 73 2C 20 25 64 20 42 6F 6E 75 73 44 61 6D 61 67 65 20 20 2C 61 6E 64 20 2D 25 64 20 68 65 61 6C 74 68 2E),
00000379                         STR: 'KarateBerserkerAttack: Health is currently %d' (2D 00 00 00 4B 61 72 61 74 65 42 65 72 73 65 72 6B 65 72 41 74 74 61 63 6B 3A 20 48 65 61 6C 74 68 20 69 73 20 63 75 72 72 65 6E 74 6C 79 20 25 64),
000003AB                         INT: 1 (01 00 00 00),
000003B0                         STR: "KarateBerserkerAttack: Health set to 1 to ensure charater doesn't die. (Temp Solution)" (56 00 00 00 4B 61 72 61 74 65 42 65 72 73 65 72 6B 65 72 41 74 74 61 63 6B 3A 20 48 65 61 6C 74 68 20 73 65 74 20 74 6F 20 31 20 74 6F 20 65 6E 73 75 72 65 20 63 68 61 72 61 74 65 72 20 64 6F 65 73 6E 27 74 20 64 69 65 2E 20 28 54 65 6D 70 20 53 6F 6C 75 74 69 6F 6E 29)
                             )
                         names:
0000040B                     TUPLE: (
00000410                         STR: 'msg' (03 00 00 00 6D 73 67),
00000418                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00000423                         STR: 'DEFLECTED' (09 00 00 00 44 45 46 4C 45 43 54 45 44),
00000431                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
0000043D                         STR: 'SendAbilityOutputToCaster' (19 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 43 61 73 74 65 72),
0000045B                         STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
0000046B                         STR: 'ID_ABILITY_NOT_ENOUGH_LIFE' (1A 00 00 00 49 44 5F 41 42 49 4C 49 54 59 5F 4E 4F 54 5F 45 4E 4F 55 47 48 5F 4C 49 46 45),
0000048A                         STR: 'KarateBerserkerAttackAbility' (1C 00 00 00 4B 61 72 61 74 65 42 65 72 73 65 72 6B 65 72 41 74 74 61 63 6B 41 62 69 6C 69 74 79),
000004AB                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
000004BE                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
000004D6                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000004E2                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
000004F1                         STR: 'addTempMod' (0A 00 00 00 61 64 64 54 65 6D 70 4D 6F 64),
00000500                         STR: 'DefenseAbility' (0E 00 00 00 44 65 66 65 6E 73 65 41 62 69 6C 69 74 79),
00000513                         STR: 'KARATE_BERSERKER_DEFENSE_MOD' (1C 00 00 00 4B 41 52 41 54 45 5F 42 45 52 53 45 52 4B 45 52 5F 44 45 46 45 4E 53 45 5F 4D 4F 44),
00000534                         STR: 'KARATE_BERSERKER_MODS_DURATION' (1E 00 00 00 4B 41 52 41 54 45 5F 42 45 52 53 45 52 4B 45 52 5F 4D 4F 44 53 5F 44 55 52 41 54 49 4F 4E),
00000557                         STR: 'AttackAbility' (0D 00 00 00 41 74 74 61 63 6B 41 62 69 6C 69 74 79),
00000569                         STR: 'KARATE_BERSERKER_ATTACK_MOD' (1B 00 00 00 4B 41 52 41 54 45 5F 42 45 52 53 45 52 4B 45 52 5F 41 54 54 41 43 4B 5F 4D 4F 44),
00000589                         STR: 'DamageBonus' (0B 00 00 00 44 61 6D 61 67 65 42 6F 6E 75 73),
00000599                         STR: 'KARATE_BERSERKER_DAMAGE_BONUS_MOD' (21 00 00 00 4B 41 52 41 54 45 5F 42 45 52 53 45 52 4B 45 52 5F 44 41 4D 41 47 45 5F 42 4F 4E 55 53 5F 4D 4F 44),
000005BF                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
000005D6                         STR: 'KARATE_BERSERKER_LIFE_COST' (1A 00 00 00 4B 41 52 41 54 45 5F 42 45 52 53 45 52 4B 45 52 5F 4C 49 46 45 5F 43 4F 53 54),
000005F5                         STR: 'Health' (06 00 00 00 48 65 61 6C 74 68),
00000600                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
0000060E                         STR: 'specialityDamageFromAbility' (1B 00 00 00 73 70 65 63 69 61 6C 69 74 79 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
0000062E                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
00000639                         STR: 'ID_APPLY_DAMGE_TO_SELF' (16 00 00 00 49 44 5F 41 50 50 4C 59 5F 44 41 4D 47 45 5F 54 4F 5F 53 45 4C 46)
                             )
                         varnames:
00000654                     TUPLE: (
00000659                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000665                         STR: 'msg' (03 00 00 00 6D 73 67),
0000066D                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00000678                     TUPLE: ()
                         cellvars:
0000067D                     TUPLE: ()
                         filename:
00000682                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_karate.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 6B 61 72 61 74 65 2E 70 79)
                         name:
000006DC                     STR: 'KarateBerserkerAttack_Subject' (1D 00 00 00 4B 61 72 61 74 65 42 65 72 73 65 72 6B 65 72 41 74 74 61 63 6B 5F 53 75 62 6A 65 63 74)
                         firslineno:
000006FE                     LONG: 47L (2F 00 00 00)
                         lnotab:
00000702                     STR: '\x00\x04\x10\x01"\x01\x08\x02\x1f\x01\x1f\x01\x1f\x02\x1d\x04\x17\x02\x13\x01"\x01"\x01\x11\x02\x18\x01' (1C 00 00 00 00 04 10 01 22 01 08 02 1F 01 1F 01 1F 02 1D 04 17 02 13 01 22 01 22 01 11 02 18 01),
00000723             CODE:
                         argcount:
00000724                     LONG: 1L (01 00 00 00)
                         nlocals:
00000728                     LONG: 1L (01 00 00 00)
                         stacksize:
0000072C                     LONG: 2L (02 00 00 00)
                         flags:
00000730                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000734                     STR: 't\x00\x00|\x00\x00_\x02\x00|\x00\x00i\x03\x00i\x04\x00i\x05\x00t\x06\x00j\x01\x00o\r\x00\x01t\x07\x00|\x00\x00_\x02\x00n\x01\x00\x01d\x00\x00S' (30 00 00 00 74 00 00 7C 00 00 5F 02 00 7C 00 00 69 03 00 69 04 00 69 05 00 74 06 00 6A 01 00 6F 0D 00 01 74 07 00 7C 00 00 5F 02 00 6E 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'SUCCESS'
                             00000003     7C - LOAD_FAST           'sentence'
                             00000006     5F - STORE_ATTR          'result'
                             00000009     7C - LOAD_FAST           'sentence'
                             0000000C     69 - LOAD_ATTR           'subject'
                             0000000F     69 - LOAD_ATTR           'AbilityInv'
                             00000012     69 - LOAD_ATTR           'Health'
                             00000015     74 - LOAD_GLOBAL         'KARATE_BERSERKER_LIFE_COST'
                             00000018     6A - COMPARE_OP          "<="
                             0000001B     6F - JUMP_IF_FALSE       -> 0000002B
                             0000001E     01 - POP_TOP             
                             0000001F     74 - LOAD_GLOBAL         'DEFLECTED'
                             00000022     7C - LOAD_FAST           'sentence'
                             00000025     5F - STORE_ATTR          'result'
                             00000028     6E - JUMP_FORWARD        -> 0000002C
                             0000002B     01 - POP_TOP             
                             0000002C     64 - LOAD_CONST          None
                             0000002F     53 - RETURN_VALUE        
                         consts:
00000769                     TUPLE: (
0000076E                         None (4E)
                             )
                         names:
0000076F                     TUPLE: (
00000774                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00000780                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65),
0000078D                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00000798                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000007A4                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
000007B3                         STR: 'Health' (06 00 00 00 48 65 61 6C 74 68),
000007BE                         STR: 'KARATE_BERSERKER_LIFE_COST' (1A 00 00 00 4B 41 52 41 54 45 5F 42 45 52 53 45 52 4B 45 52 5F 4C 49 46 45 5F 43 4F 53 54),
000007DD                         STR: 'DEFLECTED' (09 00 00 00 44 45 46 4C 45 43 54 45 44)
                             )
                         varnames:
000007EB                     TUPLE: (
000007F0                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65)
                             )
                         freevars:
000007FD                     TUPLE: ()
                         cellvars:
00000802                     TUPLE: ()
                         filename:
00000807                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_karate.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 6B 61 72 61 74 65 2E 70 79)
                         name:
00000861                     STR: 'KarateBerserkerAttack_Test' (1A 00 00 00 4B 61 72 61 74 65 42 65 72 73 65 72 6B 65 72 41 74 74 61 63 6B 5F 54 65 73 74)
                         firslineno:
00000880                     LONG: 74L (4A 00 00 00)
                         lnotab:
00000884                     STR: '\x00\x02\t\x01\x16\x01' (06 00 00 00 00 02 09 01 16 01),
0000088F             CODE:
                         argcount:
00000890                     LONG: 2L (02 00 00 00)
                         nlocals:
00000894                     LONG: 5L (05 00 00 00)
                         stacksize:
00000898                     LONG: 7L (07 00 00 00)
                         flags:
0000089C                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000008A0                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00t\x03\x00f\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x05\x00i\x06\x00t\x07\x00t\x08\x00t\x02\x00\x83\x03\x00}\x03\x00|\x00\x00i\x05\x00i\x06\x00t\n\x00t\x08\x00t\x02\x00\x83\x03\x00}\x04\x00|\x00\x00i\x05\x00i\x0c\x00t\r\x00t\x0e\x00|\x03\x00t\x0f\x00d\x02\x00d\x02\x00\x83\x06\x00\x01|\x00\x00i\x05\x00i\x0c\x00t\r\x00t\x0e\x00|\x04\x00t\x0f\x00d\x02\x00d\x02\x00\x83\x06\x00\x01|\x00\x00i\x10\x00i\x11\x00|\x01\x00i\x13\x00t\x03\x00\x83\x02\x00}\x02\x00t\x00\x00i\x15\x00t\x16\x00t\r\x00|\x01\x00i\x13\x00|\x01\x00i\x17\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (C0 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 74 03 00 66 02 00 16 83 01 00 01 7C 00 00 69 05 00 69 06 00 74 07 00 74 08 00 74 02 00 83 03 00 7D 03 00 7C 00 00 69 05 00 69 06 00 74 0A 00 74 08 00 74 02 00 83 03 00 7D 04 00 7C 00 00 69 05 00 69 0C 00 74 0D 00 74 0E 00 7C 03 00 74 0F 00 64 02 00 64 02 00 83 06 00 01 7C 00 00 69 05 00 69 0C 00 74 0D 00 74 0E 00 7C 04 00 74 0F 00 64 02 00 64 02 00 83 06 00 01 7C 00 00 69 10 00 69 11 00 7C 01 00 69 13 00 74 03 00 83 02 00 7D 02 00 74 00 00 69 15 00 74 16 00 74 0D 00 7C 01 00 69 13 00 7C 01 00 69 17 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'KarateGuardBreaker: %d to Defense tactical setting and %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'KARATE_GUARD_BREAKER_BLOCK_BOOST'
                             0000000C     74 - LOAD_GLOBAL         'KARATE_GUARD_BREAKER_DAMAGE'
                             0000000F     66 - BUILD_TUPLE         r0002
                             00000012     16 - BINARY_MODULO       
                             00000013     83 - CALL_FUNCTION       r0001
                             00000016     01 - POP_TOP             
                             00000017     7C - LOAD_FAST           'subject'
                             0000001A     69 - LOAD_ATTR           'AbilityInv'
                             0000001D     69 - LOAD_ATTR           'createSpecificMod'
                             00000020     74 - LOAD_GLOBAL         'MOD_AFFECTS_DEFENSEMOD'
                             00000023     74 - LOAD_GLOBAL         'MOD_BLOCK'
                             00000026     74 - LOAD_GLOBAL         'KARATE_GUARD_BREAKER_BLOCK_BOOST'
                             00000029     83 - CALL_FUNCTION       r0003
                             0000002C     7D - STORE_FAST          'value'
                             0000002F     7C - LOAD_FAST           'subject'
                             00000032     69 - LOAD_ATTR           'AbilityInv'
                             00000035     69 - LOAD_ATTR           'createSpecificMod'
                             00000038     74 - LOAD_GLOBAL         'MOD_AFFECTS_ATTACKMOD'
                             0000003B     74 - LOAD_GLOBAL         'MOD_BLOCK'
                             0000003E     74 - LOAD_GLOBAL         'KARATE_GUARD_BREAKER_BLOCK_BOOST'
                             00000041     83 - CALL_FUNCTION       r0003
                             00000044     7D - STORE_FAST          'value2'
                             00000047     7C - LOAD_FAST           'subject'
                             0000004A     69 - LOAD_ATTR           'AbilityInv'
                             0000004D     69 - LOAD_ATTR           'addTempMod'
                             00000050     74 - LOAD_GLOBAL         'KarateGuardBreakerAbility'
                             00000053     74 - LOAD_GLOBAL         'CombatModifierAbility'
                             00000056     7C - LOAD_FAST           'value'
                             00000059     74 - LOAD_GLOBAL         'KARATE_GUARD_BREAKER_BLOCK_BOOST_DURATION'
                             0000005C     64 - LOAD_CONST          0
                             0000005F     64 - LOAD_CONST          0
                             00000062     83 - CALL_FUNCTION       r0006
                             00000065     01 - POP_TOP             
                             00000066     7C - LOAD_FAST           'subject'
                             00000069     69 - LOAD_ATTR           'AbilityInv'
                             0000006C     69 - LOAD_ATTR           'addTempMod'
                             0000006F     74 - LOAD_GLOBAL         'KarateGuardBreakerAbility'
                             00000072     74 - LOAD_GLOBAL         'CombatModifierAbility'
                             00000075     7C - LOAD_FAST           'value2'
                             00000078     74 - LOAD_GLOBAL         'KARATE_GUARD_BREAKER_BLOCK_BOOST_DURATION'
                             0000007B     64 - LOAD_CONST          0
                             0000007E     64 - LOAD_CONST          0
                             00000081     83 - CALL_FUNCTION       r0006
                             00000084     01 - POP_TOP             
                             00000085     7C - LOAD_FAST           'subject'
                             00000088     69 - LOAD_ATTR           'Interlock'
                             0000008B     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000008E     7C - LOAD_FAST           'msg'
                             00000091     69 - LOAD_ATTR           'subjectLocator'
                             00000094     74 - LOAD_GLOBAL         'KARATE_GUARD_BREAKER_DAMAGE'
                             00000097     83 - CALL_FUNCTION       r0002
                             0000009A     7D - STORE_FAST          'damage'
                             0000009D     74 - LOAD_GLOBAL         'Utility'
                             000000A0     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             000000A3     74 - LOAD_GLOBAL         'SUCCESS'
                             000000A6     74 - LOAD_GLOBAL         'KarateGuardBreakerAbility'
                             000000A9     7C - LOAD_FAST           'msg'
                             000000AC     69 - LOAD_ATTR           'subjectLocator'
                             000000AF     7C - LOAD_FAST           'msg'
                             000000B2     69 - LOAD_ATTR           'directObjectLocator'
                             000000B5     7C - LOAD_FAST           'damage'
                             000000B8     83 - CALL_FUNCTION       r0005
                             000000BB     01 - POP_TOP             
                             000000BC     64 - LOAD_CONST          None
                             000000BF     53 - RETURN_VALUE        
                         consts:
00000965                     TUPLE: (
0000096A                         None (4E),
0000096B                         STR: 'KarateGuardBreaker: %d to Defense tactical setting and %d damage dealt' (46 00 00 00 4B 61 72 61 74 65 47 75 61 72 64 42 72 65 61 6B 65 72 3A 20 25 64 20 74 6F 20 44 65 66 65 6E 73 65 20 74 61 63 74 69 63 61 6C 20 73 65 74 74 69 6E 67 20 61 6E 64 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74),
000009B6                         INT: 0 (00 00 00 00)
                             )
                         names:
000009BB                     TUPLE: (
000009C0                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000009CC                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
000009E3                         STR: 'KARATE_GUARD_BREAKER_BLOCK_BOOST' (20 00 00 00 4B 41 52 41 54 45 5F 47 55 41 52 44 5F 42 52 45 41 4B 45 52 5F 42 4C 4F 43 4B 5F 42 4F 4F 53 54),
00000A08                         STR: 'KARATE_GUARD_BREAKER_DAMAGE' (1B 00 00 00 4B 41 52 41 54 45 5F 47 55 41 52 44 5F 42 52 45 41 4B 45 52 5F 44 41 4D 41 47 45),
00000A28                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000A34                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
00000A43                         STR: 'createSpecificMod' (11 00 00 00 63 72 65 61 74 65 53 70 65 63 69 66 69 63 4D 6F 64),
00000A59                         STR: 'MOD_AFFECTS_DEFENSEMOD' (16 00 00 00 4D 4F 44 5F 41 46 46 45 43 54 53 5F 44 45 46 45 4E 53 45 4D 4F 44),
00000A74                         STR: 'MOD_BLOCK' (09 00 00 00 4D 4F 44 5F 42 4C 4F 43 4B),
00000A82                         STR: 'value' (05 00 00 00 76 61 6C 75 65),
00000A8C                         STR: 'MOD_AFFECTS_ATTACKMOD' (15 00 00 00 4D 4F 44 5F 41 46 46 45 43 54 53 5F 41 54 54 41 43 4B 4D 4F 44),
00000AA6                         STR: 'value2' (06 00 00 00 76 61 6C 75 65 32),
00000AB1                         STR: 'addTempMod' (0A 00 00 00 61 64 64 54 65 6D 70 4D 6F 64),
00000AC0                         STR: 'KarateGuardBreakerAbility' (19 00 00 00 4B 61 72 61 74 65 47 75 61 72 64 42 72 65 61 6B 65 72 41 62 69 6C 69 74 79),
00000ADE                         STR: 'CombatModifierAbility' (15 00 00 00 43 6F 6D 62 61 74 4D 6F 64 69 66 69 65 72 41 62 69 6C 69 74 79),
00000AF8                         STR: 'KARATE_GUARD_BREAKER_BLOCK_BOOST_DURATION' (29 00 00 00 4B 41 52 41 54 45 5F 47 55 41 52 44 5F 42 52 45 41 4B 45 52 5F 42 4C 4F 43 4B 5F 42 4F 4F 53 54 5F 44 55 52 41 54 49 4F 4E),
00000B26                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00000B34                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00000B52                         STR: 'msg' (03 00 00 00 6D 73 67),
00000B5A                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00000B6D                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
00000B78                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00000B96                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00000BA2                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00000BBA                     TUPLE: (
00000BBF                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000BCB                         STR: 'msg' (03 00 00 00 6D 73 67),
00000BD3                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
00000BDE                         STR: 'value' (05 00 00 00 76 61 6C 75 65),
00000BE8                         STR: 'value2' (06 00 00 00 76 61 6C 75 65 32)
                             )
                         freevars:
00000BF3                     TUPLE: ()
                         cellvars:
00000BF8                     TUPLE: ()
                         filename:
00000BFD                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_karate.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 6B 61 72 61 74 65 2E 70 79)
                         name:
00000C57                     STR: 'KarateGuardBreaker_DirectObject' (1F 00 00 00 4B 61 72 61 74 65 47 75 61 72 64 42 72 65 61 6B 65 72 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000C7B                     LONG: 87L (57 00 00 00)
                         lnotab:
00000C7F                     STR: '\x00\x01\x17\x03\x18\x01\x18\x02\x12\x01\r\x01\x12\x01\r\x02\x18\x01' (12 00 00 00 00 01 17 03 18 01 18 02 12 01 0D 01 12 01 0D 02 18 01),
00000C96             CODE:
                         argcount:
00000C97                     LONG: 2L (02 00 00 00)
                         nlocals:
00000C9B                     LONG: 3L (03 00 00 00)
                         stacksize:
00000C9F                     LONG: 6L (06 00 00 00)
                         flags:
00000CA3                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000CA7                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'KarateSidekickCombo: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'KARATE_JUMP_SIDEKICK_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'KARATE_JUMP_SIDEKICK_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'KarateSidekickComboAbility'
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
00000CF8                     TUPLE: (
00000CFD                         None (4E),
00000CFE                         STR: 'KarateSidekickCombo: %d damage dealt' (24 00 00 00 4B 61 72 61 74 65 53 69 64 65 6B 69 63 6B 43 6F 6D 62 6F 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
00000D27                     TUPLE: (
00000D2C                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000D38                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000D4F                         STR: 'KARATE_JUMP_SIDEKICK_DAMAGE' (1B 00 00 00 4B 41 52 41 54 45 5F 4A 55 4D 50 5F 53 49 44 45 4B 49 43 4B 5F 44 41 4D 41 47 45),
00000D6F                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000D7B                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00000D89                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00000DA7                         STR: 'msg' (03 00 00 00 6D 73 67),
00000DAF                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00000DC2                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
00000DCD                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00000DEB                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00000DF7                         STR: 'KarateSidekickComboAbility' (1A 00 00 00 4B 61 72 61 74 65 53 69 64 65 6B 69 63 6B 43 6F 6D 62 6F 41 62 69 6C 69 74 79),
00000E16                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00000E2E                     TUPLE: (
00000E33                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000E3F                         STR: 'msg' (03 00 00 00 6D 73 67),
00000E47                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00000E52                     TUPLE: ()
                         cellvars:
00000E57                     TUPLE: ()
                         filename:
00000E5C                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_karate.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 6B 61 72 61 74 65 2E 70 79)
                         name:
00000EB6                     STR: 'KarateSidekickCombo_DirectObject' (20 00 00 00 4B 61 72 61 74 65 53 69 64 65 6B 69 63 6B 43 6F 6D 62 6F 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000EDB                     LONG: 108L (6C 00 00 00)
                         lnotab:
00000EDF                     STR: '\x00\x01\x11\x01\x18\x01' (06 00 00 00 00 01 11 01 18 01),
00000EEA             CODE:
                         argcount:
00000EEB                     LONG: 2L (02 00 00 00)
                         nlocals:
00000EEF                     LONG: 3L (03 00 00 00)
                         stacksize:
00000EF3                     LONG: 6L (06 00 00 00)
                         flags:
00000EF7                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000EFB                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'KarateKiChargedReversePunch: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'KARATE_KI_CHARGED_REVERSE_PUNCH_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'KARATE_KI_CHARGED_REVERSE_PUNCH_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'KarateKiChargedReversePunchAbility'
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
00000F4C                     TUPLE: (
00000F51                         None (4E),
00000F52                         STR: 'KarateKiChargedReversePunch: %d damage dealt' (2C 00 00 00 4B 61 72 61 74 65 4B 69 43 68 61 72 67 65 64 52 65 76 65 72 73 65 50 75 6E 63 68 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
00000F83                     TUPLE: (
00000F88                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000F94                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000FAB                         STR: 'KARATE_KI_CHARGED_REVERSE_PUNCH_DAMAGE' (26 00 00 00 4B 41 52 41 54 45 5F 4B 49 5F 43 48 41 52 47 45 44 5F 52 45 56 45 52 53 45 5F 50 55 4E 43 48 5F 44 41 4D 41 47 45),
00000FD6                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000FE2                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00000FF0                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
0000100E                         STR: 'msg' (03 00 00 00 6D 73 67),
00001016                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00001029                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
00001034                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00001052                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
0000105E                         STR: 'KarateKiChargedReversePunchAbility' (22 00 00 00 4B 61 72 61 74 65 4B 69 43 68 61 72 67 65 64 52 65 76 65 72 73 65 50 75 6E 63 68 41 62 69 6C 69 74 79),
00001085                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
0000109D                     TUPLE: (
000010A2                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000010AE                         STR: 'msg' (03 00 00 00 6D 73 67),
000010B6                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
000010C1                     TUPLE: ()
                         cellvars:
000010C6                     TUPLE: ()
                         filename:
000010CB                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_karate.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 6B 61 72 61 74 65 2E 70 79)
                         name:
00001125                     STR: 'KarateKiChargedReversePunch_DirectObject' (28 00 00 00 4B 61 72 61 74 65 4B 69 43 68 61 72 67 65 64 52 65 76 65 72 73 65 50 75 6E 63 68 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00001152                     LONG: 117L (75 00 00 00)
                         lnotab:
00001156                     STR: '\x00\x01\x11\x01\x18\x01' (06 00 00 00 00 01 11 01 18 01),
00001161             CODE:
                         argcount:
00001162                     LONG: 2L (02 00 00 00)
                         nlocals:
00001166                     LONG: 3L (03 00 00 00)
                         stacksize:
0000116A                     LONG: 6L (06 00 00 00)
                         flags:
0000116E                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001172                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x04\x00i\x05\x00|\x01\x00i\x07\x00t\x02\x00\x83\x02\x00}\x02\x00t\x00\x00i\t\x00t\n\x00t\x0b\x00|\x01\x00i\x07\x00|\x01\x00i\x0c\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (4C 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 16 83 01 00 01 7C 00 00 69 04 00 69 05 00 7C 01 00 69 07 00 74 02 00 83 02 00 7D 02 00 74 00 00 69 09 00 74 0A 00 74 0B 00 7C 01 00 69 07 00 7C 01 00 69 0C 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'KarateMachinegunKick: %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'KARATE_MACHINEGUN_KICK_DAMAGE'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     83 - CALL_FUNCTION       r0001
                             00000010     01 - POP_TOP             
                             00000011     7C - LOAD_FAST           'subject'
                             00000014     69 - LOAD_ATTR           'Interlock'
                             00000017     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             0000001A     7C - LOAD_FAST           'msg'
                             0000001D     69 - LOAD_ATTR           'subjectLocator'
                             00000020     74 - LOAD_GLOBAL         'KARATE_MACHINEGUN_KICK_DAMAGE'
                             00000023     83 - CALL_FUNCTION       r0002
                             00000026     7D - STORE_FAST          'damage'
                             00000029     74 - LOAD_GLOBAL         'Utility'
                             0000002C     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000002F     74 - LOAD_GLOBAL         'SUCCESS'
                             00000032     74 - LOAD_GLOBAL         'KarateMachinegunKickAbility'
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
000011C3                     TUPLE: (
000011C8                         None (4E),
000011C9                         STR: 'KarateMachinegunKick: %d damage dealt' (25 00 00 00 4B 61 72 61 74 65 4D 61 63 68 69 6E 65 67 75 6E 4B 69 63 6B 3A 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
000011F3                     TUPLE: (
000011F8                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00001204                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
0000121B                         STR: 'KARATE_MACHINEGUN_KICK_DAMAGE' (1D 00 00 00 4B 41 52 41 54 45 5F 4D 41 43 48 49 4E 45 47 55 4E 5F 4B 49 43 4B 5F 44 41 4D 41 47 45),
0000123D                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00001249                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00001257                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00001275                         STR: 'msg' (03 00 00 00 6D 73 67),
0000127D                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00001290                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
0000129B                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
000012B9                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
000012C5                         STR: 'KarateMachinegunKickAbility' (1B 00 00 00 4B 61 72 61 74 65 4D 61 63 68 69 6E 65 67 75 6E 4B 69 63 6B 41 62 69 6C 69 74 79),
000012E5                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
000012FD                     TUPLE: (
00001302                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000130E                         STR: 'msg' (03 00 00 00 6D 73 67),
00001316                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00001321                     TUPLE: ()
                         cellvars:
00001326                     TUPLE: ()
                         filename:
0000132B                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_karate.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 6B 61 72 61 74 65 2E 70 79)
                         name:
00001385                     STR: 'KarateMachinegunKick_DirectObject' (21 00 00 00 4B 61 72 61 74 65 4D 61 63 68 69 6E 65 67 75 6E 4B 69 63 6B 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
000013AB                     LONG: 126L (7E 00 00 00)
                         lnotab:
000013AF                     STR: '\x00\x01\x11\x03\x18\x01' (06 00 00 00 00 01 11 03 18 01),
000013BA             CODE:
                         argcount:
000013BB                     LONG: 2L (02 00 00 00)
                         nlocals:
000013BF                     LONG: 5L (05 00 00 00)
                         stacksize:
000013C3                     LONG: 7L (07 00 00 00)
                         flags:
000013C7                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000013CB                     STR: '|\x00\x00i\x01\x00i\x02\x00t\x03\x00t\x04\x00t\x05\x00\x83\x03\x00}\x03\x00|\x00\x00i\x01\x00i\x02\x00t\x07\x00t\x04\x00t\x05\x00\x83\x03\x00}\x04\x00|\x00\x00i\x01\x00i\t\x00t\n\x00t\x0b\x00|\x03\x00t\x0c\x00d\x01\x00d\x01\x00\x83\x06\x00\x01|\x00\x00i\x01\x00i\t\x00t\n\x00t\x0b\x00|\x04\x00t\x0c\x00d\x01\x00d\x01\x00\x83\x06\x00\x01|\x00\x00i\r\x00i\x0e\x00|\x01\x00i\x10\x00t\x11\x00\x83\x02\x00}\x02\x00t\x13\x00i\x14\x00t\x15\x00t\n\x00|\x01\x00i\x10\x00|\x01\x00i\x16\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (A9 00 00 00 7C 00 00 69 01 00 69 02 00 74 03 00 74 04 00 74 05 00 83 03 00 7D 03 00 7C 00 00 69 01 00 69 02 00 74 07 00 74 04 00 74 05 00 83 03 00 7D 04 00 7C 00 00 69 01 00 69 09 00 74 0A 00 74 0B 00 7C 03 00 74 0C 00 64 01 00 64 01 00 83 06 00 01 7C 00 00 69 01 00 69 09 00 74 0A 00 74 0B 00 7C 04 00 74 0C 00 64 01 00 64 01 00 83 06 00 01 7C 00 00 69 0D 00 69 0E 00 7C 01 00 69 10 00 74 11 00 83 02 00 7D 02 00 74 13 00 69 14 00 74 15 00 74 0A 00 7C 01 00 69 10 00 7C 01 00 69 16 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     7C - LOAD_FAST           'subject'
                             00000003     69 - LOAD_ATTR           'AbilityInv'
                             00000006     69 - LOAD_ATTR           'createSpecificMod'
                             00000009     74 - LOAD_GLOBAL         'MOD_AFFECTS_DEFENSEMOD'
                             0000000C     74 - LOAD_GLOBAL         'MOD_BLOCK'
                             0000000F     74 - LOAD_GLOBAL         'KARATE_POWER_SWEEP_TO_KI_CHARGED_PUNCH_BLOCK_BOOST'
                             00000012     83 - CALL_FUNCTION       r0003
                             00000015     7D - STORE_FAST          'value'
                             00000018     7C - LOAD_FAST           'subject'
                             0000001B     69 - LOAD_ATTR           'AbilityInv'
                             0000001E     69 - LOAD_ATTR           'createSpecificMod'
                             00000021     74 - LOAD_GLOBAL         'MOD_AFFECTS_ATTACKMOD'
                             00000024     74 - LOAD_GLOBAL         'MOD_BLOCK'
                             00000027     74 - LOAD_GLOBAL         'KARATE_POWER_SWEEP_TO_KI_CHARGED_PUNCH_BLOCK_BOOST'
                             0000002A     83 - CALL_FUNCTION       r0003
                             0000002D     7D - STORE_FAST          'value2'
                             00000030     7C - LOAD_FAST           'subject'
                             00000033     69 - LOAD_ATTR           'AbilityInv'
                             00000036     69 - LOAD_ATTR           'addTempMod'
                             00000039     74 - LOAD_GLOBAL         'KaratePowerSweepToKiChargedPunchAbility'
                             0000003C     74 - LOAD_GLOBAL         'CombatModifierAbility'
                             0000003F     7C - LOAD_FAST           'value'
                             00000042     74 - LOAD_GLOBAL         'KARATE_POWER_SWEEP_TO_KI_CHARGED_PUNCH_BLOCK_BOOST_DURATION'
                             00000045     64 - LOAD_CONST          0
                             00000048     64 - LOAD_CONST          0
                             0000004B     83 - CALL_FUNCTION       r0006
                             0000004E     01 - POP_TOP             
                             0000004F     7C - LOAD_FAST           'subject'
                             00000052     69 - LOAD_ATTR           'AbilityInv'
                             00000055     69 - LOAD_ATTR           'addTempMod'
                             00000058     74 - LOAD_GLOBAL         'KaratePowerSweepToKiChargedPunchAbility'
                             0000005B     74 - LOAD_GLOBAL         'CombatModifierAbility'
                             0000005E     7C - LOAD_FAST           'value2'
                             00000061     74 - LOAD_GLOBAL         'KARATE_POWER_SWEEP_TO_KI_CHARGED_PUNCH_BLOCK_BOOST_DURATION'
                             00000064     64 - LOAD_CONST          0
                             00000067     64 - LOAD_CONST          0
                             0000006A     83 - CALL_FUNCTION       r0006
                             0000006D     01 - POP_TOP             
                             0000006E     7C - LOAD_FAST           'subject'
                             00000071     69 - LOAD_ATTR           'Interlock'
                             00000074     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             00000077     7C - LOAD_FAST           'msg'
                             0000007A     69 - LOAD_ATTR           'subjectLocator'
                             0000007D     74 - LOAD_GLOBAL         'KARATE_POWER_SWEEP_TO_KI_CHARGED_PUNCH_DAMAGE'
                             00000080     83 - CALL_FUNCTION       r0002
                             00000083     7D - STORE_FAST          'damage'
                             00000086     74 - LOAD_GLOBAL         'Utility'
                             00000089     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             0000008C     74 - LOAD_GLOBAL         'SUCCESS'
                             0000008F     74 - LOAD_GLOBAL         'KaratePowerSweepToKiChargedPunchAbility'
                             00000092     7C - LOAD_FAST           'msg'
                             00000095     69 - LOAD_ATTR           'subjectLocator'
                             00000098     7C - LOAD_FAST           'msg'
                             0000009B     69 - LOAD_ATTR           'directObjectLocator'
                             0000009E     7C - LOAD_FAST           'damage'
                             000000A1     83 - CALL_FUNCTION       r0005
                             000000A4     01 - POP_TOP             
                             000000A5     64 - LOAD_CONST          None
                             000000A8     53 - RETURN_VALUE        
                         consts:
00001479                     TUPLE: (
0000147E                         None (4E),
0000147F                         INT: 0 (00 00 00 00)
                             )
                         names:
00001484                     TUPLE: (
00001489                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00001495                         STR: 'AbilityInv' (0A 00 00 00 41 62 69 6C 69 74 79 49 6E 76),
000014A4                         STR: 'createSpecificMod' (11 00 00 00 63 72 65 61 74 65 53 70 65 63 69 66 69 63 4D 6F 64),
000014BA                         STR: 'MOD_AFFECTS_DEFENSEMOD' (16 00 00 00 4D 4F 44 5F 41 46 46 45 43 54 53 5F 44 45 46 45 4E 53 45 4D 4F 44),
000014D5                         STR: 'MOD_BLOCK' (09 00 00 00 4D 4F 44 5F 42 4C 4F 43 4B),
000014E3                         STR: 'KARATE_POWER_SWEEP_TO_KI_CHARGED_PUNCH_BLOCK_BOOST' (32 00 00 00 4B 41 52 41 54 45 5F 50 4F 57 45 52 5F 53 57 45 45 50 5F 54 4F 5F 4B 49 5F 43 48 41 52 47 45 44 5F 50 55 4E 43 48 5F 42 4C 4F 43 4B 5F 42 4F 4F 53 54),
0000151A                         STR: 'value' (05 00 00 00 76 61 6C 75 65),
00001524                         STR: 'MOD_AFFECTS_ATTACKMOD' (15 00 00 00 4D 4F 44 5F 41 46 46 45 43 54 53 5F 41 54 54 41 43 4B 4D 4F 44),
0000153E                         STR: 'value2' (06 00 00 00 76 61 6C 75 65 32),
00001549                         STR: 'addTempMod' (0A 00 00 00 61 64 64 54 65 6D 70 4D 6F 64),
00001558                         STR: 'KaratePowerSweepToKiChargedPunchAbility' (27 00 00 00 4B 61 72 61 74 65 50 6F 77 65 72 53 77 65 65 70 54 6F 4B 69 43 68 61 72 67 65 64 50 75 6E 63 68 41 62 69 6C 69 74 79),
00001584                         STR: 'CombatModifierAbility' (15 00 00 00 43 6F 6D 62 61 74 4D 6F 64 69 66 69 65 72 41 62 69 6C 69 74 79),
0000159E                         STR: 'KARATE_POWER_SWEEP_TO_KI_CHARGED_PUNCH_BLOCK_BOOST_DURATION' (3B 00 00 00 4B 41 52 41 54 45 5F 50 4F 57 45 52 5F 53 57 45 45 50 5F 54 4F 5F 4B 49 5F 43 48 41 52 47 45 44 5F 50 55 4E 43 48 5F 42 4C 4F 43 4B 5F 42 4F 4F 53 54 5F 44 55 52 41 54 49 4F 4E),
000015DE                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
000015EC                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
0000160A                         STR: 'msg' (03 00 00 00 6D 73 67),
00001612                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00001625                         STR: 'KARATE_POWER_SWEEP_TO_KI_CHARGED_PUNCH_DAMAGE' (2D 00 00 00 4B 41 52 41 54 45 5F 50 4F 57 45 52 5F 53 57 45 45 50 5F 54 4F 5F 4B 49 5F 43 48 41 52 47 45 44 5F 50 55 4E 43 48 5F 44 41 4D 41 47 45),
00001657                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
00001662                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
0000166E                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
0000168C                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00001698                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
000016B0                     TUPLE: (
000016B5                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000016C1                         STR: 'msg' (03 00 00 00 6D 73 67),
000016C9                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
000016D4                         STR: 'value' (05 00 00 00 76 61 6C 75 65),
000016DE                         STR: 'value2' (06 00 00 00 76 61 6C 75 65 32)
                             )
                         freevars:
000016E9                     TUPLE: ()
                         cellvars:
000016EE                     TUPLE: ()
                         filename:
000016F3                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_karate.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 6B 61 72 61 74 65 2E 70 79)
                         name:
0000174D                     STR: 'KaratePowerSweepToKiChargedPunch_DirectObject' (2D 00 00 00 4B 61 72 61 74 65 50 6F 77 65 72 53 77 65 65 70 54 6F 4B 69 43 68 61 72 67 65 64 50 75 6E 63 68 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
0000177F                     LONG: 138L (8A 00 00 00)
                         lnotab:
00001783                     STR: '\x00\x02\x0f\x01\t\x01\x0f\x01\t\x02\x12\x01\r\x01\x12\x01\r\x02\x18\x01' (14 00 00 00 00 02 0F 01 09 01 0F 01 09 02 12 01 0D 01 12 01 0D 02 18 01),
0000179C             CODE:
                         argcount:
0000179D                     LONG: 2L (02 00 00 00)
                         nlocals:
000017A1                     LONG: 3L (03 00 00 00)
                         stacksize:
000017A5                     LONG: 6L (06 00 00 00)
                         flags:
000017A9                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000017AD                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00t\x03\x00f\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x05\x00i\x06\x00|\x01\x00i\x08\x00t\x03\x00\x83\x02\x00}\x02\x00t\x00\x00i\n\x00t\x0b\x00t\x0c\x00|\x01\x00i\x08\x00|\x01\x00i\r\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (52 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 74 03 00 66 02 00 16 83 01 00 01 7C 00 00 69 05 00 69 06 00 7C 01 00 69 08 00 74 03 00 83 02 00 7D 02 00 74 00 00 69 0A 00 74 0B 00 74 0C 00 7C 01 00 69 08 00 7C 01 00 69 0D 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'KarateSkyHighSideKick: stunned for %d seconds and %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'KARATE_SKY_HIGH_SIDE_KICK_STUN_DURATION'
                             0000000C     74 - LOAD_GLOBAL         'KARATE_SKY_HIGH_SIDE_KICK_DAMAGE'
                             0000000F     66 - BUILD_TUPLE         r0002
                             00000012     16 - BINARY_MODULO       
                             00000013     83 - CALL_FUNCTION       r0001
                             00000016     01 - POP_TOP             
                             00000017     7C - LOAD_FAST           'subject'
                             0000001A     69 - LOAD_ATTR           'Interlock'
                             0000001D     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             00000020     7C - LOAD_FAST           'msg'
                             00000023     69 - LOAD_ATTR           'subjectLocator'
                             00000026     74 - LOAD_GLOBAL         'KARATE_SKY_HIGH_SIDE_KICK_DAMAGE'
                             00000029     83 - CALL_FUNCTION       r0002
                             0000002C     7D - STORE_FAST          'damage'
                             0000002F     74 - LOAD_GLOBAL         'Utility'
                             00000032     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             00000035     74 - LOAD_GLOBAL         'SUCCESS'
                             00000038     74 - LOAD_GLOBAL         'KarateSkyHighSideKickAbility'
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
00001804                     TUPLE: (
00001809                         None (4E),
0000180A                         STR: 'KarateSkyHighSideKick: stunned for %d seconds and %d damage dealt' (41 00 00 00 4B 61 72 61 74 65 53 6B 79 48 69 67 68 53 69 64 65 4B 69 63 6B 3A 20 73 74 75 6E 6E 65 64 20 66 6F 72 20 25 64 20 73 65 63 6F 6E 64 73 20 61 6E 64 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
00001850                     TUPLE: (
00001855                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00001861                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00001878                         STR: 'KARATE_SKY_HIGH_SIDE_KICK_STUN_DURATION' (27 00 00 00 4B 41 52 41 54 45 5F 53 4B 59 5F 48 49 47 48 5F 53 49 44 45 5F 4B 49 43 4B 5F 53 54 55 4E 5F 44 55 52 41 54 49 4F 4E),
000018A4                         STR: 'KARATE_SKY_HIGH_SIDE_KICK_DAMAGE' (20 00 00 00 4B 41 52 41 54 45 5F 53 4B 59 5F 48 49 47 48 5F 53 49 44 45 5F 4B 49 43 4B 5F 44 41 4D 41 47 45),
000018C9                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000018D5                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
000018E3                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00001901                         STR: 'msg' (03 00 00 00 6D 73 67),
00001909                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
0000191C                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
00001927                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00001945                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00001951                         STR: 'KarateSkyHighSideKickAbility' (1C 00 00 00 4B 61 72 61 74 65 53 6B 79 48 69 67 68 53 69 64 65 4B 69 63 6B 41 62 69 6C 69 74 79),
00001972                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
0000198A                     TUPLE: (
0000198F                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000199B                         STR: 'msg' (03 00 00 00 6D 73 67),
000019A3                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
000019AE                     TUPLE: ()
                         cellvars:
000019B3                     TUPLE: ()
                         filename:
000019B8                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_karate.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 6B 61 72 61 74 65 2E 70 79)
                         name:
00001A12                     STR: 'KarateSkyHighSideKick_DirectObject' (22 00 00 00 4B 61 72 61 74 65 53 6B 79 48 69 67 68 53 69 64 65 4B 69 63 6B 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00001A39                     LONG: 157L (9D 00 00 00)
                         lnotab:
00001A3D                     STR: '\x00\x01\x17\x01\x18\x01' (06 00 00 00 00 01 17 01 18 01),
00001A48             CODE:
                         argcount:
00001A49                     LONG: 2L (02 00 00 00)
                         nlocals:
00001A4D                     LONG: 3L (03 00 00 00)
                         stacksize:
00001A51                     LONG: 6L (06 00 00 00)
                         flags:
00001A55                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001A59                     STR: 't\x00\x00i\x01\x00d\x01\x00t\x02\x00t\x03\x00f\x02\x00\x16\x83\x01\x00\x01|\x00\x00i\x05\x00i\x06\x00|\x01\x00i\x08\x00t\t\x00\x83\x02\x00}\x02\x00t\x00\x00i\x0b\x00t\x0c\x00t\r\x00|\x01\x00i\x08\x00|\x01\x00i\x0e\x00|\x02\x00\x83\x05\x00\x01d\x00\x00S' (52 00 00 00 74 00 00 69 01 00 64 01 00 74 02 00 74 03 00 66 02 00 16 83 01 00 01 7C 00 00 69 05 00 69 06 00 7C 01 00 69 08 00 74 09 00 83 02 00 7D 02 00 74 00 00 69 0B 00 74 0C 00 74 0D 00 7C 01 00 69 08 00 7C 01 00 69 0E 00 7C 02 00 83 05 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'KarateSwirlingKiSummon: confused for %d seconds and %d damage dealt'
                             00000009     74 - LOAD_GLOBAL         'KARATE_SWIRLING_KI_SUMMON_DURATION'
                             0000000C     74 - LOAD_GLOBAL         'KKARATE_SWIRLING_KI_SUMMON_DAMAGE'
                             0000000F     66 - BUILD_TUPLE         r0002
                             00000012     16 - BINARY_MODULO       
                             00000013     83 - CALL_FUNCTION       r0001
                             00000016     01 - POP_TOP             
                             00000017     7C - LOAD_FAST           'subject'
                             0000001A     69 - LOAD_ATTR           'Interlock'
                             0000001D     69 - LOAD_ATTR           'physicalDamageFromAbility'
                             00000020     7C - LOAD_FAST           'msg'
                             00000023     69 - LOAD_ATTR           'subjectLocator'
                             00000026     74 - LOAD_GLOBAL         'KARATE_SWIRLING_KI_SUMMON__DAMAGE'
                             00000029     83 - CALL_FUNCTION       r0002
                             0000002C     7D - STORE_FAST          'damage'
                             0000002F     74 - LOAD_GLOBAL         'Utility'
                             00000032     69 - LOAD_ATTR           'SendTakeDamageResultToAll'
                             00000035     74 - LOAD_GLOBAL         'SUCCESS'
                             00000038     74 - LOAD_GLOBAL         'KarateSwirlingKiSummon'
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
00001AB0                     TUPLE: (
00001AB5                         None (4E),
00001AB6                         STR: 'KarateSwirlingKiSummon: confused for %d seconds and %d damage dealt' (43 00 00 00 4B 61 72 61 74 65 53 77 69 72 6C 69 6E 67 4B 69 53 75 6D 6D 6F 6E 3A 20 63 6F 6E 66 75 73 65 64 20 66 6F 72 20 25 64 20 73 65 63 6F 6E 64 73 20 61 6E 64 20 25 64 20 64 61 6D 61 67 65 20 64 65 61 6C 74)
                             )
                         names:
00001AFE                     TUPLE: (
00001B03                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00001B0F                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00001B26                         STR: 'KARATE_SWIRLING_KI_SUMMON_DURATION' (22 00 00 00 4B 41 52 41 54 45 5F 53 57 49 52 4C 49 4E 47 5F 4B 49 5F 53 55 4D 4D 4F 4E 5F 44 55 52 41 54 49 4F 4E),
00001B4D                         STR: 'KKARATE_SWIRLING_KI_SUMMON_DAMAGE' (21 00 00 00 4B 4B 41 52 41 54 45 5F 53 57 49 52 4C 49 4E 47 5F 4B 49 5F 53 55 4D 4D 4F 4E 5F 44 41 4D 41 47 45),
00001B73                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00001B7F                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
00001B8D                         STR: 'physicalDamageFromAbility' (19 00 00 00 70 68 79 73 69 63 61 6C 44 61 6D 61 67 65 46 72 6F 6D 41 62 69 6C 69 74 79),
00001BAB                         STR: 'msg' (03 00 00 00 6D 73 67),
00001BB3                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00001BC6                         STR: 'KARATE_SWIRLING_KI_SUMMON__DAMAGE' (21 00 00 00 4B 41 52 41 54 45 5F 53 57 49 52 4C 49 4E 47 5F 4B 49 5F 53 55 4D 4D 4F 4E 5F 5F 44 41 4D 41 47 45),
00001BEC                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
00001BF7                         STR: 'SendTakeDamageResultToAll' (19 00 00 00 53 65 6E 64 54 61 6B 65 44 61 6D 61 67 65 52 65 73 75 6C 74 54 6F 41 6C 6C),
00001C15                         STR: 'SUCCESS' (07 00 00 00 53 55 43 43 45 53 53),
00001C21                         STR: 'KarateSwirlingKiSummon' (16 00 00 00 4B 61 72 61 74 65 53 77 69 72 6C 69 6E 67 4B 69 53 75 6D 6D 6F 6E),
00001C3C                         STR: 'directObjectLocator' (13 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00001C54                     TUPLE: (
00001C59                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00001C65                         STR: 'msg' (03 00 00 00 6D 73 67),
00001C6D                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65)
                             )
                         freevars:
00001C78                     TUPLE: ()
                         cellvars:
00001C7D                     TUPLE: ()
                         filename:
00001C82                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_karate.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 6B 61 72 61 74 65 2E 70 79)
                         name:
00001CDC                     STR: 'KarateSwirlingKiSummon_DirectObject' (23 00 00 00 4B 61 72 61 74 65 53 77 69 72 6C 69 6E 67 4B 69 53 75 6D 6D 6F 6E 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00001D04                     LONG: 168L (A8 00 00 00)
                         lnotab:
00001D08                     STR: '\x00\x01\x17\x01\x18\x01' (06 00 00 00 00 01 17 01 18 01)
                 )
             names:
00001D13         TUPLE: (
00001D18             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00001D26             STR: 'obj' (03 00 00 00 6F 62 6A),
00001D2E             STR: 'ability.utility' (0F 00 00 00 61 62 69 6C 69 74 79 2E 75 74 69 6C 69 74 79),
00001D42             STR: 'utility' (07 00 00 00 75 74 69 6C 69 74 79),
00001D4E             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00001D5A             STR: 'ability.defines' (0F 00 00 00 61 62 69 6C 69 74 79 2E 64 65 66 69 6E 65 73),
00001D6E             STR: 'stringtable_client' (12 00 00 00 73 74 72 69 6E 67 74 61 62 6C 65 5F 63 6C 69 65 6E 74),
00001D85             STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00001D95             STR: 'KUNGFU_DIMMAK_STRIKE_DAMAGE' (1B 00 00 00 4B 55 4E 47 46 55 5F 44 49 4D 4D 41 4B 5F 53 54 52 49 4B 45 5F 44 41 4D 41 47 45),
00001DB5             STR: 'KARATE_GUARD_BREAKER_DAMAGE' (1B 00 00 00 4B 41 52 41 54 45 5F 47 55 41 52 44 5F 42 52 45 41 4B 45 52 5F 44 41 4D 41 47 45),
00001DD5             STR: 'KARATE_SWIRLING_KI_SUMMON_DAMAGE' (20 00 00 00 4B 41 52 41 54 45 5F 53 57 49 52 4C 49 4E 47 5F 4B 49 5F 53 55 4D 4D 4F 4E 5F 44 41 4D 41 47 45),
00001DFA             STR: 'KARATE_JUMP_SIDEKICK_DAMAGE' (1B 00 00 00 4B 41 52 41 54 45 5F 4A 55 4D 50 5F 53 49 44 45 4B 49 43 4B 5F 44 41 4D 41 47 45),
00001E1A             STR: 'KARATE_KI_CHARGED_REVERSE_PUNCH_DAMAGE' (26 00 00 00 4B 41 52 41 54 45 5F 4B 49 5F 43 48 41 52 47 45 44 5F 52 45 56 45 52 53 45 5F 50 55 4E 43 48 5F 44 41 4D 41 47 45),
00001E45             STR: 'KARATE_MACHINEGUN_KICK_DAMAGE' (1D 00 00 00 4B 41 52 41 54 45 5F 4D 41 43 48 49 4E 45 47 55 4E 5F 4B 49 43 4B 5F 44 41 4D 41 47 45),
00001E67             STR: 'KARATE_POWER_SWEEP_TO_KI_CHARGED_PUNCH_DAMAGE' (2D 00 00 00 4B 41 52 41 54 45 5F 50 4F 57 45 52 5F 53 57 45 45 50 5F 54 4F 5F 4B 49 5F 43 48 41 52 47 45 44 5F 50 55 4E 43 48 5F 44 41 4D 41 47 45),
00001E99             STR: 'KARATE_SKY_HIGH_SIDE_KICK_DAMAGE' (20 00 00 00 4B 41 52 41 54 45 5F 53 4B 59 5F 48 49 47 48 5F 53 49 44 45 5F 4B 49 43 4B 5F 44 41 4D 41 47 45),
00001EBE             STR: 'KARATE_BERSERKER_MODS_DURATION' (1E 00 00 00 4B 41 52 41 54 45 5F 42 45 52 53 45 52 4B 45 52 5F 4D 4F 44 53 5F 44 55 52 41 54 49 4F 4E),
00001EE1             STR: 'KARATE_GUARD_BREAKER_BLOCK_BOOST_DURATION' (29 00 00 00 4B 41 52 41 54 45 5F 47 55 41 52 44 5F 42 52 45 41 4B 45 52 5F 42 4C 4F 43 4B 5F 42 4F 4F 53 54 5F 44 55 52 41 54 49 4F 4E),
00001F0F             STR: 'KARATE_SKY_HIGH_SIDE_KICK_STUN_DURATION' (27 00 00 00 4B 41 52 41 54 45 5F 53 4B 59 5F 48 49 47 48 5F 53 49 44 45 5F 4B 49 43 4B 5F 53 54 55 4E 5F 44 55 52 41 54 49 4F 4E),
00001F3B             STR: 'KARATE_POWER_SWEEP_TO_KI_CHARGED_PUNCH_BLOCK_BOOST_DURATION' (3B 00 00 00 4B 41 52 41 54 45 5F 50 4F 57 45 52 5F 53 57 45 45 50 5F 54 4F 5F 4B 49 5F 43 48 41 52 47 45 44 5F 50 55 4E 43 48 5F 42 4C 4F 43 4B 5F 42 4F 4F 53 54 5F 44 55 52 41 54 49 4F 4E),
00001F7B             STR: 'KARATE_SWIRLING_KI_SUMMON_DURATION' (22 00 00 00 4B 41 52 41 54 45 5F 53 57 49 52 4C 49 4E 47 5F 4B 49 5F 53 55 4D 4D 4F 4E 5F 44 55 52 41 54 49 4F 4E),
00001FA2             STR: 'KARATE_BERSERKER_ATTACK_MOD' (1B 00 00 00 4B 41 52 41 54 45 5F 42 45 52 53 45 52 4B 45 52 5F 41 54 54 41 43 4B 5F 4D 4F 44),
00001FC2             STR: 'KARATE_BERSERKER_DEFENSE_MOD' (1C 00 00 00 4B 41 52 41 54 45 5F 42 45 52 53 45 52 4B 45 52 5F 44 45 46 45 4E 53 45 5F 4D 4F 44),
00001FE3             STR: 'KARATE_BERSERKER_DAMAGE_BONUS_MOD' (21 00 00 00 4B 41 52 41 54 45 5F 42 45 52 53 45 52 4B 45 52 5F 44 41 4D 41 47 45 5F 42 4F 4E 55 53 5F 4D 4F 44),
00002009             STR: 'KARATE_BERSERKER_LIFE_COST' (1A 00 00 00 4B 41 52 41 54 45 5F 42 45 52 53 45 52 4B 45 52 5F 4C 49 46 45 5F 43 4F 53 54),
00002028             STR: 'KARATE_GUARD_BREAKER_BLOCK_BOOST' (20 00 00 00 4B 41 52 41 54 45 5F 47 55 41 52 44 5F 42 52 45 41 4B 45 52 5F 42 4C 4F 43 4B 5F 42 4F 4F 53 54),
0000204D             STR: 'KARATE_POWER_SWEEP_TO_KI_CHARGED_PUNCH_BLOCK_BOOST' (32 00 00 00 4B 41 52 41 54 45 5F 50 4F 57 45 52 5F 53 57 45 45 50 5F 54 4F 5F 4B 49 5F 43 48 41 52 47 45 44 5F 50 55 4E 43 48 5F 42 4C 4F 43 4B 5F 42 4F 4F 53 54),
00002084             STR: 'KARATE_SWIRLING_KI_SUMMON_SPEED_EFFECT_MOD' (2A 00 00 00 4B 41 52 41 54 45 5F 53 57 49 52 4C 49 4E 47 5F 4B 49 5F 53 55 4D 4D 4F 4E 5F 53 50 45 45 44 5F 45 46 46 45 43 54 5F 4D 4F 44),
000020B3             STR: 'KARATE_SWIRLING_KI_SUMMON_SPEED_DEFENSE' (27 00 00 00 4B 41 52 41 54 45 5F 53 57 49 52 4C 49 4E 47 5F 4B 49 5F 53 55 4D 4D 4F 4E 5F 53 50 45 45 44 5F 44 45 46 45 4E 53 45),
000020DF             STR: 'KarateBerserkerAttack_Subject' (1D 00 00 00 4B 61 72 61 74 65 42 65 72 73 65 72 6B 65 72 41 74 74 61 63 6B 5F 53 75 62 6A 65 63 74),
00002101             STR: 'KarateBerserkerAttack_Test' (1A 00 00 00 4B 61 72 61 74 65 42 65 72 73 65 72 6B 65 72 41 74 74 61 63 6B 5F 54 65 73 74),
00002120             STR: 'BaseCombatSpecialMoveDepAttr' (1C 00 00 00 42 61 73 65 43 6F 6D 62 61 74 53 70 65 63 69 61 6C 4D 6F 76 65 44 65 70 41 74 74 72),
00002141             STR: 'depAttr' (07 00 00 00 64 65 70 41 74 74 72),
0000214D             STR: 'KarateGuardBreaker_DirectObject' (1F 00 00 00 4B 61 72 61 74 65 47 75 61 72 64 42 72 65 61 6B 65 72 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00002171             STR: 'KarateSidekickCombo_DirectObject' (20 00 00 00 4B 61 72 61 74 65 53 69 64 65 6B 69 63 6B 43 6F 6D 62 6F 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00002196             STR: 'KarateKiChargedReversePunch_DirectObject' (28 00 00 00 4B 61 72 61 74 65 4B 69 43 68 61 72 67 65 64 52 65 76 65 72 73 65 50 75 6E 63 68 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
000021C3             STR: 'KarateMachinegunKick_DirectObject' (21 00 00 00 4B 61 72 61 74 65 4D 61 63 68 69 6E 65 67 75 6E 4B 69 63 6B 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
000021E9             STR: 'KaratePowerSweepToKiChargedPunch_DirectObject' (2D 00 00 00 4B 61 72 61 74 65 50 6F 77 65 72 53 77 65 65 70 54 6F 4B 69 43 68 61 72 67 65 64 50 75 6E 63 68 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
0000221B             STR: 'KarateSkyHighSideKick_DirectObject' (22 00 00 00 4B 61 72 61 74 65 53 6B 79 48 69 67 68 53 69 64 65 4B 69 63 6B 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00002242             STR: 'KarateSwirlingKiSummon_DirectObject' (23 00 00 00 4B 61 72 61 74 65 53 77 69 72 6C 69 6E 67 4B 69 53 75 6D 6D 6F 6E 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                 )
             varnames:
0000226A         TUPLE: (
0000226F             STR: 'KARATE_BERSERKER_DAMAGE_BONUS_MOD' (21 00 00 00 4B 41 52 41 54 45 5F 42 45 52 53 45 52 4B 45 52 5F 44 41 4D 41 47 45 5F 42 4F 4E 55 53 5F 4D 4F 44),
00002295             STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
000022A5             STR: 'KARATE_SKY_HIGH_SIDE_KICK_DAMAGE' (20 00 00 00 4B 41 52 41 54 45 5F 53 4B 59 5F 48 49 47 48 5F 53 49 44 45 5F 4B 49 43 4B 5F 44 41 4D 41 47 45),
000022CA             STR: 'KARATE_BERSERKER_MODS_DURATION' (1E 00 00 00 4B 41 52 41 54 45 5F 42 45 52 53 45 52 4B 45 52 5F 4D 4F 44 53 5F 44 55 52 41 54 49 4F 4E),
000022ED             STR: 'KARATE_GUARD_BREAKER_BLOCK_BOOST_DURATION' (29 00 00 00 4B 41 52 41 54 45 5F 47 55 41 52 44 5F 42 52 45 41 4B 45 52 5F 42 4C 4F 43 4B 5F 42 4F 4F 53 54 5F 44 55 52 41 54 49 4F 4E),
0000231B             STR: 'KARATE_MACHINEGUN_KICK_DAMAGE' (1D 00 00 00 4B 41 52 41 54 45 5F 4D 41 43 48 49 4E 45 47 55 4E 5F 4B 49 43 4B 5F 44 41 4D 41 47 45),
0000233D             STR: 'KARATE_BERSERKER_ATTACK_MOD' (1B 00 00 00 4B 41 52 41 54 45 5F 42 45 52 53 45 52 4B 45 52 5F 41 54 54 41 43 4B 5F 4D 4F 44),
0000235D             STR: 'KARATE_GUARD_BREAKER_BLOCK_BOOST' (20 00 00 00 4B 41 52 41 54 45 5F 47 55 41 52 44 5F 42 52 45 41 4B 45 52 5F 42 4C 4F 43 4B 5F 42 4F 4F 53 54),
00002382             STR: 'KARATE_BERSERKER_DEFENSE_MOD' (1C 00 00 00 4B 41 52 41 54 45 5F 42 45 52 53 45 52 4B 45 52 5F 44 45 46 45 4E 53 45 5F 4D 4F 44),
000023A3             STR: 'KaratePowerSweepToKiChargedPunch_DirectObject' (2D 00 00 00 4B 61 72 61 74 65 50 6F 77 65 72 53 77 65 65 70 54 6F 4B 69 43 68 61 72 67 65 64 50 75 6E 63 68 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
000023D5             STR: 'KARATE_POWER_SWEEP_TO_KI_CHARGED_PUNCH_DAMAGE' (2D 00 00 00 4B 41 52 41 54 45 5F 50 4F 57 45 52 5F 53 57 45 45 50 5F 54 4F 5F 4B 49 5F 43 48 41 52 47 45 44 5F 50 55 4E 43 48 5F 44 41 4D 41 47 45),
00002407             STR: 'KarateBerserkerAttack_Subject' (1D 00 00 00 4B 61 72 61 74 65 42 65 72 73 65 72 6B 65 72 41 74 74 61 63 6B 5F 53 75 62 6A 65 63 74),
00002429             STR: 'KarateBerserkerAttack_Test' (1A 00 00 00 4B 61 72 61 74 65 42 65 72 73 65 72 6B 65 72 41 74 74 61 63 6B 5F 54 65 73 74),
00002448             STR: 'KARATE_SWIRLING_KI_SUMMON_DURATION' (22 00 00 00 4B 41 52 41 54 45 5F 53 57 49 52 4C 49 4E 47 5F 4B 49 5F 53 55 4D 4D 4F 4E 5F 44 55 52 41 54 49 4F 4E),
0000246F             STR: 'KARATE_BERSERKER_LIFE_COST' (1A 00 00 00 4B 41 52 41 54 45 5F 42 45 52 53 45 52 4B 45 52 5F 4C 49 46 45 5F 43 4F 53 54),
0000248E             STR: 'KARATE_POWER_SWEEP_TO_KI_CHARGED_PUNCH_BLOCK_BOOST_DURATION' (3B 00 00 00 4B 41 52 41 54 45 5F 50 4F 57 45 52 5F 53 57 45 45 50 5F 54 4F 5F 4B 49 5F 43 48 41 52 47 45 44 5F 50 55 4E 43 48 5F 42 4C 4F 43 4B 5F 42 4F 4F 53 54 5F 44 55 52 41 54 49 4F 4E),
000024CE             STR: 'KarateSidekickCombo_DirectObject' (20 00 00 00 4B 61 72 61 74 65 53 69 64 65 6B 69 63 6B 43 6F 6D 62 6F 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
000024F3             STR: 'KARATE_SWIRLING_KI_SUMMON_SPEED_EFFECT_MOD' (2A 00 00 00 4B 41 52 41 54 45 5F 53 57 49 52 4C 49 4E 47 5F 4B 49 5F 53 55 4D 4D 4F 4E 5F 53 50 45 45 44 5F 45 46 46 45 43 54 5F 4D 4F 44),
00002522             STR: 'KarateKiChargedReversePunch_DirectObject' (28 00 00 00 4B 61 72 61 74 65 4B 69 43 68 61 72 67 65 64 52 65 76 65 72 73 65 50 75 6E 63 68 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
0000254F             STR: 'KARATE_POWER_SWEEP_TO_KI_CHARGED_PUNCH_BLOCK_BOOST' (32 00 00 00 4B 41 52 41 54 45 5F 50 4F 57 45 52 5F 53 57 45 45 50 5F 54 4F 5F 4B 49 5F 43 48 41 52 47 45 44 5F 50 55 4E 43 48 5F 42 4C 4F 43 4B 5F 42 4F 4F 53 54),
00002586             STR: 'KARATE_SWIRLING_KI_SUMMON_SPEED_DEFENSE' (27 00 00 00 4B 41 52 41 54 45 5F 53 57 49 52 4C 49 4E 47 5F 4B 49 5F 53 55 4D 4D 4F 4E 5F 53 50 45 45 44 5F 44 45 46 45 4E 53 45),
000025B2             STR: 'KARATE_GUARD_BREAKER_DAMAGE' (1B 00 00 00 4B 41 52 41 54 45 5F 47 55 41 52 44 5F 42 52 45 41 4B 45 52 5F 44 41 4D 41 47 45),
000025D2             STR: 'KarateMachinegunKick_DirectObject' (21 00 00 00 4B 61 72 61 74 65 4D 61 63 68 69 6E 65 67 75 6E 4B 69 63 6B 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
000025F8             STR: 'KarateSkyHighSideKick_DirectObject' (22 00 00 00 4B 61 72 61 74 65 53 6B 79 48 69 67 68 53 69 64 65 4B 69 63 6B 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
0000261F             STR: 'KARATE_JUMP_SIDEKICK_DAMAGE' (1B 00 00 00 4B 41 52 41 54 45 5F 4A 55 4D 50 5F 53 49 44 45 4B 49 43 4B 5F 44 41 4D 41 47 45),
0000263F             STR: 'KARATE_KI_CHARGED_REVERSE_PUNCH_DAMAGE' (26 00 00 00 4B 41 52 41 54 45 5F 4B 49 5F 43 48 41 52 47 45 44 5F 52 45 56 45 52 53 45 5F 50 55 4E 43 48 5F 44 41 4D 41 47 45),
0000266A             STR: 'obj' (03 00 00 00 6F 62 6A),
00002672             STR: 'KUNGFU_DIMMAK_STRIKE_DAMAGE' (1B 00 00 00 4B 55 4E 47 46 55 5F 44 49 4D 4D 41 4B 5F 53 54 52 49 4B 45 5F 44 41 4D 41 47 45),
00002692             STR: 'KARATE_SKY_HIGH_SIDE_KICK_STUN_DURATION' (27 00 00 00 4B 41 52 41 54 45 5F 53 4B 59 5F 48 49 47 48 5F 53 49 44 45 5F 4B 49 43 4B 5F 53 54 55 4E 5F 44 55 52 41 54 49 4F 4E),
000026BE             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
000026CC             STR: 'KarateSwirlingKiSummon_DirectObject' (23 00 00 00 4B 61 72 61 74 65 53 77 69 72 6C 69 6E 67 4B 69 53 75 6D 6D 6F 6E 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
000026F4             STR: 'KarateGuardBreaker_DirectObject' (1F 00 00 00 4B 61 72 61 74 65 47 75 61 72 64 42 72 65 61 6B 65 72 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00002718             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00002724             STR: 'KARATE_SWIRLING_KI_SUMMON_DAMAGE' (20 00 00 00 4B 41 52 41 54 45 5F 53 57 49 52 4C 49 4E 47 5F 4B 49 5F 53 55 4D 4D 4F 4E 5F 44 41 4D 41 47 45)
                 )
             freevars:
00002749         TUPLE: ()
             cellvars:
0000274E         TUPLE: ()
             filename:
00002753         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\soldier\\old_sm_karate.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 73 6F 6C 64 69 65 72 5C 6F 6C 64 5F 73 6D 5F 6B 61 72 61 74 65 2E 70 79)
             name:
000027AD         STR: '?' (01 00 00 00 3F)
             firslineno:
000027B3         LONG: 1L (01 00 00 00)
             lnotab:
000027B7         STR: '\t\x01\t\x01\x0c\x03\x07\x01\t\x06\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x05\x06\x01\x06\x01\x06\x01\x06\x01\x06\x05\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x06\t\x1b\t\x07\x0c\x06\t\x15\t\t\t\t\t\x0c\t\x13\t\x0b' (46 00 00 00 09 01 09 01 0C 03 07 01 09 06 06 01 06 01 06 01 06 01 06 01 06 01 06 01 06 05 06 01 06 01 06 01 06 01 06 05 06 01 06 01 06 01 06 01 06 01 06 01 06 01 06 06 09 1B 09 07 0C 06 09 15 09 09 09 09 09 0C 09 13 09 0B)

