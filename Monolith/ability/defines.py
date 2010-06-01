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
00000019         STR: 'd\x00\x00Z\x00\x00d\x01\x00Z\x01\x00d\x02\x00Z\x02\x00d\x03\x00Z\x03\x00d\x04\x00Z\x04\x00e\x04\x00d\x05\x00\x14Z\x05\x00e\x04\x00d\x06\x00\x14Z\x06\x00e\x04\x00d\x07\x00\x14Z\x07\x00e\x04\x00d\x08\x00\x14Z\x08\x00e\x04\x00d\t\x00\x14Z\t\x00d\x01\x00d\n\x00>Z\n\x00d\x0b\x00d\n\x00>Z\x0b\x00d\x0c\x00d\n\x00>Z\x0c\x00d\r\x00d\n\x00>Z\r\x00d\x0e\x00d\n\x00>Z\x0e\x00d\x01\x00d\x0f\x00>Z\x0f\x00d\x0b\x00d\x0f\x00>Z\x10\x00d\x0c\x00d\x0f\x00>Z\x11\x00d\r\x00d\x0f\x00>Z\x12\x00d\x05\x00d\x0f\x00>Z\x13\x00d\x10\x00d\x0f\x00>Z\x14\x00d\x0e\x00d\x0f\x00>Z\x15\x00d\x11\x00d\x0f\x00>Z\x16\x00d\x12\x00d\x0f\x00>Z\x17\x00d\x06\x00d\x0f\x00>Z\x18\x00d\x13\x00d\x0f\x00>Z\x19\x00d\x14\x00d\x0f\x00>Z\x1a\x00d\x15\x00d\x0f\x00>Z\x1b\x00d\x16\x00d\x0f\x00>Z\x1c\x00d\x01\x00d\x0f\x00>Z\x1d\x00d\x0b\x00d\x0f\x00>Z\x1e\x00d\x0c\x00d\x0f\x00>Z\x1f\x00d\r\x00d\x0f\x00>Z \x00d\x05\x00d\x0f\x00>Z!\x00d\x10\x00d\x0f\x00>Z"\x00d\x17\x00S' (4E 01 00 00 64 00 00 5A 00 00 64 01 00 5A 01 00 64 02 00 5A 02 00 64 03 00 5A 03 00 64 04 00 5A 04 00 65 04 00 64 05 00 14 5A 05 00 65 04 00 64 06 00 14 5A 06 00 65 04 00 64 07 00 14 5A 07 00 65 04 00 64 08 00 14 5A 08 00 65 04 00 64 09 00 14 5A 09 00 64 01 00 64 0A 00 3E 5A 0A 00 64 0B 00 64 0A 00 3E 5A 0B 00 64 0C 00 64 0A 00 3E 5A 0C 00 64 0D 00 64 0A 00 3E 5A 0D 00 64 0E 00 64 0A 00 3E 5A 0E 00 64 01 00 64 0F 00 3E 5A 0F 00 64 0B 00 64 0F 00 3E 5A 10 00 64 0C 00 64 0F 00 3E 5A 11 00 64 0D 00 64 0F 00 3E 5A 12 00 64 05 00 64 0F 00 3E 5A 13 00 64 10 00 64 0F 00 3E 5A 14 00 64 0E 00 64 0F 00 3E 5A 15 00 64 11 00 64 0F 00 3E 5A 16 00 64 12 00 64 0F 00 3E 5A 17 00 64 06 00 64 0F 00 3E 5A 18 00 64 13 00 64 0F 00 3E 5A 19 00 64 14 00 64 0F 00 3E 5A 1A 00 64 15 00 64 0F 00 3E 5A 1B 00 64 16 00 64 0F 00 3E 5A 1C 00 64 01 00 64 0F 00 3E 5A 1D 00 64 0B 00 64 0F 00 3E 5A 1E 00 64 0C 00 64 0F 00 3E 5A 1F 00 64 0D 00 64 0F 00 3E 5A 20 00 64 05 00 64 0F 00 3E 5A 21 00 64 10 00 64 0F 00 3E 5A 22 00 64 17 00 53)
                 00000000     64 - LOAD_CONST          -2
                 00000003     5A - STORE_NAME          'HYPERDODGED'
                 00000006     64 - LOAD_CONST          1
                 00000009     5A - STORE_NAME          'SUCCESS_EQUIP_ITEM'
                 0000000C     64 - LOAD_CONST          0
                 0000000F     5A - STORE_NAME          'NO_DAMAGE'
                 00000012     64 - LOAD_CONST          30.0
                 00000015     5A - STORE_NAME          'ThirtySecs'
                 00000018     64 - LOAD_CONST          60.0
                 0000001B     5A - STORE_NAME          'OneMin'
                 0000001E     65 - LOAD_NAME           'OneMin'
                 00000021     64 - LOAD_CONST          5
                 00000024     14 - BINARY_MULTIPLY     
                 00000025     5A - STORE_NAME          'FiveMins'
                 00000028     65 - LOAD_NAME           'OneMin'
                 0000002B     64 - LOAD_CONST          10
                 0000002E     14 - BINARY_MULTIPLY     
                 0000002F     5A - STORE_NAME          'TenMins'
                 00000032     65 - LOAD_NAME           'OneMin'
                 00000035     64 - LOAD_CONST          20
                 00000038     14 - BINARY_MULTIPLY     
                 00000039     5A - STORE_NAME          'TwentyMins'
                 0000003C     65 - LOAD_NAME           'OneMin'
                 0000003F     64 - LOAD_CONST          30
                 00000042     14 - BINARY_MULTIPLY     
                 00000043     5A - STORE_NAME          'ThirtyMins'
                 00000046     65 - LOAD_NAME           'OneMin'
                 00000049     64 - LOAD_CONST          60
                 0000004C     14 - BINARY_MULTIPLY     
                 0000004D     5A - STORE_NAME          'SixtyMins'
                 00000050     64 - LOAD_CONST          1
                 00000053     64 - LOAD_CONST          29
                 00000056     3E - BINARY_LSHIFT       
                 00000057     5A - STORE_NAME          'MOD_AFFECTS_TOUGHNESS'
                 0000005A     64 - LOAD_CONST          2
                 0000005D     64 - LOAD_CONST          29
                 00000060     3E - BINARY_LSHIFT       
                 00000061     5A - STORE_NAME          'MOD_AFFECTS_DAMAGE_BONUS'
                 00000064     64 - LOAD_CONST          3
                 00000067     64 - LOAD_CONST          29
                 0000006A     3E - BINARY_LSHIFT       
                 0000006B     5A - STORE_NAME          'MOD_AFFECTS_ATTACKMOD'
                 0000006E     64 - LOAD_CONST          4
                 00000071     64 - LOAD_CONST          29
                 00000074     3E - BINARY_LSHIFT       
                 00000075     5A - STORE_NAME          'MOD_AFFECTS_DEFENSEMOD'
                 00000078     64 - LOAD_CONST          7
                 0000007B     64 - LOAD_CONST          29
                 0000007E     3E - BINARY_LSHIFT       
                 0000007F     5A - STORE_NAME          'MOD_COMBAT_FLAG_ENABLER'
                 00000082     64 - LOAD_CONST          1
                 00000085     64 - LOAD_CONST          24
                 00000088     3E - BINARY_LSHIFT       
                 00000089     5A - STORE_NAME          'MOD_RANGED'
                 0000008C     64 - LOAD_CONST          2
                 0000008F     64 - LOAD_CONST          24
                 00000092     3E - BINARY_LSHIFT       
                 00000093     5A - STORE_NAME          'MOD_MELEE'
                 00000096     64 - LOAD_CONST          3
                 00000099     64 - LOAD_CONST          24
                 0000009C     3E - BINARY_LSHIFT       
                 0000009D     5A - STORE_NAME          'MOD_GUNS'
                 000000A0     64 - LOAD_CONST          4
                 000000A3     64 - LOAD_CONST          24
                 000000A6     3E - BINARY_LSHIFT       
                 000000A7     5A - STORE_NAME          'MOD_PISTOL'
                 000000AA     64 - LOAD_CONST          5
                 000000AD     64 - LOAD_CONST          24
                 000000B0     3E - BINARY_LSHIFT       
                 000000B1     5A - STORE_NAME          'MOD_RIFLE'
                 000000B4     64 - LOAD_CONST          6
                 000000B7     64 - LOAD_CONST          24
                 000000BA     3E - BINARY_LSHIFT       
                 000000BB     5A - STORE_NAME          'MOD_SUB_MACHINE_GUN'
                 000000BE     64 - LOAD_CONST          7
                 000000C1     64 - LOAD_CONST          24
                 000000C4     3E - BINARY_LSHIFT       
                 000000C5     5A - STORE_NAME          'MOD_DUAL_PISTOL'
                 000000C8     64 - LOAD_CONST          8
                 000000CB     64 - LOAD_CONST          24
                 000000CE     3E - BINARY_LSHIFT       
                 000000CF     5A - STORE_NAME          'MOD_SPEED'
                 000000D2     64 - LOAD_CONST          9
                 000000D5     64 - LOAD_CONST          24
                 000000D8     3E - BINARY_LSHIFT       
                 000000D9     5A - STORE_NAME          'MOD_POWER'
                 000000DC     64 - LOAD_CONST          10
                 000000DF     64 - LOAD_CONST          24
                 000000E2     3E - BINARY_LSHIFT       
                 000000E3     5A - STORE_NAME          'MOD_DEFENSE'
                 000000E6     64 - LOAD_CONST          11
                 000000E9     64 - LOAD_CONST          24
                 000000EC     3E - BINARY_LSHIFT       
                 000000ED     5A - STORE_NAME          'MOD_STUNNED'
                 000000F0     64 - LOAD_CONST          12
                 000000F3     64 - LOAD_CONST          24
                 000000F6     3E - BINARY_LSHIFT       
                 000000F7     5A - STORE_NAME          'MOD_CONFUSED'
                 000000FA     64 - LOAD_CONST          13
                 000000FD     64 - LOAD_CONST          24
                 00000100     3E - BINARY_LSHIFT       
                 00000101     5A - STORE_NAME          'MOD_ENRAGED'
                 00000104     64 - LOAD_CONST          14
                 00000107     64 - LOAD_CONST          24
                 0000010A     3E - BINARY_LSHIFT       
                 0000010B     5A - STORE_NAME          'MOD_BLOCK'
                 0000010E     64 - LOAD_CONST          1
                 00000111     64 - LOAD_CONST          24
                 00000114     3E - BINARY_LSHIFT       
                 00000115     5A - STORE_NAME          'MOD_FLAG_DISABLE_FIRING_INTO_MELEE_PENALTY'
                 00000118     64 - LOAD_CONST          2
                 0000011B     64 - LOAD_CONST          24
                 0000011E     3E - BINARY_LSHIFT       
                 0000011F     5A - STORE_NAME          'MOD_FLAG_DISABLE_MELEE_AT_RANGED_PENALTY'
                 00000122     64 - LOAD_CONST          3
                 00000125     64 - LOAD_CONST          24
                 00000128     3E - BINARY_LSHIFT       
                 00000129     5A - STORE_NAME          'MOD_FLAG_DISABLE_MULTI_ON_ONE_PENALTY'
                 0000012C     64 - LOAD_CONST          4
                 0000012F     64 - LOAD_CONST          24
                 00000132     3E - BINARY_LSHIFT       
                 00000133     5A - STORE_NAME          'MOD_FLAG_DISABLE_DISABLE_FAILED_WITHDRAW_PENALTY'
                 00000136     64 - LOAD_CONST          5
                 00000139     64 - LOAD_CONST          24
                 0000013C     3E - BINARY_LSHIFT       
                 0000013D     5A - STORE_NAME          'MOD_FLAG_DISABLE_FIRING_AT_SHORT_RANGE_PENALTY'
                 00000140     64 - LOAD_CONST          6
                 00000143     64 - LOAD_CONST          24
                 00000146     3E - BINARY_LSHIFT       
                 00000147     5A - STORE_NAME          'MOD_FLAG_DISABLE_ABILITY_TO_WITHDRAW'
                 0000014A     64 - LOAD_CONST          None
                 0000014D     53 - RETURN_VALUE        
             consts:
0000016C         TUPLE: (
00000171             INT: -2 (FE FF FF FF),
00000176             INT: 1 (01 00 00 00),
0000017B             INT: 0 (00 00 00 00),
00000180             FLOAT: 30.0 (04 33 30 2E 30),
00000186             FLOAT: 60.0 (04 36 30 2E 30),
0000018C             INT: 5 (05 00 00 00),
00000191             INT: 10 (0A 00 00 00),
00000196             INT: 20 (14 00 00 00),
0000019B             INT: 30 (1E 00 00 00),
000001A0             INT: 60 (3C 00 00 00),
000001A5             INT: 29 (1D 00 00 00),
000001AA             INT: 2 (02 00 00 00),
000001AF             INT: 3 (03 00 00 00),
000001B4             INT: 4 (04 00 00 00),
000001B9             INT: 7 (07 00 00 00),
000001BE             INT: 24 (18 00 00 00),
000001C3             INT: 6 (06 00 00 00),
000001C8             INT: 8 (08 00 00 00),
000001CD             INT: 9 (09 00 00 00),
000001D2             INT: 11 (0B 00 00 00),
000001D7             INT: 12 (0C 00 00 00),
000001DC             INT: 13 (0D 00 00 00),
000001E1             INT: 14 (0E 00 00 00),
000001E6             None (4E)
                 )
             names:
000001E7         TUPLE: (
000001EC             STR: 'HYPERDODGED' (0B 00 00 00 48 59 50 45 52 44 4F 44 47 45 44),
000001FC             STR: 'SUCCESS_EQUIP_ITEM' (12 00 00 00 53 55 43 43 45 53 53 5F 45 51 55 49 50 5F 49 54 45 4D),
00000213             STR: 'NO_DAMAGE' (09 00 00 00 4E 4F 5F 44 41 4D 41 47 45),
00000221             STR: 'ThirtySecs' (0A 00 00 00 54 68 69 72 74 79 53 65 63 73),
00000230             STR: 'OneMin' (06 00 00 00 4F 6E 65 4D 69 6E),
0000023B             STR: 'FiveMins' (08 00 00 00 46 69 76 65 4D 69 6E 73),
00000248             STR: 'TenMins' (07 00 00 00 54 65 6E 4D 69 6E 73),
00000254             STR: 'TwentyMins' (0A 00 00 00 54 77 65 6E 74 79 4D 69 6E 73),
00000263             STR: 'ThirtyMins' (0A 00 00 00 54 68 69 72 74 79 4D 69 6E 73),
00000272             STR: 'SixtyMins' (09 00 00 00 53 69 78 74 79 4D 69 6E 73),
00000280             STR: 'MOD_AFFECTS_TOUGHNESS' (15 00 00 00 4D 4F 44 5F 41 46 46 45 43 54 53 5F 54 4F 55 47 48 4E 45 53 53),
0000029A             STR: 'MOD_AFFECTS_DAMAGE_BONUS' (18 00 00 00 4D 4F 44 5F 41 46 46 45 43 54 53 5F 44 41 4D 41 47 45 5F 42 4F 4E 55 53),
000002B7             STR: 'MOD_AFFECTS_ATTACKMOD' (15 00 00 00 4D 4F 44 5F 41 46 46 45 43 54 53 5F 41 54 54 41 43 4B 4D 4F 44),
000002D1             STR: 'MOD_AFFECTS_DEFENSEMOD' (16 00 00 00 4D 4F 44 5F 41 46 46 45 43 54 53 5F 44 45 46 45 4E 53 45 4D 4F 44),
000002EC             STR: 'MOD_COMBAT_FLAG_ENABLER' (17 00 00 00 4D 4F 44 5F 43 4F 4D 42 41 54 5F 46 4C 41 47 5F 45 4E 41 42 4C 45 52),
00000308             STR: 'MOD_RANGED' (0A 00 00 00 4D 4F 44 5F 52 41 4E 47 45 44),
00000317             STR: 'MOD_MELEE' (09 00 00 00 4D 4F 44 5F 4D 45 4C 45 45),
00000325             STR: 'MOD_GUNS' (08 00 00 00 4D 4F 44 5F 47 55 4E 53),
00000332             STR: 'MOD_PISTOL' (0A 00 00 00 4D 4F 44 5F 50 49 53 54 4F 4C),
00000341             STR: 'MOD_RIFLE' (09 00 00 00 4D 4F 44 5F 52 49 46 4C 45),
0000034F             STR: 'MOD_SUB_MACHINE_GUN' (13 00 00 00 4D 4F 44 5F 53 55 42 5F 4D 41 43 48 49 4E 45 5F 47 55 4E),
00000367             STR: 'MOD_DUAL_PISTOL' (0F 00 00 00 4D 4F 44 5F 44 55 41 4C 5F 50 49 53 54 4F 4C),
0000037B             STR: 'MOD_SPEED' (09 00 00 00 4D 4F 44 5F 53 50 45 45 44),
00000389             STR: 'MOD_POWER' (09 00 00 00 4D 4F 44 5F 50 4F 57 45 52),
00000397             STR: 'MOD_DEFENSE' (0B 00 00 00 4D 4F 44 5F 44 45 46 45 4E 53 45),
000003A7             STR: 'MOD_STUNNED' (0B 00 00 00 4D 4F 44 5F 53 54 55 4E 4E 45 44),
000003B7             STR: 'MOD_CONFUSED' (0C 00 00 00 4D 4F 44 5F 43 4F 4E 46 55 53 45 44),
000003C8             STR: 'MOD_ENRAGED' (0B 00 00 00 4D 4F 44 5F 45 4E 52 41 47 45 44),
000003D8             STR: 'MOD_BLOCK' (09 00 00 00 4D 4F 44 5F 42 4C 4F 43 4B),
000003E6             STR: 'MOD_FLAG_DISABLE_FIRING_INTO_MELEE_PENALTY' (2A 00 00 00 4D 4F 44 5F 46 4C 41 47 5F 44 49 53 41 42 4C 45 5F 46 49 52 49 4E 47 5F 49 4E 54 4F 5F 4D 45 4C 45 45 5F 50 45 4E 41 4C 54 59),
00000415             STR: 'MOD_FLAG_DISABLE_MELEE_AT_RANGED_PENALTY' (28 00 00 00 4D 4F 44 5F 46 4C 41 47 5F 44 49 53 41 42 4C 45 5F 4D 45 4C 45 45 5F 41 54 5F 52 41 4E 47 45 44 5F 50 45 4E 41 4C 54 59),
00000442             STR: 'MOD_FLAG_DISABLE_MULTI_ON_ONE_PENALTY' (25 00 00 00 4D 4F 44 5F 46 4C 41 47 5F 44 49 53 41 42 4C 45 5F 4D 55 4C 54 49 5F 4F 4E 5F 4F 4E 45 5F 50 45 4E 41 4C 54 59),
0000046C             STR: 'MOD_FLAG_DISABLE_DISABLE_FAILED_WITHDRAW_PENALTY' (30 00 00 00 4D 4F 44 5F 46 4C 41 47 5F 44 49 53 41 42 4C 45 5F 44 49 53 41 42 4C 45 5F 46 41 49 4C 45 44 5F 57 49 54 48 44 52 41 57 5F 50 45 4E 41 4C 54 59),
000004A1             STR: 'MOD_FLAG_DISABLE_FIRING_AT_SHORT_RANGE_PENALTY' (2E 00 00 00 4D 4F 44 5F 46 4C 41 47 5F 44 49 53 41 42 4C 45 5F 46 49 52 49 4E 47 5F 41 54 5F 53 48 4F 52 54 5F 52 41 4E 47 45 5F 50 45 4E 41 4C 54 59),
000004D4             STR: 'MOD_FLAG_DISABLE_ABILITY_TO_WITHDRAW' (24 00 00 00 4D 4F 44 5F 46 4C 41 47 5F 44 49 53 41 42 4C 45 5F 41 42 49 4C 49 54 59 5F 54 4F 5F 57 49 54 48 44 52 41 57)
                 )
             varnames:
