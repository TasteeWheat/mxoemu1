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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00Z\x02\x00d\x00\x00k\x03\x00Z\x04\x00d\x00\x00k\x05\x00Z\x05\x00d\x00\x00k\x06\x00Z\x07\x00d\x00\x00k\x08\x00Z\t\x00d\x00\x00k\n\x00Z\x0b\x00d\x00\x00k\x0c\x00Z\r\x00d\x00\x00k\x0e\x00Z\x0f\x00d\x01\x00\x84\x00\x00Z\x10\x00d\x02\x00\x84\x00\x00Z\x11\x00d\x03\x00\x84\x00\x00Z\x12\x00d\x00\x00S' (79 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 5A 02 00 64 00 00 6B 03 00 5A 04 00 64 00 00 6B 05 00 5A 05 00 64 00 00 6B 06 00 5A 07 00 64 00 00 6B 08 00 5A 09 00 64 00 00 6B 0A 00 5A 0B 00 64 00 00 6B 0C 00 5A 0D 00 64 00 00 6B 0E 00 5A 0F 00 64 01 00 84 00 00 5A 10 00 64 02 00 84 00 00 5A 11 00 64 03 00 84 00 00 5A 12 00 64 00 00 53)
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
                 00000039     6B - IMPORT_NAME         'combat_innerstrength'
                 0000003C     5A - STORE_NAME          'CI'
                 0000003F     64 - LOAD_CONST          None
                 00000042     6B - IMPORT_NAME         'combat_resolution'
                 00000045     5A - STORE_NAME          'CR'
                 00000048     64 - LOAD_CONST          None
                 0000004B     6B - IMPORT_NAME         'generic_free_attacks'
                 0000004E     5A - STORE_NAME          'GenFA'
                 00000051     64 - LOAD_CONST          None
                 00000054     6B - IMPORT_NAME         'combat_calculations'
                 00000057     5A - STORE_NAME          'CC'
                 0000005A     64 - LOAD_CONST          CODE('PerformWeaponFreeAttack')
                 0000005D     84 - MAKE_FUNCTION       r0000
                 00000060     5A - STORE_NAME          'PerformWeaponFreeAttack'
                 00000063     64 - LOAD_CONST          CODE('GetMeleeFreeAttackScript')
                 00000066     84 - MAKE_FUNCTION       r0000
                 00000069     5A - STORE_NAME          'GetMeleeFreeAttackScript'
                 0000006C     64 - LOAD_CONST          CODE('PerformMeleeFreeAttack')
                 0000006F     84 - MAKE_FUNCTION       r0000
                 00000072     5A - STORE_NAME          'PerformMeleeFreeAttack'
                 00000075     64 - LOAD_CONST          None
                 00000078     53 - RETURN_VALUE        
             consts:
00000097         TUPLE: (
0000009C             None (4E),
0000009D             CODE:
                         argcount:
0000009E                     LONG: 3L (03 00 00 00)
                         nlocals:
000000A2                     LONG: 11L (0B 00 00 00)
                         stacksize:
000000A6                     LONG: 10L (0A 00 00 00)
                         flags:
000000AA                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000000AE                     STR: "t\x00\x00i\x01\x00d\x01\x00d\x02\x00\x83\x02\x00\x01t\x02\x00}\n\x00|\x00\x00i\x05\x00}\x08\x00d\x03\x00|\x02\x00_\x08\x00d\x03\x00|\x02\x00_\t\x00|\x02\x00i\n\x00}\x03\x00|\x02\x00i\x0c\x00}\x06\x00t\x00\x00i\x01\x00d\x04\x00|\x03\x00|\x06\x00f\x02\x00\x16d\x02\x00\x83\x02\x00\x01|\x01\x00i\x0f\x00o\x10\x00\x01|\x03\x00|\x06\x00j\x04\x00}\x04\x00n\x07\x00\x01t\x11\x00}\x04\x00|\x04\x00o-\x01\x01t\x12\x00i\x13\x00|\x00\x00i\x14\x00|\x00\x00i\x15\x00|\x00\x00i\x16\x00|\x00\x00i\x17\x00|\x00\x00i\x18\x00|\x00\x00i\x19\x00|\x00\x00i\x1a\x00|\x00\x00i\x1b\x00d\x05\x00\x83\t\x00}\x05\x00t\x00\x00i\x01\x00d\x06\x00|\x05\x00\x16d\x02\x00\x83\x02\x00\x01t\x12\x00i\x1d\x00|\x00\x00i\x1e\x00|\x01\x00i\x1e\x00|\x01\x00i\x1f\x00|\x01\x00i \x00\x17|\x05\x00\x83\x04\x00}\x07\x00d\x07\x00|\x07\x00\x16}\t\x00t\x00\x00i\x01\x00|\t\x00d\x02\x00\x83\x02\x00\x01t#\x00|\x05\x00\x83\x01\x00|\x07\x00\x14|\x02\x00_$\x00|\x05\x00|\x02\x00i$\x00\x18|\x02\x00_%\x00t\x00\x00i\x01\x00d\x08\x00|\x02\x00i$\x00\x16d\x02\x00\x83\x02\x00\x01|\x02\x00i%\x00d\x03\x00j\x00\x00o$\x00\x01t\x00\x00i\x01\x00d\t\x00|\x02\x00i%\x00\x16d\x02\x00\x83\x02\x00\x01d\x05\x00|\x02\x00_%\x00n\x01\x00\x01t\x00\x00i\x01\x00d\n\x00|\x02\x00i%\x00\x16d\x02\x00\x83\x02\x00\x01t&\x00i'\x00i(\x00|\x02\x00_)\x00n\x19\x00\x01d\x03\x00|\x02\x00_%\x00t&\x00i'\x00i*\x00|\x02\x00_)\x00|\x08\x00t&\x00i'\x00i+\x00j\x02\x00o\n\x00\x01t,\x00}\n\x00n\x88\x00\x01|\x08\x00t&\x00i'\x00i-\x00j\x02\x00o\n\x00\x01t.\x00}\n\x00nk\x00\x01|\x08\x00t&\x00i'\x00i/\x00j\x02\x00o\n\x00\x01t0\x00}\n\x00nN\x00\x01|\x08\x00t&\x00i'\x00i1\x00j\x02\x00o\n\x00\x01t2\x00}\n\x00n1\x00\x01|\x08\x00t&\x00i'\x00i3\x00j\x02\x00o\n\x00\x01t4\x00}\n\x00n\x14\x00\x01t&\x00i'\x00i5\x00|\x02\x00_)\x00t\x11\x00S|\x02\x00i)\x00t&\x00i'\x00i(\x00j\x02\x00o#\x00\x01|\x00\x00i6\x00i7\x00i8\x00t9\x00|\n\x00|\x01\x00i:\x00t;\x00\x83\x04\x00\x01n \x00\x01|\x00\x00i6\x00i7\x00i8\x00t9\x00|\n\x00|\x01\x00i:\x00t<\x00\x83\x04\x00\x01t=\x00Sd\x00\x00S" (CD 02 00 00 74 00 00 69 01 00 64 01 00 64 02 00 83 02 00 01 74 02 00 7D 0A 00 7C 00 00 69 05 00 7D 08 00 64 03 00 7C 02 00 5F 08 00 64 03 00 7C 02 00 5F 09 00 7C 02 00 69 0A 00 7D 03 00 7C 02 00 69 0C 00 7D 06 00 74 00 00 69 01 00 64 04 00 7C 03 00 7C 06 00 66 02 00 16 64 02 00 83 02 00 01 7C 01 00 69 0F 00 6F 10 00 01 7C 03 00 7C 06 00 6A 04 00 7D 04 00 6E 07 00 01 74 11 00 7D 04 00 7C 04 00 6F 2D 01 01 74 12 00 69 13 00 7C 00 00 69 14 00 7C 00 00 69 15 00 7C 00 00 69 16 00 7C 00 00 69 17 00 7C 00 00 69 18 00 7C 00 00 69 19 00 7C 00 00 69 1A 00 7C 00 00 69 1B 00 64 05 00 83 09 00 7D 05 00 74 00 00 69 01 00 64 06 00 7C 05 00 16 64 02 00 83 02 00 01 74 12 00 69 1D 00 7C 00 00 69 1E 00 7C 01 00 69 1E 00 7C 01 00 69 1F 00 7C 01 00 69 20 00 17 7C 05 00 83 04 00 7D 07 00 64 07 00 7C 07 00 16 7D 09 00 74 00 00 69 01 00 7C 09 00 64 02 00 83 02 00 01 74 23 00 7C 05 00 83 01 00 7C 07 00 14 7C 02 00 5F 24 00 7C 05 00 7C 02 00 69 24 00 18 7C 02 00 5F 25 00 74 00 00 69 01 00 64 08 00 7C 02 00 69 24 00 16 64 02 00 83 02 00 01 7C 02 00 69 25 00 64 03 00 6A 00 00 6F 24 00 01 74 00 00 69 01 00 64 09 00 7C 02 00 69 25 00 16 64 02 00 83 02 00 01 64 05 00 7C 02 00 5F 25 00 6E 01 00 01 74 00 00 69 01 00 64 0A 00 7C 02 00 69 25 00 16 64 02 00 83 02 00 01 74 26 00 69 27 00 69 28 00 7C 02 00 5F 29 00 6E 19 00 01 64 03 00 7C 02 00 5F 25 00 74 26 00 69 27 00 69 2A 00 7C 02 00 5F 29 00 7C 08 00 74 26 00 69 27 00 69 2B 00 6A 02 00 6F 0A 00 01 74 2C 00 7D 0A 00 6E 88 00 01 7C 08 00 74 26 00 69 27 00 69 2D 00 6A 02 00 6F 0A 00 01 74 2E 00 7D 0A 00 6E 6B 00 01 7C 08 00 74 26 00 69 27 00 69 2F 00 6A 02 00 6F 0A 00 01 74 30 00 7D 0A 00 6E 4E 00 01 7C 08 00 74 26 00 69 27 00 69 31 00 6A 02 00 6F 0A 00 01 74 32 00 7D 0A 00 6E 31 00 01 7C 08 00 74 26 00 69 27 00 69 33 00 6A 02 00 6F 0A 00 01 74 34 00 7D 0A 00 6E 14 00 01 74 26 00 69 27 00 69 35 00 7C 02 00 5F 29 00 74 11 00 53 7C 02 00 69 29 00 74 26 00 69 27 00 69 28 00 6A 02 00 6F 23 00 01 7C 00 00 69 36 00 69 37 00 69 38 00 74 39 00 7C 0A 00 7C 01 00 69 3A 00 74 3B 00 83 04 00 01 6E 20 00 01 7C 00 00 69 36 00 69 37 00 69 38 00 74 39 00 7C 0A 00 7C 01 00 69 3A 00 74 3C 00 83 04 00 01 74 3D 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CU'
                             00000003     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000006     64 - LOAD_CONST          'weapon free attack func()'
                             00000009     64 - LOAD_CONST          2
                             0000000C     83 - CALL_FUNCTION       r0002
                             0000000F     01 - POP_TOP             
                             00000010     74 - LOAD_GLOBAL         'Action_Idle'
                             00000013     7D - STORE_FAST          'action'
                             00000016     7C - LOAD_FAST           'attacker'
                             00000019     69 - LOAD_ATTR           'itemType'
                             0000001C     7D - STORE_FAST          'item'
                             0000001F     64 - LOAD_CONST          0
                             00000022     7C - LOAD_FAST           'result'
                             00000025     5F - STORE_ATTR          'attackerMod'
                             00000028     64 - LOAD_CONST          0
                             0000002B     7C - LOAD_FAST           'result'
                             0000002E     5F - STORE_ATTR          'defenderMod'
                             00000031     7C - LOAD_FAST           'result'
                             00000034     69 - LOAD_ATTR           'attackerRoll'
                             00000037     7D - STORE_FAST          'atrTotal'
                             0000003A     7C - LOAD_FAST           'result'
                             0000003D     69 - LOAD_ATTR           'defenderRoll'
                             00000040     7D - STORE_FAST          'defTotal'
                             00000043     74 - LOAD_GLOBAL         'CU'
                             00000046     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000049     64 - LOAD_CONST          'A rolls %d D rolls %d'
                             0000004C     7C - LOAD_FAST           'atrTotal'
                             0000004F     7C - LOAD_FAST           'defTotal'
                             00000052     66 - BUILD_TUPLE         r0002
                             00000055     16 - BINARY_MODULO       
                             00000056     64 - LOAD_CONST          2
                             00000059     83 - CALL_FUNCTION       r0002
                             0000005C     01 - POP_TOP             
                             0000005D     7C - LOAD_FAST           'defender'
                             00000060     69 - LOAD_ATTR           'canBeFreeAttacked'
                             00000063     6F - JUMP_IF_FALSE       -> 00000076
                             00000066     01 - POP_TOP             
                             00000067     7C - LOAD_FAST           'atrTotal'
                             0000006A     7C - LOAD_FAST           'defTotal'
                             0000006D     6A - COMPARE_OP          ">"
                             00000070     7D - STORE_FAST          'attackerWon'
                             00000073     6E - JUMP_FORWARD        -> 0000007D
                             00000076     01 - POP_TOP             
                             00000077     74 - LOAD_GLOBAL         'False'
                             0000007A     7D - STORE_FAST          'attackerWon'
                             0000007D     7C - LOAD_FAST           'attackerWon'
                             00000080     6F - JUMP_IF_FALSE       -> 000001B0
                             00000083     01 - POP_TOP             
                             00000084     74 - LOAD_GLOBAL         'CC'
                             00000087     69 - LOAD_ATTR           'GetFreeAttackDamage'
                             0000008A     7C - LOAD_FAST           'attacker'
                             0000008D     69 - LOAD_ATTR           'damageBonus'
                             00000090     7C - LOAD_FAST           'attacker'
                             00000093     69 - LOAD_ATTR           'damageInfluence'
                             00000096     7C - LOAD_FAST           'attacker'
                             00000099     69 - LOAD_ATTR           'itemDamage'
                             0000009C     7C - LOAD_FAST           'attacker'
                             0000009F     69 - LOAD_ATTR           'itemDamageRange'
                             000000A2     7C - LOAD_FAST           'attacker'
                             000000A5     69 - LOAD_ATTR           'itemWeaponSpeed'
                             000000A8     7C - LOAD_FAST           'attacker'
                             000000AB     69 - LOAD_ATTR           'isEnergizedTactic'
                             000000AE     7C - LOAD_FAST           'attacker'
                             000000B1     69 - LOAD_ATTR           'isPreciseBlows'
                             000000B4     7C - LOAD_FAST           'attacker'
                             000000B7     69 - LOAD_ATTR           'tacticSetting'
                             000000BA     64 - LOAD_CONST          1
                             000000BD     83 - CALL_FUNCTION       r0009
                             000000C0     7D - STORE_FAST          'damage_total'
                             000000C3     74 - LOAD_GLOBAL         'CU'
                             000000C6     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000C9     64 - LOAD_CONST          'PerformWeaponFreeAttack: damage = %d.'
                             000000CC     7C - LOAD_FAST           'damage_total'
                             000000CF     16 - BINARY_MODULO       
                             000000D0     64 - LOAD_CONST          2
                             000000D3     83 - CALL_FUNCTION       r0002
                             000000D6     01 - POP_TOP             
                             000000D7     74 - LOAD_GLOBAL         'CC'
                             000000DA     69 - LOAD_ATTR           'GetDamageReductionValue'
                             000000DD     7C - LOAD_FAST           'attacker'
                             000000E0     69 - LOAD_ATTR           'characterLevel'
                             000000E3     7C - LOAD_FAST           'defender'
                             000000E6     69 - LOAD_ATTR           'characterLevel'
                             000000E9     7C - LOAD_FAST           'defender'
                             000000EC     69 - LOAD_ATTR           'toughness'
                             000000EF     7C - LOAD_FAST           'defender'
                             000000F2     69 - LOAD_ATTR           'rangedToughness'
                             000000F5     17 - BINARY_ADD          
                             000000F6     7C - LOAD_FAST           'damage_total'
                             000000F9     83 - CALL_FUNCTION       r0004
                             000000FC     7D - STORE_FAST          'defender_total_toughness_percent'
                             000000FF     64 - LOAD_CONST          'PerformWeaponFreeAttack: Defender Resistance = %g'
                             00000102     7C - LOAD_FAST           'defender_total_toughness_percent'
                             00000105     16 - BINARY_MODULO       
                             00000106     7D - STORE_FAST          'str'
                             00000109     74 - LOAD_GLOBAL         'CU'
                             0000010C     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000010F     7C - LOAD_FAST           'str'
                             00000112     64 - LOAD_CONST          2
                             00000115     83 - CALL_FUNCTION       r0002
                             00000118     01 - POP_TOP             
                             00000119     74 - LOAD_GLOBAL         'float'
                             0000011C     7C - LOAD_FAST           'damage_total'
                             0000011F     83 - CALL_FUNCTION       r0001
                             00000122     7C - LOAD_FAST           'defender_total_toughness_percent'
                             00000125     14 - BINARY_MULTIPLY     
                             00000126     7C - LOAD_FAST           'result'
                             00000129     5F - STORE_ATTR          'damageAbsorbed'
                             0000012C     7C - LOAD_FAST           'damage_total'
                             0000012F     7C - LOAD_FAST           'result'
                             00000132     69 - LOAD_ATTR           'damageAbsorbed'
                             00000135     18 - BINARY_SUBTRACT     
                             00000136     7C - LOAD_FAST           'result'
                             00000139     5F - STORE_ATTR          'damage'
                             0000013C     74 - LOAD_GLOBAL         'CU'
                             0000013F     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000142     64 - LOAD_CONST          'PerformWeaponFreeAttack: Damage Resisted= %d'
                             00000145     7C - LOAD_FAST           'result'
                             00000148     69 - LOAD_ATTR           'damageAbsorbed'
                             0000014B     16 - BINARY_MODULO       
                             0000014C     64 - LOAD_CONST          2
                             0000014F     83 - CALL_FUNCTION       r0002
                             00000152     01 - POP_TOP             
                             00000153     7C - LOAD_FAST           'result'
                             00000156     69 - LOAD_ATTR           'damage'
                             00000159     64 - LOAD_CONST          0
                             0000015C     6A - COMPARE_OP          "<"
                             0000015F     6F - JUMP_IF_FALSE       -> 00000186
                             00000162     01 - POP_TOP             
                             00000163     74 - LOAD_GLOBAL         'CU'
                             00000166     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000169     64 - LOAD_CONST          'PerformWeaponFreeAttack: Damage < 0: %d'
                             0000016C     7C - LOAD_FAST           'result'
                             0000016F     69 - LOAD_ATTR           'damage'
                             00000172     16 - BINARY_MODULO       
                             00000173     64 - LOAD_CONST          2
                             00000176     83 - CALL_FUNCTION       r0002
                             00000179     01 - POP_TOP             
                             0000017A     64 - LOAD_CONST          1
                             0000017D     7C - LOAD_FAST           'result'
                             00000180     5F - STORE_ATTR          'damage'
                             00000183     6E - JUMP_FORWARD        -> 00000187
                             00000186     01 - POP_TOP             
                             00000187     74 - LOAD_GLOBAL         'CU'
                             0000018A     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000018D     64 - LOAD_CONST          'PerformWeaponFreeAttack: Final Damage: %d'
                             00000190     7C - LOAD_FAST           'result'
                             00000193     69 - LOAD_ATTR           'damage'
                             00000196     16 - BINARY_MODULO       
                             00000197     64 - LOAD_CONST          2
                             0000019A     83 - CALL_FUNCTION       r0002
                             0000019D     01 - POP_TOP             
                             0000019E     74 - LOAD_GLOBAL         'constants'
                             000001A1     69 - LOAD_ATTR           'combat'
                             000001A4     69 - LOAD_ATTR           'FA_ITEM_PERFORMED'
                             000001A7     7C - LOAD_FAST           'result'
                             000001AA     5F - STORE_ATTR          'resultCode'
                             000001AD     6E - JUMP_FORWARD        -> 000001C9
                             000001B0     01 - POP_TOP             
                             000001B1     64 - LOAD_CONST          0
                             000001B4     7C - LOAD_FAST           'result'
                             000001B7     5F - STORE_ATTR          'damage'
                             000001BA     74 - LOAD_GLOBAL         'constants'
                             000001BD     69 - LOAD_ATTR           'combat'
                             000001C0     69 - LOAD_ATTR           'FA_ITEM_FAILED'
                             000001C3     7C - LOAD_FAST           'result'
                             000001C6     5F - STORE_ATTR          'resultCode'
                             000001C9     7C - LOAD_FAST           'item'
                             000001CC     74 - LOAD_GLOBAL         'constants'
                             000001CF     69 - LOAD_ATTR           'combat'
                             000001D2     69 - LOAD_ATTR           'RANGED_SINGLE_PISTOL'
                             000001D5     6A - COMPARE_OP          "=="
                             000001D8     6F - JUMP_IF_FALSE       -> 000001E5
                             000001DB     01 - POP_TOP             
                             000001DC     74 - LOAD_GLOBAL         'Action_FreeAttackWeaponPistol'
                             000001DF     7D - STORE_FAST          'action'
                             000001E2     6E - JUMP_FORWARD        -> 0000026D
                             000001E5     01 - POP_TOP             
                             000001E6     7C - LOAD_FAST           'item'
                             000001E9     74 - LOAD_GLOBAL         'constants'
                             000001EC     69 - LOAD_ATTR           'combat'
                             000001EF     69 - LOAD_ATTR           'RANGED_DOUBLE_PISTOL'
                             000001F2     6A - COMPARE_OP          "=="
                             000001F5     6F - JUMP_IF_FALSE       -> 00000202
                             000001F8     01 - POP_TOP             
                             000001F9     74 - LOAD_GLOBAL         'Action_FreeAttackWeaponDualPistol'
                             000001FC     7D - STORE_FAST          'action'
                             000001FF     6E - JUMP_FORWARD        -> 0000026D
                             00000202     01 - POP_TOP             
                             00000203     7C - LOAD_FAST           'item'
                             00000206     74 - LOAD_GLOBAL         'constants'
                             00000209     69 - LOAD_ATTR           'combat'
                             0000020C     69 - LOAD_ATTR           'RANGED_DBL_MACHINE_GUN'
                             0000020F     6A - COMPARE_OP          "=="
                             00000212     6F - JUMP_IF_FALSE       -> 0000021F
                             00000215     01 - POP_TOP             
                             00000216     74 - LOAD_GLOBAL         'Action_FreeAttackWeaponDualSubM'
                             00000219     7D - STORE_FAST          'action'
                             0000021C     6E - JUMP_FORWARD        -> 0000026D
                             0000021F     01 - POP_TOP             
                             00000220     7C - LOAD_FAST           'item'
                             00000223     74 - LOAD_GLOBAL         'constants'
                             00000226     69 - LOAD_ATTR           'combat'
                             00000229     69 - LOAD_ATTR           'RANGED_MACHINE_GUN'
                             0000022C     6A - COMPARE_OP          "=="
                             0000022F     6F - JUMP_IF_FALSE       -> 0000023C
                             00000232     01 - POP_TOP             
                             00000233     74 - LOAD_GLOBAL         'Action_FreeAttackWeaponSubM'
                             00000236     7D - STORE_FAST          'action'
                             00000239     6E - JUMP_FORWARD        -> 0000026D
                             0000023C     01 - POP_TOP             
                             0000023D     7C - LOAD_FAST           'item'
                             00000240     74 - LOAD_GLOBAL         'constants'
                             00000243     69 - LOAD_ATTR           'combat'
                             00000246     69 - LOAD_ATTR           'RANGED_RIFLE'
                             00000249     6A - COMPARE_OP          "=="
                             0000024C     6F - JUMP_IF_FALSE       -> 00000259
                             0000024F     01 - POP_TOP             
                             00000250     74 - LOAD_GLOBAL         'Action_FreeAttackWeaponRifle'
                             00000253     7D - STORE_FAST          'action'
                             00000256     6E - JUMP_FORWARD        -> 0000026D
                             00000259     01 - POP_TOP             
                             0000025A     74 - LOAD_GLOBAL         'constants'
                             0000025D     69 - LOAD_ATTR           'combat'
                             00000260     69 - LOAD_ATTR           'FA_ERROR'
                             00000263     7C - LOAD_FAST           'result'
                             00000266     5F - STORE_ATTR          'resultCode'
                             00000269     74 - LOAD_GLOBAL         'False'
                             0000026C     53 - RETURN_VALUE        
                             0000026D     7C - LOAD_FAST           'result'
                             00000270     69 - LOAD_ATTR           'resultCode'
                             00000273     74 - LOAD_GLOBAL         'constants'
                             00000276     69 - LOAD_ATTR           'combat'
                             00000279     69 - LOAD_ATTR           'FA_ITEM_PERFORMED'
                             0000027C     6A - COMPARE_OP          "=="
                             0000027F     6F - JUMP_IF_FALSE       -> 000002A5
                             00000282     01 - POP_TOP             
                             00000283     7C - LOAD_FAST           'attacker'
                             00000286     69 - LOAD_ATTR           'gameObject'
                             00000289     69 - LOAD_ATTR           'CharMvt'
                             0000028C     69 - LOAD_ATTR           'playScriptWithTarget'
                             0000028F     74 - LOAD_GLOBAL         'Stance_Aggro'
                             00000292     7C - LOAD_FAST           'action'
                             00000295     7C - LOAD_FAST           'defender'
                             00000298     69 - LOAD_ATTR           'locator'
                             0000029B     74 - LOAD_GLOBAL         'HandgunsAbility'
                             0000029E     83 - CALL_FUNCTION       r0004
                             000002A1     01 - POP_TOP             
                             000002A2     6E - JUMP_FORWARD        -> 000002C5
                             000002A5     01 - POP_TOP             
                             000002A6     7C - LOAD_FAST           'attacker'
                             000002A9     69 - LOAD_ATTR           'gameObject'
                             000002AC     69 - LOAD_ATTR           'CharMvt'
                             000002AF     69 - LOAD_ATTR           'playScriptWithTarget'
                             000002B2     74 - LOAD_GLOBAL         'Stance_Aggro'
                             000002B5     7C - LOAD_FAST           'action'
                             000002B8     7C - LOAD_FAST           'defender'
                             000002BB     69 - LOAD_ATTR           'locator'
                             000002BE     74 - LOAD_GLOBAL         'InvalidAbility'
                             000002C1     83 - CALL_FUNCTION       r0004
                             000002C4     01 - POP_TOP             
                             000002C5     74 - LOAD_GLOBAL         'True'
                             000002C8     53 - RETURN_VALUE        
                             000002C9     64 - LOAD_CONST          None
                             000002CC     53 - RETURN_VALUE        
                         consts:
00000380                     TUPLE: (
00000385                         None (4E),
00000386                         STR: 'weapon free attack func()' (19 00 00 00 77 65 61 70 6F 6E 20 66 72 65 65 20 61 74 74 61 63 6B 20 66 75 6E 63 28 29),
000003A4                         INT: 2 (02 00 00 00),
000003A9                         INT: 0 (00 00 00 00),
000003AE                         STR: 'A rolls %d D rolls %d' (15 00 00 00 41 20 72 6F 6C 6C 73 20 25 64 20 44 20 72 6F 6C 6C 73 20 25 64),
000003C8                         INT: 1 (01 00 00 00),
000003CD                         STR: 'PerformWeaponFreeAttack: damage = %d.' (25 00 00 00 50 65 72 66 6F 72 6D 57 65 61 70 6F 6E 46 72 65 65 41 74 74 61 63 6B 3A 20 64 61 6D 61 67 65 20 3D 20 25 64 2E),
000003F7                         STR: 'PerformWeaponFreeAttack: Defender Resistance = %g' (31 00 00 00 50 65 72 66 6F 72 6D 57 65 61 70 6F 6E 46 72 65 65 41 74 74 61 63 6B 3A 20 44 65 66 65 6E 64 65 72 20 52 65 73 69 73 74 61 6E 63 65 20 3D 20 25 67),
0000042D                         STR: 'PerformWeaponFreeAttack: Damage Resisted= %d' (2C 00 00 00 50 65 72 66 6F 72 6D 57 65 61 70 6F 6E 46 72 65 65 41 74 74 61 63 6B 3A 20 44 61 6D 61 67 65 20 52 65 73 69 73 74 65 64 3D 20 25 64),
0000045E                         STR: 'PerformWeaponFreeAttack: Damage < 0: %d' (27 00 00 00 50 65 72 66 6F 72 6D 57 65 61 70 6F 6E 46 72 65 65 41 74 74 61 63 6B 3A 20 44 61 6D 61 67 65 20 3C 20 30 3A 20 25 64),
0000048A                         STR: 'PerformWeaponFreeAttack: Final Damage: %d' (29 00 00 00 50 65 72 66 6F 72 6D 57 65 61 70 6F 6E 46 72 65 65 41 74 74 61 63 6B 3A 20 46 69 6E 61 6C 20 44 61 6D 61 67 65 3A 20 25 64)
                             )
                         names:
000004B8                     TUPLE: (
000004BD                         STR: 'CU' (02 00 00 00 43 55),
000004C4                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
000004E1                         STR: 'Action_Idle' (0B 00 00 00 41 63 74 69 6F 6E 5F 49 64 6C 65),
000004F1                         STR: 'action' (06 00 00 00 61 63 74 69 6F 6E),
000004FC                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
00000509                         STR: 'itemType' (08 00 00 00 69 74 65 6D 54 79 70 65),
00000516                         STR: 'item' (04 00 00 00 69 74 65 6D),
0000051F                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
0000052A                         STR: 'attackerMod' (0B 00 00 00 61 74 74 61 63 6B 65 72 4D 6F 64),
0000053A                         STR: 'defenderMod' (0B 00 00 00 64 65 66 65 6E 64 65 72 4D 6F 64),
0000054A                         STR: 'attackerRoll' (0C 00 00 00 61 74 74 61 63 6B 65 72 52 6F 6C 6C),
0000055B                         STR: 'atrTotal' (08 00 00 00 61 74 72 54 6F 74 61 6C),
00000568                         STR: 'defenderRoll' (0C 00 00 00 64 65 66 65 6E 64 65 72 52 6F 6C 6C),
00000579                         STR: 'defTotal' (08 00 00 00 64 65 66 54 6F 74 61 6C),
00000586                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
00000593                         STR: 'canBeFreeAttacked' (11 00 00 00 63 61 6E 42 65 46 72 65 65 41 74 74 61 63 6B 65 64),
000005A9                         STR: 'attackerWon' (0B 00 00 00 61 74 74 61 63 6B 65 72 57 6F 6E),
000005B9                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
000005C3                         STR: 'CC' (02 00 00 00 43 43),
000005CA                         STR: 'GetFreeAttackDamage' (13 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65),
000005E2                         STR: 'damageBonus' (0B 00 00 00 64 61 6D 61 67 65 42 6F 6E 75 73),
000005F2                         STR: 'damageInfluence' (0F 00 00 00 64 61 6D 61 67 65 49 6E 66 6C 75 65 6E 63 65),
00000606                         STR: 'itemDamage' (0A 00 00 00 69 74 65 6D 44 61 6D 61 67 65),
00000615                         STR: 'itemDamageRange' (0F 00 00 00 69 74 65 6D 44 61 6D 61 67 65 52 61 6E 67 65),
00000629                         STR: 'itemWeaponSpeed' (0F 00 00 00 69 74 65 6D 57 65 61 70 6F 6E 53 70 65 65 64),
0000063D                         STR: 'isEnergizedTactic' (11 00 00 00 69 73 45 6E 65 72 67 69 7A 65 64 54 61 63 74 69 63),
00000653                         STR: 'isPreciseBlows' (0E 00 00 00 69 73 50 72 65 63 69 73 65 42 6C 6F 77 73),
00000666                         STR: 'tacticSetting' (0D 00 00 00 74 61 63 74 69 63 53 65 74 74 69 6E 67),
00000678                         STR: 'damage_total' (0C 00 00 00 64 61 6D 61 67 65 5F 74 6F 74 61 6C),
00000689                         STR: 'GetDamageReductionValue' (17 00 00 00 47 65 74 44 61 6D 61 67 65 52 65 64 75 63 74 69 6F 6E 56 61 6C 75 65),
000006A5                         STR: 'characterLevel' (0E 00 00 00 63 68 61 72 61 63 74 65 72 4C 65 76 65 6C),
000006B8                         STR: 'toughness' (09 00 00 00 74 6F 75 67 68 6E 65 73 73),
000006C6                         STR: 'rangedToughness' (0F 00 00 00 72 61 6E 67 65 64 54 6F 75 67 68 6E 65 73 73),
000006DA                         STR: 'defender_total_toughness_percent' (20 00 00 00 64 65 66 65 6E 64 65 72 5F 74 6F 74 61 6C 5F 74 6F 75 67 68 6E 65 73 73 5F 70 65 72 63 65 6E 74),
000006FF                         STR: 'str' (03 00 00 00 73 74 72),
00000707                         STR: 'float' (05 00 00 00 66 6C 6F 61 74),
00000711                         STR: 'damageAbsorbed' (0E 00 00 00 64 61 6D 61 67 65 41 62 73 6F 72 62 65 64),
00000724                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
0000072F                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
0000073D                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
00000748                         STR: 'FA_ITEM_PERFORMED' (11 00 00 00 46 41 5F 49 54 45 4D 5F 50 45 52 46 4F 52 4D 45 44),
0000075E                         STR: 'resultCode' (0A 00 00 00 72 65 73 75 6C 74 43 6F 64 65),
0000076D                         STR: 'FA_ITEM_FAILED' (0E 00 00 00 46 41 5F 49 54 45 4D 5F 46 41 49 4C 45 44),
00000780                         STR: 'RANGED_SINGLE_PISTOL' (14 00 00 00 52 41 4E 47 45 44 5F 53 49 4E 47 4C 45 5F 50 49 53 54 4F 4C),
00000799                         STR: 'Action_FreeAttackWeaponPistol' (1D 00 00 00 41 63 74 69 6F 6E 5F 46 72 65 65 41 74 74 61 63 6B 57 65 61 70 6F 6E 50 69 73 74 6F 6C),
000007BB                         STR: 'RANGED_DOUBLE_PISTOL' (14 00 00 00 52 41 4E 47 45 44 5F 44 4F 55 42 4C 45 5F 50 49 53 54 4F 4C),
000007D4                         STR: 'Action_FreeAttackWeaponDualPistol' (21 00 00 00 41 63 74 69 6F 6E 5F 46 72 65 65 41 74 74 61 63 6B 57 65 61 70 6F 6E 44 75 61 6C 50 69 73 74 6F 6C),
000007FA                         STR: 'RANGED_DBL_MACHINE_GUN' (16 00 00 00 52 41 4E 47 45 44 5F 44 42 4C 5F 4D 41 43 48 49 4E 45 5F 47 55 4E),
00000815                         STR: 'Action_FreeAttackWeaponDualSubM' (1F 00 00 00 41 63 74 69 6F 6E 5F 46 72 65 65 41 74 74 61 63 6B 57 65 61 70 6F 6E 44 75 61 6C 53 75 62 4D),
00000839                         STR: 'RANGED_MACHINE_GUN' (12 00 00 00 52 41 4E 47 45 44 5F 4D 41 43 48 49 4E 45 5F 47 55 4E),
00000850                         STR: 'Action_FreeAttackWeaponSubM' (1B 00 00 00 41 63 74 69 6F 6E 5F 46 72 65 65 41 74 74 61 63 6B 57 65 61 70 6F 6E 53 75 62 4D),
00000870                         STR: 'RANGED_RIFLE' (0C 00 00 00 52 41 4E 47 45 44 5F 52 49 46 4C 45),
00000881                         STR: 'Action_FreeAttackWeaponRifle' (1C 00 00 00 41 63 74 69 6F 6E 5F 46 72 65 65 41 74 74 61 63 6B 57 65 61 70 6F 6E 52 69 66 6C 65),
000008A2                         STR: 'FA_ERROR' (08 00 00 00 46 41 5F 45 52 52 4F 52),
000008AF                         STR: 'gameObject' (0A 00 00 00 67 61 6D 65 4F 62 6A 65 63 74),
000008BE                         STR: 'CharMvt' (07 00 00 00 43 68 61 72 4D 76 74),
000008CA                         STR: 'playScriptWithTarget' (14 00 00 00 70 6C 61 79 53 63 72 69 70 74 57 69 74 68 54 61 72 67 65 74),
000008E3                         STR: 'Stance_Aggro' (0C 00 00 00 53 74 61 6E 63 65 5F 41 67 67 72 6F),
000008F4                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
00000900                         STR: 'HandgunsAbility' (0F 00 00 00 48 61 6E 64 67 75 6E 73 41 62 69 6C 69 74 79),
00000914                         STR: 'InvalidAbility' (0E 00 00 00 49 6E 76 61 6C 69 64 41 62 69 6C 69 74 79),
00000927                         STR: 'True' (04 00 00 00 54 72 75 65)
                             )
                         varnames:
00000930                     TUPLE: (
00000935                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
00000942                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
0000094F                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
0000095A                         STR: 'atrTotal' (08 00 00 00 61 74 72 54 6F 74 61 6C),
00000967                         STR: 'attackerWon' (0B 00 00 00 61 74 74 61 63 6B 65 72 57 6F 6E),
00000977                         STR: 'damage_total' (0C 00 00 00 64 61 6D 61 67 65 5F 74 6F 74 61 6C),
00000988                         STR: 'defTotal' (08 00 00 00 64 65 66 54 6F 74 61 6C),
00000995                         STR: 'defender_total_toughness_percent' (20 00 00 00 64 65 66 65 6E 64 65 72 5F 74 6F 74 61 6C 5F 74 6F 75 67 68 6E 65 73 73 5F 70 65 72 63 65 6E 74),
000009BA                         STR: 'item' (04 00 00 00 69 74 65 6D),
000009C3                         STR: 'str' (03 00 00 00 73 74 72),
000009CB                         STR: 'action' (06 00 00 00 61 63 74 69 6F 6E)
                             )
                         freevars:
000009D6                     TUPLE: ()
                         cellvars:
000009DB                     TUPLE: ()
                         filename:
000009E0                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_free_attacks.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 66 72 65 65 5F 61 74 74 61 63 6B 73 2E 70 79)
                         name:
00000A3A                     STR: 'PerformWeaponFreeAttack' (17 00 00 00 50 65 72 66 6F 72 6D 57 65 61 70 6F 6E 46 72 65 65 41 74 74 61 63 6B)
                         firslineno:
00000A56                     LONG: 17L (11 00 00 00)
                         lnotab:
00000A5A                     STR: '\x00\x01\x10\x03\x06\x02\t\x05\t\x01\t\x03\t\x01\t\x02\x1a\x01\n\x01\x10\x02\x06\x02\x07\x03?\x01\x14\x03(\x02\n\x01\x10\x03\x13\x01\x10\x01\x17\x02\x10\x01\x17\x01\r\x01\x17\x03\x13\x03\t\x01\x0f\x04\x13\x01\n\x02\x13\x01\n\x02\x13\x01\n\x02\x13\x01\n\x02\x13\x01\n\x03\x0f\x01\x04\x07\x16\x01#\x02\x1f\x02' (56 00 00 00 00 01 10 03 06 02 09 05 09 01 09 03 09 01 09 02 1A 01 0A 01 10 02 06 02 07 03 3F 01 14 03 28 02 0A 01 10 03 13 01 10 01 17 02 10 01 17 01 0D 01 17 03 13 03 09 01 0F 04 13 01 0A 02 13 01 0A 02 13 01 0A 02 13 01 0A 02 13 01 0A 03 0F 01 04 07 16 01 23 02 1F 02),
00000AB5             CODE:
                         argcount:
00000AB6                     LONG: 1L (01 00 00 00)
                         nlocals:
00000ABA                     LONG: 6L (06 00 00 00)
                         stacksize:
00000ABE                     LONG: 3L (03 00 00 00)
                         flags:
00000AC2                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000AC6                     STR: "t\x00\x00i\x01\x00d\x01\x00|\x00\x00\x16d\x02\x00\x83\x02\x00\x01t\x03\x00t\x04\x00t\x05\x00f\x03\x00}\x01\x00t\x07\x00t\x08\x00t\t\x00f\x03\x00}\x02\x00t\x0b\x00t\x0c\x00t\r\x00f\x03\x00}\x03\x00t\x0f\x00t\x10\x00t\x11\x00f\x03\x00}\x04\x00|\x00\x00t\x13\x00j\x02\x00o'\x00\x01t\x14\x00i\x15\x00|\x01\x00\x83\x01\x00}\x05\x00t\x00\x00i\x01\x00d\x03\x00|\x05\x00\x16d\x02\x00\x83\x02\x00\x01n\x8c\x00\x01|\x00\x00t\x17\x00j\x02\x00o'\x00\x01t\x14\x00i\x15\x00|\x02\x00\x83\x01\x00}\x05\x00t\x00\x00i\x01\x00d\x04\x00|\x05\x00\x16d\x02\x00\x83\x02\x00\x01nX\x00\x01|\x00\x00t\x18\x00j\x02\x00o'\x00\x01t\x14\x00i\x15\x00|\x03\x00\x83\x01\x00}\x05\x00t\x00\x00i\x01\x00d\x05\x00|\x05\x00\x16d\x02\x00\x83\x02\x00\x01n$\x00\x01t\x14\x00i\x15\x00|\x04\x00\x83\x01\x00}\x05\x00t\x00\x00i\x01\x00d\x06\x00|\x05\x00\x16d\x02\x00\x83\x02\x00\x01|\x05\x00Sd\x00\x00S" (17 01 00 00 74 00 00 69 01 00 64 01 00 7C 00 00 16 64 02 00 83 02 00 01 74 03 00 74 04 00 74 05 00 66 03 00 7D 01 00 74 07 00 74 08 00 74 09 00 66 03 00 7D 02 00 74 0B 00 74 0C 00 74 0D 00 66 03 00 7D 03 00 74 0F 00 74 10 00 74 11 00 66 03 00 7D 04 00 7C 00 00 74 13 00 6A 02 00 6F 27 00 01 74 14 00 69 15 00 7C 01 00 83 01 00 7D 05 00 74 00 00 69 01 00 64 03 00 7C 05 00 16 64 02 00 83 02 00 01 6E 8C 00 01 7C 00 00 74 17 00 6A 02 00 6F 27 00 01 74 14 00 69 15 00 7C 02 00 83 01 00 7D 05 00 74 00 00 69 01 00 64 04 00 7C 05 00 16 64 02 00 83 02 00 01 6E 58 00 01 7C 00 00 74 18 00 6A 02 00 6F 27 00 01 74 14 00 69 15 00 7C 03 00 83 01 00 7D 05 00 74 00 00 69 01 00 64 05 00 7C 05 00 16 64 02 00 83 02 00 01 6E 24 00 01 74 14 00 69 15 00 7C 04 00 83 01 00 7D 05 00 74 00 00 69 01 00 64 06 00 7C 05 00 16 64 02 00 83 02 00 01 7C 05 00 53 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'CU'
                             00000003     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000006     64 - LOAD_CONST          'martial art style %d.'
                             00000009     7C - LOAD_FAST           'martialArt'
                             0000000C     16 - BINARY_MODULO       
                             0000000D     64 - LOAD_CONST          2
                             00000010     83 - CALL_FUNCTION       r0002
                             00000013     01 - POP_TOP             
                             00000014     74 - LOAD_GLOBAL         'Action_FreeAttackKarate1'
                             00000017     74 - LOAD_GLOBAL         'Action_FreeAttackKarate2'
                             0000001A     74 - LOAD_GLOBAL         'Action_FreeAttackKarate3'
                             0000001D     66 - BUILD_TUPLE         r0003
                             00000020     7D - STORE_FAST          'karateArray'
                             00000023     74 - LOAD_GLOBAL         'Action_FreeAttackWushu1'
                             00000026     74 - LOAD_GLOBAL         'Action_FreeAttackWushu2'
                             00000029     74 - LOAD_GLOBAL         'Action_FreeAttackWushu3'
                             0000002C     66 - BUILD_TUPLE         r0003
                             0000002F     7D - STORE_FAST          'kungfuArray'
                             00000032     74 - LOAD_GLOBAL         'Action_FreeAttackAikido1'
                             00000035     74 - LOAD_GLOBAL         'Action_FreeAttackAikido2'
                             00000038     74 - LOAD_GLOBAL         'Action_FreeAttackAikido3'
                             0000003B     66 - BUILD_TUPLE         r0003
                             0000003E     7D - STORE_FAST          'aikidoArray'
                             00000041     74 - LOAD_GLOBAL         'Action_FreeAttackSelfD1'
                             00000044     74 - LOAD_GLOBAL         'Action_FreeAttackSelfD2'
                             00000047     74 - LOAD_GLOBAL         'Action_FreeAttackSelfD3'
                             0000004A     66 - BUILD_TUPLE         r0003
                             0000004D     7D - STORE_FAST          'selfdefenseArray'
                             00000050     7C - LOAD_FAST           'martialArt'
                             00000053     74 - LOAD_GLOBAL         'KarateAbility'
                             00000056     6A - COMPARE_OP          "=="
                             00000059     6F - JUMP_IF_FALSE       -> 00000083
                             0000005C     01 - POP_TOP             
                             0000005D     74 - LOAD_GLOBAL         'random'
                             00000060     69 - LOAD_ATTR           'choice'
                             00000063     7C - LOAD_FAST           'karateArray'
                             00000066     83 - CALL_FUNCTION       r0001
                             00000069     7D - STORE_FAST          'action'
                             0000006C     74 - LOAD_GLOBAL         'CU'
                             0000006F     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000072     64 - LOAD_CONST          'picking karate melee attack %d.'
                             00000075     7C - LOAD_FAST           'action'
                             00000078     16 - BINARY_MODULO       
                             00000079     64 - LOAD_CONST          2
                             0000007C     83 - CALL_FUNCTION       r0002
                             0000007F     01 - POP_TOP             
                             00000080     6E - JUMP_FORWARD        -> 0000010F
                             00000083     01 - POP_TOP             
                             00000084     7C - LOAD_FAST           'martialArt'
                             00000087     74 - LOAD_GLOBAL         'KungFuAbility'
                             0000008A     6A - COMPARE_OP          "=="
                             0000008D     6F - JUMP_IF_FALSE       -> 000000B7
                             00000090     01 - POP_TOP             
                             00000091     74 - LOAD_GLOBAL         'random'
                             00000094     69 - LOAD_ATTR           'choice'
                             00000097     7C - LOAD_FAST           'kungfuArray'
                             0000009A     83 - CALL_FUNCTION       r0001
                             0000009D     7D - STORE_FAST          'action'
                             000000A0     74 - LOAD_GLOBAL         'CU'
                             000000A3     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000A6     64 - LOAD_CONST          'picking kungfu melee attack %d.'
                             000000A9     7C - LOAD_FAST           'action'
                             000000AC     16 - BINARY_MODULO       
                             000000AD     64 - LOAD_CONST          2
                             000000B0     83 - CALL_FUNCTION       r0002
                             000000B3     01 - POP_TOP             
                             000000B4     6E - JUMP_FORWARD        -> 0000010F
                             000000B7     01 - POP_TOP             
                             000000B8     7C - LOAD_FAST           'martialArt'
                             000000BB     74 - LOAD_GLOBAL         'AikidoAbility'
                             000000BE     6A - COMPARE_OP          "=="
                             000000C1     6F - JUMP_IF_FALSE       -> 000000EB
                             000000C4     01 - POP_TOP             
                             000000C5     74 - LOAD_GLOBAL         'random'
                             000000C8     69 - LOAD_ATTR           'choice'
                             000000CB     7C - LOAD_FAST           'aikidoArray'
                             000000CE     83 - CALL_FUNCTION       r0001
                             000000D1     7D - STORE_FAST          'action'
                             000000D4     74 - LOAD_GLOBAL         'CU'
                             000000D7     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000DA     64 - LOAD_CONST          'picking aikidomelee attack %d.'
                             000000DD     7C - LOAD_FAST           'action'
                             000000E0     16 - BINARY_MODULO       
                             000000E1     64 - LOAD_CONST          2
                             000000E4     83 - CALL_FUNCTION       r0002
                             000000E7     01 - POP_TOP             
                             000000E8     6E - JUMP_FORWARD        -> 0000010F
                             000000EB     01 - POP_TOP             
                             000000EC     74 - LOAD_GLOBAL         'random'
                             000000EF     69 - LOAD_ATTR           'choice'
                             000000F2     7C - LOAD_FAST           'selfdefenseArray'
                             000000F5     83 - CALL_FUNCTION       r0001
                             000000F8     7D - STORE_FAST          'action'
                             000000FB     74 - LOAD_GLOBAL         'CU'
                             000000FE     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000101     64 - LOAD_CONST          'picking self-d melee attack %d.'
                             00000104     7C - LOAD_FAST           'action'
                             00000107     16 - BINARY_MODULO       
                             00000108     64 - LOAD_CONST          2
                             0000010B     83 - CALL_FUNCTION       r0002
                             0000010E     01 - POP_TOP             
                             0000010F     7C - LOAD_FAST           'action'
                             00000112     53 - RETURN_VALUE        
                             00000113     64 - LOAD_CONST          None
                             00000116     53 - RETURN_VALUE        
                         consts:
00000BE2                     TUPLE: (
00000BE7                         None (4E),
00000BE8                         STR: 'martial art style %d.' (15 00 00 00 6D 61 72 74 69 61 6C 20 61 72 74 20 73 74 79 6C 65 20 25 64 2E),
00000C02                         INT: 2 (02 00 00 00),
00000C07                         STR: 'picking karate melee attack %d.' (1F 00 00 00 70 69 63 6B 69 6E 67 20 6B 61 72 61 74 65 20 6D 65 6C 65 65 20 61 74 74 61 63 6B 20 25 64 2E),
00000C2B                         STR: 'picking kungfu melee attack %d.' (1F 00 00 00 70 69 63 6B 69 6E 67 20 6B 75 6E 67 66 75 20 6D 65 6C 65 65 20 61 74 74 61 63 6B 20 25 64 2E),
00000C4F                         STR: 'picking aikidomelee attack %d.' (1E 00 00 00 70 69 63 6B 69 6E 67 20 61 69 6B 69 64 6F 6D 65 6C 65 65 20 61 74 74 61 63 6B 20 25 64 2E),
00000C72                         STR: 'picking self-d melee attack %d.' (1F 00 00 00 70 69 63 6B 69 6E 67 20 73 65 6C 66 2D 64 20 6D 65 6C 65 65 20 61 74 74 61 63 6B 20 25 64 2E)
                             )
                         names:
00000C96                     TUPLE: (
00000C9B                         STR: 'CU' (02 00 00 00 43 55),
00000CA2                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
00000CBF                         STR: 'martialArt' (0A 00 00 00 6D 61 72 74 69 61 6C 41 72 74),
00000CCE                         STR: 'Action_FreeAttackKarate1' (18 00 00 00 41 63 74 69 6F 6E 5F 46 72 65 65 41 74 74 61 63 6B 4B 61 72 61 74 65 31),
00000CEB                         STR: 'Action_FreeAttackKarate2' (18 00 00 00 41 63 74 69 6F 6E 5F 46 72 65 65 41 74 74 61 63 6B 4B 61 72 61 74 65 32),
00000D08                         STR: 'Action_FreeAttackKarate3' (18 00 00 00 41 63 74 69 6F 6E 5F 46 72 65 65 41 74 74 61 63 6B 4B 61 72 61 74 65 33),
00000D25                         STR: 'karateArray' (0B 00 00 00 6B 61 72 61 74 65 41 72 72 61 79),
00000D35                         STR: 'Action_FreeAttackWushu1' (17 00 00 00 41 63 74 69 6F 6E 5F 46 72 65 65 41 74 74 61 63 6B 57 75 73 68 75 31),
00000D51                         STR: 'Action_FreeAttackWushu2' (17 00 00 00 41 63 74 69 6F 6E 5F 46 72 65 65 41 74 74 61 63 6B 57 75 73 68 75 32),
00000D6D                         STR: 'Action_FreeAttackWushu3' (17 00 00 00 41 63 74 69 6F 6E 5F 46 72 65 65 41 74 74 61 63 6B 57 75 73 68 75 33),
00000D89                         STR: 'kungfuArray' (0B 00 00 00 6B 75 6E 67 66 75 41 72 72 61 79),
00000D99                         STR: 'Action_FreeAttackAikido1' (18 00 00 00 41 63 74 69 6F 6E 5F 46 72 65 65 41 74 74 61 63 6B 41 69 6B 69 64 6F 31),
00000DB6                         STR: 'Action_FreeAttackAikido2' (18 00 00 00 41 63 74 69 6F 6E 5F 46 72 65 65 41 74 74 61 63 6B 41 69 6B 69 64 6F 32),
00000DD3                         STR: 'Action_FreeAttackAikido3' (18 00 00 00 41 63 74 69 6F 6E 5F 46 72 65 65 41 74 74 61 63 6B 41 69 6B 69 64 6F 33),
00000DF0                         STR: 'aikidoArray' (0B 00 00 00 61 69 6B 69 64 6F 41 72 72 61 79),
00000E00                         STR: 'Action_FreeAttackSelfD1' (17 00 00 00 41 63 74 69 6F 6E 5F 46 72 65 65 41 74 74 61 63 6B 53 65 6C 66 44 31),
00000E1C                         STR: 'Action_FreeAttackSelfD2' (17 00 00 00 41 63 74 69 6F 6E 5F 46 72 65 65 41 74 74 61 63 6B 53 65 6C 66 44 32),
00000E38                         STR: 'Action_FreeAttackSelfD3' (17 00 00 00 41 63 74 69 6F 6E 5F 46 72 65 65 41 74 74 61 63 6B 53 65 6C 66 44 33),
00000E54                         STR: 'selfdefenseArray' (10 00 00 00 73 65 6C 66 64 65 66 65 6E 73 65 41 72 72 61 79),
00000E69                         STR: 'KarateAbility' (0D 00 00 00 4B 61 72 61 74 65 41 62 69 6C 69 74 79),
00000E7B                         STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00000E86                         STR: 'choice' (06 00 00 00 63 68 6F 69 63 65),
00000E91                         STR: 'action' (06 00 00 00 61 63 74 69 6F 6E),
00000E9C                         STR: 'KungFuAbility' (0D 00 00 00 4B 75 6E 67 46 75 41 62 69 6C 69 74 79),
00000EAE                         STR: 'AikidoAbility' (0D 00 00 00 41 69 6B 69 64 6F 41 62 69 6C 69 74 79)
                             )
                         varnames:
00000EC0                     TUPLE: (
00000EC5                         STR: 'martialArt' (0A 00 00 00 6D 61 72 74 69 61 6C 41 72 74),
00000ED4                         STR: 'karateArray' (0B 00 00 00 6B 61 72 61 74 65 41 72 72 61 79),
00000EE4                         STR: 'kungfuArray' (0B 00 00 00 6B 75 6E 67 66 75 41 72 72 61 79),
00000EF4                         STR: 'aikidoArray' (0B 00 00 00 61 69 6B 69 64 6F 41 72 72 61 79),
00000F04                         STR: 'selfdefenseArray' (10 00 00 00 73 65 6C 66 64 65 66 65 6E 73 65 41 72 72 61 79),
00000F19                         STR: 'action' (06 00 00 00 61 63 74 69 6F 6E)
                             )
                         freevars:
00000F24                     TUPLE: ()
                         cellvars:
00000F29                     TUPLE: ()
                         filename:
00000F2E                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_free_attacks.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 66 72 65 65 5F 61 74 74 61 63 6B 73 2E 70 79)
                         name:
00000F88                     STR: 'GetMeleeFreeAttackScript' (18 00 00 00 47 65 74 4D 65 6C 65 65 46 72 65 65 41 74 74 61 63 6B 53 63 72 69 70 74)
                         firslineno:
00000FA5                     LONG: 103L (67 00 00 00)
                         lnotab:
00000FA9                     STR: '\x00\x02\x14\x02\x0f\x01\x0f\x01\x0f\x01\x0f\x02\r\x01\x0f\x01\x18\x01\r\x01\x0f\x01\x18\x01\r\x01\x0f\x01\x18\x02\x0f\x01\x14\x02' (22 00 00 00 00 02 14 02 0F 01 0F 01 0F 01 0F 02 0D 01 0F 01 18 01 0D 01 0F 01 18 01 0D 01 0F 01 18 02 0F 01 14 02),
00000FD0             CODE:
                         argcount:
00000FD1                     LONG: 3L (03 00 00 00)
                         nlocals:
00000FD5                     LONG: 11L (0B 00 00 00)
                         stacksize:
00000FD9                     LONG: 7L (07 00 00 00)
                         flags:
00000FDD                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000FE1                     STR: 'd\x01\x00}\t\x00d\x01\x00|\x02\x00_\x02\x00d\x01\x00|\x02\x00_\x03\x00|\x02\x00i\x04\x00}\x05\x00|\x02\x00i\x06\x00}\n\x00t\x08\x00i\t\x00d\x02\x00|\x05\x00|\n\x00f\x02\x00\x16d\x03\x00\x83\x02\x00\x01|\x01\x00i\x0b\x00o\x10\x00\x01|\x05\x00|\n\x00j\x04\x00}\x08\x00n\x07\x00\x01t\r\x00}\x08\x00|\x08\x00o\x1b\x01\x01t\x0e\x00i\x0f\x00|\x00\x00i\x11\x00|\x00\x00i\x12\x00|\x00\x00i\x13\x00|\x00\x00i\x14\x00|\x00\x00i\x15\x00d\x04\x00\x83\x06\x00}\x07\x00t\x08\x00i\t\x00d\x05\x00|\x07\x00\x16d\x03\x00\x83\x02\x00\x01t\x0e\x00i\x17\x00|\x00\x00i\x18\x00|\x01\x00i\x18\x00|\x01\x00i\x19\x00|\x01\x00i\x1a\x00\x17|\x07\x00\x83\x04\x00}\x03\x00d\x06\x00|\x03\x00\x16}\x04\x00t\x08\x00i\t\x00|\x04\x00d\x03\x00\x83\x02\x00\x01t\x1d\x00|\x07\x00\x83\x01\x00|\x03\x00\x14|\x02\x00_\x1e\x00|\x07\x00|\x02\x00i\x1e\x00\x18|\x02\x00_\x1f\x00t\x08\x00i\t\x00d\x07\x00|\x02\x00i\x1e\x00\x16d\x03\x00\x83\x02\x00\x01|\x02\x00i\x1f\x00d\x01\x00j\x00\x00o$\x00\x01t\x08\x00i\t\x00d\x08\x00|\x02\x00i\x1f\x00\x16d\x03\x00\x83\x02\x00\x01d\x04\x00|\x02\x00_\x1f\x00n\x01\x00\x01t\x08\x00i\t\x00d\t\x00|\x02\x00i\x1f\x00\x16d\x03\x00\x83\x02\x00\x01t \x00i!\x00i"\x00|\x02\x00_#\x00n\x19\x00\x01d\x01\x00|\x02\x00_\x1f\x00t \x00i!\x00i$\x00|\x02\x00_#\x00t%\x00|\x00\x00i&\x00\x83\x01\x00}\x06\x00t\x08\x00i\t\x00d\n\x00|\x06\x00\x16d\x03\x00\x83\x02\x00\x01|\x02\x00i#\x00t \x00i!\x00i"\x00j\x02\x00o#\x00\x01|\x00\x00i(\x00i)\x00i*\x00t+\x00|\x06\x00|\x01\x00i,\x00t-\x00\x83\x04\x00\x01n \x00\x01|\x00\x00i(\x00i)\x00i*\x00t+\x00|\x06\x00|\x01\x00i,\x00t.\x00\x83\x04\x00\x01t/\x00Sd\x00\x00S' (21 02 00 00 64 01 00 7D 09 00 64 01 00 7C 02 00 5F 02 00 64 01 00 7C 02 00 5F 03 00 7C 02 00 69 04 00 7D 05 00 7C 02 00 69 06 00 7D 0A 00 74 08 00 69 09 00 64 02 00 7C 05 00 7C 0A 00 66 02 00 16 64 03 00 83 02 00 01 7C 01 00 69 0B 00 6F 10 00 01 7C 05 00 7C 0A 00 6A 04 00 7D 08 00 6E 07 00 01 74 0D 00 7D 08 00 7C 08 00 6F 1B 01 01 74 0E 00 69 0F 00 7C 00 00 69 11 00 7C 00 00 69 12 00 7C 00 00 69 13 00 7C 00 00 69 14 00 7C 00 00 69 15 00 64 04 00 83 06 00 7D 07 00 74 08 00 69 09 00 64 05 00 7C 07 00 16 64 03 00 83 02 00 01 74 0E 00 69 17 00 7C 00 00 69 18 00 7C 01 00 69 18 00 7C 01 00 69 19 00 7C 01 00 69 1A 00 17 7C 07 00 83 04 00 7D 03 00 64 06 00 7C 03 00 16 7D 04 00 74 08 00 69 09 00 7C 04 00 64 03 00 83 02 00 01 74 1D 00 7C 07 00 83 01 00 7C 03 00 14 7C 02 00 5F 1E 00 7C 07 00 7C 02 00 69 1E 00 18 7C 02 00 5F 1F 00 74 08 00 69 09 00 64 07 00 7C 02 00 69 1E 00 16 64 03 00 83 02 00 01 7C 02 00 69 1F 00 64 01 00 6A 00 00 6F 24 00 01 74 08 00 69 09 00 64 08 00 7C 02 00 69 1F 00 16 64 03 00 83 02 00 01 64 04 00 7C 02 00 5F 1F 00 6E 01 00 01 74 08 00 69 09 00 64 09 00 7C 02 00 69 1F 00 16 64 03 00 83 02 00 01 74 20 00 69 21 00 69 22 00 7C 02 00 5F 23 00 6E 19 00 01 64 01 00 7C 02 00 5F 1F 00 74 20 00 69 21 00 69 24 00 7C 02 00 5F 23 00 74 25 00 7C 00 00 69 26 00 83 01 00 7D 06 00 74 08 00 69 09 00 64 0A 00 7C 06 00 16 64 03 00 83 02 00 01 7C 02 00 69 23 00 74 20 00 69 21 00 69 22 00 6A 02 00 6F 23 00 01 7C 00 00 69 28 00 69 29 00 69 2A 00 74 2B 00 7C 06 00 7C 01 00 69 2C 00 74 2D 00 83 04 00 01 6E 20 00 01 7C 00 00 69 28 00 69 29 00 69 2A 00 74 2B 00 7C 06 00 7C 01 00 69 2C 00 74 2E 00 83 04 00 01 74 2F 00 53 64 00 00 53)
                             00000000     64 - LOAD_CONST          0
                             00000003     7D - STORE_FAST          'item'
                             00000006     64 - LOAD_CONST          0
                             00000009     7C - LOAD_FAST           'result'
                             0000000C     5F - STORE_ATTR          'attackerMod'
                             0000000F     64 - LOAD_CONST          0
                             00000012     7C - LOAD_FAST           'result'
                             00000015     5F - STORE_ATTR          'defenderMod'
                             00000018     7C - LOAD_FAST           'result'
                             0000001B     69 - LOAD_ATTR           'attackerRoll'
                             0000001E     7D - STORE_FAST          'atrTotal'
                             00000021     7C - LOAD_FAST           'result'
                             00000024     69 - LOAD_ATTR           'defenderRoll'
                             00000027     7D - STORE_FAST          'defTotal'
                             0000002A     74 - LOAD_GLOBAL         'CU'
                             0000002D     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000030     64 - LOAD_CONST          'A rolls %d D rolls %d'
                             00000033     7C - LOAD_FAST           'atrTotal'
                             00000036     7C - LOAD_FAST           'defTotal'
                             00000039     66 - BUILD_TUPLE         r0002
                             0000003C     16 - BINARY_MODULO       
                             0000003D     64 - LOAD_CONST          2
                             00000040     83 - CALL_FUNCTION       r0002
                             00000043     01 - POP_TOP             
                             00000044     7C - LOAD_FAST           'defender'
                             00000047     69 - LOAD_ATTR           'canBeFreeAttacked'
                             0000004A     6F - JUMP_IF_FALSE       -> 0000005D
                             0000004D     01 - POP_TOP             
                             0000004E     7C - LOAD_FAST           'atrTotal'
                             00000051     7C - LOAD_FAST           'defTotal'
                             00000054     6A - COMPARE_OP          ">"
                             00000057     7D - STORE_FAST          'attackerWon'
                             0000005A     6E - JUMP_FORWARD        -> 00000064
                             0000005D     01 - POP_TOP             
                             0000005E     74 - LOAD_GLOBAL         'False'
                             00000061     7D - STORE_FAST          'attackerWon'
                             00000064     7C - LOAD_FAST           'attackerWon'
                             00000067     6F - JUMP_IF_FALSE       -> 00000185
                             0000006A     01 - POP_TOP             
                             0000006B     74 - LOAD_GLOBAL         'CC'
                             0000006E     69 - LOAD_ATTR           'GetFreeAttackDamageMelee'
                             00000071     7C - LOAD_FAST           'attacker'
                             00000074     69 - LOAD_ATTR           'damageBonus'
                             00000077     7C - LOAD_FAST           'attacker'
                             0000007A     69 - LOAD_ATTR           'itemWeaponSpeed'
                             0000007D     7C - LOAD_FAST           'attacker'
                             00000080     69 - LOAD_ATTR           'isEnergizedTactic'
                             00000083     7C - LOAD_FAST           'attacker'
                             00000086     69 - LOAD_ATTR           'isPreciseBlows'
                             00000089     7C - LOAD_FAST           'attacker'
                             0000008C     69 - LOAD_ATTR           'tacticSetting'
                             0000008F     64 - LOAD_CONST          1
                             00000092     83 - CALL_FUNCTION       r0006
                             00000095     7D - STORE_FAST          'damage_total'
                             00000098     74 - LOAD_GLOBAL         'CU'
                             0000009B     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000009E     64 - LOAD_CONST          'PerformMeleeFreeAttack: damage = %d.'
                             000000A1     7C - LOAD_FAST           'damage_total'
                             000000A4     16 - BINARY_MODULO       
                             000000A5     64 - LOAD_CONST          2
                             000000A8     83 - CALL_FUNCTION       r0002
                             000000AB     01 - POP_TOP             
                             000000AC     74 - LOAD_GLOBAL         'CC'
                             000000AF     69 - LOAD_ATTR           'GetDamageReductionValue'
                             000000B2     7C - LOAD_FAST           'attacker'
                             000000B5     69 - LOAD_ATTR           'characterLevel'
                             000000B8     7C - LOAD_FAST           'defender'
                             000000BB     69 - LOAD_ATTR           'characterLevel'
                             000000BE     7C - LOAD_FAST           'defender'
                             000000C1     69 - LOAD_ATTR           'toughness'
                             000000C4     7C - LOAD_FAST           'defender'
                             000000C7     69 - LOAD_ATTR           'meleeToughness'
                             000000CA     17 - BINARY_ADD          
                             000000CB     7C - LOAD_FAST           'damage_total'
                             000000CE     83 - CALL_FUNCTION       r0004
                             000000D1     7D - STORE_FAST          'defender_total_toughness_percent'
                             000000D4     64 - LOAD_CONST          'PerformMeleeFreeAttack: Defender Resistance = %g'
                             000000D7     7C - LOAD_FAST           'defender_total_toughness_percent'
                             000000DA     16 - BINARY_MODULO       
                             000000DB     7D - STORE_FAST          'str'
                             000000DE     74 - LOAD_GLOBAL         'CU'
                             000000E1     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000000E4     7C - LOAD_FAST           'str'
                             000000E7     64 - LOAD_CONST          2
                             000000EA     83 - CALL_FUNCTION       r0002
                             000000ED     01 - POP_TOP             
                             000000EE     74 - LOAD_GLOBAL         'float'
                             000000F1     7C - LOAD_FAST           'damage_total'
                             000000F4     83 - CALL_FUNCTION       r0001
                             000000F7     7C - LOAD_FAST           'defender_total_toughness_percent'
                             000000FA     14 - BINARY_MULTIPLY     
                             000000FB     7C - LOAD_FAST           'result'
                             000000FE     5F - STORE_ATTR          'damageAbsorbed'
                             00000101     7C - LOAD_FAST           'damage_total'
                             00000104     7C - LOAD_FAST           'result'
                             00000107     69 - LOAD_ATTR           'damageAbsorbed'
                             0000010A     18 - BINARY_SUBTRACT     
                             0000010B     7C - LOAD_FAST           'result'
                             0000010E     5F - STORE_ATTR          'damage'
                             00000111     74 - LOAD_GLOBAL         'CU'
                             00000114     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000117     64 - LOAD_CONST          'PerformMeleeFreeAttack: Damage Resisted= %d'
                             0000011A     7C - LOAD_FAST           'result'
                             0000011D     69 - LOAD_ATTR           'damageAbsorbed'
                             00000120     16 - BINARY_MODULO       
                             00000121     64 - LOAD_CONST          2
                             00000124     83 - CALL_FUNCTION       r0002
                             00000127     01 - POP_TOP             
                             00000128     7C - LOAD_FAST           'result'
                             0000012B     69 - LOAD_ATTR           'damage'
                             0000012E     64 - LOAD_CONST          0
                             00000131     6A - COMPARE_OP          "<"
                             00000134     6F - JUMP_IF_FALSE       -> 0000015B
                             00000137     01 - POP_TOP             
                             00000138     74 - LOAD_GLOBAL         'CU'
                             0000013B     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             0000013E     64 - LOAD_CONST          'PerformMeleeFreeAttack: Damage < 0: %d'
                             00000141     7C - LOAD_FAST           'result'
                             00000144     69 - LOAD_ATTR           'damage'
                             00000147     16 - BINARY_MODULO       
                             00000148     64 - LOAD_CONST          2
                             0000014B     83 - CALL_FUNCTION       r0002
                             0000014E     01 - POP_TOP             
                             0000014F     64 - LOAD_CONST          1
                             00000152     7C - LOAD_FAST           'result'
                             00000155     5F - STORE_ATTR          'damage'
                             00000158     6E - JUMP_FORWARD        -> 0000015C
                             0000015B     01 - POP_TOP             
                             0000015C     74 - LOAD_GLOBAL         'CU'
                             0000015F     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             00000162     64 - LOAD_CONST          'PerformMeleeFreeAttack: Final Damage: %d'
                             00000165     7C - LOAD_FAST           'result'
                             00000168     69 - LOAD_ATTR           'damage'
                             0000016B     16 - BINARY_MODULO       
                             0000016C     64 - LOAD_CONST          2
                             0000016F     83 - CALL_FUNCTION       r0002
                             00000172     01 - POP_TOP             
                             00000173     74 - LOAD_GLOBAL         'constants'
                             00000176     69 - LOAD_ATTR           'combat'
                             00000179     69 - LOAD_ATTR           'FA_MELEE_PERFORMED'
                             0000017C     7C - LOAD_FAST           'result'
                             0000017F     5F - STORE_ATTR          'resultCode'
                             00000182     6E - JUMP_FORWARD        -> 0000019E
                             00000185     01 - POP_TOP             
                             00000186     64 - LOAD_CONST          0
                             00000189     7C - LOAD_FAST           'result'
                             0000018C     5F - STORE_ATTR          'damage'
                             0000018F     74 - LOAD_GLOBAL         'constants'
                             00000192     69 - LOAD_ATTR           'combat'
                             00000195     69 - LOAD_ATTR           'FA_MELEE_FAILED'
                             00000198     7C - LOAD_FAST           'result'
                             0000019B     5F - STORE_ATTR          'resultCode'
                             0000019E     74 - LOAD_GLOBAL         'GetMeleeFreeAttackScript'
                             000001A1     7C - LOAD_FAST           'attacker'
                             000001A4     69 - LOAD_ATTR           'specialAbility'
                             000001A7     83 - CALL_FUNCTION       r0001
                             000001AA     7D - STORE_FAST          'action'
                             000001AD     74 - LOAD_GLOBAL         'CU'
                             000001B0     69 - LOAD_ATTR           'outputCombatDebugMessage'
                             000001B3     64 - LOAD_CONST          'playing melee script %d.'
                             000001B6     7C - LOAD_FAST           'action'
                             000001B9     16 - BINARY_MODULO       
                             000001BA     64 - LOAD_CONST          2
                             000001BD     83 - CALL_FUNCTION       r0002
                             000001C0     01 - POP_TOP             
                             000001C1     7C - LOAD_FAST           'result'
                             000001C4     69 - LOAD_ATTR           'resultCode'
                             000001C7     74 - LOAD_GLOBAL         'constants'
                             000001CA     69 - LOAD_ATTR           'combat'
                             000001CD     69 - LOAD_ATTR           'FA_MELEE_PERFORMED'
                             000001D0     6A - COMPARE_OP          "=="
                             000001D3     6F - JUMP_IF_FALSE       -> 000001F9
                             000001D6     01 - POP_TOP             
                             000001D7     7C - LOAD_FAST           'attacker'
                             000001DA     69 - LOAD_ATTR           'gameObject'
                             000001DD     69 - LOAD_ATTR           'CharMvt'
                             000001E0     69 - LOAD_ATTR           'playScriptWithTarget'
                             000001E3     74 - LOAD_GLOBAL         'Stance_Aggro'
                             000001E6     7C - LOAD_FAST           'action'
                             000001E9     7C - LOAD_FAST           'defender'
                             000001EC     69 - LOAD_ATTR           'locator'
                             000001EF     74 - LOAD_GLOBAL         'HandgunsAbility'
                             000001F2     83 - CALL_FUNCTION       r0004
                             000001F5     01 - POP_TOP             
                             000001F6     6E - JUMP_FORWARD        -> 00000219
                             000001F9     01 - POP_TOP             
                             000001FA     7C - LOAD_FAST           'attacker'
                             000001FD     69 - LOAD_ATTR           'gameObject'
                             00000200     69 - LOAD_ATTR           'CharMvt'
                             00000203     69 - LOAD_ATTR           'playScriptWithTarget'
                             00000206     74 - LOAD_GLOBAL         'Stance_Aggro'
                             00000209     7C - LOAD_FAST           'action'
                             0000020C     7C - LOAD_FAST           'defender'
                             0000020F     69 - LOAD_ATTR           'locator'
                             00000212     74 - LOAD_GLOBAL         'InvalidAbility'
                             00000215     83 - CALL_FUNCTION       r0004
                             00000218     01 - POP_TOP             
                             00000219     74 - LOAD_GLOBAL         'True'
                             0000021C     53 - RETURN_VALUE        
                             0000021D     64 - LOAD_CONST          None
                             00000220     53 - RETURN_VALUE        
                         consts:
00001207                     TUPLE: (
0000120C                         None (4E),
0000120D                         INT: 0 (00 00 00 00),
00001212                         STR: 'A rolls %d D rolls %d' (15 00 00 00 41 20 72 6F 6C 6C 73 20 25 64 20 44 20 72 6F 6C 6C 73 20 25 64),
0000122C                         INT: 2 (02 00 00 00),
00001231                         INT: 1 (01 00 00 00),
00001236                         STR: 'PerformMeleeFreeAttack: damage = %d.' (24 00 00 00 50 65 72 66 6F 72 6D 4D 65 6C 65 65 46 72 65 65 41 74 74 61 63 6B 3A 20 64 61 6D 61 67 65 20 3D 20 25 64 2E),
0000125F                         STR: 'PerformMeleeFreeAttack: Defender Resistance = %g' (30 00 00 00 50 65 72 66 6F 72 6D 4D 65 6C 65 65 46 72 65 65 41 74 74 61 63 6B 3A 20 44 65 66 65 6E 64 65 72 20 52 65 73 69 73 74 61 6E 63 65 20 3D 20 25 67),
00001294                         STR: 'PerformMeleeFreeAttack: Damage Resisted= %d' (2B 00 00 00 50 65 72 66 6F 72 6D 4D 65 6C 65 65 46 72 65 65 41 74 74 61 63 6B 3A 20 44 61 6D 61 67 65 20 52 65 73 69 73 74 65 64 3D 20 25 64),
000012C4                         STR: 'PerformMeleeFreeAttack: Damage < 0: %d' (26 00 00 00 50 65 72 66 6F 72 6D 4D 65 6C 65 65 46 72 65 65 41 74 74 61 63 6B 3A 20 44 61 6D 61 67 65 20 3C 20 30 3A 20 25 64),
000012EF                         STR: 'PerformMeleeFreeAttack: Final Damage: %d' (28 00 00 00 50 65 72 66 6F 72 6D 4D 65 6C 65 65 46 72 65 65 41 74 74 61 63 6B 3A 20 46 69 6E 61 6C 20 44 61 6D 61 67 65 3A 20 25 64),
0000131C                         STR: 'playing melee script %d.' (18 00 00 00 70 6C 61 79 69 6E 67 20 6D 65 6C 65 65 20 73 63 72 69 70 74 20 25 64 2E)
                             )
                         names:
00001339                     TUPLE: (
0000133E                         STR: 'item' (04 00 00 00 69 74 65 6D),
00001347                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
00001352                         STR: 'attackerMod' (0B 00 00 00 61 74 74 61 63 6B 65 72 4D 6F 64),
00001362                         STR: 'defenderMod' (0B 00 00 00 64 65 66 65 6E 64 65 72 4D 6F 64),
00001372                         STR: 'attackerRoll' (0C 00 00 00 61 74 74 61 63 6B 65 72 52 6F 6C 6C),
00001383                         STR: 'atrTotal' (08 00 00 00 61 74 72 54 6F 74 61 6C),
00001390                         STR: 'defenderRoll' (0C 00 00 00 64 65 66 65 6E 64 65 72 52 6F 6C 6C),
000013A1                         STR: 'defTotal' (08 00 00 00 64 65 66 54 6F 74 61 6C),
000013AE                         STR: 'CU' (02 00 00 00 43 55),
000013B5                         STR: 'outputCombatDebugMessage' (18 00 00 00 6F 75 74 70 75 74 43 6F 6D 62 61 74 44 65 62 75 67 4D 65 73 73 61 67 65),
000013D2                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
000013DF                         STR: 'canBeFreeAttacked' (11 00 00 00 63 61 6E 42 65 46 72 65 65 41 74 74 61 63 6B 65 64),
000013F5                         STR: 'attackerWon' (0B 00 00 00 61 74 74 61 63 6B 65 72 57 6F 6E),
00001405                         STR: 'False' (05 00 00 00 46 61 6C 73 65),
0000140F                         STR: 'CC' (02 00 00 00 43 43),
00001416                         STR: 'GetFreeAttackDamageMelee' (18 00 00 00 47 65 74 46 72 65 65 41 74 74 61 63 6B 44 61 6D 61 67 65 4D 65 6C 65 65),
00001433                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
00001440                         STR: 'damageBonus' (0B 00 00 00 64 61 6D 61 67 65 42 6F 6E 75 73),
00001450                         STR: 'itemWeaponSpeed' (0F 00 00 00 69 74 65 6D 57 65 61 70 6F 6E 53 70 65 65 64),
00001464                         STR: 'isEnergizedTactic' (11 00 00 00 69 73 45 6E 65 72 67 69 7A 65 64 54 61 63 74 69 63),
0000147A                         STR: 'isPreciseBlows' (0E 00 00 00 69 73 50 72 65 63 69 73 65 42 6C 6F 77 73),
0000148D                         STR: 'tacticSetting' (0D 00 00 00 74 61 63 74 69 63 53 65 74 74 69 6E 67),
0000149F                         STR: 'damage_total' (0C 00 00 00 64 61 6D 61 67 65 5F 74 6F 74 61 6C),
000014B0                         STR: 'GetDamageReductionValue' (17 00 00 00 47 65 74 44 61 6D 61 67 65 52 65 64 75 63 74 69 6F 6E 56 61 6C 75 65),
000014CC                         STR: 'characterLevel' (0E 00 00 00 63 68 61 72 61 63 74 65 72 4C 65 76 65 6C),
000014DF                         STR: 'toughness' (09 00 00 00 74 6F 75 67 68 6E 65 73 73),
000014ED                         STR: 'meleeToughness' (0E 00 00 00 6D 65 6C 65 65 54 6F 75 67 68 6E 65 73 73),
00001500                         STR: 'defender_total_toughness_percent' (20 00 00 00 64 65 66 65 6E 64 65 72 5F 74 6F 74 61 6C 5F 74 6F 75 67 68 6E 65 73 73 5F 70 65 72 63 65 6E 74),
00001525                         STR: 'str' (03 00 00 00 73 74 72),
0000152D                         STR: 'float' (05 00 00 00 66 6C 6F 61 74),
00001537                         STR: 'damageAbsorbed' (0E 00 00 00 64 61 6D 61 67 65 41 62 73 6F 72 62 65 64),
0000154A                         STR: 'damage' (06 00 00 00 64 61 6D 61 67 65),
00001555                         STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
00001563                         STR: 'combat' (06 00 00 00 63 6F 6D 62 61 74),
0000156E                         STR: 'FA_MELEE_PERFORMED' (12 00 00 00 46 41 5F 4D 45 4C 45 45 5F 50 45 52 46 4F 52 4D 45 44),
00001585                         STR: 'resultCode' (0A 00 00 00 72 65 73 75 6C 74 43 6F 64 65),
00001594                         STR: 'FA_MELEE_FAILED' (0F 00 00 00 46 41 5F 4D 45 4C 45 45 5F 46 41 49 4C 45 44),
000015A8                         STR: 'GetMeleeFreeAttackScript' (18 00 00 00 47 65 74 4D 65 6C 65 65 46 72 65 65 41 74 74 61 63 6B 53 63 72 69 70 74),
000015C5                         STR: 'specialAbility' (0E 00 00 00 73 70 65 63 69 61 6C 41 62 69 6C 69 74 79),
000015D8                         STR: 'action' (06 00 00 00 61 63 74 69 6F 6E),
000015E3                         STR: 'gameObject' (0A 00 00 00 67 61 6D 65 4F 62 6A 65 63 74),
000015F2                         STR: 'CharMvt' (07 00 00 00 43 68 61 72 4D 76 74),
000015FE                         STR: 'playScriptWithTarget' (14 00 00 00 70 6C 61 79 53 63 72 69 70 74 57 69 74 68 54 61 72 67 65 74),
00001617                         STR: 'Stance_Aggro' (0C 00 00 00 53 74 61 6E 63 65 5F 41 67 67 72 6F),
00001628                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
00001634                         STR: 'HandgunsAbility' (0F 00 00 00 48 61 6E 64 67 75 6E 73 41 62 69 6C 69 74 79),
00001648                         STR: 'InvalidAbility' (0E 00 00 00 49 6E 76 61 6C 69 64 41 62 69 6C 69 74 79),
0000165B                         STR: 'True' (04 00 00 00 54 72 75 65)
                             )
                         varnames:
00001664                     TUPLE: (
00001669                         STR: 'attacker' (08 00 00 00 61 74 74 61 63 6B 65 72),
00001676                         STR: 'defender' (08 00 00 00 64 65 66 65 6E 64 65 72),
00001683                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
0000168E                         STR: 'defender_total_toughness_percent' (20 00 00 00 64 65 66 65 6E 64 65 72 5F 74 6F 74 61 6C 5F 74 6F 75 67 68 6E 65 73 73 5F 70 65 72 63 65 6E 74),
000016B3                         STR: 'str' (03 00 00 00 73 74 72),
000016BB                         STR: 'atrTotal' (08 00 00 00 61 74 72 54 6F 74 61 6C),
000016C8                         STR: 'action' (06 00 00 00 61 63 74 69 6F 6E),
000016D3                         STR: 'damage_total' (0C 00 00 00 64 61 6D 61 67 65 5F 74 6F 74 61 6C),
000016E4                         STR: 'attackerWon' (0B 00 00 00 61 74 74 61 63 6B 65 72 57 6F 6E),
000016F4                         STR: 'item' (04 00 00 00 69 74 65 6D),
000016FD                         STR: 'defTotal' (08 00 00 00 64 65 66 54 6F 74 61 6C)
                             )
                         freevars:
0000170A                     TUPLE: ()
                         cellvars:
0000170F                     TUPLE: ()
                         filename:
00001714                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_free_attacks.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 66 72 65 65 5F 61 74 74 61 63 6B 73 2E 70 79)
                         name:
0000176E                     STR: 'PerformMeleeFreeAttack' (16 00 00 00 50 65 72 66 6F 72 6D 4D 65 6C 65 65 46 72 65 65 41 74 74 61 63 6B)
                         firslineno:
00001789                     LONG: 127L (7F 00 00 00)
                         lnotab:
0000178D                     STR: '\x00\x02\x06\x04\t\x01\t\x03\t\x01\t\x02\x1a\x02\n\x01\x10\x02\x06\x02\x07\x03-\x01\x14\x03(\x02\n\x01\x10\x03\x13\x01\x10\x01\x17\x02\x10\x01\x17\x01\r\x01\x17\x03\x13\x03\t\x01\x0f\x04\x0f\x06\x14\x01\x16\x01#\x02\x1f\x02' (3E 00 00 00 00 02 06 04 09 01 09 03 09 01 09 02 1A 02 0A 01 10 02 06 02 07 03 2D 01 14 03 28 02 0A 01 10 03 13 01 10 01 17 02 10 01 17 01 0D 01 17 03 13 03 09 01 0F 04 0F 06 14 01 16 01 23 02 1F 02)
                 )
             names:
000017D0         TUPLE: (
000017D5             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
000017E0             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
000017EE             STR: 'obj' (03 00 00 00 6F 62 6A),
000017F6             STR: 'combat_defines' (0E 00 00 00 63 6F 6D 62 61 74 5F 64 65 66 69 6E 65 73),
00001809             STR: 'CD' (02 00 00 00 43 44),
00001810             STR: 'math' (04 00 00 00 6D 61 74 68),
00001819             STR: 'combat_utility' (0E 00 00 00 63 6F 6D 62 61 74 5F 75 74 69 6C 69 74 79),
0000182C             STR: 'CU' (02 00 00 00 43 55),
00001833             STR: 'combat_innerstrength' (14 00 00 00 63 6F 6D 62 61 74 5F 69 6E 6E 65 72 73 74 72 65 6E 67 74 68),
0000184C             STR: 'CI' (02 00 00 00 43 49),
00001853             STR: 'combat_resolution' (11 00 00 00 63 6F 6D 62 61 74 5F 72 65 73 6F 6C 75 74 69 6F 6E),
00001869             STR: 'CR' (02 00 00 00 43 52),
00001870             STR: 'generic_free_attacks' (14 00 00 00 67 65 6E 65 72 69 63 5F 66 72 65 65 5F 61 74 74 61 63 6B 73),
00001889             STR: 'GenFA' (05 00 00 00 47 65 6E 46 41),
00001893             STR: 'combat_calculations' (13 00 00 00 63 6F 6D 62 61 74 5F 63 61 6C 63 75 6C 61 74 69 6F 6E 73),
000018AB             STR: 'CC' (02 00 00 00 43 43),
000018B2             STR: 'PerformWeaponFreeAttack' (17 00 00 00 50 65 72 66 6F 72 6D 57 65 61 70 6F 6E 46 72 65 65 41 74 74 61 63 6B),
000018CE             STR: 'GetMeleeFreeAttackScript' (18 00 00 00 47 65 74 4D 65 6C 65 65 46 72 65 65 41 74 74 61 63 6B 53 63 72 69 70 74),
000018EB             STR: 'PerformMeleeFreeAttack' (16 00 00 00 50 65 72 66 6F 72 6D 4D 65 6C 65 65 46 72 65 65 41 74 74 61 63 6B)
                 )
             varnames:
00001906         TUPLE: (
0000190B             STR: 'CI' (02 00 00 00 43 49),
00001912             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00001920             STR: 'obj' (03 00 00 00 6F 62 6A),
00001928             STR: 'CC' (02 00 00 00 43 43),
0000192F             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
0000193A             STR: 'PerformWeaponFreeAttack' (17 00 00 00 50 65 72 66 6F 72 6D 57 65 61 70 6F 6E 46 72 65 65 41 74 74 61 63 6B),
00001956             STR: 'CD' (02 00 00 00 43 44),
0000195D             STR: 'GenFA' (05 00 00 00 47 65 6E 46 41),
00001967             STR: 'math' (04 00 00 00 6D 61 74 68),
00001970             STR: 'GetMeleeFreeAttackScript' (18 00 00 00 47 65 74 4D 65 6C 65 65 46 72 65 65 41 74 74 61 63 6B 53 63 72 69 70 74),
0000198D             STR: 'CR' (02 00 00 00 43 52),
00001994             STR: 'PerformMeleeFreeAttack' (16 00 00 00 50 65 72 66 6F 72 6D 4D 65 6C 65 65 46 72 65 65 41 74 74 61 63 6B),
000019AF             STR: 'CU' (02 00 00 00 43 55)
                 )
             freevars:
000019B6         TUPLE: ()
             cellvars:
000019BB         TUPLE: ()
             filename:
000019C0         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\interlock\\combat_free_attacks.py' (55 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 69 6E 74 65 72 6C 6F 63 6B 5C 63 6F 6D 62 61 74 5F 66 72 65 65 5F 61 74 74 61 63 6B 73 2E 70 79)
             name:
00001A1A         STR: '?' (01 00 00 00 3F)
             firslineno:
00001A20         LONG: 1L (01 00 00 00)
             lnotab:
00001A24         STR: '\t\x01\t\x01\t\x01\t\x01\t\x01\t\x01\t\x01\t\x01\t\x01\t\x07\tV\t\x18' (18 00 00 00 09 01 09 01 09 01 09 01 09 01 09 01 09 01 09 01 09 01 09 07 09 56 09 18)

