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
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00d\x00\x00k\x01\x00Z\x01\x00d\x00\x00k\x02\x00Z\x02\x00d\x00\x00k\x03\x00Z\x04\x00d\x00\x00k\x05\x00Z\x06\x00d\x00\x00k\x07\x00i\x08\x00Z\t\x00d\x00\x00k\n\x00Z\x0b\x00d\x00\x00k\x0c\x00Z\r\x00d\x01\x00k\x0e\x00Td\x02\x00Z\x0f\x00d\x03\x00Z\x10\x00d\x04\x00Z\x11\x00d\x05\x00Z\x12\x00e\r\x00i\x13\x00Z\x14\x00e\r\x00i\x15\x00Z\x16\x00e\r\x00i\x17\x00Z\x18\x00e\r\x00i\x19\x00Z\x1a\x00d\x06\x00\x84\x00\x00Z\x1b\x00d\x07\x00\x84\x00\x00Z\x1c\x00d\x08\x00\x84\x00\x00Z\x1d\x00d\t\x00e\x1d\x00_\x1e\x00d\n\x00\x84\x00\x00Z\x1f\x00d\x0b\x00\x84\x00\x00Z \x00d\t\x00e \x00_\x1e\x00d\x0c\x00\x84\x00\x00Z!\x00d\r\x00\x84\x00\x00Z"\x00d\x00\x00S' (E3 00 00 00 64 00 00 6B 00 00 5A 00 00 64 00 00 6B 01 00 5A 01 00 64 00 00 6B 02 00 5A 02 00 64 00 00 6B 03 00 5A 04 00 64 00 00 6B 05 00 5A 06 00 64 00 00 6B 07 00 69 08 00 5A 09 00 64 00 00 6B 0A 00 5A 0B 00 64 00 00 6B 0C 00 5A 0D 00 64 01 00 6B 0E 00 54 64 02 00 5A 0F 00 64 03 00 5A 10 00 64 04 00 5A 11 00 64 05 00 5A 12 00 65 0D 00 69 13 00 5A 14 00 65 0D 00 69 15 00 5A 16 00 65 0D 00 69 17 00 5A 18 00 65 0D 00 69 19 00 5A 1A 00 64 06 00 84 00 00 5A 1B 00 64 07 00 84 00 00 5A 1C 00 64 08 00 84 00 00 5A 1D 00 64 09 00 65 1D 00 5F 1E 00 64 0A 00 84 00 00 5A 1F 00 64 0B 00 84 00 00 5A 20 00 64 09 00 65 20 00 5F 1E 00 64 0C 00 84 00 00 5A 21 00 64 0D 00 84 00 00 5A 22 00 64 00 00 53)
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
                 0000001E     6B - IMPORT_NAME         'missionvalidate'
                 00000021     5A - STORE_NAME          'mv'
                 00000024     64 - LOAD_CONST          None
                 00000027     6B - IMPORT_NAME         'combatvalidate'
                 0000002A     5A - STORE_NAME          'cv'
                 0000002D     64 - LOAD_CONST          None
                 00000030     6B - IMPORT_NAME         'ability.utility'
                 00000033     69 - LOAD_ATTR           'utility'
                 00000036     5A - STORE_NAME          'Utility'
                 00000039     64 - LOAD_CONST          None
                 0000003C     6B - IMPORT_NAME         'stringtable_client'
                 0000003F     5A - STORE_NAME          'StringTable'
                 00000042     64 - LOAD_CONST          None
                 00000045     6B - IMPORT_NAME         'ltfxmap'
                 00000048     5A - STORE_NAME          'FX'
                 0000004B     64 - LOAD_CONST          ('*')
                 0000004E     6B - IMPORT_NAME         'ability.defines'
                 00000051     54 - IMPORT_STAR         
                 00000052     64 - LOAD_CONST          30
                 00000055     5A - STORE_NAME          'NEGATIVE_COND_TIME'
                 00000058     64 - LOAD_CONST          25
                 0000005B     5A - STORE_NAME          'NEGATIVE_COND_1_REMOVE_PERCENTS'
                 0000005E     64 - LOAD_CONST          50
                 00000061     5A - STORE_NAME          'NEGATIVE_COND_2_REMOVE_PERCENTS'
                 00000064     64 - LOAD_CONST          75
                 00000067     5A - STORE_NAME          'NEGATIVE_COND_3_REMOVE_PERCENTS'
                 0000006A     65 - LOAD_NAME           'FX'
                 0000006D     69 - LOAD_ATTR           'FX_CHARACTER_RECALL_MISSION_TEAM_PHASE_OUT'
                 00000070     5A - STORE_NAME          'RECALL_TEAM_FX'
                 00000073     65 - LOAD_NAME           'FX'
                 00000076     69 - LOAD_ATTR           'FX_CHARACTER_RECALL_TEAM_MEMBER_PHASE_OUT'
                 00000079     5A - STORE_NAME          'RECALL_TEAMMEMBER_FX'
                 0000007C     65 - LOAD_NAME           'FX'
                 0000007F     69 - LOAD_ATTR           'FX_CHARACTER_RECALL_MISSION_TEAM_CAST'
                 00000082     5A - STORE_NAME          'RECALL_TEAM_CASTER_FX'
                 00000085     65 - LOAD_NAME           'FX'
                 00000088     69 - LOAD_ATTR           'FX_CHARACTER_RECALL_TEAM_MEMBER_CAST'
                 0000008B     5A - STORE_NAME          'RECALL_TEAM_MEMBER_CASTER_FX'
                 0000008E     64 - LOAD_CONST          CODE('RecallTeamMember_DirectObject')
                 00000091     84 - MAKE_FUNCTION       r0000
                 00000094     5A - STORE_NAME          'RecallTeamMember_DirectObject'
                 00000097     64 - LOAD_CONST          CODE('RecallTeamMember_Subject')
                 0000009A     84 - MAKE_FUNCTION       r0000
                 0000009D     5A - STORE_NAME          'RecallTeamMember_Subject'
                 000000A0     64 - LOAD_CONST          CODE('RecallTeamMember_Test')
                 000000A3     84 - MAKE_FUNCTION       r0000
                 000000A6     5A - STORE_NAME          'RecallTeamMember_Test'
                 000000A9     64 - LOAD_CONST          '\n'
                 000000AC     65 - LOAD_NAME           'RecallTeamMember_Test'
                 000000AF     5F - STORE_ATTR          'depAttr'
                 000000B2     64 - LOAD_CONST          CODE('RecallMissionTeam_DirectObject')
                 000000B5     84 - MAKE_FUNCTION       r0000
                 000000B8     5A - STORE_NAME          'RecallMissionTeam_DirectObject'
                 000000BB     64 - LOAD_CONST          CODE('RecallMissionTeam_Test')
                 000000BE     84 - MAKE_FUNCTION       r0000
                 000000C1     5A - STORE_NAME          'RecallMissionTeam_Test'
                 000000C4     64 - LOAD_CONST          '\n'
                 000000C7     65 - LOAD_NAME           'RecallMissionTeam_Test'
                 000000CA     5F - STORE_ATTR          'depAttr'
                 000000CD     64 - LOAD_CONST          CODE('EngageFoes_DirectObject')
                 000000D0     84 - MAKE_FUNCTION       r0000
                 000000D3     5A - STORE_NAME          'EngageFoes_DirectObject'
                 000000D6     64 - LOAD_CONST          CODE('DownloadMissionMap_Deactivate')
                 000000D9     84 - MAKE_FUNCTION       r0000
                 000000DC     5A - STORE_NAME          'DownloadMissionMap_Deactivate'
                 000000DF     64 - LOAD_CONST          None
                 000000E2     53 - RETURN_VALUE        
             consts:
