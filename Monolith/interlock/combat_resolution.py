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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00Z\x02\x00d\x00\x00k\x03\x00Z\x04\x00d\x00\x00k\x05\x00Z\x05\x00d\x00\x00k\x06\x00Z\x07\x00d\x00\x00k\x08\x00Z\t\x00d\x00\x00k\n\x00Z\x0b\x00d\x01\x00\x84\x00\x00Z\x0c\x00d\x02\x00\x84\x00\x00Z\r\x00d\x03\x00\x84\x00\x00Z\x0e\x00d\x04\x00\x84\x00\x00Z\x0f\x00d\x05\x00\x84\x00\x00Z\x10\x00d\x06\x00\x84\x00\x00Z\x11\x00d\x07\x00\x84\x00\x00Z\x12\x00d\x08\x00\x84\x00\x00Z\x13\x00d\t\x00\x84\x00\x00Z\x14\x00d\n\x00\x84\x00\x00Z\x15\x00d\x0b\x00\x84\x00\x00Z\x16\x00d\x0c\x00\x84\x00\x00Z\x17\x00d\r\x00\x84\x00\x00Z\x18\x00d\x0e\x00\x84\x00\x00Z\x19\x00d\x0f\x00\x84\x00\x00Z\x1a\x00d\x10\x00\x84\x00\x00Z\x1b\x00d\x11\x00\x84\x00\x00Z\x1c\x00d\x00\x00S' (E5 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 5A 02 00 64 00 00 6B 03 00 5A 04 00 64 00 00 6B 05 00 5A 05 00 64 00 00 6B 06 00 5A 07 00 64 00 00 6B 08 00 5A 09 00 64 00 00 6B 0A 00 5A 0B 00 64 01 00 84 00 00 5A 0C 00 64 02 00 84 00 00 5A 0D 00 64 03 00 84 00 00 5A 0E 00 64 04 00 84 00 00 5A 0F 00 64 05 00 84 00 00 5A 10 00 64 06 00 84 00 00 5A 11 00 64 07 00 84 00 00 5A 12 00 64 08 00 84 00 00 5A 13 00 64 09 00 84 00 00 5A 14 00 64 0A 00 84 00 00 5A 15 00 64 0B 00 84 00 00 5A 16 00 64 0C 00 84 00 00 5A 17 00 64 0D 00 84 00 00 5A 18 00 64 0E 00 84 00 00 5A 19 00 64 0F 00 84 00 00 5A 1A 00 64 10 00 84 00 00 5A 1B 00 64 11 00 84 00 00 5A 1C 00 64 00 00 53)
                 00000000     64 - LOAD_CONST          None
                 00000003     6B - IMPORT_NAME         'random'
                 00000006     5A - STORE_NAME          'random'
                 00000009     64 - LOAD_CONST          None
                 0000000C     6B - IMPORT_NAME         'traceback'
                 0000000F     5A - STORE_NAME          'traceback'
                 00000012     64 - LOAD_CONST          None
                 00000015     6B - IMPORT_NAME         'obj'
                 00000018     5A - STORE_NAME          'obj'
                 0000001B     64 - LOAD_CONST          None
                 0000001E     6B - IMPORT_NAME         'combat_defines'
                 00000021     5A - STORE_NAME          'CD'
                 00000024     64 - LOAD_CONST          None
                 00000027     6B - IMPORT_NAME         'math'
                 0000002A     5A - STORE_NAME          'math'
                 0000002D     64 - LOAD_CONST          None
                 00000030     6B - IMPORT_NAME         'combat_utility'
                 00000033     5A - STORE_NAME          'CU'
                 00000036     64 - LOAD_CONST          None
                 00000039     6B - IMPORT_NAME         'combat_modifiers'
                 0000003C     5A - STORE_NAME          'Mods'
                 0000003F     64 - LOAD_CONST          None
                 00000042     6B - IMPORT_NAME         'combat_calculations'
                 00000045     5A - STORE_NAME          'CC'
                 00000048     64 - LOAD_CONST          CODE('generateVulnerabilities')
                 0000004B     84 - MAKE_FUNCTION       r0000
                 0000004E     5A - STORE_NAME          'generateVulnerabilities'
                 00000051     64 - LOAD_CONST          CODE('generateExploits')
                 00000054     84 - MAKE_FUNCTION       r0000
                 00000057     5A - STORE_NAME          'generateExploits'
                 0000005A     64 - LOAD_CONST          CODE('generateExploitsForPlayers')
                 0000005D     84 - MAKE_FUNCTION       r0000
                 00000060     5A - STORE_NAME          'generateExploitsForPlayers'
                 00000063     64 - LOAD_CONST          CODE('isAbilityMartialArt')
                 00000066     84 - MAKE_FUNCTION       r0000
                 00000069     5A - STORE_NAME          'isAbilityMartialArt'
                 0000006C     64 - LOAD_CONST          CODE('calcDamageForLoser')
                 0000006F     84 - MAKE_FUNCTION       r0000
                 00000072     5A - STORE_NAME          'calcDamageForLoser'
                 00000075     64 - LOAD_CONST          CODE('calculateDamage')
                 00000078     84 - MAKE_FUNCTION       r0000
                 0000007B     5A - STORE_NAME          'calculateDamage'
                 0000007E     64 - LOAD_CONST          CODE('determineAttacker')
                 00000081     84 - MAKE_FUNCTION       r0000
                 00000084     5A - STORE_NAME          'determineAttacker'
                 00000087     64 - LOAD_CONST          CODE('handleSpecialMove')
                 0000008A     84 - MAKE_FUNCTION       r0000
                 0000008D     5A - STORE_NAME          'handleSpecialMove'
                 00000090     64 - LOAD_CONST          CODE('handleOppertunityAttack')
                 00000093     84 - MAKE_FUNCTION       r0000
                 00000096     5A - STORE_NAME          'handleOppertunityAttack'
                 00000099     64 - LOAD_CONST          CODE('handleStandardExchange')
                 0000009C     84 - MAKE_FUNCTION       r0000
                 0000009F     5A - STORE_NAME          'handleStandardExchange'
                 000000A2     64 - LOAD_CONST          CODE('handleBlock')
                 000000A5     84 - MAKE_FUNCTION       r0000
                 000000A8     5A - STORE_NAME          'handleBlock'
                 000000AB     64 - LOAD_CONST          CODE('GetCorrectDefenseBonus')
                 000000AE     84 - MAKE_FUNCTION       r0000
                 000000B1     5A - STORE_NAME          'GetCorrectDefenseBonus'
                 000000B4     64 - LOAD_CONST          CODE('getCorrectDTTotals')
                 000000B7     84 - MAKE_FUNCTION       r0000
                 000000BA     5A - STORE_NAME          'getCorrectDTTotals'
                 000000BD     64 - LOAD_CONST          CODE('getCTandDTotals')
                 000000C0     84 - MAKE_FUNCTION       r0000
                 000000C3     5A - STORE_NAME          'getCTandDTotals'
                 000000C6     64 - LOAD_CONST          CODE('FlipAtkDef')
                 000000C9     84 - MAKE_FUNCTION       r0000
                 000000CC     5A - STORE_NAME          'FlipAtkDef'
                 000000CF     64 - LOAD_CONST          CODE('determineResultForStandardCombat')
                 000000D2     84 - MAKE_FUNCTION       r0000
                 000000D5     5A - STORE_NAME          'determineResultForStandardCombat'
                 000000D8     64 - LOAD_CONST          CODE('determineResultOfWithdrawalRequest')
                 000000DB     84 - MAKE_FUNCTION       r0000
                 000000DE     5A - STORE_NAME          'determineResultOfWithdrawalRequest'
                 000000E1     64 - LOAD_CONST          None
                 000000E4     53 - RETURN_VALUE        
             consts:
00000103         TUPLE: (
00000108             None (4E),
00000109             CODE:
                         argcount:
0000010A                     LONG: 1L (01 00 00 00)
                         nlocals:
0000010E                     LONG: 6L (06 00 00 00)
                         stacksize:
00000112                     LONG: 6L (06 00 00 00)
                         flags:
00000116                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000011A                     STR: 't\x00\x00i\x01\x00d\x01\x00j\x02\x00o\x08\x00\x01d\x00\x00Sn\x01\x00\x01t\x02\x00|\x00\x00i\x04\x00\x83\x01\x00\x0bd\x02\x00\x15}\x03\x00d\x03\x00}\x04\x00d\x04\x00}\x02\x00|\x00\x00i\x08\x00t\t\x00i\n\x00i\x0b\x00j\x02\x00o\x17\x00\x01t\x02\x00|\x00\x00i\x0c\x00\x83\x01\x00d\x02\x00\x15}\x02\x00n[\x00\x01|\x00\x00i\x08\x00t\t\x00i\n\x00i\r\x00j\x02\x00o\x17\x00\x01t\x02\x00|\x00\x00i\x0e\x00\x83\x01\x00d\x02\x00\x15}\x02\x00n.\x00\x01|\x00\x00i\x08\x00t\t\x00i\n\x00i\x0f\x00j\x02\x00o\x17\x00\x01t\x02\x00|\x00\x00i\x10\x00\x83\x01\x00d\x02\x00\x15}\x02\x00n\x01\x00\x01|\x04\x00|\x03\x00\x17|\x02\x00\x17}\x01\x00t\x12\x00i\x13\x00d\x05\x00|\x04\x00|\x03\x00|\x02\x00|\x01\x00f\x04\x00\x16d\x06\x00\x83\x02\x00\x01|\x00\x00i\x14\x00o"\x00\x01|\x01\x00d\x07\x009}\x01\x00t\x12\x00i\x13\x00d\x08\x00|\x01\x00\x16d\x06\x00\x83\x02\x00\x01n\x01\x00\x01t\x15\x00i\x16\x00d\t\x00d\n\x00\x83\x02\x00}\x05\x00t\x12\x00i\x13\x00d\x0b\x00|\x05\x00|\x01\x00f\x02\x00\x16d\x06\x00\x83\x02\x00\x01|\x05\x00|\x01\x00d\n\x00\x14j\x04\x00o\x86\x00\x01|\x00\x00i\x08\x00t\t\x00i\n\x00i\x0b\x00j\x02\x00o\x14\x00\x01|\x00\x00i\x0c\x00d\x0c\x00\x17|\x00\x00_\x0c\x00nU\x00\x01|\x00\x00i\x08\x00t\t\x00i\n\x00i\r\x00j\x02\x00o\x14\x00\x01|\x00\x00i\x0e\x00d\x0c\x00\x17|\x00\x00_\x0e\x00n+\x00\x01|\x00\x00i\x08\x00t\t\x00i\n\x00i\x0f\x00j\x02\x00o\x14\x00\x01|\x00\x00i\x10\x00d\x0c\x00\x17|\x00\x00_\x10\x00n\x01\x00\x01d\x00\x00Sn\x01\x00\x01|\x00\x00i\x08\x00t\t\x00i\n\x00i\x0b\x00j\x02\x00o\x16\x00\x01d\t\x00|\x00\x00_\x18\x00d\x01\x00|\x00\x00_\x0c\x00nY\x00\x01|\x00\x00i\x08\x00t\t\x00i\n\x00i\r\x00j\x02\x00o\x16\x00\x01d\t\x00|\x00\x00_\x19\x00d\x01\x00|\x00\x00_\x0e\x00n-\x00\x01|\x00\x00i\x08\x00t\t\x00i\n\x00i\x0f\x00j\x02\x00o\x16\x00\x01d\t\x00|\x00\x00_\x1a\x00d\x01\x00|\x00\x00_\x10\x00n\x01\x00\x01t\x15\x00i\x16\x00d\t\x00d\n\x00\x83\x02\x00}\x05\x00|\x05\x00d\r\x00j\x00\x00o\r\x00\x01d\x0e\x00|\x00\x00_\x1b\x00n>\x00\x01|\x05\x00d\x0f\x00j\x00\x00o\r\x00\x01d\x10\x00|\x00\x00_\x1b\x00n$\x00\x01|\x05\x00d\x11\x00j\x00\x00o\r\x00\x01d\x0c\x00|\x00\x00_\x1b\x00n\n\x00\x01d\x12\x00|\x00\x00_\x1b\x00d\x00\x00S' (CD 02 00 00 74 00 00 69 01 00 64 01 00 6A 02 00 6F 08 00 01 64 00 00 53 6E 01 00 01 74 02 00 7C 00 00 69 04 00 83 01 00 0B 64 02 00 15 7D 03 00 64 03 00 7D 04 00 64 04 00 7D 02 00 7C 00 00 69 08 00 74 09 00 69 0A 00 69 0B 00 6A 02 00 6F 17 00 01 74 02 00 7C 00 00 69 0C 00 83 01 00 64 02 00 15 7D 02 00 6E 5B 00 01 7C 00 00 69 08 00 74 09 00 69 0A 00 69 0D 00 6A 02 00 6F 17 00 01 74 02 00 7C 00 00 69 0E 00 83 01 00 64 02 00 15 7D 02 00 6E 2E 00 01 7C 00 00 69 08 00 74 09 00 69 0A 00 69 0F 00 6A 02 00 6F 17 00 01 74 02 00 7C 00 00 69 10 00 83 01 00 64 02 00 15 7D 02 00 6E 01 00 01 7C 04 00 7C 03 00 17 7C 02 00 17 7D 01 00 74 12 00 69 13 00 64 05 00 7C 04 00 7C 03 00 7C 02 00 7C 01 00 66 04 00 16 64 06 00 83 02 00 01 7C 00 00 69 14 00 6F 22 00 01 7C 01 00 64 07 00 39 7D 01 00 74 12 00 69 13 00 64 08 00 7C 01 00 16 64 06 00 83 02 00 01 6E 01 00 01 74 15 00 69 16 00 64 09 00 64 0A 00 83 02 00 7D 05 00 74 12 00 69 13 00 64 0B 00 7C 05 00 7C 01 00 66 02 00 16 64 06 00 83 02 00 01 7C 05 00 7C 01 00 64 0A 00 14 6A 04 00 6F 86 00 01 7C 00 00 69 08 00 74 09 00 69 0A 00 69 0B 00 6A 02 00 6F 14 00 01 7C 00 00 69 0C 00 64 0C 00 17 7C 00 00 5F 0C 00 6E 55 00 01 7C 00 00 69 08 00 74 09 00 69 0A 00 69 0D 00 6A 02 00 6F 14 00 01 7C 00 00 69 0E 00 64 0C 00 17 7C 00 00 5F 0E 00 6E 2B 00 01 7C 00 00 69 08 00 74 09 00 69 0A 00 69 0F 00 6A 02 00 6F 14 00 01 7C 00 00 69 10 00 64 0C 00 17 7C 00 00 5F 10 00 6E 01 00 01 64 00 00 53 6E 01 00 01 7C 00 00 69 08 00 74 09 00 69 0A 00 69 0B 00 6A 02 00 6F 16 00 01 64 09 00 7C 00 00 5F 18 00 64 01 00 7C 00 00 5F 0C 00 6E 59 00 01 7C 00 00 69 08 00 74 09 00 69 0A 00 69 0D 00 6A 02 00 6F 16 00 01 64 09 00 7C 00 00 5F 19 00 64 01 00 7C 00 00 5F 0E 00 6E 2D 00 01 7C 00 00 69 08 00 74 09 00 69 0A 00 69 0F 00 6A 02 00 6F 16 00 01 64 09 00 7C 00 00 5F 1A 00 64 01 00 7C 00 00 5F 10 00 6E 01 00 01 74 15 00 69 16 00 64 09 00 64 0A 00 83 02 00 7D 05 00 7C 05 00 64 0D 00 6A 00 00 6F 0D 00 01 64 0E 00 7C 00 00 5F 1B 00 6E 3E 00 01 7C 05 00 64 0F 00 6A 00 00 6F 0D 00 01 64 10 00 7C 00 00 5F 1B 00 6E 24 00 01 7C 05 00 64 11 00 6A 00 00 6F 0D 00 01 64 0C 00 7C 00 00 5F 1B 00 6E 0A 00 01 64 12 00 7C 00 00 5F 1B 00 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consolevar'
                             00000003     69 - LOAD_ATTR           'CombatTacticVulner'
                             00000006     64 - LOAD_CONST          0
                             00000009     6A - COMPARE_OP          "=="
                             0000000C     6F - JUMP_IF_FALSE       -> 00000017
                             0000000F     01 - POP_TOP             
                             00000010     64 - LOAD_CONST          None
                             00000013     53 - RETURN_VALUE        
                             00000014     6E - JUMP_FORWARD        -> 00000018
                             00000017     01 - POP_TOP             
                             00000018     74 - LOAD_GLOBAL         'float'
                             0000001B     7C - LOAD_FAST           'player'
                             0000001E     69 - LOAD_ATTR           'vulnerabilityGenerationBonus'
                             00000021     83 - CALL_FUNCTION       r0001
                             00000024     0B - UNARY_NEGATIVE      
                             00000025     64 - LOAD_CONST          100.0
                             00000028     15 - BINARY_DIVIDE       
                             00000029     7D - STORE_FAST          'vulnerabilityPercentModifier'
                             0000002C     64 - LOAD_CONST          0.20000000000000001
                             0000002F     7D - STORE_FAST          'vulnerabilityBase'
                             00000032     64 - LOAD_CONST          0.0
                             00000035     7D - STORE_FAST          'vulnerabilityTactic'
                             00000038     7C - LOAD_FAST           'player'
                             0000003B     69 - LOAD_ATTR           'tacticalSetting'
                             0000003E     74 - LOAD_GLOBAL         'constants'
                             00000041     69 - LOAD_ATTR           'combat'
                             00000044     69 - LOAD_ATTR           'POWER'
                             00000047     6A - COMPARE_OP          "=="
                             0000004A     6F - JUMP_IF_FALSE       -> 00000064
                             0000004D     01 - POP_TOP             
                             0000004E     74 - LOAD_GLOBAL         'float'
                             00000051     7C - LOAD_FAST           'player'
                             00000054     69 - LOAD_ATTR           'vuln_speed_chance'
                             00000057     83 - CALL_FUNCTION       r0001
                             0000005A     64 - LOAD_CONST          100.0
                             0000005D     15 - BINARY_DIVIDE       
                             0000005E     7D - STORE_FAST          'vulnerabilityTactic'
                             00000061     6E - JUMP_FORWARD        -> 000000BF
                             00000064     01 - POP_TOP             
                             00000065     7C - LOAD_FAST           'player'
                             00000068     69 - LOAD_ATTR           'tacticalSetting'
                             0000006B     74 - LOAD_GLOBAL         'constants'
                             0000006E     69 - LOAD_ATTR           'combat'
                             00000071     69 - LOAD_ATTR           'DEFENSE'
                             00000074     6A - COMPARE_OP          "=="
                             00000077     6F - JUMP_IF_FALSE       -> 00000091
                             0000007A     01 - POP_TOP             
                             0000007B     74 - LOAD_GLOBAL         'float'
                             0000007E     7C - LOAD_FAST           'player'
                             00000081     69 - LOAD_ATTR           'vuln_power_chance'
                             00000084     83 - CALL_FUNCTION       r0001
                             00000087     64 - LOAD_CONST          100.0
                             0000008A     15 - BINARY_DIVIDE       
                             0000008B     7D - STORE_FAST          'vulnerabilityTactic'
                             0000008E     6E - JUMP_FORWARD        -> 000000BF
                             00000091     01 - POP_TOP             
                             00000092     7C - LOAD_FAST           'player'
                             00000095     69 - LOAD_ATTR           'tacticalSetting'
                             00000098     74 - LOAD_GLOBAL         'constants'
                             0000009B     69 - LOAD_ATTR           'combat'
                             0000009E     69 - LOAD_ATTR           'SPEED'
                             000000A1     6A - COMPARE_OP          "=="
                             000000A4     6F - JUMP_IF_FALSE       -> 000000BE
                             000000A7     01 - POP_TOP             
                             000000A8     74 - LOAD_GLOBAL         'float'
                             000000AB     7C - LOAD_FAST           'player'
                             000000AE     69 - LOAD_ATTR           'vuln_defense_chance'
                             000000B1     83 - CALL_FUNCTION       r0001
                             000000B4     64 - LOAD_CONST          100.0
                             000000B7     15 - BINARY_DIVIDE       
                             000000B8     7D - STORE_FAST          'vulnerabilityTactic'
                             000000BB     6E - JUMP_FORWARD        -> 000000BF
                             000000BE     01 - POP_TOP             
                             000000BF     7C - LOAD_FAST           'vulnerabilityBase'
                             000000C2     7C - LOAD_FAST           'vulnerabilityPercentModifier'
                             000000C5     17 - BINARY_ADD          
                             000000C6     7C - LOAD_FAST           'vulnerabilityTactic'
                             000000C9     17 - BINARY_ADD          
                             000000CA     7D - STORE_FAST          'vulnerability'
                             000000CD     74 - LOAD_GLOBAL         'CU'
                             000000D0     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             000000D3     64 - LOAD_CONST          'vulnerability percent: %gBase + %gBonus +%gTacticChange = %g'
                             000000D6     7C - LOAD_FAST           'vulnerabilityBase'
                             000000D9     7C - LOAD_FAST           'vulnerabilityPercentModifier'
                             000000DC     7C - LOAD_FAST           'vulnerabilityTactic'
                             000000DF     7C - LOAD_FAST           'vulnerability'
                             000000E2     66 - BUILD_TUPLE         r0004
                             000000E5     16 - BINARY_MODULO       
                             000000E6     64 - LOAD_CONST          11
                             000000E9     83 - CALL_FUNCTION       r0002
                             000000EC     01 - POP_TOP             
                             000000ED     7C - LOAD_FAST           'player'
                             000000F0     69 - LOAD_ATTR           'isEnergizedTactic'
                             000000F3     6F - JUMP_IF_FALSE       -> 00000118
                             000000F6     01 - POP_TOP             
                             000000F7     7C - LOAD_FAST           'vulnerability'
                             000000FA     64 - LOAD_CONST          1.5
                             000000FD     39 - INPLACE_MULTIPLY    
                             000000FE     7D - STORE_FAST          'vulnerability'
                             00000101     74 - LOAD_GLOBAL         'CU'
                             00000104     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000107     64 - LOAD_CONST          'vulnerability doubled from energized tactic to %g'
                             0000010A     7C - LOAD_FAST           'vulnerability'
                             0000010D     16 - BINARY_MODULO       
                             0000010E     64 - LOAD_CONST          11
                             00000111     83 - CALL_FUNCTION       r0002
                             00000114     01 - POP_TOP             
                             00000115     6E - JUMP_FORWARD        -> 00000119
                             00000118     01 - POP_TOP             
                             00000119     74 - LOAD_GLOBAL         'random'
                             0000011C     69 - LOAD_ATTR           'randrange'
                             0000011F     64 - LOAD_CONST          1
                             00000122     64 - LOAD_CONST          100
                             00000125     83 - CALL_FUNCTION       r0002
                             00000128     7D - STORE_FAST          'roll'
                             0000012B     74 - LOAD_GLOBAL         'CU'
                             0000012E     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000131     64 - LOAD_CONST          'vulnerability check: %d %f'
                             00000134     7C - LOAD_FAST           'roll'
                             00000137     7C - LOAD_FAST           'vulnerability'
                             0000013A     66 - BUILD_TUPLE         r0002
                             0000013D     16 - BINARY_MODULO       
                             0000013E     64 - LOAD_CONST          11
                             00000141     83 - CALL_FUNCTION       r0002
                             00000144     01 - POP_TOP             
                             00000145     7C - LOAD_FAST           'roll'
                             00000148     7C - LOAD_FAST           'vulnerability'
                             0000014B     64 - LOAD_CONST          100
                             0000014E     14 - BINARY_MULTIPLY     
                             0000014F     6A - COMPARE_OP          ">"
                             00000152     6F - JUMP_IF_FALSE       -> 000001DB
                             00000155     01 - POP_TOP             
                             00000156     7C - LOAD_FAST           'player'
                             00000159     69 - LOAD_ATTR           'tacticalSetting'
                             0000015C     74 - LOAD_GLOBAL         'constants'
                             0000015F     69 - LOAD_ATTR           'combat'
                             00000162     69 - LOAD_ATTR           'POWER'
                             00000165     6A - COMPARE_OP          "=="
                             00000168     6F - JUMP_IF_FALSE       -> 0000017F
                             0000016B     01 - POP_TOP             
                             0000016C     7C - LOAD_FAST           'player'
                             0000016F     69 - LOAD_ATTR           'vuln_speed_chance'
                             00000172     64 - LOAD_CONST          5
                             00000175     17 - BINARY_ADD          
                             00000176     7C - LOAD_FAST           'player'
                             00000179     5F - STORE_ATTR          'vuln_speed_chance'
                             0000017C     6E - JUMP_FORWARD        -> 000001D4
                             0000017F     01 - POP_TOP             
                             00000180     7C - LOAD_FAST           'player'
                             00000183     69 - LOAD_ATTR           'tacticalSetting'
                             00000186     74 - LOAD_GLOBAL         'constants'
                             00000189     69 - LOAD_ATTR           'combat'
                             0000018C     69 - LOAD_ATTR           'DEFENSE'
                             0000018F     6A - COMPARE_OP          "=="
                             00000192     6F - JUMP_IF_FALSE       -> 000001A9
                             00000195     01 - POP_TOP             
                             00000196     7C - LOAD_FAST           'player'
                             00000199     69 - LOAD_ATTR           'vuln_power_chance'
                             0000019C     64 - LOAD_CONST          5
                             0000019F     17 - BINARY_ADD          
                             000001A0     7C - LOAD_FAST           'player'
                             000001A3     5F - STORE_ATTR          'vuln_power_chance'
                             000001A6     6E - JUMP_FORWARD        -> 000001D4
                             000001A9     01 - POP_TOP             
                             000001AA     7C - LOAD_FAST           'player'
                             000001AD     69 - LOAD_ATTR           'tacticalSetting'
                             000001B0     74 - LOAD_GLOBAL         'constants'
                             000001B3     69 - LOAD_ATTR           'combat'
                             000001B6     69 - LOAD_ATTR           'SPEED'
                             000001B9     6A - COMPARE_OP          "=="
                             000001BC     6F - JUMP_IF_FALSE       -> 000001D3
                             000001BF     01 - POP_TOP             
                             000001C0     7C - LOAD_FAST           'player'
                             000001C3     69 - LOAD_ATTR           'vuln_defense_chance'
                             000001C6     64 - LOAD_CONST          5
                             000001C9     17 - BINARY_ADD          
                             000001CA     7C - LOAD_FAST           'player'
                             000001CD     5F - STORE_ATTR          'vuln_defense_chance'
                             000001D0     6E - JUMP_FORWARD        -> 000001D4
                             000001D3     01 - POP_TOP             
                             000001D4     64 - LOAD_CONST          None
                             000001D7     53 - RETURN_VALUE        
                             000001D8     6E - JUMP_FORWARD        -> 000001DC
                             000001DB     01 - POP_TOP             
                             000001DC     7C - LOAD_FAST           'player'
                             000001DF     69 - LOAD_ATTR           'tacticalSetting'
                             000001E2     74 - LOAD_GLOBAL         'constants'
                             000001E5     69 - LOAD_ATTR           'combat'
                             000001E8     69 - LOAD_ATTR           'POWER'
                             000001EB     6A - COMPARE_OP          "=="
                             000001EE     6F - JUMP_IF_FALSE       -> 00000207
                             000001F1     01 - POP_TOP             
                             000001F2     64 - LOAD_CONST          1
                             000001F5     7C - LOAD_FAST           'player'
                             000001F8     5F - STORE_ATTR          'vuln_created_speed'
                             000001FB     64 - LOAD_CONST          0
                             000001FE     7C - LOAD_FAST           'player'
                             00000201     5F - STORE_ATTR          'vuln_speed_chance'
                             00000204     6E - JUMP_FORWARD        -> 00000260
                             00000207     01 - POP_TOP             
                             00000208     7C - LOAD_FAST           'player'
                             0000020B     69 - LOAD_ATTR           'tacticalSetting'
                             0000020E     74 - LOAD_GLOBAL         'constants'
                             00000211     69 - LOAD_ATTR           'combat'
                             00000214     69 - LOAD_ATTR           'DEFENSE'
                             00000217     6A - COMPARE_OP          "=="
                             0000021A     6F - JUMP_IF_FALSE       -> 00000233
                             0000021D     01 - POP_TOP             
                             0000021E     64 - LOAD_CONST          1
                             00000221     7C - LOAD_FAST           'player'
                             00000224     5F - STORE_ATTR          'vuln_created_power'
                             00000227     64 - LOAD_CONST          0
                             0000022A     7C - LOAD_FAST           'player'
                             0000022D     5F - STORE_ATTR          'vuln_power_chance'
                             00000230     6E - JUMP_FORWARD        -> 00000260
                             00000233     01 - POP_TOP             
                             00000234     7C - LOAD_FAST           'player'
                             00000237     69 - LOAD_ATTR           'tacticalSetting'
                             0000023A     74 - LOAD_GLOBAL         'constants'
                             0000023D     69 - LOAD_ATTR           'combat'
                             00000240     69 - LOAD_ATTR           'SPEED'
                             00000243     6A - COMPARE_OP          "=="
                             00000246     6F - JUMP_IF_FALSE       -> 0000025F
                             00000249     01 - POP_TOP             
                             0000024A     64 - LOAD_CONST          1
                             0000024D     7C - LOAD_FAST           'player'
                             00000250     5F - STORE_ATTR          'vuln_created_defense'
                             00000253     64 - LOAD_CONST          0
                             00000256     7C - LOAD_FAST           'player'
                             00000259     5F - STORE_ATTR          'vuln_defense_chance'
                             0000025C     6E - JUMP_FORWARD        -> 00000260
                             0000025F     01 - POP_TOP             
                             00000260     74 - LOAD_GLOBAL         'random'
                             00000263     69 - LOAD_ATTR           'randrange'
                             00000266     64 - LOAD_CONST          1
                             00000269     64 - LOAD_CONST          100
                             0000026C     83 - CALL_FUNCTION       r0002
                             0000026F     7D - STORE_FAST          'roll'
                             00000272     7C - LOAD_FAST           'roll'
                             00000275     64 - LOAD_CONST          20
                             00000278     6A - COMPARE_OP          "<"
                             0000027B     6F - JUMP_IF_FALSE       -> 0000028B
                             0000027E     01 - POP_TOP             
                             0000027F     64 - LOAD_CONST          3
                             00000282     7C - LOAD_FAST           'player'
                             00000285     5F - STORE_ATTR          'vuln_created_duration'
                             00000288     6E - JUMP_FORWARD        -> 000002C9
                             0000028B     01 - POP_TOP             
                             0000028C     7C - LOAD_FAST           'roll'
                             0000028F     64 - LOAD_CONST          50
                             00000292     6A - COMPARE_OP          "<"
                             00000295     6F - JUMP_IF_FALSE       -> 000002A5
                             00000298     01 - POP_TOP             
                             00000299     64 - LOAD_CONST          4
                             0000029C     7C - LOAD_FAST           'player'
                             0000029F     5F - STORE_ATTR          'vuln_created_duration'
                             000002A2     6E - JUMP_FORWARD        -> 000002C9
                             000002A5     01 - POP_TOP             
                             000002A6     7C - LOAD_FAST           'roll'
                             000002A9     64 - LOAD_CONST          80
                             000002AC     6A - COMPARE_OP          "<"
                             000002AF     6F - JUMP_IF_FALSE       -> 000002BF
                             000002B2     01 - POP_TOP             
                             000002B3     64 - LOAD_CONST          5
                             000002B6     7C - LOAD_FAST           'player'
                             000002B9     5F - STORE_ATTR          'vuln_created_duration'
                             000002BC     6E - JUMP_FORWARD        -> 000002C9
                             000002BF     01 - POP_TOP             
                             000002C0     64 - LOAD_CONST          6
                             000002C3     7C - LOAD_FAST           'player'
                             000002C6     5F - STORE_ATTR          'vuln_created_duration'
                             000002C9     64 - LOAD_CONST          None
                             000002CC     53 - RETURN_VALUE        
                         consts:
000003EC                     TUPLE: (
000003F1                         None (4E),
000003F2                         INT: 0 (00 00 00 00),
000003F7                         FLOAT: 100.0 (05 31 30 30 2E 30),
000003FE                         FLOAT: 0.20000000000000001 (13 30 2E 32 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 31),
00000413                         FLOAT: 0.0 (03 30 2E 30),
00000418                         STR: 'vulnerability percent: %gBase + %gBonus +%gTacticChange = %g' (3C 00 00 00 76 75 6C 6E 65 72 61 62 69 6C 69 74 79 20 70 65 72 63 65 6E 74 3A 20 25 67 42 61 73 65 20 2B 20 25 67 42 6F 6E 75 73 20 2B 25 67 54 61 63 74 69 63 43 68 61 6E 67 65 20 3D 20 25 67),
00000459                         INT: 11 (0B 00 00 00),
0000045E                         FLOAT: 1.5 (03 31 2E 35),
00000463                         STR: 'vulnerability doubled from energized tactic to %g' (31 00 00 00 76 75 6C 6E 65 72 61 62 69 6C 69 74 79 20 64 6F 75 62 6C 65 64 20 66 72 6F 6D 20 65 6E 65 72 67 69 7A 65 64 20 74 61 63 74 69 63 20 74 6F 20 25 67),
00000499                         INT: 1 (01 00 00 00),
0000049E                         INT: 100 (64 00 00 00),
000004A3                         STR: 'vulnerability check: %d %f' (1A 00 00 00 76 75 6C 6E 65 72 61 62 69 6C 69 74 79 20 63 68 65 63 6B 3A 20 25 64 20 25 66),
000004C2                         INT: 5 (05 00 00 00),
000004C7                         INT: 20 (14 00 00 00),
000004CC                         INT: 3 (03 00 00 00),
000004D1                         INT: 50 (32 00 00 00),
000004D6                         INT: 4 (04 00 00 00),
000004DB                         INT: 80 (50 00 00 00),
000004E0                         INT: 6 (06 00 00 00)
                             )
                         names:
000004E5                     TUPLE: (
000004EA                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
000004F9                         STR: 'CombatTacticVulner' (12 00 00 00 43 6F 6D 62 61 74 54 61 63 74 69 63 56 75 6C 6E 65 72),
00000510                         STR: 'float' (05 00 00 00 66 6C 6F 61 74),
0000051A                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
00000525                         STR: 'vulnerabilityGenerationBonus' (1C 00 00 00 76 75 6C 6E 65 72 61 62 69 6C 69 74 79 47 65 6E 65 72 61 74 69 6F 6E 42 6F 6E 75 73),
00000546                         STR: 'vulnerabilityPercentModifier' (1C 00 00 00 76 75 6C 6E 65 72 61 62 69 6C 69 74 79 50 65 72 63 65 6E 74 4D 6F 64 69 66 69 65 72),
00000567                         STR: 'vulnerabilityBase' (11 00 00 00 76 75 6C 6E 65 72 61 62 69 6C 69 74 79 42 61 73 65),
0000057D                         STR: 'vulnerabilityTactic' (13 00 00 00 76 75 6C 6E 65 72 61 62 69 6C 69 74 79 54 61 63 74 69 63),
00000595                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
000005A9                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
000005B7                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
000005C2                         STR: 'POWER' (05 00 00 00 50 4F 57 45 52),
000005CC                         STR: 'vuln_speed_chance' (11 00 00 00 76 75 6C 6E 5F 73 70 65 65 64 5F 63 68 61 6E 63 65),
000005E2                         STR: 'DEFENSE' (07 00 00 00 44 45 46 45 4E 53 45),
000005EE                         STR: 'vuln_power_chance' (11 00 00 00 76 75 6C 6E 5F 70 6F 77 65 72 5F 63 68 61 6E 63 65),
00000604                         STR: 'SPEED' (05 00 00 00 53 50 45 45 44),
0000060E                         STR: 'vuln_defense_chance' (13 00 00 00 76 75 6C 6E 5F 64 65 66 65 6E 73 65 5F 63 68 61 6E 63 65),
00000626                         STR: 'vulnerability' (0D 00 00 00 76 75 6C 6E 65 72 61 62 69 6C 69 74 79),
00000638                         STR: 'CU' (02 00 00 00 43 55),
0000063F                         STR: 'outputCombatDebugMessageOnMatch' (1F 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 4F 6E 4D 61 74 63 68),
00000663                         STR: 'isEnergizedTactic' (11 00 00 00 69 73 45 6E 65 72 67 69 7A 65 64 54 61 63 74 69 63),
00000679                         STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00000684                         STR: 'randrange' (09 00 00 00 72 61 6E 64 72 61 6E 67 65),
00000692                         STR: 'roll' (04 00 00 00 72 6F 6C 6C),
0000069B                         STR: 'vuln_created_speed' (12 00 00 00 76 75 6C 6E 5F 63 72 65 61 74 65 64 5F 73 70 65 65 64),
000006B2                         STR: 'vuln_created_power' (12 00 00 00 76 75 6C 6E 5F 63 72 65 61 74 65 64 5F 70 6F 77 65 72),
000006C9                         STR: 'vuln_created_defense' (14 00 00 00 76 75 6C 6E 5F 63 72 65 61 74 65 64 5F 64 65 66 65 6E 73 65),
000006E2                         STR: 'vuln_created_duration' (15 00 00 00 76 75 6C 6E 5F 63 72 65 61 74 65 64 5F 64 75 72 61 74 69 6F 6E)
                             )
                         varnames:
000006FC                     TUPLE: (
00000701                         STR: 'player' (06 00 00 00 70 6C 61 79 65 72),
0000070C                         STR: 'vulnerability' (0D 00 00 00 76 75 6C 6E 65 72 61 62 69 6C 69 74 79),
0000071E                         STR: 'vulnerabilityTactic' (13 00 00 00 76 75 6C 6E 65 72 61 62 69 6C 69 74 79 54 61 63 74 69 63),
00000736                         STR: 'vulnerabilityPercentModifier' (1C 00 00 00 76 75 6C 6E 65 72 61 62 69 6C 69 74 79 50 65 72 63 65 6E 74 4D 6F 64 69 66 69 65 72),
00000757                         STR: 'vulnerabilityBase' (11 00 00 00 76 75 6C 6E 65 72 61 62 69 6C 69 74 79 42 61 73 65),
0000076D                         STR: 'roll' (04 00 00 00 72 6F 6C 6C)
                             )
                         freevars:
00000776                     TUPLE: ()
                         cellvars:
0000077B                     TUPLE: ()
                         filename:
00000780                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_resolution.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 72 65 73 6F 6C 75 74 69 6F 6E 2E 70 79)
                         name:
000007D8                     STR: 'generateVulnerabilities' (17 00 00 00 67 65 6E 65 72 61 74 65 56 75 6C 6E 65 72 61 62 69 6C 69 74 69 65 73)
                         firslineno:
000007F4                     LONG: 13L (0D 00 00 00)
                         lnotab:
000007F8                     STR: '\x00\x02\x10\x01\x08\x03\x14\x01\x06\x01\x06\x03\x16\x01\x17\x01\x16\x01\x17\x01\x16\x01\x17\x03\x0e\x01 \x02\n\x01\n\x01\x18\x06\x12\x01\x1a\x02\x11\x01\x16\x01\x14\x01\x16\x01\x14\x01\x16\x01\x14\x02\x08\x03\x16\x01\t\x01\r\x01\x16\x01\t\x01\r\x01\x16\x01\t\x01\r\x03\x12\x01\r\x01\r\x01\r\x01\r\x01\r\x01\r\x02' (56 00 00 00 00 02 10 01 08 03 14 01 06 01 06 03 16 01 17 01 16 01 17 01 16 01 17 03 0E 01 20 02 0A 01 0A 01 18 06 12 01 1A 02 11 01 16 01 14 01 16 01 14 01 16 01 14 02 08 03 16 01 09 01 0D 01 16 01 09 01 0D 01 16 01 09 01 0D 03 12 01 0D 01 0D 01 0D 01 0D 01 0D 01 0D 02),
00000853             CODE:
                         argcount:
00000854                     LONG: 2L (02 00 00 00)
                         nlocals:
00000858                     LONG: 2L (02 00 00 00)
                         stacksize:
0000085C                     LONG: 3L (03 00 00 00)
                         flags:
00000860                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000864                     STR: '|\x00\x00i\x01\x00\x0co\x08\x00\x01d\x00\x00Sn\x01\x00\x01t\x02\x00i\x03\x00d\x01\x00d\x02\x00\x83\x02\x00\x01|\x00\x00i\x04\x00t\x05\x00i\x06\x00i\x07\x00j\x02\x00o\r\x00\x01|\x01\x00i\t\x00d\x03\x00j\x04\x00o\r\x00\x01d\x04\x00|\x01\x00_\n\x00ng\x00\x01|\x00\x00i\x04\x00t\x05\x00i\x06\x00i\x0b\x00j\x02\x00o\r\x00\x01|\x01\x00i\x0c\x00d\x03\x00j\x04\x00o\r\x00\x01d\x04\x00|\x01\x00_\r\x00n4\x00\x01|\x00\x00i\x04\x00t\x05\x00i\x06\x00i\x0e\x00j\x02\x00o\r\x00\x01|\x01\x00i\x0f\x00d\x03\x00j\x04\x00o\r\x00\x01d\x04\x00|\x01\x00_\x10\x00n\x01\x00\x01d\x00\x00S' (C0 00 00 00 7C 00 00 69 01 00 0C 6F 08 00 01 64 00 00 53 6E 01 00 01 74 02 00 69 03 00 64 01 00 64 02 00 83 02 00 01 7C 00 00 69 04 00 74 05 00 69 06 00 69 07 00 6A 02 00 6F 0D 00 01 7C 01 00 69 09 00 64 03 00 6A 04 00 6F 0D 00 01 64 04 00 7C 01 00 5F 0A 00 6E 67 00 01 7C 00 00 69 04 00 74 05 00 69 06 00 69 0B 00 6A 02 00 6F 0D 00 01 7C 01 00 69 0C 00 64 03 00 6A 04 00 6F 0D 00 01 64 04 00 7C 01 00 5F 0D 00 6E 34 00 01 7C 00 00 69 04 00 74 05 00 69 06 00 69 0E 00 6A 02 00 6F 0D 00 01 7C 01 00 69 0F 00 64 03 00 6A 04 00 6F 0D 00 01 64 04 00 7C 01 00 5F 10 00 6E 01 00 01 64 00 00 53)
                             00000000     7C - LOAD_FAST           'player1'
                             00000003     69 - LOAD_ATTR           'canExploitVulnerabilities'
                             00000006     0C - UNARY_NOT           
                             00000007     6F - JUMP_IF_FALSE       -> 00000012
                             0000000A     01 - POP_TOP             
                             0000000B     64 - LOAD_CONST          None
                             0000000E     53 - RETURN_VALUE        
                             0000000F     6E - JUMP_FORWARD        -> 00000013
                             00000012     01 - POP_TOP             
                             00000013     74 - LOAD_GLOBAL         'CU'
                             00000016     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             00000019     64 - LOAD_CONST          'exploit check'
                             0000001C     64 - LOAD_CONST          3
                             0000001F     83 - CALL_FUNCTION       r0002
                             00000022     01 - POP_TOP             
                             00000023     7C - LOAD_FAST           'player1'
                             00000026     69 - LOAD_ATTR           'tacticalSetting'
                             00000029     74 - LOAD_GLOBAL         'constants'
                             0000002C     69 - LOAD_ATTR           'combat'
                             0000002F     69 - LOAD_ATTR           'SPEED'
                             00000032     6A - COMPARE_OP          "=="
                             00000035     6F - JUMP_IF_FALSE       -> 00000045
                             00000038     01 - POP_TOP             
                             00000039     7C - LOAD_FAST           'player2'
                             0000003C     69 - LOAD_ATTR           'speedVulnerabilityCount'
                             0000003F     64 - LOAD_CONST          0
                             00000042     6A - COMPARE_OP          ">"
                             00000045     6F - JUMP_IF_FALSE       -> 00000055
                             00000048     01 - POP_TOP             
                             00000049     64 - LOAD_CONST          1
                             0000004C     7C - LOAD_FAST           'player2'
                             0000004F     5F - STORE_ATTR          'vuln_exploited_speed'
                             00000052     6E - JUMP_FORWARD        -> 000000BC
                             00000055     01 - POP_TOP             
                             00000056     7C - LOAD_FAST           'player1'
                             00000059     69 - LOAD_ATTR           'tacticalSetting'
                             0000005C     74 - LOAD_GLOBAL         'constants'
                             0000005F     69 - LOAD_ATTR           'combat'
                             00000062     69 - LOAD_ATTR           'POWER'
                             00000065     6A - COMPARE_OP          "=="
                             00000068     6F - JUMP_IF_FALSE       -> 00000078
                             0000006B     01 - POP_TOP             
                             0000006C     7C - LOAD_FAST           'player2'
                             0000006F     69 - LOAD_ATTR           'powerVulnerabilityCount'
                             00000072     64 - LOAD_CONST          0
                             00000075     6A - COMPARE_OP          ">"
                             00000078     6F - JUMP_IF_FALSE       -> 00000088
                             0000007B     01 - POP_TOP             
                             0000007C     64 - LOAD_CONST          1
                             0000007F     7C - LOAD_FAST           'player2'
                             00000082     5F - STORE_ATTR          'vuln_exploited_power'
                             00000085     6E - JUMP_FORWARD        -> 000000BC
                             00000088     01 - POP_TOP             
                             00000089     7C - LOAD_FAST           'player1'
                             0000008C     69 - LOAD_ATTR           'tacticalSetting'
                             0000008F     74 - LOAD_GLOBAL         'constants'
                             00000092     69 - LOAD_ATTR           'combat'
                             00000095     69 - LOAD_ATTR           'DEFENSE'
                             00000098     6A - COMPARE_OP          "=="
                             0000009B     6F - JUMP_IF_FALSE       -> 000000AB
                             0000009E     01 - POP_TOP             
                             0000009F     7C - LOAD_FAST           'player2'
                             000000A2     69 - LOAD_ATTR           'defenseVulnerabilityCount'
                             000000A5     64 - LOAD_CONST          0
                             000000A8     6A - COMPARE_OP          ">"
                             000000AB     6F - JUMP_IF_FALSE       -> 000000BB
                             000000AE     01 - POP_TOP             
                             000000AF     64 - LOAD_CONST          1
                             000000B2     7C - LOAD_FAST           'player2'
                             000000B5     5F - STORE_ATTR          'vuln_exploited_defense'
                             000000B8     6E - JUMP_FORWARD        -> 000000BC
                             000000BB     01 - POP_TOP             
                             000000BC     64 - LOAD_CONST          None
                             000000BF     53 - RETURN_VALUE        
                         consts:
00000929                     TUPLE: (
0000092E                         None (4E),
0000092F                         STR: 'exploit check' (0D 00 00 00 65 78 70 6C 6F 69 74 20 63 68 65 63 6B),
00000941                         INT: 3 (03 00 00 00),
00000946                         INT: 0 (00 00 00 00),
0000094B                         INT: 1 (01 00 00 00)
                             )
                         names:
00000950                     TUPLE: (
00000955                         STR: 'player1' (07 00 00 00 70 6C 61 79 65 72 31),
00000961                         STR: 'canExploitVulnerabilities' (19 00 00 00 63 61 6E 45 78 70 6C 6F 69 74 56 75 6C 6E 65 72 61 62 69 6C 69 74 69 65 73),
0000097F                         STR: 'CU' (02 00 00 00 43 55),
00000986                         STR: 'outputCombatDebugMessageOnMatch' (1F 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 4F 6E 4D 61 74 63 68),
000009AA                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
000009BE                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
000009CC                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
000009D7                         STR: 'SPEED' (05 00 00 00 53 50 45 45 44),
000009E1                         STR: 'player2' (07 00 00 00 70 6C 61 79 65 72 32),
000009ED                         STR: 'speedVulnerabilityCount' (17 00 00 00 73 70 65 65 64 56 75 6C 6E 65 72 61 62 69 6C 69 74 79 43 6F 75 6E 74),
00000A09                         STR: 'vuln_exploited_speed' (14 00 00 00 76 75 6C 6E 5F 65 78 70 6C 6F 69 74 65 64 5F 73 70 65 65 64),
00000A22                         STR: 'POWER' (05 00 00 00 50 4F 57 45 52),
00000A2C                         STR: 'powerVulnerabilityCount' (17 00 00 00 70 6F 77 65 72 56 75 6C 6E 65 72 61 62 69 6C 69 74 79 43 6F 75 6E 74),
00000A48                         STR: 'vuln_exploited_power' (14 00 00 00 76 75 6C 6E 5F 65 78 70 6C 6F 69 74 65 64 5F 70 6F 77 65 72),
00000A61                         STR: 'DEFENSE' (07 00 00 00 44 45 46 45 4E 53 45),
00000A6D                         STR: 'defenseVulnerabilityCount' (19 00 00 00 64 65 66 65 6E 73 65 56 75 6C 6E 65 72 61 62 69 6C 69 74 79 43 6F 75 6E 74),
00000A8B                         STR: 'vuln_exploited_defense' (16 00 00 00 76 75 6C 6E 5F 65 78 70 6C 6F 69 74 65 64 5F 64 65 66 65 6E 73 65)
                             )
                         varnames:
00000AA6                     TUPLE: (
00000AAB                         STR: 'player1' (07 00 00 00 70 6C 61 79 65 72 31),
00000AB7                         STR: 'player2' (07 00 00 00 70 6C 61 79 65 72 32)
                             )
                         freevars:
00000AC3                     TUPLE: ()
                         cellvars:
00000AC8                     TUPLE: ()
                         filename:
00000ACD                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_resolution.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 72 65 73 6F 6C 75 74 69 6F 6E 2E 70 79)
                         name:
00000B25                     STR: 'generateExploits' (10 00 00 00 67 65 6E 65 72 61 74 65 45 78 70 6C 6F 69 74 73)
                         firslineno:
00000B3A                     LONG: 78L (4E 00 00 00)
                         lnotab:
00000B3E                     STR: '\x00\x02\x0b\x01\x08\x02\x10\x02&\x01\r\x01&\x01\r\x01&\x01' (12 00 00 00 00 02 0B 01 08 02 10 02 26 01 0D 01 26 01 0D 01 26 01),
00000B55             CODE:
                         argcount:
00000B56                     LONG: 2L (02 00 00 00)
                         nlocals:
00000B5A                     LONG: 2L (02 00 00 00)
                         stacksize:
00000B5E                     LONG: 3L (03 00 00 00)
                         flags:
00000B62                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000B66                     STR: 't\x00\x00i\x01\x00d\x01\x00j\x02\x00o\x08\x00\x01d\x00\x00Sn\x01\x00\x01t\x02\x00|\x00\x00|\x01\x00\x83\x02\x00\x01t\x02\x00|\x01\x00|\x00\x00\x83\x02\x00\x01d\x00\x00S' (36 00 00 00 74 00 00 69 01 00 64 01 00 6A 02 00 6F 08 00 01 64 00 00 53 6E 01 00 01 74 02 00 7C 00 00 7C 01 00 83 02 00 01 74 02 00 7C 01 00 7C 00 00 83 02 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'consolevar'
                             00000003     69 - LOAD_ATTR           'CombatTacticVulner'
                             00000006     64 - LOAD_CONST          0
                             00000009     6A - COMPARE_OP          "=="
                             0000000C     6F - JUMP_IF_FALSE       -> 00000017
                             0000000F     01 - POP_TOP             
                             00000010     64 - LOAD_CONST          None
                             00000013     53 - RETURN_VALUE        
                             00000014     6E - JUMP_FORWARD        -> 00000018
                             00000017     01 - POP_TOP             
                             00000018     74 - LOAD_GLOBAL         'generateExploits'
                             0000001B     7C - LOAD_FAST           'player1'
                             0000001E     7C - LOAD_FAST           'player2'
                             00000021     83 - CALL_FUNCTION       r0002
                             00000024     01 - POP_TOP             
                             00000025     74 - LOAD_GLOBAL         'generateExploits'
                             00000028     7C - LOAD_FAST           'player2'
                             0000002B     7C - LOAD_FAST           'player1'
                             0000002E     83 - CALL_FUNCTION       r0002
                             00000031     01 - POP_TOP             
                             00000032     64 - LOAD_CONST          None
                             00000035     53 - RETURN_VALUE        
                         consts:
00000BA1                     TUPLE: (
00000BA6                         None (4E),
00000BA7                         INT: 0 (00 00 00 00)
                             )
                         names:
00000BAC                     TUPLE: (
00000BB1                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
00000BC0                         STR: 'CombatTacticVulner' (12 00 00 00 43 6F 6D 62 61 74 54 61 63 74 69 63 56 75 6C 6E 65 72),
00000BD7                         STR: 'generateExploits' (10 00 00 00 67 65 6E 65 72 61 74 65 45 78 70 6C 6F 69 74 73),
00000BEC                         STR: 'player1' (07 00 00 00 70 6C 61 79 65 72 31),
00000BF8                         STR: 'player2' (07 00 00 00 70 6C 61 79 65 72 32)
                             )
                         varnames:
00000C04                     TUPLE: (
00000C09                         STR: 'player1' (07 00 00 00 70 6C 61 79 65 72 31),
00000C15                         STR: 'player2' (07 00 00 00 70 6C 61 79 65 72 32)
                             )
                         freevars:
00000C21                     TUPLE: ()
                         cellvars:
00000C26                     TUPLE: ()
                         filename:
00000C2B                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_resolution.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 72 65 73 6F 6C 75 74 69 6F 6E 2E 70 79)
                         name:
00000C83                     STR: 'generateExploitsForPlayers' (1A 00 00 00 67 65 6E 65 72 61 74 65 45 78 70 6C 6F 69 74 73 46 6F 72 50 6C 61 79 65 72 73)
                         firslineno:
00000CA2                     LONG: 92L (5C 00 00 00)
                         lnotab:
00000CA6                     STR: '\x00\x02\x10\x01\x08\x02\r\x01' (08 00 00 00 00 02 10 01 08 02 0D 01),
00000CB3             CODE:
                         argcount:
00000CB4                     LONG: 1L (01 00 00 00)
                         nlocals:
00000CB8                     LONG: 1L (01 00 00 00)
                         stacksize:
00000CBC                     LONG: 2L (02 00 00 00)
                         flags:
00000CC0                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000CC4                     STR: '|\x00\x00t\x01\x00j\x02\x00o\x08\x00\x01t\x02\x00Sn/\x00\x01|\x00\x00t\x03\x00j\x02\x00o\x08\x00\x01t\x02\x00Sn\x1a\x00\x01|\x00\x00t\x04\x00j\x02\x00o\x08\x00\x01t\x02\x00Sn\x05\x00\x01t\x05\x00Sd\x00\x00S' (47 00 00 00 7C 00 00 74 01 00 6A 02 00 6F 08 00 01 74 02 00 53 6E 2F 00 01 7C 00 00 74 03 00 6A 02 00 6F 08 00 01 74 02 00 53 6E 1A 00 01 7C 00 00 74 04 00 6A 02 00 6F 08 00 01 74 02 00 53 6E 05 00 01 74 05 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'ability'
                             00000003     74 - LOAD_GLOBAL         'AikidoAbility'
                             00000006     6A - COMPARE_OP          "=="
                             00000009     6F - JUMP_IF_FALSE       -> 00000014
                             0000000C     01 - POP_TOP             
                             0000000D     74 - LOAD_GLOBAL         'True'
                             00000010     53 - RETURN_VALUE        
                             00000011     6E - JUMP_FORWARD        -> 00000043
                             00000014     01 - POP_TOP             
                             00000015     7C - LOAD_FAST           'ability'
                             00000018     74 - LOAD_GLOBAL         'KarateAbility'
                             0000001B     6A - COMPARE_OP          "=="
                             0000001E     6F - JUMP_IF_FALSE       -> 00000029
                             00000021     01 - POP_TOP             
                             00000022     74 - LOAD_GLOBAL         'True'
                             00000025     53 - RETURN_VALUE        
                             00000026     6E - JUMP_FORWARD        -> 00000043
                             00000029     01 - POP_TOP             
                             0000002A     7C - LOAD_FAST           'ability'
                             0000002D     74 - LOAD_GLOBAL         'KungFuAbility'
                             00000030     6A - COMPARE_OP          "=="
                             00000033     6F - JUMP_IF_FALSE       -> 0000003E
                             00000036     01 - POP_TOP             
                             00000037     74 - LOAD_GLOBAL         'True'
                             0000003A     53 - RETURN_VALUE        
                             0000003B     6E - JUMP_FORWARD        -> 00000043
                             0000003E     01 - POP_TOP             
                             0000003F     74 - LOAD_GLOBAL         'False'
                             00000042     53 - RETURN_VALUE        
                             00000043     64 - LOAD_CONST          None
                             00000046     53 - RETURN_VALUE        
                         consts:
00000D10                     TUPLE: (
00000D15                         None (4E)
                             )
                         names:
00000D16                     TUPLE: (
00000D1B                         STR: 'ability' (07 00 00 00 61 62 69 6C 69 74 79),
00000D27                         STR: 'AikidoAbility' (0D 00 00 00 41 69 6B 69 64 6F 41 62 69 6C 69 74 79),
00000D39                         STR: 'True' (04 00 00 00 54 72 75 65),
00000D42                         STR: 'KarateAbility' (0D 00 00 00 4B 61 72 61 74 65 41 62 69 6C 69 74 79),
00000D54                         STR: 'KungFuAbility' (0D 00 00 00 4B 75 6E 67 46 75 41 62 69 6C 69 74 79),
00000D66                         STR: 'False' (05 00 00 00 46 61 6C 73 65)
                             )
                         varnames:
00000D70                     TUPLE: (
00000D75                         STR: 'ability' (07 00 00 00 61 62 69 6C 69 74 79)
                             )
                         freevars:
00000D81                     TUPLE: ()
                         cellvars:
00000D86                     TUPLE: ()
                         filename:
00000D8B                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_resolution.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 72 65 73 6F 6C 75 74 69 6F 6E 2E 70 79)
                         name:
00000DE3                     STR: 'isAbilityMartialArt' (13 00 00 00 69 73 41 62 69 6C 69 74 79 4D 61 72 74 69 61 6C 41 72 74)
                         firslineno:
00000DFB                     LONG: 104L (68 00 00 00)
                         lnotab:
00000DFF                     STR: '\x00\x01\r\x01\x08\x01\r\x01\x08\x01\r\x01\x08\x02' (0E 00 00 00 00 01 0D 01 08 01 0D 01 08 01 0D 01 08 02),
00000E12             CODE:
                         argcount:
00000E13                     LONG: 2L (02 00 00 00)
                         nlocals:
00000E17                     LONG: 9L (09 00 00 00)
                         stacksize:
00000E1B                     LONG: 12L (0C 00 00 00)
                         flags:
00000E1F                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000E23                     STR: 'd\x01\x00}\x04\x00|\x01\x00i\x02\x00d\x02\x00j\x04\x00o5\x00\x01t\x03\x00i\x04\x00d\x03\x00d\x04\x00\x83\x02\x00\x01|\x04\x00d\x05\x007}\x04\x00|\x04\x00t\x05\x00|\x00\x00i\x07\x00\x83\x01\x00d\x06\x00\x157}\x04\x00n\x01\x00\x01t\x08\x00i\t\x00|\x00\x00i\n\x00|\x00\x00i\x0b\x00|\x00\x00i\x0c\x00|\x00\x00i\r\x00|\x00\x00i\x0e\x00|\x00\x00i\x0f\x00d\x07\x00|\x04\x00|\x00\x00i\x10\x00|\x00\x00i\x11\x00|\x00\x00i\x12\x00\x83\x0b\x00}\x08\x00t\x03\x00i\x14\x00d\x08\x00|\x08\x00\x16d\x04\x00\x83\x02\x00\x01|\x01\x00i\x15\x00}\x03\x00t\x03\x00i\x17\x00|\x00\x00i\x0c\x00\x83\x01\x00}\x06\x00|\x06\x00t\x19\x00j\x02\x00o\r\x00\x01|\x01\x00i\x1a\x00}\x05\x00n\n\x00\x01|\x01\x00i\x1c\x00}\x05\x00t\x08\x00i\x1d\x00|\x00\x00i\x1e\x00|\x01\x00i\x1e\x00|\x03\x00|\x05\x00\x17|\x08\x00\x83\x04\x00}\x07\x00t\x03\x00i\x14\x00d\t\x00|\x07\x00\x16d\x04\x00\x83\x02\x00\x01t \x00t\x05\x00|\x08\x00\x83\x01\x00|\x07\x00\x14\x83\x01\x00}\x02\x00t\x03\x00i\x14\x00d\n\x00|\x02\x00\x16d\x04\x00\x83\x02\x00\x01|\x08\x00|\x02\x008}\x08\x00|\x08\x00d\x07\x00j\x00\x00o\n\x00\x01d\x07\x00}\x08\x00n\x01\x00\x01t\x03\x00i\x14\x00d\x0b\x00|\x08\x00\x16d\x04\x00\x83\x02\x00\x01t \x00|\x08\x00\x83\x01\x00t \x00|\x02\x00\x83\x01\x00f\x02\x00Sd\x00\x00S' (94 01 00 00 64 01 00 7D 04 00 7C 01 00 69 02 00 64 02 00 6A 04 00 6F 35 00 01 74 03 00 69 04 00 64 03 00 64 04 00 83 02 00 01 7C 04 00 64 05 00 37 7D 04 00 7C 04 00 74 05 00 7C 00 00 69 07 00 83 01 00 64 06 00 15 37 7D 04 00 6E 01 00 01 74 08 00 69 09 00 7C 00 00 69 0A 00 7C 00 00 69 0B 00 7C 00 00 69 0C 00 7C 00 00 69 0D 00 7C 00 00 69 0E 00 7C 00 00 69 0F 00 64 07 00 7C 04 00 7C 00 00 69 10 00 7C 00 00 69 11 00 7C 00 00 69 12 00 83 0B 00 7D 08 00 74 03 00 69 14 00 64 08 00 7C 08 00 16 64 04 00 83 02 00 01 7C 01 00 69 15 00 7D 03 00 74 03 00 69 17 00 7C 00 00 69 0C 00 83 01 00 7D 06 00 7C 06 00 74 19 00 6A 02 00 6F 0D 00 01 7C 01 00 69 1A 00 7D 05 00 6E 0A 00 01 7C 01 00 69 1C 00 7D 05 00 74 08 00 69 1D 00 7C 00 00 69 1E 00 7C 01 00 69 1E 00 7C 03 00 7C 05 00 17 7C 08 00 83 04 00 7D 07 00 74 03 00 69 14 00 64 09 00 7C 07 00 16 64 04 00 83 02 00 01 74 20 00 74 05 00 7C 08 00 83 01 00 7C 07 00 14 83 01 00 7D 02 00 74 03 00 69 14 00 64 0A 00 7C 02 00 16 64 04 00 83 02 00 01 7C 08 00 7C 02 00 38 7D 08 00 7C 08 00 64 07 00 6A 00 00 6F 0A 00 01 64 07 00 7D 08 00 6E 01 00 01 74 03 00 69 14 00 64 0B 00 7C 08 00 16 64 04 00 83 02 00 01 74 20 00 7C 08 00 83 01 00 74 20 00 7C 02 00 83 01 00 66 02 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          1.0
                             00000003     7D - STORE_FAST          'damage_multiplier'
                             00000006     7C - LOAD_FAST           'loser'
                             00000009     69 - LOAD_ATTR           'vuln_exploited_count'
                             0000000C     64 - LOAD_CONST          0
                             0000000F     6A - COMPARE_OP          ">"
                             00000012     6F - JUMP_IF_FALSE       -> 0000004A
                             00000015     01 - POP_TOP             
                             00000016     74 - LOAD_GLOBAL         'CU'
                             00000019     69 - LOAD_ATTR           'outputCombatDebugMessageOnMatch'
                             0000001C     64 - LOAD_CONST          'calcDamageForLoser: giving exploited damage bonus'
                             0000001F     64 - LOAD_CONST          10
                             00000022     83 - CALL_FUNCTION       r0002
                             00000025     01 - POP_TOP             
                             00000026     7C - LOAD_FAST           'damage_multiplier'
                             00000029     64 - LOAD_CONST          0.14999999999999999
                             0000002C     37 - INPLACE_ADD         
                             0000002D     7D - STORE_FAST          'damage_multiplier'
                             00000030     7C - LOAD_FAST           'damage_multiplier'
                             00000033     74 - LOAD_GLOBAL         'float'
                             00000036     7C - LOAD_FAST           'winner'
                             00000039     69 - LOAD_ATTR           'damageAgainstVulnerability'
                             0000003C     83 - CALL_FUNCTION       r0001
                             0000003F     64 - LOAD_CONST          100.0
                             00000042     15 - BINARY_DIVIDE       
                             00000043     37 - INPLACE_ADD         
                             00000044     7D - STORE_FAST          'damage_multiplier'
                             00000047     6E - JUMP_FORWARD        -> 0000004B
                             0000004A     01 - POP_TOP             
                             0000004B     74 - LOAD_GLOBAL         'CC'
                             0000004E     69 - LOAD_ATTR           'GetCloseCombatDamage'
                             00000051     7C - LOAD_FAST           'winner'
                             00000054     69 - LOAD_ATTR           'damageBonus'
                             00000057     7C - LOAD_FAST           'winner'
                             0000005A     69 - LOAD_ATTR           'damageInfluence'
                             0000005D     7C - LOAD_FAST           'winner'
                             00000060     69 - LOAD_ATTR           'equippedItemType'
                             00000063     7C - LOAD_FAST           'winner'
                             00000066     69 - LOAD_ATTR           'equippedItemBaseDamage'
                             00000069     7C - LOAD_FAST           'winner'
                             0000006C     69 - LOAD_ATTR           'equippedItemDeltaDamage'
                             0000006F     7C - LOAD_FAST           'winner'
                             00000072     69 - LOAD_ATTR           'tacticalSetting'
                             00000075     64 - LOAD_CONST          1
                             00000078     7C - LOAD_FAST           'damage_multiplier'
                             0000007B     7C - LOAD_FAST           'winner'
                             0000007E     69 - LOAD_ATTR           'isPreciseBlow'
                             00000081     7C - LOAD_FAST           'winner'
                             00000084     69 - LOAD_ATTR           'isEnergizedTactic'
                             00000087     7C - LOAD_FAST           'winner'
                             0000008A     69 - LOAD_ATTR           'opponentCount'
                             0000008D     83 - CALL_FUNCTION       r000B
                             00000090     7D - STORE_FAST          'damage_amount'
                             00000093     74 - LOAD_GLOBAL         'CU'
                             00000096     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000099     64 - LOAD_CONST          'calcDamageForLoser: Damage returned: %d.'
                             0000009C     7C - LOAD_FAST           'damage_amount'
                             0000009F     16 - BINARY_MODULO       
                             000000A0     64 - LOAD_CONST          10
                             000000A3     83 - CALL_FUNCTION       r0002
                             000000A6     01 - POP_TOP             
                             000000A7     7C - LOAD_FAST           'loser'
                             000000AA     69 - LOAD_ATTR           'toughness'
                             000000AD     7D - STORE_FAST          'damage_resist'
                             000000B0     74 - LOAD_GLOBAL         'CU'
                             000000B3     69 - LOAD_ATTR           'isUsingWeapon'
                             000000B6     7C - LOAD_FAST           'winner'
                             000000B9     69 - LOAD_ATTR           'equippedItemType'
                             000000BC     83 - CALL_FUNCTION       r0001
                             000000BF     7D - STORE_FAST          'bUsing_weapon'
                             000000C2     7C - LOAD_FAST           'bUsing_weapon'
                             000000C5     74 - LOAD_GLOBAL         'True'
                             000000C8     6A - COMPARE_OP          "=="
                             000000CB     6F - JUMP_IF_FALSE       -> 000000DB
                             000000CE     01 - POP_TOP             
                             000000CF     7C - LOAD_FAST           'loser'
                             000000D2     69 - LOAD_ATTR           'rangedToughness'
                             000000D5     7D - STORE_FAST          'damage_resist_boost'
                             000000D8     6E - JUMP_FORWARD        -> 000000E5
                             000000DB     01 - POP_TOP             
                             000000DC     7C - LOAD_FAST           'loser'
                             000000DF     69 - LOAD_ATTR           'meleeToughness'
                             000000E2     7D - STORE_FAST          'damage_resist_boost'
                             000000E5     74 - LOAD_GLOBAL         'CC'
                             000000E8     69 - LOAD_ATTR           'GetDamageReductionValue'
                             000000EB     7C - LOAD_FAST           'winner'
                             000000EE     69 - LOAD_ATTR           'playerLevel'
                             000000F1     7C - LOAD_FAST           'loser'
                             000000F4     69 - LOAD_ATTR           'playerLevel'
                             000000F7     7C - LOAD_FAST           'damage_resist'
                             000000FA     7C - LOAD_FAST           'damage_resist_boost'
                             000000FD     17 - BINARY_ADD          
                             000000FE     7C - LOAD_FAST           'damage_amount'
                             00000101     83 - CALL_FUNCTION       r0004
                             00000104     7D - STORE_FAST          'damage_resist_total'
                             00000107     74 - LOAD_GLOBAL         'CU'
                             0000010A     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000010D     64 - LOAD_CONST          'calcDamageForLoser: resistance = %g'
                             00000110     7C - LOAD_FAST           'damage_resist_total'
                             00000113     16 - BINARY_MODULO       
                             00000114     64 - LOAD_CONST          10
                             00000117     83 - CALL_FUNCTION       r0002
                             0000011A     01 - POP_TOP             
                             0000011B     74 - LOAD_GLOBAL         'int'
                             0000011E     74 - LOAD_GLOBAL         'float'
                             00000121     7C - LOAD_FAST           'damage_amount'
                             00000124     83 - CALL_FUNCTION       r0001
                             00000127     7C - LOAD_FAST           'damage_resist_total'
                             0000012A     14 - BINARY_MULTIPLY     
                             0000012B     83 - CALL_FUNCTION       r0001
                             0000012E     7D - STORE_FAST          'damage_resisted'
                             00000131     74 - LOAD_GLOBAL         'CU'
                             00000134     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000137     64 - LOAD_CONST          'calcDamageForLoser: damage resisted = %d'
                             0000013A     7C - LOAD_FAST           'damage_resisted'
                             0000013D     16 - BINARY_MODULO       
                             0000013E     64 - LOAD_CONST          10
                             00000141     83 - CALL_FUNCTION       r0002
                             00000144     01 - POP_TOP             
                             00000145     7C - LOAD_FAST           'damage_amount'
                             00000148     7C - LOAD_FAST           'damage_resisted'
                             0000014B     38 - INPLACE_SUBTRACT    
                             0000014C     7D - STORE_FAST          'damage_amount'
                             0000014F     7C - LOAD_FAST           'damage_amount'
                             00000152     64 - LOAD_CONST          1
                             00000155     6A - COMPARE_OP          "<"
                             00000158     6F - JUMP_IF_FALSE       -> 00000165
                             0000015B     01 - POP_TOP             
                             0000015C     64 - LOAD_CONST          1
                             0000015F     7D - STORE_FAST          'damage_amount'
                             00000162     6E - JUMP_FORWARD        -> 00000166
                             00000165     01 - POP_TOP             
                             00000166     74 - LOAD_GLOBAL         'CU'
                             00000169     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000016C     64 - LOAD_CONST          'calcDamageForLoser: final Damage: %d'
                             0000016F     7C - LOAD_FAST           'damage_amount'
                             00000172     16 - BINARY_MODULO       
                             00000173     64 - LOAD_CONST          10
                             00000176     83 - CALL_FUNCTION       r0002
                             00000179     01 - POP_TOP             
                             0000017A     74 - LOAD_GLOBAL         'int'
                             0000017D     7C - LOAD_FAST           'damage_amount'
                             00000180     83 - CALL_FUNCTION       r0001
                             00000183     74 - LOAD_GLOBAL         'int'
                             00000186     7C - LOAD_FAST           'damage_resisted'
                             00000189     83 - CALL_FUNCTION       r0001
                             0000018C     66 - BUILD_TUPLE         r0002
                             0000018F     53 - RETURN_VALUE        
                             00000190     64 - LOAD_CONST          None
                             00000193     53 - RETURN_VALUE        
                         consts:
00000FBC                     TUPLE: (
00000FC1                         None (4E),
00000FC2                         FLOAT: 1.0 (03 31 2E 30),
00000FC7                         INT: 0 (00 00 00 00),
00000FCC                         STR: 'calcDamageForLoser: giving exploited damage bonus' (31 00 00 00 63 61 6C 63 44 61 6D 61 67 65 46 6F 72 4C 6F 73 65 72 3A 20 67 69 76 69 6E 67 20 65 78 70 6C 6F 69 74 65 64 20 64 61 6D 61 67 65 20 62 6F 6E 75 73),
00001002                         INT: 10 (0A 00 00 00),
00001007                         FLOAT: 0.14999999999999999 (13 30 2E 31 34 39 39 39 39 39 39 39 39 39 39 39 39 39 39 39),
0000101C                         FLOAT: 100.0 (05 31 30 30 2E 30),
00001023                         INT: 1 (01 00 00 00),
00001028                         STR: 'calcDamageForLoser: Damage returned: %d.' (28 00 00 00 63 61 6C 63 44 61 6D 61 67 65 46 6F 72 4C 6F 73 65 72 3A 20 44 61 6D 61 67 65 20 72 65 74 75 72 6E 65 64 3A 20 25 64 2E),
00001055                         STR: 'calcDamageForLoser: resistance = %g' (23 00 00 00 63 61 6C 63 44 61 6D 61 67 65 46 6F 72 4C 6F 73 65 72 3A 20 72 65 73 69 73 74 61 6E 63 65 20 3D 20 25 67),
0000107D                         STR: 'calcDamageForLoser: damage resisted = %d' (28 00 00 00 63 61 6C 63 44 61 6D 61 67 65 46 6F 72 4C 6F 73 65 72 3A 20 64 61 6D 61 67 65 20 72 65 73 69 73 74 65 64 20 3D 20 25 64),
000010AA                         STR: 'calcDamageForLoser: final Damage: %d' (24 00 00 00 63 61 6C 63 44 61 6D 61 67 65 46 6F 72 4C 6F 73 65 72 3A 20 66 69 6E 61 6C 20 44 61 6D 61 67 65 3A 20 25 64)
                             )
                         names:
000010D3                     TUPLE: (
000010D8                         STR: 'damage_multiplier' (11 00 00 00 64 61 6D 61 67 65 5F 6D 75 6C 74 69 70 6C 69 65 72),
000010EE                         STR: 'loser' (05 00 00 00 6C 6F 73 65 72),
000010F8                         STR: 'vuln_exploited_count' (14 00 00 00 76 75 6C 6E 5F 65 78 70 6C 6F 69 74 65 64 5F 63 6F 75 6E 74),
00001111                         STR: 'CU' (02 00 00 00 43 55),
00001118                         STR: 'outputCombatDebugMessageOnMatch' (1F 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 4F 6E 4D 61 74 63 68),
0000113C                         STR: 'float' (05 00 00 00 66 6C 6F 61 74),
00001146                         STR: 'winner' (06 00 00 00 77 69 6E 6E 65 72),
00001151                         STR: 'damageAgainstVulnerability' (1A 00 00 00 64 61 6D 61 67 65 41 67 61 69 6E 73 74 56 75 6C 6E 65 72 61 62 69 6C 69 74 79),
00001170                         STR: 'CC' (02 00 00 00 43 43),
00001177                         STR: 'GetCloseCombatDamage' (14 00 00 00 47 65 74 43 6C 6F 73 65 43 6F 6D 62 61 74 44 61 6D 61 67 65),
00001190                         STR: 'damageBonus' (0B 00 00 00 64 61 6D 61 67 65 42 6F 6E 75 73),
000011A0                         STR: 'damageInfluence' (0F 00 00 00 64 61 6D 61 67 65 49 6E 66 6C 75 65 6E 63 65),
000011B4                         STR: 'equippedItemType' (10 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D 54 79 70 65),
000011C9                         STR: 'equippedItemBaseDamage' (16 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D 42 61 73 65 44 61 6D 61 67 65),
000011E4                         STR: 'equippedItemDeltaDamage' (17 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D 44 65 6C 74 61 44 61 6D 61 67 65),
00001200                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
00001214                         STR: 'isPreciseBlow' (0D 00 00 00 69 73 50 72 65 63 69 73 65 42 6C 6F 77),
00001226                         STR: 'isEnergizedTactic' (11 00 00 00 69 73 45 6E 65 72 67 69 7A 65 64 54 61 63 74 69 63),
0000123C                         STR: 'opponentCount' (0D 00 00 00 6F 70 70 6F 6E 65 6E 74 43 6F 75 6E 74),
0000124E                         STR: 'damage_amount' (0D 00 00 00 64 61 6D 61 67 65 5F 61 6D 6F 75 6E 74),
00001260                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
0000127D                         STR: 'toughness' (09 00 00 00 74 6F 75 67 68 6E 65 73 73),
0000128B                         STR: 'damage_resist' (0D 00 00 00 64 61 6D 61 67 65 5F 72 65 73 69 73 74),
0000129D                         STR: 'isUsingWeapon' (0D 00 00 00 69 73 55 73 69 6E 67 57 65 61 70 6F 6E),
000012AF                         STR: 'bUsing_weapon' (0D 00 00 00 62 55 73 69 6E 67 5F 77 65 61 70 6F 6E),
000012C1                         STR: 'True' (04 00 00 00 54 72 75 65),
000012CA                         STR: 'rangedToughness' (0F 00 00 00 72 61 6E 67 65 64 54 6F 75 67 68 6E 65 73 73),
000012DE                         STR: 'damage_resist_boost' (13 00 00 00 64 61 6D 61 67 65 5F 72 65 73 69 73 74 5F 62 6F 6F 73 74),
000012F6                         STR: 'meleeToughness' (0E 00 00 00 6D 65 6C 65 65 54 6F 75 67 68 6E 65 73 73),
00001309                         STR: 'GetDamageReductionValue' (17 00 00 00 47 65 74 44 61 6D 61 67 65 52 65 64 75 63 74 69 6F 6E 56 61 6C 75 65),
00001325                         STR: 'playerLevel' (0B 00 00 00 70 6C 61 79 65 72 4C 65 76 65 6C),
00001335                         STR: 'damage_resist_total' (13 00 00 00 64 61 6D 61 67 65 5F 72 65 73 69 73 74 5F 74 6F 74 61 6C),
0000134D                         STR: 'int' (03 00 00 00 69 6E 74),
00001355                         STR: 'damage_resisted' (0F 00 00 00 64 61 6D 61 67 65 5F 72 65 73 69 73 74 65 64)
                             )
                         varnames:
00001369                     TUPLE: (
0000136E                         STR: 'winner' (06 00 00 00 77 69 6E 6E 65 72),
00001379                         STR: 'loser' (05 00 00 00 6C 6F 73 65 72),
00001383                         STR: 'damage_resisted' (0F 00 00 00 64 61 6D 61 67 65 5F 72 65 73 69 73 74 65 64),
00001397                         STR: 'damage_resist' (0D 00 00 00 64 61 6D 61 67 65 5F 72 65 73 69 73 74),
000013A9                         STR: 'damage_multiplier' (11 00 00 00 64 61 6D 61 67 65 5F 6D 75 6C 74 69 70 6C 69 65 72),
000013BF                         STR: 'damage_resist_boost' (13 00 00 00 64 61 6D 61 67 65 5F 72 65 73 69 73 74 5F 62 6F 6F 73 74),
000013D7                         STR: 'bUsing_weapon' (0D 00 00 00 62 55 73 69 6E 67 5F 77 65 61 70 6F 6E),
000013E9                         STR: 'damage_resist_total' (13 00 00 00 64 61 6D 61 67 65 5F 72 65 73 69 73 74 5F 74 6F 74 61 6C),
00001401                         STR: 'damage_amount' (0D 00 00 00 64 61 6D 61 67 65 5F 61 6D 6F 75 6E 74)
                             )
                         freevars:
00001413                     TUPLE: ()
                         cellvars:
00001418                     TUPLE: ()
                         filename:
0000141D                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_resolution.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 72 65 73 6F 6C 75 74 69 6F 6E 2E 70 79)
                         name:
00001475                     STR: 'calcDamageForLoser' (12 00 00 00 63 61 6C 63 44 61 6D 61 67 65 46 6F 72 4C 6F 73 65 72)
                         firslineno:
0000148C                     LONG: 115L (73 00 00 00)
                         lnotab:
00001490                     STR: '\x00\x04\x06\x01\x10\x01\x10\x01\n\x03\x1b\x02H\x01\x14\x04\t\x02\x12\x03\r\x01\r\x02\t\x03"\x01\x14\x02\x16\x01\x14\x02\n\x01\r\x01\n\x02\x14\x02' (2A 00 00 00 00 04 06 01 10 01 10 01 0A 03 1B 02 48 01 14 04 09 02 12 03 0D 01 0D 02 09 03 22 01 14 02 16 01 14 02 0A 01 0D 01 0A 02 14 02),
000014BF             CODE:
                         argcount:
000014C0                     LONG: 3L (03 00 00 00)
                         nlocals:
000014C4                     LONG: 5L (05 00 00 00)
                         stacksize:
000014C8                     LONG: 4L (04 00 00 00)
                         flags:
000014CC                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000014D0                     STR: 't\x00\x00i\x01\x00|\x00\x00i\x03\x00\x83\x01\x00o\x0e\x00\x01d\x01\x00d\x01\x00f\x02\x00Sn\x01\x00\x01t\x04\x00|\x00\x00|\x01\x00\x83\x02\x00\\\x02\x00}\x04\x00}\x03\x00t\x08\x00t\t\x00|\x04\x00\x83\x01\x00t\n\x00i\x0b\x00\x14\x83\x01\x00}\x04\x00t\x00\x00i\x0c\x00d\x02\x00|\x04\x00|\x03\x00f\x02\x00\x16d\x03\x00\x83\x02\x00\x01|\x04\x00|\x03\x00f\x02\x00Sd\x00\x00S' (77 00 00 00 74 00 00 69 01 00 7C 00 00 69 03 00 83 01 00 6F 0E 00 01 64 01 00 64 01 00 66 02 00 53 6E 01 00 01 74 04 00 7C 00 00 7C 01 00 83 02 00 5C 02 00 7D 04 00 7D 03 00 74 08 00 74 09 00 7C 04 00 83 01 00 74 0A 00 69 0B 00 14 83 01 00 7D 04 00 74 00 00 69 0C 00 64 02 00 7C 04 00 7C 03 00 66 02 00 16 64 03 00 83 02 00 01 7C 04 00 7C 03 00 66 02 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CU'
                             00000003     69 - LOAD_ATTR           'isSpecialMove'
                             00000006     7C - LOAD_FAST           'winner'
                             00000009     69 - LOAD_ATTR           'requestedSpecialMove'
                             0000000C     83 - CALL_FUNCTION       r0001
                             0000000F     6F - JUMP_IF_FALSE       -> 00000020
                             00000012     01 - POP_TOP             
                             00000013     64 - LOAD_CONST          0
                             00000016     64 - LOAD_CONST          0
                             00000019     66 - BUILD_TUPLE         r0002
                             0000001C     53 - RETURN_VALUE        
                             0000001D     6E - JUMP_FORWARD        -> 00000021
                             00000020     01 - POP_TOP             
                             00000021     74 - LOAD_GLOBAL         'calcDamageForLoser'
                             00000024     7C - LOAD_FAST           'winner'
                             00000027     7C - LOAD_FAST           'loser'
                             0000002A     83 - CALL_FUNCTION       r0002
                             0000002D     5C - UNPACK_SEQUENCE     r0002
                             00000030     7D - STORE_FAST          'damage_taken'
                             00000033     7D - STORE_FAST          'damage_resisted'
                             00000036     74 - LOAD_GLOBAL         'int'
                             00000039     74 - LOAD_GLOBAL         'float'
                             0000003C     7C - LOAD_FAST           'damage_taken'
                             0000003F     83 - CALL_FUNCTION       r0001
                             00000042     74 - LOAD_GLOBAL         'consolevar'
                             00000045     69 - LOAD_ATTR           'CombatScaleDamage'
                             00000048     14 - BINARY_MULTIPLY     
                             00000049     83 - CALL_FUNCTION       r0001
                             0000004C     7D - STORE_FAST          'damage_taken'
                             0000004F     74 - LOAD_GLOBAL         'CU'
                             00000052     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000055     64 - LOAD_CONST          'Damage done: %d, Damage resisted: %d'
                             00000058     7C - LOAD_FAST           'damage_taken'
                             0000005B     7C - LOAD_FAST           'damage_resisted'
                             0000005E     66 - BUILD_TUPLE         r0002
                             00000061     16 - BINARY_MODULO       
                             00000062     64 - LOAD_CONST          2
                             00000065     83 - CALL_FUNCTION       r0002
                             00000068     01 - POP_TOP             
                             00000069     7C - LOAD_FAST           'damage_taken'
                             0000006C     7C - LOAD_FAST           'damage_resisted'
                             0000006F     66 - BUILD_TUPLE         r0002
                             00000072     53 - RETURN_VALUE        
                             00000073     64 - LOAD_CONST          None
                             00000076     53 - RETURN_VALUE        
                         consts:
0000154C                     TUPLE: (
00001551                         None (4E),
00001552                         INT: 0 (00 00 00 00),
00001557                         STR: 'Damage done: %d, Damage resisted: %d' (24 00 00 00 44 61 6D 61 67 65 20 64 6F 6E 65 3A 20 25 64 2C 20 44 61 6D 61 67 65 20 72 65 73 69 73 74 65 64 3A 20 25 64),
00001580                         INT: 2 (02 00 00 00)
                             )
                         names:
00001585                     TUPLE: (
0000158A                         STR: 'CU' (02 00 00 00 43 55),
00001591                         STR: 'isSpecialMove' (0D 00 00 00 69 73 53 70 65 63 69 61 6C 4D 6F 76 65),
000015A3                         STR: 'winner' (06 00 00 00 77 69 6E 6E 65 72),
000015AE                         STR: 'requestedSpecialMove' (14 00 00 00 72 65 71 75 65 73 74 65 64 53 70 65 63 69 61 6C 4D 6F 76 65),
000015C7                         STR: 'calcDamageForLoser' (12 00 00 00 63 61 6C 63 44 61 6D 61 67 65 46 6F 72 4C 6F 73 65 72),
000015DE                         STR: 'loser' (05 00 00 00 6C 6F 73 65 72),
000015E8                         STR: 'damage_taken' (0C 00 00 00 64 61 6D 61 67 65 5F 74 61 6B 65 6E),
000015F9                         STR: 'damage_resisted' (0F 00 00 00 64 61 6D 61 67 65 5F 72 65 73 69 73 74 65 64),
0000160D                         STR: 'int' (03 00 00 00 69 6E 74),
00001615                         STR: 'float' (05 00 00 00 66 6C 6F 61 74),
0000161F                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
0000162E                         STR: 'CombatScaleDamage' (11 00 00 00 43 6F 6D 62 61 74 53 63 61 6C 65 44 61 6D 61 67 65),
00001644                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65)
                             )
                         varnames:
00001661                     TUPLE: (
00001666                         STR: 'winner' (06 00 00 00 77 69 6E 6E 65 72),
00001671                         STR: 'loser' (05 00 00 00 6C 6F 73 65 72),
0000167B                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00001686                         STR: 'damage_resisted' (0F 00 00 00 64 61 6D 61 67 65 5F 72 65 73 69 73 74 65 64),
0000169A                         STR: 'damage_taken' (0C 00 00 00 64 61 6D 61 67 65 5F 74 61 6B 65 6E)
                             )
                         freevars:
000016AB                     TUPLE: ()
                         cellvars:
000016B0                     TUPLE: ()
                         filename:
000016B5                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_resolution.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 72 65 73 6F 6C 75 74 69 6F 6E 2E 70 79)
                         name:
0000170D                     STR: 'calculateDamage' (0F 00 00 00 63 61 6C 63 75 6C 61 74 65 44 61 6D 61 67 65)
                         firslineno:
00001721                     LONG: 157L (9D 00 00 00)
                         lnotab:
00001725                     STR: '\x00\x01\x13\x01\x0e\x02\x15\x01\x19\x02\x1a\x02' (0C 00 00 00 00 01 13 01 0E 02 15 01 19 02 1A 02),
00001736             CODE:
                         argcount:
00001737                     LONG: 3L (03 00 00 00)
                         nlocals:
0000173B                     LONG: 4L (04 00 00 00)
                         stacksize:
0000173F                     LONG: 3L (03 00 00 00)
                         flags:
00001743                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001747                     STR: 't\x00\x00i\x01\x00|\x00\x00\x83\x01\x00o\x18\x00\x01t\x00\x00i\x03\x00d\x01\x00d\x02\x00\x83\x02\x00\x01|\x01\x00Sn)\x00\x01t\x00\x00i\x01\x00|\x01\x00\x83\x01\x00o\x18\x00\x01t\x00\x00i\x03\x00d\x03\x00d\x02\x00\x83\x02\x00\x01|\x00\x00Sn\x01\x00\x01t\x00\x00i\x05\x00|\x00\x00\x83\x01\x00o\x08\x00\x01|\x01\x00Sn\x19\x00\x01t\x00\x00i\x05\x00|\x01\x00\x83\x01\x00o\x08\x00\x01|\x00\x00Sn\x01\x00\x01|\x00\x00i\x06\x00o\x08\x00\x01|\x00\x00Sn\x13\x00\x01|\x01\x00i\x06\x00o\x08\x00\x01|\x01\x00Sn\x01\x00\x01|\x00\x00i\x07\x00|\x01\x00i\x07\x00j\x03\x00o-\x00\x01t\x00\x00i\x08\x00|\x00\x00i\x07\x00|\x01\x00i\x07\x00\x83\x02\x00o\n\x00\x01|\x00\x00}\x03\x00q\r\x02\x01|\x01\x00}\x03\x00n*\x01\x01t\x00\x00i\n\x00|\x00\x00\x83\x01\x00o\r\x00\x01t\x00\x00i\n\x00|\x01\x00\x83\x01\x00oD\x00\x01|\x00\x00i\x0b\x00|\x01\x00i\x0c\x00j\x02\x00o\n\x00\x01|\x00\x00}\x03\x00n\x01\x00\x01|\x01\x00i\x0b\x00|\x00\x00i\x0c\x00j\x02\x00o\n\x00\x01|\x01\x00}\x03\x00q\r\x02\x01|\x00\x00}\x03\x00n\xc6\x00\x01t\x00\x00i\n\x00|\x00\x00\x83\x01\x00o!\x00\x01t\x00\x00i\x03\x00d\x04\x00|\x00\x00i\x0c\x00\x16d\x05\x00\x83\x02\x00\x01|\x01\x00}\x03\x00n\x95\x00\x01t\x00\x00i\n\x00|\x01\x00\x83\x01\x00o!\x00\x01t\x00\x00i\x03\x00d\x04\x00|\x01\x00i\x0c\x00\x16d\x05\x00\x83\x02\x00\x01|\x00\x00}\x03\x00nd\x00\x01|\x00\x00i\r\x00|\x01\x00i\r\x00j\x04\x00o\n\x00\x01|\x00\x00}\x03\x00nG\x00\x01|\x01\x00i\r\x00|\x00\x00i\r\x00j\x04\x00o\n\x00\x01|\x01\x00}\x03\x00n*\x00\x01t\x0e\x00i\x0f\x00d\x06\x00d\x07\x00\x83\x02\x00d\x06\x00j\x04\x00o\n\x00\x01|\x00\x00}\x03\x00n\x07\x00\x01|\x01\x00}\x03\x00|\x03\x00Sd\x00\x00S' (15 02 00 00 74 00 00 69 01 00 7C 00 00 83 01 00 6F 18 00 01 74 00 00 69 03 00 64 01 00 64 02 00 83 02 00 01 7C 01 00 53 6E 29 00 01 74 00 00 69 01 00 7C 01 00 83 01 00 6F 18 00 01 74 00 00 69 03 00 64 03 00 64 02 00 83 02 00 01 7C 00 00 53 6E 01 00 01 74 00 00 69 05 00 7C 00 00 83 01 00 6F 08 00 01 7C 01 00 53 6E 19 00 01 74 00 00 69 05 00 7C 01 00 83 01 00 6F 08 00 01 7C 00 00 53 6E 01 00 01 7C 00 00 69 06 00 6F 08 00 01 7C 00 00 53 6E 13 00 01 7C 01 00 69 06 00 6F 08 00 01 7C 01 00 53 6E 01 00 01 7C 00 00 69 07 00 7C 01 00 69 07 00 6A 03 00 6F 2D 00 01 74 00 00 69 08 00 7C 00 00 69 07 00 7C 01 00 69 07 00 83 02 00 6F 0A 00 01 7C 00 00 7D 03 00 71 0D 02 01 7C 01 00 7D 03 00 6E 2A 01 01 74 00 00 69 0A 00 7C 00 00 83 01 00 6F 0D 00 01 74 00 00 69 0A 00 7C 01 00 83 01 00 6F 44 00 01 7C 00 00 69 0B 00 7C 01 00 69 0C 00 6A 02 00 6F 0A 00 01 7C 00 00 7D 03 00 6E 01 00 01 7C 01 00 69 0B 00 7C 00 00 69 0C 00 6A 02 00 6F 0A 00 01 7C 01 00 7D 03 00 71 0D 02 01 7C 00 00 7D 03 00 6E C6 00 01 74 00 00 69 0A 00 7C 00 00 83 01 00 6F 21 00 01 74 00 00 69 03 00 64 04 00 7C 00 00 69 0C 00 16 64 05 00 83 02 00 01 7C 01 00 7D 03 00 6E 95 00 01 74 00 00 69 0A 00 7C 01 00 83 01 00 6F 21 00 01 74 00 00 69 03 00 64 04 00 7C 01 00 69 0C 00 16 64 05 00 83 02 00 01 7C 00 00 7D 03 00 6E 64 00 01 7C 00 00 69 0D 00 7C 01 00 69 0D 00 6A 04 00 6F 0A 00 01 7C 00 00 7D 03 00 6E 47 00 01 7C 01 00 69 0D 00 7C 00 00 69 0D 00 6A 04 00 6F 0A 00 01 7C 01 00 7D 03 00 6E 2A 00 01 74 0E 00 69 0F 00 64 06 00 64 07 00 83 02 00 64 06 00 6A 04 00 6F 0A 00 01 7C 00 00 7D 03 00 6E 07 00 01 7C 01 00 7D 03 00 7C 03 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CU'
                             00000003     69 - LOAD_ATTR           'isPlayerWithdrawing'
                             00000006     7C - LOAD_FAST           'player1'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     6F - JUMP_IF_FALSE       -> 00000027
                             0000000F     01 - POP_TOP             
                             00000010     74 - LOAD_GLOBAL         'CU'
                             00000013     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000016     64 - LOAD_CONST          'determineAttacker: Player 1 is withdrawing... player 2 is attacker'
                             00000019     64 - LOAD_CONST          13
                             0000001C     83 - CALL_FUNCTION       r0002
                             0000001F     01 - POP_TOP             
                             00000020     7C - LOAD_FAST           'player2'
                             00000023     53 - RETURN_VALUE        
                             00000024     6E - JUMP_FORWARD        -> 00000050
                             00000027     01 - POP_TOP             
                             00000028     74 - LOAD_GLOBAL         'CU'
                             0000002B     69 - LOAD_ATTR           'isPlayerWithdrawing'
                             0000002E     7C - LOAD_FAST           'player2'
                             00000031     83 - CALL_FUNCTION       r0001
                             00000034     6F - JUMP_IF_FALSE       -> 0000004F
                             00000037     01 - POP_TOP             
                             00000038     74 - LOAD_GLOBAL         'CU'
                             0000003B     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000003E     64 - LOAD_CONST          'determineAttacker: Player 2 is withdrawing... player 1 is attacker'
                             00000041     64 - LOAD_CONST          13
                             00000044     83 - CALL_FUNCTION       r0002
                             00000047     01 - POP_TOP             
                             00000048     7C - LOAD_FAST           'player1'
                             0000004B     53 - RETURN_VALUE        
                             0000004C     6E - JUMP_FORWARD        -> 00000050
                             0000004F     01 - POP_TOP             
                             00000050     74 - LOAD_GLOBAL         'CU'
                             00000053     69 - LOAD_ATTR           'isPlayerCombatProne'
                             00000056     7C - LOAD_FAST           'player1'
                             00000059     83 - CALL_FUNCTION       r0001
                             0000005C     6F - JUMP_IF_FALSE       -> 00000067
                             0000005F     01 - POP_TOP             
                             00000060     7C - LOAD_FAST           'player2'
                             00000063     53 - RETURN_VALUE        
                             00000064     6E - JUMP_FORWARD        -> 00000080
                             00000067     01 - POP_TOP             
                             00000068     74 - LOAD_GLOBAL         'CU'
                             0000006B     69 - LOAD_ATTR           'isPlayerCombatProne'
                             0000006E     7C - LOAD_FAST           'player2'
                             00000071     83 - CALL_FUNCTION       r0001
                             00000074     6F - JUMP_IF_FALSE       -> 0000007F
                             00000077     01 - POP_TOP             
                             00000078     7C - LOAD_FAST           'player1'
                             0000007B     53 - RETURN_VALUE        
                             0000007C     6E - JUMP_FORWARD        -> 00000080
                             0000007F     01 - POP_TOP             
                             00000080     7C - LOAD_FAST           'player1'
                             00000083     69 - LOAD_ATTR           'opportunityAttack'
                             00000086     6F - JUMP_IF_FALSE       -> 00000091
                             00000089     01 - POP_TOP             
                             0000008A     7C - LOAD_FAST           'player1'
                             0000008D     53 - RETURN_VALUE        
                             0000008E     6E - JUMP_FORWARD        -> 000000A4
                             00000091     01 - POP_TOP             
                             00000092     7C - LOAD_FAST           'player2'
                             00000095     69 - LOAD_ATTR           'opportunityAttack'
                             00000098     6F - JUMP_IF_FALSE       -> 000000A3
                             0000009B     01 - POP_TOP             
                             0000009C     7C - LOAD_FAST           'player2'
                             0000009F     53 - RETURN_VALUE        
                             000000A0     6E - JUMP_FORWARD        -> 000000A4
                             000000A3     01 - POP_TOP             
                             000000A4     7C - LOAD_FAST           'player1'
                             000000A7     69 - LOAD_ATTR           'tacticalSetting'
                             000000AA     7C - LOAD_FAST           'player2'
                             000000AD     69 - LOAD_ATTR           'tacticalSetting'
                             000000B0     6A - COMPARE_OP          "!="
                             000000B3     6F - JUMP_IF_FALSE       -> 000000E3
                             000000B6     01 - POP_TOP             
                             000000B7     74 - LOAD_GLOBAL         'CU'
                             000000BA     69 - LOAD_ATTR           'isPreferredTactical'
                             000000BD     7C - LOAD_FAST           'player1'
                             000000C0     69 - LOAD_ATTR           'tacticalSetting'
                             000000C3     7C - LOAD_FAST           'player2'
                             000000C6     69 - LOAD_ATTR           'tacticalSetting'
                             000000C9     83 - CALL_FUNCTION       r0002
                             000000CC     6F - JUMP_IF_FALSE       -> 000000D9
                             000000CF     01 - POP_TOP             
                             000000D0     7C - LOAD_FAST           'player1'
                             000000D3     7D - STORE_FAST          'attacker'
                             000000D6     71 - JUMP_ABSOLUTE       -> 0000020D
                             000000D9     01 - POP_TOP             
                             000000DA     7C - LOAD_FAST           'player2'
                             000000DD     7D - STORE_FAST          'attacker'
                             000000E0     6E - JUMP_FORWARD        -> 0000020D
                             000000E3     01 - POP_TOP             
                             000000E4     74 - LOAD_GLOBAL         'CU'
                             000000E7     69 - LOAD_ATTR           'isPlayerBeingGanged'
                             000000EA     7C - LOAD_FAST           'player1'
                             000000ED     83 - CALL_FUNCTION       r0001
                             000000F0     6F - JUMP_IF_FALSE       -> 00000100
                             000000F3     01 - POP_TOP             
                             000000F4     74 - LOAD_GLOBAL         'CU'
                             000000F7     69 - LOAD_ATTR           'isPlayerBeingGanged'
                             000000FA     7C - LOAD_FAST           'player2'
                             000000FD     83 - CALL_FUNCTION       r0001
                             00000100     6F - JUMP_IF_FALSE       -> 00000147
                             00000103     01 - POP_TOP             
                             00000104     7C - LOAD_FAST           'player1'
                             00000107     69 - LOAD_ATTR           'targetSlot'
                             0000010A     7C - LOAD_FAST           'player2'
                             0000010D     69 - LOAD_ATTR           'slot'
                             00000110     6A - COMPARE_OP          "=="
                             00000113     6F - JUMP_IF_FALSE       -> 00000120
                             00000116     01 - POP_TOP             
                             00000117     7C - LOAD_FAST           'player1'
                             0000011A     7D - STORE_FAST          'attacker'
                             0000011D     6E - JUMP_FORWARD        -> 00000121
                             00000120     01 - POP_TOP             
                             00000121     7C - LOAD_FAST           'player2'
                             00000124     69 - LOAD_ATTR           'targetSlot'
                             00000127     7C - LOAD_FAST           'player1'
                             0000012A     69 - LOAD_ATTR           'slot'
                             0000012D     6A - COMPARE_OP          "=="
                             00000130     6F - JUMP_IF_FALSE       -> 0000013D
                             00000133     01 - POP_TOP             
                             00000134     7C - LOAD_FAST           'player2'
                             00000137     7D - STORE_FAST          'attacker'
                             0000013A     71 - JUMP_ABSOLUTE       -> 0000020D
                             0000013D     01 - POP_TOP             
                             0000013E     7C - LOAD_FAST           'player1'
                             00000141     7D - STORE_FAST          'attacker'
                             00000144     6E - JUMP_FORWARD        -> 0000020D
                             00000147     01 - POP_TOP             
                             00000148     74 - LOAD_GLOBAL         'CU'
                             0000014B     69 - LOAD_ATTR           'isPlayerBeingGanged'
                             0000014E     7C - LOAD_FAST           'player1'
                             00000151     83 - CALL_FUNCTION       r0001
                             00000154     6F - JUMP_IF_FALSE       -> 00000178
                             00000157     01 - POP_TOP             
                             00000158     74 - LOAD_GLOBAL         'CU'
                             0000015B     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000015E     64 - LOAD_CONST          'determineAttacker() player %d being ganged'
                             00000161     7C - LOAD_FAST           'player1'
                             00000164     69 - LOAD_ATTR           'slot'
                             00000167     16 - BINARY_MODULO       
                             00000168     64 - LOAD_CONST          3
                             0000016B     83 - CALL_FUNCTION       r0002
                             0000016E     01 - POP_TOP             
                             0000016F     7C - LOAD_FAST           'player2'
                             00000172     7D - STORE_FAST          'attacker'
                             00000175     6E - JUMP_FORWARD        -> 0000020D
                             00000178     01 - POP_TOP             
                             00000179     74 - LOAD_GLOBAL         'CU'
                             0000017C     69 - LOAD_ATTR           'isPlayerBeingGanged'
                             0000017F     7C - LOAD_FAST           'player2'
                             00000182     83 - CALL_FUNCTION       r0001
                             00000185     6F - JUMP_IF_FALSE       -> 000001A9
                             00000188     01 - POP_TOP             
                             00000189     74 - LOAD_GLOBAL         'CU'
                             0000018C     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000018F     64 - LOAD_CONST          'determineAttacker() player %d being ganged'
                             00000192     7C - LOAD_FAST           'player2'
                             00000195     69 - LOAD_ATTR           'slot'
                             00000198     16 - BINARY_MODULO       
                             00000199     64 - LOAD_CONST          3
                             0000019C     83 - CALL_FUNCTION       r0002
                             0000019F     01 - POP_TOP             
                             000001A0     7C - LOAD_FAST           'player1'
                             000001A3     7D - STORE_FAST          'attacker'
                             000001A6     6E - JUMP_FORWARD        -> 0000020D
                             000001A9     01 - POP_TOP             
                             000001AA     7C - LOAD_FAST           'player1'
                             000001AD     69 - LOAD_ATTR           'abilityLevel'
                             000001B0     7C - LOAD_FAST           'player2'
                             000001B3     69 - LOAD_ATTR           'abilityLevel'
                             000001B6     6A - COMPARE_OP          ">"
                             000001B9     6F - JUMP_IF_FALSE       -> 000001C6
                             000001BC     01 - POP_TOP             
                             000001BD     7C - LOAD_FAST           'player1'
                             000001C0     7D - STORE_FAST          'attacker'
                             000001C3     6E - JUMP_FORWARD        -> 0000020D
                             000001C6     01 - POP_TOP             
                             000001C7     7C - LOAD_FAST           'player2'
                             000001CA     69 - LOAD_ATTR           'abilityLevel'
                             000001CD     7C - LOAD_FAST           'player1'
                             000001D0     69 - LOAD_ATTR           'abilityLevel'
                             000001D3     6A - COMPARE_OP          ">"
                             000001D6     6F - JUMP_IF_FALSE       -> 000001E3
                             000001D9     01 - POP_TOP             
                             000001DA     7C - LOAD_FAST           'player2'
                             000001DD     7D - STORE_FAST          'attacker'
                             000001E0     6E - JUMP_FORWARD        -> 0000020D
                             000001E3     01 - POP_TOP             
                             000001E4     74 - LOAD_GLOBAL         'random'
                             000001E7     69 - LOAD_ATTR           'randint'
                             000001EA     64 - LOAD_CONST          0
                             000001ED     64 - LOAD_CONST          1
                             000001F0     83 - CALL_FUNCTION       r0002
                             000001F3     64 - LOAD_CONST          0
                             000001F6     6A - COMPARE_OP          ">"
                             000001F9     6F - JUMP_IF_FALSE       -> 00000206
                             000001FC     01 - POP_TOP             
                             000001FD     7C - LOAD_FAST           'player1'
                             00000200     7D - STORE_FAST          'attacker'
                             00000203     6E - JUMP_FORWARD        -> 0000020D
                             00000206     01 - POP_TOP             
                             00000207     7C - LOAD_FAST           'player2'
                             0000020A     7D - STORE_FAST          'attacker'
                             0000020D     7C - LOAD_FAST           'attacker'
                             00000210     53 - RETURN_VALUE        
                             00000211     64 - LOAD_CONST          None
                             00000214     53 - RETURN_VALUE        
                         consts:
00001961                     TUPLE: (
00001966                         None (4E),
00001967                         STR: 'determineAttacker: Player 1 is withdrawing... player 2 is attacker' (42 00 00 00 64 65 74 65 72 6D 69 6E 65 41 74 74 61 63 6B 65 72 3A 20 50 6C 61 79 65 72 20 31 20 69 73 20 77 69 74 68 64 72 61 77 69 6E 67 2E 2E 2E 20 70 6C 61 79 65 72 20 32 20 69 73 20 61 74 74 61 63 6B 65 72),
000019AE                         INT: 13 (0D 00 00 00),
000019B3                         STR: 'determineAttacker: Player 2 is withdrawing... player 1 is attacker' (42 00 00 00 64 65 74 65 72 6D 69 6E 65 41 74 74 61 63 6B 65 72 3A 20 50 6C 61 79 65 72 20 32 20 69 73 20 77 69 74 68 64 72 61 77 69 6E 67 2E 2E 2E 20 70 6C 61 79 65 72 20 31 20 69 73 20 61 74 74 61 63 6B 65 72),
000019FA                         STR: 'determineAttacker() player %d being ganged' (2A 00 00 00 64 65 74 65 72 6D 69 6E 65 41 74 74 61 63 6B 65 72 28 29 20 70 6C 61 79 65 72 20 25 64 20 62 65 69 6E 67 20 67 61 6E 67 65 64),
00001A29                         INT: 3 (03 00 00 00),
00001A2E                         INT: 0 (00 00 00 00),
00001A33                         INT: 1 (01 00 00 00)
                             )
                         names:
00001A38                     TUPLE: (
00001A3D                         STR: 'CU' (02 00 00 00 43 55),
00001A44                         STR: 'isPlayerWithdrawing' (13 00 00 00 69 73 50 6C 61 79 65 72 57 69 74 68 64 72 61 77 69 6E 67),
00001A5C                         STR: 'player1' (07 00 00 00 70 6C 61 79 65 72 31),
00001A68                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
00001A85                         STR: 'player2' (07 00 00 00 70 6C 61 79 65 72 32),
00001A91                         STR: 'isPlayerCombatProne' (13 00 00 00 69 73 50 6C 61 79 65 72 43 6F 6D 62 61 74 50 72 6F 6E 65),
00001AA9                         STR: 'opportunityAttack' (11 00 00 00 6F 70 70 6F 72 74 75 6E 69 74 79 41 74 74 61 63 6B),
00001ABF                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
00001AD3                         STR: 'isPreferredTactical' (13 00 00 00 69 73 50 72 65 66 65 72 72 65 64 54 61 63 74 69 63 61 6C),
00001AEB                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
00001AF8                         STR: 'isPlayerBeingGanged' (13 00 00 00 69 73 50 6C 61 79 65 72 42 65 69 6E 67 47 61 6E 67 65 64),
00001B10                         STR: 'targetSlot' (0A 00 00 00 74 61 72 67 65 74 53 6C 6F 74),
00001B1F                         STR: 'slot' (04 00 00 00 73 6C 6F 74),
00001B28                         STR: 'abilityLevel' (0C 00 00 00 61 62 69 6C 69 74 79 4C 65 76 65 6C),
00001B39                         STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00001B44                         STR: 'randint' (07 00 00 00 72 61 6E 64 69 6E 74)
                             )
                         varnames:
00001B50                     TUPLE: (
00001B55                         STR: 'player1' (07 00 00 00 70 6C 61 79 65 72 31),
00001B61                         STR: 'player2' (07 00 00 00 70 6C 61 79 65 72 32),
00001B6D                         STR: 'combat_range' (0C 00 00 00 63 6F 6D 62 61 74 5F 72 61 6E 67 65),
00001B7E                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72)
                             )
                         freevars:
00001B8B                     TUPLE: ()
                         cellvars:
00001B90                     TUPLE: ()
                         filename:
00001B95                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_resolution.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 72 65 73 6F 6C 75 74 69 6F 6E 2E 70 79)
                         name:
00001BED                     STR: 'determineAttacker' (11 00 00 00 64 65 74 65 72 6D 69 6E 65 41 74 74 61 63 6B 65 72)
                         firslineno:
00001C03                     LONG: 169L (A9 00 00 00)
                         lnotab:
00001C07                     STR: '\x00\x03\x10\x01\x10\x01\x08\x01\x10\x01\x10\x01\x08\x03\x10\x01\x08\x01\x10\x01\x08\x03\n\x01\x08\x01\n\x01\x08\x03\x13\x02\x19\x01\n\x02\n\x05 \x02\x13\x01\n\x01\x13\x01\n\x03\n\x02\x10\x01\x17\x01\n\x01\x10\x01\x17\x01\n\x03\x13\x01\n\x01\x13\x01\n\x03\x19\x01\n\x02\x06\x02' (4C 00 00 00 00 03 10 01 10 01 08 01 10 01 10 01 08 03 10 01 08 01 10 01 08 03 0A 01 08 01 0A 01 08 03 13 02 19 01 0A 02 0A 05 20 02 13 01 0A 01 13 01 0A 03 0A 02 10 01 17 01 0A 01 10 01 17 01 0A 03 13 01 0A 01 13 01 0A 03 19 01 0A 02 06 02),
00001C58             CODE:
                         argcount:
00001C59                     LONG: 2L (02 00 00 00)
                         nlocals:
00001C5D                     LONG: 2L (02 00 00 00)
                         stacksize:
00001C61                     LONG: 3L (03 00 00 00)
                         flags:
00001C65                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001C69                     STR: 't\x00\x00i\x01\x00d\x01\x00d\x02\x00\x83\x02\x00\x01|\x00\x00i\x03\x00|\x01\x00_\x05\x00t\x06\x00i\x07\x00i\x08\x00|\x01\x00_\t\x00d\x03\x00|\x01\x00_\n\x00d\x03\x00|\x01\x00_\x0b\x00d\x00\x00S' (41 00 00 00 74 00 00 69 01 00 64 01 00 64 02 00 83 02 00 01 7C 00 00 69 03 00 7C 01 00 5F 05 00 74 06 00 69 07 00 69 08 00 7C 01 00 5F 09 00 64 03 00 7C 01 00 5F 0A 00 64 03 00 7C 01 00 5F 0B 00 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CU'
                             00000003     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000006     64 - LOAD_CONST          'Short circuiting for special move, true_attacker is winner'
                             00000009     64 - LOAD_CONST          3
                             0000000C     83 - CALL_FUNCTION       r0002
                             0000000F     01 - POP_TOP             
                             00000010     7C - LOAD_FAST           'attacker'
                             00000013     69 - LOAD_ATTR           'slot'
                             00000016     7C - LOAD_FAST           'result'
                             00000019     5F - STORE_ATTR          'winnerSlot'
                             0000001C     74 - LOAD_GLOBAL         'constants'
                             0000001F     69 - LOAD_ATTR           'combat'
                             00000022     69 - LOAD_ATTR           'SPECIAL_MOVE'
                             00000025     7C - LOAD_FAST           'result'
                             00000028     5F - STORE_ATTR          'outcomeFlag'
                             0000002B     64 - LOAD_CONST          0
                             0000002E     7C - LOAD_FAST           'result'
                             00000031     5F - STORE_ATTR          'winnerDamage'
                             00000034     64 - LOAD_CONST          0
                             00000037     7C - LOAD_FAST           'result'
                             0000003A     5F - STORE_ATTR          'loserDamage'
                             0000003D     64 - LOAD_CONST          None
                             00000040     53 - RETURN_VALUE        
                         consts:
00001CAF                     TUPLE: (
00001CB4                         None (4E),
00001CB5                         STR: 'Short circuiting for special move, true_attacker is winner' (3A 00 00 00 53 68 6F 72 74 20 63 69 72 63 75 69 74 69 6E 67 20 66 6F 72 20 73 70 65 63 69 61 6C 20 6D 6F 76 65 2C 20 74 72 75 65 5F 61 74 74 61 63 6B 65 72 20 69 73 20 77 69 6E 6E 65 72),
00001CF4                         INT: 3 (03 00 00 00),
00001CF9                         INT: 0 (00 00 00 00)
                             )
                         names:
00001CFE                     TUPLE: (
00001D03                         STR: 'CU' (02 00 00 00 43 55),
00001D0A                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
00001D27                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
00001D34                         STR: 'slot' (04 00 00 00 73 6C 6F 74),
00001D3D                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00001D48                         STR: 'winnerSlot' (0A 00 00 00 77 69 6E 6E 65 72 53 6C 6F 74),
00001D57                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00001D65                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
00001D70                         STR: 'SPECIAL_MOVE' (0C 00 00 00 53 50 45 43 49 41 4C 5F 4D 4F 56 45),
00001D81                         STR: 'outcomeFlag' (0B 00 00 00 6F 75 74 63 6F 6D 65 46 6C 61 67),
00001D91                         STR: 'winnerDamage' (0C 00 00 00 77 69 6E 6E 65 72 44 61 6D 61 67 65),
00001DA2                         STR: 'loserDamage' (0B 00 00 00 6C 6F 73 65 72 44 61 6D 61 67 65)
                             )
                         varnames:
00001DB2                     TUPLE: (
00001DB7                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
00001DC4                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74)
                             )
                         freevars:
00001DCF                     TUPLE: ()
                         cellvars:
00001DD4                     TUPLE: ()
                         filename:
00001DD9                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_resolution.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 72 65 73 6F 6C 75 74 69 6F 6E 2E 70 79)
                         name:
00001E31                     STR: 'handleSpecialMove' (11 00 00 00 68 61 6E 64 6C 65 53 70 65 63 69 61 6C 4D 6F 76 65)
                         firslineno:
00001E47                     LONG: 233L (E9 00 00 00)
                         lnotab:
00001E4B                     STR: '\x00\x01\x10\x01\x0c\x01\x0f\x01\t\x01' (0A 00 00 00 00 01 10 01 0C 01 0F 01 09 01),
00001E5A             CODE:
                         argcount:
00001E5B                     LONG: 4L (04 00 00 00)
                         nlocals:
00001E5F                     LONG: 4L (04 00 00 00)
                         stacksize:
00001E63                     LONG: 4L (04 00 00 00)
                         flags:
00001E67                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00001E6B                     STR: 't\x00\x00i\x01\x00d\x01\x00d\x02\x00\x83\x02\x00\x01|\x00\x00i\x03\x00|\x02\x00_\x05\x00|\x03\x00|\x00\x00j\x02\x00oK\x00\x01t\x00\x00i\x01\x00d\x03\x00d\x02\x00\x83\x02\x00\x01t\x07\x00i\x08\x00i\t\x00t\x07\x00i\x08\x00i\n\x00B|\x02\x00_\x0b\x00t\x0c\x00|\x00\x00|\x01\x00|\x02\x00\x83\x03\x00\\\x02\x00|\x02\x00_\x0e\x00|\x02\x00_\x0f\x00nH\x00\x01t\x00\x00i\x01\x00d\x04\x00d\x02\x00\x83\x02\x00\x01t\x07\x00i\x08\x00i\x10\x00t\x07\x00i\x08\x00i\n\x00B|\x02\x00_\x0b\x00t\x0c\x00|\x01\x00|\x00\x00|\x02\x00\x83\x03\x00\\\x02\x00|\x02\x00_\x11\x00|\x02\x00_\x12\x00d\x00\x00S' (BF 00 00 00 74 00 00 69 01 00 64 01 00 64 02 00 83 02 00 01 7C 00 00 69 03 00 7C 02 00 5F 05 00 7C 03 00 7C 00 00 6A 02 00 6F 4B 00 01 74 00 00 69 01 00 64 03 00 64 02 00 83 02 00 01 74 07 00 69 08 00 69 09 00 74 07 00 69 08 00 69 0A 00 42 7C 02 00 5F 0B 00 74 0C 00 7C 00 00 7C 01 00 7C 02 00 83 03 00 5C 02 00 7C 02 00 5F 0E 00 7C 02 00 5F 0F 00 6E 48 00 01 74 00 00 69 01 00 64 04 00 64 02 00 83 02 00 01 74 07 00 69 08 00 69 10 00 74 07 00 69 08 00 69 0A 00 42 7C 02 00 5F 0B 00 74 0C 00 7C 01 00 7C 00 00 7C 02 00 83 03 00 5C 02 00 7C 02 00 5F 11 00 7C 02 00 5F 12 00 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CU'
                             00000003     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000006     64 - LOAD_CONST          'handleOppertunityAttack: Handling attacker opportunity attack'
                             00000009     64 - LOAD_CONST          3
                             0000000C     83 - CALL_FUNCTION       r0002
                             0000000F     01 - POP_TOP             
                             00000010     7C - LOAD_FAST           'attacker'
                             00000013     69 - LOAD_ATTR           'slot'
                             00000016     7C - LOAD_FAST           'result'
                             00000019     5F - STORE_ATTR          'winnerSlot'
                             0000001C     7C - LOAD_FAST           'true_attacker'
                             0000001F     7C - LOAD_FAST           'attacker'
                             00000022     6A - COMPARE_OP          "=="
                             00000025     6F - JUMP_IF_FALSE       -> 00000073
                             00000028     01 - POP_TOP             
                             00000029     74 - LOAD_GLOBAL         'CU'
                             0000002C     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000002F     64 - LOAD_CONST          'handleOppertunityAttack: Attacker wins'
                             00000032     64 - LOAD_CONST          3
                             00000035     83 - CALL_FUNCTION       r0002
                             00000038     01 - POP_TOP             
                             00000039     74 - LOAD_GLOBAL         'constants'
                             0000003C     69 - LOAD_ATTR           'combat'
                             0000003F     69 - LOAD_ATTR           'AHITS_DMISSES'
                             00000042     74 - LOAD_GLOBAL         'constants'
                             00000045     69 - LOAD_ATTR           'combat'
                             00000048     69 - LOAD_ATTR           'OPPORTUNITY_ATTACK'
                             0000004B     42 - BINARY_OR           
                             0000004C     7C - LOAD_FAST           'result'
                             0000004F     5F - STORE_ATTR          'outcomeFlag'
                             00000052     74 - LOAD_GLOBAL         'calculateDamage'
                             00000055     7C - LOAD_FAST           'attacker'
                             00000058     7C - LOAD_FAST           'defender'
                             0000005B     7C - LOAD_FAST           'result'
                             0000005E     83 - CALL_FUNCTION       r0003
                             00000061     5C - UNPACK_SEQUENCE     r0002
                             00000064     7C - LOAD_FAST           'result'
                             00000067     5F - STORE_ATTR          'loserDamage'
                             0000006A     7C - LOAD_FAST           'result'
                             0000006D     5F - STORE_ATTR          'loserDamageAbsorbed'
                             00000070     6E - JUMP_FORWARD        -> 000000BB
                             00000073     01 - POP_TOP             
                             00000074     74 - LOAD_GLOBAL         'CU'
                             00000077     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000007A     64 - LOAD_CONST          'handleOppertunityAttack: Defender wins'
                             0000007D     64 - LOAD_CONST          3
                             00000080     83 - CALL_FUNCTION       r0002
                             00000083     01 - POP_TOP             
                             00000084     74 - LOAD_GLOBAL         'constants'
                             00000087     69 - LOAD_ATTR           'combat'
                             0000008A     69 - LOAD_ATTR           'DRAW'
                             0000008D     74 - LOAD_GLOBAL         'constants'
                             00000090     69 - LOAD_ATTR           'combat'
                             00000093     69 - LOAD_ATTR           'OPPORTUNITY_ATTACK'
                             00000096     42 - BINARY_OR           
                             00000097     7C - LOAD_FAST           'result'
                             0000009A     5F - STORE_ATTR          'outcomeFlag'
                             0000009D     74 - LOAD_GLOBAL         'calculateDamage'
                             000000A0     7C - LOAD_FAST           'defender'
                             000000A3     7C - LOAD_FAST           'attacker'
                             000000A6     7C - LOAD_FAST           'result'
                             000000A9     83 - CALL_FUNCTION       r0003
                             000000AC     5C - UNPACK_SEQUENCE     r0002
                             000000AF     7C - LOAD_FAST           'result'
                             000000B2     5F - STORE_ATTR          'winnerDamage'
                             000000B5     7C - LOAD_FAST           'result'
                             000000B8     5F - STORE_ATTR          'winnerDamageAbsorbed'
                             000000BB     64 - LOAD_CONST          None
                             000000BE     53 - RETURN_VALUE        
                         consts:
00001F2F                     TUPLE: (
00001F34                         None (4E),
00001F35                         STR: 'handleOppertunityAttack: Handling attacker opportunity attack' (3D 00 00 00 68 61 6E 64 6C 65 4F 70 70 65 72 74 75 6E 69 74 79 41 74 74 61 63 6B 3A 20 48 61 6E 64 6C 69 6E 67 20 61 74 74 61 63 6B 65 72 20 6F 70 70 6F 72 74 75 6E 69 74 79 20 61 74 74 61 63 6B),
00001F77                         INT: 3 (03 00 00 00),
00001F7C                         STR: 'handleOppertunityAttack: Attacker wins' (26 00 00 00 68 61 6E 64 6C 65 4F 70 70 65 72 74 75 6E 69 74 79 41 74 74 61 63 6B 3A 20 41 74 74 61 63 6B 65 72 20 77 69 6E 73),
00001FA7                         STR: 'handleOppertunityAttack: Defender wins' (26 00 00 00 68 61 6E 64 6C 65 4F 70 70 65 72 74 75 6E 69 74 79 41 74 74 61 63 6B 3A 20 44 65 66 65 6E 64 65 72 20 77 69 6E 73)
                             )
                         names:
00001FD2                     TUPLE: (
00001FD7                         STR: 'CU' (02 00 00 00 43 55),
00001FDE                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
00001FFB                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
00002008                         STR: 'slot' (04 00 00 00 73 6C 6F 74),
00002011                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
0000201C                         STR: 'winnerSlot' (0A 00 00 00 77 69 6E 6E 65 72 53 6C 6F 74),
0000202B                         STR: 'true_attacker' (0D 00 00 00 74 72 75 65 5F 61 74 74 61 63 6B 65 72),
0000203D                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
0000204B                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
00002056                         STR: 'AHITS_DMISSES' (0D 00 00 00 41 48 49 54 53 5F 44 4D 49 53 53 45 53),
00002068                         STR: 'OPPORTUNITY_ATTACK' (12 00 00 00 4F 50 50 4F 52 54 55 4E 49 54 59 5F 41 54 54 41 43 4B),
0000207F                         STR: 'outcomeFlag' (0B 00 00 00 6F 75 74 63 6F 6D 65 46 6C 61 67),
0000208F                         STR: 'calculateDamage' (0F 00 00 00 63 61 6C 63 75 6C 61 74 65 44 61 6D 61 67 65),
000020A3                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
000020B0                         STR: 'loserDamage' (0B 00 00 00 6C 6F 73 65 72 44 61 6D 61 67 65),
000020C0                         STR: 'loserDamageAbsorbed' (13 00 00 00 6C 6F 73 65 72 44 61 6D 61 67 65 41 62 73 6F 72 62 65 64),
000020D8                         STR: 'DRAW' (04 00 00 00 44 52 41 57),
000020E1                         STR: 'winnerDamage' (0C 00 00 00 77 69 6E 6E 65 72 44 61 6D 61 67 65),
000020F2                         STR: 'winnerDamageAbsorbed' (14 00 00 00 77 69 6E 6E 65 72 44 61 6D 61 67 65 41 62 73 6F 72 62 65 64)
                             )
                         varnames:
0000210B                     TUPLE: (
00002110                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
0000211D                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
0000212A                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00002135                         STR: 'true_attacker' (0D 00 00 00 74 72 75 65 5F 61 74 74 61 63 6B 65 72)
                             )
                         freevars:
00002147                     TUPLE: ()
                         cellvars:
0000214C                     TUPLE: ()
                         filename:
00002151                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_resolution.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 72 65 73 6F 6C 75 74 69 6F 6E 2E 70 79)
                         name:
000021A9                     STR: 'handleOppertunityAttack' (17 00 00 00 68 61 6E 64 6C 65 4F 70 70 65 72 74 75 6E 69 74 79 41 74 74 61 63 6B)
                         firslineno:
000021C5                     LONG: 240L (F0 00 00 00)
                         lnotab:
000021C9                     STR: '\x00\x01\x10\x01\x0c\x02\r\x01\x10\x01\x19\x01"\x02\x10\x01\x19\x01' (12 00 00 00 00 01 10 01 0C 02 0D 01 10 01 19 01 22 02 10 01 19 01),
000021E0             CODE:
                         argcount:
000021E1                     LONG: 5L (05 00 00 00)
                         nlocals:
000021E5                     LONG: 12L (0C 00 00 00)
                         stacksize:
000021E9                     LONG: 5L (05 00 00 00)
                         flags:
000021ED                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000021F1                     STR: 't\x00\x00i\x01\x00d\x01\x00d\x02\x00\x83\x02\x00\x01|\x00\x00i\x03\x00|\x02\x00_\x05\x00t\x06\x00}\x05\x00|\x03\x00oB\x00\x01t\t\x00|\x00\x00|\x01\x00|\x02\x00\x83\x03\x00\\\x02\x00|\x02\x00_\x0b\x00|\x02\x00_\x0c\x00t\x00\x00i\x01\x00d\x03\x00|\x02\x00i\x0b\x00|\x02\x00i\x0c\x00f\x02\x00\x16d\x04\x00\x83\x02\x00\x01n\x01\x00\x01|\x04\x00oB\x00\x01t\t\x00|\x01\x00|\x00\x00|\x02\x00\x83\x03\x00\\\x02\x00|\x02\x00_\x0e\x00|\x02\x00_\x0f\x00t\x00\x00i\x01\x00d\x05\x00|\x02\x00i\x0e\x00|\x02\x00i\x0f\x00f\x02\x00\x16d\x04\x00\x83\x02\x00\x01n\x01\x00\x01|\x03\x00o\x04\x00\x01|\x04\x00o#\x00\x01t\x00\x00i\x01\x00d\x06\x00d\x02\x00\x83\x02\x00\x01t\x10\x00i\x11\x00i\x12\x00|\x02\x00_\x13\x00n\x98\x00\x01|\x03\x00o\x05\x00\x01|\x04\x00\x0co#\x00\x01t\x00\x00i\x01\x00d\x07\x00d\x02\x00\x83\x02\x00\x01t\x10\x00i\x11\x00i\x14\x00|\x02\x00_\x13\x00nf\x00\x01|\x03\x00\x0co\x04\x00\x01|\x04\x00o#\x00\x01t\x00\x00i\x01\x00d\x08\x00d\x02\x00\x83\x02\x00\x01t\x10\x00i\x11\x00i\x15\x00|\x02\x00_\x13\x00n4\x00\x01|\x03\x00\x0co\x05\x00\x01|\x04\x00\x0co#\x00\x01t\x00\x00i\x01\x00d\t\x00d\x02\x00\x83\x02\x00\x01t\x10\x00i\x11\x00i\x16\x00|\x02\x00_\x13\x00n\x01\x00\x01t\x00\x00i\x17\x00|\x00\x00|\x01\x00|\x02\x00t\x06\x00\x83\x04\x00}\n\x00t\x00\x00i\x17\x00|\x00\x00|\x01\x00|\x02\x00t\x19\x00\x83\x04\x00}\x0b\x00|\n\x00\x0co\x1b\x00\x01|\x0b\x00\x0co\x13\x00\x01t\x00\x00i\x1b\x00|\x00\x00|\x01\x00|\x02\x00\x83\x03\x00o*\x00\x01|\x02\x00i\x13\x00t\x10\x00i\x11\x00i\x1c\x00B|\x02\x00_\x13\x00t\x00\x00i\x01\x00d\n\x00d\x02\x00\x83\x02\x00\x01nQ\x01\x01|\n\x00p\x04\x00\x01|\x0b\x00oB\x01\x01|\x02\x00i\x13\x00t\x10\x00i\x11\x00i\x12\x00j\x02\x00o\x02\x01\x01|\n\x00o\x05\x00\x01|\x0b\x00\x0co~\x00\x01|\x02\x00i\x13\x00t\x10\x00i\x11\x00i\x1d\x00B|\x02\x00_\x13\x00t\x00\x00i\x01\x00d\x0b\x00d\x02\x00\x83\x02\x00\x01|\x01\x00i\x03\x00|\x02\x00_\x05\x00|\x02\x00i\x0b\x00}\x06\x00|\x02\x00i\x0c\x00}\x07\x00|\x02\x00i\x0e\x00}\x08\x00|\x02\x00i\x0f\x00}\t\x00|\t\x00|\x02\x00_\x0b\x00|\x08\x00|\x02\x00_\x0c\x00|\x06\x00|\x02\x00_\x0e\x00|\x07\x00|\x02\x00_\x0f\x00qH\x03\x01|\n\x00\x0co\x04\x00\x01|\x0b\x00o*\x00\x01|\x02\x00i\x13\x00t\x10\x00i\x11\x00i\x1d\x00B|\x02\x00_\x13\x00t\x00\x00i\x01\x00d\x0c\x00d\x02\x00\x83\x02\x00\x01qH\x03\x01|\n\x00o\x04\x00\x01|\x0b\x00o*\x00\x01|\x02\x00i\x13\x00t\x10\x00i\x11\x00i"\x00B|\x02\x00_\x13\x00t\x00\x00i\x01\x00d\r\x00d\x02\x00\x83\x02\x00\x01qH\x03\x01qL\x03\x01|\x02\x00i\x13\x00t\x10\x00i\x11\x00i\x1d\x00B|\x02\x00_\x13\x00t\x00\x00i\x01\x00d\x0e\x00d\x02\x00\x83\x02\x00\x01n\x01\x00\x01|\x05\x00Sd\x00\x00S' (54 03 00 00 74 00 00 69 01 00 64 01 00 64 02 00 83 02 00 01 7C 00 00 69 03 00 7C 02 00 5F 05 00 74 06 00 7D 05 00 7C 03 00 6F 42 00 01 74 09 00 7C 00 00 7C 01 00 7C 02 00 83 03 00 5C 02 00 7C 02 00 5F 0B 00 7C 02 00 5F 0C 00 74 00 00 69 01 00 64 03 00 7C 02 00 69 0B 00 7C 02 00 69 0C 00 66 02 00 16 64 04 00 83 02 00 01 6E 01 00 01 7C 04 00 6F 42 00 01 74 09 00 7C 01 00 7C 00 00 7C 02 00 83 03 00 5C 02 00 7C 02 00 5F 0E 00 7C 02 00 5F 0F 00 74 00 00 69 01 00 64 05 00 7C 02 00 69 0E 00 7C 02 00 69 0F 00 66 02 00 16 64 04 00 83 02 00 01 6E 01 00 01 7C 03 00 6F 04 00 01 7C 04 00 6F 23 00 01 74 00 00 69 01 00 64 06 00 64 02 00 83 02 00 01 74 10 00 69 11 00 69 12 00 7C 02 00 5F 13 00 6E 98 00 01 7C 03 00 6F 05 00 01 7C 04 00 0C 6F 23 00 01 74 00 00 69 01 00 64 07 00 64 02 00 83 02 00 01 74 10 00 69 11 00 69 14 00 7C 02 00 5F 13 00 6E 66 00 01 7C 03 00 0C 6F 04 00 01 7C 04 00 6F 23 00 01 74 00 00 69 01 00 64 08 00 64 02 00 83 02 00 01 74 10 00 69 11 00 69 15 00 7C 02 00 5F 13 00 6E 34 00 01 7C 03 00 0C 6F 05 00 01 7C 04 00 0C 6F 23 00 01 74 00 00 69 01 00 64 09 00 64 02 00 83 02 00 01 74 10 00 69 11 00 69 16 00 7C 02 00 5F 13 00 6E 01 00 01 74 00 00 69 17 00 7C 00 00 7C 01 00 7C 02 00 74 06 00 83 04 00 7D 0A 00 74 00 00 69 17 00 7C 00 00 7C 01 00 7C 02 00 74 19 00 83 04 00 7D 0B 00 7C 0A 00 0C 6F 1B 00 01 7C 0B 00 0C 6F 13 00 01 74 00 00 69 1B 00 7C 00 00 7C 01 00 7C 02 00 83 03 00 6F 2A 00 01 7C 02 00 69 13 00 74 10 00 69 11 00 69 1C 00 42 7C 02 00 5F 13 00 74 00 00 69 01 00 64 0A 00 64 02 00 83 02 00 01 6E 51 01 01 7C 0A 00 70 04 00 01 7C 0B 00 6F 42 01 01 7C 02 00 69 13 00 74 10 00 69 11 00 69 12 00 6A 02 00 6F 02 01 01 7C 0A 00 6F 05 00 01 7C 0B 00 0C 6F 7E 00 01 7C 02 00 69 13 00 74 10 00 69 11 00 69 1D 00 42 7C 02 00 5F 13 00 74 00 00 69 01 00 64 0B 00 64 02 00 83 02 00 01 7C 01 00 69 03 00 7C 02 00 5F 05 00 7C 02 00 69 0B 00 7D 06 00 7C 02 00 69 0C 00 7D 07 00 7C 02 00 69 0E 00 7D 08 00 7C 02 00 69 0F 00 7D 09 00 7C 09 00 7C 02 00 5F 0B 00 7C 08 00 7C 02 00 5F 0C 00 7C 06 00 7C 02 00 5F 0E 00 7C 07 00 7C 02 00 5F 0F 00 71 48 03 01 7C 0A 00 0C 6F 04 00 01 7C 0B 00 6F 2A 00 01 7C 02 00 69 13 00 74 10 00 69 11 00 69 1D 00 42 7C 02 00 5F 13 00 74 00 00 69 01 00 64 0C 00 64 02 00 83 02 00 01 71 48 03 01 7C 0A 00 6F 04 00 01 7C 0B 00 6F 2A 00 01 7C 02 00 69 13 00 74 10 00 69 11 00 69 22 00 42 7C 02 00 5F 13 00 74 00 00 69 01 00 64 0D 00 64 02 00 83 02 00 01 71 48 03 01 71 4C 03 01 7C 02 00 69 13 00 74 10 00 69 11 00 69 1D 00 42 7C 02 00 5F 13 00 74 00 00 69 01 00 64 0E 00 64 02 00 83 02 00 01 6E 01 00 01 7C 05 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CU'
                             00000003     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000006     64 - LOAD_CONST          'true_attacker is winner'
                             00000009     64 - LOAD_CONST          3
                             0000000C     83 - CALL_FUNCTION       r0002
                             0000000F     01 - POP_TOP             
                             00000010     7C - LOAD_FAST           'true_attacker'
                             00000013     69 - LOAD_ATTR           'slot'
                             00000016     7C - LOAD_FAST           'result'
                             00000019     5F - STORE_ATTR          'winnerSlot'
                             0000001C     74 - LOAD_GLOBAL         'False'
                             0000001F     7D - STORE_FAST          'flipAtkDef'
                             00000022     7C - LOAD_FAST           'attackerHits'
                             00000025     6F - JUMP_IF_FALSE       -> 0000006A
                             00000028     01 - POP_TOP             
                             00000029     74 - LOAD_GLOBAL         'calculateDamage'
                             0000002C     7C - LOAD_FAST           'true_attacker'
                             0000002F     7C - LOAD_FAST           'true_defender'
                             00000032     7C - LOAD_FAST           'result'
                             00000035     83 - CALL_FUNCTION       r0003
                             00000038     5C - UNPACK_SEQUENCE     r0002
                             0000003B     7C - LOAD_FAST           'result'
                             0000003E     5F - STORE_ATTR          'loserDamage'
                             00000041     7C - LOAD_FAST           'result'
                             00000044     5F - STORE_ATTR          'loserDamageAbsorbed'
                             00000047     74 - LOAD_GLOBAL         'CU'
                             0000004A     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000004D     64 - LOAD_CONST          'Attacker deals %d. Defender resisted %d'
                             00000050     7C - LOAD_FAST           'result'
                             00000053     69 - LOAD_ATTR           'loserDamage'
                             00000056     7C - LOAD_FAST           'result'
                             00000059     69 - LOAD_ATTR           'loserDamageAbsorbed'
                             0000005C     66 - BUILD_TUPLE         r0002
                             0000005F     16 - BINARY_MODULO       
                             00000060     64 - LOAD_CONST          10
                             00000063     83 - CALL_FUNCTION       r0002
                             00000066     01 - POP_TOP             
                             00000067     6E - JUMP_FORWARD        -> 0000006B
                             0000006A     01 - POP_TOP             
                             0000006B     7C - LOAD_FAST           'defenderHits'
                             0000006E     6F - JUMP_IF_FALSE       -> 000000B3
                             00000071     01 - POP_TOP             
                             00000072     74 - LOAD_GLOBAL         'calculateDamage'
                             00000075     7C - LOAD_FAST           'true_defender'
                             00000078     7C - LOAD_FAST           'true_attacker'
                             0000007B     7C - LOAD_FAST           'result'
                             0000007E     83 - CALL_FUNCTION       r0003
                             00000081     5C - UNPACK_SEQUENCE     r0002
                             00000084     7C - LOAD_FAST           'result'
                             00000087     5F - STORE_ATTR          'winnerDamage'
                             0000008A     7C - LOAD_FAST           'result'
                             0000008D     5F - STORE_ATTR          'winnerDamageAbsorbed'
                             00000090     74 - LOAD_GLOBAL         'CU'
                             00000093     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000096     64 - LOAD_CONST          'Defender deals %d. Attacker resisted %d'
                             00000099     7C - LOAD_FAST           'result'
                             0000009C     69 - LOAD_ATTR           'winnerDamage'
                             0000009F     7C - LOAD_FAST           'result'
                             000000A2     69 - LOAD_ATTR           'winnerDamageAbsorbed'
                             000000A5     66 - BUILD_TUPLE         r0002
                             000000A8     16 - BINARY_MODULO       
                             000000A9     64 - LOAD_CONST          10
                             000000AC     83 - CALL_FUNCTION       r0002
                             000000AF     01 - POP_TOP             
                             000000B0     6E - JUMP_FORWARD        -> 000000B4
                             000000B3     01 - POP_TOP             
                             000000B4     7C - LOAD_FAST           'attackerHits'
                             000000B7     6F - JUMP_IF_FALSE       -> 000000BE
                             000000BA     01 - POP_TOP             
                             000000BB     7C - LOAD_FAST           'defenderHits'
                             000000BE     6F - JUMP_IF_FALSE       -> 000000E4
                             000000C1     01 - POP_TOP             
                             000000C2     74 - LOAD_GLOBAL         'CU'
                             000000C5     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000C8     64 - LOAD_CONST          'Result: HH'
                             000000CB     64 - LOAD_CONST          3
                             000000CE     83 - CALL_FUNCTION       r0002
                             000000D1     01 - POP_TOP             
                             000000D2     74 - LOAD_GLOBAL         'constants'
                             000000D5     69 - LOAD_ATTR           'combat'
                             000000D8     69 - LOAD_ATTR           'AHITS_DHITS'
                             000000DB     7C - LOAD_FAST           'result'
                             000000DE     5F - STORE_ATTR          'outcomeFlag'
                             000000E1     6E - JUMP_FORWARD        -> 0000017C
                             000000E4     01 - POP_TOP             
                             000000E5     7C - LOAD_FAST           'attackerHits'
                             000000E8     6F - JUMP_IF_FALSE       -> 000000F0
                             000000EB     01 - POP_TOP             
                             000000EC     7C - LOAD_FAST           'defenderHits'
                             000000EF     0C - UNARY_NOT           
                             000000F0     6F - JUMP_IF_FALSE       -> 00000116
                             000000F3     01 - POP_TOP             
                             000000F4     74 - LOAD_GLOBAL         'CU'
                             000000F7     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000FA     64 - LOAD_CONST          'Result: HM'
                             000000FD     64 - LOAD_CONST          3
                             00000100     83 - CALL_FUNCTION       r0002
                             00000103     01 - POP_TOP             
                             00000104     74 - LOAD_GLOBAL         'constants'
                             00000107     69 - LOAD_ATTR           'combat'
                             0000010A     69 - LOAD_ATTR           'AHITS_DMISSES'
                             0000010D     7C - LOAD_FAST           'result'
                             00000110     5F - STORE_ATTR          'outcomeFlag'
                             00000113     6E - JUMP_FORWARD        -> 0000017C
                             00000116     01 - POP_TOP             
                             00000117     7C - LOAD_FAST           'attackerHits'
                             0000011A     0C - UNARY_NOT           
                             0000011B     6F - JUMP_IF_FALSE       -> 00000122
                             0000011E     01 - POP_TOP             
                             0000011F     7C - LOAD_FAST           'defenderHits'
                             00000122     6F - JUMP_IF_FALSE       -> 00000148
                             00000125     01 - POP_TOP             
                             00000126     74 - LOAD_GLOBAL         'CU'
                             00000129     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000012C     64 - LOAD_CONST          'Result: MH'
                             0000012F     64 - LOAD_CONST          3
                             00000132     83 - CALL_FUNCTION       r0002
                             00000135     01 - POP_TOP             
                             00000136     74 - LOAD_GLOBAL         'constants'
                             00000139     69 - LOAD_ATTR           'combat'
                             0000013C     69 - LOAD_ATTR           'AMISSES_DHITS'
                             0000013F     7C - LOAD_FAST           'result'
                             00000142     5F - STORE_ATTR          'outcomeFlag'
                             00000145     6E - JUMP_FORWARD        -> 0000017C
                             00000148     01 - POP_TOP             
                             00000149     7C - LOAD_FAST           'attackerHits'
                             0000014C     0C - UNARY_NOT           
                             0000014D     6F - JUMP_IF_FALSE       -> 00000155
                             00000150     01 - POP_TOP             
                             00000151     7C - LOAD_FAST           'defenderHits'
                             00000154     0C - UNARY_NOT           
                             00000155     6F - JUMP_IF_FALSE       -> 0000017B
                             00000158     01 - POP_TOP             
                             00000159     74 - LOAD_GLOBAL         'CU'
                             0000015C     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000015F     64 - LOAD_CONST          'Result: MM'
                             00000162     64 - LOAD_CONST          3
                             00000165     83 - CALL_FUNCTION       r0002
                             00000168     01 - POP_TOP             
                             00000169     74 - LOAD_GLOBAL         'constants'
                             0000016C     69 - LOAD_ATTR           'combat'
                             0000016F     69 - LOAD_ATTR           'AMISSES_DMISSES'
                             00000172     7C - LOAD_FAST           'result'
                             00000175     5F - STORE_ATTR          'outcomeFlag'
                             00000178     6E - JUMP_FORWARD        -> 0000017C
                             0000017B     01 - POP_TOP             
                             0000017C     74 - LOAD_GLOBAL         'CU'
                             0000017F     69 - LOAD_ATTR           'finishingMoveAllowed'
                             00000182     7C - LOAD_FAST           'true_attacker'
                             00000185     7C - LOAD_FAST           'true_defender'
                             00000188     7C - LOAD_FAST           'result'
                             0000018B     74 - LOAD_GLOBAL         'False'
                             0000018E     83 - CALL_FUNCTION       r0004
                             00000191     7D - STORE_FAST          'atkIsFM'
                             00000194     74 - LOAD_GLOBAL         'CU'
                             00000197     69 - LOAD_ATTR           'finishingMoveAllowed'
                             0000019A     7C - LOAD_FAST           'true_attacker'
                             0000019D     7C - LOAD_FAST           'true_defender'
                             000001A0     7C - LOAD_FAST           'result'
                             000001A3     74 - LOAD_GLOBAL         'True'
                             000001A6     83 - CALL_FUNCTION       r0004
                             000001A9     7D - STORE_FAST          'defIsFM'
                             000001AC     7C - LOAD_FAST           'atkIsFM'
                             000001AF     0C - UNARY_NOT           
                             000001B0     6F - JUMP_IF_FALSE       -> 000001CE
                             000001B3     01 - POP_TOP             
                             000001B4     7C - LOAD_FAST           'defIsFM'
                             000001B7     0C - UNARY_NOT           
                             000001B8     6F - JUMP_IF_FALSE       -> 000001CE
                             000001BB     01 - POP_TOP             
                             000001BC     74 - LOAD_GLOBAL         'CU'
                             000001BF     69 - LOAD_ATTR           'killingMoveAllowed'
                             000001C2     7C - LOAD_FAST           'true_attacker'
                             000001C5     7C - LOAD_FAST           'true_defender'
                             000001C8     7C - LOAD_FAST           'result'
                             000001CB     83 - CALL_FUNCTION       r0003
                             000001CE     6F - JUMP_IF_FALSE       -> 000001FB
                             000001D1     01 - POP_TOP             
                             000001D2     7C - LOAD_FAST           'result'
                             000001D5     69 - LOAD_ATTR           'outcomeFlag'
                             000001D8     74 - LOAD_GLOBAL         'constants'
                             000001DB     69 - LOAD_ATTR           'combat'
                             000001DE     69 - LOAD_ATTR           'KILLING_MOVE'
                             000001E1     42 - BINARY_OR           
                             000001E2     7C - LOAD_FAST           'result'
                             000001E5     5F - STORE_ATTR          'outcomeFlag'
                             000001E8     74 - LOAD_GLOBAL         'CU'
                             000001EB     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000001EE     64 - LOAD_CONST          'Result: KILLING_MOVE'
                             000001F1     64 - LOAD_CONST          3
                             000001F4     83 - CALL_FUNCTION       r0002
                             000001F7     01 - POP_TOP             
                             000001F8     6E - JUMP_FORWARD        -> 0000034C
                             000001FB     01 - POP_TOP             
                             000001FC     7C - LOAD_FAST           'atkIsFM'
                             000001FF     70 - JUMP_IF_TRUE        -> 00000206
                             00000202     01 - POP_TOP             
                             00000203     7C - LOAD_FAST           'defIsFM'
                             00000206     6F - JUMP_IF_FALSE       -> 0000034B
                             00000209     01 - POP_TOP             
                             0000020A     7C - LOAD_FAST           'result'
                             0000020D     69 - LOAD_ATTR           'outcomeFlag'
                             00000210     74 - LOAD_GLOBAL         'constants'
                             00000213     69 - LOAD_ATTR           'combat'
                             00000216     69 - LOAD_ATTR           'AHITS_DHITS'
                             00000219     6A - COMPARE_OP          "=="
                             0000021C     6F - JUMP_IF_FALSE       -> 00000321
                             0000021F     01 - POP_TOP             
                             00000220     7C - LOAD_FAST           'atkIsFM'
                             00000223     6F - JUMP_IF_FALSE       -> 0000022B
                             00000226     01 - POP_TOP             
                             00000227     7C - LOAD_FAST           'defIsFM'
                             0000022A     0C - UNARY_NOT           
                             0000022B     6F - JUMP_IF_FALSE       -> 000002AC
                             0000022E     01 - POP_TOP             
                             0000022F     7C - LOAD_FAST           'result'
                             00000232     69 - LOAD_ATTR           'outcomeFlag'
                             00000235     74 - LOAD_GLOBAL         'constants'
                             00000238     69 - LOAD_ATTR           'combat'
                             0000023B     69 - LOAD_ATTR           'FINISHING_MOVE'
                             0000023E     42 - BINARY_OR           
                             0000023F     7C - LOAD_FAST           'result'
                             00000242     5F - STORE_ATTR          'outcomeFlag'
                             00000245     74 - LOAD_GLOBAL         'CU'
                             00000248     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000024B     64 - LOAD_CONST          'Result: HFM vs H'
                             0000024E     64 - LOAD_CONST          3
                             00000251     83 - CALL_FUNCTION       r0002
                             00000254     01 - POP_TOP             
                             00000255     7C - LOAD_FAST           'true_defender'
                             00000258     69 - LOAD_ATTR           'slot'
                             0000025B     7C - LOAD_FAST           'result'
                             0000025E     5F - STORE_ATTR          'winnerSlot'
                             00000261     7C - LOAD_FAST           'result'
                             00000264     69 - LOAD_ATTR           'loserDamage'
                             00000267     7D - STORE_FAST          'tempLoserDmg'
                             0000026A     7C - LOAD_FAST           'result'
                             0000026D     69 - LOAD_ATTR           'loserDamageAbsorbed'
                             00000270     7D - STORE_FAST          'tempLoserDmgAb'
                             00000273     7C - LOAD_FAST           'result'
                             00000276     69 - LOAD_ATTR           'winnerDamage'
                             00000279     7D - STORE_FAST          'tempWinnerDmgAb'
                             0000027C     7C - LOAD_FAST           'result'
                             0000027F     69 - LOAD_ATTR           'winnerDamageAbsorbed'
                             00000282     7D - STORE_FAST          'tempWinnerDmg'
                             00000285     7C - LOAD_FAST           'tempWinnerDmg'
                             00000288     7C - LOAD_FAST           'result'
                             0000028B     5F - STORE_ATTR          'loserDamage'
                             0000028E     7C - LOAD_FAST           'tempWinnerDmgAb'
                             00000291     7C - LOAD_FAST           'result'
                             00000294     5F - STORE_ATTR          'loserDamageAbsorbed'
                             00000297     7C - LOAD_FAST           'tempLoserDmg'
                             0000029A     7C - LOAD_FAST           'result'
                             0000029D     5F - STORE_ATTR          'winnerDamage'
                             000002A0     7C - LOAD_FAST           'tempLoserDmgAb'
                             000002A3     7C - LOAD_FAST           'result'
                             000002A6     5F - STORE_ATTR          'winnerDamageAbsorbed'
                             000002A9     71 - JUMP_ABSOLUTE       -> 00000348
                             000002AC     01 - POP_TOP             
                             000002AD     7C - LOAD_FAST           'atkIsFM'
                             000002B0     0C - UNARY_NOT           
                             000002B1     6F - JUMP_IF_FALSE       -> 000002B8
                             000002B4     01 - POP_TOP             
                             000002B5     7C - LOAD_FAST           'defIsFM'
                             000002B8     6F - JUMP_IF_FALSE       -> 000002E5
                             000002BB     01 - POP_TOP             
                             000002BC     7C - LOAD_FAST           'result'
                             000002BF     69 - LOAD_ATTR           'outcomeFlag'
                             000002C2     74 - LOAD_GLOBAL         'constants'
                             000002C5     69 - LOAD_ATTR           'combat'
                             000002C8     69 - LOAD_ATTR           'FINISHING_MOVE'
                             000002CB     42 - BINARY_OR           
                             000002CC     7C - LOAD_FAST           'result'
                             000002CF     5F - STORE_ATTR          'outcomeFlag'
                             000002D2     74 - LOAD_GLOBAL         'CU'
                             000002D5     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000002D8     64 - LOAD_CONST          'Result: H vs HFM'
                             000002DB     64 - LOAD_CONST          3
                             000002DE     83 - CALL_FUNCTION       r0002
                             000002E1     01 - POP_TOP             
                             000002E2     71 - JUMP_ABSOLUTE       -> 00000348
                             000002E5     01 - POP_TOP             
                             000002E6     7C - LOAD_FAST           'atkIsFM'
                             000002E9     6F - JUMP_IF_FALSE       -> 000002F0
                             000002EC     01 - POP_TOP             
                             000002ED     7C - LOAD_FAST           'defIsFM'
                             000002F0     6F - JUMP_IF_FALSE       -> 0000031D
                             000002F3     01 - POP_TOP             
                             000002F4     7C - LOAD_FAST           'result'
                             000002F7     69 - LOAD_ATTR           'outcomeFlag'
                             000002FA     74 - LOAD_GLOBAL         'constants'
                             000002FD     69 - LOAD_ATTR           'combat'
                             00000300     69 - LOAD_ATTR           'FINISHING_MOVE_BOTH'
                             00000303     42 - BINARY_OR           
                             00000304     7C - LOAD_FAST           'result'
                             00000307     5F - STORE_ATTR          'outcomeFlag'
                             0000030A     74 - LOAD_GLOBAL         'CU'
                             0000030D     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000310     64 - LOAD_CONST          'Result: FMH vs HFM'
                             00000313     64 - LOAD_CONST          3
                             00000316     83 - CALL_FUNCTION       r0002
                             00000319     01 - POP_TOP             
                             0000031A     71 - JUMP_ABSOLUTE       -> 00000348
                             0000031D     01 - POP_TOP             
                             0000031E     71 - JUMP_ABSOLUTE       -> 0000034C
                             00000321     01 - POP_TOP             
                             00000322     7C - LOAD_FAST           'result'
                             00000325     69 - LOAD_ATTR           'outcomeFlag'
                             00000328     74 - LOAD_GLOBAL         'constants'
                             0000032B     69 - LOAD_ATTR           'combat'
                             0000032E     69 - LOAD_ATTR           'FINISHING_MOVE'
                             00000331     42 - BINARY_OR           
                             00000332     7C - LOAD_FAST           'result'
                             00000335     5F - STORE_ATTR          'outcomeFlag'
                             00000338     74 - LOAD_GLOBAL         'CU'
                             0000033B     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000033E     64 - LOAD_CONST          'Result: FMH vs M'
                             00000341     64 - LOAD_CONST          3
                             00000344     83 - CALL_FUNCTION       r0002
                             00000347     01 - POP_TOP             
                             00000348     6E - JUMP_FORWARD        -> 0000034C
                             0000034B     01 - POP_TOP             
                             0000034C     7C - LOAD_FAST           'flipAtkDef'
                             0000034F     53 - RETURN_VALUE        
                             00000350     64 - LOAD_CONST          None
                             00000353     53 - RETURN_VALUE        
                         consts:
0000254A                     TUPLE: (
0000254F                         None (4E),
00002550                         STR: 'true_attacker is winner' (17 00 00 00 74 72 75 65 5F 61 74 74 61 63 6B 65 72 20 69 73 20 77 69 6E 6E 65 72),
0000256C                         INT: 3 (03 00 00 00),
00002571                         STR: 'Attacker deals %d. Defender resisted %d' (27 00 00 00 41 74 74 61 63 6B 65 72 20 64 65 61 6C 73 20 25 64 2E 20 44 65 66 65 6E 64 65 72 20 72 65 73 69 73 74 65 64 20 25 64),
0000259D                         INT: 10 (0A 00 00 00),
000025A2                         STR: 'Defender deals %d. Attacker resisted %d' (27 00 00 00 44 65 66 65 6E 64 65 72 20 64 65 61 6C 73 20 25 64 2E 20 41 74 74 61 63 6B 65 72 20 72 65 73 69 73 74 65 64 20 25 64),
000025CE                         STR: 'Result: HH' (0A 00 00 00 52 65 73 75 6C 74 3A 20 48 48),
000025DD                         STR: 'Result: HM' (0A 00 00 00 52 65 73 75 6C 74 3A 20 48 4D),
000025EC                         STR: 'Result: MH' (0A 00 00 00 52 65 73 75 6C 74 3A 20 4D 48),
000025FB                         STR: 'Result: MM' (0A 00 00 00 52 65 73 75 6C 74 3A 20 4D 4D),
0000260A                         STR: 'Result: KILLING_MOVE' (14 00 00 00 52 65 73 75 6C 74 3A 20 4B 49 4C 4C 49 4E 47 5F 4D 4F 56 45),
00002623                         STR: 'Result: HFM vs H' (10 00 00 00 52 65 73 75 6C 74 3A 20 48 46 4D 20 76 73 20 48),
00002638                         STR: 'Result: H vs HFM' (10 00 00 00 52 65 73 75 6C 74 3A 20 48 20 76 73 20 48 46 4D),
0000264D                         STR: 'Result: FMH vs HFM' (12 00 00 00 52 65 73 75 6C 74 3A 20 46 4D 48 20 76 73 20 48 46 4D),
00002664                         STR: 'Result: FMH vs M' (10 00 00 00 52 65 73 75 6C 74 3A 20 46 4D 48 20 76 73 20 4D)
                             )
                         names:
00002679                     TUPLE: (
0000267E                         STR: 'CU' (02 00 00 00 43 55),
00002685                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
000026A2                         STR: 'true_attacker' (0D 00 00 00 74 72 75 65 5F 61 74 74 61 63 6B 65 72),
000026B4                         STR: 'slot' (04 00 00 00 73 6C 6F 74),
000026BD                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
000026C8                         STR: 'winnerSlot' (0A 00 00 00 77 69 6E 6E 65 72 53 6C 6F 74),
000026D7                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
000026E1                         STR: 'flipAtkDef' (0A 00 00 00 66 6C 69 70 41 74 6B 44 65 66),
000026F0                         STR: 'attackerHits' (0C 00 00 00 61 74 74 61 63 6B 65 72 48 69 74 73),
00002701                         STR: 'calculateDamage' (0F 00 00 00 63 61 6C 63 75 6C 61 74 65 44 61 6D 61 67 65),
00002715                         STR: 'true_defender' (0D 00 00 00 74 72 75 65 5F 64 65 66 65 6E 64 65 72),
00002727                         STR: 'loserDamage' (0B 00 00 00 6C 6F 73 65 72 44 61 6D 61 67 65),
00002737                         STR: 'loserDamageAbsorbed' (13 00 00 00 6C 6F 73 65 72 44 61 6D 61 67 65 41 62 73 6F 72 62 65 64),
0000274F                         STR: 'defenderHits' (0C 00 00 00 64 65 66 65 6E 64 65 72 48 69 74 73),
00002760                         STR: 'winnerDamage' (0C 00 00 00 77 69 6E 6E 65 72 44 61 6D 61 67 65),
00002771                         STR: 'winnerDamageAbsorbed' (14 00 00 00 77 69 6E 6E 65 72 44 61 6D 61 67 65 41 62 73 6F 72 62 65 64),
0000278A                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00002798                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
000027A3                         STR: 'AHITS_DHITS' (0B 00 00 00 41 48 49 54 53 5F 44 48 49 54 53),
000027B3                         STR: 'outcomeFlag' (0B 00 00 00 6F 75 74 63 6F 6D 65 46 6C 61 67),
000027C3                         STR: 'AHITS_DMISSES' (0D 00 00 00 41 48 49 54 53 5F 44 4D 49 53 53 45 53),
000027D5                         STR: 'AMISSES_DHITS' (0D 00 00 00 41 4D 49 53 53 45 53 5F 44 48 49 54 53),
000027E7                         STR: 'AMISSES_DMISSES' (0F 00 00 00 41 4D 49 53 53 45 53 5F 44 4D 49 53 53 45 53),
000027FB                         STR: 'finishingMoveAllowed' (14 00 00 00 66 69 6E 69 73 68 69 6E 67 4D 6F 76 65 41 6C 6C 6F 77 65 64),
00002814                         STR: 'atkIsFM' (07 00 00 00 61 74 6B 49 73 46 4D),
00002820                         STR: 'True' (04 00 00 00 54 72 75 65),
00002829                         STR: 'defIsFM' (07 00 00 00 64 65 66 49 73 46 4D),
00002835                         STR: 'killingMoveAllowed' (12 00 00 00 6B 69 6C 6C 69 6E 67 4D 6F 76 65 41 6C 6C 6F 77 65 64),
0000284C                         STR: 'KILLING_MOVE' (0C 00 00 00 4B 49 4C 4C 49 4E 47 5F 4D 4F 56 45),
0000285D                         STR: 'FINISHING_MOVE' (0E 00 00 00 46 49 4E 49 53 48 49 4E 47 5F 4D 4F 56 45),
00002870                         STR: 'tempLoserDmg' (0C 00 00 00 74 65 6D 70 4C 6F 73 65 72 44 6D 67),
00002881                         STR: 'tempLoserDmgAb' (0E 00 00 00 74 65 6D 70 4C 6F 73 65 72 44 6D 67 41 62),
00002894                         STR: 'tempWinnerDmgAb' (0F 00 00 00 74 65 6D 70 57 69 6E 6E 65 72 44 6D 67 41 62),
000028A8                         STR: 'tempWinnerDmg' (0D 00 00 00 74 65 6D 70 57 69 6E 6E 65 72 44 6D 67),
000028BA                         STR: 'FINISHING_MOVE_BOTH' (13 00 00 00 46 49 4E 49 53 48 49 4E 47 5F 4D 4F 56 45 5F 42 4F 54 48)
                             )
                         varnames:
000028D2                     TUPLE: (
000028D7                         STR: 'true_attacker' (0D 00 00 00 74 72 75 65 5F 61 74 74 61 63 6B 65 72),
000028E9                         STR: 'true_defender' (0D 00 00 00 74 72 75 65 5F 64 65 66 65 6E 64 65 72),
000028FB                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00002906                         STR: 'attackerHits' (0C 00 00 00 61 74 74 61 63 6B 65 72 48 69 74 73),
00002917                         STR: 'defenderHits' (0C 00 00 00 64 65 66 65 6E 64 65 72 48 69 74 73),
00002928                         STR: 'flipAtkDef' (0A 00 00 00 66 6C 69 70 41 74 6B 44 65 66),
00002937                         STR: 'tempLoserDmg' (0C 00 00 00 74 65 6D 70 4C 6F 73 65 72 44 6D 67),
00002948                         STR: 'tempLoserDmgAb' (0E 00 00 00 74 65 6D 70 4C 6F 73 65 72 44 6D 67 41 62),
0000295B                         STR: 'tempWinnerDmgAb' (0F 00 00 00 74 65 6D 70 57 69 6E 6E 65 72 44 6D 67 41 62),
0000296F                         STR: 'tempWinnerDmg' (0D 00 00 00 74 65 6D 70 57 69 6E 6E 65 72 44 6D 67),
00002981                         STR: 'atkIsFM' (07 00 00 00 61 74 6B 49 73 46 4D),
0000298D                         STR: 'defIsFM' (07 00 00 00 64 65 66 49 73 46 4D)
                             )
                         freevars:
00002999                     TUPLE: ()
                         cellvars:
0000299E                     TUPLE: ()
                         filename:
000029A3                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_resolution.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 72 65 73 6F 6C 75 74 69 6F 6E 2E 70 79)
                         name:
000029FB                     STR: 'handleStandardExchange' (16 00 00 00 68 61 6E 64 6C 65 53 74 61 6E 64 61 72 64 45 78 63 68 61 6E 67 65)
                         firslineno:
00002A16                     LONG: 253L (FD 00 00 00)
                         lnotab:
00002A1A                     STR: '\x00\x01\x10\x01\x0c\x01\x06\x02\x07\x01\x1e\x01$\x01\x07\x01\x1e\x01$\x03\x0e\x01\x10\x01\x13\x01\x0f\x01\x10\x01\x13\x01\x0f\x01\x10\x01\x13\x01\x10\x01\x10\x01\x13\x03\x18\x01\x18\x02&\x01\x16\x01\x14\x01\x0e\x01\x16\x01\x0f\x02\x16\x01\x10\x03\x0c\x02\t\x01\t\x01\t\x01\t\x02\t\x01\t\x01\t\x01\r\x04\x0f\x01\x16\x01\x14\x01\x0e\x01\x16\x01\x18\x02\x16\x01\x14\x02' (62 00 00 00 00 01 10 01 0C 01 06 02 07 01 1E 01 24 01 07 01 1E 01 24 03 0E 01 10 01 13 01 0F 01 10 01 13 01 0F 01 10 01 13 01 10 01 10 01 13 03 18 01 18 02 26 01 16 01 14 01 0E 01 16 01 0F 02 16 01 10 03 0C 02 09 01 09 01 09 01 09 02 09 01 09 01 09 01 0D 04 0F 01 16 01 14 01 0E 01 16 01 18 02 16 01 14 02),
00002A81             CODE:
                         argcount:
00002A82                     LONG: 3L (03 00 00 00)
                         nlocals:
00002A86                     LONG: 3L (03 00 00 00)
                         stacksize:
00002A8A                     LONG: 3L (03 00 00 00)
                         flags:
00002A8E                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00002A92                     STR: 't\x00\x00i\x01\x00d\x01\x00d\x02\x00\x83\x02\x00\x01|\x01\x00i\x03\x00t\x04\x00i\x05\x00i\x06\x00j\x02\x00o\x80\x00\x01t\x00\x00i\x07\x00|\x01\x00\x83\x01\x00o \x00\x01t\x00\x00i\x01\x00d\x03\x00d\x02\x00\x83\x02\x00\x01|\x00\x00i\t\x00|\x02\x00_\x0b\x00q\xc2\x00\x01t\x00\x00i\x07\x00|\x00\x00\x83\x01\x00o \x00\x01t\x00\x00i\x01\x00d\x04\x00d\x02\x00\x83\x02\x00\x01|\x01\x00i\t\x00|\x02\x00_\x0b\x00q\xc2\x00\x01t\x00\x00i\x01\x00d\x05\x00d\x02\x00\x83\x02\x00\x01|\x00\x00i\t\x00|\x02\x00_\x0b\x00n\x1d\x00\x01t\x00\x00i\x01\x00d\x06\x00d\x02\x00\x83\x02\x00\x01|\x01\x00i\t\x00|\x02\x00_\x0b\x00t\x04\x00i\x05\x00i\x0c\x00|\x02\x00_\r\x00d\x07\x00|\x02\x00_\x0e\x00|\x01\x00i\x03\x00t\x04\x00i\x05\x00i\x06\x00j\x03\x00oH\x00\x01t\x00\x00i\x01\x00d\x08\x00d\x02\x00\x83\x02\x00\x01|\x00\x00i\x0f\x00|\x01\x00i\x10\x00\x18d\t\x00j\x04\x00o\x1d\x00\x01t\x00\x00i\x01\x00d\n\x00d\x02\x00\x83\x02\x00\x01d\x0b\x00|\x02\x00_\x11\x00q8\x01\x01n\x01\x00\x01d\x00\x00S' (3C 01 00 00 74 00 00 69 01 00 64 01 00 64 02 00 83 02 00 01 7C 01 00 69 03 00 74 04 00 69 05 00 69 06 00 6A 02 00 6F 80 00 01 74 00 00 69 07 00 7C 01 00 83 01 00 6F 20 00 01 74 00 00 69 01 00 64 03 00 64 02 00 83 02 00 01 7C 00 00 69 09 00 7C 02 00 5F 0B 00 71 C2 00 01 74 00 00 69 07 00 7C 00 00 83 01 00 6F 20 00 01 74 00 00 69 01 00 64 04 00 64 02 00 83 02 00 01 7C 01 00 69 09 00 7C 02 00 5F 0B 00 71 C2 00 01 74 00 00 69 01 00 64 05 00 64 02 00 83 02 00 01 7C 00 00 69 09 00 7C 02 00 5F 0B 00 6E 1D 00 01 74 00 00 69 01 00 64 06 00 64 02 00 83 02 00 01 7C 01 00 69 09 00 7C 02 00 5F 0B 00 74 04 00 69 05 00 69 0C 00 7C 02 00 5F 0D 00 64 07 00 7C 02 00 5F 0E 00 7C 01 00 69 03 00 74 04 00 69 05 00 69 06 00 6A 03 00 6F 48 00 01 74 00 00 69 01 00 64 08 00 64 02 00 83 02 00 01 7C 00 00 69 0F 00 7C 01 00 69 10 00 18 64 09 00 6A 04 00 6F 1D 00 01 74 00 00 69 01 00 64 0A 00 64 02 00 83 02 00 01 64 0B 00 7C 02 00 5F 11 00 71 38 01 01 6E 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CU'
                             00000003     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000006     64 - LOAD_CONST          'Handling a block!'
                             00000009     64 - LOAD_CONST          3
                             0000000C     83 - CALL_FUNCTION       r0002
                             0000000F     01 - POP_TOP             
                             00000010     7C - LOAD_FAST           'true_defender'
                             00000013     69 - LOAD_ATTR           'tacticalSetting'
                             00000016     74 - LOAD_GLOBAL         'constants'
                             00000019     69 - LOAD_ATTR           'combat'
                             0000001C     69 - LOAD_ATTR           'BLOCK'
                             0000001F     6A - COMPARE_OP          "=="
                             00000022     6F - JUMP_IF_FALSE       -> 000000A5
                             00000025     01 - POP_TOP             
                             00000026     74 - LOAD_GLOBAL         'CU'
                             00000029     69 - LOAD_ATTR           'isPlayerBeingGanged'
                             0000002C     7C - LOAD_FAST           'true_defender'
                             0000002F     83 - CALL_FUNCTION       r0001
                             00000032     6F - JUMP_IF_FALSE       -> 00000055
                             00000035     01 - POP_TOP             
                             00000036     74 - LOAD_GLOBAL         'CU'
                             00000039     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000003C     64 - LOAD_CONST          'defender is being ganged, true_attacker is winner'
                             0000003F     64 - LOAD_CONST          3
                             00000042     83 - CALL_FUNCTION       r0002
                             00000045     01 - POP_TOP             
                             00000046     7C - LOAD_FAST           'true_attacker'
                             00000049     69 - LOAD_ATTR           'slot'
                             0000004C     7C - LOAD_FAST           'result'
                             0000004F     5F - STORE_ATTR          'winnerSlot'
                             00000052     71 - JUMP_ABSOLUTE       -> 000000C2
                             00000055     01 - POP_TOP             
                             00000056     74 - LOAD_GLOBAL         'CU'
                             00000059     69 - LOAD_ATTR           'isPlayerBeingGanged'
                             0000005C     7C - LOAD_FAST           'true_attacker'
                             0000005F     83 - CALL_FUNCTION       r0001
                             00000062     6F - JUMP_IF_FALSE       -> 00000085
                             00000065     01 - POP_TOP             
                             00000066     74 - LOAD_GLOBAL         'CU'
                             00000069     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000006C     64 - LOAD_CONST          'attacker is being ganged, true_defender is winner'
                             0000006F     64 - LOAD_CONST          3
                             00000072     83 - CALL_FUNCTION       r0002
                             00000075     01 - POP_TOP             
                             00000076     7C - LOAD_FAST           'true_defender'
                             00000079     69 - LOAD_ATTR           'slot'
                             0000007C     7C - LOAD_FAST           'result'
                             0000007F     5F - STORE_ATTR          'winnerSlot'
                             00000082     71 - JUMP_ABSOLUTE       -> 000000C2
                             00000085     01 - POP_TOP             
                             00000086     74 - LOAD_GLOBAL         'CU'
                             00000089     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000008C     64 - LOAD_CONST          'no one is being ganged, true_attacker is winner'
                             0000008F     64 - LOAD_CONST          3
                             00000092     83 - CALL_FUNCTION       r0002
                             00000095     01 - POP_TOP             
                             00000096     7C - LOAD_FAST           'true_attacker'
                             00000099     69 - LOAD_ATTR           'slot'
                             0000009C     7C - LOAD_FAST           'result'
                             0000009F     5F - STORE_ATTR          'winnerSlot'
                             000000A2     6E - JUMP_FORWARD        -> 000000C2
                             000000A5     01 - POP_TOP             
                             000000A6     74 - LOAD_GLOBAL         'CU'
                             000000A9     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000AC     64 - LOAD_CONST          'true_defender is winner'
                             000000AF     64 - LOAD_CONST          3
                             000000B2     83 - CALL_FUNCTION       r0002
                             000000B5     01 - POP_TOP             
                             000000B6     7C - LOAD_FAST           'true_defender'
                             000000B9     69 - LOAD_ATTR           'slot'
                             000000BC     7C - LOAD_FAST           'result'
                             000000BF     5F - STORE_ATTR          'winnerSlot'
                             000000C2     74 - LOAD_GLOBAL         'constants'
                             000000C5     69 - LOAD_ATTR           'combat'
                             000000C8     69 - LOAD_ATTR           'AMISSES_DMISSES'
                             000000CB     7C - LOAD_FAST           'result'
                             000000CE     5F - STORE_ATTR          'outcomeFlag'
                             000000D1     64 - LOAD_CONST          0
                             000000D4     7C - LOAD_FAST           'result'
                             000000D7     5F - STORE_ATTR          'loserDamage'
                             000000DA     7C - LOAD_FAST           'true_defender'
                             000000DD     69 - LOAD_ATTR           'tacticalSetting'
                             000000E0     74 - LOAD_GLOBAL         'constants'
                             000000E3     69 - LOAD_ATTR           'combat'
                             000000E6     69 - LOAD_ATTR           'BLOCK'
                             000000E9     6A - COMPARE_OP          "!="
                             000000EC     6F - JUMP_IF_FALSE       -> 00000137
                             000000EF     01 - POP_TOP             
                             000000F0     74 - LOAD_GLOBAL         'CU'
                             000000F3     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000F6     64 - LOAD_CONST          'Checking for hyper dodge'
                             000000F9     64 - LOAD_CONST          3
                             000000FC     83 - CALL_FUNCTION       r0002
                             000000FF     01 - POP_TOP             
                             00000100     7C - LOAD_FAST           'true_attacker'
                             00000103     69 - LOAD_ATTR           'tacticalValue'
                             00000106     7C - LOAD_FAST           'true_defender'
                             00000109     69 - LOAD_ATTR           'meleeDefenseTactics'
                             0000010C     18 - BINARY_SUBTRACT     
                             0000010D     64 - LOAD_CONST          50
                             00000110     6A - COMPARE_OP          ">"
                             00000113     6F - JUMP_IF_FALSE       -> 00000133
                             00000116     01 - POP_TOP             
                             00000117     74 - LOAD_GLOBAL         'CU'
                             0000011A     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000011D     64 - LOAD_CONST          'using hyper dodge'
                             00000120     64 - LOAD_CONST          3
                             00000123     83 - CALL_FUNCTION       r0002
                             00000126     01 - POP_TOP             
                             00000127     64 - LOAD_CONST          1
                             0000012A     7C - LOAD_FAST           'result'
                             0000012D     5F - STORE_ATTR          'hyper_dodge'
                             00000130     71 - JUMP_ABSOLUTE       -> 00000138
                             00000133     01 - POP_TOP             
                             00000134     6E - JUMP_FORWARD        -> 00000138
                             00000137     01 - POP_TOP             
                             00000138     64 - LOAD_CONST          None
                             0000013B     53 - RETURN_VALUE        
                         consts:
00002BD3                     TUPLE: (
00002BD8                         None (4E),
00002BD9                         STR: 'Handling a block!' (11 00 00 00 48 61 6E 64 6C 69 6E 67 20 61 20 62 6C 6F 63 6B 21),
00002BEF                         INT: 3 (03 00 00 00),
00002BF4                         STR: 'defender is being ganged, true_attacker is winner' (31 00 00 00 64 65 66 65 6E 64 65 72 20 69 73 20 62 65 69 6E 67 20 67 61 6E 67 65 64 2C 20 74 72 75 65 5F 61 74 74 61 63 6B 65 72 20 69 73 20 77 69 6E 6E 65 72),
00002C2A                         STR: 'attacker is being ganged, true_defender is winner' (31 00 00 00 61 74 74 61 63 6B 65 72 20 69 73 20 62 65 69 6E 67 20 67 61 6E 67 65 64 2C 20 74 72 75 65 5F 64 65 66 65 6E 64 65 72 20 69 73 20 77 69 6E 6E 65 72),
00002C60                         STR: 'no one is being ganged, true_attacker is winner' (2F 00 00 00 6E 6F 20 6F 6E 65 20 69 73 20 62 65 69 6E 67 20 67 61 6E 67 65 64 2C 20 74 72 75 65 5F 61 74 74 61 63 6B 65 72 20 69 73 20 77 69 6E 6E 65 72),
00002C94                         STR: 'true_defender is winner' (17 00 00 00 74 72 75 65 5F 64 65 66 65 6E 64 65 72 20 69 73 20 77 69 6E 6E 65 72),
00002CB0                         INT: 0 (00 00 00 00),
00002CB5                         STR: 'Checking for hyper dodge' (18 00 00 00 43 68 65 63 6B 69 6E 67 20 66 6F 72 20 68 79 70 65 72 20 64 6F 64 67 65),
00002CD2                         INT: 50 (32 00 00 00),
00002CD7                         STR: 'using hyper dodge' (11 00 00 00 75 73 69 6E 67 20 68 79 70 65 72 20 64 6F 64 67 65),
00002CED                         INT: 1 (01 00 00 00)
                             )
                         names:
00002CF2                     TUPLE: (
00002CF7                         STR: 'CU' (02 00 00 00 43 55),
00002CFE                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
00002D1B                         STR: 'true_defender' (0D 00 00 00 74 72 75 65 5F 64 65 66 65 6E 64 65 72),
00002D2D                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
00002D41                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00002D4F                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
00002D5A                         STR: 'BLOCK' (05 00 00 00 42 4C 4F 43 4B),
00002D64                         STR: 'isPlayerBeingGanged' (13 00 00 00 69 73 50 6C 61 79 65 72 42 65 69 6E 67 47 61 6E 67 65 64),
00002D7C                         STR: 'true_attacker' (0D 00 00 00 74 72 75 65 5F 61 74 74 61 63 6B 65 72),
00002D8E                         STR: 'slot' (04 00 00 00 73 6C 6F 74),
00002D97                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00002DA2                         STR: 'winnerSlot' (0A 00 00 00 77 69 6E 6E 65 72 53 6C 6F 74),
00002DB1                         STR: 'AMISSES_DMISSES' (0F 00 00 00 41 4D 49 53 53 45 53 5F 44 4D 49 53 53 45 53),
00002DC5                         STR: 'outcomeFlag' (0B 00 00 00 6F 75 74 63 6F 6D 65 46 6C 61 67),
00002DD5                         STR: 'loserDamage' (0B 00 00 00 6C 6F 73 65 72 44 61 6D 61 67 65),
00002DE5                         STR: 'tacticalValue' (0D 00 00 00 74 61 63 74 69 63 61 6C 56 61 6C 75 65),
00002DF7                         STR: 'meleeDefenseTactics' (13 00 00 00 6D 65 6C 65 65 44 65 66 65 6E 73 65 54 61 63 74 69 63 73),
00002E0F                         STR: 'hyper_dodge' (0B 00 00 00 68 79 70 65 72 5F 64 6F 64 67 65)
                             )
                         varnames:
00002E1F                     TUPLE: (
00002E24                         STR: 'true_attacker' (0D 00 00 00 74 72 75 65 5F 61 74 74 61 63 6B 65 72),
00002E36                         STR: 'true_defender' (0D 00 00 00 74 72 75 65 5F 64 65 66 65 6E 64 65 72),
00002E48                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74)
                             )
                         freevars:
00002E53                     TUPLE: ()
                         cellvars:
00002E58                     TUPLE: ()
                         filename:
00002E5D                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_resolution.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 72 65 73 6F 6C 75 74 69 6F 6E 2E 70 79)
                         name:
00002EB5                     STR: 'handleBlock' (0B 00 00 00 68 61 6E 64 6C 65 42 6C 6F 63 6B)
                         firslineno:
00002EC5                     LONG: 320L (40 01 00 00)
                         lnotab:
00002EC9                     STR: '\x00\x01\x10\x03\x16\x02\x10\x01\x10\x01\x10\x01\x10\x01\x10\x01\x10\x02\x10\x01\x10\x02\x10\x01\x0c\x02\x0f\x01\t\x05\x16\x01\x10\x01\x17\x01\x10\x01' (26 00 00 00 00 01 10 03 16 02 10 01 10 01 10 01 10 01 10 01 10 02 10 01 10 02 10 01 0C 02 0F 01 09 05 16 01 10 01 17 01 10 01),
00002EF4             CODE:
                         argcount:
00002EF5                     LONG: 2L (02 00 00 00)
                         nlocals:
00002EF9                     LONG: 2L (02 00 00 00)
                         stacksize:
00002EFD                     LONG: 2L (02 00 00 00)
                         flags:
00002F01                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00002F05                     STR: '|\x01\x00t\x01\x00j\x02\x00o\x08\x00\x01d\x01\x00Sne\x00\x01|\x01\x00t\x02\x00j\x02\x00o\x0b\x00\x01|\x00\x00i\x04\x00SnM\x00\x01|\x01\x00t\x05\x00j\x02\x00o\x0b\x00\x01|\x00\x00i\x06\x00Sn5\x00\x01|\x01\x00t\x07\x00j\x02\x00o\x0b\x00\x01|\x00\x00i\x08\x00Sn\x1d\x00\x01|\x01\x00t\t\x00j\x02\x00o\x0b\x00\x01|\x00\x00i\n\x00Sn\x05\x00\x01d\x01\x00Sd\x00\x00S' (7D 00 00 00 7C 01 00 74 01 00 6A 02 00 6F 08 00 01 64 01 00 53 6E 65 00 01 7C 01 00 74 02 00 6A 02 00 6F 0B 00 01 7C 00 00 69 04 00 53 6E 4D 00 01 7C 01 00 74 05 00 6A 02 00 6F 0B 00 01 7C 00 00 69 06 00 53 6E 35 00 01 7C 01 00 74 07 00 6A 02 00 6F 0B 00 01 7C 00 00 69 08 00 53 6E 1D 00 01 7C 01 00 74 09 00 6A 02 00 6F 0B 00 01 7C 00 00 69 0A 00 53 6E 05 00 01 64 01 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'abilityType'
                             00000003     74 - LOAD_GLOBAL         'None'
                             00000006     6A - COMPARE_OP          "=="
                             00000009     6F - JUMP_IF_FALSE       -> 00000014
                             0000000C     01 - POP_TOP             
                             0000000D     64 - LOAD_CONST          0
                             00000010     53 - RETURN_VALUE        
                             00000011     6E - JUMP_FORWARD        -> 00000079
                             00000014     01 - POP_TOP             
                             00000015     7C - LOAD_FAST           'abilityType'
                             00000018     74 - LOAD_GLOBAL         'RangedDefenseTacticsAbility'
                             0000001B     6A - COMPARE_OP          "=="
                             0000001E     6F - JUMP_IF_FALSE       -> 0000002C
                             00000021     01 - POP_TOP             
                             00000022     7C - LOAD_FAST           'character'
                             00000025     69 - LOAD_ATTR           'rangeDefenseTactics'
                             00000028     53 - RETURN_VALUE        
                             00000029     6E - JUMP_FORWARD        -> 00000079
                             0000002C     01 - POP_TOP             
                             0000002D     7C - LOAD_FAST           'abilityType'
                             00000030     74 - LOAD_GLOBAL         'ViralDeflectionAbility'
                             00000033     6A - COMPARE_OP          "=="
                             00000036     6F - JUMP_IF_FALSE       -> 00000044
                             00000039     01 - POP_TOP             
                             0000003A     7C - LOAD_FAST           'character'
                             0000003D     69 - LOAD_ATTR           'viralDefenseTactics'
                             00000040     53 - RETURN_VALUE        
                             00000041     6E - JUMP_FORWARD        -> 00000079
                             00000044     01 - POP_TOP             
                             00000045     7C - LOAD_FAST           'abilityType'
                             00000048     74 - LOAD_GLOBAL         'MeleeDefenseTacticsAbility'
                             0000004B     6A - COMPARE_OP          "=="
                             0000004E     6F - JUMP_IF_FALSE       -> 0000005C
                             00000051     01 - POP_TOP             
                             00000052     7C - LOAD_FAST           'character'
                             00000055     69 - LOAD_ATTR           'meleeDefenseTactics'
                             00000058     53 - RETURN_VALUE        
                             00000059     6E - JUMP_FORWARD        -> 00000079
                             0000005C     01 - POP_TOP             
                             0000005D     7C - LOAD_FAST           'abilityType'
                             00000060     74 - LOAD_GLOBAL         'ThrowDefenseTacticsAbility'
                             00000063     6A - COMPARE_OP          "=="
                             00000066     6F - JUMP_IF_FALSE       -> 00000074
                             00000069     01 - POP_TOP             
                             0000006A     7C - LOAD_FAST           'character'
                             0000006D     69 - LOAD_ATTR           'thrownDefenseTactics'
                             00000070     53 - RETURN_VALUE        
                             00000071     6E - JUMP_FORWARD        -> 00000079
                             00000074     01 - POP_TOP             
                             00000075     64 - LOAD_CONST          0
                             00000078     53 - RETURN_VALUE        
                             00000079     64 - LOAD_CONST          None
                             0000007C     53 - RETURN_VALUE        
                         consts:
00002F87                     TUPLE: (
00002F8C                         None (4E),
00002F8D                         INT: 0 (00 00 00 00)
                             )
                         names:
00002F92                     TUPLE: (
00002F97                         STR: 'abilityType' (0B 00 00 00 61 62 69 6C 69 74 79 54 79 70 65),
00002FA7                         STR: 'None' (04 00 00 00 4E 6F 6E 65),
00002FB0                         STR: 'RangedDefenseTacticsAbility' (1B 00 00 00 52 61 6E 67 65 64 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 41 62 69 6C 69 74 79),
00002FD0                         STR: 'character' (09 00 00 00 63 68 61 72 61 63 74 65 72),
00002FDE                         STR: 'rangeDefenseTactics' (13 00 00 00 72 61 6E 67 65 44 65 66 65 6E 73 65 54 61 63 74 69 63 73),
00002FF6                         STR: 'ViralDeflectionAbility' (16 00 00 00 56 69 72 61 6C 44 65 66 6C 65 63 74 69 6F 6E 41 62 69 6C 69 74 79),
00003011                         STR: 'viralDefenseTactics' (13 00 00 00 76 69 72 61 6C 44 65 66 65 6E 73 65 54 61 63 74 69 63 73),
00003029                         STR: 'MeleeDefenseTacticsAbility' (1A 00 00 00 4D 65 6C 65 65 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 41 62 69 6C 69 74 79),
00003048                         STR: 'meleeDefenseTactics' (13 00 00 00 6D 65 6C 65 65 44 65 66 65 6E 73 65 54 61 63 74 69 63 73),
00003060                         STR: 'ThrowDefenseTacticsAbility' (1A 00 00 00 54 68 72 6F 77 44 65 66 65 6E 73 65 54 61 63 74 69 63 73 41 62 69 6C 69 74 79),
0000307F                         STR: 'thrownDefenseTactics' (14 00 00 00 74 68 72 6F 77 6E 44 65 66 65 6E 73 65 54 61 63 74 69 63 73)
                             )
                         varnames:
00003098                     TUPLE: (
0000309D                         STR: 'character' (09 00 00 00 63 68 61 72 61 63 74 65 72),
000030AB                         STR: 'abilityType' (0B 00 00 00 61 62 69 6C 69 74 79 54 79 70 65)
                             )
                         freevars:
000030BB                     TUPLE: ()
                         cellvars:
000030C0                     TUPLE: ()
                         filename:
000030C5                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_resolution.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 72 65 73 6F 6C 75 74 69 6F 6E 2E 70 79)
                         name:
0000311D                     STR: 'GetCorrectDefenseBonus' (16 00 00 00 47 65 74 43 6F 72 72 65 63 74 44 65 66 65 6E 73 65 42 6F 6E 75 73)
                         firslineno:
00003138                     LONG: 359L (67 01 00 00)
                         lnotab:
0000313C                     STR: '\x00\x01\r\x01\x08\x01\r\x01\x0b\x01\r\x01\x0b\x01\r\x01\x0b\x01\r\x01\x0b\x02' (16 00 00 00 00 01 0D 01 08 01 0D 01 0B 01 0D 01 0B 01 0D 01 0B 01 0D 01 0B 02),
00003157             CODE:
                         argcount:
00003158                     LONG: 2L (02 00 00 00)
                         nlocals:
0000315C                     LONG: 7L (07 00 00 00)
                         stacksize:
00003160                     LONG: 3L (03 00 00 00)
                         flags:
00003164                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00003168                     STR: 'd\x01\x00}\x05\x00d\x01\x00}\x04\x00d\x01\x00}\x02\x00d\x01\x00}\x03\x00t\x04\x00i\x05\x00|\x00\x00i\x07\x00\x83\x01\x00o?\x00\x01t\x08\x00i\t\x00|\x00\x00i\x07\x00\x83\x01\x00}\x06\x00t\x0b\x00|\x01\x00|\x06\x00\x83\x02\x00}\x05\x00t\x04\x00i\r\x00d\x02\x00|\x05\x00\x16d\x03\x00\x83\x02\x00\x01d\x03\x00}\x03\x00n\x01\x00\x01t\x04\x00i\x05\x00|\x01\x00i\x07\x00\x83\x01\x00o?\x00\x01t\x08\x00i\t\x00|\x01\x00i\x07\x00\x83\x01\x00}\x06\x00t\x0b\x00|\x00\x00|\x06\x00\x83\x02\x00}\x04\x00t\x04\x00i\r\x00d\x04\x00|\x04\x00\x16d\x03\x00\x83\x02\x00\x01d\x03\x00}\x02\x00n\x01\x00\x01|\x02\x00d\x01\x00j\x02\x00oL\x00\x01|\x01\x00i\x0e\x00o!\x00\x01|\x00\x00i\x0f\x00}\x04\x00t\x04\x00i\r\x00d\x05\x00|\x04\x00\x16d\x03\x00\x83\x02\x00\x01q\x15\x01\x01|\x00\x00i\x10\x00}\x04\x00t\x04\x00i\r\x00d\x06\x00|\x04\x00\x16d\x03\x00\x83\x02\x00\x01n\x01\x00\x01|\x03\x00d\x01\x00j\x02\x00oL\x00\x01|\x00\x00i\x0e\x00o!\x00\x01|\x01\x00i\x0f\x00}\x05\x00t\x04\x00i\r\x00d\x07\x00|\x05\x00\x16d\x03\x00\x83\x02\x00\x01qn\x01\x01|\x01\x00i\x10\x00}\x05\x00t\x04\x00i\r\x00d\x08\x00|\x05\x00\x16d\x03\x00\x83\x02\x00\x01n\x01\x00\x01|\x04\x00|\x05\x00f\x02\x00Sd\x00\x00S' (7C 01 00 00 64 01 00 7D 05 00 64 01 00 7D 04 00 64 01 00 7D 02 00 64 01 00 7D 03 00 74 04 00 69 05 00 7C 00 00 69 07 00 83 01 00 6F 3F 00 01 74 08 00 69 09 00 7C 00 00 69 07 00 83 01 00 7D 06 00 74 0B 00 7C 01 00 7C 06 00 83 02 00 7D 05 00 74 04 00 69 0D 00 64 02 00 7C 05 00 16 64 03 00 83 02 00 01 64 03 00 7D 03 00 6E 01 00 01 74 04 00 69 05 00 7C 01 00 69 07 00 83 01 00 6F 3F 00 01 74 08 00 69 09 00 7C 01 00 69 07 00 83 01 00 7D 06 00 74 0B 00 7C 00 00 7C 06 00 83 02 00 7D 04 00 74 04 00 69 0D 00 64 04 00 7C 04 00 16 64 03 00 83 02 00 01 64 03 00 7D 02 00 6E 01 00 01 7C 02 00 64 01 00 6A 02 00 6F 4C 00 01 7C 01 00 69 0E 00 6F 21 00 01 7C 00 00 69 0F 00 7D 04 00 74 04 00 69 0D 00 64 05 00 7C 04 00 16 64 03 00 83 02 00 01 71 15 01 01 7C 00 00 69 10 00 7D 04 00 74 04 00 69 0D 00 64 06 00 7C 04 00 16 64 03 00 83 02 00 01 6E 01 00 01 7C 03 00 64 01 00 6A 02 00 6F 4C 00 01 7C 00 00 69 0E 00 6F 21 00 01 7C 01 00 69 0F 00 7D 05 00 74 04 00 69 0D 00 64 07 00 7C 05 00 16 64 03 00 83 02 00 01 71 6E 01 01 7C 01 00 69 10 00 7D 05 00 74 04 00 69 0D 00 64 08 00 7C 05 00 16 64 03 00 83 02 00 01 6E 01 00 01 7C 04 00 7C 05 00 66 02 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          0
                             00000003     7D - STORE_FAST          'defenderD_total'
                             00000006     64 - LOAD_CONST          0
                             00000009     7D - STORE_FAST          'attackerD_total'
                             0000000C     64 - LOAD_CONST          0
                             0000000F     7D - STORE_FAST          'attackerAssigned'
                             00000012     64 - LOAD_CONST          0
                             00000015     7D - STORE_FAST          'defenderAssigned'
                             00000018     74 - LOAD_GLOBAL         'CU'
                             0000001B     69 - LOAD_ATTR           'isSpecialMove'
                             0000001E     7C - LOAD_FAST           'attacker'
                             00000021     69 - LOAD_ATTR           'requestedSpecialMove'
                             00000024     83 - CALL_FUNCTION       r0001
                             00000027     6F - JUMP_IF_FALSE       -> 00000069
                             0000002A     01 - POP_TOP             
                             0000002B     74 - LOAD_GLOBAL         'abilitylib'
                             0000002E     69 - LOAD_ATTR           'getDefenseTacticBonusType'
                             00000031     7C - LOAD_FAST           'attacker'
                             00000034     69 - LOAD_ATTR           'requestedSpecialMove'
                             00000037     83 - CALL_FUNCTION       r0001
                             0000003A     7D - STORE_FAST          'abilityDefenseType'
                             0000003D     74 - LOAD_GLOBAL         'GetCorrectDefenseBonus'
                             00000040     7C - LOAD_FAST           'defender'
                             00000043     7C - LOAD_FAST           'abilityDefenseType'
                             00000046     83 - CALL_FUNCTION       r0002
                             00000049     7D - STORE_FAST          'defenderD_total'
                             0000004C     74 - LOAD_GLOBAL         'CU'
                             0000004F     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000052     64 - LOAD_CONST          '(ASM) defender DT: %d '
                             00000055     7C - LOAD_FAST           'defenderD_total'
                             00000058     16 - BINARY_MODULO       
                             00000059     64 - LOAD_CONST          1
                             0000005C     83 - CALL_FUNCTION       r0002
                             0000005F     01 - POP_TOP             
                             00000060     64 - LOAD_CONST          1
                             00000063     7D - STORE_FAST          'defenderAssigned'
                             00000066     6E - JUMP_FORWARD        -> 0000006A
                             00000069     01 - POP_TOP             
                             0000006A     74 - LOAD_GLOBAL         'CU'
                             0000006D     69 - LOAD_ATTR           'isSpecialMove'
                             00000070     7C - LOAD_FAST           'defender'
                             00000073     69 - LOAD_ATTR           'requestedSpecialMove'
                             00000076     83 - CALL_FUNCTION       r0001
                             00000079     6F - JUMP_IF_FALSE       -> 000000BB
                             0000007C     01 - POP_TOP             
                             0000007D     74 - LOAD_GLOBAL         'abilitylib'
                             00000080     69 - LOAD_ATTR           'getDefenseTacticBonusType'
                             00000083     7C - LOAD_FAST           'defender'
                             00000086     69 - LOAD_ATTR           'requestedSpecialMove'
                             00000089     83 - CALL_FUNCTION       r0001
                             0000008C     7D - STORE_FAST          'abilityDefenseType'
                             0000008F     74 - LOAD_GLOBAL         'GetCorrectDefenseBonus'
                             00000092     7C - LOAD_FAST           'attacker'
                             00000095     7C - LOAD_FAST           'abilityDefenseType'
                             00000098     83 - CALL_FUNCTION       r0002
                             0000009B     7D - STORE_FAST          'attackerD_total'
                             0000009E     74 - LOAD_GLOBAL         'CU'
                             000000A1     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000A4     64 - LOAD_CONST          '(DSM) attacker DT: %d '
                             000000A7     7C - LOAD_FAST           'attackerD_total'
                             000000AA     16 - BINARY_MODULO       
                             000000AB     64 - LOAD_CONST          1
                             000000AE     83 - CALL_FUNCTION       r0002
                             000000B1     01 - POP_TOP             
                             000000B2     64 - LOAD_CONST          1
                             000000B5     7D - STORE_FAST          'attackerAssigned'
                             000000B8     6E - JUMP_FORWARD        -> 000000BC
                             000000BB     01 - POP_TOP             
                             000000BC     7C - LOAD_FAST           'attackerAssigned'
                             000000BF     64 - LOAD_CONST          0
                             000000C2     6A - COMPARE_OP          "=="
                             000000C5     6F - JUMP_IF_FALSE       -> 00000114
                             000000C8     01 - POP_TOP             
                             000000C9     7C - LOAD_FAST           'defender'
                             000000CC     69 - LOAD_ATTR           'equippedItemType'
                             000000CF     6F - JUMP_IF_FALSE       -> 000000F3
                             000000D2     01 - POP_TOP             
                             000000D3     7C - LOAD_FAST           'attacker'
                             000000D6     69 - LOAD_ATTR           'rangeDefenseTactics'
                             000000D9     7D - STORE_FAST          'attackerD_total'
                             000000DC     74 - LOAD_GLOBAL         'CU'
                             000000DF     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000E2     64 - LOAD_CONST          '(Defender Gun) attacker DT: %d '
                             000000E5     7C - LOAD_FAST           'attackerD_total'
                             000000E8     16 - BINARY_MODULO       
                             000000E9     64 - LOAD_CONST          1
                             000000EC     83 - CALL_FUNCTION       r0002
                             000000EF     01 - POP_TOP             
                             000000F0     71 - JUMP_ABSOLUTE       -> 00000115
                             000000F3     01 - POP_TOP             
                             000000F4     7C - LOAD_FAST           'attacker'
                             000000F7     69 - LOAD_ATTR           'meleeDefenseTactics'
                             000000FA     7D - STORE_FAST          'attackerD_total'
                             000000FD     74 - LOAD_GLOBAL         'CU'
                             00000100     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000103     64 - LOAD_CONST          '(Defender Fists) attacker DT: %d '
                             00000106     7C - LOAD_FAST           'attackerD_total'
                             00000109     16 - BINARY_MODULO       
                             0000010A     64 - LOAD_CONST          1
                             0000010D     83 - CALL_FUNCTION       r0002
                             00000110     01 - POP_TOP             
                             00000111     6E - JUMP_FORWARD        -> 00000115
                             00000114     01 - POP_TOP             
                             00000115     7C - LOAD_FAST           'defenderAssigned'
                             00000118     64 - LOAD_CONST          0
                             0000011B     6A - COMPARE_OP          "=="
                             0000011E     6F - JUMP_IF_FALSE       -> 0000016D
                             00000121     01 - POP_TOP             
                             00000122     7C - LOAD_FAST           'attacker'
                             00000125     69 - LOAD_ATTR           'equippedItemType'
                             00000128     6F - JUMP_IF_FALSE       -> 0000014C
                             0000012B     01 - POP_TOP             
                             0000012C     7C - LOAD_FAST           'defender'
                             0000012F     69 - LOAD_ATTR           'rangeDefenseTactics'
                             00000132     7D - STORE_FAST          'defenderD_total'
                             00000135     74 - LOAD_GLOBAL         'CU'
                             00000138     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000013B     64 - LOAD_CONST          '(Attacker Gun) defender DT: %d '
                             0000013E     7C - LOAD_FAST           'defenderD_total'
                             00000141     16 - BINARY_MODULO       
                             00000142     64 - LOAD_CONST          1
                             00000145     83 - CALL_FUNCTION       r0002
                             00000148     01 - POP_TOP             
                             00000149     71 - JUMP_ABSOLUTE       -> 0000016E
                             0000014C     01 - POP_TOP             
                             0000014D     7C - LOAD_FAST           'defender'
                             00000150     69 - LOAD_ATTR           'meleeDefenseTactics'
                             00000153     7D - STORE_FAST          'defenderD_total'
                             00000156     74 - LOAD_GLOBAL         'CU'
                             00000159     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000015C     64 - LOAD_CONST          '(Attacker Fists) defender DT: %d '
                             0000015F     7C - LOAD_FAST           'defenderD_total'
                             00000162     16 - BINARY_MODULO       
                             00000163     64 - LOAD_CONST          1
                             00000166     83 - CALL_FUNCTION       r0002
                             00000169     01 - POP_TOP             
                             0000016A     6E - JUMP_FORWARD        -> 0000016E
                             0000016D     01 - POP_TOP             
                             0000016E     7C - LOAD_FAST           'attackerD_total'
                             00000171     7C - LOAD_FAST           'defenderD_total'
                             00000174     66 - BUILD_TUPLE         r0002
                             00000177     53 - RETURN_VALUE        
                             00000178     64 - LOAD_CONST          None
                             0000017B     53 - RETURN_VALUE        
                         consts:
000032E9                     TUPLE: (
000032EE                         None (4E),
000032EF                         INT: 0 (00 00 00 00),
000032F4                         STR: '(ASM) defender DT: %d ' (16 00 00 00 28 41 53 4D 29 20 64 65 66 65 6E 64 65 72 20 44 54 3A 20 25 64 20),
0000330F                         INT: 1 (01 00 00 00),
00003314                         STR: '(DSM) attacker DT: %d ' (16 00 00 00 28 44 53 4D 29 20 61 74 74 61 63 6B 65 72 20 44 54 3A 20 25 64 20),
0000332F                         STR: '(Defender Gun) attacker DT: %d ' (1F 00 00 00 28 44 65 66 65 6E 64 65 72 20 47 75 6E 29 20 61 74 74 61 63 6B 65 72 20 44 54 3A 20 25 64 20),
00003353                         STR: '(Defender Fists) attacker DT: %d ' (21 00 00 00 28 44 65 66 65 6E 64 65 72 20 46 69 73 74 73 29 20 61 74 74 61 63 6B 65 72 20 44 54 3A 20 25 64 20),
00003379                         STR: '(Attacker Gun) defender DT: %d ' (1F 00 00 00 28 41 74 74 61 63 6B 65 72 20 47 75 6E 29 20 64 65 66 65 6E 64 65 72 20 44 54 3A 20 25 64 20),
0000339D                         STR: '(Attacker Fists) defender DT: %d ' (21 00 00 00 28 41 74 74 61 63 6B 65 72 20 46 69 73 74 73 29 20 64 65 66 65 6E 64 65 72 20 44 54 3A 20 25 64 20)
                             )
                         names:
000033C3                     TUPLE: (
000033C8                         STR: 'defenderD_total' (0F 00 00 00 64 65 66 65 6E 64 65 72 44 5F 74 6F 74 61 6C),
000033DC                         STR: 'attackerD_total' (0F 00 00 00 61 74 74 61 63 6B 65 72 44 5F 74 6F 74 61 6C),
000033F0                         STR: 'attackerAssigned' (10 00 00 00 61 74 74 61 63 6B 65 72 41 73 73 69 67 6E 65 64),
00003405                         STR: 'defenderAssigned' (10 00 00 00 64 65 66 65 6E 64 65 72 41 73 73 69 67 6E 65 64),
0000341A                         STR: 'CU' (02 00 00 00 43 55),
00003421                         STR: 'isSpecialMove' (0D 00 00 00 69 73 53 70 65 63 69 61 6C 4D 6F 76 65),
00003433                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
00003440                         STR: 'requestedSpecialMove' (14 00 00 00 72 65 71 75 65 73 74 65 64 53 70 65 63 69 61 6C 4D 6F 76 65),
00003459                         STR: 'abilitylib' (0A 00 00 00 61 62 69 6C 69 74 79 6C 69 62),
00003468                         STR: 'getDefenseTacticBonusType' (19 00 00 00 67 65 74 44 65 66 65 6E 73 65 54 61 63 74 69 63 42 6F 6E 75 73 54 79 70 65),
00003486                         STR: 'abilityDefenseType' (12 00 00 00 61 62 69 6C 69 74 79 44 65 66 65 6E 73 65 54 79 70 65),
0000349D                         STR: 'GetCorrectDefenseBonus' (16 00 00 00 47 65 74 43 6F 72 72 65 63 74 44 65 66 65 6E 73 65 42 6F 6E 75 73),
000034B8                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
000034C5                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
000034E2                         STR: 'equippedItemType' (10 00 00 00 65 71 75 69 70 70 65 64 49 74 65 6D 54 79 70 65),
000034F7                         STR: 'rangeDefenseTactics' (13 00 00 00 72 61 6E 67 65 44 65 66 65 6E 73 65 54 61 63 74 69 63 73),
0000350F                         STR: 'meleeDefenseTactics' (13 00 00 00 6D 65 6C 65 65 44 65 66 65 6E 73 65 54 61 63 74 69 63 73)
                             )
                         varnames:
00003527                     TUPLE: (
0000352C                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
00003539                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
00003546                         STR: 'attackerAssigned' (10 00 00 00 61 74 74 61 63 6B 65 72 41 73 73 69 67 6E 65 64),
0000355B                         STR: 'defenderAssigned' (10 00 00 00 64 65 66 65 6E 64 65 72 41 73 73 69 67 6E 65 64),
00003570                         STR: 'attackerD_total' (0F 00 00 00 61 74 74 61 63 6B 65 72 44 5F 74 6F 74 61 6C),
00003584                         STR: 'defenderD_total' (0F 00 00 00 64 65 66 65 6E 64 65 72 44 5F 74 6F 74 61 6C),
00003598                         STR: 'abilityDefenseType' (12 00 00 00 61 62 69 6C 69 74 79 44 65 66 65 6E 73 65 54 79 70 65)
                             )
                         freevars:
000035AF                     TUPLE: ()
                         cellvars:
000035B4                     TUPLE: ()
                         filename:
000035B9                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_resolution.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 72 65 73 6F 6C 75 74 69 6F 6E 2E 70 79)
                         name:
00003611                     STR: 'getCorrectDTTotals' (12 00 00 00 67 65 74 43 6F 72 72 65 63 74 44 54 54 6F 74 61 6C 73)
                         firslineno:
00003628                     LONG: 381L (7D 01 00 00)
                         lnotab:
0000362C                     STR: '\x00\x01\x06\x01\x06\x01\x06\x01\x06\x03\x13\x01\x12\x01\x0f\x01\x14\x01\n\x03\x13\x01\x12\x01\x0f\x01\x14\x01\n\x04\r\x01\n\x01\t\x01\x18\x02\t\x01\x18\x04\r\x01\n\x01\t\x01\x18\x02\t\x01\x18\x02' (36 00 00 00 00 01 06 01 06 01 06 01 06 03 13 01 12 01 0F 01 14 01 0A 03 13 01 12 01 0F 01 14 01 0A 04 0D 01 0A 01 09 01 18 02 09 01 18 04 0D 01 0A 01 09 01 18 02 09 01 18 02),
00003667             CODE:
                         argcount:
00003668                     LONG: 2L (02 00 00 00)
                         nlocals:
0000366C                     LONG: 12L (0C 00 00 00)
                         stacksize:
00003670                     LONG: 8L (08 00 00 00)
                         flags:
00003674                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00003678                     STR: '|\x00\x00i\x01\x00}\x04\x00|\x01\x00i\x01\x00}\x06\x00t\x05\x00|\x00\x00|\x01\x00\x83\x02\x00\\\x02\x00}\x03\x00}\x05\x00|\x04\x00|\x05\x00\x18}\x07\x00|\x06\x00|\x03\x00\x18}\n\x00|\x07\x00d\x01\x00j\x04\x00}\x02\x00|\n\x00d\x01\x00j\x04\x00}\x08\x00d\x01\x00}\t\x00t\r\x00i\x0e\x00|\x00\x00i\x0f\x00\x83\x01\x00o\r\x00\x01|\x00\x00i\x0f\x00}\t\x00n\x01\x00\x01d\x01\x00}\x0b\x00t\r\x00i\x0e\x00|\x01\x00i\x0f\x00\x83\x01\x00o\r\x00\x01|\x01\x00i\x0f\x00}\x0b\x00n\x01\x00\x01t\r\x00i\x11\x00d\x02\x00|\x00\x00i\x01\x00\x16d\x03\x00|\x00\x00|\x01\x00\x83\x04\x00\x01t\r\x00i\x11\x00d\x04\x00|\x03\x00\x16d\x03\x00|\x00\x00|\x01\x00\x83\x04\x00\x01t\r\x00i\x11\x00d\x05\x00|\x01\x00i\x01\x00\x16d\x03\x00|\x00\x00|\x01\x00\x83\x04\x00\x01t\r\x00i\x11\x00d\x06\x00|\x05\x00\x16d\x03\x00|\x00\x00|\x01\x00\x83\x04\x00\x01t\r\x00i\x11\x00d\x07\x00|\x02\x00|\x08\x00f\x02\x00\x16d\x03\x00|\x00\x00|\x01\x00\x83\x04\x00\x01t\r\x00i\x11\x00d\x08\x00|\t\x00|\x0b\x00f\x02\x00\x16d\x03\x00|\x00\x00|\x01\x00\x83\x04\x00\x01|\x04\x00|\x03\x00|\x07\x00|\x02\x00|\x06\x00|\x05\x00|\n\x00|\x08\x00f\x08\x00Sd\x00\x00S' (6D 01 00 00 7C 00 00 69 01 00 7D 04 00 7C 01 00 69 01 00 7D 06 00 74 05 00 7C 00 00 7C 01 00 83 02 00 5C 02 00 7D 03 00 7D 05 00 7C 04 00 7C 05 00 18 7D 07 00 7C 06 00 7C 03 00 18 7D 0A 00 7C 07 00 64 01 00 6A 04 00 7D 02 00 7C 0A 00 64 01 00 6A 04 00 7D 08 00 64 01 00 7D 09 00 74 0D 00 69 0E 00 7C 00 00 69 0F 00 83 01 00 6F 0D 00 01 7C 00 00 69 0F 00 7D 09 00 6E 01 00 01 64 01 00 7D 0B 00 74 0D 00 69 0E 00 7C 01 00 69 0F 00 83 01 00 6F 0D 00 01 7C 01 00 69 0F 00 7D 0B 00 6E 01 00 01 74 0D 00 69 11 00 64 02 00 7C 00 00 69 01 00 16 64 03 00 7C 00 00 7C 01 00 83 04 00 01 74 0D 00 69 11 00 64 04 00 7C 03 00 16 64 03 00 7C 00 00 7C 01 00 83 04 00 01 74 0D 00 69 11 00 64 05 00 7C 01 00 69 01 00 16 64 03 00 7C 00 00 7C 01 00 83 04 00 01 74 0D 00 69 11 00 64 06 00 7C 05 00 16 64 03 00 7C 00 00 7C 01 00 83 04 00 01 74 0D 00 69 11 00 64 07 00 7C 02 00 7C 08 00 66 02 00 16 64 03 00 7C 00 00 7C 01 00 83 04 00 01 74 0D 00 69 11 00 64 08 00 7C 09 00 7C 0B 00 66 02 00 16 64 03 00 7C 00 00 7C 01 00 83 04 00 01 7C 04 00 7C 03 00 7C 07 00 7C 02 00 7C 06 00 7C 05 00 7C 0A 00 7C 08 00 66 08 00 53 64 00 00 53)
                             00000000     7C - LOAD_FAST           'attacker'
                             00000003     69 - LOAD_ATTR           'tacticalValue'
                             00000006     7D - STORE_FAST          'attackerCT_total'
                             00000009     7C - LOAD_FAST           'defender'
                             0000000C     69 - LOAD_ATTR           'tacticalValue'
                             0000000F     7D - STORE_FAST          'defenderCT_total'
                             00000012     74 - LOAD_GLOBAL         'getCorrectDTTotals'
                             00000015     7C - LOAD_FAST           'attacker'
                             00000018     7C - LOAD_FAST           'defender'
                             0000001B     83 - CALL_FUNCTION       r0002
                             0000001E     5C - UNPACK_SEQUENCE     r0002
                             00000021     7D - STORE_FAST          'attackerD_total'
                             00000024     7D - STORE_FAST          'defenderD_total'
                             00000027     7C - LOAD_FAST           'attackerCT_total'
                             0000002A     7C - LOAD_FAST           'defenderD_total'
                             0000002D     18 - BINARY_SUBTRACT     
                             0000002E     7D - STORE_FAST          'attackersAdvantage'
                             00000031     7C - LOAD_FAST           'defenderCT_total'
                             00000034     7C - LOAD_FAST           'attackerD_total'
                             00000037     18 - BINARY_SUBTRACT     
                             00000038     7D - STORE_FAST          'defendersAdvantage'
                             0000003B     7C - LOAD_FAST           'attackersAdvantage'
                             0000003E     64 - LOAD_CONST          0
                             00000041     6A - COMPARE_OP          ">"
                             00000044     7D - STORE_FAST          'attackerHits'
                             00000047     7C - LOAD_FAST           'defendersAdvantage'
                             0000004A     64 - LOAD_CONST          0
                             0000004D     6A - COMPARE_OP          ">"
                             00000050     7D - STORE_FAST          'defenderHits'
                             00000053     64 - LOAD_CONST          0
                             00000056     7D - STORE_FAST          'attackersSM'
                             00000059     74 - LOAD_GLOBAL         'CU'
                             0000005C     69 - LOAD_ATTR           'isSpecialMove'
                             0000005F     7C - LOAD_FAST           'attacker'
                             00000062     69 - LOAD_ATTR           'requestedSpecialMove'
                             00000065     83 - CALL_FUNCTION       r0001
                             00000068     6F - JUMP_IF_FALSE       -> 00000078
                             0000006B     01 - POP_TOP             
                             0000006C     7C - LOAD_FAST           'attacker'
                             0000006F     69 - LOAD_ATTR           'requestedSpecialMove'
                             00000072     7D - STORE_FAST          'attackersSM'
                             00000075     6E - JUMP_FORWARD        -> 00000079
                             00000078     01 - POP_TOP             
                             00000079     64 - LOAD_CONST          0
                             0000007C     7D - STORE_FAST          'defendersSM'
                             0000007F     74 - LOAD_GLOBAL         'CU'
                             00000082     69 - LOAD_ATTR           'isSpecialMove'
                             00000085     7C - LOAD_FAST           'defender'
                             00000088     69 - LOAD_ATTR           'requestedSpecialMove'
                             0000008B     83 - CALL_FUNCTION       r0001
                             0000008E     6F - JUMP_IF_FALSE       -> 0000009E
                             00000091     01 - POP_TOP             
                             00000092     7C - LOAD_FAST           'defender'
                             00000095     69 - LOAD_ATTR           'requestedSpecialMove'
                             00000098     7D - STORE_FAST          'defendersSM'
                             0000009B     6E - JUMP_FORWARD        -> 0000009F
                             0000009E     01 - POP_TOP             
                             0000009F     74 - LOAD_GLOBAL         'CU'
                             000000A2     69 - LOAD_ATTR           'outputCombatDebugMessageAll'
                             000000A5     64 - LOAD_CONST          'attacker CT: %d  '
                             000000A8     7C - LOAD_FAST           'attacker'
                             000000AB     69 - LOAD_ATTR           'tacticalValue'
                             000000AE     16 - BINARY_MODULO       
                             000000AF     64 - LOAD_CONST          1
                             000000B2     7C - LOAD_FAST           'attacker'
                             000000B5     7C - LOAD_FAST           'defender'
                             000000B8     83 - CALL_FUNCTION       r0004
                             000000BB     01 - POP_TOP             
                             000000BC     74 - LOAD_GLOBAL         'CU'
                             000000BF     69 - LOAD_ATTR           'outputCombatDebugMessageAll'
                             000000C2     64 - LOAD_CONST          'attacker DT: %d '
                             000000C5     7C - LOAD_FAST           'attackerD_total'
                             000000C8     16 - BINARY_MODULO       
                             000000C9     64 - LOAD_CONST          1
                             000000CC     7C - LOAD_FAST           'attacker'
                             000000CF     7C - LOAD_FAST           'defender'
                             000000D2     83 - CALL_FUNCTION       r0004
                             000000D5     01 - POP_TOP             
                             000000D6     74 - LOAD_GLOBAL         'CU'
                             000000D9     69 - LOAD_ATTR           'outputCombatDebugMessageAll'
                             000000DC     64 - LOAD_CONST          'defender CT: %d'
                             000000DF     7C - LOAD_FAST           'defender'
                             000000E2     69 - LOAD_ATTR           'tacticalValue'
                             000000E5     16 - BINARY_MODULO       
                             000000E6     64 - LOAD_CONST          1
                             000000E9     7C - LOAD_FAST           'attacker'
                             000000EC     7C - LOAD_FAST           'defender'
                             000000EF     83 - CALL_FUNCTION       r0004
                             000000F2     01 - POP_TOP             
                             000000F3     74 - LOAD_GLOBAL         'CU'
                             000000F6     69 - LOAD_ATTR           'outputCombatDebugMessageAll'
                             000000F9     64 - LOAD_CONST          'defender DT: %d '
                             000000FC     7C - LOAD_FAST           'defenderD_total'
                             000000FF     16 - BINARY_MODULO       
                             00000100     64 - LOAD_CONST          1
                             00000103     7C - LOAD_FAST           'attacker'
                             00000106     7C - LOAD_FAST           'defender'
                             00000109     83 - CALL_FUNCTION       r0004
                             0000010C     01 - POP_TOP             
                             0000010D     74 - LOAD_GLOBAL         'CU'
                             00000110     69 - LOAD_ATTR           'outputCombatDebugMessageAll'
                             00000113     64 - LOAD_CONST          'result: AHits(%d) & DHits(%d)'
                             00000116     7C - LOAD_FAST           'attackerHits'
                             00000119     7C - LOAD_FAST           'defenderHits'
                             0000011C     66 - BUILD_TUPLE         r0002
                             0000011F     16 - BINARY_MODULO       
                             00000120     64 - LOAD_CONST          1
                             00000123     7C - LOAD_FAST           'attacker'
                             00000126     7C - LOAD_FAST           'defender'
                             00000129     83 - CALL_FUNCTION       r0004
                             0000012C     01 - POP_TOP             
                             0000012D     74 - LOAD_GLOBAL         'CU'
                             00000130     69 - LOAD_ATTR           'outputCombatDebugMessageAll'
                             00000133     64 - LOAD_CONST          'result: ASM(%d) & DSM(%d)'
                             00000136     7C - LOAD_FAST           'attackersSM'
                             00000139     7C - LOAD_FAST           'defendersSM'
                             0000013C     66 - BUILD_TUPLE         r0002
                             0000013F     16 - BINARY_MODULO       
                             00000140     64 - LOAD_CONST          1
                             00000143     7C - LOAD_FAST           'attacker'
                             00000146     7C - LOAD_FAST           'defender'
                             00000149     83 - CALL_FUNCTION       r0004
                             0000014C     01 - POP_TOP             
                             0000014D     7C - LOAD_FAST           'attackerCT_total'
                             00000150     7C - LOAD_FAST           'attackerD_total'
                             00000153     7C - LOAD_FAST           'attackersAdvantage'
                             00000156     7C - LOAD_FAST           'attackerHits'
                             00000159     7C - LOAD_FAST           'defenderCT_total'
                             0000015C     7C - LOAD_FAST           'defenderD_total'
                             0000015F     7C - LOAD_FAST           'defendersAdvantage'
                             00000162     7C - LOAD_FAST           'defenderHits'
                             00000165     66 - BUILD_TUPLE         r0008
                             00000168     53 - RETURN_VALUE        
                             00000169     64 - LOAD_CONST          None
                             0000016C     53 - RETURN_VALUE        
                         consts:
000037EA                     TUPLE: (
000037EF                         None (4E),
000037F0                         INT: 0 (00 00 00 00),
000037F5                         STR: 'attacker CT: %d  ' (11 00 00 00 61 74 74 61 63 6B 65 72 20 43 54 3A 20 25 64 20 20),
0000380B                         INT: 1 (01 00 00 00),
00003810                         STR: 'attacker DT: %d ' (10 00 00 00 61 74 74 61 63 6B 65 72 20 44 54 3A 20 25 64 20),
00003825                         STR: 'defender CT: %d' (0F 00 00 00 64 65 66 65 6E 64 65 72 20 43 54 3A 20 25 64),
00003839                         STR: 'defender DT: %d ' (10 00 00 00 64 65 66 65 6E 64 65 72 20 44 54 3A 20 25 64 20),
0000384E                         STR: 'result: AHits(%d) & DHits(%d)' (1D 00 00 00 72 65 73 75 6C 74 3A 20 41 48 69 74 73 28 25 64 29 20 26 20 44 48 69 74 73 28 25 64 29),
00003870                         STR: 'result: ASM(%d) & DSM(%d)' (19 00 00 00 72 65 73 75 6C 74 3A 20 41 53 4D 28 25 64 29 20 26 20 44 53 4D 28 25 64 29)
                             )
                         names:
0000388E                     TUPLE: (
00003893                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
000038A0                         STR: 'tacticalValue' (0D 00 00 00 74 61 63 74 69 63 61 6C 56 61 6C 75 65),
000038B2                         STR: 'attackerCT_total' (10 00 00 00 61 74 74 61 63 6B 65 72 43 54 5F 74 6F 74 61 6C),
000038C7                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
000038D4                         STR: 'defenderCT_total' (10 00 00 00 64 65 66 65 6E 64 65 72 43 54 5F 74 6F 74 61 6C),
000038E9                         STR: 'getCorrectDTTotals' (12 00 00 00 67 65 74 43 6F 72 72 65 63 74 44 54 54 6F 74 61 6C 73),
00003900                         STR: 'attackerD_total' (0F 00 00 00 61 74 74 61 63 6B 65 72 44 5F 74 6F 74 61 6C),
00003914                         STR: 'defenderD_total' (0F 00 00 00 64 65 66 65 6E 64 65 72 44 5F 74 6F 74 61 6C),
00003928                         STR: 'attackersAdvantage' (12 00 00 00 61 74 74 61 63 6B 65 72 73 41 64 76 61 6E 74 61 67 65),
0000393F                         STR: 'defendersAdvantage' (12 00 00 00 64 65 66 65 6E 64 65 72 73 41 64 76 61 6E 74 61 67 65),
00003956                         STR: 'attackerHits' (0C 00 00 00 61 74 74 61 63 6B 65 72 48 69 74 73),
00003967                         STR: 'defenderHits' (0C 00 00 00 64 65 66 65 6E 64 65 72 48 69 74 73),
00003978                         STR: 'attackersSM' (0B 00 00 00 61 74 74 61 63 6B 65 72 73 53 4D),
00003988                         STR: 'CU' (02 00 00 00 43 55),
0000398F                         STR: 'isSpecialMove' (0D 00 00 00 69 73 53 70 65 63 69 61 6C 4D 6F 76 65),
000039A1                         STR: 'requestedSpecialMove' (14 00 00 00 72 65 71 75 65 73 74 65 64 53 70 65 63 69 61 6C 4D 6F 76 65),
000039BA                         STR: 'defendersSM' (0B 00 00 00 64 65 66 65 6E 64 65 72 73 53 4D),
000039CA                         STR: 'outputCombatDebugMessageAll' (1B 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 41 6C 6C)
                             )
                         varnames:
000039EA                     TUPLE: (
000039EF                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
000039FC                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
00003A09                         STR: 'attackerHits' (0C 00 00 00 61 74 74 61 63 6B 65 72 48 69 74 73),
00003A1A                         STR: 'attackerD_total' (0F 00 00 00 61 74 74 61 63 6B 65 72 44 5F 74 6F 74 61 6C),
00003A2E                         STR: 'attackerCT_total' (10 00 00 00 61 74 74 61 63 6B 65 72 43 54 5F 74 6F 74 61 6C),
00003A43                         STR: 'defenderD_total' (0F 00 00 00 64 65 66 65 6E 64 65 72 44 5F 74 6F 74 61 6C),
00003A57                         STR: 'defenderCT_total' (10 00 00 00 64 65 66 65 6E 64 65 72 43 54 5F 74 6F 74 61 6C),
00003A6C                         STR: 'attackersAdvantage' (12 00 00 00 61 74 74 61 63 6B 65 72 73 41 64 76 61 6E 74 61 67 65),
00003A83                         STR: 'defenderHits' (0C 00 00 00 64 65 66 65 6E 64 65 72 48 69 74 73),
00003A94                         STR: 'attackersSM' (0B 00 00 00 61 74 74 61 63 6B 65 72 73 53 4D),
00003AA4                         STR: 'defendersAdvantage' (12 00 00 00 64 65 66 65 6E 64 65 72 73 41 64 76 61 6E 74 61 67 65),
00003ABB                         STR: 'defendersSM' (0B 00 00 00 64 65 66 65 6E 64 65 72 73 53 4D)
                             )
                         freevars:
00003ACB                     TUPLE: ()
                         cellvars:
00003AD0                     TUPLE: ()
                         filename:
00003AD5                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_resolution.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 72 65 73 6F 6C 75 74 69 6F 6E 2E 70 79)
                         name:
00003B2D                     STR: 'getCTandDTotals' (0F 00 00 00 67 65 74 43 54 61 6E 64 44 54 6F 74 61 6C 73)
                         firslineno:
00003B41                     LONG: 431L (AF 01 00 00)
                         lnotab:
00003B45                     STR: '\x00\x02\t\x01\t\x02\x15\x03\n\x01\n\x01\x0c\x01\x0c\x01\x06\x01\x13\x01\r\x01\x06\x01\x13\x01\r\x03\x1d\x01\x1a\x01\x1d\x01\x1a\x01 \x01 \x02' (28 00 00 00 00 02 09 01 09 02 15 03 0A 01 0A 01 0C 01 0C 01 06 01 13 01 0D 01 06 01 13 01 0D 03 1D 01 1A 01 1D 01 1A 01 20 01 20 02),
00003B72             CODE:
                         argcount:
00003B73                     LONG: 3L (03 00 00 00)
                         nlocals:
00003B77                     LONG: 3L (03 00 00 00)
                         stacksize:
00003B7B                     LONG: 2L (02 00 00 00)
                         flags:
00003B7F                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00003B83                     STR: '|\x02\x00i\x01\x00|\x00\x00_\x03\x00d\x00\x00S' (10 00 00 00 7C 02 00 69 01 00 7C 00 00 5F 03 00 64 00 00 53)
                             00000000     7C - LOAD_FAST           'loser'
                             00000003     69 - LOAD_ATTR           'slot'
                             00000006     7C - LOAD_FAST           'result'
                             00000009     5F - STORE_ATTR          'winnerSlot'
                             0000000C     64 - LOAD_CONST          None
                             0000000F     53 - RETURN_VALUE        
                         consts:
00003B98                     TUPLE: (
00003B9D                         None (4E)
                             )
                         names:
00003B9E                     TUPLE: (
00003BA3                         STR: 'loser' (05 00 00 00 6C 6F 73 65 72),
00003BAD                         STR: 'slot' (04 00 00 00 73 6C 6F 74),
00003BB6                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00003BC1                         STR: 'winnerSlot' (0A 00 00 00 77 69 6E 6E 65 72 53 6C 6F 74)
                             )
                         varnames:
00003BD0                     TUPLE: (
00003BD5                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00003BE0                         STR: 'winner' (06 00 00 00 77 69 6E 6E 65 72),
00003BEB                         STR: 'loser' (05 00 00 00 6C 6F 73 65 72)
                             )
                         freevars:
00003BF5                     TUPLE: ()
                         cellvars:
00003BFA                     TUPLE: ()
                         filename:
00003BFF                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_resolution.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 72 65 73 6F 6C 75 74 69 6F 6E 2E 70 79)
                         name:
00003C57                     STR: 'FlipAtkDef' (0A 00 00 00 46 6C 69 70 41 74 6B 44 65 66)
                         firslineno:
00003C66                     LONG: 468L (D4 01 00 00)
                         lnotab:
00003C6A                     STR: '\x00\x01' (02 00 00 00 00 01),
00003C71             CODE:
                         argcount:
00003C72                     LONG: 4L (04 00 00 00)
                         nlocals:
00003C76                     LONG: 26L (1A 00 00 00)
                         stacksize:
00003C7A                     LONG: 8L (08 00 00 00)
                         flags:
00003C7E                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00003C82                     STR: '|\x00\x00i\x01\x00|\x03\x00_\x03\x00|\x01\x00i\x01\x00|\x03\x00_\x05\x00t\x06\x00|\x00\x00|\x01\x00\x83\x02\x00\\\x08\x00}\n\x00}\t\x00}\x07\x00}\x0e\x00}\x17\x00}\x11\x00}\r\x00}\x0f\x00t\x0f\x00i\x10\x00d\x01\x00j\x05\x00o<\x00\x01t\x11\x00i\x12\x00|\x00\x00i\x13\x00d\x02\x00t\x14\x00i\x15\x00i\x16\x00\x83\x03\x00\x01t\x11\x00i\x12\x00|\x01\x00i\x13\x00d\x03\x00t\x14\x00i\x15\x00i\x16\x00\x83\x03\x00\x01n\x01\x00\x01|\x01\x00i\x17\x00p\x10\x00\x01t\x18\x00i\x19\x00|\x01\x00i\x1a\x00\x83\x01\x00o&\x00\x01t\x18\x00i\x1b\x00d\x04\x00d\x01\x00|\x00\x00|\x01\x00\x83\x04\x00\x01d\x05\x00}\x17\x00t\x1c\x00}\x0f\x00n\x01\x00\x01|\x00\x00i\x17\x00p\x10\x00\x01t\x18\x00i\x19\x00|\x00\x00i\x1a\x00\x83\x01\x00o&\x00\x01t\x18\x00i\x1b\x00d\x06\x00d\x01\x00|\x00\x00|\x01\x00\x83\x04\x00\x01d\x05\x00}\n\x00t\x1c\x00}\x0e\x00n\x01\x00\x01d\x05\x00}\x10\x00|\x00\x00}\x18\x00|\x01\x00}\x12\x00|\x0f\x00o\x05\x00\x01|\x0e\x00\x0co\n\x00\x01d\x01\x00}\x10\x00n\x01\x00\x01|\x0f\x00o\x04\x00\x01|\x0e\x00}\x13\x00t\x18\x00i!\x00|\x18\x00i\x1a\x00\x83\x01\x00}\x06\x00t\x18\x00i!\x00|\x12\x00i\x1a\x00\x83\x01\x00}\x14\x00|\x06\x00o\x04\x00\x01|\x14\x00}\x0b\x00|\x06\x00o\x1a\x00\x01t\x18\x00i\x1b\x00d\x07\x00d\x01\x00|\x00\x00|\x01\x00\x83\x04\x00\x01n\x01\x00\x01|\x14\x00o\x1a\x00\x01t\x18\x00i\x1b\x00d\x08\x00d\x01\x00|\x00\x00|\x01\x00\x83\x04\x00\x01n\x01\x00\x01|\x13\x00o\x04\x00\x01|\x0b\x00oG\x00\x01t\x18\x00i\x1b\x00d\t\x00d\x01\x00|\x00\x00|\x01\x00\x83\x04\x00\x01|\x17\x00|\n\x00j\x04\x00o \x00\x01t\x18\x00i\x1b\x00d\n\x00d\x01\x00|\x00\x00|\x01\x00\x83\x04\x00\x01d\x01\x00}\x10\x00q)\x02\x01n\x19\x00\x01|\x14\x00o\x04\x00\x01|\x0f\x00o\n\x00\x01d\x01\x00}\x10\x00n\x01\x00\x01|\x10\x00d\x01\x00j\x02\x00on\x00\x01t\x18\x00i\x1b\x00d\x0b\x00d\x01\x00|\x00\x00|\x01\x00\x83\x04\x00\x01|\x01\x00}\x18\x00|\x00\x00}\x12\x00|\x0e\x00}\x08\x00|\x07\x00}\x19\x00|\n\x00}\x16\x00|\t\x00}\x0c\x00|\x0f\x00}\x0e\x00|\r\x00}\x07\x00|\x17\x00}\n\x00|\x11\x00}\t\x00|\x08\x00}\x0f\x00|\x19\x00}\r\x00|\x16\x00}\x17\x00|\x0c\x00}\x11\x00n\x01\x00\x01t\x1c\x00}\x04\x00t\x18\x00i!\x00|\x18\x00i\x1a\x00\x83\x01\x00o\x04\x00\x01|\x0e\x00o-\x00\x01t\x18\x00i\x1b\x00d\x0c\x00d\x01\x00|\x00\x00|\x01\x00\x83\x04\x00\x01t*\x00|\x18\x00|\x03\x00\x83\x02\x00\x01t\x1c\x00}\x0f\x00n\xa0\x00\x01|\x00\x00i+\x00o-\x00\x01t\x18\x00i\x1b\x00d\r\x00d\x01\x00|\x00\x00|\x01\x00\x83\x04\x00\x01t,\x00|\x00\x00|\x01\x00|\x03\x00|\x18\x00\x83\x04\x00\x01ni\x00\x01|\x18\x00i-\x00t\x14\x00i.\x00i/\x00j\x02\x00o$\x00\x01t\x18\x00i\x1b\x00d\x0e\x00d\x01\x00\x83\x02\x00\x01t0\x00|\x18\x00|\x12\x00|\x03\x00\x83\x03\x00\x01n/\x00\x01t\x18\x00i\x1b\x00d\x0f\x00d\x01\x00|\x00\x00|\x01\x00\x83\x04\x00\x01t1\x00|\x18\x00|\x12\x00|\x03\x00|\x0e\x00|\x0f\x00\x83\x05\x00}\x04\x00t2\x00}\x05\x00t2\x00}\x15\x00|\x03\x00i5\x00|\x00\x00i6\x00j\x02\x00o"\x00\x01|\x00\x00}\x05\x00|\x01\x00}\x15\x00|\n\x00|\x03\x00_7\x00|\x17\x00|\x03\x00_8\x00n\x1f\x00\x01|\x01\x00}\x05\x00|\x00\x00}\x15\x00|\x17\x00|\x03\x00_7\x00|\n\x00|\x03\x00_8\x00t\x18\x00i\x1b\x00d\x10\x00|\x05\x00i6\x00|\x03\x00i5\x00|\x15\x00i6\x00f\x03\x00\x16d\x01\x00|\x00\x00|\x01\x00\x83\x04\x00\x01|\x03\x00i9\x00t\x14\x00i.\x00i:\x00j\x02\x00oD\x00\x01t\x18\x00i!\x00|\x05\x00i\x1a\x00\x83\x01\x00o\r\x00\x01d\x01\x00|\x03\x00_;\x00qu\x04\x01t\x18\x00i!\x00|\x15\x00i\x1a\x00\x83\x01\x00o\r\x00\x01d\x01\x00|\x03\x00_<\x00qu\x04\x01n\x01\x00\x01d\x00\x00S' (79 04 00 00 7C 00 00 69 01 00 7C 03 00 5F 03 00 7C 01 00 69 01 00 7C 03 00 5F 05 00 74 06 00 7C 00 00 7C 01 00 83 02 00 5C 08 00 7D 0A 00 7D 09 00 7D 07 00 7D 0E 00 7D 17 00 7D 11 00 7D 0D 00 7D 0F 00 74 0F 00 69 10 00 64 01 00 6A 05 00 6F 3C 00 01 74 11 00 69 12 00 7C 00 00 69 13 00 64 02 00 74 14 00 69 15 00 69 16 00 83 03 00 01 74 11 00 69 12 00 7C 01 00 69 13 00 64 03 00 74 14 00 69 15 00 69 16 00 83 03 00 01 6E 01 00 01 7C 01 00 69 17 00 70 10 00 01 74 18 00 69 19 00 7C 01 00 69 1A 00 83 01 00 6F 26 00 01 74 18 00 69 1B 00 64 04 00 64 01 00 7C 00 00 7C 01 00 83 04 00 01 64 05 00 7D 17 00 74 1C 00 7D 0F 00 6E 01 00 01 7C 00 00 69 17 00 70 10 00 01 74 18 00 69 19 00 7C 00 00 69 1A 00 83 01 00 6F 26 00 01 74 18 00 69 1B 00 64 06 00 64 01 00 7C 00 00 7C 01 00 83 04 00 01 64 05 00 7D 0A 00 74 1C 00 7D 0E 00 6E 01 00 01 64 05 00 7D 10 00 7C 00 00 7D 18 00 7C 01 00 7D 12 00 7C 0F 00 6F 05 00 01 7C 0E 00 0C 6F 0A 00 01 64 01 00 7D 10 00 6E 01 00 01 7C 0F 00 6F 04 00 01 7C 0E 00 7D 13 00 74 18 00 69 21 00 7C 18 00 69 1A 00 83 01 00 7D 06 00 74 18 00 69 21 00 7C 12 00 69 1A 00 83 01 00 7D 14 00 7C 06 00 6F 04 00 01 7C 14 00 7D 0B 00 7C 06 00 6F 1A 00 01 74 18 00 69 1B 00 64 07 00 64 01 00 7C 00 00 7C 01 00 83 04 00 01 6E 01 00 01 7C 14 00 6F 1A 00 01 74 18 00 69 1B 00 64 08 00 64 01 00 7C 00 00 7C 01 00 83 04 00 01 6E 01 00 01 7C 13 00 6F 04 00 01 7C 0B 00 6F 47 00 01 74 18 00 69 1B 00 64 09 00 64 01 00 7C 00 00 7C 01 00 83 04 00 01 7C 17 00 7C 0A 00 6A 04 00 6F 20 00 01 74 18 00 69 1B 00 64 0A 00 64 01 00 7C 00 00 7C 01 00 83 04 00 01 64 01 00 7D 10 00 71 29 02 01 6E 19 00 01 7C 14 00 6F 04 00 01 7C 0F 00 6F 0A 00 01 64 01 00 7D 10 00 6E 01 00 01 7C 10 00 64 01 00 6A 02 00 6F 6E 00 01 74 18 00 69 1B 00 64 0B 00 64 01 00 7C 00 00 7C 01 00 83 04 00 01 7C 01 00 7D 18 00 7C 00 00 7D 12 00 7C 0E 00 7D 08 00 7C 07 00 7D 19 00 7C 0A 00 7D 16 00 7C 09 00 7D 0C 00 7C 0F 00 7D 0E 00 7C 0D 00 7D 07 00 7C 17 00 7D 0A 00 7C 11 00 7D 09 00 7C 08 00 7D 0F 00 7C 19 00 7D 0D 00 7C 16 00 7D 17 00 7C 0C 00 7D 11 00 6E 01 00 01 74 1C 00 7D 04 00 74 18 00 69 21 00 7C 18 00 69 1A 00 83 01 00 6F 04 00 01 7C 0E 00 6F 2D 00 01 74 18 00 69 1B 00 64 0C 00 64 01 00 7C 00 00 7C 01 00 83 04 00 01 74 2A 00 7C 18 00 7C 03 00 83 02 00 01 74 1C 00 7D 0F 00 6E A0 00 01 7C 00 00 69 2B 00 6F 2D 00 01 74 18 00 69 1B 00 64 0D 00 64 01 00 7C 00 00 7C 01 00 83 04 00 01 74 2C 00 7C 00 00 7C 01 00 7C 03 00 7C 18 00 83 04 00 01 6E 69 00 01 7C 18 00 69 2D 00 74 14 00 69 2E 00 69 2F 00 6A 02 00 6F 24 00 01 74 18 00 69 1B 00 64 0E 00 64 01 00 83 02 00 01 74 30 00 7C 18 00 7C 12 00 7C 03 00 83 03 00 01 6E 2F 00 01 74 18 00 69 1B 00 64 0F 00 64 01 00 7C 00 00 7C 01 00 83 04 00 01 74 31 00 7C 18 00 7C 12 00 7C 03 00 7C 0E 00 7C 0F 00 83 05 00 7D 04 00 74 32 00 7D 05 00 74 32 00 7D 15 00 7C 03 00 69 35 00 7C 00 00 69 36 00 6A 02 00 6F 22 00 01 7C 00 00 7D 05 00 7C 01 00 7D 15 00 7C 0A 00 7C 03 00 5F 37 00 7C 17 00 7C 03 00 5F 38 00 6E 1F 00 01 7C 01 00 7D 05 00 7C 00 00 7D 15 00 7C 17 00 7C 03 00 5F 37 00 7C 0A 00 7C 03 00 5F 38 00 74 18 00 69 1B 00 64 10 00 7C 05 00 69 36 00 7C 03 00 69 35 00 7C 15 00 69 36 00 66 03 00 16 64 01 00 7C 00 00 7C 01 00 83 04 00 01 7C 03 00 69 39 00 74 14 00 69 2E 00 69 3A 00 6A 02 00 6F 44 00 01 74 18 00 69 21 00 7C 05 00 69 1A 00 83 01 00 6F 0D 00 01 64 01 00 7C 03 00 5F 3B 00 71 75 04 01 74 18 00 69 21 00 7C 15 00 69 1A 00 83 01 00 6F 0D 00 01 64 01 00 7C 03 00 5F 3C 00 71 75 04 01 6E 01 00 01 64 00 00 53)
                             00000000     7C - LOAD_FAST           'attacker'
                             00000003     69 - LOAD_ATTR           'tacticalValue'
                             00000006     7C - LOAD_FAST           'result'
                             00000009     5F - STORE_ATTR          'attacker_level'
                             0000000C     7C - LOAD_FAST           'defender'
                             0000000F     69 - LOAD_ATTR           'tacticalValue'
                             00000012     7C - LOAD_FAST           'result'
                             00000015     5F - STORE_ATTR          'defender_level'
                             00000018     74 - LOAD_GLOBAL         'getCTandDTotals'
                             0000001B     7C - LOAD_FAST           'attacker'
                             0000001E     7C - LOAD_FAST           'defender'
                             00000021     83 - CALL_FUNCTION       r0002
                             00000024     5C - UNPACK_SEQUENCE     r0008
                             00000027     7D - STORE_FAST          'attackerCT_total'
                             0000002A     7D - STORE_FAST          'attackerD_total'
                             0000002D     7D - STORE_FAST          'attackersAdvantage'
                             00000030     7D - STORE_FAST          'attackerHits'
                             00000033     7D - STORE_FAST          'defenderCT_total'
                             00000036     7D - STORE_FAST          'defenderD_total'
                             00000039     7D - STORE_FAST          'defendersAdvantage'
                             0000003C     7D - STORE_FAST          'defenderHits'
                             0000003F     74 - LOAD_GLOBAL         'consolevar'
                             00000042     69 - LOAD_ATTR           'SendClientCombatData'
                             00000045     64 - LOAD_CONST          1
                             00000048     6A - COMPARE_OP          ">="
                             0000004B     6F - JUMP_IF_FALSE       -> 0000008A
                             0000004E     01 - POP_TOP             
                             0000004F     74 - LOAD_GLOBAL         'discovery'
                             00000052     69 - LOAD_ATTR           'clientSystemMessage2'
                             00000055     7C - LOAD_FAST           'attacker'
                             00000058     69 - LOAD_ATTR           'locator'
                             0000005B     64 - LOAD_CONST          'You are attacker.'
                             0000005E     74 - LOAD_GLOBAL         'constants'
                             00000061     69 - LOAD_ATTR           'Chat'
                             00000064     69 - LOAD_ATTR           'CT_SYS_DEBUG'
                             00000067     83 - CALL_FUNCTION       r0003
                             0000006A     01 - POP_TOP             
                             0000006B     74 - LOAD_GLOBAL         'discovery'
                             0000006E     69 - LOAD_ATTR           'clientSystemMessage2'
                             00000071     7C - LOAD_FAST           'defender'
                             00000074     69 - LOAD_ATTR           'locator'
                             00000077     64 - LOAD_CONST          'You are defender.'
                             0000007A     74 - LOAD_GLOBAL         'constants'
                             0000007D     69 - LOAD_ATTR           'Chat'
                             00000080     69 - LOAD_ATTR           'CT_SYS_DEBUG'
                             00000083     83 - CALL_FUNCTION       r0003
                             00000086     01 - POP_TOP             
                             00000087     6E - JUMP_FORWARD        -> 0000008B
                             0000008A     01 - POP_TOP             
                             0000008B     7C - LOAD_FAST           'defender'
                             0000008E     69 - LOAD_ATTR           'isAttemptingWithdraw'
                             00000091     70 - JUMP_IF_TRUE        -> 000000A4
                             00000094     01 - POP_TOP             
                             00000095     74 - LOAD_GLOBAL         'CU'
                             00000098     69 - LOAD_ATTR           'isEscapeAbility'
                             0000009B     7C - LOAD_FAST           'defender'
                             0000009E     69 - LOAD_ATTR           'requestedSpecialMove'
                             000000A1     83 - CALL_FUNCTION       r0001
                             000000A4     6F - JUMP_IF_FALSE       -> 000000CD
                             000000A7     01 - POP_TOP             
                             000000A8     74 - LOAD_GLOBAL         'CU'
                             000000AB     69 - LOAD_ATTR           'outputCombatDebugMessageAll'
                             000000AE     64 - LOAD_CONST          'defender withdrawing: CT -> 0. No hit'
                             000000B1     64 - LOAD_CONST          1
                             000000B4     7C - LOAD_FAST           'attacker'
                             000000B7     7C - LOAD_FAST           'defender'
                             000000BA     83 - CALL_FUNCTION       r0004
                             000000BD     01 - POP_TOP             
                             000000BE     64 - LOAD_CONST          0
                             000000C1     7D - STORE_FAST          'defenderCT_total'
                             000000C4     74 - LOAD_GLOBAL         'False'
                             000000C7     7D - STORE_FAST          'defenderHits'
                             000000CA     6E - JUMP_FORWARD        -> 000000CE
                             000000CD     01 - POP_TOP             
                             000000CE     7C - LOAD_FAST           'attacker'
                             000000D1     69 - LOAD_ATTR           'isAttemptingWithdraw'
                             000000D4     70 - JUMP_IF_TRUE        -> 000000E7
                             000000D7     01 - POP_TOP             
                             000000D8     74 - LOAD_GLOBAL         'CU'
                             000000DB     69 - LOAD_ATTR           'isEscapeAbility'
                             000000DE     7C - LOAD_FAST           'attacker'
                             000000E1     69 - LOAD_ATTR           'requestedSpecialMove'
                             000000E4     83 - CALL_FUNCTION       r0001
                             000000E7     6F - JUMP_IF_FALSE       -> 00000110
                             000000EA     01 - POP_TOP             
                             000000EB     74 - LOAD_GLOBAL         'CU'
                             000000EE     69 - LOAD_ATTR           'outputCombatDebugMessageAll'
                             000000F1     64 - LOAD_CONST          'attacker withdrawing: CT -> 0. No hit'
                             000000F4     64 - LOAD_CONST          1
                             000000F7     7C - LOAD_FAST           'attacker'
                             000000FA     7C - LOAD_FAST           'defender'
                             000000FD     83 - CALL_FUNCTION       r0004
                             00000100     01 - POP_TOP             
                             00000101     64 - LOAD_CONST          0
                             00000104     7D - STORE_FAST          'attackerCT_total'
                             00000107     74 - LOAD_GLOBAL         'False'
                             0000010A     7D - STORE_FAST          'attackerHits'
                             0000010D     6E - JUMP_FORWARD        -> 00000111
                             00000110     01 - POP_TOP             
                             00000111     64 - LOAD_CONST          0
                             00000114     7D - STORE_FAST          'switchAttackerDefender'
                             00000117     7C - LOAD_FAST           'attacker'
                             0000011A     7D - STORE_FAST          'true_attacker'
                             0000011D     7C - LOAD_FAST           'defender'
                             00000120     7D - STORE_FAST          'true_defender'
                             00000123     7C - LOAD_FAST           'defenderHits'
                             00000126     6F - JUMP_IF_FALSE       -> 0000012E
                             00000129     01 - POP_TOP             
                             0000012A     7C - LOAD_FAST           'attackerHits'
                             0000012D     0C - UNARY_NOT           
                             0000012E     6F - JUMP_IF_FALSE       -> 0000013B
                             00000131     01 - POP_TOP             
                             00000132     64 - LOAD_CONST          1
                             00000135     7D - STORE_FAST          'switchAttackerDefender'
                             00000138     6E - JUMP_FORWARD        -> 0000013C
                             0000013B     01 - POP_TOP             
                             0000013C     7C - LOAD_FAST           'defenderHits'
                             0000013F     6F - JUMP_IF_FALSE       -> 00000146
                             00000142     01 - POP_TOP             
                             00000143     7C - LOAD_FAST           'attackerHits'
                             00000146     7D - STORE_FAST          'bothHit'
                             00000149     74 - LOAD_GLOBAL         'CU'
                             0000014C     69 - LOAD_ATTR           'isSpecialMove'
                             0000014F     7C - LOAD_FAST           'true_attacker'
                             00000152     69 - LOAD_ATTR           'requestedSpecialMove'
                             00000155     83 - CALL_FUNCTION       r0001
                             00000158     7D - STORE_FAST          'aUsesSM'
                             0000015B     74 - LOAD_GLOBAL         'CU'
                             0000015E     69 - LOAD_ATTR           'isSpecialMove'
                             00000161     7C - LOAD_FAST           'true_defender'
                             00000164     69 - LOAD_ATTR           'requestedSpecialMove'
                             00000167     83 - CALL_FUNCTION       r0001
                             0000016A     7D - STORE_FAST          'dUsesSM'
                             0000016D     7C - LOAD_FAST           'aUsesSM'
                             00000170     6F - JUMP_IF_FALSE       -> 00000177
                             00000173     01 - POP_TOP             
                             00000174     7C - LOAD_FAST           'dUsesSM'
                             00000177     7D - STORE_FAST          'bothUseSM'
                             0000017A     7C - LOAD_FAST           'aUsesSM'
                             0000017D     6F - JUMP_IF_FALSE       -> 0000019A
                             00000180     01 - POP_TOP             
                             00000181     74 - LOAD_GLOBAL         'CU'
                             00000184     69 - LOAD_ATTR           'outputCombatDebugMessageAll'
                             00000187     64 - LOAD_CONST          'Attacker requesting special move'
                             0000018A     64 - LOAD_CONST          1
                             0000018D     7C - LOAD_FAST           'attacker'
                             00000190     7C - LOAD_FAST           'defender'
                             00000193     83 - CALL_FUNCTION       r0004
                             00000196     01 - POP_TOP             
                             00000197     6E - JUMP_FORWARD        -> 0000019B
                             0000019A     01 - POP_TOP             
                             0000019B     7C - LOAD_FAST           'dUsesSM'
                             0000019E     6F - JUMP_IF_FALSE       -> 000001BB
                             000001A1     01 - POP_TOP             
                             000001A2     74 - LOAD_GLOBAL         'CU'
                             000001A5     69 - LOAD_ATTR           'outputCombatDebugMessageAll'
                             000001A8     64 - LOAD_CONST          'Defender requesting special move'
                             000001AB     64 - LOAD_CONST          1
                             000001AE     7C - LOAD_FAST           'attacker'
                             000001B1     7C - LOAD_FAST           'defender'
                             000001B4     83 - CALL_FUNCTION       r0004
                             000001B7     01 - POP_TOP             
                             000001B8     6E - JUMP_FORWARD        -> 000001BC
                             000001BB     01 - POP_TOP             
                             000001BC     7C - LOAD_FAST           'bothHit'
                             000001BF     6F - JUMP_IF_FALSE       -> 000001C6
                             000001C2     01 - POP_TOP             
                             000001C3     7C - LOAD_FAST           'bothUseSM'
                             000001C6     6F - JUMP_IF_FALSE       -> 00000210
                             000001C9     01 - POP_TOP             
                             000001CA     74 - LOAD_GLOBAL         'CU'
                             000001CD     69 - LOAD_ATTR           'outputCombatDebugMessageAll'
                             000001D0     64 - LOAD_CONST          'SM BOTH: !!!'
                             000001D3     64 - LOAD_CONST          1
                             000001D6     7C - LOAD_FAST           'attacker'
                             000001D9     7C - LOAD_FAST           'defender'
                             000001DC     83 - CALL_FUNCTION       r0004
                             000001DF     01 - POP_TOP             
                             000001E0     7C - LOAD_FAST           'defenderCT_total'
                             000001E3     7C - LOAD_FAST           'attackerCT_total'
                             000001E6     6A - COMPARE_OP          ">"
                             000001E9     6F - JUMP_IF_FALSE       -> 0000020C
                             000001EC     01 - POP_TOP             
                             000001ED     74 - LOAD_GLOBAL         'CU'
                             000001F0     69 - LOAD_ATTR           'outputCombatDebugMessageAll'
                             000001F3     64 - LOAD_CONST          'SM BOTH: Defender wins!'
                             000001F6     64 - LOAD_CONST          1
                             000001F9     7C - LOAD_FAST           'attacker'
                             000001FC     7C - LOAD_FAST           'defender'
                             000001FF     83 - CALL_FUNCTION       r0004
                             00000202     01 - POP_TOP             
                             00000203     64 - LOAD_CONST          1
                             00000206     7D - STORE_FAST          'switchAttackerDefender'
                             00000209     71 - JUMP_ABSOLUTE       -> 00000229
                             0000020C     01 - POP_TOP             
                             0000020D     6E - JUMP_FORWARD        -> 00000229
                             00000210     01 - POP_TOP             
                             00000211     7C - LOAD_FAST           'dUsesSM'
                             00000214     6F - JUMP_IF_FALSE       -> 0000021B
                             00000217     01 - POP_TOP             
                             00000218     7C - LOAD_FAST           'defenderHits'
                             0000021B     6F - JUMP_IF_FALSE       -> 00000228
                             0000021E     01 - POP_TOP             
                             0000021F     64 - LOAD_CONST          1
                             00000222     7D - STORE_FAST          'switchAttackerDefender'
                             00000225     6E - JUMP_FORWARD        -> 00000229
                             00000228     01 - POP_TOP             
                             00000229     7C - LOAD_FAST           'switchAttackerDefender'
                             0000022C     64 - LOAD_CONST          1
                             0000022F     6A - COMPARE_OP          "=="
                             00000232     6F - JUMP_IF_FALSE       -> 000002A3
                             00000235     01 - POP_TOP             
                             00000236     74 - LOAD_GLOBAL         'CU'
                             00000239     69 - LOAD_ATTR           'outputCombatDebugMessageAll'
                             0000023C     64 - LOAD_CONST          'switching Attacker/Defender'
                             0000023F     64 - LOAD_CONST          1
                             00000242     7C - LOAD_FAST           'attacker'
                             00000245     7C - LOAD_FAST           'defender'
                             00000248     83 - CALL_FUNCTION       r0004
                             0000024B     01 - POP_TOP             
                             0000024C     7C - LOAD_FAST           'defender'
                             0000024F     7D - STORE_FAST          'true_attacker'
                             00000252     7C - LOAD_FAST           'attacker'
                             00000255     7D - STORE_FAST          'true_defender'
                             00000258     7C - LOAD_FAST           'attackerHits'
                             0000025B     7D - STORE_FAST          'tempAHit'
                             0000025E     7C - LOAD_FAST           'attackersAdvantage'
                             00000261     7D - STORE_FAST          'tempAAdvan'
                             00000264     7C - LOAD_FAST           'attackerCT_total'
                             00000267     7D - STORE_FAST          'tempACT'
                             0000026A     7C - LOAD_FAST           'attackerD_total'
                             0000026D     7D - STORE_FAST          'tempAD'
                             00000270     7C - LOAD_FAST           'defenderHits'
                             00000273     7D - STORE_FAST          'attackerHits'
                             00000276     7C - LOAD_FAST           'defendersAdvantage'
                             00000279     7D - STORE_FAST          'attackersAdvantage'
                             0000027C     7C - LOAD_FAST           'defenderCT_total'
                             0000027F     7D - STORE_FAST          'attackerCT_total'
                             00000282     7C - LOAD_FAST           'defenderD_total'
                             00000285     7D - STORE_FAST          'attackerD_total'
                             00000288     7C - LOAD_FAST           'tempAHit'
                             0000028B     7D - STORE_FAST          'defenderHits'
                             0000028E     7C - LOAD_FAST           'tempAAdvan'
                             00000291     7D - STORE_FAST          'defendersAdvantage'
                             00000294     7C - LOAD_FAST           'tempACT'
                             00000297     7D - STORE_FAST          'defenderCT_total'
                             0000029A     7C - LOAD_FAST           'tempAD'
                             0000029D     7D - STORE_FAST          'defenderD_total'
                             000002A0     6E - JUMP_FORWARD        -> 000002A4
                             000002A3     01 - POP_TOP             
                             000002A4     74 - LOAD_GLOBAL         'False'
                             000002A7     7D - STORE_FAST          'flipAtkDef'
                             000002AA     74 - LOAD_GLOBAL         'CU'
                             000002AD     69 - LOAD_ATTR           'isSpecialMove'
                             000002B0     7C - LOAD_FAST           'true_attacker'
                             000002B3     69 - LOAD_ATTR           'requestedSpecialMove'
                             000002B6     83 - CALL_FUNCTION       r0001
                             000002B9     6F - JUMP_IF_FALSE       -> 000002C0
                             000002BC     01 - POP_TOP             
                             000002BD     7C - LOAD_FAST           'attackerHits'
                             000002C0     6F - JUMP_IF_FALSE       -> 000002F0
                             000002C3     01 - POP_TOP             
                             000002C4     74 - LOAD_GLOBAL         'CU'
                             000002C7     69 - LOAD_ATTR           'outputCombatDebugMessageAll'
                             000002CA     64 - LOAD_CONST          'Special Move handled!'
                             000002CD     64 - LOAD_CONST          1
                             000002D0     7C - LOAD_FAST           'attacker'
                             000002D3     7C - LOAD_FAST           'defender'
                             000002D6     83 - CALL_FUNCTION       r0004
                             000002D9     01 - POP_TOP             
                             000002DA     74 - LOAD_GLOBAL         'handleSpecialMove'
                             000002DD     7C - LOAD_FAST           'true_attacker'
                             000002E0     7C - LOAD_FAST           'result'
                             000002E3     83 - CALL_FUNCTION       r0002
                             000002E6     01 - POP_TOP             
                             000002E7     74 - LOAD_GLOBAL         'False'
                             000002EA     7D - STORE_FAST          'defenderHits'
                             000002ED     6E - JUMP_FORWARD        -> 00000390
                             000002F0     01 - POP_TOP             
                             000002F1     7C - LOAD_FAST           'attacker'
                             000002F4     69 - LOAD_ATTR           'opportunityAttack'
                             000002F7     6F - JUMP_IF_FALSE       -> 00000327
                             000002FA     01 - POP_TOP             
                             000002FB     74 - LOAD_GLOBAL         'CU'
                             000002FE     69 - LOAD_ATTR           'outputCombatDebugMessageAll'
                             00000301     64 - LOAD_CONST          'Opportunity Attack Handled!'
                             00000304     64 - LOAD_CONST          1
                             00000307     7C - LOAD_FAST           'attacker'
                             0000030A     7C - LOAD_FAST           'defender'
                             0000030D     83 - CALL_FUNCTION       r0004
                             00000310     01 - POP_TOP             
                             00000311     74 - LOAD_GLOBAL         'handleOppertunityAttack'
                             00000314     7C - LOAD_FAST           'attacker'
                             00000317     7C - LOAD_FAST           'defender'
                             0000031A     7C - LOAD_FAST           'result'
                             0000031D     7C - LOAD_FAST           'true_attacker'
                             00000320     83 - CALL_FUNCTION       r0004
                             00000323     01 - POP_TOP             
                             00000324     6E - JUMP_FORWARD        -> 00000390
                             00000327     01 - POP_TOP             
                             00000328     7C - LOAD_FAST           'true_attacker'
                             0000032B     69 - LOAD_ATTR           'tacticalSetting'
                             0000032E     74 - LOAD_GLOBAL         'constants'
                             00000331     69 - LOAD_ATTR           'combat'
                             00000334     69 - LOAD_ATTR           'BLOCK'
                             00000337     6A - COMPARE_OP          "=="
                             0000033A     6F - JUMP_IF_FALSE       -> 00000361
                             0000033D     01 - POP_TOP             
                             0000033E     74 - LOAD_GLOBAL         'CU'
                             00000341     69 - LOAD_ATTR           'outputCombatDebugMessageAll'
                             00000344     64 - LOAD_CONST          'Block Handled!'
                             00000347     64 - LOAD_CONST          1
                             0000034A     83 - CALL_FUNCTION       r0002
                             0000034D     01 - POP_TOP             
                             0000034E     74 - LOAD_GLOBAL         'handleBlock'
                             00000351     7C - LOAD_FAST           'true_attacker'
                             00000354     7C - LOAD_FAST           'true_defender'
                             00000357     7C - LOAD_FAST           'result'
                             0000035A     83 - CALL_FUNCTION       r0003
                             0000035D     01 - POP_TOP             
                             0000035E     6E - JUMP_FORWARD        -> 00000390
                             00000361     01 - POP_TOP             
                             00000362     74 - LOAD_GLOBAL         'CU'
                             00000365     69 - LOAD_ATTR           'outputCombatDebugMessageAll'
                             00000368     64 - LOAD_CONST          'Standard Exchange Handled!'
                             0000036B     64 - LOAD_CONST          1
                             0000036E     7C - LOAD_FAST           'attacker'
                             00000371     7C - LOAD_FAST           'defender'
                             00000374     83 - CALL_FUNCTION       r0004
                             00000377     01 - POP_TOP             
                             00000378     74 - LOAD_GLOBAL         'handleStandardExchange'
                             0000037B     7C - LOAD_FAST           'true_attacker'
                             0000037E     7C - LOAD_FAST           'true_defender'
                             00000381     7C - LOAD_FAST           'result'
                             00000384     7C - LOAD_FAST           'attackerHits'
                             00000387     7C - LOAD_FAST           'defenderHits'
                             0000038A     83 - CALL_FUNCTION       r0005
                             0000038D     7D - STORE_FAST          'flipAtkDef'
                             00000390     74 - LOAD_GLOBAL         'None'
                             00000393     7D - STORE_FAST          'winner'
                             00000396     74 - LOAD_GLOBAL         'None'
                             00000399     7D - STORE_FAST          'loser'
                             0000039C     7C - LOAD_FAST           'result'
                             0000039F     69 - LOAD_ATTR           'winnerSlot'
                             000003A2     7C - LOAD_FAST           'attacker'
                             000003A5     69 - LOAD_ATTR           'slot'
                             000003A8     6A - COMPARE_OP          "=="
                             000003AB     6F - JUMP_IF_FALSE       -> 000003D0
                             000003AE     01 - POP_TOP             
                             000003AF     7C - LOAD_FAST           'attacker'
                             000003B2     7D - STORE_FAST          'winner'
                             000003B5     7C - LOAD_FAST           'defender'
                             000003B8     7D - STORE_FAST          'loser'
                             000003BB     7C - LOAD_FAST           'attackerCT_total'
                             000003BE     7C - LOAD_FAST           'result'
                             000003C1     5F - STORE_ATTR          'attackerValue'
                             000003C4     7C - LOAD_FAST           'defenderCT_total'
                             000003C7     7C - LOAD_FAST           'result'
                             000003CA     5F - STORE_ATTR          'defenderValue'
                             000003CD     6E - JUMP_FORWARD        -> 000003EF
                             000003D0     01 - POP_TOP             
                             000003D1     7C - LOAD_FAST           'defender'
                             000003D4     7D - STORE_FAST          'winner'
                             000003D7     7C - LOAD_FAST           'attacker'
                             000003DA     7D - STORE_FAST          'loser'
                             000003DD     7C - LOAD_FAST           'defenderCT_total'
                             000003E0     7C - LOAD_FAST           'result'
                             000003E3     5F - STORE_ATTR          'attackerValue'
                             000003E6     7C - LOAD_FAST           'attackerCT_total'
                             000003E9     7C - LOAD_FAST           'result'
                             000003EC     5F - STORE_ATTR          'defenderValue'
                             000003EF     74 - LOAD_GLOBAL         'CU'
                             000003F2     69 - LOAD_ATTR           'outputCombatDebugMessageAll'
                             000003F5     64 - LOAD_CONST          'winner: %d(%d) loser %d'
                             000003F8     7C - LOAD_FAST           'winner'
                             000003FB     69 - LOAD_ATTR           'slot'
                             000003FE     7C - LOAD_FAST           'result'
                             00000401     69 - LOAD_ATTR           'winnerSlot'
                             00000404     7C - LOAD_FAST           'loser'
                             00000407     69 - LOAD_ATTR           'slot'
                             0000040A     66 - BUILD_TUPLE         r0003
                             0000040D     16 - BINARY_MODULO       
                             0000040E     64 - LOAD_CONST          1
                             00000411     7C - LOAD_FAST           'attacker'
                             00000414     7C - LOAD_FAST           'defender'
                             00000417     83 - CALL_FUNCTION       r0004
                             0000041A     01 - POP_TOP             
                             0000041B     7C - LOAD_FAST           'result'
                             0000041E     69 - LOAD_ATTR           'outcomeFlag'
                             00000421     74 - LOAD_GLOBAL         'constants'
                             00000424     69 - LOAD_ATTR           'combat'
                             00000427     69 - LOAD_ATTR           'SPECIAL_MOVE'
                             0000042A     6A - COMPARE_OP          "=="
                             0000042D     6F - JUMP_IF_FALSE       -> 00000474
                             00000430     01 - POP_TOP             
                             00000431     74 - LOAD_GLOBAL         'CU'
                             00000434     69 - LOAD_ATTR           'isSpecialMove'
                             00000437     7C - LOAD_FAST           'winner'
                             0000043A     69 - LOAD_ATTR           'requestedSpecialMove'
                             0000043D     83 - CALL_FUNCTION       r0001
                             00000440     6F - JUMP_IF_FALSE       -> 00000450
                             00000443     01 - POP_TOP             
                             00000444     64 - LOAD_CONST          1
                             00000447     7C - LOAD_FAST           'result'
                             0000044A     5F - STORE_ATTR          'winnerSpecialMoveUsed'
                             0000044D     71 - JUMP_ABSOLUTE       -> 00000475
                             00000450     01 - POP_TOP             
                             00000451     74 - LOAD_GLOBAL         'CU'
                             00000454     69 - LOAD_ATTR           'isSpecialMove'
                             00000457     7C - LOAD_FAST           'loser'
                             0000045A     69 - LOAD_ATTR           'requestedSpecialMove'
                             0000045D     83 - CALL_FUNCTION       r0001
                             00000460     6F - JUMP_IF_FALSE       -> 00000470
                             00000463     01 - POP_TOP             
                             00000464     64 - LOAD_CONST          1
                             00000467     7C - LOAD_FAST           'result'
                             0000046A     5F - STORE_ATTR          'loserSpecialMoveUsed'
                             0000046D     71 - JUMP_ABSOLUTE       -> 00000475
                             00000470     01 - POP_TOP             
                             00000471     6E - JUMP_FORWARD        -> 00000475
                             00000474     01 - POP_TOP             
                             00000475     64 - LOAD_CONST          None
                             00000478     53 - RETURN_VALUE        
                         consts:
00004100                     TUPLE: (
00004105                         None (4E),
00004106                         INT: 1 (01 00 00 00),
0000410B                         STR: 'You are attacker.' (11 00 00 00 59 6F 75 20 61 72 65 20 61 74 74 61 63 6B 65 72 2E),
00004121                         STR: 'You are defender.' (11 00 00 00 59 6F 75 20 61 72 65 20 64 65 66 65 6E 64 65 72 2E),
00004137                         STR: 'defender withdrawing: CT -> 0. No hit' (25 00 00 00 64 65 66 65 6E 64 65 72 20 77 69 74 68 64 72 61 77 69 6E 67 3A 20 43 54 20 2D 3E 20 30 2E 20 4E 6F 20 68 69 74),
00004161                         INT: 0 (00 00 00 00),
00004166                         STR: 'attacker withdrawing: CT -> 0. No hit' (25 00 00 00 61 74 74 61 63 6B 65 72 20 77 69 74 68 64 72 61 77 69 6E 67 3A 20 43 54 20 2D 3E 20 30 2E 20 4E 6F 20 68 69 74),
00004190                         STR: 'Attacker requesting special move' (20 00 00 00 41 74 74 61 63 6B 65 72 20 72 65 71 75 65 73 74 69 6E 67 20 73 70 65 63 69 61 6C 20 6D 6F 76 65),
000041B5                         STR: 'Defender requesting special move' (20 00 00 00 44 65 66 65 6E 64 65 72 20 72 65 71 75 65 73 74 69 6E 67 20 73 70 65 63 69 61 6C 20 6D 6F 76 65),
000041DA                         STR: 'SM BOTH: !!!' (0C 00 00 00 53 4D 20 42 4F 54 48 3A 20 21 21 21),
000041EB                         STR: 'SM BOTH: Defender wins!' (17 00 00 00 53 4D 20 42 4F 54 48 3A 20 44 65 66 65 6E 64 65 72 20 77 69 6E 73 21),
00004207                         STR: 'switching Attacker/Defender' (1B 00 00 00 73 77 69 74 63 68 69 6E 67 20 41 74 74 61 63 6B 65 72 2F 44 65 66 65 6E 64 65 72),
00004227                         STR: 'Special Move handled!' (15 00 00 00 53 70 65 63 69 61 6C 20 4D 6F 76 65 20 68 61 6E 64 6C 65 64 21),
00004241                         STR: 'Opportunity Attack Handled!' (1B 00 00 00 4F 70 70 6F 72 74 75 6E 69 74 79 20 41 74 74 61 63 6B 20 48 61 6E 64 6C 65 64 21),
00004261                         STR: 'Block Handled!' (0E 00 00 00 42 6C 6F 63 6B 20 48 61 6E 64 6C 65 64 21),
00004274                         STR: 'Standard Exchange Handled!' (1A 00 00 00 53 74 61 6E 64 61 72 64 20 45 78 63 68 61 6E 67 65 20 48 61 6E 64 6C 65 64 21),
00004293                         STR: 'winner: %d(%d) loser %d' (17 00 00 00 77 69 6E 6E 65 72 3A 20 25 64 28 25 64 29 20 6C 6F 73 65 72 20 25 64)
                             )
                         names:
000042AF                     TUPLE: (
000042B4                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
000042C1                         STR: 'tacticalValue' (0D 00 00 00 74 61 63 74 69 63 61 6C 56 61 6C 75 65),
000042D3                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
000042DE                         STR: 'attacker_level' (0E 00 00 00 61 74 74 61 63 6B 65 72 5F 6C 65 76 65 6C),
000042F1                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
000042FE                         STR: 'defender_level' (0E 00 00 00 64 65 66 65 6E 64 65 72 5F 6C 65 76 65 6C),
00004311                         STR: 'getCTandDTotals' (0F 00 00 00 67 65 74 43 54 61 6E 64 44 54 6F 74 61 6C 73),
00004325                         STR: 'attackerCT_total' (10 00 00 00 61 74 74 61 63 6B 65 72 43 54 5F 74 6F 74 61 6C),
0000433A                         STR: 'attackerD_total' (0F 00 00 00 61 74 74 61 63 6B 65 72 44 5F 74 6F 74 61 6C),
0000434E                         STR: 'attackersAdvantage' (12 00 00 00 61 74 74 61 63 6B 65 72 73 41 64 76 61 6E 74 61 67 65),
00004365                         STR: 'attackerHits' (0C 00 00 00 61 74 74 61 63 6B 65 72 48 69 74 73),
00004376                         STR: 'defenderCT_total' (10 00 00 00 64 65 66 65 6E 64 65 72 43 54 5F 74 6F 74 61 6C),
0000438B                         STR: 'defenderD_total' (0F 00 00 00 64 65 66 65 6E 64 65 72 44 5F 74 6F 74 61 6C),
0000439F                         STR: 'defendersAdvantage' (12 00 00 00 64 65 66 65 6E 64 65 72 73 41 64 76 61 6E 74 61 67 65),
000043B6                         STR: 'defenderHits' (0C 00 00 00 64 65 66 65 6E 64 65 72 48 69 74 73),
000043C7                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
000043D6                         STR: 'SendClientCombatData' (14 00 00 00 53 65 6E 64 43 6C 69 65 6E 74 43 6F 6D 62 61 74 44 61 74 61),
000043EF                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
000043FD                         STR: 'clientSystemMessage2' (14 00 00 00 63 6C 69 65 6E 74 53 79 73 74 65 6D 4D 65 73 73 61 67 65 32),
00004416                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
00004422                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00004430                         STR: 'Chat' (04 00 00 00 43 68 61 74),
00004439                         STR: 'CT_SYS_DEBUG' (0C 00 00 00 43 54 5F 53 59 53 5F 44 45 42 55 47),
0000444A                         STR: 'isAttemptingWithdraw' (14 00 00 00 69 73 41 74 74 65 6D 70 74 69 6E 67 57 69 74 68 64 72 61 77),
00004463                         STR: 'CU' (02 00 00 00 43 55),
0000446A                         STR: 'isEscapeAbility' (0F 00 00 00 69 73 45 73 63 61 70 65 41 62 69 6C 69 74 79),
0000447E                         STR: 'requestedSpecialMove' (14 00 00 00 72 65 71 75 65 73 74 65 64 53 70 65 63 69 61 6C 4D 6F 76 65),
00004497                         STR: 'outputCombatDebugMessageAll' (1B 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65 41 6C 6C),
000044B7                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
000044C1                         STR: 'switchAttackerDefender' (16 00 00 00 73 77 69 74 63 68 41 74 74 61 63 6B 65 72 44 65 66 65 6E 64 65 72),
000044DC                         STR: 'true_attacker' (0D 00 00 00 74 72 75 65 5F 61 74 74 61 63 6B 65 72),
000044EE                         STR: 'true_defender' (0D 00 00 00 74 72 75 65 5F 64 65 66 65 6E 64 65 72),
00004500                         STR: 'bothHit' (07 00 00 00 62 6F 74 68 48 69 74),
0000450C                         STR: 'isSpecialMove' (0D 00 00 00 69 73 53 70 65 63 69 61 6C 4D 6F 76 65),
0000451E                         STR: 'aUsesSM' (07 00 00 00 61 55 73 65 73 53 4D),
0000452A                         STR: 'dUsesSM' (07 00 00 00 64 55 73 65 73 53 4D),
00004536                         STR: 'bothUseSM' (09 00 00 00 62 6F 74 68 55 73 65 53 4D),
00004544                         STR: 'tempAHit' (08 00 00 00 74 65 6D 70 41 48 69 74),
00004551                         STR: 'tempAAdvan' (0A 00 00 00 74 65 6D 70 41 41 64 76 61 6E),
00004560                         STR: 'tempACT' (07 00 00 00 74 65 6D 70 41 43 54),
0000456C                         STR: 'tempAD' (06 00 00 00 74 65 6D 70 41 44),
00004577                         STR: 'flipAtkDef' (0A 00 00 00 66 6C 69 70 41 74 6B 44 65 66),
00004586                         STR: 'handleSpecialMove' (11 00 00 00 68 61 6E 64 6C 65 53 70 65 63 69 61 6C 4D 6F 76 65),
0000459C                         STR: 'opportunityAttack' (11 00 00 00 6F 70 70 6F 72 74 75 6E 69 74 79 41 74 74 61 63 6B),
000045B2                         STR: 'handleOppertunityAttack' (17 00 00 00 68 61 6E 64 6C 65 4F 70 70 65 72 74 75 6E 69 74 79 41 74 74 61 63 6B),
000045CE                         STR: 'tacticalSetting' (0F 00 00 00 74 61 63 74 69 63 61 6C 53 65 74 74 69 6E 67),
000045E2                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
000045ED                         STR: 'BLOCK' (05 00 00 00 42 4C 4F 43 4B),
000045F7                         STR: 'handleBlock' (0B 00 00 00 68 61 6E 64 6C 65 42 6C 6F 63 6B),
00004607                         STR: 'handleStandardExchange' (16 00 00 00 68 61 6E 64 6C 65 53 74 61 6E 64 61 72 64 45 78 63 68 61 6E 67 65),
00004622                         STR: 'None' (04 00 00 00 4E 6F 6E 65),
0000462B                         STR: 'winner' (06 00 00 00 77 69 6E 6E 65 72),
00004636                         STR: 'loser' (05 00 00 00 6C 6F 73 65 72),
00004640                         STR: 'winnerSlot' (0A 00 00 00 77 69 6E 6E 65 72 53 6C 6F 74),
0000464F                         STR: 'slot' (04 00 00 00 73 6C 6F 74),
00004658                         STR: 'attackerValue' (0D 00 00 00 61 74 74 61 63 6B 65 72 56 61 6C 75 65),
0000466A                         STR: 'defenderValue' (0D 00 00 00 64 65 66 65 6E 64 65 72 56 61 6C 75 65),
0000467C                         STR: 'outcomeFlag' (0B 00 00 00 6F 75 74 63 6F 6D 65 46 6C 61 67),
0000468C                         STR: 'SPECIAL_MOVE' (0C 00 00 00 53 50 45 43 49 41 4C 5F 4D 4F 56 45),
0000469D                         STR: 'winnerSpecialMoveUsed' (15 00 00 00 77 69 6E 6E 65 72 53 70 65 63 69 61 6C 4D 6F 76 65 55 73 65 64),
000046B7                         STR: 'loserSpecialMoveUsed' (14 00 00 00 6C 6F 73 65 72 53 70 65 63 69 61 6C 4D 6F 76 65 55 73 65 64)
                             )
                         varnames:
000046D0                     TUPLE: (
000046D5                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
000046E2                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
000046EF                         STR: 'failed_to_withdraw' (12 00 00 00 66 61 69 6C 65 64 5F 74 6F 5F 77 69 74 68 64 72 61 77),
00004706                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00004711                         STR: 'flipAtkDef' (0A 00 00 00 66 6C 69 70 41 74 6B 44 65 66),
00004720                         STR: 'winner' (06 00 00 00 77 69 6E 6E 65 72),
0000472B                         STR: 'aUsesSM' (07 00 00 00 61 55 73 65 73 53 4D),
00004737                         STR: 'attackersAdvantage' (12 00 00 00 61 74 74 61 63 6B 65 72 73 41 64 76 61 6E 74 61 67 65),
0000474E                         STR: 'tempAHit' (08 00 00 00 74 65 6D 70 41 48 69 74),
0000475B                         STR: 'attackerD_total' (0F 00 00 00 61 74 74 61 63 6B 65 72 44 5F 74 6F 74 61 6C),
0000476F                         STR: 'attackerCT_total' (10 00 00 00 61 74 74 61 63 6B 65 72 43 54 5F 74 6F 74 61 6C),
00004784                         STR: 'bothUseSM' (09 00 00 00 62 6F 74 68 55 73 65 53 4D),
00004792                         STR: 'tempAD' (06 00 00 00 74 65 6D 70 41 44),
0000479D                         STR: 'defendersAdvantage' (12 00 00 00 64 65 66 65 6E 64 65 72 73 41 64 76 61 6E 74 61 67 65),
000047B4                         STR: 'attackerHits' (0C 00 00 00 61 74 74 61 63 6B 65 72 48 69 74 73),
000047C5                         STR: 'defenderHits' (0C 00 00 00 64 65 66 65 6E 64 65 72 48 69 74 73),
000047D6                         STR: 'switchAttackerDefender' (16 00 00 00 73 77 69 74 63 68 41 74 74 61 63 6B 65 72 44 65 66 65 6E 64 65 72),
000047F1                         STR: 'defenderD_total' (0F 00 00 00 64 65 66 65 6E 64 65 72 44 5F 74 6F 74 61 6C),
00004805                         STR: 'true_defender' (0D 00 00 00 74 72 75 65 5F 64 65 66 65 6E 64 65 72),
00004817                         STR: 'bothHit' (07 00 00 00 62 6F 74 68 48 69 74),
00004823                         STR: 'dUsesSM' (07 00 00 00 64 55 73 65 73 53 4D),
0000482F                         STR: 'loser' (05 00 00 00 6C 6F 73 65 72),
00004839                         STR: 'tempACT' (07 00 00 00 74 65 6D 70 41 43 54),
00004845                         STR: 'defenderCT_total' (10 00 00 00 64 65 66 65 6E 64 65 72 43 54 5F 74 6F 74 61 6C),
0000485A                         STR: 'true_attacker' (0D 00 00 00 74 72 75 65 5F 61 74 74 61 63 6B 65 72),
0000486C                         STR: 'tempAAdvan' (0A 00 00 00 74 65 6D 70 41 41 64 76 61 6E)
                             )
                         freevars:
0000487B                     TUPLE: ()
                         cellvars:
00004880                     TUPLE: ()
                         filename:
00004885                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_resolution.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 72 65 73 6F 6C 75 74 69 6F 6E 2E 70 79)
                         name:
000048DD                     STR: 'determineResultForStandardCombat' (20 00 00 00 64 65 74 65 72 6D 69 6E 65 52 65 73 75 6C 74 46 6F 72 53 74 61 6E 64 61 72 64 43 6F 6D 62 61 74)
                         firslineno:
00004902                     LONG: 480L (E0 01 00 00)
                         lnotab:
00004906                     STR: "\x00\x02\x0c\x01\x0c\x02'\x02\x10\x01\x1c\x01 \x03\x1d\x01\x16\x01\x06\x01\n\x03\x1d\x01\x16\x01\x06\x01\n\x03\x06\x01\x06\x01\x06\x03\x0f\x01\n\x02\r\x01\x12\x01\x12\x01\r\x01\x07\x01\x1a\x01\x07\x01\x1a\x03\x0e\x01\x16\x02\r\x01\x16\x01\x0e\x03\x0e\x01\n\x02\r\x01\x16\x01\x06\x01\x06\x02\x06\x01\x06\x01\x06\x01\x06\x02\x06\x01\x06\x01\x06\x01\x06\x02\x06\x01\x06\x01\x06\x01\n\x03\x06\x03\x1a\x01\x16\x01\r\x01\n\x03\n\x01\x16\x01\x17\x04\x16\x01\x10\x01\x14\x03\x16\x01\x18\x03\x06\x01\x06\x01\x13\x01\x06\x01\x06\x01\t\x01\r\x02\x06\x01\x06\x01\t\x01\t\x04,\x02\x16\x01\x13\x01\r\x01\x13\x01" (A0 00 00 00 00 02 0C 01 0C 02 27 02 10 01 1C 01 20 03 1D 01 16 01 06 01 0A 03 1D 01 16 01 06 01 0A 03 06 01 06 01 06 03 0F 01 0A 02 0D 01 12 01 12 01 0D 01 07 01 1A 01 07 01 1A 03 0E 01 16 02 0D 01 16 01 0E 03 0E 01 0A 02 0D 01 16 01 06 01 06 02 06 01 06 01 06 01 06 02 06 01 06 01 06 01 06 02 06 01 06 01 06 01 0A 03 06 03 1A 01 16 01 0D 01 0A 03 0A 01 16 01 17 04 16 01 10 01 14 03 16 01 18 03 06 01 06 01 13 01 06 01 06 01 09 01 0D 02 06 01 06 01 09 01 09 04 2C 02 16 01 13 01 0D 01 13 01),
000049AB             CODE:
                         argcount:
000049AC                     LONG: 3L (03 00 00 00)
                         nlocals:
000049B0                     LONG: 5L (05 00 00 00)
                         stacksize:
000049B4                     LONG: 4L (04 00 00 00)
                         flags:
000049B8                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000049BC                     STR: 't\x00\x00i\x01\x00d\x01\x00d\x02\x00\x83\x02\x00\x01t\x00\x00i\x02\x00|\x00\x00\x83\x01\x00o-\x00\x01t\x00\x00i\x02\x00|\x01\x00\x83\x01\x00o\x1d\x00\x01|\x00\x00i\x05\x00d\x03\x00j\x02\x00o\r\x00\x01|\x01\x00i\x05\x00d\x03\x00j\x02\x00oz\x00\x01t\x00\x00i\x06\x00|\x00\x00i\x07\x00\x83\x01\x00t\x08\x00j\x02\x00o(\x00\x01t\t\x00i\n\x00i\x0b\x00|\x02\x00_\r\x00|\x00\x00i\x0e\x00|\x02\x00_\x0f\x00d\x04\x00|\x02\x00_\x10\x00n\x1c\x00\x01t\t\x00i\n\x00i\x11\x00|\x02\x00_\r\x00|\x00\x00i\x0e\x00|\x02\x00_\x0f\x00t\x00\x00i\x01\x00d\x05\x00d\x02\x00\x83\x02\x00\x01t\x08\x00t\x12\x00f\x02\x00Sn\x01\x00\x01t\x00\x00i\x02\x00|\x01\x00\x83\x01\x00t\x08\x00j\x03\x00o\x1e\x00\x01t\x00\x00i\x01\x00d\x06\x00d\x02\x00\x83\x02\x00\x01t\x12\x00t\x12\x00f\x02\x00Sn\x01\x00\x01|\x01\x00i\x05\x00d\x03\x00j\x03\x00o\x1e\x00\x01t\x00\x00i\x01\x00d\x07\x00d\x02\x00\x83\x02\x00\x01t\x12\x00t\x12\x00f\x02\x00Sn\x01\x00\x01|\x01\x00i\x13\x00d\x04\x00j\x00\x00o\x1e\x00\x01t\x00\x00i\x01\x00d\x08\x00d\x02\x00\x83\x02\x00\x01t\x08\x00t\x12\x00f\x02\x00Sn\x01\x00\x01t\x00\x00i\x01\x00d\t\x00d\x02\x00\x83\x02\x00\x01|\x00\x00i\x14\x00}\x04\x00|\x01\x00i\x14\x00}\x03\x00|\x03\x00|\x04\x00\x18|\x02\x00_\x17\x00|\x02\x00i\x17\x00d\x03\x00j\x04\x00p\r\x00\x01t\x18\x00i\x19\x00d\x03\x00j\x04\x00o\x88\x00\x01t\x00\x00i\x01\x00d\n\x00|\x04\x00|\x03\x00f\x02\x00\x16d\x02\x00\x83\x02\x00\x01|\x01\x00i\x0e\x00|\x02\x00_\x0f\x00t\t\x00i\n\x00i\x11\x00|\x02\x00_\r\x00t\x00\x00i\x06\x00|\x01\x00i\x07\x00\x83\x01\x00t\x08\x00j\x02\x00o,\x00\x01t\x00\x00i\x01\x00d\x0b\x00d\x0c\x00\x83\x02\x00\x01t\t\x00i\n\x00i\x0b\x00|\x02\x00_\r\x00d\x04\x00|\x02\x00_\x10\x00n\x01\x00\x01t\x08\x00t\x12\x00f\x02\x00Sn%\x00\x01t\x00\x00i\x01\x00d\r\x00|\x03\x00|\x04\x00f\x02\x00\x16d\x02\x00\x83\x02\x00\x01t\x08\x00t\x08\x00f\x02\x00Sd\x00\x00S' (59 02 00 00 74 00 00 69 01 00 64 01 00 64 02 00 83 02 00 01 74 00 00 69 02 00 7C 00 00 83 01 00 6F 2D 00 01 74 00 00 69 02 00 7C 01 00 83 01 00 6F 1D 00 01 7C 00 00 69 05 00 64 03 00 6A 02 00 6F 0D 00 01 7C 01 00 69 05 00 64 03 00 6A 02 00 6F 7A 00 01 74 00 00 69 06 00 7C 00 00 69 07 00 83 01 00 74 08 00 6A 02 00 6F 28 00 01 74 09 00 69 0A 00 69 0B 00 7C 02 00 5F 0D 00 7C 00 00 69 0E 00 7C 02 00 5F 0F 00 64 04 00 7C 02 00 5F 10 00 6E 1C 00 01 74 09 00 69 0A 00 69 11 00 7C 02 00 5F 0D 00 7C 00 00 69 0E 00 7C 02 00 5F 0F 00 74 00 00 69 01 00 64 05 00 64 02 00 83 02 00 01 74 08 00 74 12 00 66 02 00 53 6E 01 00 01 74 00 00 69 02 00 7C 01 00 83 01 00 74 08 00 6A 03 00 6F 1E 00 01 74 00 00 69 01 00 64 06 00 64 02 00 83 02 00 01 74 12 00 74 12 00 66 02 00 53 6E 01 00 01 7C 01 00 69 05 00 64 03 00 6A 03 00 6F 1E 00 01 74 00 00 69 01 00 64 07 00 64 02 00 83 02 00 01 74 12 00 74 12 00 66 02 00 53 6E 01 00 01 7C 01 00 69 13 00 64 04 00 6A 00 00 6F 1E 00 01 74 00 00 69 01 00 64 08 00 64 02 00 83 02 00 01 74 08 00 74 12 00 66 02 00 53 6E 01 00 01 74 00 00 69 01 00 64 09 00 64 02 00 83 02 00 01 7C 00 00 69 14 00 7D 04 00 7C 01 00 69 14 00 7D 03 00 7C 03 00 7C 04 00 18 7C 02 00 5F 17 00 7C 02 00 69 17 00 64 03 00 6A 04 00 70 0D 00 01 74 18 00 69 19 00 64 03 00 6A 04 00 6F 88 00 01 74 00 00 69 01 00 64 0A 00 7C 04 00 7C 03 00 66 02 00 16 64 02 00 83 02 00 01 7C 01 00 69 0E 00 7C 02 00 5F 0F 00 74 09 00 69 0A 00 69 11 00 7C 02 00 5F 0D 00 74 00 00 69 06 00 7C 01 00 69 07 00 83 01 00 74 08 00 6A 02 00 6F 2C 00 01 74 00 00 69 01 00 64 0B 00 64 0C 00 83 02 00 01 74 09 00 69 0A 00 69 0B 00 7C 02 00 5F 0D 00 64 04 00 7C 02 00 5F 10 00 6E 01 00 01 74 08 00 74 12 00 66 02 00 53 6E 25 00 01 74 00 00 69 01 00 64 0D 00 7C 03 00 7C 04 00 66 02 00 16 64 02 00 83 02 00 01 74 08 00 74 08 00 66 02 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CU'
                             00000003     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000006     64 - LOAD_CONST          'determineResultOfWithdrawalRequest: Redraw request check.'
                             00000009     64 - LOAD_CONST          13
                             0000000C     83 - CALL_FUNCTION       r0002
                             0000000F     01 - POP_TOP             
                             00000010     74 - LOAD_GLOBAL         'CU'
                             00000013     69 - LOAD_ATTR           'isPlayerWithdrawing'
                             00000016     7C - LOAD_FAST           'attacker'
                             00000019     83 - CALL_FUNCTION       r0001
                             0000001C     6F - JUMP_IF_FALSE       -> 0000004C
                             0000001F     01 - POP_TOP             
                             00000020     74 - LOAD_GLOBAL         'CU'
                             00000023     69 - LOAD_ATTR           'isPlayerWithdrawing'
                             00000026     7C - LOAD_FAST           'defender'
                             00000029     83 - CALL_FUNCTION       r0001
                             0000002C     6F - JUMP_IF_FALSE       -> 0000004C
                             0000002F     01 - POP_TOP             
                             00000030     7C - LOAD_FAST           'attacker'
                             00000033     69 - LOAD_ATTR           'proneState'
                             00000036     64 - LOAD_CONST          0
                             00000039     6A - COMPARE_OP          "=="
                             0000003C     6F - JUMP_IF_FALSE       -> 0000004C
                             0000003F     01 - POP_TOP             
                             00000040     7C - LOAD_FAST           'defender'
                             00000043     69 - LOAD_ATTR           'proneState'
                             00000046     64 - LOAD_CONST          0
                             00000049     6A - COMPARE_OP          "=="
                             0000004C     6F - JUMP_IF_FALSE       -> 000000C9
                             0000004F     01 - POP_TOP             
                             00000050     74 - LOAD_GLOBAL         'CU'
                             00000053     69 - LOAD_ATTR           'isEscapeAbility'
                             00000056     7C - LOAD_FAST           'attacker'
                             00000059     69 - LOAD_ATTR           'requestedSpecialMove'
                             0000005C     83 - CALL_FUNCTION       r0001
                             0000005F     74 - LOAD_GLOBAL         'True'
                             00000062     6A - COMPARE_OP          "=="
                             00000065     6F - JUMP_IF_FALSE       -> 00000090
                             00000068     01 - POP_TOP             
                             00000069     74 - LOAD_GLOBAL         'constants'
                             0000006C     69 - LOAD_ATTR           'combat'
                             0000006F     69 - LOAD_ATTR           'SPECIAL_MOVE'
                             00000072     7C - LOAD_FAST           'result'
                             00000075     5F - STORE_ATTR          'outcomeFlag'
                             00000078     7C - LOAD_FAST           'attacker'
                             0000007B     69 - LOAD_ATTR           'slot'
                             0000007E     7C - LOAD_FAST           'result'
                             00000081     5F - STORE_ATTR          'winnerSlot'
                             00000084     64 - LOAD_CONST          1
                             00000087     7C - LOAD_FAST           'result'
                             0000008A     5F - STORE_ATTR          'winnerSpecialMoveUsed'
                             0000008D     6E - JUMP_FORWARD        -> 000000AC
                             00000090     01 - POP_TOP             
                             00000091     74 - LOAD_GLOBAL         'constants'
                             00000094     69 - LOAD_ATTR           'combat'
                             00000097     69 - LOAD_ATTR           'WITHDRAW'
                             0000009A     7C - LOAD_FAST           'result'
                             0000009D     5F - STORE_ATTR          'outcomeFlag'
                             000000A0     7C - LOAD_FAST           'attacker'
                             000000A3     69 - LOAD_ATTR           'slot'
                             000000A6     7C - LOAD_FAST           'result'
                             000000A9     5F - STORE_ATTR          'winnerSlot'
                             000000AC     74 - LOAD_GLOBAL         'CU'
                             000000AF     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000B2     64 - LOAD_CONST          'uncontested withdraw successful'
                             000000B5     64 - LOAD_CONST          13
                             000000B8     83 - CALL_FUNCTION       r0002
                             000000BB     01 - POP_TOP             
                             000000BC     74 - LOAD_GLOBAL         'True'
                             000000BF     74 - LOAD_GLOBAL         'False'
                             000000C2     66 - BUILD_TUPLE         r0002
                             000000C5     53 - RETURN_VALUE        
                             000000C6     6E - JUMP_FORWARD        -> 000000CA
                             000000C9     01 - POP_TOP             
                             000000CA     74 - LOAD_GLOBAL         'CU'
                             000000CD     69 - LOAD_ATTR           'isPlayerWithdrawing'
                             000000D0     7C - LOAD_FAST           'defender'
                             000000D3     83 - CALL_FUNCTION       r0001
                             000000D6     74 - LOAD_GLOBAL         'True'
                             000000D9     6A - COMPARE_OP          "!="
                             000000DC     6F - JUMP_IF_FALSE       -> 000000FD
                             000000DF     01 - POP_TOP             
                             000000E0     74 - LOAD_GLOBAL         'CU'
                             000000E3     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000E6     64 - LOAD_CONST          'determineResultOfWithdrawalRequest: No withdraw request from defender.'
                             000000E9     64 - LOAD_CONST          13
                             000000EC     83 - CALL_FUNCTION       r0002
                             000000EF     01 - POP_TOP             
                             000000F0     74 - LOAD_GLOBAL         'False'
                             000000F3     74 - LOAD_GLOBAL         'False'
                             000000F6     66 - BUILD_TUPLE         r0002
                             000000F9     53 - RETURN_VALUE        
                             000000FA     6E - JUMP_FORWARD        -> 000000FE
                             000000FD     01 - POP_TOP             
                             000000FE     7C - LOAD_FAST           'defender'
                             00000101     69 - LOAD_ATTR           'proneState'
                             00000104     64 - LOAD_CONST          0
                             00000107     6A - COMPARE_OP          "!="
                             0000010A     6F - JUMP_IF_FALSE       -> 0000012B
                             0000010D     01 - POP_TOP             
                             0000010E     74 - LOAD_GLOBAL         'CU'
                             00000111     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000114     64 - LOAD_CONST          'player attempting to withdraw while prone'
                             00000117     64 - LOAD_CONST          13
                             0000011A     83 - CALL_FUNCTION       r0002
                             0000011D     01 - POP_TOP             
                             0000011E     74 - LOAD_GLOBAL         'False'
                             00000121     74 - LOAD_GLOBAL         'False'
                             00000124     66 - BUILD_TUPLE         r0002
                             00000127     53 - RETURN_VALUE        
                             00000128     6E - JUMP_FORWARD        -> 0000012C
                             0000012B     01 - POP_TOP             
                             0000012C     7C - LOAD_FAST           'defender'
                             0000012F     69 - LOAD_ATTR           'opponentCount'
                             00000132     64 - LOAD_CONST          1
                             00000135     6A - COMPARE_OP          "<"
                             00000138     6F - JUMP_IF_FALSE       -> 00000159
                             0000013B     01 - POP_TOP             
                             0000013C     74 - LOAD_GLOBAL         'CU'
                             0000013F     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000142     64 - LOAD_CONST          'determineResultOfWithdrawalRequest: Noone targeting defender.'
                             00000145     64 - LOAD_CONST          13
                             00000148     83 - CALL_FUNCTION       r0002
                             0000014B     01 - POP_TOP             
                             0000014C     74 - LOAD_GLOBAL         'True'
                             0000014F     74 - LOAD_GLOBAL         'False'
                             00000152     66 - BUILD_TUPLE         r0002
                             00000155     53 - RETURN_VALUE        
                             00000156     6E - JUMP_FORWARD        -> 0000015A
                             00000159     01 - POP_TOP             
                             0000015A     74 - LOAD_GLOBAL         'CU'
                             0000015D     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000160     64 - LOAD_CONST          'determining withdraw result'
                             00000163     64 - LOAD_CONST          13
                             00000166     83 - CALL_FUNCTION       r0002
                             00000169     01 - POP_TOP             
                             0000016A     7C - LOAD_FAST           'attacker'
                             0000016D     69 - LOAD_ATTR           'tacticalValue'
                             00000170     7D - STORE_FAST          'attacker_total'
                             00000173     7C - LOAD_FAST           'defender'
                             00000176     69 - LOAD_ATTR           'tacticalValue'
                             00000179     7D - STORE_FAST          'defender_total'
                             0000017C     7C - LOAD_FAST           'defender_total'
                             0000017F     7C - LOAD_FAST           'attacker_total'
                             00000182     18 - BINARY_SUBTRACT     
                             00000183     7C - LOAD_FAST           'result'
                             00000186     5F - STORE_ATTR          'combatResult'
                             00000189     7C - LOAD_FAST           'result'
                             0000018C     69 - LOAD_ATTR           'combatResult'
                             0000018F     64 - LOAD_CONST          0
                             00000192     6A - COMPARE_OP          ">"
                             00000195     70 - JUMP_IF_TRUE        -> 000001A5
                             00000198     01 - POP_TOP             
                             00000199     74 - LOAD_GLOBAL         'consolevar'
                             0000019C     69 - LOAD_ATTR           'CombatFreeWithdraw'
                             0000019F     64 - LOAD_CONST          0
                             000001A2     6A - COMPARE_OP          ">"
                             000001A5     6F - JUMP_IF_FALSE       -> 00000230
                             000001A8     01 - POP_TOP             
                             000001A9     74 - LOAD_GLOBAL         'CU'
                             000001AC     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000001AF     64 - LOAD_CONST          'Successfuly withdrew: %d <= %d'
                             000001B2     7C - LOAD_FAST           'attacker_total'
                             000001B5     7C - LOAD_FAST           'defender_total'
                             000001B8     66 - BUILD_TUPLE         r0002
                             000001BB     16 - BINARY_MODULO       
                             000001BC     64 - LOAD_CONST          13
                             000001BF     83 - CALL_FUNCTION       r0002
                             000001C2     01 - POP_TOP             
                             000001C3     7C - LOAD_FAST           'defender'
                             000001C6     69 - LOAD_ATTR           'slot'
                             000001C9     7C - LOAD_FAST           'result'
                             000001CC     5F - STORE_ATTR          'winnerSlot'
                             000001CF     74 - LOAD_GLOBAL         'constants'
                             000001D2     69 - LOAD_ATTR           'combat'
                             000001D5     69 - LOAD_ATTR           'WITHDRAW'
                             000001D8     7C - LOAD_FAST           'result'
                             000001DB     5F - STORE_ATTR          'outcomeFlag'
                             000001DE     74 - LOAD_GLOBAL         'CU'
                             000001E1     69 - LOAD_ATTR           'isEscapeAbility'
                             000001E4     7C - LOAD_FAST           'defender'
                             000001E7     69 - LOAD_ATTR           'requestedSpecialMove'
                             000001EA     83 - CALL_FUNCTION       r0001
                             000001ED     74 - LOAD_GLOBAL         'True'
                             000001F0     6A - COMPARE_OP          "=="
                             000001F3     6F - JUMP_IF_FALSE       -> 00000222
                             000001F6     01 - POP_TOP             
                             000001F7     74 - LOAD_GLOBAL         'CU'
                             000001FA     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000001FD     64 - LOAD_CONST          'Escape performed'
                             00000200     64 - LOAD_CONST          3
                             00000203     83 - CALL_FUNCTION       r0002
                             00000206     01 - POP_TOP             
                             00000207     74 - LOAD_GLOBAL         'constants'
                             0000020A     69 - LOAD_ATTR           'combat'
                             0000020D     69 - LOAD_ATTR           'SPECIAL_MOVE'
                             00000210     7C - LOAD_FAST           'result'
                             00000213     5F - STORE_ATTR          'outcomeFlag'
                             00000216     64 - LOAD_CONST          1
                             00000219     7C - LOAD_FAST           'result'
                             0000021C     5F - STORE_ATTR          'winnerSpecialMoveUsed'
                             0000021F     6E - JUMP_FORWARD        -> 00000223
                             00000222     01 - POP_TOP             
                             00000223     74 - LOAD_GLOBAL         'True'
                             00000226     74 - LOAD_GLOBAL         'False'
                             00000229     66 - BUILD_TUPLE         r0002
                             0000022C     53 - RETURN_VALUE        
                             0000022D     6E - JUMP_FORWARD        -> 00000255
                             00000230     01 - POP_TOP             
                             00000231     74 - LOAD_GLOBAL         'CU'
                             00000234     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000237     64 - LOAD_CONST          'Unsuccessfuly withdrew: %d <= %d'
                             0000023A     7C - LOAD_FAST           'defender_total'
                             0000023D     7C - LOAD_FAST           'attacker_total'
                             00000240     66 - BUILD_TUPLE         r0002
                             00000243     16 - BINARY_MODULO       
                             00000244     64 - LOAD_CONST          13
                             00000247     83 - CALL_FUNCTION       r0002
                             0000024A     01 - POP_TOP             
                             0000024B     74 - LOAD_GLOBAL         'True'
                             0000024E     74 - LOAD_GLOBAL         'True'
                             00000251     66 - BUILD_TUPLE         r0002
                             00000254     53 - RETURN_VALUE        
                             00000255     64 - LOAD_CONST          None
                             00000258     53 - RETURN_VALUE        
                         consts:
00004C1A                     TUPLE: (
00004C1F                         None (4E),
00004C20                         STR: 'determineResultOfWithdrawalRequest: Redraw request check.' (39 00 00 00 64 65 74 65 72 6D 69 6E 65 52 65 73 75 6C 74 4F 66 57 69 74 68 64 72 61 77 61 6C 52 65 71 75 65 73 74 3A 20 52 65 64 72 61 77 20 72 65 71 75 65 73 74 20 63 68 65 63 6B 2E),
00004C5E                         INT: 13 (0D 00 00 00),
00004C63                         INT: 0 (00 00 00 00),
00004C68                         INT: 1 (01 00 00 00),
00004C6D                         STR: 'uncontested withdraw successful' (1F 00 00 00 75 6E 63 6F 6E 74 65 73 74 65 64 20 77 69 74 68 64 72 61 77 20 73 75 63 63 65 73 73 66 75 6C),
00004C91                         STR: 'determineResultOfWithdrawalRequest: No withdraw request from defender.' (46 00 00 00 64 65 74 65 72 6D 69 6E 65 52 65 73 75 6C 74 4F 66 57 69 74 68 64 72 61 77 61 6C 52 65 71 75 65 73 74 3A 20 4E 6F 20 77 69 74 68 64 72 61 77 20 72 65 71 75 65 73 74 20 66 72 6F 6D 20 64 65 66 65 6E 64 65 72 2E),
00004CDC                         STR: 'player attempting to withdraw while prone' (29 00 00 00 70 6C 61 79 65 72 20 61 74 74 65 6D 70 74 69 6E 67 20 74 6F 20 77 69 74 68 64 72 61 77 20 77 68 69 6C 65 20 70 72 6F 6E 65),
00004D0A                         STR: 'determineResultOfWithdrawalRequest: Noone targeting defender.' (3D 00 00 00 64 65 74 65 72 6D 69 6E 65 52 65 73 75 6C 74 4F 66 57 69 74 68 64 72 61 77 61 6C 52 65 71 75 65 73 74 3A 20 4E 6F 6F 6E 65 20 74 61 72 67 65 74 69 6E 67 20 64 65 66 65 6E 64 65 72 2E),
00004D4C                         STR: 'determining withdraw result' (1B 00 00 00 64 65 74 65 72 6D 69 6E 69 6E 67 20 77 69 74 68 64 72 61 77 20 72 65 73 75 6C 74),
00004D6C                         STR: 'Successfuly withdrew: %d <= %d' (1E 00 00 00 53 75 63 63 65 73 73 66 75 6C 79 20 77 69 74 68 64 72 65 77 3A 20 25 64 20 3C 3D 20 25 64),
00004D8F                         STR: 'Escape performed' (10 00 00 00 45 73 63 61 70 65 20 70 65 72 66 6F 72 6D 65 64),
00004DA4                         INT: 3 (03 00 00 00),
00004DA9                         STR: 'Unsuccessfuly withdrew: %d <= %d' (20 00 00 00 55 6E 73 75 63 63 65 73 73 66 75 6C 79 20 77 69 74 68 64 72 65 77 3A 20 25 64 20 3C 3D 20 25 64)
                             )
                         names:
00004DCE                     TUPLE: (
00004DD3                         STR: 'CU' (02 00 00 00 43 55),
00004DDA                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
00004DF7                         STR: 'isPlayerWithdrawing' (13 00 00 00 69 73 50 6C 61 79 65 72 57 69 74 68 64 72 61 77 69 6E 67),
00004E0F                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
00004E1C                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
00004E29                         STR: 'proneState' (0A 00 00 00 70 72 6F 6E 65 53 74 61 74 65),
00004E38                         STR: 'isEscapeAbility' (0F 00 00 00 69 73 45 73 63 61 70 65 41 62 69 6C 69 74 79),
00004E4C                         STR: 'requestedSpecialMove' (14 00 00 00 72 65 71 75 65 73 74 65 64 53 70 65 63 69 61 6C 4D 6F 76 65),
00004E65                         STR: 'True' (04 00 00 00 54 72 75 65),
00004E6E                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00004E7C                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
00004E87                         STR: 'SPECIAL_MOVE' (0C 00 00 00 53 50 45 43 49 41 4C 5F 4D 4F 56 45),
00004E98                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00004EA3                         STR: 'outcomeFlag' (0B 00 00 00 6F 75 74 63 6F 6D 65 46 6C 61 67),
00004EB3                         STR: 'slot' (04 00 00 00 73 6C 6F 74),
00004EBC                         STR: 'winnerSlot' (0A 00 00 00 77 69 6E 6E 65 72 53 6C 6F 74),
00004ECB                         STR: 'winnerSpecialMoveUsed' (15 00 00 00 77 69 6E 6E 65 72 53 70 65 63 69 61 6C 4D 6F 76 65 55 73 65 64),
00004EE5                         STR: 'WITHDRAW' (08 00 00 00 57 49 54 48 44 52 41 57),
00004EF2                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
00004EFC                         STR: 'opponentCount' (0D 00 00 00 6F 70 70 6F 6E 65 6E 74 43 6F 75 6E 74),
00004F0E                         STR: 'tacticalValue' (0D 00 00 00 74 61 63 74 69 63 61 6C 56 61 6C 75 65),
00004F20                         STR: 'attacker_total' (0E 00 00 00 61 74 74 61 63 6B 65 72 5F 74 6F 74 61 6C),
00004F33                         STR: 'defender_total' (0E 00 00 00 64 65 66 65 6E 64 65 72 5F 74 6F 74 61 6C),
00004F46                         STR: 'combatResult' (0C 00 00 00 63 6F 6D 62 61 74 52 65 73 75 6C 74),
00004F57                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
00004F66                         STR: 'CombatFreeWithdraw' (12 00 00 00 43 6F 6D 62 61 74 46 72 65 65 57 69 74 68 64 72 61 77)
                             )
                         varnames:
00004F7D                     TUPLE: (
00004F82                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
00004F8F                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
00004F9C                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00004FA7                         STR: 'defender_total' (0E 00 00 00 64 65 66 65 6E 64 65 72 5F 74 6F 74 61 6C),
00004FBA                         STR: 'attacker_total' (0E 00 00 00 61 74 74 61 63 6B 65 72 5F 74 6F 74 61 6C)
                             )
                         freevars:
00004FCD                     TUPLE: ()
                         cellvars:
00004FD2                     TUPLE: ()
                         filename:
00004FD7                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_resolution.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 72 65 73 6F 6C 75 74 69 6F 6E 2E 70 79)
                         name:
0000502F                     STR: 'determineResultOfWithdrawalRequest' (22 00 00 00 64 65 74 65 72 6D 69 6E 65 52 65 73 75 6C 74 4F 66 57 69 74 68 64 72 61 77 61 6C 52 65 71 75 65 73 74)
                         firslineno:
00005056                     LONG: 603L (5B 02 00 00)
                         lnotab:
0000505A                     STR: '\x00\x02\x10\x03@\x01\x19\x01\x0f\x01\x0c\x01\r\x02\x0f\x01\x0c\x02\x10\x01\x0e\x03\x16\x01\x10\x01\x0e\x03\x10\x01\x10\x01\x0e\x03\x10\x01\x10\x01\x0e\x02\x10\x03\t\x01\t\x01\r\x03 \x01\x1a\x01\x0c\x01\x0f\x01\x19\x01\x10\x01\x0f\x01\r\x02\x0e\x04\x1a\x01' (44 00 00 00 00 02 10 03 40 01 19 01 0F 01 0C 01 0D 02 0F 01 0C 02 10 01 0E 03 16 01 10 01 0E 03 10 01 10 01 0E 03 10 01 10 01 0E 02 10 03 09 01 09 01 0D 03 20 01 1A 01 0C 01 0F 01 19 01 10 01 0F 01 0D 02 0E 04 1A 01)
                 )
             names:
000050A3         TUPLE: (
000050A8             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
000050B3             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
000050C1             STR: 'obj' (03 00 00 00 6F 62 6A),
000050C9             STR: 'combat_defines' (0E 00 00 00 63 6F 6D 62 61 74 5F 64 65 66 69 6E 65 73),
000050DC             STR: 'CD' (02 00 00 00 43 44),
000050E3             STR: 'math' (04 00 00 00 6D 61 74 68),
000050EC             STR: 'combat_utility' (0E 00 00 00 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79),
000050FF             STR: 'CU' (02 00 00 00 43 55),
00005106             STR: 'combat_modifiers' (10 00 00 00 63 6F 6D 62 61 74 5F 6D 6F 64 69 66 69 65 72 73),
0000511B             STR: 'Mods' (04 00 00 00 4D 6F 64 73),
00005124             STR: 'combat_calculations' (13 00 00 00 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73),
0000513C             STR: 'CC' (02 00 00 00 43 43),
00005143             STR: 'generateVulnerabilities' (17 00 00 00 67 65 6E 65 72 61 74 65 56 75 6C 6E 65 72 61 62 69 6C 69 74 69 65 73),
0000515F             STR: 'generateExploits' (10 00 00 00 67 65 6E 65 72 61 74 65 45 78 70 6C 6F 69 74 73),
00005174             STR: 'generateExploitsForPlayers' (1A 00 00 00 67 65 6E 65 72 61 74 65 45 78 70 6C 6F 69 74 73 46 6F 72 50 6C 61 79 65 72 73),
00005193             STR: 'isAbilityMartialArt' (13 00 00 00 69 73 41 62 69 6C 69 74 79 4D 61 72 74 69 61 6C 41 72 74),
000051AB             STR: 'calcDamageForLoser' (12 00 00 00 63 61 6C 63 44 61 6D 61 67 65 46 6F 72 4C 6F 73 65 72),
000051C2             STR: 'calculateDamage' (0F 00 00 00 63 61 6C 63 75 6C 61 74 65 44 61 6D 61 67 65),
000051D6             STR: 'determineAttacker' (11 00 00 00 64 65 74 65 72 6D 69 6E 65 41 74 74 61 63 6B 65 72),
000051EC             STR: 'handleSpecialMove' (11 00 00 00 68 61 6E 64 6C 65 53 70 65 63 69 61 6C 4D 6F 76 65),
00005202             STR: 'handleOppertunityAttack' (17 00 00 00 68 61 6E 64 6C 65 4F 70 70 65 72 74 75 6E 69 74 79 41 74 74 61 63 6B),
0000521E             STR: 'handleStandardExchange' (16 00 00 00 68 61 6E 64 6C 65 53 74 61 6E 64 61 72 64 45 78 63 68 61 6E 67 65),
00005239             STR: 'handleBlock' (0B 00 00 00 68 61 6E 64 6C 65 42 6C 6F 63 6B),
00005249             STR: 'GetCorrectDefenseBonus' (16 00 00 00 47 65 74 43 6F 72 72 65 63 74 44 65 66 65 6E 73 65 42 6F 6E 75 73),
00005264             STR: 'getCorrectDTTotals' (12 00 00 00 67 65 74 43 6F 72 72 65 63 74 44 54 54 6F 74 61 6C 73),
0000527B             STR: 'getCTandDTotals' (0F 00 00 00 67 65 74 43 54 61 6E 64 44 54 6F 74 61 6C 73),
0000528F             STR: 'FlipAtkDef' (0A 00 00 00 46 6C 69 70 41 74 6B 44 65 66),
0000529E             STR: 'determineResultForStandardCombat' (20 00 00 00 64 65 74 65 72 6D 69 6E 65 52 65 73 75 6C 74 46 6F 72 53 74 61 6E 64 61 72 64 43 6F 6D 62 61 74),
000052C3             STR: 'determineResultOfWithdrawalRequest' (22 00 00 00 64 65 74 65 72 6D 69 6E 65 52 65 73 75 6C 74 4F 66 57 69 74 68 64 72 61 77 61 6C 52 65 71 75 65 73 74)
                 )
             varnames:
000052EA         TUPLE: (
000052EF             STR: 'getCorrectDTTotals' (12 00 00 00 67 65 74 43 6F 72 72 65 63 74 44 54 54 6F 74 61 6C 73),
00005306             STR: 'handleBlock' (0B 00 00 00 68 61 6E 64 6C 65 42 6C 6F 63 6B),
00005316             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00005321             STR: 'handleStandardExchange' (16 00 00 00 68 61 6E 64 6C 65 53 74 61 6E 64 61 72 64 45 78 63 68 61 6E 67 65),
0000533C             STR: 'handleSpecialMove' (11 00 00 00 68 61 6E 64 6C 65 53 70 65 63 69 61 6C 4D 6F 76 65),
00005352             STR: 'getCTandDTotals' (0F 00 00 00 67 65 74 43 54 61 6E 64 44 54 6F 74 61 6C 73),
00005366             STR: 'calcDamageForLoser' (12 00 00 00 63 61 6C 63 44 61 6D 61 67 65 46 6F 72 4C 6F 73 65 72),
0000537D             STR: 'determineResultForStandardCombat' (20 00 00 00 64 65 74 65 72 6D 69 6E 65 52 65 73 75 6C 74 46 6F 72 53 74 61 6E 64 61 72 64 43 6F 6D 62 61 74),
000053A2             STR: 'math' (04 00 00 00 6D 61 74 68),
000053AB             STR: 'generateExploitsForPlayers' (1A 00 00 00 67 65 6E 65 72 61 74 65 45 78 70 6C 6F 69 74 73 46 6F 72 50 6C 61 79 65 72 73),
000053CA             STR: 'Mods' (04 00 00 00 4D 6F 64 73),
000053D3             STR: 'handleOppertunityAttack' (17 00 00 00 68 61 6E 64 6C 65 4F 70 70 65 72 74 75 6E 69 74 79 41 74 74 61 63 6B),
000053EF             STR: 'determineResultOfWithdrawalRequest' (22 00 00 00 64 65 74 65 72 6D 69 6E 65 52 65 73 75 6C 74 4F 66 57 69 74 68 64 72 61 77 61 6C 52 65 71 75 65 73 74),
00005416             STR: 'CC' (02 00 00 00 43 43),
0000541D             STR: 'CD' (02 00 00 00 43 44),
00005424             STR: 'isAbilityMartialArt' (13 00 00 00 69 73 41 62 69 6C 69 74 79 4D 61 72 74 69 61 6C 41 72 74),
0000543C             STR: 'GetCorrectDefenseBonus' (16 00 00 00 47 65 74 43 6F 72 72 65 63 74 44 65 66 65 6E 73 65 42 6F 6E 75 73),
00005457             STR: 'CU' (02 00 00 00 43 55),
0000545E             STR: 'FlipAtkDef' (0A 00 00 00 46 6C 69 70 41 74 6B 44 65 66),
0000546D             STR: 'determineAttacker' (11 00 00 00 64 65 74 65 72 6D 69 6E 65 41 74 74 61 63 6B 65 72),
00005483             STR: 'obj' (03 00 00 00 6F 62 6A),
0000548B             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00005499             STR: 'generateExploits' (10 00 00 00 67 65 6E 65 72 61 74 65 45 78 70 6C 6F 69 74 73),
000054AE             STR: 'calculateDamage' (0F 00 00 00 63 61 6C 63 75 6C 61 74 65 44 61 6D 61 67 65),
000054C2             STR: 'generateVulnerabilities' (17 00 00 00 67 65 6E 65 72 61 74 65 56 75 6C 6E 65 72 61 62 69 6C 69 74 69 65 73)
                 )
             freevars:
000054DE         TUPLE: ()
             cellvars:
000054E3         TUPLE: ()
             filename:
000054E8         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_resolution.py' (53 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 72 65 73 6F 6C 75 74 69 6F 6E 2E 70 79)
             name:
00005540         STR: '?' (01 00 00 00 3F)
             firslineno:
00005546         LONG: 1L (01 00 00 00)
             lnotab:
0000554A         STR: "\t\x01\t\x01\t\x01\t\x01\t\x01\t\x01\t\x01\t\x05\tA\t\x0e\t\x0c\t\x0b\t*\t\x0c\t@\t\x07\t\r\tC\t'\t\x16\t2\t%\t\x0c\t{" (30 00 00 00 09 01 09 01 09 01 09 01 09 01 09 01 09 01 09 05 09 41 09 0E 09 0C 09 0B 09 2A 09 0C 09 40 09 07 09 0D 09 43 09 27 09 16 09 32 09 25 09 0C 09 7B)