000004FD         TUPLE: (
00000502             STR: 'FiveMins' (08 00 00 00 46 69 76 65 4D 69 6E 73),
0000050F             STR: 'MOD_GUNS' (08 00 00 00 4D 4F 44 5F 47 55 4E 53),
0000051C             STR: 'MOD_DUAL_PISTOL' (0F 00 00 00 4D 4F 44 5F 44 55 41 4C 5F 50 49 53 54 4F 4C),
00000530             STR: 'MOD_FLAG_DISABLE_DISABLE_FAILED_WITHDRAW_PENALTY' (30 00 00 00 4D 4F 44 5F 46 4C 41 47 5F 44 49 53 41 42 4C 45 5F 44 49 53 41 42 4C 45 5F 46 41 49 4C 45 44 5F 57 49 54 48 44 52 41 57 5F 50 45 4E 41 4C 54 59),
00000565             STR: 'MOD_FLAG_DISABLE_MELEE_AT_RANGED_PENALTY' (28 00 00 00 4D 4F 44 5F 46 4C 41 47 5F 44 49 53 41 42 4C 45 5F 4D 45 4C 45 45 5F 41 54 5F 52 41 4E 47 45 44 5F 50 45 4E 41 4C 54 59),
00000592             STR: 'MOD_FLAG_DISABLE_FIRING_AT_SHORT_RANGE_PENALTY' (2E 00 00 00 4D 4F 44 5F 46 4C 41 47 5F 44 49 53 41 42 4C 45 5F 46 49 52 49 4E 47 5F 41 54 5F 53 48 4F 52 54 5F 52 41 4E 47 45 5F 50 45 4E 41 4C 54 59),
000005C5             STR: 'ThirtySecs' (0A 00 00 00 54 68 69 72 74 79 53 65 63 73),
000005D4             STR: 'MOD_COMBAT_FLAG_ENABLER' (17 00 00 00 4D 4F 44 5F 43 4F 4D 42 41 54 5F 46 4C 41 47 5F 45 4E 41 42 4C 45 52),
000005F0             STR: 'MOD_RIFLE' (09 00 00 00 4D 4F 44 5F 52 49 46 4C 45),
000005FE             STR: 'MOD_ENRAGED' (0B 00 00 00 4D 4F 44 5F 45 4E 52 41 47 45 44),
0000060E             STR: 'MOD_CONFUSED' (0C 00 00 00 4D 4F 44 5F 43 4F 4E 46 55 53 45 44),
0000061F             STR: 'MOD_PISTOL' (0A 00 00 00 4D 4F 44 5F 50 49 53 54 4F 4C),
0000062E             STR: 'ThirtyMins' (0A 00 00 00 54 68 69 72 74 79 4D 69 6E 73),
0000063D             STR: 'MOD_DEFENSE' (0B 00 00 00 4D 4F 44 5F 44 45 46 45 4E 53 45),
0000064D             STR: 'MOD_POWER' (09 00 00 00 4D 4F 44 5F 50 4F 57 45 52),
0000065B             STR: 'TenMins' (07 00 00 00 54 65 6E 4D 69 6E 73),
00000667             STR: 'MOD_RANGED' (0A 00 00 00 4D 4F 44 5F 52 41 4E 47 45 44),
00000676             STR: 'HYPERDODGED' (0B 00 00 00 48 59 50 45 52 44 4F 44 47 45 44),
00000686             STR: 'SixtyMins' (09 00 00 00 53 69 78 74 79 4D 69 6E 73),
00000694             STR: 'MOD_FLAG_DISABLE_MULTI_ON_ONE_PENALTY' (25 00 00 00 4D 4F 44 5F 46 4C 41 47 5F 44 49 53 41 42 4C 45 5F 4D 55 4C 54 49 5F 4F 4E 5F 4F 4E 45 5F 50 45 4E 41 4C 54 59),
000006BE             STR: 'SUCCESS_EQUIP_ITEM' (12 00 00 00 53 55 43 43 45 53 53 5F 45 51 55 49 50 5F 49 54 45 4D),
000006D5             STR: 'MOD_FLAG_DISABLE_ABILITY_TO_WITHDRAW' (24 00 00 00 4D 4F 44 5F 46 4C 41 47 5F 44 49 53 41 42 4C 45 5F 41 42 49 4C 49 54 59 5F 54 4F 5F 57 49 54 48 44 52 41 57),
000006FE             STR: 'MOD_AFFECTS_TOUGHNESS' (15 00 00 00 4D 4F 44 5F 41 46 46 45 43 54 53 5F 54 4F 55 47 48 4E 45 53 53),
00000718             STR: 'NO_DAMAGE' (09 00 00 00 4E 4F 5F 44 41 4D 41 47 45),
00000726             STR: 'MOD_STUNNED' (0B 00 00 00 4D 4F 44 5F 53 54 55 4E 4E 45 44),
00000736             STR: 'MOD_MELEE' (09 00 00 00 4D 4F 44 5F 4D 45 4C 45 45),
00000744             STR: 'MOD_AFFECTS_DAMAGE_BONUS' (18 00 00 00 4D 4F 44 5F 41 46 46 45 43 54 53 5F 44 41 4D 41 47 45 5F 42 4F 4E 55 53),
00000761             STR: 'MOD_AFFECTS_DEFENSEMOD' (16 00 00 00 4D 4F 44 5F 41 46 46 45 43 54 53 5F 44 45 46 45 4E 53 45 4D 4F 44),
0000077C             STR: 'MOD_AFFECTS_ATTACKMOD' (15 00 00 00 4D 4F 44 5F 41 46 46 45 43 54 53 5F 41 54 54 41 43 4B 4D 4F 44),
00000796             STR: 'TwentyMins' (0A 00 00 00 54 77 65 6E 74 79 4D 69 6E 73),
000007A5             STR: 'MOD_FLAG_DISABLE_FIRING_INTO_MELEE_PENALTY' (2A 00 00 00 4D 4F 44 5F 46 4C 41 47 5F 44 49 53 41 42 4C 45 5F 46 49 52 49 4E 47 5F 49 4E 54 4F 5F 4D 45 4C 45 45 5F 50 45 4E 41 4C 54 59),
000007D4             STR: 'MOD_SUB_MACHINE_GUN' (13 00 00 00 4D 4F 44 5F 53 55 42 5F 4D 41 43 48 49 4E 45 5F 47 55 4E),
000007EC             STR: 'MOD_SPEED' (09 00 00 00 4D 4F 44 5F 53 50 45 45 44),
000007FA             STR: 'MOD_BLOCK' (09 00 00 00 4D 4F 44 5F 42 4C 4F 43 4B),
00000808             STR: 'OneMin' (06 00 00 00 4F 6E 65 4D 69 6E)
                 )
             freevars:
00000813         TUPLE: ()
             cellvars:
00000818         TUPLE: ()
             filename:
0000081D         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\defines.py' (47 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 64 65 66 69 6E 65 73 2E 70 79)
             name:
00000869         STR: '?' (01 00 00 00 3F)
             firslineno:
0000086F         LONG: 2L (02 00 00 00)
             lnotab:
00000873         STR: '\x06\x03\x06\x03\x06\x01\x06\x01\x06\x01\n\x01\n\x01\n\x01\n\x01\n\x04\n\x01\n\x01\n\x01\n\x01\n\x03\n\x01\n\x01\n\x01\n\x01\n\x01\n\x01\n\x01\n\x01\n\x01\n\x01\n\x01\n\x01\n\x01\n\x03\n\x01\n\x01\n\x01\n\x01\n\x01' (44 00 00 00 06 03 06 03 06 01 06 01 06 01 0A 01 0A 01 0A 01 0A 01 0A 04 0A 01 0A 01 0A 01 0A 01 0A 03 0A 01 0A 01 0A 01 0A 01 0A 01 0A 01 0A 01 0A 01 0A 01 0A 01 0A 01 0A 01 0A 01 0A 03 0A 01 0A 01 0A 01 0A 01 0A 01)