00000101         TUPLE: (
00000106             None (4E),
00000107             TUPLE: (
0000010C                 STR: '*' (01 00 00 00 2A)
                     ),
00000112             INT: 30 (1E 00 00 00),
00000117             INT: 25 (19 00 00 00),
0000011C             INT: 50 (32 00 00 00),
00000121             INT: 75 (4B 00 00 00),
00000126             CODE:
                         argcount:
00000127                     LONG: 2L (02 00 00 00)
                         nlocals:
0000012B                     LONG: 2L (02 00 00 00)
                         stacksize:
0000012F                     LONG: 5L (05 00 00 00)
                         flags:
00000133                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000137                     STR: 't\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01t\x00\x00i\x01\x00d\x02\x00|\x01\x00i\x03\x00|\x00\x00i\x05\x00i\x06\x00\x83\x00\x00f\x02\x00\x16\x83\x01\x00\x01|\x01\x00i\x03\x00t\x07\x00i\x08\x00j\x03\x00p\r\x00\x01|\x00\x00i\x05\x00i\t\x00\x83\x00\x00o\x1e\x00\x01t\x00\x00i\n\x00t\x0b\x00i\x0c\x00t\r\x00|\x01\x00\x83\x03\x00\x01d\x00\x00Sn\x01\x00\x01|\x00\x00i\x0e\x00i\x0f\x00o\x1e\x00\x01t\x00\x00i\n\x00t\x0b\x00i\x10\x00t\r\x00|\x01\x00\x83\x03\x00\x01d\x00\x00Sn\x01\x00\x01|\x00\x00i\x11\x00o\x1e\x00\x01t\x00\x00i\n\x00t\x0b\x00i\x12\x00t\r\x00|\x01\x00\x83\x03\x00\x01d\x00\x00Sn\x01\x00\x01t\x13\x00i\x14\x00|\x00\x00i\x15\x00|\x00\x00i\x15\x00t\x16\x00d\x03\x00\x83\x04\x00\x01|\x00\x00i\x05\x00i\x17\x00|\x01\x00i\x03\x00|\x01\x00i\x18\x00\x83\x02\x00\x01d\x00\x00S' (FD 00 00 00 74 00 00 69 01 00 64 01 00 83 01 00 01 74 00 00 69 01 00 64 02 00 7C 01 00 69 03 00 7C 00 00 69 05 00 69 06 00 83 00 00 66 02 00 16 83 01 00 01 7C 01 00 69 03 00 74 07 00 69 08 00 6A 03 00 70 0D 00 01 7C 00 00 69 05 00 69 09 00 83 00 00 6F 1E 00 01 74 00 00 69 0A 00 74 0B 00 69 0C 00 74 0D 00 7C 01 00 83 03 00 01 64 00 00 53 6E 01 00 01 7C 00 00 69 0E 00 69 0F 00 6F 1E 00 01 74 00 00 69 0A 00 74 0B 00 69 10 00 74 0D 00 7C 01 00 83 03 00 01 64 00 00 53 6E 01 00 01 7C 00 00 69 11 00 6F 1E 00 01 74 00 00 69 0A 00 74 0B 00 69 12 00 74 0D 00 7C 01 00 83 03 00 01 64 00 00 53 6E 01 00 01 74 13 00 69 14 00 7C 00 00 69 15 00 7C 00 00 69 15 00 74 16 00 64 03 00 83 04 00 01 7C 00 00 69 05 00 69 17 00 7C 01 00 69 03 00 7C 01 00 69 18 00 83 02 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'RecallTeamMember_DirectObject: Recalling team member'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     01 - POP_TOP             
                             0000000D     74 - LOAD_GLOBAL         'Utility'
                             00000010     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000013     64 - LOAD_CONST          'Result: %d, current construct: %d'
                             00000016     7C - LOAD_FAST           'msg'
                             00000019     69 - LOAD_ATTR           'result'
                             0000001C     7C - LOAD_FAST           'subject'
                             0000001F     69 - LOAD_ATTR           'CharMvt'
                             00000022     69 - LOAD_ATTR           'getCurrentConstructID'
                             00000025     83 - CALL_FUNCTION       r0000
                             00000028     66 - BUILD_TUPLE         r0002
                             0000002B     16 - BINARY_MODULO       
                             0000002C     83 - CALL_FUNCTION       r0001
                             0000002F     01 - POP_TOP             
                             00000030     7C - LOAD_FAST           'msg'
                             00000033     69 - LOAD_ATTR           'result'
                             00000036     74 - LOAD_GLOBAL         'consolevar'
                             00000039     69 - LOAD_ATTR           'ConID'
                             0000003C     6A - COMPARE_OP          "!="
                             0000003F     70 - JUMP_IF_TRUE        -> 0000004F
                             00000042     01 - POP_TOP             
                             00000043     7C - LOAD_FAST           'subject'
                             00000046     69 - LOAD_ATTR           'CharMvt'
                             00000049     69 - LOAD_ATTR           'isInLoadingArea'
                             0000004C     83 - CALL_FUNCTION       r0000
                             0000004F     6F - JUMP_IF_FALSE       -> 00000070
                             00000052     01 - POP_TOP             
                             00000053     74 - LOAD_GLOBAL         'Utility'
                             00000056     69 - LOAD_ATTR           'SendAbilityOutputToCasterMsg'
                             00000059     74 - LOAD_GLOBAL         'StringTable'
                             0000005C     69 - LOAD_ATTR           'ID_CLIENT_RECALL_ACROSS_CONSTRUCTS'
                             0000005F     74 - LOAD_GLOBAL         'RecallTeamMemberAbility'
                             00000062     7C - LOAD_FAST           'msg'
                             00000065     83 - CALL_FUNCTION       r0003
                             00000068     01 - POP_TOP             
                             00000069     64 - LOAD_CONST          None
                             0000006C     53 - RETURN_VALUE        
                             0000006D     6E - JUMP_FORWARD        -> 00000071
                             00000070     01 - POP_TOP             
                             00000071     7C - LOAD_FAST           'subject'
                             00000074     69 - LOAD_ATTR           'Interlock'
                             00000077     69 - LOAD_ATTR           'IsInCombat'
                             0000007A     6F - JUMP_IF_FALSE       -> 0000009B
                             0000007D     01 - POP_TOP             
                             0000007E     74 - LOAD_GLOBAL         'Utility'
                             00000081     69 - LOAD_ATTR           'SendAbilityOutputToCasterMsg'
                             00000084     74 - LOAD_GLOBAL         'StringTable'
                             00000087     69 - LOAD_ATTR           'ID_CLIENT_TELEPORTING_INCOMBAT'
                             0000008A     74 - LOAD_GLOBAL         'RecallTeamMemberAbility'
                             0000008D     7C - LOAD_FAST           'msg'
                             00000090     83 - CALL_FUNCTION       r0003
                             00000093     01 - POP_TOP             
                             00000094     64 - LOAD_CONST          None
                             00000097     53 - RETURN_VALUE        
                             00000098     6E - JUMP_FORWARD        -> 0000009C
                             0000009B     01 - POP_TOP             
                             0000009C     7C - LOAD_FAST           'subject'
                             0000009F     69 - LOAD_ATTR           'IsDead'
                             000000A2     6F - JUMP_IF_FALSE       -> 000000C3
                             000000A5     01 - POP_TOP             
                             000000A6     74 - LOAD_GLOBAL         'Utility'
                             000000A9     69 - LOAD_ATTR           'SendAbilityOutputToCasterMsg'
                             000000AC     74 - LOAD_GLOBAL         'StringTable'
                             000000AF     69 - LOAD_ATTR           'ID_CLIENT_TELEPORTING_DEAD'
                             000000B2     74 - LOAD_GLOBAL         'RecallTeamMemberAbility'
                             000000B5     7C - LOAD_FAST           'msg'
                             000000B8     83 - CALL_FUNCTION       r0003
                             000000BB     01 - POP_TOP             
                             000000BC     64 - LOAD_CONST          None
                             000000BF     53 - RETURN_VALUE        
                             000000C0     6E - JUMP_FORWARD        -> 000000C4
                             000000C3     01 - POP_TOP             
                             000000C4     74 - LOAD_GLOBAL         'discovery'
                             000000C7     69 - LOAD_ATTR           'playEffect'
                             000000CA     7C - LOAD_FAST           'subject'
                             000000CD     69 - LOAD_ATTR           'locator'
                             000000D0     7C - LOAD_FAST           'subject'
                             000000D3     69 - LOAD_ATTR           'locator'
                             000000D6     74 - LOAD_GLOBAL         'RECALL_TEAMMEMBER_FX'
                             000000D9     64 - LOAD_CONST          0
                             000000DC     83 - CALL_FUNCTION       r0004
                             000000DF     01 - POP_TOP             
                             000000E0     7C - LOAD_FAST           'subject'
                             000000E3     69 - LOAD_ATTR           'CharMvt'
                             000000E6     69 - LOAD_ATTR           'realTeleport'
                             000000E9     7C - LOAD_FAST           'msg'
                             000000EC     69 - LOAD_ATTR           'result'
                             000000EF     7C - LOAD_FAST           'msg'
                             000000F2     69 - LOAD_ATTR           'location'
                             000000F5     83 - CALL_FUNCTION       r0002
                             000000F8     01 - POP_TOP             
                             000000F9     64 - LOAD_CONST          None
                             000000FC     53 - RETURN_VALUE        
                         consts:
00000239                     TUPLE: (
0000023E                         None (4E),
0000023F                         STR: 'RecallTeamMember_DirectObject: Recalling team member' (34 00 00 00 52 65 63 61 6C 6C 54 65 61 6D 4D 65 6D 62 65 72 5F 44 69 72 65 63 74 4F 62 6A 65 63 74 3A 20 52 65 63 61 6C 6C 69 6E 67 20 74 65 61 6D 20 6D 65 6D 62 65 72),
00000278                         STR: 'Result: %d, current construct: %d' (21 00 00 00 52 65 73 75 6C 74 3A 20 25 64 2C 20 63 75 72 72 65 6E 74 20 63 6F 6E 73 74 72 75 63 74 3A 20 25 64),
0000029E                         INT: 0 (00 00 00 00)
                             )
                         names:
000002A3                     TUPLE: (
000002A8                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000002B4                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
000002CB                         STR: 'msg' (03 00 00 00 6D 73 67),
000002D3                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
000002DE                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000002EA                         STR: 'CharMvt' (07 00 00 00 43 68 61 72 4D 76 74),
000002F6                         STR: 'getCurrentConstructID' (15 00 00 00 67 65 74 43 75 72 72 65 6E 74 43 6F 6E 73 74 72 75 63 74 49 44),
00000310                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
0000031F                         STR: 'ConID' (05 00 00 00 43 6F 6E 49 44),
00000329                         STR: 'isInLoadingArea' (0F 00 00 00 69 73 49 6E 4C 6F 61 64 69 6E 67 41 72 65 61),
0000033D                         STR: 'SendAbilityOutputToCasterMsg' (1C 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 43 61 73 74 65 72 4D 73 67),
0000035E                         STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
0000036E                         STR: 'ID_CLIENT_RECALL_ACROSS_CONSTRUCTS' (22 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 52 45 43 41 4C 4C 5F 41 43 52 4F 53 53 5F 43 4F 4E 53 54 52 55 43 54 53),
00000395                         STR: 'RecallTeamMemberAbility' (17 00 00 00 52 65 63 61 6C 6C 54 65 61 6D 4D 65 6D 62 65 72 41 62 69 6C 69 74 79),
000003B1                         STR: 'Interlock' (09 00 00 00 49 6E 74 65 72 6C 6F 63 6B),
000003BF                         STR: 'IsInCombat' (0A 00 00 00 49 73 49 6E 43 6F 6D 62 61 74),
000003CE                         STR: 'ID_CLIENT_TELEPORTING_INCOMBAT' (1E 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 54 45 4C 45 50 4F 52 54 49 4E 47 5F 49 4E 43 4F 4D 42 41 54),
000003F1                         STR: 'IsDead' (06 00 00 00 49 73 44 65 61 64),
000003FC                         STR: 'ID_CLIENT_TELEPORTING_DEAD' (1A 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 54 45 4C 45 50 4F 52 54 49 4E 47 5F 44 45 41 44),
0000041B                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
00000429                         STR: 'playEffect' (0A 00 00 00 70 6C 61 79 45 66 66 65 63 74),
00000438                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
00000444                         STR: 'RECALL_TEAMMEMBER_FX' (14 00 00 00 52 45 43 41 4C 4C 5F 54 45 41 4D 4D 45 4D 42 45 52 5F 46 58),
0000045D                         STR: 'realTeleport' (0C 00 00 00 72 65 61 6C 54 65 6C 65 70 6F 72 74),
0000046E                         STR: 'location' (08 00 00 00 6C 6F 63 61 74 69 6F 6E)
                             )
                         varnames:
0000047B                     TUPLE: (
00000480                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
0000048C                         STR: 'msg' (03 00 00 00 6D 73 67)
                             )
                         freevars:
00000494                     TUPLE: ()
                         cellvars:
00000499                     TUPLE: ()
                         filename:
0000049E                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\misc.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 6D 69 73 63 2E 70 79)
                         name:
000004EE                     STR: 'RecallTeamMember_DirectObject' (1D 00 00 00 52 65 63 61 6C 6C 54 65 61 6D 4D 65 6D 62 65 72 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000510                     LONG: 55L (37 00 00 00)
                         lnotab:
00000514                     STR: '\x00\x02\r\x01#\x01#\x01\x16\x01\x08\x01\r\x01\x16\x01\x08\x01\n\x01\x16\x01\x08\x04\x1c\x04' (1A 00 00 00 00 02 0D 01 23 01 23 01 16 01 08 01 0D 01 16 01 08 01 0A 01 16 01 08 04 1C 04),
00000533             CODE:
                         argcount:
00000534                     LONG: 2L (02 00 00 00)
                         nlocals:
00000538                     LONG: 2L (02 00 00 00)
                         stacksize:
0000053C                     LONG: 4L (04 00 00 00)
                         flags:
00000540                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000544                     STR: 't\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01t\x00\x00i\x02\x00t\x03\x00i\x04\x00t\x05\x00|\x01\x00\x83\x03\x00\x01t\x00\x00i\x07\x00t\x03\x00i\x08\x00t\x05\x00|\x01\x00\x83\x03\x00\x01d\x00\x00S' (3D 00 00 00 74 00 00 69 01 00 64 01 00 83 01 00 01 74 00 00 69 02 00 74 03 00 69 04 00 74 05 00 7C 01 00 83 03 00 01 74 00 00 69 07 00 74 03 00 69 08 00 74 05 00 7C 01 00 83 03 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'RecallTeamMember_Subject: Recalling team member'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     01 - POP_TOP             
                             0000000D     74 - LOAD_GLOBAL         'Utility'
                             00000010     69 - LOAD_ATTR           'SendAbilityOutputToCasterMsg'
                             00000013     74 - LOAD_GLOBAL         'StringTable'
                             00000016     69 - LOAD_ATTR           'ID_CLIENT_TELEPORTING_CASTER'
                             00000019     74 - LOAD_GLOBAL         'RecallTeamMemberAbility'
                             0000001C     7C - LOAD_FAST           'msg'
                             0000001F     83 - CALL_FUNCTION       r0003
                             00000022     01 - POP_TOP             
                             00000023     74 - LOAD_GLOBAL         'Utility'
                             00000026     69 - LOAD_ATTR           'SendAbilityOutputToTargetMsg'
                             00000029     74 - LOAD_GLOBAL         'StringTable'
                             0000002C     69 - LOAD_ATTR           'ID_CLIENT_TELEPORTING_TARGET'
                             0000002F     74 - LOAD_GLOBAL         'RecallTeamMemberAbility'
                             00000032     7C - LOAD_FAST           'msg'
                             00000035     83 - CALL_FUNCTION       r0003
                             00000038     01 - POP_TOP             
                             00000039     64 - LOAD_CONST          None
                             0000003C     53 - RETURN_VALUE        
                         consts:
00000586                     TUPLE: (
0000058B                         None (4E),
0000058C                         STR: 'RecallTeamMember_Subject: Recalling team member' (2F 00 00 00 52 65 63 61 6C 6C 54 65 61 6D 4D 65 6D 62 65 72 5F 53 75 62 6A 65 63 74 3A 20 52 65 63 61 6C 6C 69 6E 67 20 74 65 61 6D 20 6D 65 6D 62 65 72)
                             )
                         names:
000005C0                     TUPLE: (
000005C5                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
000005D1                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
000005E8                         STR: 'SendAbilityOutputToCasterMsg' (1C 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 43 61 73 74 65 72 4D 73 67),
00000609                         STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00000619                         STR: 'ID_CLIENT_TELEPORTING_CASTER' (1C 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 54 45 4C 45 50 4F 52 54 49 4E 47 5F 43 41 53 54 45 52),
0000063A                         STR: 'RecallTeamMemberAbility' (17 00 00 00 52 65 63 61 6C 6C 54 65 61 6D 4D 65 6D 62 65 72 41 62 69 6C 69 74 79),
00000656                         STR: 'msg' (03 00 00 00 6D 73 67),
0000065E                         STR: 'SendAbilityOutputToTargetMsg' (1C 00 00 00 53 65 6E 64 41 62 69 6C 69 74 79 4F 75 74 70 75 74 54 6F 54 61 72 67 65 74 4D 73 67),
0000067F                         STR: 'ID_CLIENT_TELEPORTING_TARGET' (1C 00 00 00 49 44 5F 43 4C 49 45 4E 54 5F 54 45 4C 45 50 4F 52 54 49 4E 47 5F 54 41 52 47 45 54)
                             )
                         varnames:
000006A0                     TUPLE: (
000006A5                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
000006B1                         STR: 'msg' (03 00 00 00 6D 73 67)
                             )
                         freevars:
000006B9                     TUPLE: ()
                         cellvars:
000006BE                     TUPLE: ()
                         filename:
000006C3                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\misc.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 6D 69 73 63 2E 70 79)
                         name:
00000713                     STR: 'RecallTeamMember_Subject' (18 00 00 00 52 65 63 61 6C 6C 54 65 61 6D 4D 65 6D 62 65 72 5F 53 75 62 6A 65 63 74)
                         firslineno:
00000730                     LONG: 77L (4D 00 00 00)
                         lnotab:
00000734                     STR: '\x00\x01\r\x03\x16\x01' (06 00 00 00 00 01 0D 03 16 01),
0000073F             CODE:
                         argcount:
00000740                     LONG: 1L (01 00 00 00)
                         nlocals:
00000744                     LONG: 1L (01 00 00 00)
                         stacksize:
00000748                     LONG: 4L (04 00 00 00)
                         flags:
0000074C                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000750                     STR: 't\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01|\x00\x00i\x03\x00i\x04\x00|\x00\x00i\x05\x00i\x04\x00j\x02\x00o\x15\x00\x01t\x00\x00i\x01\x00d\x02\x00\x83\x01\x00\x01d\x00\x00Sn\x01\x00\x01t\x06\x00i\x07\x00|\x00\x00_\x08\x00t\x00\x00i\x01\x00d\x03\x00|\x00\x00i\x08\x00|\x00\x00i\x03\x00i\t\x00i\n\x00\x83\x00\x00f\x02\x00\x16\x83\x01\x00\x01d\x00\x00S' (71 00 00 00 74 00 00 69 01 00 64 01 00 83 01 00 01 7C 00 00 69 03 00 69 04 00 7C 00 00 69 05 00 69 04 00 6A 02 00 6F 15 00 01 74 00 00 69 01 00 64 02 00 83 01 00 01 64 00 00 53 6E 01 00 01 74 06 00 69 07 00 7C 00 00 5F 08 00 74 00 00 69 01 00 64 03 00 7C 00 00 69 08 00 7C 00 00 69 03 00 69 09 00 69 0A 00 83 00 00 66 02 00 16 83 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'RecallTeamMember_test'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     01 - POP_TOP             
                             0000000D     7C - LOAD_FAST           'sentence'
                             00000010     69 - LOAD_ATTR           'subject'
                             00000013     69 - LOAD_ATTR           'locator'
                             00000016     7C - LOAD_FAST           'sentence'
                             00000019     69 - LOAD_ATTR           'directObject'
                             0000001C     69 - LOAD_ATTR           'locator'
                             0000001F     6A - COMPARE_OP          "=="
                             00000022     6F - JUMP_IF_FALSE       -> 0000003A
                             00000025     01 - POP_TOP             
                             00000026     74 - LOAD_GLOBAL         'Utility'
                             00000029     69 - LOAD_ATTR           'outputAbilityDebug'
                             0000002C     64 - LOAD_CONST          "Can't recall self"
                             0000002F     83 - CALL_FUNCTION       r0001
                             00000032     01 - POP_TOP             
                             00000033     64 - LOAD_CONST          None
                             00000036     53 - RETURN_VALUE        
                             00000037     6E - JUMP_FORWARD        -> 0000003B
                             0000003A     01 - POP_TOP             
                             0000003B     74 - LOAD_GLOBAL         'consolevar'
                             0000003E     69 - LOAD_ATTR           'ConID'
                             00000041     7C - LOAD_FAST           'sentence'
                             00000044     5F - STORE_ATTR          'result'
                             00000047     74 - LOAD_GLOBAL         'Utility'
                             0000004A     69 - LOAD_ATTR           'outputAbilityDebug'
                             0000004D     64 - LOAD_CONST          'Result: %d, current construct: %d'
                             00000050     7C - LOAD_FAST           'sentence'
                             00000053     69 - LOAD_ATTR           'result'
                             00000056     7C - LOAD_FAST           'sentence'
                             00000059     69 - LOAD_ATTR           'subject'
                             0000005C     69 - LOAD_ATTR           'CharMvt'
                             0000005F     69 - LOAD_ATTR           'getCurrentConstructID'
                             00000062     83 - CALL_FUNCTION       r0000
                             00000065     66 - BUILD_TUPLE         r0002
                             00000068     16 - BINARY_MODULO       
                             00000069     83 - CALL_FUNCTION       r0001
                             0000006C     01 - POP_TOP             
                             0000006D     64 - LOAD_CONST          None
                             00000070     53 - RETURN_VALUE        
                         consts:
000007C6                     TUPLE: (
000007CB                         None (4E),
000007CC                         STR: 'RecallTeamMember_test' (15 00 00 00 52 65 63 61 6C 6C 54 65 61 6D 4D 65 6D 62 65 72 5F 74 65 73 74),
000007E6                         STR: "Can't recall self" (11 00 00 00 43 61 6E 27 74 20 72 65 63 61 6C 6C 20 73 65 6C 66),
000007FC                         STR: 'Result: %d, current construct: %d' (21 00 00 00 52 65 73 75 6C 74 3A 20 25 64 2C 20 63 75 72 72 65 6E 74 20 63 6F 6E 73 74 72 75 63 74 3A 20 25 64)
                             )
                         names:
00000822                     TUPLE: (
00000827                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000833                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
0000084A                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65),
00000857                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000863                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
0000086F                         STR: 'directObject' (0C 00 00 00 64 69 72 65 63 74 4F 62 6A 65 63 74),
00000880                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
0000088F                         STR: 'ConID' (05 00 00 00 43 6F 6E 49 44),
00000899                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74),
000008A4                         STR: 'CharMvt' (07 00 00 00 43 68 61 72 4D 76 74),
000008B0                         STR: 'getCurrentConstructID' (15 00 00 00 67 65 74 43 75 72 72 65 6E 74 43 6F 6E 73 74 72 75 63 74 49 44)
                             )
                         varnames:
000008CA                     TUPLE: (
000008CF                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65)
                             )
                         freevars:
000008DC                     TUPLE: ()
                         cellvars:
000008E1                     TUPLE: ()
                         filename:
000008E6                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\misc.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 6D 69 73 63 2E 70 79)
                         name:
00000936                     STR: 'RecallTeamMember_Test' (15 00 00 00 52 65 63 61 6C 6C 54 65 61 6D 4D 65 6D 62 65 72 5F 54 65 73 74)
                         firslineno:
00000950                     LONG: 86L (56 00 00 00)
                         lnotab:
00000954                     STR: '\x00\x01\r\x02\x19\x01\r\x01\x08\x02\x0c\x01' (0C 00 00 00 00 01 0D 02 19 01 0D 01 08 02 0C 01),
00000965             STR: '\n' (01 00 00 00 0A),
0000096B             CODE:
                         argcount:
0000096C                     LONG: 2L (02 00 00 00)
                         nlocals:
00000970                     LONG: 2L (02 00 00 00)
                         stacksize:
00000974                     LONG: 3L (03 00 00 00)
                         flags:
00000978                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000097C                     STR: 't\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01|\x00\x00i\x03\x00|\x01\x00i\x05\x00j\x02\x00o\x08\x00\x01d\x00\x00Sn\x01\x00\x01t\x06\x00|\x00\x00|\x01\x00\x83\x02\x00\x01d\x00\x00S' (39 00 00 00 74 00 00 69 01 00 64 01 00 83 01 00 01 7C 00 00 69 03 00 7C 01 00 69 05 00 6A 02 00 6F 08 00 01 64 00 00 53 6E 01 00 01 74 06 00 7C 00 00 7C 01 00 83 02 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'RecallTeam_DirectObject: Recalling team member'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     01 - POP_TOP             
                             0000000D     7C - LOAD_FAST           'subject'
                             00000010     69 - LOAD_ATTR           'locator'
                             00000013     7C - LOAD_FAST           'msg'
                             00000016     69 - LOAD_ATTR           'subjectLocator'
                             00000019     6A - COMPARE_OP          "=="
                             0000001C     6F - JUMP_IF_FALSE       -> 00000027
                             0000001F     01 - POP_TOP             
                             00000020     64 - LOAD_CONST          None
                             00000023     53 - RETURN_VALUE        
                             00000024     6E - JUMP_FORWARD        -> 00000028
                             00000027     01 - POP_TOP             
                             00000028     74 - LOAD_GLOBAL         'RecallTeamMember_DirectObject'
                             0000002B     7C - LOAD_FAST           'subject'
                             0000002E     7C - LOAD_FAST           'msg'
                             00000031     83 - CALL_FUNCTION       r0002
                             00000034     01 - POP_TOP             
                             00000035     64 - LOAD_CONST          None
                             00000038     53 - RETURN_VALUE        
                         consts:
000009BA                     TUPLE: (
000009BF                         None (4E),
000009C0                         STR: 'RecallTeam_DirectObject: Recalling team member' (2E 00 00 00 52 65 63 61 6C 6C 54 65 61 6D 5F 44 69 72 65 63 74 4F 62 6A 65 63 74 3A 20 52 65 63 61 6C 6C 69 6E 67 20 74 65 61 6D 20 6D 65 6D 62 65 72)
                             )
                         names:
000009F3                     TUPLE: (
000009F8                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000A04                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000A1B                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000A27                         STR: 'locator' (07 00 00 00 6C 6F 63 61 74 6F 72),
00000A33                         STR: 'msg' (03 00 00 00 6D 73 67),
00000A3B                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72),
00000A4E                         STR: 'RecallTeamMember_DirectObject' (1D 00 00 00 52 65 63 61 6C 6C 54 65 61 6D 4D 65 6D 62 65 72 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                             )
                         varnames:
00000A70                     TUPLE: (
00000A75                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000A81                         STR: 'msg' (03 00 00 00 6D 73 67)
                             )
                         freevars:
00000A89                     TUPLE: ()
                         cellvars:
00000A8E                     TUPLE: ()
                         filename:
00000A93                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\misc.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 6D 69 73 63 2E 70 79)
                         name:
00000AE3                     STR: 'RecallMissionTeam_DirectObject' (1E 00 00 00 52 65 63 61 6C 6C 4D 69 73 73 69 6F 6E 54 65 61 6D 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000B06                     LONG: 103L (67 00 00 00)
                         lnotab:
00000B0A                     STR: '\x00\x01\r\x03\x13\x01\x08\x02' (08 00 00 00 00 01 0D 03 13 01 08 02),
00000B17             CODE:
                         argcount:
00000B18                     LONG: 1L (01 00 00 00)
                         nlocals:
00000B1C                     LONG: 1L (01 00 00 00)
                         stacksize:
00000B20                     LONG: 2L (02 00 00 00)
                         flags:
00000B24                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000B28                     STR: 't\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01t\x02\x00i\x03\x00|\x00\x00_\x05\x00d\x00\x00S' (1D 00 00 00 74 00 00 69 01 00 64 01 00 83 01 00 01 74 02 00 69 03 00 7C 00 00 5F 05 00 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'outputAbilityDebug'
                             00000006     64 - LOAD_CONST          'RecallMissionTeam_Test'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     01 - POP_TOP             
                             0000000D     74 - LOAD_GLOBAL         'consolevar'
                             00000010     69 - LOAD_ATTR           'ConID'
                             00000013     7C - LOAD_FAST           'sentence'
                             00000016     5F - STORE_ATTR          'result'
                             00000019     64 - LOAD_CONST          None
                             0000001C     53 - RETURN_VALUE        
                         consts:
00000B4A                     TUPLE: (
00000B4F                         None (4E),
00000B50                         STR: 'RecallMissionTeam_Test' (16 00 00 00 52 65 63 61 6C 6C 4D 69 73 73 69 6F 6E 54 65 61 6D 5F 54 65 73 74)
                             )
                         names:
00000B6B                     TUPLE: (
00000B70                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000B7C                         STR: 'outputAbilityDebug' (12 00 00 00 6F 75 74 70 75 74 41 62 69 6C 69 74 79 44 65 62 75 67),
00000B93                         STR: 'consolevar' (0A 00 00 00 63 6F 6E 73 6F 6C 65 76 61 72),
00000BA2                         STR: 'ConID' (05 00 00 00 43 6F 6E 49 44),
00000BAC                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65),
00000BB9                         STR: 'result' (06 00 00 00 72 65 73 75 6C 74)
                             )
                         varnames:
00000BC4                     TUPLE: (
00000BC9                         STR: 'sentence' (08 00 00 00 73 65 6E 74 65 6E 63 65)
                             )
                         freevars:
00000BD6                     TUPLE: ()
                         cellvars:
00000BDB                     TUPLE: ()
                         filename:
00000BE0                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\misc.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 6D 69 73 63 2E 70 79)
                         name:
00000C30                     STR: 'RecallMissionTeam_Test' (16 00 00 00 52 65 63 61 6C 6C 4D 69 73 73 69 6F 6E 54 65 61 6D 5F 54 65 73 74)
                         firslineno:
00000C4B                     LONG: 112L (70 00 00 00)
                         lnotab:
00000C4F                     STR: '\x00\x01\r\x01' (04 00 00 00 00 01 0D 01),
00000C58             CODE:
                         argcount:
00000C59                     LONG: 2L (02 00 00 00)
                         nlocals:
00000C5D                     LONG: 2L (02 00 00 00)
                         stacksize:
00000C61                     LONG: 2L (02 00 00 00)
                         flags:
00000C65                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000C69                     STR: 't\x00\x00i\x01\x00|\x00\x00\x83\x01\x00\x0co\x08\x00\x01d\x00\x00Sn\x01\x00\x01|\x00\x00i\x03\x00o\x17\x00\x01|\x00\x00i\x03\x00i\x04\x00|\x01\x00i\x06\x00\x83\x01\x00\x01n\x01\x00\x01d\x00\x00S' (3E 00 00 00 74 00 00 69 01 00 7C 00 00 83 01 00 0C 6F 08 00 01 64 00 00 53 6E 01 00 01 7C 00 00 69 03 00 6F 17 00 01 7C 00 00 69 03 00 69 04 00 7C 01 00 69 06 00 83 01 00 01 6E 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'Utility'
                             00000003     69 - LOAD_ATTR           'IsAnNPC'
                             00000006     7C - LOAD_FAST           'subject'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     0C - UNARY_NOT           
                             0000000D     6F - JUMP_IF_FALSE       -> 00000018
                             00000010     01 - POP_TOP             
                             00000011     64 - LOAD_CONST          None
                             00000014     53 - RETURN_VALUE        
                             00000015     6E - JUMP_FORWARD        -> 00000019
                             00000018     01 - POP_TOP             
                             00000019     7C - LOAD_FAST           'subject'
                             0000001C     69 - LOAD_ATTR           'AI'
                             0000001F     6F - JUMP_IF_FALSE       -> 00000039
                             00000022     01 - POP_TOP             
                             00000023     7C - LOAD_FAST           'subject'
                             00000026     69 - LOAD_ATTR           'AI'
                             00000029     69 - LOAD_ATTR           'setMostHated'
                             0000002C     7C - LOAD_FAST           'msg'
                             0000002F     69 - LOAD_ATTR           'subjectLocator'
                             00000032     83 - CALL_FUNCTION       r0001
                             00000035     01 - POP_TOP             
                             00000036     6E - JUMP_FORWARD        -> 0000003A
                             00000039     01 - POP_TOP             
                             0000003A     64 - LOAD_CONST          None
                             0000003D     53 - RETURN_VALUE        
                         consts:
00000CAC                     TUPLE: (
00000CB1                         None (4E)
                             )
                         names:
00000CB2                     TUPLE: (
00000CB7                         STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000CC3                         STR: 'IsAnNPC' (07 00 00 00 49 73 41 6E 4E 50 43),
00000CCF                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000CDB                         STR: 'AI' (02 00 00 00 41 49),
00000CE2                         STR: 'setMostHated' (0C 00 00 00 73 65 74 4D 6F 73 74 48 61 74 65 64),
00000CF3                         STR: 'msg' (03 00 00 00 6D 73 67),
00000CFB                         STR: 'subjectLocator' (0E 00 00 00 73 75 62 6A 65 63 74 4C 6F 63 61 74 6F 72)
                             )
                         varnames:
00000D0E                     TUPLE: (
00000D13                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000D1F                         STR: 'msg' (03 00 00 00 6D 73 67)
                             )
                         freevars:
00000D27                     TUPLE: ()
                         cellvars:
00000D2C                     TUPLE: ()
                         filename:
00000D31                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\misc.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 6D 69 73 63 2E 70 79)
                         name:
00000D81                     STR: 'EngageFoes_DirectObject' (17 00 00 00 45 6E 67 61 67 65 46 6F 65 73 5F 44 69 72 65 63 74 4F 62 6A 65 63 74)
                         firslineno:
00000D9D                     LONG: 122L (7A 00 00 00)
                         lnotab:
00000DA1                     STR: '\x00\x01\x11\x01\x08\x02\n\x01' (08 00 00 00 00 01 11 01 08 02 0A 01),
00000DAE             CODE:
                         argcount:
00000DAF                     LONG: 1L (01 00 00 00)
                         nlocals:
00000DB3                     LONG: 1L (01 00 00 00)
                         stacksize:
00000DB7                     LONG: 1L (01 00 00 00)
                         flags:
00000DBB                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
00000DBF                     STR: '|\x00\x00i\x01\x00i\x02\x00\x83\x00\x00\x01d\x00\x00S' (11 00 00 00 7C 00 00 69 01 00 69 02 00 83 00 00 01 64 00 00 53)
                             00000000     7C - LOAD_FAST           'subject'
                             00000003     69 - LOAD_ATTR           'MissionTeam'
                             00000006     69 - LOAD_ATTR           'disableMissionMap'
                             00000009     83 - CALL_FUNCTION       r0000
                             0000000C     01 - POP_TOP             
                             0000000D     64 - LOAD_CONST          None
                             00000010     53 - RETURN_VALUE        
                         consts:
00000DD5                     TUPLE: (
00000DDA                         None (4E)
                             )
                         names:
00000DDB                     TUPLE: (
00000DE0                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74),
00000DEC                         STR: 'MissionTeam' (0B 00 00 00 4D 69 73 73 69 6F 6E 54 65 61 6D),
00000DFC                         STR: 'disableMissionMap' (11 00 00 00 64 69 73 61 62 6C 65 4D 69 73 73 69 6F 6E 4D 61 70)
                             )
                         varnames:
00000E12                     TUPLE: (
00000E17                         STR: 'subject' (07 00 00 00 73 75 62 6A 65 63 74)
                             )
                         freevars:
00000E23                     TUPLE: ()
                         cellvars:
00000E28                     TUPLE: ()
                         filename:
00000E2D                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\misc.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 6D 69 73 63 2E 70 79)
                         name:
00000E7D                     STR: 'DownloadMissionMap_Deactivate' (1D 00 00 00 44 6F 77 6E 6C 6F 61 64 4D 69 73 73 69 6F 6E 4D 61 70 5F 44 65 61 63 74 69 76 61 74 65)
                         firslineno:
00000E9F                     LONG: 133L (85 00 00 00)
                         lnotab:
00000EA3                     STR: '\x00\x01' (02 00 00 00 00 01)
                 )
             names:
00000EAA         TUPLE: (
00000EAF             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00000EBA             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
00000EC8             STR: 'obj' (03 00 00 00 6F 62 6A),
00000ED0             STR: 'missionvalidate' (0F 00 00 00 6D 69 73 73 69 6F 6E 76 61 6C 69 64 61 74 65),
00000EE4             STR: 'mv' (02 00 00 00 6D 76),
00000EEB             STR: 'combatvalidate' (0E 00 00 00 63 6F 6D 62 61 74 76 61 6C 69 64 61 74 65),
00000EFE             STR: 'cv' (02 00 00 00 63 76),
00000F05             STR: 'ability.utility' (0F 00 00 00 61 62 69 6C 69 74 79 2E 75 74 69 6C 69 74 79),
00000F19             STR: 'utility' (07 00 00 00 75 74 69 6C 69 74 79),
00000F25             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79),
00000F31             STR: 'stringtable_client' (12 00 00 00 73 74 72 69 6E 67 74 61 62 6C 65 5F 63 6C 69 65 6E 74),
00000F48             STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00000F58             STR: 'ltfxmap' (07 00 00 00 6C 74 66 78 6D 61 70),
00000F64             STR: 'FX' (02 00 00 00 46 58),
00000F6B             STR: 'ability.defines' (0F 00 00 00 61 62 69 6C 69 74 79 2E 64 65 66 69 6E 65 73),
00000F7F             STR: 'NEGATIVE_COND_TIME' (12 00 00 00 4E 45 47 41 54 49 56 45 5F 43 4F 4E 44 5F 54 49 4D 45),
00000F96             STR: 'NEGATIVE_COND_1_REMOVE_PERCENTS' (1F 00 00 00 4E 45 47 41 54 49 56 45 5F 43 4F 4E 44 5F 31 5F 52 45 4D 4F 56 45 5F 50 45 52 43 45 4E 54 53),
00000FBA             STR: 'NEGATIVE_COND_2_REMOVE_PERCENTS' (1F 00 00 00 4E 45 47 41 54 49 56 45 5F 43 4F 4E 44 5F 32 5F 52 45 4D 4F 56 45 5F 50 45 52 43 45 4E 54 53),
00000FDE             STR: 'NEGATIVE_COND_3_REMOVE_PERCENTS' (1F 00 00 00 4E 45 47 41 54 49 56 45 5F 43 4F 4E 44 5F 33 5F 52 45 4D 4F 56 45 5F 50 45 52 43 45 4E 54 53),
00001002             STR: 'FX_CHARACTER_RECALL_MISSION_TEAM_PHASE_OUT' (2A 00 00 00 46 58 5F 43 48 41 52 41 43 54 45 52 5F 52 45 43 41 4C 4C 5F 4D 49 53 53 49 4F 4E 5F 54 45 41 4D 5F 50 48 41 53 45 5F 4F 55 54),
00001031             STR: 'RECALL_TEAM_FX' (0E 00 00 00 52 45 43 41 4C 4C 5F 54 45 41 4D 5F 46 58),
00001044             STR: 'FX_CHARACTER_RECALL_TEAM_MEMBER_PHASE_OUT' (29 00 00 00 46 58 5F 43 48 41 52 41 43 54 45 52 5F 52 45 43 41 4C 4C 5F 54 45 41 4D 5F 4D 45 4D 42 45 52 5F 50 48 41 53 45 5F 4F 55 54),
00001072             STR: 'RECALL_TEAMMEMBER_FX' (14 00 00 00 52 45 43 41 4C 4C 5F 54 45 41 4D 4D 45 4D 42 45 52 5F 46 58),
0000108B             STR: 'FX_CHARACTER_RECALL_MISSION_TEAM_CAST' (25 00 00 00 46 58 5F 43 48 41 52 41 43 54 45 52 5F 52 45 43 41 4C 4C 5F 4D 49 53 53 49 4F 4E 5F 54 45 41 4D 5F 43 41 53 54),
000010B5             STR: 'RECALL_TEAM_CASTER_FX' (15 00 00 00 52 45 43 41 4C 4C 5F 54 45 41 4D 5F 43 41 53 54 45 52 5F 46 58),
000010CF             STR: 'FX_CHARACTER_RECALL_TEAM_MEMBER_CAST' (24 00 00 00 46 58 5F 43 48 41 52 41 43 54 45 52 5F 52 45 43 41 4C 4C 5F 54 45 41 4D 5F 4D 45 4D 42 45 52 5F 43 41 53 54),
000010F8             STR: 'RECALL_TEAM_MEMBER_CASTER_FX' (1C 00 00 00 52 45 43 41 4C 4C 5F 54 45 41 4D 5F 4D 45 4D 42 45 52 5F 43 41 53 54 45 52 5F 46 58),
00001119             STR: 'RecallTeamMember_DirectObject' (1D 00 00 00 52 65 63 61 6C 6C 54 65 61 6D 4D 65 6D 62 65 72 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
0000113B             STR: 'RecallTeamMember_Subject' (18 00 00 00 52 65 63 61 6C 6C 54 65 61 6D 4D 65 6D 62 65 72 5F 53 75 62 6A 65 63 74),
00001158             STR: 'RecallTeamMember_Test' (15 00 00 00 52 65 63 61 6C 6C 54 65 61 6D 4D 65 6D 62 65 72 5F 54 65 73 74),
00001172             STR: 'depAttr' (07 00 00 00 64 65 70 41 74 74 72),
0000117E             STR: 'RecallMissionTeam_DirectObject' (1E 00 00 00 52 65 63 61 6C 6C 4D 69 73 73 69 6F 6E 54 65 61 6D 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
000011A1             STR: 'RecallMissionTeam_Test' (16 00 00 00 52 65 63 61 6C 6C 4D 69 73 73 69 6F 6E 54 65 61 6D 5F 54 65 73 74),
000011BC             STR: 'EngageFoes_DirectObject' (17 00 00 00 45 6E 67 61 67 65 46 6F 65 73 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
000011D8             STR: 'DownloadMissionMap_Deactivate' (1D 00 00 00 44 6F 77 6E 6C 6F 61 64 4D 69 73 73 69 6F 6E 4D 61 70 5F 44 65 61 63 74 69 76 61 74 65)
                 )
             varnames:
000011FA         TUPLE: (
000011FF             STR: 'FX' (02 00 00 00 46 58),
00001206             STR: 'StringTable' (0B 00 00 00 53 74 72 69 6E 67 54 61 62 6C 65),
00001216             STR: 'random' (06 00 00 00 72 61 6E 64 6F 6D),
00001221             STR: 'RECALL_TEAMMEMBER_FX' (14 00 00 00 52 45 43 41 4C 4C 5F 54 45 41 4D 4D 45 4D 42 45 52 5F 46 58),
0000123A             STR: 'cv' (02 00 00 00 63 76),
00001241             STR: 'RecallMissionTeam_DirectObject' (1E 00 00 00 52 65 63 61 6C 6C 4D 69 73 73 69 6F 6E 54 65 61 6D 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001264             STR: 'RecallTeamMember_DirectObject' (1D 00 00 00 52 65 63 61 6C 6C 54 65 61 6D 4D 65 6D 62 65 72 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001286             STR: 'NEGATIVE_COND_1_REMOVE_PERCENTS' (1F 00 00 00 4E 45 47 41 54 49 56 45 5F 43 4F 4E 44 5F 31 5F 52 45 4D 4F 56 45 5F 50 45 52 43 45 4E 54 53),
000012AA             STR: 'RECALL_TEAM_CASTER_FX' (15 00 00 00 52 45 43 41 4C 4C 5F 54 45 41 4D 5F 43 41 53 54 45 52 5F 46 58),
000012C4             STR: 'RecallMissionTeam_Test' (16 00 00 00 52 65 63 61 6C 6C 4D 69 73 73 69 6F 6E 54 65 61 6D 5F 54 65 73 74),
000012DF             STR: 'RecallTeamMember_Subject' (18 00 00 00 52 65 63 61 6C 6C 54 65 61 6D 4D 65 6D 62 65 72 5F 53 75 62 6A 65 63 74),
000012FC             STR: 'RECALL_TEAM_FX' (0E 00 00 00 52 45 43 41 4C 4C 5F 54 45 41 4D 5F 46 58),
0000130F             STR: 'DownloadMissionMap_Deactivate' (1D 00 00 00 44 6F 77 6E 6C 6F 61 64 4D 69 73 73 69 6F 6E 4D 61 70 5F 44 65 61 63 74 69 76 61 74 65),
00001331             STR: 'RecallTeamMember_Test' (15 00 00 00 52 65 63 61 6C 6C 54 65 61 6D 4D 65 6D 62 65 72 5F 54 65 73 74),
0000134B             STR: 'RECALL_TEAM_MEMBER_CASTER_FX' (1C 00 00 00 52 45 43 41 4C 4C 5F 54 45 41 4D 5F 4D 45 4D 42 45 52 5F 43 41 53 54 45 52 5F 46 58),
0000136C             STR: 'EngageFoes_DirectObject' (17 00 00 00 45 6E 67 61 67 65 46 6F 65 73 5F 44 69 72 65 63 74 4F 62 6A 65 63 74),
00001388             STR: 'NEGATIVE_COND_2_REMOVE_PERCENTS' (1F 00 00 00 4E 45 47 41 54 49 56 45 5F 43 4F 4E 44 5F 32 5F 52 45 4D 4F 56 45 5F 50 45 52 43 45 4E 54 53),
000013AC             STR: 'obj' (03 00 00 00 6F 62 6A),
000013B4             STR: 'NEGATIVE_COND_TIME' (12 00 00 00 4E 45 47 41 54 49 56 45 5F 43 4F 4E 44 5F 54 49 4D 45),
000013CB             STR: 'traceback' (09 00 00 00 74 72 61 63 65 62 61 63 6B),
000013D9             STR: 'NEGATIVE_COND_3_REMOVE_PERCENTS' (1F 00 00 00 4E 45 47 41 54 49 56 45 5F 43 4F 4E 44 5F 33 5F 52 45 4D 4F 56 45 5F 50 45 52 43 45 4E 54 53),
000013FD             STR: 'mv' (02 00 00 00 6D 76),
00001404             STR: 'Utility' (07 00 00 00 55 74 69 6C 69 74 79)
                 )
             freevars:
00001410         TUPLE: ()
             cellvars:
00001415         TUPLE: ()
             filename:
0000141A         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\ability\\hacker\\misc.py' (4B 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 61 62 69 6C 69 74 79 5C 68 61 63 6B 65 72 5C 6D 69 73 63 2E 70 79)
             name:
0000146A         STR: '?' (01 00 00 00 3F)
             firslineno:
00001470         LONG: 5L (05 00 00 00)
             lnotab:
00001474         STR: '\t\x01\t\x01\t\x03\t\x01\t\x01\x0c\x01\t\x01\t\x03\x07\t\x06\x0b\x06\x01\x06\x01\x06\x06\t\x01\t\x02\t\x01\t\x06\t\x16\t\t\t\n\t\x07\t\t\t\x04\t\x06\t\x0b' (32 00 00 00 09 01 09 01 09 03 09 01 09 01 0C 01 09 01 09 03 07 09 06 0B 06 01 06 01 06 06 09 01 09 02 09 01 09 06 09 16 09 09 09 0A 09 07 09 09 09 04 09 06 09 0B)

